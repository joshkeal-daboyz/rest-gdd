job: enoch-sheet-013-back-head-inpaint
job-hash: a52573cce528c90e
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
In 010's on-track seed 248, the head in view 3 (back view with tail) is turned over the shoulder with the mask, eye and muzzle showing. Whole-image img2img either left the turn in place (011) or lost the shading (012). So this job inpaints only that head so it faces away like view 4, and leaves the shaded sheet around it untouched.

## Will this job do it?
Yes, very likely. Inpainting is the right tool here, and the settings fit the goal.

- **Mask.** On `mask-preview.png` the red ellipse runs from about x 1200 to 1533 and y 29 to 311 (original pixels). It covers the whole turned head: ears, muzzle tip at about x 1250, and the neck down to the shoulder line. It stays inside view 3 and touches neither view 2 nor view 4. A facing-away head is centred over the spine and is wider at the cheeks. 011 and 012 drew view 3's head that way at about x 1253 to 1483, with cheek fur down to about y 280, and the mask holds that shape with room to spare. It is centred at x 1368, about the body's centre line. The body, tail and shading are outside the mask, so they can't change.
- **Denoise 0.9 with fill 1 (original).** The pose has to change completely, from a profile face to the back of the head, so a high denoise is right. 0.9 still keeps the teal and the outline weight from the original pixels. The fallback the job names (fill 2) is sensible if a face survives.
- **Prompt.** The words that should turn the head are `rear view, back view, from behind, facing away, (back of head:1.3)`. All the eye, mask, smile and muzzle words from 010 are gone, which matters most here: 010's face chunk is what kept pulling a face into view 3. The shading words `(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, thick outlines` are carried over from 010, so the new head should match the shaded body.
- **Negative.** `(face:1.4), (eyes:1.3), (muzzle:1.3), (snout:1.3), nose, mouth, (looking back:1.3), looking over shoulder, (head turned:1.3), profile, three-quarter view, front view, (mask:1.2), raccoon mask` pushes directly against the current fault. None of these words appear in the prompt, so prompt and negative don't conflict. All weights are 1.4 or lower.
- **Inpaint settings.** `inpaint_full_res` at 1024 with 64 px padding draws the crop at roughly 2x, with the neck and shoulders as context. Mask blur 8 suits a seam at the neck.
- **Model and LoRA.** The model is the approved Indigo Void. The charsheet LoRA is left out on purpose. That matches 010 (on-track) and 009, where removing the LoRA is what made the shading appear. The job redraws only one head, not a full sheet, so leaving the LoRA out is right even though `kind` is character-sheet.
- **Seeds.** Four consecutive fixed seeds. For a pose fix, variety is useful, and only one image has to come out right.
- **No IP-Adapter.** The reason given is sound: the reference's front and side heads show faces.

## Risks and rule conflicts
- **Anatomy words in the negative.** The known-faults table ties these to the censor mark on the lower back. The why gives a real reason to keep them: the lower back is outside the mask, and every listed word names a part of the head. I accept that. The only remaining risk is a stray mark inside the masked shoulder area, which would show up in the check.
- **Ear colours.** `rounded ears with navy outer tips` doesn't match view 4 in the parent, whose ears from behind are teal with a white rim. The locked reference's back view also has teal ears with white inside. Navy tips could leave view 3's ears different from view 4's, and the check asks for them to match.
- **Grey fur.** `teal fur` is unweighted here, while 010 had `(teal fur:1.2)` and `(teal body:1.3)`. The surrounding teal and fill 1 should carry the colour, and `(grey fur:1.3)` is in the negative, but grey fur is a known fault.
- **Head size.** The mask is about 280 px tall and the head about 195 px, so at denoise 0.9 the new head could come out larger or smaller than view 4's (head ratio target 0.19 to 0.21). Measure it on the outputs.
- **Seam.** A head facing away has a wider neck and cheek-fur base than the narrow turned neck now at y 262 to 290. The mask reaches only just past the shoulder line, so check the join for a step in the outline.
- No palette, proportion, foot, tail or clothing rules are touched. Nothing locked is changed: the parent is a job output, not the locked sheet.

## Must fix
none

## Could improve
1. Change `rounded ears with navy outer tips and white inner rim` to `rounded teal ears with white rim` (or just `rounded ears`). Expected effect: the new ears match view 4 and the reference back view instead of growing navy tips.
2. Weight the teal: `(teal fur:1.2)` in place of plain `teal fur`, as in 010. Expected effect: less chance of a grey head at denoise 0.9, with no change to the pose wording.
