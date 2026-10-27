"""Upscale a finished sheet with a Forge upscaler, then snap it back to the palette.

The upscaler keeps lines crisp; the snap keeps the colours exactly the sheet's flat palette.
The unsnapped result is saved next to the output as <out>.raw.png.

usage:
  python upscale.py <in.png> <out.png> [--scale 2] [--upscaler "R-ESRGAN 4x+ Anime6B"]
"""
import argparse, base64, io, json, pathlib, urllib.request
import numpy as np
from PIL import Image

FORGE = "http://127.0.0.1:7860"
PALETTE = np.array([(72, 194, 195), (42, 67, 101), (208, 255, 250), (2, 3, 4), (250, 247, 239),
                    (255, 255, 255), (141, 63, 76)], np.int32)  # same as final_pass.py


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=2); ap.add_argument("--upscaler", default="R-ESRGAN 4x+ Anime6B")
    a = ap.parse_args()
    buf = io.BytesIO(); Image.open(a.src).convert("RGB").save(buf, "PNG")
    payload = {"image": base64.b64encode(buf.getvalue()).decode(), "resize_mode": 0,
               "upscaling_resize": a.scale, "upscaler_1": a.upscaler}
    req = urllib.request.Request(f"{FORGE}/sdapi/v1/extra-single-image", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    res = json.load(urllib.request.urlopen(req, timeout=3600))
    img = Image.open(io.BytesIO(base64.b64decode(res["image"]))).convert("RGB")
    img.save(pathlib.Path(a.out).with_suffix(".raw.png"))
    px = np.asarray(img)
    # white and iris only where the source already has them (eyes, inner ears), so the
    # upscaler's light fringes along outlines don't snap to white
    ref = np.asarray(Image.open(a.src).convert("RGB").resize(img.size, Image.NEAREST)).astype(np.int32)
    out = np.empty_like(px)
    for y in range(0, px.shape[0], 256):  # in strips to keep memory low
        s = px[y:y + 256].astype(np.int32)
        d = ((s[:, :, None, :] - PALETTE[None, None]) ** 2).sum(3)
        r = ref[y:y + 256]
        for k in (5, 6):
            near = np.abs(r - PALETTE[k]).sum(2) < 30
            near = near | np.roll(near, 1, 0) | np.roll(near, -1, 0) | np.roll(near, 1, 1) | np.roll(near, -1, 1)
            d[:, :, k][~near] = 1 << 30
        out[y:y + 256] = PALETTE[d.argmin(2)].astype(np.uint8)
    Image.fromarray(out).save(a.out, optimize=True)
    print(a.out, img.size)


if __name__ == "__main__":
    main()
