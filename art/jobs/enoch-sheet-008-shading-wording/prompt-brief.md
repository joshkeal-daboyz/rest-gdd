job: enoch-sheet-008-shading-wording
job-hash: 3abdc912d5e2f32d

# Reason for the change

**What we're trying to change:** Get visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour) on the locked less-human 246 sheet by removing flat-colour wording and the flat v14 reference, adding shading words, and raising denoise to 0.7, while keeping its paws, heads, symmetry, four views, palette and plain white background.

**Why this job should do it:** Josh asked for shading ("Lets add shading.", "I would like you to apply anime style cell shading") and locked less-human 246 as the parent. He then said: "It sounds like flat colors is getting in way", "I think you should use img2img", "Use the new locked image as the reference". Shading overrides the style guide's flat-colour rule; the rule and palette get updated with shadow tones if he calls this job on-track. Jobs 006 (denoise 0.45) and 007 (0.55, plus anime coloring) both gave no visible shading: all eight images stayed flat, with only paw pads drifting browner. Likely causes: (a) flat-colour wording in the prompt and negative, and a flat v14 reference at IP-Adapter 0.2, held every fill flat; (b) denoise too low to repaint fills. Job 005 at denoise 0.7 showed that 0.7 kept the four-view layout and heads but 2 of 4 images had stray marks, so 0.7 carries that risk and the marks must be checked. Changes against job 007: (1) Parent is the locked copy art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png, img2img, no canny or edge map. (2) Denoise 0.55 to 0.7, enough to repaint fills with a shadow tone. (3) Prompt: adds 'shaded, shadow, sidelighting' after the shading tags to give the shadows a direction and a reason to exist; removes 'simple shapes, minimal interior lines' (they asked for fewer marks and so work against added shadow shapes); keeps '(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1)'. No flat-colour words are in the prompt. (4) Negative: adds 'flat colors' so the model avoids flat fills; removes '(gradient:1.1)' because it contradicts the shadow wording; keeps '(grey fur:1.3)', 'charcoal grey', '(painterly:1.2)', 'airbrush' and the rest so shadows stay hard-edged and teal does not go grey. (5) IP-Adapter ip-adapter-plus_sdxl_vit-h now uses the locked image as reference in place of v14, at weight 0.25, end 0.5. The reference carries the colours, paws and head so they don't drift at 0.7, but the locked image is flat too, so a low weight and early end (guidance stops at half the steps) leave the later steps free to add shadow tones. This is my choice of weight; it is lower than the 0.4 used before, and higher than 007's 0.2 since the reference is now the exact character rather than the old v14 sheet. Same as 007: seeds 231506246-249 (4 images), Euler a, 30 steps, CFG 6, charsheet_lora_v1 at 0.6, no hires. Check: shading, paws and heads, symmetry, four views, pupils and mask, grey teal, paw-pad drift and stray marks. No masks, guides or pixel edits.

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`
- `art/enoch-sheet/enoch-rules.md`

# Images to look at
- parent: `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png`
- ControlNet image: `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png`
- reference: `art/enoch-sheet/enoch_character_sheet.png`
- earlier output of `enoch-sheet-006-shading-v2`: `art/jobs/enoch-sheet-006-shading-v2/out/enoch-sheet_231506246.png`
- earlier output of `enoch-sheet-006-shading-v2`: `art/jobs/enoch-sheet-006-shading-v2/out/enoch-sheet_231506247.png`
- earlier output of `enoch-sheet-007-shading-v3`: `art/jobs/enoch-sheet-007-shading-v3/out/enoch-sheet_231506246.png`
- earlier output of `enoch-sheet-007-shading-v3`: `art/jobs/enoch-sheet-007-shading-v3/out/enoch-sheet_231506247.png`

# Earlier jobs on this track
- `enoch-sheet-001-tail-rings`: goal "On the C2 candidate sheet (eyetest/C2/enoch_231506246.png), the side-view and back-view tails show exactly four navy rings, navy at the base and a navy tip (navy, teal, navy, teal, navy, teal, navy tip), instead of 5-6 thin bands, while the four views, brown eyes with solid pupils, solid navy mask with white brow stripe, bright teal/navy, square lean build, smooth linework, white background and the tailless back view's tail-base spot stay as they are."; reviewer said partly; Josh's verdict off-track: Off-track. Draft job 2 with the reviewer's wording 1 and the jewelry negatives.; measured head 0.195-0.198, line 0.38-0.42%
- `enoch-sheet-001-tail-wording`: goal "On the C2 candidate sheet, remove the gold finger rings and grey tail-base disc that job 1 introduced, and get thicker, cleaner tail bands (ideally nearer four) on the side and back tails, by changing only the tail wording and the negative; the ring count is not expected to reach exactly four without a mask or guide."; reviewer said partly; Josh's verdict not run
- `enoch-sheet-002-shading`: goal "Josh asked for this in chat ("Lets add shading."), deliberately overriding the style guide's flat-colour rule: add hard-edged cartoon cel shading (one shadow tone per colour) to the generator's and Claude's pick from job 1 (seed 231506246; Josh has not confirmed it yet), keeping the outlines, palette, face and plain white background."; reviewer said partly; Josh's verdict not run
- `enoch-sheet-003-symmetry`: goal "In the front view, the back view with tail and the back view without tail, make the body left-right symmetrical (arms and hands, shoulders, legs and feet, and the white hip wedges and tail-base spot on the backs); the tail is exempt and the ring count is no longer a goal. The flat style stays as it is."; reviewer said partly; Josh's verdict on-track: Josh judged the views symmetrical; the remaining problem is that the body reads too human, which is the next job.
- `enoch-sheet-004-centred-tail`: goal "A new four-view sheet (front, side, back with tail, back without tail) in which the back view with tail has the tail hanging straight down the centre, so that view is left-right symmetrical; the front view and the tailless back are also symmetrical apart from the front view's tail. Keep the C2/246 look: brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade feet."; reviewer said partly; Josh's verdict off-track: No image centred the back tail; without a guide the sheets lost the 246 look, the four-view layout and the head size.; measured head 0.139-0.178, line 0.28-0.82%
- `enoch-sheet-005-less-human`: goal "Make Enoch read as a raccoon, not a human in a raccoon suit: paw-like hands with short fingers, fuller fur at the shoulders, hips and cheeks, a softer furry silhouette and fewer interior lines, while keeping the symmetry of the front and back views and what Josh likes (four views, brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade hind paws)."; reviewer said will help; Josh's verdict on-track: Josh called these the best images so far: paw hands, fewer muscle lines, heads in range; back views still read human.; measured head 0.190-0.196, line 0.38-0.38%
- `enoch-sheet-006-shading-v2`: goal "Add hard-edged cartoon cel shading (one shadow tone per colour) to enoch-sheet-005-less-human's seed 246 image (marked on-track by Josh), keeping its paws, heads, symmetry, bold outlines, palette and plain white background."; reviewer said will help; Josh's verdict off-track: No shading came through at denoise 0.45; Josh asked for a retry at 0.55.; measured head 0.192-0.194, line 0.38-0.38%
- `enoch-sheet-007-shading-v3`: goal "Get visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour, as in anime screencaps) on enoch-sheet-005-less-human's seed 246 image at denoise 0.55, keeping its paws, heads, symmetry, bold outlines, palette and plain white background."; reviewer said will help; Josh's verdict not run; measured head 0.187-0.197, line 0.38-0.38%

# Earlier review rounds on this job
- none: this is the first review of this job

# The job, explained

# Forge job enoch-sheet-008-shading-wording

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Get visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour) on the locked less-human 246 sheet by removing flat-colour wording and the flat v14 reference, adding shading words, and raising denoise to 0.7, while keeping its paws, heads, symmetry, four views, palette and plain white background.

## Why this job should do it
Josh asked for shading ("Lets add shading.", "I would like you to apply anime style cell shading") and locked less-human 246 as the parent. He then said: "It sounds like flat colors is getting in way", "I think you should use img2img", "Use the new locked image as the reference". Shading overrides the style guide's flat-colour rule; the rule and palette get updated with shadow tones if he calls this job on-track. Jobs 006 (denoise 0.45) and 007 (0.55, plus anime coloring) both gave no visible shading: all eight images stayed flat, with only paw pads drifting browner. Likely causes: (a) flat-colour wording in the prompt and negative, and a flat v14 reference at IP-Adapter 0.2, held every fill flat; (b) denoise too low to repaint fills. Job 005 at denoise 0.7 showed that 0.7 kept the four-view layout and heads but 2 of 4 images had stray marks, so 0.7 carries that risk and the marks must be checked. Changes against job 007: (1) Parent is the locked copy art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png, img2img, no canny or edge map. (2) Denoise 0.55 to 0.7, enough to repaint fills with a shadow tone. (3) Prompt: adds 'shaded, shadow, sidelighting' after the shading tags to give the shadows a direction and a reason to exist; removes 'simple shapes, minimal interior lines' (they asked for fewer marks and so work against added shadow shapes); keeps '(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1)'. No flat-colour words are in the prompt. (4) Negative: adds 'flat colors' so the model avoids flat fills; removes '(gradient:1.1)' because it contradicts the shadow wording; keeps '(grey fur:1.3)', 'charcoal grey', '(painterly:1.2)', 'airbrush' and the rest so shadows stay hard-edged and teal does not go grey. (5) IP-Adapter ip-adapter-plus_sdxl_vit-h now uses the locked image as reference in place of v14, at weight 0.25, end 0.5. The reference carries the colours, paws and head so they don't drift at 0.7, but the locked image is flat too, so a low weight and early end (guidance stops at half the steps) leave the later steps free to add shadow tones. This is my choice of weight; it is lower than the 0.4 used before, and higher than 007's 0.2 since the reference is now the exact character rather than the old v14 sheet. Same as 007: seeds 231506246-249 (4 images), Euler a, 30 steps, CFG 6, charsheet_lora_v1 at 0.6, no hires. Check: shading, paws and heads, symmetry, four views, pupils and mask, grey teal, paw-pad drift and stray marks. No masks, guides or pixel edits.

## What Forge will do
Redraw `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png` 4 time(s). Denoise 0.7: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.25, using `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png`. Reference image: the locked less-human 246 sheet, so colours, paws and head carry over; weight kept low because the locked image is flat-coloured and would pull the result back to flat.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-007-shading-v3`:
- added: `shaded`
- added: `shadow`
- added: `sidelighting`
- removed: `simple shapes`
- removed: `minimal interior lines`

```
charsheet, masterpiece, best quality, newest, absurdres, (cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, (symmetrical:1.2), symmetry, (symmetrical pose:1.2), digitigrade, simple background, white background, plain white background, thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail
BREAK (fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette
BREAK lean, broad shoulders, flat chest, narrow hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (asymmetrical:1.2), (asymmetrical pose:1.2), uneven body, human, (human-like:1.2), human proportions, skin-tight, sketchy lines, (painterly:1.2), airbrush, drop shadow, charcoal grey, flat colors
```

## Output
Images go to `art/jobs/enoch-sheet-008-shading-wording/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: 3abdc912d5e2f32d


# Settings a job can use

```
Top-level job fields: asset, compare_to, controlnet, count, follows, goal, hires, kind, loras, mask, mode, model, negative, parent, prompt, settings, track, upscale, why

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
```