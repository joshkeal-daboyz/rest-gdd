"""Final Forge pass: redraw a finished sheet at higher resolution and low strength so hand-made
fixes (eye colour, shine, tufts) blend in, then snap back to the palette.

usage:
  python final_pass.py <in.png> <out.png> <prompt.txt> <negative.txt> [--scale 2] [--denoise 0.3]
"""
import argparse, base64, io, json, pathlib, urllib.request
import numpy as np
from PIL import Image

FORGE = "http://127.0.0.1:7860"
PALETTE = [(72, 194, 195), (42, 67, 101), (208, 255, 250), (2, 3, 4), (250, 247, 239),
           (255, 255, 255), (141, 63, 76)]   # teal, navy, mint, line, background, white, iris


def b64(im):
    buf = io.BytesIO(); im.save(buf, "PNG"); return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("prompt"); ap.add_argument("negative")
    ap.add_argument("--scale", type=float, default=2.0); ap.add_argument("--denoise", type=float, default=0.3)
    a = ap.parse_args()
    read = lambda f: pathlib.Path(f).read_text(encoding="utf-8-sig").strip()
    src = Image.open(a.src).convert("RGB")
    W, H = int(src.width * a.scale) // 8 * 8, int(src.height * a.scale) // 8 * 8
    big = src.resize((W, H), Image.LANCZOS)
    payload = {"init_images": [b64(big)], "denoising_strength": a.denoise, "prompt": read(a.prompt),
               "negative_prompt": read(a.negative), "width": W, "height": H, "steps": 30, "cfg_scale": 6,
               "sampler_name": "Euler a", "seed": -1}
    req = urllib.request.Request(f"{FORGE}/sdapi/v1/img2img", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    res = json.load(urllib.request.urlopen(req, timeout=1800))
    img = Image.open(io.BytesIO(base64.b64decode(res["images"][0]))).convert("RGB")
    raw = pathlib.Path(a.out).with_suffix(".raw.png"); img.save(raw)
    px = np.asarray(img).astype(float); P = np.array(PALETTE, float)
    k = np.linalg.norm(px[:, :, None] - P[None, None], axis=3).argmin(2)
    Image.fromarray(P[k].astype(np.uint8)).save(a.out)
    print(a.out, (W, H))


if __name__ == "__main__":
    main()
