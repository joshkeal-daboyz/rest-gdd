"""Generate Enoch character sheets from the rules, finish them the same way every time, and measure them.

Steps for each image:
  1. Generate with the prompt files (built from art/enoch-sheet/enoch-rules.md).
  2. Snap every pixel to the palette (teal, navy, mint, line, background).
  3. Light areas touching the image edge become background; enclosed light areas in the upper
     part of a figure become mint (chest), the rest background (gaps between limbs).
  4. Thicken outlines to the target weight and recolour them to the line colour.
  5. Measure head size and line weight, and write them on a preview grid.

usage:
  python enoch_pipeline.py <out_dir> <prompt.txt> <negative.txt> [--count 16]
                           [--guide body.png --weight 0.6 --end 0.6]
"""
import argparse, base64, io, json, pathlib, sys, urllib.request
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from measure_head import head_ratio      # noqa: E402
from line_width import measure as line_measure  # noqa: E402

FORGE = "http://127.0.0.1:7860"
# sampled from art/female-raccoon/baseline-highres.png
TEAL, NAVY, MINT, LINE, BG = (72, 194, 195), (42, 67, 101), (208, 255, 250), (2, 3, 4), (250, 247, 239)
RAW_LINE = (0, 3, 9)
TARGET_LINE = 0.0033  # outline width as a fraction of figure height (hers is 0.33%)


def generate(prompt, negative, count, w=1536, h=1024, guide=None, weight=0.6, end=0.6, edges=False):
    imgs = []
    for _ in range((count + 1) // 2):
        payload = {"prompt": prompt, "negative_prompt": negative, "width": w, "height": h, "steps": 30,
                   "cfg_scale": 6, "sampler_name": "Euler a", "batch_size": 2, "seed": -1}
        if guide:
            # lock the body outline to the guide image's edges; the prompt controls everything else
            buf = io.BytesIO(); Image.open(guide).convert("RGB").resize((w, h)).save(buf, "PNG")
            payload["alwayson_scripts"] = {"ControlNet": {"args": [{
                "enabled": True, "module": "None" if edges else "canny", "model": "diffusion_pytorch_model_V2 [ab7dc06d]",
                "weight": weight, "guidance_start": 0.0, "guidance_end": end,
                "image": base64.b64encode(buf.getvalue()).decode(), "resize_mode": "Crop and Resize",
                "control_mode": "Balanced", "pixel_perfect": True}]}}
        req = urllib.request.Request(f"{FORGE}/sdapi/v1/txt2img", data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"})
        res = json.load(urllib.request.urlopen(req, timeout=1800))
        seeds = json.loads(res["info"]).get("all_seeds", [])
        for i, d in enumerate(res["images"][:2]):
            imgs.append((seeds[i] if i < len(seeds) else len(imgs), Image.open(io.BytesIO(base64.b64decode(d))).convert("RGB")))
    return imgs[:count]


def finish(img):
    a = np.asarray(img).astype(float)
    pal = np.array([TEAL, NAVY, MINT, RAW_LINE, BG, (255, 255, 255)], float)
    # the background is decided by edge-connectivity below, so a coloured backdrop doesn't stay teal
    corners = np.array([a[3, 3], a[3, -4], a[-4, 3], a[-4, -4]])
    bgc = np.median(corners, axis=0)
    is_bg_colour = np.linalg.norm(a - bgc, axis=2) < 25
    k = np.linalg.norm(a[:, :, None] - pal[None, None], axis=3).argmin(2)
    out = pal[k].astype(np.uint8)
    out[k == 5] = BG
    bg_lab, _ = ndimage.label(is_bg_colour)
    edge_ids = set(np.unique(np.concatenate([bg_lab[0], bg_lab[-1], bg_lab[:, 0], bg_lab[:, -1]]))) - {0}
    out[np.isin(bg_lab, list(edge_ids))] = BG
    H = out.shape[0]
    light = np.all(out == BG, 2) | np.all(out == MINT, 2)
    lab, n = ndimage.label(light)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    for i, sl in enumerate(ndimage.find_objects(lab)):
        m = lab[sl] == i + 1
        if i + 1 in edge:
            out[sl][m] = BG; continue
        cy = (sl[0].start + sl[0].stop) / 2
        if m.sum() < 8000:
            # small patch: if the fur just around it is mostly teal, it's a stray mark on the body
            full = lab == i + 1
            ring = ndimage.binary_dilation(full, iterations=6) & ~ndimage.binary_dilation(full, iterations=3)
            rc = out[ring]; rc = rc[~np.all(rc == RAW_LINE, axis=1)]  # ignore the outline itself
            if len(rc) and np.all(rc == TEAL, axis=1).mean() > 0.5:
                out[sl][m] = TEAL; continue
        out[sl][m] = MINT if (cy < 0.6 * H and m.sum() > 3000) else BG
    # outline weight
    line = np.all(out == RAW_LINE, 2)
    dist = ndimage.distance_transform_edt(line)
    from skimage.morphology import skeletonize
    sk = skeletonize(line)
    width = float(np.median(dist[sk]) * 2) if sk.any() else 2
    fig_h = H * 0.9
    grow = max(0, round((TARGET_LINE * fig_h - width) / 2))
    if grow: line = ndimage.binary_dilation(line, structure=np.ones((3, 3)), iterations=grow)
    out[line] = LINE
    return Image.fromarray(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir"); ap.add_argument("prompt"); ap.add_argument("negative")
    ap.add_argument("--count", type=int, default=16)
    ap.add_argument("--guide", help="image whose outline sets the body shape (canny ControlNet)")
    ap.add_argument("--weight", type=float, default=0.6); ap.add_argument("--end", type=float, default=0.6)
    ap.add_argument("--refinish", action="store_true", help="skip generating; re-finish out_dir/raw")
    ap.add_argument("--edges", action="store_true", help="the guide is already an edge map (from square_guide.py)")
    a = ap.parse_args()
    read = lambda f: pathlib.Path(f).read_text(encoding="utf-8-sig").strip()
    out = pathlib.Path(a.out_dir); (out / "raw").mkdir(parents=True, exist_ok=True)
    rows = []
    if a.refinish:  # re-run the finishing steps on images already generated
        batch = [(p.stem, Image.open(p).convert("RGB")) for p in sorted((out / "raw").glob("*.png"))]
    else:
        batch = generate(read(a.prompt), read(a.negative), a.count, guide=a.guide, weight=a.weight, end=a.end, edges=a.edges)
    for seed, img in batch:
        img.save(out / "raw" / f"{seed}.png")
        f = out / f"enoch_{seed}.png"; finish(img).save(f)
        try: hr = head_ratio(f)
        except Exception: hr = float("nan")
        lw, fh = line_measure(f)
        rows.append((seed, f, hr, lw / fh))
        print(f"{seed}  head {hr:.3f}  line {lw / fh * 100:.2f}%")
    cols = 4; tw, th = 384, 256
    grid = Image.new("RGB", (tw * cols, th * ((len(rows) + cols - 1) // cols)), "white"); d = ImageDraw.Draw(grid)
    for i, (seed, f, hr, lr) in enumerate(rows):
        x, y = (i % cols) * tw, (i // cols) * th
        grid.paste(Image.open(f).resize((tw, th)), (x, y))
        d.text((x + 6, y + 6), f"{i + 1}  head {hr:.2f}", fill=(200, 0, 0))
    grid.save(out / "options.png"); print(out / "options.png")


if __name__ == "__main__":
    main()
