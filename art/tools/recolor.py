"""Swap a flat-coloured character sheet to a new palette, keeping every shape and the line work.

Each pixel is matched to its nearest source colour and moved by the same offset as that colour,
so shading and anti-aliasing carry over.

usage:
  python recolor.py <in.png> <out.png> --map "#src=#dst" "#src=#dst" ... [--bg "#src,#bg,#enclosed"]
"""
import argparse
import numpy as np
from PIL import Image


def hexrgb(h): h = h.strip().lstrip("#"); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--map", nargs="+", required=True)
    ap.add_argument("--keep-dist", type=float, default=90, help="leave pixels this far from every source colour alone")
    ap.add_argument("--bg", help='"#src,#background,#enclosed": split one colour into background and enclosed areas')
    a = ap.parse_args()
    pairs = [m.split("=") for m in a.map]
    S = np.stack([hexrgb(s) for s, _ in pairs]); D = np.stack([hexrgb(d) for _, d in pairs])
    img = np.asarray(Image.open(a.src).convert("RGB")).astype(float)
    dist = np.linalg.norm(img[:, :, None, :] - S[None, None], axis=3)
    k = dist.argmin(2); near = dist.min(2) < a.keep_dist
    out = img.copy()
    out[near] = img[near] + (D[k] - S[k])[near]
    if a.bg:
        # background and enclosed areas (like a chest) can share one colour: only the part that
        # touches the image edge is background; enclosed areas get --enclosed
        from scipy import ndimage
        src, bg_dst, enc_dst = (hexrgb(c) for c in a.bg.split(","))
        same = np.linalg.norm(img - src, axis=2) < 18
        lab, _ = ndimage.label(same)
        edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
        is_bg = np.isin(lab, list(edge))
        out[is_bg] = img[is_bg] + (bg_dst - src)
        enc = same & ~is_bg
        out[enc] = img[enc] + (enc_dst - src)
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(a.out); print(a.out)


if __name__ == "__main__":
    main()
