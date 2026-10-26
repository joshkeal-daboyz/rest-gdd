"""Build an edge guide from a sheet with the torso sides redrawn as straight lines.

Takes the sheet's outlines (canny edges), erases them in bands along each side of the torso, and
draws straight lines from shoulder to hip in their place. The result feeds the edge ControlNet
(module "none"), so the generated body keeps the sheet's pose but gets a square torso.

usage:
  python square_guide.py <sheet.png> <guide_out.png> <preview_out.png>
"""
import sys
import numpy as np
from PIL import Image, ImageDraw
from skimage import feature

# per view: (erase box, straight line). Coordinates are for enoch_sheet_v9.png (1536x1024).
EDITS = [
    # front view: torso sides (and the arm-torso gap), then the hourglass belly patch
    ((232, 300, 292, 525), ((264, 300), (264, 522))),
    ((370, 300, 432, 525), ((399, 300), (399, 522))),
    ((292, 330, 370, 480), None),
    # back view
    ((1165, 290, 1238, 548), ((1203, 290), (1203, 545))),
    ((1312, 290, 1385, 548), ((1345, 290), (1345, 545))),
]


def main():
    src, out, preview = sys.argv[1:4]
    img = Image.open(src).convert("L")
    edges = feature.canny(np.asarray(img).astype(float), sigma=1.5)
    g = Image.fromarray((edges * 255).astype(np.uint8))
    d = ImageDraw.Draw(g)
    for box, line in EDITS:
        d.rectangle(box, fill=0)
        if line: d.line(line, fill=255, width=2)
    g.save(out)
    # preview: guide in red over the sheet
    base = Image.open(src).convert("RGB")
    over = np.asarray(base).copy(); over[np.asarray(g) > 0] = (230, 20, 20)
    Image.fromarray(over).save(preview)
    print(out)


if __name__ == "__main__":
    main()
