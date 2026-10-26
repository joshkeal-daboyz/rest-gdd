"""Snap every pixel of a flat-colour image to the nearest colour in a fixed palette.

Guarantees the result uses only the palette's colours (for example, the favourite sheet's).

usage:
  python palette_snap.py <in.png> <out.png> --palette "#44C1BE" "#1D3147" ...
"""
import argparse
import numpy as np
from PIL import Image


def hexrgb(h): h = h.strip().lstrip("#"); return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--palette", nargs="+", required=True)
    a = ap.parse_args()
    P = np.array([hexrgb(c) for c in a.palette], float)
    img = np.asarray(Image.open(a.src).convert("RGB")).astype(float)
    k = np.linalg.norm(img[:, :, None, :] - P[None, None], axis=3).argmin(2)
    Image.fromarray(P[k].astype(np.uint8)).save(a.out); print(a.out)


if __name__ == "__main__":
    main()
