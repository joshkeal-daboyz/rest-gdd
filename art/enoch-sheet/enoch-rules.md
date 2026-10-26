# Enoch: character rules

**Approved character sheet:** [enoch_character_sheet.png](enoch_character_sheet.png) (locked 2026-10-26). Every new image of Enoch should match it.

The rules shared by every raccoon, and how males and females differ, are in the [raccoon style guide](../raccoon-style-guide.md).

The rules for every image of Enoch. When an image breaks a rule, it gets regenerated, not patched. To change how he looks, change a rule here and its prompt fragment in [enoch.prompt.txt](enoch.prompt.txt) and [enoch.negative.txt](enoch.negative.txt), then regenerate.

How the approved sheet was made:
1. [enoch_pipeline.py](../tools/enoch_pipeline.py) with the prompt files and the square-torso edge guide [square_guide.png](square_guide.png) (made by [square_guide.py](../tools/square_guide.py)). Finishing (palette, outlines, chest and background) is automatic.
2. [color_eyes.py](../tools/color_eyes.py): her iris colour on the lower half of each pupil, plus a small shine.
3. [final_pass.py](../tools/final_pass.py): a Forge pass at double resolution and low strength, then a snap back to the palette.

These images are reference art. The final design is still the creative director's hand-drawn concept art (see [Art and audio](../../docs/08-art-audio.md)).

## Identity

- A young adult male raccoon, the tribe's best mechanic.
- Anthro: upright and humanoid, with usable hands, while keeping a raccoon's build, mask, and tail.

## Build

- Lean and wiry, slightly muscular: toned arms and chest, not bulky.
- Wide shoulders, narrow straight hips. No popping or swaying hips.
- **Square body:** from shoulders to hips the sides of the torso run in a mostly straight line. No pinched waist and no hourglass curve. This is the main thing that makes him read as male.
- **Shoulders as wide as the thighs:** the shoulders line up with the outer edge of the thighs, so one straight line runs from shoulder to knee. Widen the shoulders to get there; don't slim the thighs.
- Upright, rigid posture: squared shoulders, weight on both feet, arms straight at his sides.

## Proportions

An adult, with the same proportions as the female raccoon sheet. Measured on her front view, as a fraction of total height (ear tips to feet):

| Part | Ratio | Rough guide |
| --- | --- | --- |
| Head, including ears | 0.19 | About 5 heads tall |
| Ears | 0.07 | Small next to the head |
| Arm, shoulder to fingertips | 0.27 | Fingertips stop just above the crotch |
| Leg, crotch to floor | 0.46 | Nearly half his height |

Check a new image against these. Within ±0.02 counts as a match.

- **Height:** Enoch is slightly taller than the female raccoon, about 5%. Side by side, his eyes are level with the top of her head's mask band.

## Eyes

Same size and shape as generated: don't enlarge them. The pupil gets her red-brown `#8D3F4C` in its lower half, with the top staying black, as on her eyes. The finishing step adds this ([color_eyes.py](../tools/color_eyes.py)).

## Face

- Masculine, with a calm expression and a slight smile. Never angry or scowling.
- Side view: a true profile, with the mask band wrapping around the eye and a pointed white muzzle.

## Colors

Sampled from the high-res favourite sheet, [art/female-raccoon/baseline-highres.png](../female-raccoon/baseline-highres.png). That sheet sets the colours and the art style; Enoch is a male version of it.

| Part | Color |
| --- | --- |
| Fur | Teal `#48C2C3` |
| Mask, hands (to the wrist), lower legs (from mid-calf), tail rings and tip | Navy `#2A4365` |
| Muzzle, chest, belly | Mint `#D0FFFA` |
| Inner ears, eye whites | White |
| Iris crescent | Red-brown `#8D3F4C` |
| Line work | Near-black `#020304`, about 0.33% of figure height |
| Sheet background | Off-white `#FAF7EF` |

Sampled from flat areas of her sheet, not averaged over the whole image (averaging pulls in line work and makes the navy too dark).

## Markings and line work

- Navy on the legs starts halfway up the calf, just below the knee, with a short jagged fur edge. It covers about the bottom quarter of his height.
- Sleeves: the navy on his forearms starts with a zigzag fur edge (a female raccoon's sleeve edge is flat).
- Small spiky fur tufts stick out sideways where the neck meets each shoulder (front and back views), like hers.
- Outlines are about 0.33% of figure height, the same weight as hers (measured on the high-res sheet).

## Feet

- Digitigrade: he stands on his toes, with raccoon hind paws. Never flat feet.

## Tail

- Big and fluffy, about as long as his leg.
- **Exactly four navy rings, matching the female raccoon sheet.** The first ring sits at the base of the tail and the last one is the tip. The pattern from base to tip is navy, teal, navy, teal, navy, teal, navy tip.
- Rings are smooth, even bands, not zigzags.
- The same length and pattern in every view.

## Base body (unclothed sheet)

- No clothes and no accessories.
- A plain cartoon body with no anatomical detail.

## Sheet layout

- Four poses: front, three-quarter, side (facing left), back.
- One figure per pose, each clearly separated by empty space. Nothing overlaps.
- Plain light background. No text, color swatches, icons, or props.

## Review checklist

Check every image before it's used:

1. Calm face, slight smile, not angry.
2. Square body: sides straight from shoulders to hips, no waist, and shoulders as wide as the thighs.
3. Adult proportions: head about 0.19 of his height, short arms, long legs (see Proportions).
4. On his toes, not flat-footed.
5. Tail: four navy rings, from a navy base to a navy tip.
6. Colors match the table, and the sleeve edges are zigzag.
7. Nothing extra: no text, swatches, props, clothing, or anatomical detail.
8. Side view is a true profile.
