"""Colour Enoch's pupils when they came out as hollow rings or thin lines (color_eyes.py expects
solid pupils, and on such sheets it can mistake the nose for an eye).

Each pupil becomes solid black, keeps its generated size, gets her red-brown on its lower half
inside a thin black rim, and a small white shine at the top.

usage:
  python fill_pupils.py <in.png> <out.png> <spec.json>

spec.json (key "pupils"):
  {"rings":   [[x, y], ...],               # a point inside each hollow ring
   "ellipses": [[cx, cy, rx, ry], ...]}    # pupils drawn fresh, e.g. a side view's thin line
"""
import json, sys
import numpy as np
from PIL import Image
from scipy import ndimage

LINE, IRIS, WHITE = (2, 3, 4), (141, 63, 76), (255, 255, 255)


def main():
    src, dst, spec = sys.argv[1:4]
    spec = json.load(open(spec))["pupils"]
    a = np.asarray(Image.open(src).convert("RGB")).copy()
    yy, xx = np.mgrid[:a.shape[0], :a.shape[1]]
    pupils = [((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1 for cx, cy, rx, ry in spec.get("ellipses", [])]
    for p in pupils:  # draw the new pupils first so they count as line work below
        a[p] = LINE
    dark = np.linalg.norm(a.astype(int) - LINE, axis=2) < 90
    lab, _ = ndimage.label(~dark)
    for x, y in spec.get("rings", []):
        m = lab == lab[y, x]
        if m.sum() >= 400:
            sys.exit(f"({x},{y}) is not inside a small pupil ring")
        pupils.append(ndimage.binary_dilation(m, iterations=2))  # ring and its inside
    for p in pupils:
        a[p] = LINE
        cy = np.nonzero(p)[0].mean()
        inner = ndimage.binary_erosion(p, iterations=2)
        a[inner & (yy > cy)] = IRIS
        ys, xs = np.nonzero(inner)
        ty, tx = ys.min() + 1, int(np.percentile(xs, 30))
        a[ty:ty + 2, tx:tx + 2] = WHITE
    Image.fromarray(a).save(dst)
    print(f"{len(pupils)} pupils -> {dst}")


if __name__ == "__main__":
    main()
