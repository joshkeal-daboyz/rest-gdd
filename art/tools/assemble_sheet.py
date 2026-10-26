"""Lay out single-pose images side by side as a character sheet, each clearly separated.

usage:
  python assemble_sheet.py <out.png> <pose1.png> <pose2.png> ... [--gap 120] [--height 960]

Each pose is cropped to the figure, scaled to the same figure height, and placed with an even gap.
"""
import argparse
import numpy as np
from PIL import Image

SHEET_BG = (240, 240, 240)


def cutout(path, height):
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    corners = np.array([a[5, 5], a[5, -6], a[-6, 5], a[-6, -6]])
    bg = np.median(corners, axis=0)
    fg = np.abs(a - bg).sum(2) > 45
    ys, xs = np.where(fg)
    a = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    fg = fg[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    a[~fg] = SHEET_BG  # unify each image's background with the sheet's
    img = Image.fromarray(a.astype(np.uint8))
    return img.resize((round(img.width * height / img.height), height), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("poses", nargs="+")
    ap.add_argument("--gap", type=int, default=120); ap.add_argument("--height", type=int, default=960)
    a = ap.parse_args()
    figs = [cutout(p, a.height) for p in a.poses]
    margin = a.gap // 2
    W = sum(f.width for f in figs) + a.gap * (len(figs) - 1) + margin * 2
    sheet = Image.new("RGB", (W, a.height + margin * 2), SHEET_BG)
    x = margin
    for f in figs:
        sheet.paste(f, (x, margin)); x += f.width + a.gap
    sheet.save(a.out); print(a.out, sheet.size)


if __name__ == "__main__":
    main()
