job: enoch-sheet-011-back-head-forward
job-hash: 1206859544f2c81a
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh marked job 010 on-track but said the third view (the back view with the tail) must not have its head turned. In seed 248 that head looks back over the shoulder. This job tries to fix that by adding only turned-head negatives, with everything else the same as 010.

## Will this job do it?
Probably, and it's a clean test. The only change is at the end of the negative: `(looking back:1.3), looking over shoulder, (head turned:1.2)`. `looking back` and `looking over shoulder` are the Danbooru tags this model links to "a face on a rear-view figure", so putting them in the negative pushes directly against the fault. Weights of 1.2–1.3 are well under the ~1.5 point where images break. The fixed seeds 231506246–249 match 010, so seed 248 is a direct twin and will show whether the wording alone fixes it. The positive is unchanged, so the shading Josh accepted in 010 (`cel shading:1.3` etc., no charsheet LoRA, denoise 0.7, IP-Adapter at 0.25 ending at 0.5) should carry over.

The drafter was right to leave out `profile` and `looking at viewer`. Both would fight the side view and the front view. `head turned` carries a small risk to the side-view profile. On this checkpoint it is usually read as the head turned *relative to the body*, which the side view doesn't have, so the risk is low.

From the images: the parent's two back views both face away cleanly, so denoise 0.7 is what lets the model invent the turn. The negative is the right lever without lowering denoise, which would cost the shading. The 010 seed-247 back-with-tail head is not quite "facing away with only a goggle piece", as the brief says. A navy mask edge and white cheek show on its left side, with eyewear over them, so it is a partial turn too (009 seed 247 looks the same). The new negatives should help 247 as well, and its eyewear may partly be the model drawing the mask as goggles. When judging the results, check 247's third head as well as 248's.

Head size is not a concern. 009 and 010 measured 0.186–0.197 and 0.192–0.196, and this job keeps the same parent and denoise.

## Risks and rule conflicts
- No rule breaks. The model is the approved Indigo Void. No LoRA on a `character-sheet` job is a stated, tested choice from job 009 (the LoRA blocked shading). IP-Adapter `ip-adapter-plus_sdxl_vit-h` is approved. There are no clothes, props or anatomy words in the negative.
- `head turned` could slightly stiffen or change the side view's head. Compare the side view of 248 with its 010 twin.
- Only one seed in four (248, plus 247 partly) showed the fault in 010. A clean result on all four is good evidence, but not proof that the fault can't come back on new seeds.
- The head-object faults in 247 and 249 (goggles, strap) are knowingly not addressed. They may persist, which is fine for this one-question job.

## Must fix
none

## Could improve
1. If 248's third head still turns, the next single-change job could add `facing away` to the positive, in the first chunk next to `rear view, back view`. That gives a positive pull towards the back of the head without touching the side view. Keep it out of this job so the negative-only test stays isolated.
