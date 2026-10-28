job: enoch-sheet-008-shading-wording
job-hash: 3abdc912d5e2f32d
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Jobs 006 (denoise 0.45) and 007 (0.55) returned the locked less-human 246 sheet almost unchanged and still flat. Josh wants visible anime cel shading: hard-edged shadow shapes, one shadow tone per colour. He also asked for img2img with the locked image as reference and said flat colours are getting in the way. This job removes the pressure toward flat fills and raises denoise so Forge can repaint them. Paws, heads, symmetry, the four views, the palette and the white background should stay.

## Will this job do it?
Probably yes, at least far more than 006/007. I looked at the parent and at 006/007 seeds 246/247. Those outputs are almost pixel-identical to the parent, apart from the paw pads drifting brown. At 0.45–0.55 the model was mostly cleaning up the parent's flat fills rather than repainting them, so the denoise was too low.

What should produce the change:
- **`denoising_strength` 0.55 → 0.7.** This is the main lever. Job 005 ran at 0.7 from a sheet and kept the four-view layout and heads at 0.190–0.196, so 0.7 can repaint fills without losing the layout. The style guide's own recipe for sheets is img2img at 0.6–0.7.
- **`(cel shading:1.3), (anime coloring:1.1)` plus `shaded, shadow, sidelighting`.** These are all real Danbooru-style tags that NoobAI-based checkpoints know. `sidelighting` gives the shadows a direction, which helps keep the one-tone shadow shapes consistent across the views.
- **`flat colors` in the negative, and `simple shapes, minimal interior lines` removed from the prompt.** These take away the pull toward flat fills. The weights are all ≤1.3, which is safe.
- **IP-Adapter on the locked image, 0.25, ending at 0.5.** It is low and stops early, so it holds identity and colour in the early steps but can't flatten the late detail steps where the shading is painted. That's sensible. 0.25 is a little under the usual 0.3 floor, but here a weak hold is the point.
- **Fixed seeds 231506246–249, the same as 007.** The results compare directly with 007.

What works against it, mildly:
- Removing `(gradient:1.1)` from the negative, while adding `flat colors` there and `shaded, shadow` to the prompt, lets the model answer with soft or gradient shading instead of hard cel shapes. `(cel shading:1.3)`, `(painterly:1.2)` and `airbrush` still guard against that, so this is not a blocker. But the goal is specifically *hard-edged* shading, and a gradient isn't the same thing as shadow, so the reason given for dropping `gradient` is weak.
- `(simple shading:1.1)` asks for less shading at the same time as `shaded`. It fits the one-tone goal, but it pulls slightly back toward minimal shading.

## Risks and rule conflicts
- The flat-colour rule in the style guide ("No gradients or painted shading") is broken on purpose, on Josh's explicit request. The brief says the rule and palette get updated if he calls this on-track. Accepted.
- The shadow tones add colours outside the palette by design. The real palette risk is that **teal shadow tones read as grey**. `(grey fur:1.3)` and `charcoal grey` stay in the negative, which is right. Check the shadowed teal in every image.
- At 0.7, job 005 gave stray marks on 2 of 4 images. Expect some here too.
- The generic word `shadow` may add a cast or floor shadow under the feet, which would break the plain white background. `drop shadow` in the negative covers only part of this.
- The 006/007 outputs show paw pads drifting brown. Nothing in this job targets that, and 0.7 may make it worse.
- The tailless back view in the parent already has the X-shaped mark on the lower back, the censor-mark fault. At 0.7 it will likely carry over or change. That's not this job's question, but don't mistake it for a new fault.
- The job changes four things at once: denoise, the prompt words, the negative and the IP-Adapter image. If shading appears, we won't know which change did it. This is defensible here: two single-lever jobs failed, and Josh asked for all of these directly. Just don't credit the result to the wording alone, even though the job is named "shading-wording".
- Model, LoRA (`charsheet_lora_v1:0.6` with the `charsheet` trigger, kind `character-sheet`) and ControlNet model are all approved and correct. The parent is the locked copy and is used read-only. No masks or guides are needed.

## Must fix
none

## Could improve
1. Put `(gradient:1.1)` back in the negative, or add `soft shading, gradient` at weight 1.0–1.1. Gradients are the failure mode most likely to replace flat fills when `flat colors` is negated, so this keeps the shadows hard-edged without bringing back any flat-fill pressure.
2. Add `(brown paw pads:1.2)` to the negative, or `navy paw pads` to the hands chunk, to stop the pad drift seen in 006/007 from getting worse at 0.7.
3. Add `floor shadow`, `cast shadow` to the negative so that `shadow` stays on the body and the white background stays plain.
4. If the results still come out flat, try `cfg_scale` 7 in the next job, with nothing else changed. That gives the shading tags more pull while the img2img parent holds the layout.
