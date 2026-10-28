job: enoch-sheet-010-shading-fix-faults
job-hash: 3e2d72ccedf34bf5
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh marked job 009 on-track for seed 231506249 but said "the faults not good". The aim is to keep 009's shading while removing the stray head and neck objects (headband, goggles, sunglasses, straps, collar) and the half-closed eyes. The only change is to the negative prompt.

## Will this job do it?
Mostly yes. It is set up as a clean A/B against 009:
- **Same settings as 009.** The positive prompt, model, LoRAs (none), denoise 0.7, IP-Adapter (0.25, ends at 0.5), parent, sampler, steps and CFG are all unchanged.
- **Same seeds.** Seeds 231506246–249 are fixed, so each image has a twin in 009. Any difference comes from the negative, which is what the job is testing.
- **The added negatives match the faults.** In the 009/247 and 008/247 images I viewed, there is a black band on the front head, a black visor or goggle with a strap on the tailed back view, a black collar on the tailless back, and smug half-lidded eyes. The negative now names each of these: `(headband:1.2)`, `(headwear:1.2)`, `eyewear`, `sunglasses`, `eyewear on head`, `goggles`, `goggles on head`, `strap`, `collar` and `(half-closed eyes:1.2)`. These are real booru tags that a NoobAI-based checkpoint like Indigo Void knows, so it should respond to them.
- **Weights are safe.** None is above 1.2.
- **No conflicts.** No added word conflicts with the positive prompt.
- **No body-part words.** Nothing added names a body part, so this should not set off the censor-mark fault.
- **The LoRA is correctly left off.** The charsheet LoRA is missing from a `character-sheet` job, but that has a stated reason: 009 showed that removing it was what let the shading through, and Josh marked that on-track.

**Main uncertainty: shading may not survive.** With Euler a at denoise 0.7, any change to the conditioning, including the negative, can shift the whole image, not just the head objects. 009's shading was marginal (248 and 249 only; 246 and 247 were flat), so the shading on the 249 twin may come out weaker or stronger. That is a fair result for this test, not a flaw in the job. I couldn't view the shaded 248 and 249 outputs because the brief lists only 009's 246 and 247, so I'm relying on the brief's description of them.

## Risks and rule conflicts
- **Heads stay slightly small.** 009 measured 0.186–0.197 (248: 0.186, 249: 0.188), and Josh's verdict note names "slightly small heads" as a fault. Nothing in this job targets head size, so expect the same again. 0.186–0.188 is inside Enoch's ±0.02 tolerance but below the style guide's 0.19–0.21. Leaving it for a later job keeps this one to a single change, which is fine, but Josh should know it is not being addressed.
- **Thin lines stay thin.** 248 measured 0.19% and 247 and 249 measured 0.27%, against a target of about 0.33%. This is left alone on purpose.
- **Tail rings are unchanged.** The tails still show 5–6 rings, not four, as in the locked 246 parent. This is a known track-wide issue and outside this job's goal.
- **Shading overrides the style guide.** The style guide's flat-colour rule is overridden for this track by Josh's request in job 002 ("Lets add shading."). That is not a rule break here.
- **A lower-back mark is already in the parent.** The locked parent and every output so far have a dark spot or "X" mark on the tailless back view. It is not caused by this job and not in its scope.
- **The tags may not match 248's face-shaped lump.** The grey animal-face lump on 248's head may not be read as `goggles` or `headwear`. The model may tag it as an animal hood or a headset instead, so it could survive these negatives.

## Must fix
none

## Could improve
1. **Add `headset, headphones, hood` to the negative.** These tags are generic, name no body parts, and are the likeliest names for the dark visor or earpiece in 008/247 and the face-shaped lump on 248. Expected effect: those shapes are more likely to disappear on the tailed back view. Leave out `mask on head`, because it shares the `mask` token with the positive's mask-band wording.
2. **Add `smug, bedroom eyes` to the negative.** The eyes in 008/247 and 009/247 have a smug, heavy-lidded look, which booru tags call `bedroom eyes` or `smug` more often than `half-closed eyes`. Expected effect: rounder, calmer eyes, as the "big, round, friendly eyes" rule asks.
3. **Plan the next job for heads and line weight.** Once this one settles which objects to remove, a follow-up job could target head size and line weight, for example a low-weight canny unit from the locked 246 sheet (`diffusion_pytorch_model_V2`), or `(thick outlines:1.3)`. That job should test one of these at a time, not both in this job.
