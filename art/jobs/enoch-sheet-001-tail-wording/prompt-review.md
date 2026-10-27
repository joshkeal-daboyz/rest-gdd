job: enoch-sheet-001-tail-wording
job-hash: f5c4e9868fe202dc
assessment: partly

## Reason for the change, as I understood it
Job 1 put gold finger rings on the hands in every image, turned the tailless back's tail-base spot into a grey disc or hollow ring, and gave ragged 5-6 band tails. This job changes only the tail wording and the negative. It aims to remove the jewelry and the disc and to get thicker, cleaner bands. It does not expect exactly four rings.

## Will this job do it?
**Gold finger rings: likely fixed.** I viewed job 1's 231506246 and 231506247 outputs. Both show small gold bands on the fingers of the back views. Neither the parent nor v14 has them, so the cause is almost certainly the positive phrases job 1 used: `four thick dark navy rings on tail`, `between the rings` and `ring at the tail base`. This job removes all three. It also adds `jewelry, (gold ring:1.2), finger ring, gold` to the negative. Either change alone would probably work, and together they are close to certain. The seed (231506246, counting up) is the same as job 1's, so it compares cleanly with job 1.

**Thicker, cleaner bands: plausible, but weakly driven.** The only new band words are `(thick tail stripes:1.2)`, plus `(dark blue tail tip:1.2)` and `teal tail`. Job 1 already asked for `four thick ... rings` at 1.3 and still drew ragged, zigzag-edged bands. The raggedness more likely comes from denoise 0.6 redrawing the parent's tail together with `big fluffy tail`, and those are unchanged. The parent's own bands are cleaner than job 1's. I expect bands about as clean as the parent's, a little wider, and still 5-6, which the brief accepts. The IP-Adapter on v14 (0.4, ending at 0.6) is the only input showing four thick bands, and it is unchanged. Its pull toward four is real but weak. `ringed tail` is a reasonable band tag. It does contain the "ring" stem, but `ringed tail` was also in job 1 and the hand rings are better explained by the loose "rings" phrases.

**Grey tail-base disc: not targeted.** The goal lists removing it, but no word addresses it, as the brief admits. In the parent (C2) the tailless back has a small solid navy spot. In job 1 it became a grey disc or open ring, most likely from `dark navy ring at the tail base`, so removing that phrase may restore it. This part of the goal is an observation, not a designed fix. That is the main reason for "partly".

**Size.** Both changes (positive tail wording and the jewelry negatives) aim at the same symptom, and Josh asked for exactly this pair in his job 1 verdict. If the jewelry goes, we won't know which change removed it. That is acceptable here because the aim is to remove it, not to explain it.

**Forge/SDXL settings.** The highest weight is 1.3, so no weight is near breaking. The model is Indigo Void. `charsheet_lora_v1:0.6` has its trigger, and kind `character-sheet` matches a full multi-view sheet. The ControlNet model is approved, and v14 is only used as a reference, so nothing locked is changed. There is no mask, which Josh chose.

## Risks and rule conflicts
- Bare `gold` in the negative may push the brown irises toward darker or less warm brown, because the model's amber and brown eye colours sit close to gold. The risk is small, since `(brown eyes:1.3)` is strong, but the eyes are the C2 feature Josh chose to keep.
- The negative now carries "ring" three times: `(gold ring:1.2)`, `finger ring` and the existing `(zigzag tail rings:1.2)`. This may slightly weaken tail banding overall. It would show as fewer or fainter bands, which is harmless here and could even help the count.
- The tail rule (exactly four navy rings, smooth bands) will still be broken. The brief expects this. Getting four will need the masked inpaint or a four-band guide from Josh, not more wording. Job 1 has already shown that wording at 1.3 doesn't move the count.
- The grey disc may persist because nothing targets it. If it does, the next job should handle it with a mask from Josh, not with more words.
- Parent rule drift carried over from C2, not introduced here: four views where the rules ask for three, a white crotch and buttocks patch on both back views, and navy that reads slightly purple in job 1's outputs. These are outside this job's question, but each output should be checked for them.
- No conflict with digitigrade feet, the calm expression, clothes or props, or locked art.

## Recommendations
1. Optional: remove the bare `gold` from the negative and keep `jewelry, (gold ring:1.2), finger ring`. Expected effect: the jewelry is still blocked, with less risk to the brown irises. If this would cost a revision round, run as written instead. The risk is minor.
2. No other changes. The job answers its question (do the jewelry and disc go away, and do the bands get thicker and cleaner, from wording alone?) and keeps job 1's seed and settings for a clean comparison. When judging outputs, count the bands on the side and back tails and look at the tailless back's tail-base spot. The likely next job is a tail-mask inpaint (a mask from Josh) to reach four rings.
