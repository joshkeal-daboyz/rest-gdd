job: enoch-sheet-004-centred-tail
job-hash: 0ffa9d9c61fcae4c
assessment: partly

## Reason for the change, as I understood it
Josh wants a four-view Enoch sheet whose back view (with tail) has the tail hanging straight down the middle, so that view is symmetrical. The C2/246 look stays as it is: brown eyes with solid pupils, navy mask with white brow stripe, bright teal/navy, white chest, flat smooth lines, digitigrade feet. img2img can't move the tail, so this is a fresh txt2img.

## Will this job do it?
Switching to txt2img is the right call. In all four earlier outputs I viewed (001-tail-wording 246/247, 003-symmetry 246/247), the back-view tail runs from the hip out to the lower right, exactly as in the parent. No img2img prompt change at a look-keeping denoise was going to move it. Dropping the 4-pose canny guide is also right for the tail, because its back-view tail is swept to the side as well.

The words meant to do the work are in their own BREAK chunk: `(tail down:1.2)`, `(straight tail:1.1)`, `(symmetrical rear view:1.2)`, plus `(curled tail:1.1), tail wrapped around leg` in the negative. `tail down` is a real booru-style tag that NoobAI-based checkpoints know, and it does the most here. `straight tail` is weak but harmless. `symmetrical rear view` isn't a tag; the model will mostly read it as more `symmetrical`, which the first chunk already has at 1.2. All weights are 1.3 or below, and nothing in the prompt contradicts the negative. Euler a with four counting-up seeds gives the variety needed to see whether the model ever centres the tail. That suits a probe, though the fixed seed buys no comparison with jobs 1–3, because the mode is different.

The main thing pulling against the goal is the IP-Adapter reference. Its back-view tail sweeps right, and ip-adapter-plus carries some composition as well as style. Starting at 0.2 (step 6 of 30) at weight 0.45 is a reasonable compromise: the coarse pose is mostly set before it starts. It can still bend the tail sideways in steps 6–18, though. I'd expect some, not all, of the four to centre the tail, which matches the author's own expectation.

What this job will almost certainly not do is give a sheet Josh can use. With no edge guide, the style guide's known fault applies: heads about 0.13 of height against the 0.19–0.21 rule, and a drift toward a realistic furry style. Jobs 1–3 kept heads at 0.195–0.198 only because the img2img parent carried them. The brief admits this. The IP-Adapter at 0.45 won't fix head size; the style guide says a prompt or reference alone doesn't. So the job answers "can txt2img centre the tail?" but not "give me a centred-tail sheet in the C2 look".

## Risks and rule conflicts
- **Head size (rule: 0.19–0.21).** Expect about 0.13 without a guide. This repeats a known failure, and nothing in the job addresses it. The outputs are a probe, not candidates.
- **Four views aren't guaranteed.** Nothing in the prompt asks for a second back view without a tail. `front view, side view, rear view, back view` and the reference layout may give four, but the model may also draw three, or two back views that both have tails. Check the layout before judging the tail.
- **Several changes at once:** img2img to txt2img, a new IP reference and start step, the tail chunk, new negatives, and no guide. If the look drifts (grey fur, small heads, realistic style), you can't tell which change caused it. For the tail question alone this is acceptable, because the mode change is the point.
- **The reference can pull the tail sideways** after step 6, as described above.
- **`(curled tail:1.1)` is global.** It may straighten the side-view tail's natural curve slightly. That's minor and probably harmless.
- **Inherited, not new:** `cel shading` sits beside `flat color`. Earlier outputs stayed flat, so it's low risk. The white hip wedges on the back views are an open item from job 3, and this job doesn't address them.
- Model, LoRA (`charsheet_lora_v1:0.6`, trigger present, kind `character-sheet` correct for a full sheet) and ControlNet model are all on the approved list. No clothes or props are requested, and nothing locked is touched.

## Recommendations
none: run as written, as a probe of whether txt2img can centre the back-view tail. Treat the outputs as layout evidence, not as sheet candidates. Two follow-ups:
1. If most of the four still sweep the tail sideways, change only `controlnet[0].guidance_start` from 0.2 to 0.3 in the next job. The reference then joins after the pose is fixed, which should help centre the tail at a small cost to the look.
2. Question for Josh, not a change I can make: a lasting fix for both the centred tail and the head size needs a symmetrical four-pose canny guide (`diffusion_pytorch_model_V2`), with the back-view tail hanging straight down the centre and few tail band lines. Only Josh makes guides. With one, the next job could run canny at about 0.6, ending at 0.6, as in Enoch's rules, and heads should return to about 0.19–0.21.
