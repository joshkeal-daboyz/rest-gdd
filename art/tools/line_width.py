"""Measure outline thickness, in pixels and as a fraction of the front figure's height.

Line pixels are the darkest ones (near-black). Thickness is read from the distance transform
along each line's centre (skeleton), then the median is taken.

usage:
  python line_width.py <sheet.png> [<sheet.png> ...]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize


def measure(path):
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    line = a.sum(2) < 120
    dist = ndimage.distance_transform_edt(line)
    skel = skeletonize(line)
    width = float(np.median(dist[skel]) * 2)
    bg = np.median(np.array([a[3, 3], a[3, -4], a[-4, 3], a[-4, -4]]), axis=0)
    fg = ndimage.binary_closing(np.abs(a - bg).sum(2) > 60, iterations=2)
    lab, n = ndimage.label(fg)
    sizes = ndimage.sum(fg, lab, range(1, n + 1))
    figs = [sl for i, sl in enumerate(ndimage.find_objects(lab))
            if sizes[i] > fg.size * 0.01 and (sl[0].stop - sl[0].start) > a.shape[0] * 0.6]
    sl = min(figs, key=lambda s: s[1].start)
    height = sl[0].stop - sl[0].start
    return width, height


if __name__ == "__main__":
    for p in sys.argv[1:]:
        w, h = measure(p)
        print(f"line {w:.1f}px  figure {h}px  ratio {w / h * 100:.2f}%  {p}")
