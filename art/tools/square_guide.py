"""Build an edge guide from a sheet with the body sides redrawn as straight lines.

Takes the sheet's outlines (canny edges), erases them in bands along each side of the body, and
draws straight lines in their place. The result feeds the edge ControlNet (module "none"), so the
generated body keeps the sheet's pose but gets the straight sides.

Presets:
  torso   for enoch_sheet_v9.png: straight torso sides, shoulders to hips.
  thighs  for enoch_character_sheet.png: straight sides from the armpits down to the knees, so the
          thighs line up with the shoulders instead of flaring out at the hips.
  shoulders  for enoch_character_sheet.png: the other way round. Keeps the thighs, moves each arm
          outward and runs the torso sides straight down from the wider shoulders to the thighs.

usage:
  python square_guide.py <sheet.png> <guide_out.png> <preview_out.png> [--preset torso|thighs]
"""
import argparse
import numpy as np
from PIL import Image, ImageDraw
from skimage import feature

W, H = 1536, 1024  # coordinates below are for the sheet scaled to this size

# per view: (erase box, polyline or None)
PRESETS = {
    "torso": [
        # front view: torso sides (and the arm-torso gap), then the hourglass belly patch
        ((232, 300, 292, 525), [(264, 300), (264, 522)]),
        ((370, 300, 432, 525), [(399, 300), (399, 522)]),
        ((292, 330, 370, 480), None),
        # back view
        ((1165, 290, 1238, 548), [(1203, 290), (1203, 545)]),
        ((1312, 290, 1385, 548), [(1345, 290), (1345, 545)]),
    ],
    "thighs": [
        # front view: armpit straight down to the knee, then a short step out to the calf
        ((216, 300, 274, 728), [(262, 300), (262, 700), (244, 728)]),
        ((388, 300, 440, 728), [(398, 300), (398, 700), (406, 728)]),
        ((268, 330, 392, 560), None),  # belly patch outline: let it redraw inside the new sides
        # back view
        ((1166, 290, 1218, 740), [(1207, 290), (1207, 705), (1194, 740)]),
        ((1336, 290, 1386, 740), [(1345, 290), (1345, 705), (1360, 740)]),
    ],
}

# moves: (polygon around an arm, dx). The arm's edges are cut out and pasted dx pixels sideways.
SHIFTS = {
    "shoulders": [
        # front view
        ([(140, 262), (252, 262), (262, 300), (262, 400), (256, 450), (246, 490), (232, 530), (224, 545),
          (224, 665), (140, 665)], -40),
        ([(398, 262), (520, 262), (520, 665), (436, 665), (436, 545), (426, 530), (420, 490), (412, 450),
          (400, 400), (398, 300)], 35),
        # back view
        ([(1100, 262), (1205, 262), (1207, 300), (1207, 400), (1200, 450), (1190, 490), (1176, 530),
          (1168, 545), (1168, 665), (1100, 665)], -25),
        ([(1345, 262), (1460, 262), (1460, 665), (1380, 665), (1380, 545), (1372, 530), (1360, 490),
          (1352, 450), (1345, 400), (1345, 300)], 25),
    ],
}
PRESETS["shoulders"] = [
    # front view: old torso sides and belly patch out, straight sides from shoulder to thigh in
    ((228, 300, 272, 545), [(227, 296), (227, 600)]),
    ((388, 300, 431, 545), [(432, 296), (432, 600)]),
    ((272, 330, 388, 560), None),
    # back view
    ((1186, 295, 1215, 545), [(1185, 292), (1185, 610)]),
    ((1336, 295, 1364, 545), [(1365, 292), (1365, 610)]),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("preview")
    ap.add_argument("--preset", default="torso", choices=PRESETS)
    a = ap.parse_args()
    img = Image.open(a.src).convert("L").resize((W, H), Image.LANCZOS)
    edges = feature.canny(np.asarray(img).astype(float), sigma=1.5)
    e = (edges * 255).astype(np.uint8)
    for poly, dx in SHIFTS.get(a.preset, []):
        m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon(poly, fill=255)
        m = np.asarray(m) > 0
        part = np.where(m, e, 0); e[m] = 0
        e = np.maximum(e, np.roll(part, dx, axis=1))
    g = Image.fromarray(e)
    d = ImageDraw.Draw(g)
    for box, line in PRESETS[a.preset]:
        d.rectangle(box, fill=0)
        if line: d.line(line, fill=255, width=2)
    g.save(a.out)
    # preview: guide in red over the sheet
    base = Image.open(a.src).convert("RGB").resize((W, H), Image.LANCZOS)
    over = np.asarray(base).copy(); over[np.asarray(g) > 0] = (230, 20, 20)
    Image.fromarray(over).save(a.preview)
    print(a.out)


if __name__ == "__main__":
    main()
