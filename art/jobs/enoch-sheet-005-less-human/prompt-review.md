job: enoch-sheet-005-less-human
job-hash: df10dc0b22466e27
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh accepted job 3's symmetry but said Enoch reads as "too human". This job should make him read as a raccoon, with short paw-like hands, fur tufts at the shoulders, hips and cheeks, a softer silhouette and fewer muscle and rib lines. It should keep the four views, the symmetry, the face, the palette and the flat style of job 3's pick (seed 248).

## Will this job do it?
Mostly yes. This is a reasonable single-question test: "do animal and fur words plus a heavier redraw move the body away from human?"

- **Hands.** `(raccoon paws:1.2)` and `(paw-like hands with short stubby fingers:1.2)` are the words most likely to shorten the parent's long fingers with claw tips. "raccoon paws" is a strong tag for this checkpoint. The long phrase works mainly through "short fingers" and "stubby". Putting them in their own BREAK chunk is right, because it gives them a full 75-token chunk instead of a place at the end of the colour chunk.
- **Fur and silhouette.** `(fluffy fur:1.2)`, `(shoulder fur tufts:1.2)` and `fluffy cheek fur` match the style guide's shoulder-tuft rule, which the parent mostly lacks. They should break up the skin-tight outline. Leaving `hip fur tufts` at plain weight after round 1 is sensible against the square-torso rule.
- **Interior lines.** `minimal interior lines` and `simple shapes` are weak, non-tag phrases, and the checkpoint will largely ignore them. The redraw at 0.7 and `human, (human-like:1.2), human proportions, skin-tight` in the negative will do more to remove the rib, back-muscle and buttock lines seen in the parent and in job 3's 246/247.
- **Denoise 0.7.** This is justified. Job 3's outputs (246, 247, 248) are near-identical in hands and hips at 0.6, so 0.6 cannot reshape them. At 0.7 on a 2304x1152 parent with a clear four-figure layout, the layout and head size should mostly carry over.
- **Fixed seeds.** Seeds 231506246–249 are the same as job 3, so each output can be compared one-to-one with job 3's image of the same seed.
- **Model and LoRA.** The model is correct, `charsheet_lora_v1:0.6` is correct, and the trigger `charsheet` is present. `kind: character-sheet` matches a full multi-view sheet. The IP-Adapter is approved, and its weight (0.4, ending at 0.6) is unchanged from the parent's recipe.
- **Negative.** No body-part words were added, which follows the known-faults table on the censor mark.

## Risks and rule conflicts
- **No edge guide at 0.7.** Job 4 had no guide and showed this model's drift: heads at 0.139–0.178, extra face insets, gradient legs, nipples and abs, and a realistic style. The 0.7 img2img redraw keeps far more than job 4's free generation did, but some head shrink and some lost symmetry are possible. Measure the heads against 0.19–0.21.
- **Fluffy fur against flat style.** `(fluffy fur:1.2)` pulls against the negative's `detailed fur` and could add painted fur strokes or more interior lines, which is the opposite of the goal. `realistic` and `3d` in the negative should hold it back.
- **White on the back views is promoted by the positive.** `white countershading` is still in the positive. The parent and job 3's 246/247 have white hip wedges and a buttock cleft on both back views. The style guide's male back view is "all teal from neck to legs, no mint patch, flat back". The new wording does nothing to stop these marks, so the back views may stay "human" even if the hands improve. The marks were there before this job, so this is not a blocker.
- **Mark at the tail base.** The tailless back view in every job 3 output has a dark circular X mark at the tail base, which looks like the censor-mark fault. This job doesn't add body parts to the negative, so it shouldn't get worse. Nothing here removes it either.
- **`cel shading` against the flat-colour rule.** This is carried over from job 3 and follows Josh's shading request, so it's not new here.
- **Several changes at once.** Wording, negative and denoise all change together. All three serve the same goal, so the run still answers "less human, yes or no". It won't show which change did it.

## Must fix
none

## Could improve
1. **Clear the back views.** Add `(plain teal back:1.2), (all teal back view:1.1)` to the positive. This is the style guide's male back-view rule in plain words, so it stays out of the body-part negative. It would also help to move `white countershading` to `white chest` (`white belly` and `white muzzle` are already there). Expected effect: fewer white hip wedges and less buttock shape on both back views, and these are a large part of the "human" read.
2. **Keep the fur flat.** If the outputs show painted fur strokes, change `(fluffy fur:1.2)` to `fluffy fur` at plain weight and keep `(shoulder fur tufts:1.2)`. The tufts carry the silhouette change, and the general fur weight mostly adds texture lines.
3. **Back-off plan for denoise.** If the outputs lose the four-view layout or the heads fall below about 0.18, the next job should drop to 0.65 instead of adding a canny guide that locks the long fingers. This doesn't need to change before the run.
