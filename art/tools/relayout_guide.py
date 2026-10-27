"""Drop a pose from an edge guide and re-space the rest, with the middle pose centred.

Edge pixels belong to a pose by column (bounds below, for enoch_character_sheet.png at 1536x1024;
the side view's tail tip and the back view's hand meet at x=1100). The dropped pose is erased.
With three poses left, the middle one is centred on the sheet and the outer two are centred in
the space on either side, so every pose has clear space around it.

usage:
  python relayout_guide.py <guide.png> <out.png> [--drop 1]
"""
import argparse
import numpy as np
from PIL import Image

# pose columns: front, side without tail, side with tail, back
BOUNDS = [0, 560, 820, 1100, 1536]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("guide"); ap.add_argument("out")
    ap.add_argument("--drop", type=int, default=1, help="index of the pose to remove (0 = front)")
    a = ap.parse_args()
    e = np.asarray(Image.open(a.guide).convert("L")) > 0
    H, W = e.shape
    poses = []
    for k in range(len(BOUNDS) - 1):
        if k == a.drop: continue
        p = np.zeros_like(e); p[:, BOUNDS[k]:BOUNDS[k + 1]] = e[:, BOUNDS[k]:BOUNDS[k + 1]]
        poses.append(p)
    spans = [np.nonzero(p.any(0))[0][[0, -1]] for p in poses]
    widths = [x1 - x0 + 1 for x0, x1 in spans]
    if len(poses) == 3:
        mid = (W - widths[1]) // 2
        starts = [(mid - widths[0]) // 2, mid, mid + widths[1] + (W - mid - widths[1] - widths[2]) // 2]
    else:
        gap = (W - sum(widths)) / (len(poses) + 1); starts = []; x = gap
        for w in widths: starts.append(int(round(x))); x += w + gap
    out = np.zeros_like(e)
    for p, (x0, x1), s, w in zip(poses, spans, starts, widths):
        out |= np.roll(p, s - x0, axis=1)
        print(f"pose at {x0}-{x1} -> {s}-{s + w - 1}")
    Image.fromarray((out * 255).astype(np.uint8)).save(a.out)


if __name__ == "__main__":
    main()
