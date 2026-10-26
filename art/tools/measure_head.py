"""Measure head size as a fraction of height, for the leftmost (front-view) figure on a sheet.

The neck is taken as the narrowest row between 10% and 35% of the figure's height; everything
above it (ears included) is the head.

usage:
  python measure_head.py <sheet.png> [<sheet.png> ...]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage


def head_ratio(path):
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    bg = np.median(np.array([a[3, 3], a[3, -4], a[-4, 3], a[-4, -4]]), axis=0)
    fg = ndimage.binary_fill_holes(ndimage.binary_closing(np.abs(a - bg).sum(2) > 60, iterations=2))
    lab, n = ndimage.label(fg)
    sizes = ndimage.sum(fg, lab, range(1, n + 1))
    tall = lambda sl: (sl[0].stop - sl[0].start) > a.shape[0] * 0.6  # whole figures, not a loose tail
    figs = [(sl, i + 1) for i, sl in enumerate(ndimage.find_objects(lab)) if sizes[i] > fg.size * 0.01 and tall(sl)]
    sl, idx = min(figs, key=lambda f: f[0][1].start)  # leftmost large figure
    m = lab[sl] == idx
    rows = np.where(m.any(1))[0]; top, bottom = rows[0], rows[-1]; h = bottom - top
    widths = m.sum(1)
    lo, hi = top + int(h * 0.10), top + int(h * 0.35)
    neck = lo + int(np.argmin(widths[lo:hi]))
    return (neck - top) / h


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(f"{head_ratio(p):.3f}  {p}")
