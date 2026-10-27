"""Repaint a finished sheet's tails to Enoch's ring rule, and clear light gaps that should be background.

Ring rule (art/enoch-sheet/enoch-rules.md): 4 navy rings, the first at the base and the last at the
tip -> 7 equal bands: navy, teal, navy, teal, navy, teal, navy.

Each tail is given as a centreline from base to tip (hand-picked on the sheet). Pixels inside the
tail's outline are found by flood fill from the centreline, then coloured by how far along the
centreline they sit. Band edges bow slightly toward the tip so they read as rings, not straight cuts.

usage:
  python fix_tail_rings.py <in.png> <out.png> <spec.json>

spec.json:
  {"tails": [{"centre": [[x, y], ...], "cut": [[x1, y1], [x2, y2]]?}, ...],
   "gaps": [[x, y], ...]}   # a point inside each light area to turn into background
"""
import json, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
from scipy.spatial import cKDTree

TEAL, NAVY, MINT, LINE, BG = (72, 194, 195), (42, 67, 101), (208, 255, 250), (2, 3, 4), (250, 247, 239)
BANDS = 7
BOW = 0.06  # how far (as a fraction of tail length) band edges curve at the tail's sides


def dense(pts, step=1.0):
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(int(np.hypot(x1 - x0, y1 - y0) / step), 1)
        out += [(x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n) for k in range(n)]
    out.append(tuple(pts[-1]))
    return np.array(out)


def main():
    src, dst, spec = sys.argv[1:4]
    spec = json.load(open(spec))
    img = Image.open(src).convert("RGB")
    a = np.asarray(img).astype(int)
    line = np.linalg.norm(a - LINE, axis=2) < 90

    for t in spec.get("tails", []):
        wall = Image.fromarray(line.astype(np.uint8) * 255)
        if t.get("cut"):  # seal an open tail base so the fill can't leak into the body
            ImageDraw.Draw(wall).line([tuple(p) for p in t["cut"]], fill=255, width=3)
        open_ = np.asarray(wall) == 0
        lab, _ = ndimage.label(open_)
        c = dense(t["centre"])
        seeds = {lab[int(y), int(x)] for x, y in c[2:-2] if lab[int(y), int(x)]}
        region = np.isin(lab, list(seeds))
        ys, xs = np.nonzero(region)
        # arc length along the centreline, and signed distance to the side of it
        seg = np.r_[0, np.cumsum(np.hypot(*np.diff(c, axis=0).T))]
        L = seg[-1]
        d, i = cKDTree(c).query(np.c_[xs, ys])
        keep = (i > 0) & (d < 0.4 * L)  # pixels level with or past the base only
        ys, xs, d, i = ys[keep], xs[keep], d[keep], i[keep]
        tan = c[np.minimum(i + 1, len(c) - 1)] - c[np.maximum(i - 1, 0)]
        side = np.sign(tan[:, 0] * (ys - c[i, 1]) - tan[:, 1] * (xs - c[i, 0]))
        half = np.percentile(d, 98) or 1
        s = seg[i] / L + BOW * (np.clip(d / half, 0, 1) ** 2)  # bow the edges toward the tip
        band = np.clip((s * BANDS).astype(int), 0, BANDS - 1)
        out = np.where((band % 2 == 0)[:, None], NAVY, TEAL)
        a[ys, xs] = out
        print(f"tail: {len(ys)} px, length {L:.0f}, components {len(seeds)}")

    for x, y in spec.get("gaps", []):
        light = np.linalg.norm(a - MINT, axis=2) < 60
        lab, _ = ndimage.label(light)
        k = lab[y, x]
        if k:
            a[lab == k] = BG
            print(f"gap at ({x},{y}): {int((lab == k).sum())} px -> background")
        else:
            print(f"gap at ({x},{y}): not a light area, skipped")

    Image.fromarray(a.astype(np.uint8)).save(dst); print(dst)


if __name__ == "__main__":
    main()
