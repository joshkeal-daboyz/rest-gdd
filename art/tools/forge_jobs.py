"""Concept-art pipeline: every change to an image is a Forge job, explained and approved before it runs.

Rules this script enforces:
  * Images are only ever made or changed by Forge (txt2img, img2img, inpaint, Forge's upscaler).
    The script never edits pixels. It only adds a text note (the job id) to each PNG Forge returns.
  * Before Josh can approve a job, it must be explained (`explain`), reviewed independently by the
    forge-prompt-reviewer agent (`brief`, then the agent writes prompt-review.md), and answered by
    Claude (`respond agree|disagree`). A disagreement goes to Josh. Approval (`approve`) comes only from
    Josh: he replies in chat and Claude records his exact words with --chat, or he types it at a
    terminal. Editing the job, its parent image or its mask cancels every step after it.
  * Small jobs come first. A large job (more than SMALL_MAX images, hires fix, or an upscale) only runs
    if it follows a small job on the same asset and track that Josh gave an "on-track" verdict.

Jobs live in art/jobs/<id>/: job.json (what to do), explain.md, state.json, out/ (Forge's images).

usage (run from the repo root with `py art/tools/forge_jobs.py ...`):
  new <asset> <track> <slug> [--from JOB]   make a job skeleton to fill in
  explain <job>                             check the job and write a plain-English explanation
  brief <job>                               write prompt-brief.md for the forge-prompt-reviewer agent
  respond <job> agree|disagree "note"       Claude's answer to the reviewer (disagree = talk to Josh)
  approve <job> [--chat "Josh's words"]     record Josh's approval (from chat, or typed at a terminal)
  run <job>                                 send an approved job to Forge
  verdict <job> on-track|off-track [note]   Josh: is a small job heading the right way?
  status <image.png> exploration|candidate|locked|rejected [note]
  list                                      every job and where it stands
  catalog                                   write art/catalog.json (every image, its job, Forge settings, status)
  gallery                                   write art/gallery.html to compare images side by side
"""
import argparse, base64, datetime, hashlib, html, json, math, pathlib, struct, sys, urllib.request, zlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ART = ROOT / "art"
JOBS = ART / "jobs"
STATUS_FILE = ART / "asset-status.json"
FORGE = "http://127.0.0.1:7860"

SMALL_MAX = 4          # a small job makes at most this many images, with no hires fix and no upscale
HARD_MAX = 32          # no job makes more than this
MODES = ("txt2img", "img2img", "inpaint", "upscale")
KINDS = ("character-sheet", "single-character", "prop", "other")  # what the job's image is
STATUSES = ("exploration", "candidate", "locked", "rejected")
JOB_KEYS = {"asset", "track", "kind", "goal", "why", "mode", "parent", "mask", "prompt", "negative", "model", "loras",
            "settings", "count", "hires", "controlnet", "upscale", "follows", "compare_to"}
PROMPT_ORDER = ["style", "identity", "build", "posture", "face", "colors", "feet", "tail", "base_body"]


# ---------- small helpers ----------

def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def rel(p):
    return pathlib.Path(p).resolve().relative_to(ROOT).as_posix()


def die(msg):
    sys.exit(f"stopped: {msg}")


def read_json(p, default=None):
    p = pathlib.Path(p)
    return json.loads(p.read_text(encoding="utf-8-sig")) if p.exists() else default


def write_json(p, data):
    pathlib.Path(p).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def job_dir(job_id):
    d = JOBS / job_id
    if not (d / "job.json").exists():
        die(f"no job called {job_id} (looked in {rel(d)})")
    return d


def load_job(job_id):
    return read_json(job_dir(job_id) / "job.json")


def load_state(job_id):
    return read_json(JOBS / job_id / "state.json", {})


def save_state(job_id, state):
    write_json(JOBS / job_id / "state.json", state)


def job_hash(job_id, job):
    """Fingerprint of the job and every file it reads, so any change after approval is caught."""
    h = hashlib.sha256(json.dumps(job, sort_keys=True).encode())
    for f in input_files(job):
        h.update(f.encode()); h.update((ROOT / f).read_bytes())
    return h.hexdigest()[:16]


def input_files(job):
    files = [job[k] for k in ("parent", "mask") if job.get(k)]
    p = job.get("prompt")
    if isinstance(p, dict) and p.get("from"):
        files.append(p["from"])
    files += [c["image"] for c in job.get("controlnet", []) if c.get("image")]
    return files


# ---------- PNG text chunks (metadata only, the pixels are never touched) ----------

def png_text(path):
    out = {}
    with open(path, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            return out
        while True:
            head = f.read(8)
            if len(head) < 8:
                break
            n, kind = struct.unpack(">I4s", head)
            if kind in (b"tEXt", b"iTXt", b"zTXt"):
                data = f.read(n); f.seek(4, 1)
                try:
                    key, rest = data.split(b"\0", 1)
                    if kind == b"tEXt":
                        val = rest.decode("latin-1")
                    elif kind == b"zTXt":
                        val = zlib.decompress(rest[1:]).decode("latin-1")
                    else:
                        comp, _method, rest = rest[0], rest[1], rest[2:]
                        _lang, _tkey, text = rest.split(b"\0", 2)
                        val = (zlib.decompress(text) if comp else text).decode("utf-8")
                    out[key.decode("latin-1")] = val
                except Exception:
                    pass
            elif kind == b"IEND":
                break
            else:
                f.seek(n + 4, 1)
    return out


def add_png_text(png_bytes, notes):
    """Insert iTXt chunks before IEND. Image data is copied byte for byte."""
    end = png_bytes.rfind(b"IEND") - 4
    chunks = b""
    for key, val in notes.items():
        body = key.encode("latin-1") + b"\0\0\0\0\0" + val.encode("utf-8")
        chunks += struct.pack(">I", len(body)) + b"iTXt" + body + struct.pack(">I", zlib.crc32(b"iTXt" + body))
    return png_bytes[:end] + chunks + png_bytes[end:]


def png_size(path):
    with open(path, "rb") as f:
        f.seek(16)
        return struct.unpack(">II", f.read(8))


def parse_infotext(text):
    """Forge's 'parameters' note -> prompt, negative and the settings line as a dict."""
    if not text:
        return {}
    lines = text.strip().split("\n")
    settings_line = lines[-1] if "Steps:" in lines[-1] else ""
    body = lines[:-1] if settings_line else lines
    prompt, neg, in_neg = [], [], False
    for ln in body:
        if ln.startswith("Negative prompt:"):
            in_neg = True; ln = ln[len("Negative prompt:"):].strip()
        (neg if in_neg else prompt).append(ln)
    out = {"prompt": "\n".join(prompt).strip(), "negative": "\n".join(neg).strip()}
    for part in settings_line.split(", "):
        if ": " in part:
            k, v = part.split(": ", 1); out[k.strip()] = v.strip()
    return out


# ---------- building the request ----------

def prompt_parts(job):
    """Returns (prompt, negative, default settings)."""
    p, defaults = job["prompt"], {}
    if isinstance(p, dict):
        src = read_json(ROOT / p["from"])
        pieces = ([src["views"][p["view"]]] if p.get("view") else []) + [src[k] for k in PROMPT_ORDER if src.get(k)]
        if p.get("extra"):
            pieces.append(p["extra"])
        prompt, neg, defaults = ", ".join(pieces), src.get("negative", ""), src.get("settings", {})
    else:
        prompt, neg = p, ""
    if job.get("negative") is not None:
        neg = job["negative"]
    prompt += "".join(f", <lora:{l}>" for l in job.get("loras", []))
    return prompt, neg, defaults


def tier(job):
    big = job.get("count", 1) > SMALL_MAX or job.get("hires") or job["mode"] == "upscale"
    return "large" if big else "small"


def base_name(name):
    """'x.safetensors [hash]' and 'x' are the same model."""
    name = str(name).split(" [")[0].strip()
    for ext in (".safetensors", ".ckpt", ".pt", ".pth", ".bin"):
        if name.lower().endswith(ext):
            name = name[:-len(ext)]
    return name.replace("\\", "/").rsplit("/", 1)[-1]


_installed = None


def forge_installed():
    """What Forge has installed right now: {"checkpoints", "loras", "controlnet"} as sets of base names."""
    global _installed
    if _installed is None:
        get = lambda path: json.load(urllib.request.urlopen(f"{FORGE}{path}", timeout=10))
        try:
            _installed = {
                "checkpoints": {base_name(m["title"]) for m in get("/sdapi/v1/sd-models")},
                "loras": {base_name(l["name"]) for l in get("/sdapi/v1/loras")},
                "controlnet": {base_name(m) for m in get("/controlnet/model_list")["model_list"] if m != "None"}}
        except Exception as e:
            die(f"can't reach Forge at {FORGE} to check its installed models ({e}). Start Forge and try again.")
    return _installed


def approved():
    return read_json(ROOT / "art/tools/forge-approved.json")


def model_errors(job):
    """The job may only use the approved checkpoint, LoRAs and ControlNet models, and only ones Forge has."""
    ok, have, errs = approved(), forge_installed(), []
    ok_ckpt = {base_name(n) for n in ok["checkpoints"]}
    ok_lora = {base_name(n): v for n, v in ok["loras"].items()}
    ok_cn = {base_name(n) for n in ok["controlnet"]}

    def need(label, key, name, allowed):
        if name not in allowed:
            errs.append(f"{label} '{name}' isn't on the approved list (art/tools/forge-approved.json); only Josh adds to it")
        elif name not in have[key]:
            errs.append(f"{label} '{name}' is approved but Forge doesn't have it installed")

    if job["mode"] != "upscale":
        if not job.get("model"):
            errs.append(f"set 'model' (the approved one is {', '.join(ok['checkpoints'])}); otherwise Forge uses whatever is loaded")
        else:
            need("model", "checkpoints", base_name(job["model"]), ok_ckpt)
        prompt = prompt_parts(job)[0]
        used = {base_name(t.split(":")[0]) for t in
                (seg.split(">")[0] for seg in prompt.split("<lora:")[1:])}
        for name in sorted(used):
            need("LoRA", "loras", name, ok_lora)
            only = ok_lora.get(name, {}).get("only_for")
            if only and job.get("kind") != only:
                errs.append(f"LoRA '{name}' is only for {only} jobs, and this job's kind is '{job.get('kind')}'")
            if name in ok_lora and ok_lora[name].get("trigger") and ok_lora[name]["trigger"] not in prompt.replace(f"<lora:{name}", ""):
                errs.append(f"LoRA '{name}' needs its trigger word '{ok_lora[name]['trigger']}' in the prompt")
    for c in job.get("controlnet", []):
        need("ControlNet model", "controlnet", base_name(c.get("model", "")), ok_cn)
    return errs


def check(job_id, job):
    """Everything that must be true before a job can be explained, approved or run."""
    errs = []
    unknown = set(job) - JOB_KEYS
    if unknown:
        errs.append(f"unknown fields {sorted(unknown)} (typo?)")
    for k in ("asset", "track", "goal", "why", "mode"):
        if not str(job.get(k, "")).strip() or str(job.get(k, "")).startswith("TODO"):
            errs.append(f"'{k}' must be filled in")
    if job.get("kind") not in KINDS:
        errs.append(f"'kind' must be one of {KINDS}")
    mode = job.get("mode")
    if mode not in MODES:
        errs.append(f"mode must be one of {MODES}")
    if mode != "upscale" and not job.get("prompt"):
        errs.append("needs a prompt")
    if mode in ("img2img", "inpaint", "upscale") and not job.get("parent"):
        errs.append(f"{mode} needs a parent image")
    if mode == "inpaint" and not job.get("mask"):
        errs.append("inpaint needs a mask image (white = area Forge may redraw)")
    if mode in ("img2img", "inpaint") and "denoising_strength" not in job.get("settings", {}):
        errs.append(f"{mode} needs settings.denoising_strength")
    for f in input_files(job):
        if not (ROOT / f).exists():
            errs.append(f"file not found: {f}")
    count = job.get("count", 1)
    if not isinstance(count, int) or not 1 <= count <= HARD_MAX:
        errs.append(f"count must be 1 to {HARD_MAX}")
    if mode in MODES and tier(job) == "large":
        f = job.get("follows")
        if not f:
            errs.append(f"this is a large job, so it must 'follow' a small job on track '{job.get('track')}' with an on-track verdict")
        elif not (JOBS / f / "job.json").exists():
            errs.append(f"follows {f}, which doesn't exist")
        else:
            fj, fs = load_job(f), load_state(f)
            if (fj["asset"], fj["track"]) != (job.get("asset"), job.get("track")):
                errs.append(f"follows {f}, which is on a different asset or track")
            if fs.get("verdict") != "on-track":
                errs.append(f"follows {f}, which doesn't have an on-track verdict (it has: {fs.get('verdict', 'none')})")
    if mode in MODES:
        errs += model_errors(job)
    if errs:
        die(f"job {job_id} isn't ready:\n  - " + "\n  - ".join(errs))


def previous_job(job):
    """The job to compare the prompt against: compare_to, follows, or the job that made the parent image."""
    for k in ("compare_to", "follows"):
        if job.get(k):
            return job[k]
    if job.get("parent"):
        return png_text(ROOT / job["parent"]).get("forge_job")
    return None


def fragments(prompt):
    return [s.strip() for s in prompt.replace("\n", ",").split(",") if s.strip()]


def denoise_words(d):
    if d < 0.3:
        return "a light touch-up: shapes and colours stay, small details change"
    if d < 0.55:
        return "a moderate change: pose and layout stay, details, colours and line can change"
    if d < 0.8:
        return "a heavy redraw: only the rough layout carries over"
    return "close to a fresh image: very little of the parent survives"


def explain_text(job_id, job):
    prompt, neg, defaults = prompt_parts(job)
    s = {**defaults, **job.get("settings", {})}
    mode, count = job["mode"], job.get("count", 1)
    L = [f"# Forge job {job_id}", "",
         f"**Asset:** {job['asset']} | **Track:** {job['track']} | **Kind:** {job['kind']} | **Size:** {tier(job)} ({count} image{'s' * (count > 1)})", "",
         "## What we're trying to change", job["goal"], "",
         "## Why this job should do it", job["why"], "",
         "## What Forge will do"]
    if mode == "txt2img":
        L.append(f"Draw {count} new image(s) from the prompt, starting from noise.")
    elif mode == "img2img":
        d = s["denoising_strength"]
        L.append(f"Redraw `{job['parent']}` {count} time(s). Denoise {d}: {denoise_words(d)}.")
    elif mode == "inpaint":
        d = s["denoising_strength"]
        L.append(f"Redraw only the white area of `{job['mask']}` on `{job['parent']}`, {count} time(s). "
                 f"Everything outside the mask is kept. Denoise {d}: {denoise_words(d)}.")
    else:
        u = job.get("upscale", {})
        L.append(f"Enlarge `{job['parent']}` {u.get('scale', 2)}x with Forge's {u.get('upscaler', 'R-ESRGAN 4x+ Anime6B')} "
                 "upscaler. Nothing is redrawn.")
    if job.get("hires"):
        L.append(f"Hires fix on: a second pass at {job['hires']}x size so detail is drawn, not just enlarged "
                 f"(denoise {s.get('hr_denoise', 0.35)}).")
    for c in job.get("controlnet", []):
        L.append(f"ControlNet `{c.get('module')}` / `{c.get('model')}` at weight {c.get('weight', 1)}, using "
                 f"`{c.get('image', 'the parent')}`. {c.get('purpose', '')}".rstrip())
    if mode != "upscale":
        own = job.get("settings", {})
        if mode == "txt2img":
            size = f"{s.get('width', '?')}x{s.get('height', '?')}"
        elif "width" in own:
            crop = s.get("inpaint_full_res") and mode == "inpaint"
            size = f"{own['width']}x{own.get('height', '?')}" + (" (the masked area is drawn at this size)" if crop else "")
        else:
            size = "parent's size"
        seed = s.get("seed", -1)
        L += ["", "## Settings",
              f"- Model: `{job.get('model') or 'whatever Forge has loaded now'}`",
              f"- LoRAs: {lora_words(job) or 'none'}",
              f"- {s.get('steps', '?')} steps, CFG {s.get('cfg_scale', '?')}, sampler {s.get('sampler_name', '?')}, size {size}",
              f"- Seed: {'random (the seeds used are saved with each image)' if seed == -1 else f'{seed}, counting up per image'}"]
        prev = previous_job(job)
        L += ["", "## Prompt"]
        if prev and (JOBS / prev / "job.json").exists():
            old = fragments(prompt_parts(load_job(prev))[0]); new = fragments(prompt)
            added = [f for f in new if f not in old]; removed = [f for f in old if f not in new]
            L.append(f"Compared with job `{prev}`:")
            L += [f"- added: `{f}`" for f in added] + [f"- removed: `{f}`" for f in removed]
            if not added and not removed:
                L.append("- no change to the prompt")
        L += ["", "```", prompt, "```", "", "Negative:", "```", neg or "(none)", "```"]
    if tier(job) == "large":
        L += ["", "## Why a large job is allowed now",
              f"It follows `{job['follows']}`, which Josh gave an on-track verdict: "
              f"{load_state(job['follows']).get('verdict_note') or '(no note)'}"]
    L += ["", "## Output", f"Images go to `art/jobs/{job_id}/out/` exactly as Forge returns them. "
          "Nothing is edited afterwards; only the job id is written into each file's PNG notes."]
    return "\n".join(L) + "\n"


def lora_words(job):
    ok = {base_name(n): v for n, v in approved()["loras"].items()}
    out = []
    for l in job.get("loras", []):
        name, _, w = l.partition(":")
        a = ok.get(base_name(name), {})
        note = f" (approved weight {a['weight']}, trigger `{a.get('trigger')}`)" if a.get("weight") is not None else ""
        out.append(f"`{l}`{note}")
    return ", ".join(out)


def build_request(job):
    prompt, neg, defaults = prompt_parts(job)
    s = {**defaults, **job.get("settings", {})}
    mode, count = job["mode"], job.get("count", 1)
    if mode == "upscale":
        u = job.get("upscale", {})
        return "extra-single-image", {"image": b64(job["parent"]), "resize_mode": 0,
                                      "upscaling_resize": u.get("scale", 2),
                                      "upscaler_1": u.get("upscaler", "R-ESRGAN 4x+ Anime6B")}
    per = 2 if count > 1 else 1
    payload = {"prompt": prompt, "negative_prompt": neg, "batch_size": per, "n_iter": math.ceil(count / per),
               "seed": s.pop("seed", -1), **{k: v for k, v in s.items() if k != "hr_denoise"}}
    if job.get("model"):
        payload["override_settings"] = {"sd_model_checkpoint": job["model"]}
        payload["override_settings_restore_afterwards"] = False
    if job.get("hires"):
        payload.update({"enable_hr": True, "hr_scale": job["hires"], "hr_upscaler": "R-ESRGAN 4x+ Anime6B",
                        "denoising_strength": s.get("hr_denoise", 0.35), "hr_second_pass_steps": 15,
                        "hr_additional_modules": ["Use same choices"]})  # Forge errors without this
    if job.get("controlnet"):
        args = []
        for c in job["controlnet"]:
            a = {"enabled": True, "resize_mode": "Crop and Resize", "pixel_perfect": True,
                 "control_mode": "Balanced", **{k: v for k, v in c.items() if k not in ("image", "purpose")}}
            if c.get("image"):
                a["image"] = b64(c["image"])
            args.append(a)
        payload["alwayson_scripts"] = {"ControlNet": {"args": args}}
    if mode == "txt2img":
        return "txt2img", payload
    w, h = png_size(ROOT / job["parent"])
    own = job.get("settings", {})  # only the job's own size counts here, not the prompt file's txt2img size
    payload.update({"init_images": [b64(job["parent"])], "width": own.get("width", w // 8 * 8),
                    "height": own.get("height", h // 8 * 8), "resize_mode": 0})
    if mode == "inpaint":
        payload.update({"mask": b64(job["mask"]), "inpainting_fill": s.get("inpainting_fill", 1),
                        "mask_blur": s.get("mask_blur", 4), "inpaint_full_res": s.get("inpaint_full_res", False)})
    return "img2img", payload


def b64(path):
    return base64.b64encode((ROOT / path).read_bytes()).decode()


def forge(endpoint, payload):
    req = urllib.request.Request(f"{FORGE}/sdapi/v1/{endpoint}", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=3600))


# ---------- commands ----------

def cmd_new(a):
    JOBS.mkdir(parents=True, exist_ok=True)
    n = 1 + max([int(d.name.split("-")[1]) for d in JOBS.iterdir()
                 if d.is_dir() and d.name.startswith(a.asset + "-") and d.name.split("-")[1].isdigit()] or [0])
    job_id = f"{a.asset}-{n:03d}-{a.slug}"
    if a.__dict__.get("from"):
        job = load_job(a.__dict__["from"])
        job.update(goal="TODO", why="TODO", compare_to=a.__dict__["from"]); job.pop("follows", None)
    else:
        job = {"mode": "txt2img",
               "prompt": {"from": "art/enoch-sheet/enoch-prompts.json", "view": "front", "extra": ""},
               "model": next(iter(approved()["checkpoints"])), "loras": [], "settings": {"seed": -1},
               "count": 4, "kind": "TODO", "goal": "TODO", "why": "TODO"}
    job.update(asset=a.asset, track=a.track)
    (JOBS / job_id).mkdir()
    write_json(JOBS / job_id / "job.json", job)
    print(f"made {rel(JOBS / job_id / 'job.json')}; fill in goal, why and the settings, then: explain {job_id}")


def cmd_explain(a):
    job = load_job(a.job); check(a.job, job)
    text = explain_text(a.job, job)
    (JOBS / a.job / "explain.md").write_text(text, encoding="utf-8")
    st = load_state(a.job)
    st.update(explained_at=now(), explained_hash=job_hash(a.job, job))
    st.pop("approved_hash", None); st.pop("approved_at", None)
    save_state(a.job, st)
    print(text)
    if needs_prompt_review(job):
        print(f"--- next: py art/tools/forge_jobs.py brief {a.job}   (then the forge-prompt-reviewer agent)")
    else:
        print(f"--- no prompt to review; ask Josh to approve in chat; then: approve {a.job} --chat \"<his exact words>\"")


def needs_prompt_review(job):
    return job["mode"] != "upscale"


def rule_files(job):
    files = ["art/raccoon-style-guide.md"]
    files += [rel(f) for f in sorted(ART.rglob(f"{job['asset']}-rules.md"))]
    return files


def reference_images():
    return ["art/female-raccoon/baseline-highres.png", "art/enoch-sheet/enoch_character_sheet.png"]


def track_history(job_id, job):
    rows = []
    for j in all_jobs():
        if j == job_id:
            continue
        oj, ost = load_job(j), load_state(j)
        if (oj.get("asset"), oj.get("track")) == (job["asset"], job["track"]):
            rows.append((j, oj, ost, read_review(j)))
    return rows


def read_review(job_id):
    """The reviewer's file as {job-hash, assessment, text}, or {}."""
    f = JOBS / job_id / "prompt-review.md"
    if not f.exists():
        return {}
    text = f.read_text(encoding="utf-8")
    head = {}
    for ln in text.splitlines()[:5]:
        if ":" in ln:
            k, v = ln.split(":", 1)
            head[k.strip().lower()] = v.strip()
    head["text"] = text
    return head


def cmd_brief(a):
    job = load_job(a.job); check(a.job, job); st = load_state(a.job)
    h = job_hash(a.job, job)
    if st.get("explained_hash") != h:
        die("the job changed since it was last explained (or was never explained); run explain first")
    if not needs_prompt_review(job):
        die("an upscale has no prompt to review; Josh can approve it directly")
    imgs = [f"- parent: `{job['parent']}`"] if job.get("parent") else []
    imgs += [f"- mask (white = redrawn): `{job['mask']}`"] if job.get("mask") else []
    imgs += [f"- ControlNet image: `{c['image']}`" for c in job.get("controlnet", []) if c.get("image")]
    imgs += [f"- reference: `{r}`" for r in reference_images()]
    hist = []
    for j, oj, ost, rv in track_history(a.job, job):
        imgs += [f"- earlier output of `{j}`: `{o}`" for o in ost.get("outputs", [])[:4]]
        note = f": {ost['verdict_note']}" if ost.get("verdict_note") else ""
        hist.append(f"- `{j}`: goal \"{oj.get('goal', '')}\"; reviewer said {rv.get('assessment', 'n/a')}; "
                    f"Josh's verdict {ost.get('verdict', 'not run')}{note}")
    text = "\n".join([
        f"job: {a.job}", f"job-hash: {h}", "",
        "# Reason for the change", "",
        f"**What we're trying to change:** {job['goal']}", "",
        f"**Why this job should do it:** {job['why']}", "",
        "Judge the job against this reason.", "",
        "# Rules to check", *[f"- `{r}`" for r in rule_files(job)], "",
        "# Images to look at", *imgs, "",
        "# Earlier jobs on this track", *(hist or ["- none"]), "",
        "# The job, explained", "",
        (JOBS / a.job / "explain.md").read_text(encoding="utf-8")])
    (JOBS / a.job / "prompt-brief.md").write_text(text, encoding="utf-8")
    st.update(briefed_hash=h, briefed_at=now()); save_state(a.job, st)
    print(f"wrote {rel(JOBS / a.job / 'prompt-brief.md')}")
    print(f"--- next: give job id {a.job} to the forge-prompt-reviewer agent; it writes prompt-review.md")


def current_review(job_id, job):
    rv = read_review(job_id)
    return rv if rv.get("job-hash") == job_hash(job_id, job) else {}


def cmd_respond(a):
    job = load_job(a.job); st = load_state(a.job)
    rv = current_review(a.job, job)
    if not rv:
        die("no prompt review for the job as it stands now; brief it and ask the forge-prompt-reviewer agent")
    if not a.note.strip():
        die("say why you agree or disagree")
    st.update(response=a.response, response_note=a.note, response_hash=rv["job-hash"], responded_at=now())
    save_state(a.job, st)
    print(f"reviewer: {rv.get('assessment')}  |  Claude: {a.response}")
    if a.response == "disagree":
        print("--- DISAGREEMENT: talk it through with Josh before he approves.")
    else:
        print(f"--- ask Josh to approve in chat; then: approve {a.job} --chat \"<his exact words>\"")


def cmd_approve(a):
    job = load_job(a.job); check(a.job, job); st = load_state(a.job)
    if st.get("explained_hash") != job_hash(a.job, job):
        die("the job changed since it was last explained (or was never explained); run explain first")
    if needs_prompt_review(job):
        rv = current_review(a.job, job)
        if not rv:
            die("the forge-prompt-reviewer agent hasn't reviewed the job as it stands now")
        if st.get("response_hash") != rv["job-hash"]:
            die("Claude hasn't responded to the prompt review yet (respond agree|disagree)")
    if a.chat is not None:
        # Josh approved in chat; Claude records his exact words. Only ever from Josh's own message.
        if not a.chat.strip():
            die("--chat needs Josh's exact words of approval")
        st.update(approved_at=now(), approved_hash=st["explained_hash"], approved_via="chat",
                  approval_words=a.chat.strip()); save_state(a.job, st)
        print(f"approved in chat by Josh: \"{a.chat.strip()}\". Run it with:  py art/tools/forge_jobs.py run {a.job}")
        return
    if not real_console():
        die("approve needs Josh: either typed at a terminal, or --chat \"<his exact words>\" after he approves in chat")
    print((JOBS / a.job / "explain.md").read_text(encoding="utf-8"))
    if needs_prompt_review(job):
        print("\n========== independent prompt review ==========\n")
        print(rv["text"])
        print(f"\n========== Claude's response: {st['response'].upper()} ==========\n{st['response_note']}\n")
        if st["response"] == "disagree":
            print("!! Claude and the reviewer disagree. Settle it before approving.\n")
    try:
        typed = input(f"Type the job id to approve it ({a.job}): ").strip()
    except EOFError:
        typed = ""
    if typed != a.job:
        die("not approved")
    st.update(approved_at=now(), approved_hash=st["explained_hash"], approved_via="terminal"); save_state(a.job, st)
    print(f"approved. Run it with:  py art/tools/forge_jobs.py run {a.job}")


def real_console():
    """True only for a keyboard at a console window (on Windows, the NUL device also counts as a tty)."""
    if not sys.stdin.isatty():
        return False
    if sys.platform != "win32":
        return True
    import ctypes, msvcrt
    mode = ctypes.c_uint32()
    return bool(ctypes.windll.kernel32.GetConsoleMode(msvcrt.get_osfhandle(sys.stdin.fileno()), ctypes.byref(mode)))


def cmd_run(a):
    job = load_job(a.job); check(a.job, job); st = load_state(a.job)
    if not st.get("approved_hash"):
        die("not approved yet")
    if st["approved_hash"] != job_hash(a.job, job):
        die("the job or one of its files changed after approval; explain and approve again")
    if st.get("ran_at") and not a.again:
        die(f"already ran at {st['ran_at']}; make a new job, or pass --again to repeat it")
    endpoint, payload = build_request(job)
    print(f"sending {a.job} to Forge ({endpoint}, {job.get('count', 1)} image(s))...")
    res = forge(endpoint, payload)
    out = JOBS / a.job / "out"; out.mkdir(exist_ok=True)
    if endpoint == "extra-single-image":
        images, infos, seeds = [res["image"]], [res.get("html_info", "")], ["up"]
    else:
        info = json.loads(res.get("info", "{}"))
        images = res["images"][:job.get("count", 1)]
        infos, seeds = info.get("infotexts", []), info.get("all_seeds", [])
    saved = []
    for i, data in enumerate(images):
        raw = base64.b64decode(data)
        notes = {"forge_job": a.job}
        if i < len(infos) and "parameters" not in png_text_bytes(raw):
            notes["parameters"] = infos[i]
        f = out / f"{job['asset']}_{seeds[i] if i < len(seeds) else i}.png"
        f.write_bytes(add_png_text(raw, notes)); saved.append(rel(f)); print(" ", rel(f))
    st.update(ran_at=now(), outputs=saved); save_state(a.job, st)
    if tier(job) == "small":
        print(f"look at them, then:  py art/tools/forge_jobs.py verdict {a.job} on-track|off-track \"what you saw\"")


def png_text_bytes(raw):
    import tempfile, os
    fd, tmp = tempfile.mkstemp(suffix=".png"); os.write(fd, raw); os.close(fd)
    try:
        return png_text(tmp)
    finally:
        os.remove(tmp)


def cmd_verdict(a):
    load_job(a.job); st = load_state(a.job)
    if not st.get("ran_at"):
        die("the job hasn't run yet")
    st.update(verdict=a.verdict, verdict_note=a.note, reviewed_at=now()); save_state(a.job, st)
    print(f"{a.job}: {a.verdict}")


def cmd_status(a):
    p = pathlib.Path(a.image)
    p = p if p.is_absolute() else (pathlib.Path.cwd() / p)
    if not p.exists():
        die(f"no image at {a.image}")
    reg = read_json(STATUS_FILE, {})
    reg[rel(p)] = {"status": a.status, "note": a.note, "at": now()}
    write_json(STATUS_FILE, dict(sorted(reg.items())))
    print(f"{rel(p)}: {a.status}")


def all_jobs():
    return sorted(d.name for d in JOBS.iterdir() if (d / "job.json").exists()) if JOBS.exists() else []


def stage(job_id):
    st, job = load_state(job_id), load_job(job_id)
    h = job_hash(job_id, job) if all((ROOT / f).exists() for f in input_files(job)) else None
    if st.get("ran_at"):
        return f"ran, verdict: {st.get('verdict', 'not given')}"
    if st.get("approved_hash") == h:
        return "approved, ready to run"
    if st.get("explained_hash") == h:
        if not needs_prompt_review(job):
            return "explained, waiting for approval"
        rv = read_review(job_id)
        if rv.get("job-hash") != h:
            return "explained, needs prompt review"
        if st.get("response_hash") != h:
            return f"reviewed ({rv.get('assessment')}), needs response"
        return f"reviewed, Claude {st['response']}s; waiting for Josh"
    return "draft (needs explain)"


def cmd_list(a):
    for j in all_jobs():
        job = load_job(j)
        print(f"{j:34} {tier(job):5}  {stage(j):44} {job.get('goal', '')[:50]}")


def cmd_catalog(a=None):
    reg = read_json(STATUS_FILE, {})
    images = []
    for p in sorted(ART.rglob("*.png")):
        r = rel(p); notes = png_text(p)
        job = notes.get("forge_job")
        if not job and r.startswith("art/jobs/"):
            job = r.split("/")[2]
        params = parse_infotext(notes.get("parameters"))
        images.append({"path": r, "folder": r.rsplit("/", 1)[0], "job": job,
                       "status": reg.get(r, {}).get("status", "exploration"), "status_note": reg.get(r, {}).get("note", ""),
                       "bytes": p.stat().st_size,
                       "modified": datetime.datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds"),
                       "model": params.get("Model"), "seed": params.get("Seed"), "prompt": params.get("prompt")})
    jobs = {}
    for j in all_jobs():
        job, st = load_job(j), load_state(j)
        jobs[j] = {"asset": job.get("asset"), "track": job.get("track"), "goal": job.get("goal"), "why": job.get("why"),
                   "mode": job.get("mode"), "tier": tier(job), "stage": stage(j),
                   "verdict_note": st.get("verdict_note", "")}
    cat = {"made": now(), "jobs": jobs, "images": images}
    write_json(ART / "catalog.json", cat)
    known = sum(1 for i in images if i["job"] or i["seed"])
    print(f"art/catalog.json: {len(images)} images, {len(jobs)} jobs, {known} with a recorded source")
    return cat


def cmd_gallery(a):
    cat = cmd_catalog()
    groups = {}
    for im in cat["images"]:
        key = f"job:{im['job']}" if im["job"] else im["folder"]
        groups.setdefault(key, []).append(im)
    order = sorted(groups, key=lambda k: (not k.startswith("job:"), k))
    E = html.escape
    parts = []
    for k in order:
        head = ""
        if k.startswith("job:") and k[4:] in cat["jobs"]:
            j = cat["jobs"][k[4:]]
            head = (f"<p class=meta>{E(j['asset'])} | {E(j['track'])} | {E(j['tier'])} | {E(j['stage'])}</p>"
                    f"<p><b>Goal:</b> {E(j['goal'] or '')}</p>"
                    + (f"<p><b>Review:</b> {E(j['verdict_note'])}</p>" if j["verdict_note"] else ""))
        cards = []
        for im in groups[k]:
            src = pathlib.PurePosixPath(im["path"]).relative_to("art").as_posix()
            tip = E(f"seed {im['seed']} | {im['model']}\n{im['prompt'] or ''}" if im["seed"] else "no Forge settings recorded")
            cards.append(f"<figure data-status={im['status']} data-text=\"{E(im['path'].lower())}\">"
                         f"<a href=\"{E(src)}\" target=_blank><img loading=lazy src=\"{E(src)}\" title=\"{tip}\"></a>"
                         f"<figcaption><span class=\"b {im['status']}\">{im['status']}</span> {E(src.rsplit('/', 1)[-1])}"
                         f"<code>{E(im['path'])}</code></figcaption></figure>")
        parts.append(f"<section data-text=\"{E(k.lower())}\"><h2>{E(k[4:] if k.startswith('job:') else k)}</h2>{head}"
                     f"<div class=grid>{''.join(cards)}</div></section>")
    page = GALLERY.replace("%BODY%", "\n".join(parts)).replace("%MADE%", E(cat["made"])).replace(
        "%COUNT%", str(len(cat["images"])))
    (ART / "gallery.html").write_text(page, encoding="utf-8")
    print("art/gallery.html")


GALLERY = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Concept Art Gallery</title><style>
:root{--bg:#f7f5ef;--fg:#1d2430;--muted:#6b7280;--card:#fff;--line:#e3e0d8}
@media (prefers-color-scheme:dark){:root{--bg:#15181d;--fg:#e6e8eb;--muted:#9aa1ab;--card:#1e2229;--line:#2c313a}}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,sans-serif}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 16px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;z-index:1}
header h1{font-size:16px;margin:0 12px 0 0}input,select{font:inherit;padding:4px 8px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg)}
main{padding:0 16px 40px}section{margin-top:24px}h2{font-size:15px;margin:0 0 4px}p{margin:2px 0;max-width:80ch}.meta{color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(var(--w,220px),1fr));gap:10px;margin-top:8px}
figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden}
img{width:100%;aspect-ratio:3/2;object-fit:contain;background:#fff;display:block}
figcaption{padding:6px 8px;font-size:12px;word-break:break-all}code{display:none}
.b{display:inline-block;padding:0 6px;border-radius:9px;font-size:11px;color:#fff;background:#8a8f98}
.candidate{background:#b7791f}.locked{background:#2f855a}.rejected{background:#c53030}
</style></head><body><header><h1>Concept art</h1><span class=meta>%COUNT% images | made %MADE%</span>
<input id=q placeholder="filter by path or job"><select id=s><option value="">all statuses</option><option>exploration</option>
<option>candidate</option><option>locked</option><option>rejected</option></select>
<label class=meta>size <input id=z type=range min=120 max=600 value=220></label></header><main>%BODY%</main>
<script>
const q=document.getElementById('q'),s=document.getElementById('s'),z=document.getElementById('z');
function f(){const t=q.value.toLowerCase(),st=s.value;document.querySelectorAll('section').forEach(sec=>{let n=0;
const hit=sec.dataset.text.includes(t);sec.querySelectorAll('figure').forEach(fi=>{const ok=(hit||fi.dataset.text.includes(t))&&(!st||fi.dataset.status===st);
fi.hidden=!ok;n+=ok});sec.hidden=!n})}
q.oninput=f;s.onchange=f;z.oninput=()=>document.body.style.setProperty('--w',z.value+'px');
</script></body></html>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new"); p.add_argument("asset"); p.add_argument("track"); p.add_argument("slug")
    p.add_argument("--from", help="copy settings from this job")
    for name in ("explain", "brief"):
        sub.add_parser(name).add_argument("job")
    p = sub.add_parser("approve"); p.add_argument("job")
    p.add_argument("--chat", help="Josh's exact words when he approved in chat")
    p = sub.add_parser("respond"); p.add_argument("job"); p.add_argument("response", choices=["agree", "disagree"])
    p.add_argument("note")
    p = sub.add_parser("run"); p.add_argument("job"); p.add_argument("--again", action="store_true")
    p = sub.add_parser("verdict"); p.add_argument("job"); p.add_argument("verdict", choices=["on-track", "off-track"])
    p.add_argument("note", nargs="?", default="")
    p = sub.add_parser("status"); p.add_argument("image"); p.add_argument("status", choices=STATUSES)
    p.add_argument("note", nargs="?", default="")
    for name in ("list", "catalog", "gallery"):
        sub.add_parser(name)
    a = ap.parse_args()
    globals()[f"cmd_{a.cmd}"](a)


if __name__ == "__main__":
    main()
