job: enoch-sheet-002-shading
job-hash: e9208f0853e64b12
assessment: partly

## Reason for the change, as I understood it
Josh asked to "add shading". On the job-1 pick (tail-wording seed 231506246), add hard-edged cartoon cel shading with one shadow tone per colour, and keep the outlines, palette, face and plain white background. This knowingly overrides the flat-colour rule.

## Will this job do it?
Mostly yes. The wording is aimed the right way:
- **Removing `flat color`** matters most. With it gone, nothing in the prompt asks for flat fill any more.
- **`(cel shading:1.3)`** is a real Danbooru/NoobAI tag for hard, one-step anime shadows. The weight is safe (below 1.5).
- **`(simple shading:1.1)`** is a weak tag, but it pushes the same way and does no harm.
- **Settings:** the same seed (231506246, counting up), denoise 0.6, sampler, steps and CFG as job 1. Each output can be compared directly with the job-1 image of the same seed.
- **Denoise 0.6:** jobs 001-tail-rings and 001-tail-wording show that this parent keeps its layout, face and linework well at 0.6. That should be enough to add shadow shapes to a flat parent.
- **Negatives:** `charcoal grey` matches the style guide's fix for the grey-fur fault. The jewelry negatives that removed job 1's gold rings are kept.

Four things weaken the job:
1. **It is not one change.** The brief says the job "changes only the shading wording", but it also lowers the IP-Adapter weight from 0.4 to 0.2. Both changes push toward more shading, so if shading appears we won't know which caused it. A weaker reference can also loosen colour and identity: v14 is what carries the teal/navy and the thick rings. That variable should be tested on its own.
2. **Negatives that work against the goal.** `(soft shading:1.2)` puts the concept "shading" in the negative at a higher weight than `(simple shading:1.1)` in the positive. This partly cancels what we are asking for. `cast shadow` also suppresses the shadows that cel shading is made of: under the chin, arm onto torso, tail onto leg. `drop shadow`, `simple background` and `plain white background` already keep the background clean.
3. **The shading words come last in a long first chunk.** The first BREAK chunk is about 80 tokens, so `(cel shading:1.3), (simple shading:1.1), thick outlines` likely spill into a small chunk of their own after the quality, view and background tags. They will still work, but placed earlier they get steadier attention.
4. **Nothing names the colour of the shadows.** On this model, shadow on teal can drift toward grey, and shadow on navy toward the near-black outline colour. The negatives `grey fur` and `charcoal grey` help. A positive hint would help more.

## Risks and rule conflicts
- Style guide "Flat colours… No gradients or painted shading" (Line and style, checklist 8) and the exact-palette rule (checklist 1) are broken on purpose. This is Josh's override and the brief records it. If he calls the job on-track, the rules must be updated.
- Grey-fur fault: shadow tones on teal may read as grey. Navy shadows may merge into the outlines and erase the zigzag sleeve edges and the leg fur edges.
- At 0.6 every seed redraws the whole sheet. Earlier jobs at this denoise brought back gold finger rings and a grey tail-base disc. The negatives that fixed this are kept, but check the hands and the back of the tailless view again.
- `cel shading` sometimes pulls NoobAI toward an anime-screenshot or semi-3D look. `3d` and `realistic` are in the negative, which should be enough.
- Process: the parent is "the generator's and Claude's pick" and Josh hasn't confirmed it. Confirm the parent with Josh when asking for approval.
- Inherited and outside this job's scope: four views instead of the rules' three, a pure white background instead of off-white `#FAF7EF`, and the tail ring count.
- Model, LoRA (`charsheet_lora_v1:0.6`, `charsheet` trigger, kind `character-sheet`) and IP-Adapter model are all on the approved list and correct.

## Recommendations
1. Put the IP-Adapter weight back to 0.4, as in job 1. The shading wording is then the only change, and each seed can be compared directly with job 1. If shading comes out too faint, test 0.2 in the next small job.
2. Remove `(soft shading:1.2)` from the negative. Change `(gradient:1.2)` to `(gradient:1.1), airbrush`. This keeps soft and blended shadows down without cancelling the positive "shading" tokens.
3. Remove `cast shadow` from the negative and keep `drop shadow`. The background is already protected, and cel shading needs shadows on the body.
4. Move `(cel shading:1.3), (simple shading:1.1)` to just after `absurdres` in the first chunk, so they don't spill into a fragment chunk at the end.
5. Optional, but best tested in its own job if 1–4 still give grey shadows: add `(darker teal shadows:1.1)` to the colour chunk after `(teal fur:1.2)`. This names the shadow colour and should keep shadows teal, not grey. If it goes into this job, the brief should say it does, and the job is no longer testing just the shading words.
