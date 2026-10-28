job: enoch-sheet-013-back-head-inpaint
job-hash: a52573cce528c90e

# Reason for the change

**What we're trying to change:** Repaint only the head in view 3 (back view with tail) of 010's seed 248 so it faces away like view 4 (back of the head and ears, no face, muzzle or eye), keeping everything outside the mask exactly as it is.

**Why this job should do it:** Josh said: "I have given you permission to create masks, lets try and use inpaint to fix the problem with the side ways head". Job 010 (on-track) has good shading, but in seed 248 the head in view 3 (back view with tail) is turned over the shoulder with the mask and eye showing. Job 011 (turn-away negatives, img2img) did not fix it, and 012 (denoise 0.6) fixed the head but lost all the shading, so a whole-image redraw cannot do both. Inpainting only the head leaves the shading elsewhere unchanged. Parent: art/jobs/enoch-sheet-010-shading-fix-faults/out/enoch-sheet_231506248.png (2304x1152). Mask, made with forge_jobs.py mask: one ellipse centred (1368,170), radii 150x125, grown by 16 px, so about x 1202-1534, y 29-311 (about 2.9% of the sheet). Josh looked at the first mask preview (a 118x97 ellipse grown by 8) and said: "Its going to need to be larger". View 3's head spans about x 1253-1482, y 67-262, the narrowest neck is y 262 and the shoulders start around y 290, so this mask has generous margins beyond the ears, the top and the muzzle side, and reaches down over the neck onto the top of the shoulders so the new head can blend in. It stays in view 3: its right edge (x 1534) is well short of view 4's head (x 1744 and up) and its left edge (x 1202) is clear of view 2. Prompt (a plain string, written for the back of a head): 'rear view, back view, from behind, facing away, (back of head:1.3), teal fur, teal head fur, fur tufts, rounded ears with navy outer tips and white inner rim', plus the sheet's shading words '(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, thick outlines' and the white background, so the new head matches the shaded style; no eye, mask or smile words. Negative: '(face:1.4), (eyes:1.3), (muzzle:1.3), (snout:1.3), nose, mouth, (looking back:1.3), looking over shoulder, (head turned:1.3), profile, three-quarter view, front view, (mask:1.2), raccoon mask' against any face, plus 010's stray-object negatives (headband, headwear, eyewear, sunglasses, goggles, strap, collar), 'grey fur, charcoal grey', 'flat colors' and the general style negatives. The known-faults table warns against body-part words in the negative because of the lower-back censor mark; here every word names the head, and the lower back is outside the mask and so cannot change. Settings: inpaint, no charsheet LoRA (as in 010), seeds 231506246-249 over 4 images, Euler a, 30 steps, CFG 6. Denoise 0.9: a pose change (face turned to face away) needs most of the masked area to be redrawn, and 0.75-0.9 is the usual range; 0.9 still starts from the original, so the teal, outlines and neck join carry over. inpainting_fill is 1 (original); if a face survives, the next job can try fill 2 (latent noise). inpaint_full_res is on with 64 px of padding, so Forge draws the crop (a crop of head, neck and top of the shoulders) at 1024x1024 for detail and sees the neck and shoulders for context. Mask blur 8 softens the seam so the new head blends into the old neck. The IP-Adapter is left out on purpose: the locked reference's front and side heads show faces and could pull the new head to face forward. Everything outside the mask is kept as it is. Check: is the head facing away, with no face, muzzle or eye; do the ears, fur and outline match view 4's head; is the seam at the neck clean; is the rest of the sheet unchanged. No guides, no pixel edits.

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`
- `art/enoch-sheet/enoch-rules.md`

# Images to look at
- parent: `art/jobs/enoch-sheet-010-shading-fix-faults/out/enoch-sheet_231506248.png`
- mask (white = redrawn): `art/jobs/enoch-sheet-013-back-head-inpaint/mask.png`
- mask preview (the mask in red over the parent, with a pixel grid): `art/jobs/enoch-sheet-013-back-head-inpaint/mask-preview.png`
- reference: `art/enoch-sheet/enoch_character_sheet.png`
- earlier output of `enoch-sheet-011-back-head-forward`: `art/jobs/enoch-sheet-011-back-head-forward/out/enoch-sheet_231506246.png`
- earlier output of `enoch-sheet-011-back-head-forward`: `art/jobs/enoch-sheet-011-back-head-forward/out/enoch-sheet_231506247.png`
- earlier output of `enoch-sheet-012-shading-0.6`: `art/jobs/enoch-sheet-012-shading-0.6/out/enoch-sheet_231506246.png`
- earlier output of `enoch-sheet-012-shading-0.6`: `art/jobs/enoch-sheet-012-shading-0.6/out/enoch-sheet_231506247.png`

# Earlier jobs on this track
- `enoch-sheet-001-tail-rings`: goal "On the C2 candidate sheet (eyetest/C2/enoch_231506246.png), the side-view and back-view tails show exactly four navy rings, navy at the base and a navy tip (navy, teal, navy, teal, navy, teal, navy tip), instead of 5-6 thin bands, while the four views, brown eyes with solid pupils, solid navy mask with white brow stripe, bright teal/navy, square lean build, smooth linework, white background and the tailless back view's tail-base spot stay as they are."; reviewer said partly; Josh's verdict off-track: Off-track. Draft job 2 with the reviewer's wording 1 and the jewelry negatives.; measured head 0.195-0.198, line 0.38-0.42%
- `enoch-sheet-001-tail-wording`: goal "On the C2 candidate sheet, remove the gold finger rings and grey tail-base disc that job 1 introduced, and get thicker, cleaner tail bands (ideally nearer four) on the side and back tails, by changing only the tail wording and the negative; the ring count is not expected to reach exactly four without a mask or guide."; reviewer said partly; Josh's verdict not run
- `enoch-sheet-002-shading`: goal "Josh asked for this in chat ("Lets add shading."), deliberately overriding the style guide's flat-colour rule: add hard-edged cartoon cel shading (one shadow tone per colour) to the generator's and Claude's pick from job 1 (seed 231506246; Josh has not confirmed it yet), keeping the outlines, palette, face and plain white background."; reviewer said partly; Josh's verdict not run
- `enoch-sheet-003-symmetry`: goal "In the front view, the back view with tail and the back view without tail, make the body left-right symmetrical (arms and hands, shoulders, legs and feet, and the white hip wedges and tail-base spot on the backs); the tail is exempt and the ring count is no longer a goal. The flat style stays as it is."; reviewer said partly; Josh's verdict on-track: Josh judged the views symmetrical; the remaining problem is that the body reads too human, which is the next job.
- `enoch-sheet-004-centred-tail`: goal "A new four-view sheet (front, side, back with tail, back without tail) in which the back view with tail has the tail hanging straight down the centre, so that view is left-right symmetrical; the front view and the tailless back are also symmetrical apart from the front view's tail. Keep the C2/246 look: brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade feet."; reviewer said partly; Josh's verdict off-track: No image centred the back tail; without a guide the sheets lost the 246 look, the four-view layout and the head size.; measured head 0.139-0.178, line 0.28-0.82%
- `enoch-sheet-005-less-human`: goal "Make Enoch read as a raccoon, not a human in a raccoon suit: paw-like hands with short fingers, fuller fur at the shoulders, hips and cheeks, a softer furry silhouette and fewer interior lines, while keeping the symmetry of the front and back views and what Josh likes (four views, brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade hind paws)."; reviewer said will help; Josh's verdict on-track: Josh called these the best images so far: paw hands, fewer muscle lines, heads in range; back views still read human.; measured head 0.190-0.196, line 0.38-0.38%
- `enoch-sheet-006-shading-v2`: goal "Add hard-edged cartoon cel shading (one shadow tone per colour) to enoch-sheet-005-less-human's seed 246 image (marked on-track by Josh), keeping its paws, heads, symmetry, bold outlines, palette and plain white background."; reviewer said will help; Josh's verdict off-track: No shading came through at denoise 0.45; Josh asked for a retry at 0.55.; measured head 0.192-0.194, line 0.38-0.38%
- `enoch-sheet-007-shading-v3`: goal "Get visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour, as in anime screencaps) on enoch-sheet-005-less-human's seed 246 image at denoise 0.55, keeping its paws, heads, symmetry, bold outlines, palette and plain white background."; reviewer said will help; Josh's verdict off-track: Still flat at denoise 0.55 with anime coloring; no shading came through.; measured head 0.187-0.197, line 0.38-0.38%
- `enoch-sheet-008-shading-wording`: goal "Get visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour) on the locked less-human 246 sheet by removing flat-colour wording and the flat v14 reference, adding shading words, and raising denoise to 0.7, while keeping its paws, heads, symmetry, four views, palette and plain white background."; reviewer said will help; Josh's verdict off-track: Still flat at denoise 0.7 with shading wording and the locked image as reference; 3 of 4 grew stray objects.; measured head 0.191-0.200, line 0.27-0.38%
- `enoch-sheet-009-shading-no-lora`: goal "Test whether removing the charsheet LoRA lets visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour) appear on the locked less-human 246 sheet; this is the only change from job 008."; reviewer said will help; Josh's verdict on-track: Removing the charsheet LoRA gave the first shading (best: seed 231506249); faults to fix: sunglasses/straps on the head, half-closed eyes, slightly small heads.; measured head 0.186-0.197, line 0.19-0.38%
- `enoch-sheet-010-shading-fix-faults`: goal "Keep the shading that job 009 produced (seed 249 was on-track) and remove its faults: stray head objects (sunglasses, goggles, straps, headband, collar) and half-closed eyes, by adding fault negatives only."; reviewer said will help; Josh's verdict on-track: Eyes fixed, heads in range, shading kept in 248/249; 248's back view with tail has the head turned over the shoulder, to fix next.; measured head 0.192-0.196, line 0.27-0.38%
- `enoch-sheet-011-back-head-forward`: goal "Make the head on the back view with the tail (third view) face away like the other back view, instead of turning to look over the shoulder, by adding turned-head negatives only."; reviewer said will help; Josh's verdict off-track: Seed 248's back-view head still turned; turn-away negatives did not fix it, and three heads fell just under the size rule.; measured head 0.183-0.194, line 0.19-0.38%
- `enoch-sheet-012-shading-0.6`: goal "Keep the shading from job 010 while carrying more of the locked parent's pose (including the back-view head facing away) and fewer stray objects, by lowering denoise from 0.7 to 0.6; this is the only change."; reviewer said will help; Josh's verdict off-track: Denoise 0.6 fixed the head turn and stray objects but lost all the shading.; measured head 0.188-0.199, line 0.27-0.38%

# Earlier review rounds on this job
- none: this is the first review of this job

# The job, explained

# Forge job enoch-sheet-013-back-head-inpaint

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Repaint only the head in view 3 (back view with tail) of 010's seed 248 so it faces away like view 4 (back of the head and ears, no face, muzzle or eye), keeping everything outside the mask exactly as it is.

## Why this job should do it
Josh said: "I have given you permission to create masks, lets try and use inpaint to fix the problem with the side ways head". Job 010 (on-track) has good shading, but in seed 248 the head in view 3 (back view with tail) is turned over the shoulder with the mask and eye showing. Job 011 (turn-away negatives, img2img) did not fix it, and 012 (denoise 0.6) fixed the head but lost all the shading, so a whole-image redraw cannot do both. Inpainting only the head leaves the shading elsewhere unchanged. Parent: art/jobs/enoch-sheet-010-shading-fix-faults/out/enoch-sheet_231506248.png (2304x1152). Mask, made with forge_jobs.py mask: one ellipse centred (1368,170), radii 150x125, grown by 16 px, so about x 1202-1534, y 29-311 (about 2.9% of the sheet). Josh looked at the first mask preview (a 118x97 ellipse grown by 8) and said: "Its going to need to be larger". View 3's head spans about x 1253-1482, y 67-262, the narrowest neck is y 262 and the shoulders start around y 290, so this mask has generous margins beyond the ears, the top and the muzzle side, and reaches down over the neck onto the top of the shoulders so the new head can blend in. It stays in view 3: its right edge (x 1534) is well short of view 4's head (x 1744 and up) and its left edge (x 1202) is clear of view 2. Prompt (a plain string, written for the back of a head): 'rear view, back view, from behind, facing away, (back of head:1.3), teal fur, teal head fur, fur tufts, rounded ears with navy outer tips and white inner rim', plus the sheet's shading words '(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, thick outlines' and the white background, so the new head matches the shaded style; no eye, mask or smile words. Negative: '(face:1.4), (eyes:1.3), (muzzle:1.3), (snout:1.3), nose, mouth, (looking back:1.3), looking over shoulder, (head turned:1.3), profile, three-quarter view, front view, (mask:1.2), raccoon mask' against any face, plus 010's stray-object negatives (headband, headwear, eyewear, sunglasses, goggles, strap, collar), 'grey fur, charcoal grey', 'flat colors' and the general style negatives. The known-faults table warns against body-part words in the negative because of the lower-back censor mark; here every word names the head, and the lower back is outside the mask and so cannot change. Settings: inpaint, no charsheet LoRA (as in 010), seeds 231506246-249 over 4 images, Euler a, 30 steps, CFG 6. Denoise 0.9: a pose change (face turned to face away) needs most of the masked area to be redrawn, and 0.75-0.9 is the usual range; 0.9 still starts from the original, so the teal, outlines and neck join carry over. inpainting_fill is 1 (original); if a face survives, the next job can try fill 2 (latent noise). inpaint_full_res is on with 64 px of padding, so Forge draws the crop (a crop of head, neck and top of the shoulders) at 1024x1024 for detail and sees the neck and shoulders for context. Mask blur 8 softens the seam so the new head blends into the old neck. The IP-Adapter is left out on purpose: the locked reference's front and side heads show faces and could pull the new head to face forward. Everything outside the mask is kept as it is. Check: is the head facing away, with no face, muzzle or eye; do the ears, fur and outline match view 4's head; is the seam at the neck clean; is the rest of the sheet unchanged. No guides, no pixel edits.

## What Forge will do
Redraw only the white area of `art/jobs/enoch-sheet-013-back-head-inpaint/mask.png` on `art/jobs/enoch-sheet-010-shading-fix-faults/out/enoch-sheet_231506248.png`, 4 time(s). Everything outside the mask is kept. Denoise 0.9: close to a fresh image: very little of the parent survives.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: none
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size 1024x1024 (the masked area is drawn at this size)
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-010-shading-fix-faults`:
- added: `from behind`
- added: `facing away`
- added: `back of head`
- added: `(back of head:1.3)`
- added: `teal fur`
- added: `teal head fur`
- added: `fur tufts`
- added: `rounded ears with navy outer tips and white inner rim`
- removed: `male`
- removed: `multiple views`
- removed: `reference sheet`
- removed: `turnaround`
- removed: `front view`
- removed: `side view`
- removed: `full body`
- removed: `standing`
- removed: `arms at sides`
- removed: `(symmetrical:1.2)`
- removed: `symmetry`
- removed: `(symmetrical pose:1.2)`
- removed: `digitigrade`
- removed: `BREAK (brown eyes:1.3)`
- removed: `(red eyes:0.6)`
- removed: `black pupils`
- removed: `(large pupils:1.1)`
- removed: `eye shine`
- removed: `white sclera`
- removed: `BREAK (teal body:1.3)`
- removed: `(teal fur:1.2)`
- removed: `(wide solid dark navy raccoon mask band across both eyes:1.3)`
- removed: `(navy mask directly touching the eyes:1.2)`
- removed: `(thin white stripe above the mask:1.2)`
- removed: `smile`
- removed: `closed mouth`
- removed: `BREAK white countershading`
- removed: `white muzzle`
- removed: `white belly`
- removed: `dark blue inner ears`
- removed: `gloves \(marking\)`
- removed: `socks \(marking\)`
- removed: `dark blue hands`
- removed: `dark blue lower legs`
- removed: `raccoon tail`
- removed: `ringed tail`
- removed: `big fluffy tail`
- removed: `(thick tail stripes:1.2)`
- removed: `(dark blue tail tip:1.2)`
- removed: `teal tail`
- removed: `BREAK (fluffy fur:1.2)`
- removed: `(shoulder fur tufts:1.2)`
- removed: `hip fur tufts`
- removed: `fluffy cheek fur`
- removed: `(raccoon paws:1.2)`
- removed: `(paw-like hands with short stubby fingers:1.2)`
- removed: `soft furry silhouette`
- removed: `BREAK lean`
- removed: `broad shoulders`
- removed: `flat chest`
- removed: `narrow hips`
- removed: `featureless crotch`

```
masterpiece, best quality, newest, absurdres, safe, solo, anthro, furry, raccoon, rear view, back view, from behind, facing away, back of head, (back of head:1.3), teal fur, teal head fur, fur tufts, rounded ears with navy outer tips and white inner rim, (cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, thick outlines, simple background, white background, plain white background
```

Negative:
```
nsfw, worst quality, low quality, lowres, (text:1.3), watermark, signature, (face:1.4), (eyes:1.3), (muzzle:1.3), (snout:1.3), nose, mouth, (looking back:1.3), looking over shoulder, (head turned:1.3), profile, three-quarter view, front view, (mask:1.2), raccoon mask, (grey fur:1.3), charcoal grey, (headband:1.2), (headwear:1.2), eyewear, sunglasses, goggles, strap, collar, jewelry, (painterly:1.2), airbrush, flat colors, human, 3d, realistic
```

## Output
Images go to `art/jobs/enoch-sheet-013-back-head-inpaint/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: a52573cce528c90e


# Settings a job can use

```
Top-level job fields: asset, compare_to, controlnet, count, follows, goal, hires, kind, loras, mask, mask_shapes, mode, model, negative, parent, prompt, settings, track, upscale, why

settings:
  seed: -1 for random; a fixed number repeats an image (consecutive seeds per image)
  steps: sampling steps (default 30)
  cfg_scale: how strictly the prompt is followed (default 6)
  sampler_name: default Euler a
  scheduler: default Automatic
  width: txt2img size; for img2img/inpaint, the size Forge draws at (default: the parent's)
  height: as width
  denoising_strength: img2img/inpaint: 0 keeps the parent, 1 replaces it
  inpainting_fill: inpaint: 1 starts from the original (default), 0 fill, 2 latent noise, 3 latent nothing
  mask_blur: inpaint: soften the mask edge, in pixels (default 4)
  inpaint_full_res: inpaint: true draws only the masked area, at width x height
  inpaint_full_res_padding: inpaint with inpaint_full_res: pixels of context around the mask
  hr_denoise: hires fix: denoise of the second pass (default 0.35)
  hr_upscaler: hires fix: an approved upscaler (default the first approved)

controlnet (a list; one entry per unit):
  module: preprocessor: canny (edge guide from an image), None (image is already an edge map), CLIP-ViT-H (IPAdapter) (reference)
  model: an approved ControlNet model
  image: repo path of the guide or reference image
  weight: strength, about 0.3-1.0
  guidance_start: fraction of the steps where it starts (0-1, default 0)
  guidance_end: fraction of the steps where it stops (0-1, default 1)
  control_mode: Balanced | My prompt is more important | ControlNet is more important
  resize_mode: Crop and Resize (default) | Resize and Fill | Just Resize
  pixel_perfect: true (default) sizes the preprocessor to the image
  processor_res: preprocessor resolution, when pixel_perfect is false
  threshold_a: canny low threshold
  threshold_b: canny high threshold
  purpose: plain words: what this unit is for (shown in explain.md, not sent to Forge)

upscale (upscale mode): scale, upscaler
hires: a number such as 1.5 turns on hires fix (large job)
mask, mask_shapes: written by `mask <job> --ellipse cx,cy,rx,ry | --rect x0,y0,x1,y1 | --poly "x,y x,y x,y" [--grow px]`
```