"""Rerun an image from the settings embedded in it, changing only one piece of its prompt.

Good for: "I like this one, but the tail is off." Everything else (seed, size, sampler, the rest
of the prompt) stays the same, so only the wording you swap can change the result.

usage:
  python rerun_variant.py <image.png> <out.png> --old "text in the prompt" --new "replacement"
                          [--neg-add "extra negative terms"]
"""
import argparse, base64, json, re, urllib.request
from PIL import Image

FORGE = "http://127.0.0.1:7860"


def parse(params):
    prompt, rest = params.split("\nNegative prompt: ", 1)
    neg, settings = rest.rsplit("\nSteps: ", 1)
    s = {k.strip(): v.strip() for k, v in re.findall(r"([A-Za-z ]+): ([^,]+)", "Steps: " + settings)}
    w, h = map(int, s["Size"].split("x"))
    return prompt, neg, {"steps": int(s["Steps"]), "sampler_name": s["Sampler"].strip(),
                         "cfg_scale": float(s["CFG scale"]), "seed": int(s["Seed"]), "width": w, "height": h}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--old", required=True); ap.add_argument("--new", required=True)
    ap.add_argument("--neg-add", default="")
    a = ap.parse_args()
    prompt, neg, settings = parse(Image.open(a.src).info["parameters"])
    if a.old not in prompt:
        raise SystemExit(f"--old text not found in the prompt: {a.old!r}")
    prompt = prompt.replace(a.old, a.new)
    if a.neg_add: neg = a.neg_add + ", " + neg
    payload = {"prompt": prompt, "negative_prompt": neg, **settings}
    req = urllib.request.Request(f"{FORGE}/sdapi/v1/txt2img", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    res = json.load(urllib.request.urlopen(req, timeout=1800))
    open(a.out, "wb").write(base64.b64decode(res["images"][0])); print(a.out)


if __name__ == "__main__":
    main()
