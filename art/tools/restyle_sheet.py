"""Make a new version of a reference sheet: same colours, style and layout, with the prompt's changes.

The reference is used twice: as the starting image (keeps layout, colours, tail pattern) and as an
IP-Adapter style reference (keeps the art style). --denoise sets how far the result may move away.

usage:
  python restyle_sheet.py <reference.png|jpg> <out_dir> <prompt.txt> <negative.txt>
                          [--denoise 0.55] [--count 4] [--width 1536] [--style-weight 0.5]
                          [--start shapes.png]
"""
import argparse, base64, io, json, pathlib, urllib.request
from PIL import Image

FORGE = "http://127.0.0.1:7860"


def b64(img):
    buf = io.BytesIO(); img.save(buf, "PNG"); return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref"); ap.add_argument("out_dir"); ap.add_argument("prompt"); ap.add_argument("negative")
    ap.add_argument("--denoise", type=float, default=0.55); ap.add_argument("--count", type=int, default=4)
    ap.add_argument("--width", type=int, default=1536); ap.add_argument("--style-weight", type=float, default=0.5)
    ap.add_argument("--tag", default="")
    ap.add_argument("--start", help="start from this image instead of the reference (keeps its shapes)")
    ap.add_argument("--fresh", action="store_true", help="start from noise; the reference only guides style")
    ap.add_argument("--height", type=int, default=1024)
    a = ap.parse_args()

    ref = Image.open(a.ref).convert("RGB")
    base = Image.open(a.start).convert("RGB") if a.start else ref
    W = a.width // 8 * 8; H = round(base.height * W / base.width) // 8 * 8
    start = base.resize((W, H), Image.LANCZOS)
    read = lambda f: pathlib.Path(f).read_text(encoding="utf-8-sig").strip()
    out = pathlib.Path(a.out_dir); out.mkdir(parents=True, exist_ok=True)
    n = 0
    for _ in range((a.count + 1) // 2):
        payload = {"init_images": [b64(start)], "denoising_strength": a.denoise,
                   "prompt": read(a.prompt), "negative_prompt": read(a.negative),
                   "width": W, "height": H, "steps": 30, "cfg_scale": 6, "sampler_name": "Euler a",
                   "batch_size": 2, "seed": -1,
                   "alwayson_scripts": {"ControlNet": {"args": [{
                       "enabled": True, "module": "CLIP-ViT-H (IPAdapter)",
                       "model": "ip-adapter-plus_sdxl_vit-h [bc449f62]", "weight": a.style_weight,
                       "image": b64(ref), "resize_mode": "Crop and Resize",
                       "control_mode": "My prompt is more important", "pixel_perfect": True}]}}}
        if a.style_weight <= 0: payload.pop("alwayson_scripts")
        endpoint = "img2img"
        if a.fresh:
            for k in ("init_images", "denoising_strength"): payload.pop(k)
            payload["height"] = a.height // 8 * 8; endpoint = "txt2img"
        req = urllib.request.Request(f"{FORGE}/sdapi/v1/{endpoint}", data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"})
        res = json.load(urllib.request.urlopen(req, timeout=1800))
        seeds = json.loads(res["info"]).get("all_seeds", [])
        for i, data in enumerate(res["images"][:2]):
            n += 1
            f = out / f"sheet{a.tag}_d{int(a.denoise*100)}_{seeds[i] if i < len(seeds) else n}.png"
            f.write_bytes(base64.b64decode(data)); print(f)


if __name__ == "__main__":
    main()
