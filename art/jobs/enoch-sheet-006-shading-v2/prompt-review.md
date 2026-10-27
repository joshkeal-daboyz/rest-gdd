job: enoch-sheet-006-shading-v2
job-hash: 8e170171189672b3
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh asked for shading. This job adds hard-edged cel shading, with one shadow tone per colour, to job 005's seed-246 sheet, which Josh marked on-track. The paws, head size, symmetry, bold outlines, palette and plain white background should stay as they are. Josh is knowingly overriding the style guide's "flat colours, no shading" rule for this test.

## Will this job do it?
Mostly yes. The levers point the right way, and the parent already has what Josh wants to keep.

- **Prompt.** `flat color` is removed, which is the right call: on NoobAI-based checkpoints `flat color` is the main tag that keeps fills as single tones. `(cel shading:1.3)` sits in the first chunk, and that is the checkpoint's real tag for hard-edged, one-step shadow. The weight is safely below 1.5. `(simple shading:1.1)` is a weak, rarely used tag and will probably do little either way, but it does no harm. `thick outlines`, `simple shapes` and `minimal interior lines` don't fight cel shading, because cel shadows are tone shapes, not lines.
- **Negative.** `(painterly:1.2)`, `(gradient:1.1)` and `airbrush` are the right blocks for soft or painted shading. `(gradient:1.1)` also guards against the blurred teal-to-navy sleeve fades seen in job 004's seed 247. `charcoal grey` and the existing `(grey fur:1.3)` together cover the known fault where teal turns grey, which is exactly what a shadow tone on teal could slide into. `drop shadow` keeps the sticker-style shadow off the white background. Nothing in the negative blocks shading itself: `soft shading`, `shading` and `cast shadow` are correctly left out.
- **Denoise 0.45 on the 005/246 parent.** The parent has heads in range (0.190–0.196), paw hands, a symmetrical front and back, and lines of about 0.38%. At 0.45 the layout, the four views and the head size will hold, so no edge guide is needed. Job 004's head failure came from a txt2img-style redraw without a guide, and that doesn't apply here. The real risk is that 0.45 is on the low side for turning flat fills into shaded ones. The shadows may come out faint or appear on only some views. The brief states this risk and names the next step (raise the denoise), so that's acceptable for a first test.
- **IP-Adapter 0.2, ending at 0.6.** The v14 reference (viewed) is completely flat. Lowering its pull makes sense for a shading goal. At this denoise the parent carries the colours anyway, so little is lost. It is a second change made alongside the prompt change (see Could improve).
- **Seeds.** 231506246–249 are fixed and consecutive, starting from the seed that made the parent. That gives four variants of one wording change, which suits the job.
- **Model, LoRA and kind.** The model is Indigo Void, as required. `charsheet_lora_v1:0.6` with the `charsheet` trigger is correct, because this is a full four-view sheet and `kind` is `character-sheet`. The ControlNet model is on the approved list.
- **Size.** 4 images, no hires fix, no masks. That is small.

## Risks and rule conflicts
- Shading breaks the style guide's line "Flat colours … No gradients or painted shading" and checklist item 8 ("Clean, flat style"), and it adds tones that aren't in the palette table. The brief says Josh asked for this on purpose, and that the rules get updated only if he calls the job on-track. His verdict has to settle this, not this review.
- Navy shadows on the hands, lower legs, mask and tail rings may come out near-black, merge with the outlines and make the tail rings harder to read. Look for this in the outputs.
- At 0.45 the shading may be too faint to judge. If so, the result won't show whether the denoise or the halved IP-Adapter was the cause.
- The parent's tailless back view has a dark "X" spot at the tail base and a white wedge between the buttocks. Those read close to the known censor-mark fault and to anatomical detail. This job neither causes nor fixes them, and at 0.45 they will carry over. Josh should know they are still there.
- The parent's background is pure white, not the palette's off-white `#FAF7EF`, and the sheet has four views where the guide specifies three. Both were accepted on this track before this job, so neither is new here.

## Must fix
none

## Could improve
1. **IP-Adapter: change one thing at a time.** The job changes the prompt, the denoise and the IP-Adapter weight together. If you want the shading test cleaner, leave the IP-Adapter at job 005's 0.4. If you'd rather keep 0.2 (reasonable, since v14 is flat), note in `why` that a faint result means raising the denoise first and the IP-Adapter second. Then the next job knows which lever to try.
2. **A fallback if the shading is too faint (next job, not this one).** Raise `denoising_strength` to about 0.55, and/or add `(flat color:0.8)` to the negative to push actively away from flat fills. Don't go back to 0.6 or higher: job 001 showed that redraws the hands and faces.
3. **Optional wording.** `(simple shading:1.1)` adds little. To keep it to one shadow tone, `two-tone shading`, or a small boost on `(hard shadow:1.1)`, may read more clearly to this checkpoint. This is a minor point, and it's fine to leave as is for this test.
