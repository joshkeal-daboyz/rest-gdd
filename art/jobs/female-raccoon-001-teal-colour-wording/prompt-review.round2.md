job: female-raccoon-001-teal-colour-wording
job-hash: e8378352924170bc
assessment: partly

## Reason for the change, as I understood it
The last two jobs gave pale seafoam/sage fur, a cream chest, near-black purple navy and extra things on the sheet (swatch dots, busts, head studies, limb studies). This job should move the colours toward teal #48C2C3, mint #D0FFFA and blue navy #2A4365, and stop the extra pieces, keeping the same seeds so the result can be compared with the weight-wording job.

## Will this job do it?
Partly. The colour wording is aimed well, but the job makes two changes and both of them affect colour, so a colour result won't show which change caused it.

**Colour.** `(teal fur:1.3)` placed early, with `(green fur:1.2), mint green` in the negative, goes straight at the sage/seafoam drift in the earlier outputs. Dropping the word "mint" makes sense: in weight-wording seed 20261028 the fur is clearly green. `(black fur:1.1), purple` in the negative and `navy blue raccoon mask markings` should push the markings from purple-black toward blue. But:
- The fur in all four earlier outputs I viewed is **pale and desaturated**, not only green. Nothing in the prompt asks for saturation, and `(pale cyan chest and belly:1.2)`, `pale cyan muzzle` and `(pale cyan patch across back of hips:1.1)` add three more "pale" colour words that can lighten the whole body.
- The IP-Adapter drop from 0.8 to 0.6 weakens the main thing carrying the reference's saturated teal and blue navy into the image. The brief's own test ("grey or pale means the 0.6 weight may be to blame") can't be read, because pale is the failure we already have, and pale could also come from the new "pale cyan" words. If the fur comes out pale again, there's no way to tell whether the wording or the weight caused it.
- `navy` is still the only blue word on the hands, lower legs, rings and tail tip. In the earlier runs this model drew "navy" as purple-black. One `navy blue` on the mask is a light push.

**Leaks.** The reference `baseline-highres.png` itself has a column of colour swatch dots, a cropped bust, and four figures. The leaks in the weight-wording job (a swatch row and a bust in 20261027, head studies in 20261028) match it closely, so they almost certainly come from the IP-Adapter, not the prompt. The pipeline sends units with "Crop and Resize", and the CLIP-ViT-H preprocessor works on a square crop. My expectation, which I haven't confirmed, is that the crop of this 3:2 sheet is centred on the middle: the swatches, the back view and the bust, with the front figure's face cut off. Lowering the weight to 0.6 is the right kind of lever, but it is tied to the colour test. `(color swatches:1.3)` alone is weak: `(color palette:1.3)` was already in the negative last time, and swatches still appeared at 0.8.

The other settings carry over unchanged: same model, LoRA, seeds, size, steps and CFG. A fixed seed is right for testing wording.

## Risks and rule conflicts
- **Two changes on one result (job size).** The IP weight change affects both leaks and colour. A pale or grey result can't be pinned on one cause.
- "pale cyan" ×3 at up to 1.2 may lighten the main fur, which is the failure we have now.
- A lower IP weight means less of the reference's look: expect more of the model's realistic-furry default (thin limbs, fur texture), less flat colour, and possibly greyer fur, a known fault of the model.
- The reference image contains the very items we want removed (swatches, a bust, a fourth figure). The negative prompt is fighting the reference.
- Small heads are expected, since there is no female edge guide. The brief already says so; not counted against this job.
- No conflicts with the palette, digitigrade, tail, expression or clothing rules in the prompt. The model, the charsheet LoRA at 0.6 with its trigger, `kind: character-sheet` and the IP-Adapter model are all on the approved list, and right for a three-view sheet.

## Recommendations
1. **Make this job test colour only: set the IP-Adapter weight back to 0.8.** Keep the colour wording changes and `(color swatches:1.3)`; the negative change barely affects colour. Expected effect: any change in fur, chest or navy colour, relative to the weight-wording outputs on the same seeds, can be traced to the wording. Test the leaks in the next job.
2. **Ask for saturation, not just a hue.** Add `(vivid colors:1.1)` after `flat colors`, and add `muted colors, desaturated, pastel colors` to the negative. Expected effect: fur moves from pastel seafoam toward the strong #48C2C3, and navy away from grey-black.
3. **Cut the pale bleed.** Lower `(pale cyan chest and belly:1.2)` to `1.1`, and change `pale cyan muzzle` to `white muzzle`. White is the actual colour of the reference's muzzle area, and inner ears are already white. Expected effect: fewer "pale" tokens pulling the body colour light, while the chest still differs from cream.
4. **Optional, part of the same colour lever:** replace `(turquoise fur:1.1)` with `(teal body:1.1)`, the e621 tag form this NoobAI-based checkpoint is more likely to have learned, and write the hands, legs and rings as `dark blue` instead of `navy` (for example `dark blue hands`, `dark blue lower legs`, `(four dark blue rings:1.1)`, `(dark blue tail tip:1.3)`). Expected effect: blue markings rather than purple-black. If you'd rather keep this job smaller, leave this for the next job.
5. **For the next (leak) job, not this one:** at IP weight 0.8, try `"guidance_start": 0.25` on the IP-Adapter unit instead of lowering the weight. The pipeline passes extra keys through to the unit. Expected effect: the reference shapes colour and style in the later steps but has less say over layout, so fewer copied swatches and busts, with less colour loss than weight 0.6.
6. **Question for Josh:** would he make a clean reference image (front, side and back only, no swatch dots, no bust, ideally close to square) for the IP-Adapter? The current sheet puts the swatches and bust right in the part the IP-Adapter likely sees. No prompt negative will fully beat that.
