job: enoch-sheet-012-shading-0.6
job-hash: 0dc37d57c9f37526
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh wants to retry shading before working on the head turn. The job keeps job 010 exactly as it was and lowers denoise from 0.7 to 0.6. The test is whether more of the locked 246 sheet carries over (the back-view head facing away, no invented goggles or straps) while the cel shading that 010 got without the charsheet LoRA survives.

## Will this job do it?
It is a clean one-variable test. I diffed it against the description of 010 in the brief. The prompt, the negative, the IP-Adapter (ip-adapter-plus_sdxl_vit-h, 0.25, ending at 0.5), the seeds 231506246–249, Euler a, 30 steps, CFG 6 and the lack of LoRA all match. Only `denoising_strength: 0.6` changes. 011's turn-away negatives are correctly left out, so 011's smaller heads (0.183–0.194) shouldn't come back. The 0.192–0.196 heads from 010 should hold, or move closer to the parent's 0.190–0.196.

- **Pose and objects:** lowering denoise is the right lever for this. The parent's third-view head faces cleanly away with no props (I viewed it). The 010 outputs I viewed show what goes wrong at 0.7. In seed 247 the back-with-tail head has turned into a three-quarter view and grown a dark goggle/strap. In seed 246 the head stays facing away. At 0.6 the sampler keeps more of the parent's large shapes, so both faults should drop. The `goggles, strap, eyewear on head` negatives from 010 still help.
- **Shading:** this is the real risk. The shading comes from `(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting`, with `flat colors` in the negative. In the 010 outputs I viewed (246, 247), the shading is already faint: almost flat fills with only light tone on the limbs and tail. The brief says the clear shading was in 248 and 249. At 0.6 less of the image is redrawn, so expect the shading to weaken, most on 246 and 247. The brief admits this. The result is useful either way: it tells us whether 0.6 without the LoRA can hold shading. That is what this job is meant to find out.
- The settings work in Forge: no weight is above 1.3, the prompt and negative don't conflict, the model is the approved one, and kind `character-sheet` without the charsheet LoRA has a stated, evidence-based reason (009 vs 008).

## Risks and rule conflicts
- Shading goes against the style guide's "Flat colours… no painted shading" rule, and `flat colors` is in the negative. Josh asked for this ("Lets add shading", and now "adding shading all over again"), so it's not a blocker, but the result is still a deviation from the guide that Josh chose.
- With Euler a, changing denoise changes both how many steps actually run (about 18 instead of 21) and the noise path. The same seed won't give a near-twin of 010, so the image-by-image comparison is rough. Seed 248's head may move for reasons unrelated to the denoise change.
- The parent's problems carry over and get stronger at lower denoise: five navy tail bands instead of four, a four-view layout instead of the rules' three, and the tailless back view's tail-base spot or hip wedge. This job doesn't try to fix any of them, which is fine for a one-change test. Don't read them as new faults.
- `smile` stays in the prompt, but the male rule asks for a calmer, flatter mouth. The parent's slight smile is accepted, so this isn't a new problem.
- No anatomy words in the negative, and the parent is img2img from a locked sheet, so none of the Warnings apply.

## Must fix
none

## Could improve
1. When you check the results, compare each image to its 010 twin for overall look only, not detail by detail: with Euler a, a denoise change moves the whole noise path. If the head-turn result is unclear, a later follow-up could run the same job with `sampler_name` set to a non-ancestral sampler. That's for after this job, not a change to it now.
2. If shading fades at 0.6 but the pose holds, the next single change should be the shading words (for example, `(cel shading:1.4)` or adding `hard shadows`) at 0.6, not going back to 0.7. Raising denoise again would bring the head turn and goggles back.
