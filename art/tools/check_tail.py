"""Check the tail rule: exactly four dark rings, the first at the base and the last at the tip.

Samples colours along the tail's centre line (from tail-paths.json, base to tip) and counts
the black sections.

usage:
  python check_tail.py <tail-paths.json> <pose> <image.png> [<image.png> ...]

Prints PASS or FAIL for each image, with the colour pattern it read (T = teal, B = black).
Exits with 1 if any image fails.
"""
import json, math, sys
from PIL import Image

DARK_MAX = 300   # R+G+B at or below this counts as black
MIN_RUN = 5      # ignore colour runs shorter than this many samples (anti-aliasing, fur tufts)
STEP = 2         # pixels between samples
RINGS = 4        # dark rings required (see art/enoch-sheet/enoch-rules.md)


def sample(img, segments):
    px = img.load(); out = []
    for seg in segments:
        for (x0, y0), (x1, y1) in zip(seg, seg[1:]):
            n = max(1, int(math.dist((x0, y0), (x1, y1)) / STEP))
            for i in range(n):
                x = round(x0 + (x1 - x0) * i / n); y = round(y0 + (y1 - y0) * i / n)
                out.append("B" if sum(px[x, y][:3]) <= DARK_MAX else "T")
        out.append("|")  # hidden part between segments
    return out


def pattern(samples):
    runs = []
    for s in samples:
        if s == "|":
            continue
        if runs and runs[-1][0] == s: runs[-1][1] += 1
        else: runs.append([s, 1])
    runs = [r for r in runs if r[1] >= MIN_RUN]
    merged = []
    for c, n in runs:
        if merged and merged[-1][0] == c: merged[-1][1] += n
        else: merged.append([c, n])
    return "".join(c for c, _ in merged)


def check(img_path, segments):
    p = pattern(sample(Image.open(img_path).convert("RGB"), segments))
    ok = p.count("B") == RINGS and p.startswith("B") and p.endswith("B")
    return ok, p


def main():
    paths = json.load(open(sys.argv[1], encoding="utf-8-sig"))
    segs = paths[sys.argv[2]]; failed = False
    for f in sys.argv[3:]:
        ok, p = check(f, segs)
        failed |= not ok
        print(("PASS" if ok else "FAIL"), p, f)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
