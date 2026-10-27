job: enoch-sheet-001-tail-rings
job-hash: 0d9d7f63f67cdcb0
assessment: partly

## Reason for the change, as I understood it
On the C2 candidate sheet, the side-view and back-view tails have 5-6 thin navy bands. They should have exactly four navy rings (navy base, teal, navy, teal, navy, teal, navy tip). The rest of the sheet should stay roughly as it is, though some face and eye drift is accepted for this test.

## Will this job do it?
The prompt changes point the right way. Dropping `striped tail` and `multicolored tail` removes the two tags most likely to produce many thin stripes on a NoobAI-based model. `ringed tail` at plain weight keeps the raccoon banding. `(dark navy ring at the tail base:1.2)` and `(dark navy tail tip:1.3)` pin both ends of the pattern, which the rule needs. Asking for "thick" rings and "wide" teal bands is the most useful lever, because the model can't count and wider bands fit fewer into the same tail. The "four" in `(four thick dark navy rings on tail:1.3)` will mostly be ignored, but the rest of the phrase still helps. The weights (1.2–1.3) are safe.

The weak point is the method, not the wording. Whole-sheet img2img at denoise 0.6 starts from a parent whose tails are high-contrast navy/teal stripes, each roughly 50–60 px tall. At this scale those stripes are coarse structure, and at 0.6 coarse structure usually survives. I expect some seeds to keep 5–6 bands, or to merge them into uneven, part-zigzag bands, rather than to land cleanly on four. Meanwhile 0.6 redraws everything else, including the brown eyes and the mask that C2 is valued for. The brief accepts that drift, but it is a high price for a test that is only judged on the tails.

The resolution adds risk. The job runs at 2304x1152 (about 2.65 MP) with no hires pass and denoise 0.6. A denoise of 0.6 is far heavier than a normal hires pass at that size, and SDXL is coherent at about 1 MP. Expect doubled or garbled small details (fingers, eyes, ear tufts), and it is tight on 8 GB VRAM.

The IP-Adapter (plus, ViT-H, 0.4, end 0.6) will carry v14's colours and flat style. It works from a 224 px CLIP view of the whole sheet, so it won't transfer a ring count. The brief's claim that "v14's four thick rings pull the same way" is overstated. The IP-Adapter is harmless, but don't count on it for the count.

Several things change at once compared with the parent. The tail wording changes, the 4-pose canny guide is dropped (the brief itself names it as the likely source of the extra rings), the LoRA goes from 0.5 to 0.6, and the job moves from txt2img+hires to img2img. If the rings improve, we won't know whether the wording or the dropped guide did it. The LoRA and guide changes are forced by the rules, so I accept them, but Josh should read the result with that in mind.

Model, LoRA, kind and trigger are all correct. Model is Indigo Void, `charsheet_lora_v1:0.6` with `charsheet` in the prompt, and the job is a real full-sheet `character-sheet`. The IP-Adapter model is on the approved list. The fixed seed counting up is right for a wording test.

## Risks and rule conflicts
- **Wrong tool for a local fix.** A count change confined to two tails is an inpaint job. Whole-sheet img2img at 0.6 risks keeping the old bands and also changing the eyes and face.
- **`(zigzag tail rings:1.2)` in the negative** can bleed onto the male zigzag sleeve edges and the jagged leg-fur edges, which the rules require. The parent's sleeves and leg edges are zigzag now, and this negative pushes against them.
- **Resolution:** 2304x1152 at denoise 0.6 without a hires step risks repeated or garbled details and uses a lot of VRAM on an 8 GB 3070.
- **Long fourth BREAK chunk:** with the tail phrases added it likely runs past 75 tokens, so Forge will split it and the tail words may end up in a chunk with the body words. This is a small risk.
- **Layout rule (question for Josh):** the parent and the prompt (`front view, side view, rear view, back view`) keep four views with two back views. The style guide and Enoch's rules ask for three views with one side view. The goal explicitly preserves this, so it is outside this job, but C2 doesn't meet the layout rule.
- **Anatomical detail (question for Josh):** the "tail-base spot" on the tailless back view, which the goal says to keep, reads as anatomical detail. That conflicts with "a plain cartoon body with no anatomical detail". It is also a by-product of the extra tailless view.
- **Palette, inherited from the parent and not this job's change:** the prompt asks for `white` belly and muzzle (the rule is mint `#D0FFFA`), `dark blue inner ears` (the rule is white), and a `white background` (the rule is off-white `#FAF7EF`). These are worth their own later job, not this one.
- The proportions, digitigrade feet, calm smile and absence of clothes or props in the parent all look fine. The job doesn't touch locked art: v14 is only the IP-Adapter reference.

## Recommendations
1. **Preferred: ask Josh for a tail mask** covering the side-view and back-view tails, then make this an inpaint (masked only, denoise about 0.8, same prompt, seeds and IP-Adapter). Effect: the tail bands are redrawn freely enough to change their count, and the eyes, mask and face of C2 are kept exactly. That answers the one question cleanly.
2. If Josh prefers to run whole-sheet img2img now, **set the output size to 1536x768** (Forge resizes the init itself) instead of the parent's 2304x1152. Effect: SDXL works near its native scale, so it is less likely to garble details and lighter on VRAM. Each tail band is also a smaller share of the image, so 0.6 redraws the pattern more readily. Upscaling can come in a later large job if this one is on-track.
3. **Remove `(zigzag tail rings:1.2)` from the negative.** Effect: no pressure against the required zigzag sleeve and leg-fur edges. "Thick", "wide" and `(many thin tail bands:1.3)` already do the tail work.
4. **Move the tail words into their own BREAK chunk**, placed after the body words: `BREAK big fluffy tail, ringed tail, (four thick dark navy rings on tail:1.3), (wide teal bands between the rings:1.2), (dark navy ring at the tail base:1.2), (dark navy tail tip:1.3)`. Effect: the tail phrases stay together in one chunk under 75 tokens and aren't split across a boundary.
5. Keep denoise at 0.6 for this run. Don't raise it as well, since that would add a second variable. If the bands survive, the next job should be the inpaint in (1), not a higher whole-sheet denoise.
6. Question for Josh, not for this job: should the C2 track keep its four-view layout and the tail-base spot, given the three-view and no-anatomical-detail rules?
