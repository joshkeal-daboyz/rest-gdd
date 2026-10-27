# Enoch: character rules

**Approved character sheet:** [enoch_character_sheet.png](enoch_character_sheet.png) (v14, locked 2026-10-27; replaces the 2026-10-26 sheet). Every new image of Enoch should match it.

The rules shared by every raccoon, and how males and females differ, are in the [raccoon style guide](../raccoon-style-guide.md).

The rules for every image of Enoch. When an image breaks a rule, it gets regenerated, not patched by hand; the scripted fixes below are the only exceptions. To change how he looks, change a rule here and its prompt fragment in [enoch.prompt.txt](enoch.prompt.txt) and [enoch.negative.txt](enoch.negative.txt), then regenerate.

How the approved sheet (v14) was made:
1. [enoch_pipeline.py](../tools/enoch_pipeline.py) in Forge with the model `indigoVoidFurryFusedXL_noobaiV35_fp16` and the LoRA `charsheet_lora_v1` at 0.6 ([Civitai 2925755](https://civitai.com/models/2925755), trigger word `charsheet`), the prompt files [charsheet-toon.prompt.txt](charsheet-toon.prompt.txt) and [charsheet-toon.negative.txt](charsheet-toon.negative.txt), and the three-pose edge guide [shoulder_guide_3pose_v2.png](shoulder_guide_3pose_v2.png) (`--edges --weight 0.6 --end 0.6`). Seed 1480935357. Finishing (palette, outlines, chest and background) is automatic.
2. The guide comes from [fix_3pose_guide.py](../tools/fix_3pose_guide.py), which gives the side view an arm and a full tail and the back view a tail. Without the guide this model draws heads about 0.13 of his height and a realistic furry style.
3. [fix_tail_rings.py](../tools/fix_tail_rings.py) with [v14_fix.json](v14_fix.json): repaints the side and back tails to four navy rings and turns the light gap under his left arm into background. The front tail is left as generated: its fourth ring is at the base, hidden behind his body.
4. [fill_pupils.py](../tools/fill_pupils.py) with the same file: this model drew hollow pupils, so they're filled and coloured here. [color_eyes.py](../tools/color_eyes.py) does this for solid pupils, but on this sheet it took the nose for an eye.

This model sometimes draws a grey raccoon even when asked for teal; the palette step then turns him mint. Regenerate when that happens. Anatomy words in the negative prompt can make it draw a censor mark on the lower back.

These images are reference art. The final design is still the creative director's hand-drawn concept art (see [Art and audio](../../docs/08-art-audio.md)).

## Identity

- A young adult male raccoon, the tribe's best mechanic.
- Anthro: upright and humanoid, with usable hands, while keeping a raccoon's build, mask, and tail.

## Build

- Lean and wiry, slightly muscular: toned arms and chest, not bulky.
- Wide shoulders, narrow straight hips. No popping or swaying hips.
- **Square body:** from shoulders to hips the sides of the torso run in a mostly straight line. No pinched waist and no hourglass curve. This is the main thing that makes him read as male.
- **Shoulders nearly as wide as the thighs:** the sides run almost straight from shoulder to knee, easing out a little at the thighs. Widen the shoulders to get there; don't slim the thighs. Fully in line with the thighs was too wide; the guide ([square_guide.py](../tools/square_guide.py) `--preset shoulders`) sets them halfway between the original sheet and that.
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

Same size and shape as generated: don't enlarge them. The pupil gets her red-brown `#8D3F4C` in its lower half, with the top staying black, as on her eyes. The finishing step adds this ([color_eyes.py](../tools/color_eyes.py), or [fill_pupils.py](../tools/fill_pupils.py) when the pupils come out hollow).

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

- Three poses: front, side (facing left, with the tail showing), back. The side view sits in the centre of the sheet. A second side view without the tail was dropped: it repeated the same angle.
- One figure per pose, each clearly separated by empty space. Nothing overlaps.
- Plain light background. No text, color swatches, icons, or props.

## Review checklist

Check every image before it's used:

1. Calm face, slight smile, not angry.
2. Square body: sides straight from shoulders to hips, no waist, and shoulders nearly as wide as the thighs.
3. Adult proportions: head about 0.19 of his height, short arms, long legs (see Proportions).
4. On his toes, not flat-footed.
5. Tail: four navy rings, from a navy base to a navy tip.
6. Colors match the table, and the sleeve edges are zigzag.
7. Nothing extra: no text, swatches, props, clothing, or anatomical detail.
8. Side view is a true profile.
