"""Patch the 3-pose edge guide: give the side view an arm and a full tail, and give the back view a tail.

The side view on shoulder_guide_3pose.png has a circle where the arm should be and a tail clipped
flat at the panel edge; the back view has no tail. This draws those parts as white outlines on the
black edge map (each shape is filled black first, so lines behind it disappear).

usage:
  python fix_3pose_guide.py [in.png] [out.png] [--preview preview.png]
"""
import argparse, math
from PIL import Image, ImageDraw

LINE = 2  # matches the guide's edge width


def spline(pts, n=24):
    """Catmull-Rom through the points, so hand-picked centrelines come out smooth."""
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(p) - 2):
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * (2 * p[i][j] + (-p[i - 1][j] + p[i + 1][j]) * t
                                    + (2 * p[i - 1][j] - 5 * p[i][j] + 4 * p[i + 1][j] - p[i + 2][j]) * t * t
                                    + (-p[i - 1][j] + 3 * p[i][j] - 3 * p[i + 1][j] + p[i + 2][j]) * t ** 3)
                             for j in range(2)))
    out.append(pts[-1])
    return out


def ribbon(centre, widths):
    """Outline of a shape that follows a centreline with the given widths, with a rounded tip."""
    c = spline(centre)
    w = [widths[min(int(i / len(c) * (len(widths) - 1) + 0.5), len(widths) - 1)] for i in range(len(c))]
    # smooth the width steps
    w = [sum(w[max(0, i - 6):i + 7]) / len(w[max(0, i - 6):i + 7]) for i in range(len(w))]
    left, right, normals = [], [], []
    for i in range(len(c)):
        a, b = c[max(i - 1, 0)], c[min(i + 1, len(c) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        normals.append((nx, ny))
        left.append((c[i][0] + nx * w[i] / 2, c[i][1] + ny * w[i] / 2))
        right.append((c[i][0] - nx * w[i] / 2, c[i][1] - ny * w[i] / 2))
    # rounded tip: half circle around the last centre point
    (ex, ey), (nx, ny), r = c[-1], normals[-1], w[-1] / 2
    ang0 = math.atan2(ny, nx)
    tip = [(ex + r * math.cos(ang0 - math.pi * k / 16), ey + r * math.sin(ang0 - math.pi * k / 16)) for k in range(17)]
    return c, w, normals, left + tip + right[::-1]


def tail(d, centre, widths, rings=6, open_base=True):
    """Ringed tail: black fill, outline (open at the body), then ring boundaries across it."""
    c, w, normals, poly = ribbon(centre, widths)
    d.polygon(poly, fill=0)
    n = len(c)
    edge = poly[:n + 17 + n] if open_base else poly + [poly[0]]
    d.line(edge, fill=255, width=LINE, joint="curve")
    # 6 boundaries -> 7 bands (navy, teal, navy, teal, navy, teal, navy tip); slight curve on each
    for k in range(1, rings + 1):
        i = int(n * (0.12 + 0.82 * k / (rings + 1)))
        (x, y), (nx, ny), h = c[i], normals[i], w[i] / 2 - 1
        bend = (c[min(i + 3, n - 1)][0] - c[i][0], c[min(i + 3, n - 1)][1] - c[i][1])
        arc = [(x + nx * h * s + bend[0] * 0.35 * (1 - s * s), y + ny * h * s + bend[1] * 0.35 * (1 - s * s))
               for s in [1 - 2 * t / 12 for t in range(13)]]
        d.line(arc, fill=255, width=LINE, joint="curve")


def arm(d):
    """Side-view arm hanging straight down in front of the torso, navy below a zigzag cuff."""
    front = spline([(724, 282), (720, 360), (722, 450), (726, 540), (728, 575)])
    back = spline([(778, 288), (784, 360), (783, 450), (780, 540), (778, 575)])
    hand = spline([(728, 575), (722, 610), (734, 642), (756, 650), (776, 636), (782, 604), (778, 575)])
    d.polygon(front + hand[1:] + back[::-1] + [(750, 270)], fill=0)
    d.arc((722, 262, 780, 316), 180, 360, fill=255, width=LINE)  # shoulder cap
    for part in (front, back, hand):
        d.line(part, fill=255, width=LINE, joint="curve")
    # zigzag cuff where the navy forearm starts (males zigzag, per the style guide)
    y = 462; xs = range(724, 784, 10)
    d.line([(x, y + (8 if i % 2 else 0)) for i, x in enumerate(xs)] + [(782, y + 4)], fill=255, width=LINE)
    # finger hints
    for fx in (742, 756):
        d.line([(fx, 628), (fx + 2, 646)], fill=255, width=LINE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", nargs="?", default="art/enoch-sheet/shoulder_guide_3pose.png")
    ap.add_argument("out", nargs="?", default="art/enoch-sheet/shoulder_guide_3pose_v2.png")
    ap.add_argument("--preview")
    a = ap.parse_args()
    im = Image.open(a.src).convert("L"); d = ImageDraw.Draw(im)

    # side view: remove the shoulder circle and the clipped tail (body outline stays)
    d.ellipse((708, 258, 788, 348), fill=0)
    d.rectangle((823, 455, 915, 635), fill=0)
    tail(d, [(808, 505), (870, 560), (925, 640), (960, 730), (968, 790)], [64, 84, 96, 92, 70])
    arm(d)

    # back view: drop the leftover hip crease the tail now covers, then add the tail,
    # hanging from the lower back down and out to the viewer's right
    d.rectangle((1148, 536, 1186, 556), fill=0)
    tail(d, [(1212, 505), (1228, 590), (1280, 680), (1360, 745), (1420, 770)], [62, 82, 98, 96, 74])

    im.convert("RGB").save(a.out); print(a.out)
    if a.preview:
        Image.open(a.out).resize((768, 512)).save(a.preview)


if __name__ == "__main__":
    main()
