job: enoch-sheet-003-symmetry
job-hash: 40cbe56f70f4eb5b
assessment: partly

## Reason for the change, as I understood it
Josh wants the front view, the back view with tail and the tailless back view of job 2's pick (seed 231506246) to be left-right symmetrical. That covers the hands, arms, shoulders, legs and feet, the white hip wedges and the tail-base spot. The tail itself is exempt, and the flat style must stay unchanged.

## Will this job do it?
Partly, and probably only a little. The job is valid and tests one thing: three symmetry tags in the positive prompt (`(symmetrical:1.2)`, `symmetry`, `(symmetrical pose:1.2)`), placed in the first chunk next to `standing, arms at sides`, plus `(asymmetrical:1.2), (asymmetrical pose:1.2), uneven body` in the negative. The weights are moderate. Nothing in the prompt works against the tags, and the model, LoRA and kind are correct. The generator is honest that the gain will be modest.

The problem is the method, not the wording. Look at the earlier outputs on this track: job 1's 231506246/247 and job 2's 231506246/247 against each other and against the parent. Whole-sheet img2img at denoise 0.6 with the same seeds kept almost every shape from its input. The hands, the arm angles, the lopsided hip wedges and where the tail sits all came back nearly unchanged in both jobs. Wording changed only small, local things (the gold rings went, the grey disc became a dark spot). So the claim that 0.6 "is high enough for the model to redraw hands and the hip wedges toward a symmetric shape" goes against what this track has already shown. Expect the same again: the init image will hold the lopsided hip wedges and hands, and the tags may nudge small details only.

Where it might help most: the tailless back (view 4). Its white wedge and cleft are small, local shapes that the model already draws as a mirrored motif, so a slight re-centring there is plausible. The front-view hands and the hip wedges in view 3, which sit beside the tail, are the least likely to change.

The fixed seeds 231506246–249 are a sound choice for comparing wording against job 2. Keep in mind that the parent is also different (job 2's pick, not C2), so this is not a pure A/B test.

## Risks and rule conflicts
- **The white hip wedges may break a rule in themselves.** The style guide's male back view is "All teal from neck to legs. No mint patch, and a flat back." The white wedges on both backs, with the cleft and the spot that has a mark inside, read as anatomical detail ("A plain cartoon body with no anatomical detail"). Making them symmetrical may polish something the rules say shouldn't be there. Josh should decide: keep and balance them, or remove them? Note the model's censor-mark fault. Adding body-part words to the negative to remove them would risk a censor mark, so that fix would need a mask or positive colour wording (for example "teal back, teal hips"), not anatomy negatives.
- **The tags could affect the side view and the tail, which the reason exempts.** `symmetrical`/`symmetrical pose` apply to the whole sheet, so the profile could be pulled slightly toward three-quarter or frontal, and the model might centre or hide the tail in the front view. Check view 2 for a true profile (Enoch checklist 8) and check that every view still has its tail.
- Re-running img2img on an img2img output adds drift with each pass: lines get fussier (the back views already have extra muscle lines) and colours shift slightly. This is small at one more pass. Watch the teal against `#48C2C3` and for any greying.
- The IP-Adapter reference (v14, weight 0.4, end 0.6) has its own lopsided back view with the tail off to one side. At this weight it mostly carries colour and style, so it's not a real conflict.
- No conflicts between prompt and negative, no weight above 1.2 on the new tags, and model and LoRA are approved and right for a `character-sheet` job. Palette, digitigrade feet, the calm face and the no-clothes rule are not affected by this change.
- No repeat of a past failure. The jewelry and grey-disc negatives from job 2 are kept.

## Recommendations
1. Run it as written if Josh wants a cheap test of whether the tags alone help. It answers one question cleanly. Set his expectations: on this track's evidence, 0.6 img2img changes little geometry, so most of the asymmetry will probably remain.
2. Don't raise the whole-sheet denoise to force it (for example to 0.7+). That would put the face, eyes and four-view layout at risk across the whole sheet just to move the hands and hips. The better next job is a masked inpaint: ask Josh for a mask over the front-view hands and both back views' hip area (leaving out the tail), then inpaint that region at denoise about 0.7–0.75 with these same tags. The model can then redraw those shapes while the face and layout stay protected. Expected effect: a much larger symmetry change where it's wanted.
3. Question for Josh before running: should the white hip wedges and the cleft on the back views exist at all? The style guide says a male back is all teal. If they should go, the job's goal changes from "balance them" to "remove them" (positive `teal back` style wording in a masked inpaint, not anatomy words in the negative). That would be a better use of the run than balancing them.
4. When judging the outputs, check view 2 is still a true profile and every view keeps its tail. Those are the side effects most likely to come from the global symmetry tags.
