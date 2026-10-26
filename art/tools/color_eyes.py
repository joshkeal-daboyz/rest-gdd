"""Give a finished Enoch sheet eyes like the female raccoon's: a big black pupil, a red-brown
crescent along its bottom, and a white highlight at the top.

Eye whites are found as small light areas in the top part of the sheet that sit inside the
navy mask; the existing pupil inside each one sets the eye's centre.

usage:
  python color_eyes.py <in.png> <out.png>
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

NAVY, LINE = np.array([42, 67, 101]), np.array([2, 3, 4])
IRIS = np.array([141, 63, 76])     # sampled from her sheet (#8D3F4C)
WHITE = np.array([255, 255, 255])


def main():
    src, dst = sys.argv[1:3]
    a = np.asarray(Image.open(src).convert("RGB")).copy()
    H, W, _ = a.shape
    ai = a.astype(int)
    # eye whites are white or near-white, not the mint of the muzzle (green well above red)
    light = (ai.sum(2) > 650) & ((ai[:, :, 1] - ai[:, :, 0]) < 20)
    light[int(H * 0.3):] = False                      # eyes are in the top 30% of the sheet
    lab, n = ndimage.label(light)
    yy, xx = np.mgrid[0:H, 0:W]
    disk = np.hypot(*np.mgrid[-3:4, -3:4]) <= 3
    solid_dark = ndimage.binary_opening(np.all(a == LINE, axis=2), structure=disk)  # pupils, not thin lines
    done = 0
    for i, sl in enumerate(ndimage.find_objects(lab)):
        region = lab == i + 1
        area = region.sum()
        if not 150 < area < 6000: continue
        ring = ndimage.binary_dilation(region, iterations=8) & ~ndimage.binary_dilation(region, iterations=3)
        rc = a[ring]
        navy_share = np.all(rc == NAVY, axis=1).mean()
        if navy_share < 0.3: continue                 # not inside the mask, so not an eye
        pupil = solid_dark & ndimage.binary_dilation(region, iterations=3)
        if pupil.sum() < 10: continue
        eye = ndimage.binary_fill_holes(region | pupil)
        # keep the pupil exactly as drawn; only colour a crescent along its bottom
        pupil = ndimage.binary_fill_holes(pupil)
        cy, cx = ndimage.center_of_mass(pupil)
        ys, xs = np.where(pupil)
        r = (ys.max() - ys.min()) / 2
        w = xs.max() - xs.min()
        inner = ndimage.binary_erosion(pupil, iterations=1) if w > 10 else pupil  # thin pupils: no rim
        cres = inner & (yy > cy - 0.1 * r)  # lower half: small pupils need the colour to show
        a[cres & np.all(a == LINE, axis=2)] = IRIS
        # eye shine: a small white oval in the upper part of the pupil, like hers
        hr = max(1.5, 0.28 * min(r, w / 2 + 1))
        shine = pupil & (((xx - (cx - 0.15 * w)) / hr) ** 2 + ((yy - (cy - 0.45 * r)) / (hr * 1.2)) ** 2 <= 1)
        a[shine] = WHITE
        done += 1
    Image.fromarray(a).save(dst)
    print(f"{done} eyes coloured -> {dst}")


if __name__ == "__main__":
    main()
