"""Remove stray lines inside the gaps between the arms and the body.

A stray line is a dark stroke with background on both sides (left and right). Real outlines always
have fur on one side, so they are kept. Then the faint fringes the stroke leaves are cleared, and
any pixel mostly surrounded by background (the stub where the stroke met an outline) is shaved
off until none are left. Last, the gap itself is smoothed and its outline redrawn at an even
thickness (--line, in pixels), so no bumps are left where a stroke used to join. Only the boxes
given are touched.

usage:
  python clean_gaps.py <in.png> <out.png> x0,y0,x1,y1 [x0,y0,x1,y1 ...] [--reach 14]
"""
import argparse
import numpy as np
from PIL import Image
from scipy import ndimage

BG, LINE = np.array([250, 247, 239]), np.array([2, 3, 4])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("boxes", nargs="+")
    ap.add_argument("--reach", type=int, default=14, help="how far to look left and right for background")
    ap.add_argument("--line", type=int, default=8, help="outline thickness to redraw around each gap")
    ap.add_argument("--smooth", type=int, default=8, help="radius for smoothing the gap's shape")
    a = ap.parse_args()
    im = np.asarray(Image.open(a.src).convert("RGB")).copy()
    bg = np.abs(im.astype(int) - BG).sum(2) < 30
    dark = np.abs(im.astype(int) - LINE).sum(2) < 120
    total = 0
    for b in a.boxes:
        x0, y0, x1, y1 = map(int, b.split(","))
        sub_bg, sub_dark = bg[y0:y1, x0:x1], dark[y0:y1, x0:x1]
        H, W = sub_bg.shape
        left = np.zeros_like(sub_bg); right = np.zeros_like(sub_bg)
        for d in range(1, a.reach + 1):  # background somewhere within reach on each side
            left[:, d:] |= sub_bg[:, :-d]; right[:, :-d] |= sub_bg[:, d:]
        stray = sub_dark & left & right
        # whole strokes only: keep pieces that are mostly stray
        lab, n = ndimage.label(ndimage.binary_dilation(stray, iterations=1) & sub_dark)
        for i in range(1, n + 1):
            piece = lab == i
            if stray[piece].mean() > 0.6 and piece.sum() > 40:
                im[y0:y1, x0:x1][ndimage.binary_dilation(piece, iterations=1) & ~sub_bg] = BG
                total += piece.sum()
        s = im[y0:y1, x0:x1]
        # fringes: thin non-line pixels lying inside the background
        sbg = np.abs(s.astype(int) - BG).sum(2) < 30
        sdark = np.abs(s.astype(int) - LINE).sum(2) < 120
        s[ndimage.binary_closing(sbg, structure=np.ones((5, 5))) & ~sbg & ~sdark] = BG
        # stubs: shave pixels mostly surrounded by background
        for size, frac in ((11, 0.62), (15, 0.56)):
            for _ in range(6):
                sbg = np.abs(s.astype(int) - BG).sum(2) < 30
                kill = ~sbg & (ndimage.uniform_filter(sbg.astype(float), size) > frac)
                if not kill.any(): break
                s[kill] = BG
        # redraw: the gap is the background in the box that doesn't touch its left or right side
        sbg = np.abs(s.astype(int) - BG).sum(2) < 30
        lab, n = ndimage.label(sbg)
        side = set(lab[:, 0]) | set(lab[:, -1])
        gap = np.isin(lab, [i for i in range(1, n + 1) if i not in side])
        r = a.smooth; yy, xx = np.mgrid[-r:r + 1, -r:r + 1]; disk = xx ** 2 + yy ** 2 <= r * r
        padded = np.pad(gap, r + 1, mode="edge")
        smooth = ndimage.binary_closing(padded, structure=disk)[r + 1:-r - 1, r + 1:-r - 1]
        band = (ndimage.distance_transform_edt(~smooth) <= a.line) & ~smooth
        s[smooth] = BG
        s[band] = LINE
    Image.fromarray(im).save(a.out)
    print("removed", total, "px")


if __name__ == "__main__":
    main()
