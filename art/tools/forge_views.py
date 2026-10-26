"""Generate one view of a character through a local Forge (Stable Diffusion WebUI Forge) API.

The prompt is built from a prompts JSON (see art/enoch-sheet/enoch-prompts.json), so changing
a rule there changes every future image.

usage:
  python forge_views.py <prompts.json> <out_dir> <view> [--count N] [--ref image.png]
                        [--guide image.png --denoise 0.45] [--check tail-paths.json]

  view       one of the keys under "views" in the prompts file
  --ref      an approved image of the character; keeps the new view looking like the same character
  --guide    start from this image instead of from noise. Pose, layout and the tail pattern carry over;
             --denoise sets how much may change (0 = nothing, 1 = everything)
  --check    run the tail rule check (check_tail.py) on every result; failures go to out_dir/rejected
"""
import argparse, base64, io, json, pathlib, shutil, urllib.request
from PIL import Image

import check_tail

FORGE = "http://127.0.0.1:7860"
ORDER = ["style", "identity", "build", "posture", "face", "colors", "feet", "tail", "base_body"]


def build_prompt(p, view):
    return ", ".join([p["views"][view]] + [p[k] for k in ORDER if p.get(k)])


def b64(img):
    buf = io.BytesIO(); img.save(buf, "PNG"); return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompts"); ap.add_argument("out_dir"); ap.add_argument("view")
    ap.add_argument("--count", type=int, default=4); ap.add_argument("--ref")
    ap.add_argument("--guide"); ap.add_argument("--denoise", type=float, default=0.45)
    ap.add_argument("--check"); ap.add_argument("--seed", type=int, default=-1)
    ap.add_argument("--tail", help="override the tail fragment, for testing a new wording")
    ap.add_argument("--tag", default="", help="added to output file names")
    a = ap.parse_args()

    p = json.loads(pathlib.Path(a.prompts).read_text(encoding="utf-8-sig"))
    if a.tail: p["tail"] = a.tail
    out = pathlib.Path(a.out_dir); out.mkdir(parents=True, exist_ok=True)
    # a fixed seed makes one image per call, so a change in wording is the only change
    batch = (1, 1) if a.seed >= 0 else (2, (a.count + 1) // 2)
    payload = {"prompt": build_prompt(p, a.view), "negative_prompt": p["negative"], "seed": a.seed,
               "batch_size": batch[0], "n_iter": batch[1], **p["settings"]}
    endpoint, guide_size = "txt2img", None
    if a.guide:
        g = Image.open(a.guide).convert("RGB"); guide_size = g.size
        W, H = -(-g.width // 8) * 8, -(-g.height // 8) * 8  # round up to a multiple of 8
        padded = Image.new("RGB", (W, H), (255, 255, 255)); padded.paste(g, (0, 0))
        payload.update(init_images=[b64(padded)], denoising_strength=a.denoise, width=W, height=H)
        endpoint = "img2img"
    if a.ref:
        r = p["reference"]
        payload["alwayson_scripts"] = {"ControlNet": {"args": [{
            "enabled": True, "module": r["module"], "model": r["model"], "weight": r["weight"],
            "image": base64.b64encode(pathlib.Path(a.ref).read_bytes()).decode(),
            "resize_mode": "Crop and Resize", "control_mode": r.get("control_mode", "Balanced"),
            "pixel_perfect": True}]}}

    req = urllib.request.Request(f"{FORGE}/sdapi/v1/{endpoint}", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    res = json.load(urllib.request.urlopen(req, timeout=1800))
    seeds = json.loads(res["info"]).get("all_seeds", [])
    segs = json.load(open(a.check, encoding="utf-8-sig"))[a.view] if a.check else None
    for i, data in enumerate(res["images"][:a.count]):
        f = out / f"{a.view}{a.tag}_{seeds[i] if i < len(seeds) else i}.png"
        img = Image.open(io.BytesIO(base64.b64decode(data)))
        if guide_size: img = img.crop((0, 0, *guide_size))
        img.save(f)
        if segs:
            ok, pat = check_tail.check(f, segs)
            if not ok:
                (out / "rejected").mkdir(exist_ok=True)
                f = pathlib.Path(shutil.move(str(f), out / "rejected" / f.name))
            print("PASS" if ok else "FAIL", pat, f)
        else:
            print(f)


if __name__ == "__main__":
    main()
