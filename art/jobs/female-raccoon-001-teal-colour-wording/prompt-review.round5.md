job: female-raccoon-001-teal-colour-wording
job-hash: 7452d2da09386494
assessment: partly

## Reason for the change, as I understood it
The last two jobs got the colours wrong in all outputs: the fur was a pale seafoam or sage, the chest cream or white, the markings near-black or purple, and the back of the hips had no mint patch. This job keeps the seeds and settings, changes only the colour words, and checks whether Forge then gives teal #48C2C3 fur, a mint/pale-cyan (#D0FFFA) chest, belly, muzzle and hip patch, and blue navy (#2A4365) markings. It also swaps the IP-Adapter reference to baseline.jpg.

## Will this job do it?
Partly. The chest and markings changes are well aimed. The fur and the hip patch are less certain.

- **Chest not cream.** Two changes work together here. `(pale cyan chest and belly:1.1)` replaces `pale mint belly`, and `(cream fur:1.2), beige` go in the negative. In the weight-wording outputs, "mint" next to `mint green` in the negative probably turned into cream. Naming the hue as "cyan" avoids that. This is the change most likely to show up.
- **Markings blue, not black.** All six marking terms now say `navy blue`, and the old `dark navy` is gone. "dark" was pulling the markings toward black, so dropping it is the right move. `(black fur:1.1)` and `purple` stay in the negative. The model has a strong habit of drawing raccoon markings black, though, and the mask, hands and lower legs are unweighted. Expect bluer markings, but they may still read as very dark slate. The female rules also ask for `black markings` in the negative, and it's missing (see recommendations).
- **Fur near #48C2C3.** `(teal fur:1.3), (turquoise fur:1.1)`, `(vivid colors:1.1)` and the kept `muted colors, desaturated, (green fur:1.2), mint green` all push the right way. Turquoise is a good second word, because it pulls away from the sage/green cast in the weight-wording outputs. One risk works against this: "pale cyan" now appears four times, and SDXL often lets colour words bleed across the whole figure. The fur could lighten toward the pale seafoam this job is meant to fix. Dropping `pastel colors` is right, because it was fighting the chest. I would not add it back, since that would only undo the last round. If the fur still comes out pale, the next lever is the chest wording (see recommendation 3), not the negative.
- **Hip patch in the back view.** `(pale cyan patch across back of hips:1.1)` describes the patch more exactly than "lower back". No earlier output I viewed had any patch, and 1.1 is a mild weight for a feature the model has never drawn. It may still not appear.
- **Seeds and settings.** Seed 20261027, CFG 6, Euler a, 30 steps, 1536x1024, IP-Adapter Plus at 0.8 and Balanced mode are all unchanged from the base job. That's correct for isolating a wording change.
- **Reference swap.** baseline.jpg is the same sheet as baseline-highres.png, at lower resolution and as a JPEG. I viewed both: same layout, same colours. IP-Adapter's CLIP-ViT-H encoder shrinks the image to 224 px in any case. This second change should matter very little, so I don't count it as a real confound.
- **Model and LoRA.** The model is the Indigo Void checkpoint. `charsheet_lora_v1:0.6` is on a `character-sheet` job asking for front, side and back views, with the trigger `charsheet` first in the prompt. All of this is approved and correct.

## Risks and rule conflicts
- "pale cyan" four times, next to the fur words, may lighten the body fur (colour bleed). This works against the fur goal.
- The female rules say to put `black markings` and `white chest` in the negative. Neither is there. The baseline job's chest came out pure white.
- The rules file still names baseline-highres.png as the IP-Adapter reference. The job uses baseline.jpg because Josh asked for it, so this is not a breach. The rules file is just out of date.
- The prompt runs past 75 tokens, and the colour words fall near the start of the second chunk. That's fine for attention, but a word near the boundary could get split. This is a minor risk.
- Rules: palette, digitigrade (`digitigrade legs`, `standing on toes`, `plantigrade` and `flat feet` in the negative), four tail rings with a navy tip, calm expression, and no clothes or props all check out. Nothing locked is touched.
- Past failures: the stray objects and reference leaks seen in both earlier jobs will probably appear again at 0.8. The brief says those aren't judged here, which is fair for a colour test.

## Recommendations
1. Add `(black markings:1.2), white chest` to the negative, as the female rules ask. Expected effect: markings pushed further toward blue, and no fall-back from cream to pure white on the chest. These are colour words only, so the job stays a single test.
2. Raise the face marking to `(navy blue raccoon mask markings:1.1)` so it matches the weighted tail and tip. Expected effect: a bluer mask, so the front view can be judged on the blue-versus-black question.
3. Optional. If Josh wants to guard the fur goal now instead of next round: reduce the pale-cyan bleed by naming it once as a contrast, e.g. `(pale cyan chest and belly:1.1)` and `pale cyan muzzle`, and changing the hip term to `(light cyan patch across back of hips:1.2)`. Expected effect: less pale wash on the body, and a stronger push for the hip patch that has never appeared. If Josh doesn't take this, run without it and judge fur lightness against chest colour on the outputs.
