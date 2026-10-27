job: female-raccoon-001-ipadapter-weight-wording
job-hash: 648832c8a3dee4fb
assessment: partly

## Reason for the change, as I understood it
Rerun 001's female three-view sheet on the same seeds and fix its two failures. The first is colour: pale seafoam fur, a cream chest, no hip patch, near-black/purple navy and dark inner ears, where the targets are teal #48C2C3, a mint chest and hip patch, blue navy #2A4365 and white inner ears. The second is clutter in the empty space: hourglasses, arrows, hooks, a tiara, devil tails, limb studies and logo tiles.

## Will this job do it?
I looked at all four 001 outputs, baseline-highres.png and Enoch's sheet. The brief describes 001 accurately, and the goal now names the navy and inner-ear failures too.

**Clutter: likely to work for the named objects, less sure for the studies.**
- Removing `(hourglass figure:1.2)` from the positive is the decisive fix. 001 drew a literal hourglass in 27, 29 and 30, and `(hourglass:1.3)` in the negative backs the fix up. I expect the hourglasses to be gone.
- Removing `(no clothes, no accessories:1.2)` and adding `accessories, jewelry, tiara` to the negative should take out the tiara in 27.
- `(devil tail:1.2)`, `(arrows:1.2)` and `logo` aim at exactly what appeared in 27, 29 and 30.
- `props, objects, symbols, icons` are vague tags, so they will do little, but they do no harm.
- The weaker part is the uncoloured outline figures and the paw, hand and tail studies in 28 and 30. These come from the charsheet LoRA's training sheets. Swapping `clean lineart` for `clean bold outlines` removes one cause, and `(sketches:1.2)` helps a little. But nothing in the negative names an uncoloured figure the way the Danbooru-trained model knows it (`monochrome`, `lineart`). Expect fewer studies, not none.

**Colour: right lever, with wording still pulling the wrong way.**
- Moving the IP-Adapter from 0.5 to 0.8 should give a large shift. ip-adapter-plus carries flat colour well. The CLIP-ViT-H crop of this 3:2 reference is mostly the middle back view, the swatches, the bust and half the front chest. So it carries saturated teal, blue navy and the mint hip patch strongly. I expect the fur to move clearly toward #48C2C3.
- Several prompt words still work against the goal, and the job leaves all of them unchanged:
  - **Navy.** Every navy word is `dark navy`: the mask, hands, lower legs and `(dark navy tail tip:1.3)`. On this model "dark" pushes navy toward near-black, which is exactly 001's failure. The IP-Adapter at 0.8 may override it, but this wording is the most likely reason the navy stays black-purple.
  - **Chest.** `pale mint belly` and `pale mint muzzle` explain the cream chest. "Pale" plus `plain off-white background` drifts to cream or white.
  - **Hip patch.** `(pale mint patch on lower back:1.1)` points at the wrong place. The guide and the reference put it across the back of the hips. The IP-Adapter may still bring it in from the middle figure.
- The brief now admits that dropping `lineart` is also a colour lever, and that Balanced mode does nothing to guard the layout. That is correct, and it means the colour result can't be credited to 0.8 alone.

**Setup.** The setup is correct:
- Model: Indigo Void.
- `kind: character-sheet`, which is right for a true three-view sheet.
- `charsheet_lora_v1:0.6`, with `charsheet` as the first token.
- The ControlNet model is approved.
- No weight is above 1.4.
- Fixed seeds 20261027–30, 4 images, no hires fix: a fair one-to-one comparison with 001.

The job bundles two changes, but they are judged on different parts of the image, and the brief states where the readouts overlap. That's acceptable for a small job.

## Risks and rule conflicts
- At 0.8 the reference may leak into the output: the swatch dots (including the off-palette yellow), the side bust, a fourth figure, or the oval mark on the right back view's hip. All of these sit inside the centre crop and break the palette and sheet-layout rules. Only `(color swatch:1.2)`, `(color palette:1.3)`, `bust` and `head studies` push against them.
- The `dark navy` wording (×5, one at 1.3) works against the goal's "navy reads as blue". If the navy is still black, it may be blamed on the weight when the wording is the cause.
- `(extra tails:1.2), (devil tail:1.2)` put "tail" in the negative. The risk is low, but if the main tail comes out smaller or thinner than in 001, suspect these first.
- `(hourglass:1.3)` in the negative might soften the waist a little. 001's waist was already very pinched, so the risk is low.
- Head size: about 0.13–0.15 of height in 001, against the 0.19–0.21 rule. It can't pass without a female edge guide from Josh. The job puts this out of scope.
- Nothing locked is touched. There are no anatomy words in the negative (censor-mark rule), and nothing unapproved is used.

## Recommendations
1. Add `monochrome, lineart, uncolored` to the negative, next to `(sketches:1.2)`. Expected effect: these are the Danbooru tags for 001's outline-only figures and line studies, so they target the leftover clutter more directly than `sketches`. This stays within the "stray objects" wording change, and `thick outlines, clean bold outlines` in the positive keep the outlines. Optional: the job can also run as written.
2. Keep the colour wording as it is for this job, so the change stays readable. But record the next colour levers now, in `why` under NOT TESTED: `dark navy` → `navy` (and `(navy tail tip:1.3)`), `pale mint` → `mint`, `(teal fur:1.2)` moved early in the prompt, and `(mint patch across back of hips:1.1)`. Expected effect: if the navy is still black or the chest still cream at 0.8, the next job knows the wording is the suspect, not the weight.
3. When judging the results: read a fourth figure, swatch dots, a bust or a yellow accent as the weight being too high (next try 0.65–0.7), not as a wording failure. Question for Josh, carried over from 001's review: would he supply a cleaner IP-Adapter reference, such as a square image of one figure, made in Forge or by hand? With one, the centre crop would see her face and front markings instead of the swatches and bust.
