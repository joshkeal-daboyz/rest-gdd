job: enoch-sheet-005-less-human
job-hash: df10dc0b22466e27

# Reason for the change

**What we're trying to change:** Make Enoch read as a raccoon, not a human in a raccoon suit: paw-like hands with short fingers, fuller fur at the shoulders, hips and cheeks, a softer furry silhouette and fewer interior lines, while keeping the symmetry of the front and back views and what Josh likes (four views, brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade hind paws).

**Why this job should do it:** Josh said job 3's images are symmetrical but 'too human'. Parent: job 3 seed 248 (art/jobs/enoch-sheet-003-symmetry/out/enoch-sheet_231506248.png), the pick from that job. What reads human in it: long-fingered hands with small claw tips, a buttock shape and dark cleft with white hip wedges on the back views, many muscle and rib lines on the chest and back, and body proportions like a person's. Changes (wording and denoise only; everything else is as in job 3: img2img of the parent at its own size, Euler a, 30 steps, CFG 6, seeds 231506246-249, charsheet_lora_v1 at 0.6, the same IP-Adapter ip-adapter-plus_sdxl_vit-h with enoch_sheet_v14.png at 0.4 ending at 0.6, and the symmetry tags, tail wording and jewelry negatives are kept): (1) Positive: a new BREAK chunk of animal and fur wording, '(fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines'. A chunk of its own gives these words full weight instead of leaving them at the end of the long colour chunk. They push the cues named in the goal: paws instead of long fingers, fur at the shoulders, hips and cheeks, a softer silhouette instead of skin-tight shape, and fewer interior lines (which are mostly the muscle and rib lines). The flat style words stay (flat color, cel shading, thick outlines) and the existing negative still has 'realistic, detailed fur', so the fluffy fur stays flat-coloured fur tufts, not painted fur. 'featureless crotch', 'digitigrade' and the tail wording are untouched. (2) Negative: job 3's negative plus 'human, (human-like:1.2), human proportions, skin-tight, sketchy lines'. These are general style terms. No body-part words are added, because the style guide's known-faults table says body parts in the negative can set off the censor mark on the lower back; the human hands, buttock shape and wedges are therefore fought only through the positive wording above. (3) Denoise 0.7 (job 3 used 0.6). Job 3 showed 0.6 keeps the parent's shapes and made almost no change to hands and hips; the hands, hip shape and interior line work are shape-level things, so they need a bigger redraw. 0.7 is a heavy redraw: the layout of the four views carries over, but outlines and fills are largely redrawn. The risks are the ones to judge: the front and back views may lose some of the symmetry job 3 reached, the face and the brown pupils may drift, and the tail bands may change (the tail is exempt and its band count is no longer a goal). The symmetry tags stay in the prompt to keep the sides matched. I did not go higher than 0.7 so the face, mask and four-view layout survive. Guide: not used. The cleared 4-pose guide's own hands and arms are not mirror images, and a canny guide would also lock the very long-fingered hand outlines and human body outline this job is meant to change, so it would work against the goal. No masks, no new guides, no pixel edits. Revision: the tuft wording is split into shoulder tufts at 1.2 and hip tufts at plain weight, so the hips are not widened (square-torso rule).

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`
- `art/enoch-sheet/enoch-rules.md`

# Images to look at
- parent: `art/jobs/enoch-sheet-003-symmetry/out/enoch-sheet_231506248.png`
- ControlNet image: `art/enoch-sheet/enoch_sheet_v14.png`
- reference: `art/enoch-sheet/enoch_character_sheet.png`
- earlier output of `enoch-sheet-003-symmetry`: `art/jobs/enoch-sheet-003-symmetry/out/enoch-sheet_231506246.png`
- earlier output of `enoch-sheet-003-symmetry`: `art/jobs/enoch-sheet-003-symmetry/out/enoch-sheet_231506247.png`
- earlier output of `enoch-sheet-004-centred-tail`: `art/jobs/enoch-sheet-004-centred-tail/out/enoch-sheet_231506246.png`
- earlier output of `enoch-sheet-004-centred-tail`: `art/jobs/enoch-sheet-004-centred-tail/out/enoch-sheet_231506247.png`

# Earlier jobs on this track
- `enoch-sheet-001-tail-rings`: goal "On the C2 candidate sheet (eyetest/C2/enoch_231506246.png), the side-view and back-view tails show exactly four navy rings, navy at the base and a navy tip (navy, teal, navy, teal, navy, teal, navy tip), instead of 5-6 thin bands, while the four views, brown eyes with solid pupils, solid navy mask with white brow stripe, bright teal/navy, square lean build, smooth linework, white background and the tailless back view's tail-base spot stay as they are."; reviewer said partly; Josh's verdict off-track: Off-track. Draft job 2 with the reviewer's wording 1 and the jewelry negatives.; measured head 0.195-0.198, line 0.38-0.42%
- `enoch-sheet-001-tail-wording`: goal "On the C2 candidate sheet, remove the gold finger rings and grey tail-base disc that job 1 introduced, and get thicker, cleaner tail bands (ideally nearer four) on the side and back tails, by changing only the tail wording and the negative; the ring count is not expected to reach exactly four without a mask or guide."; reviewer said partly; Josh's verdict not run
- `enoch-sheet-002-shading`: goal "Josh asked for this in chat ("Lets add shading."), deliberately overriding the style guide's flat-colour rule: add hard-edged cartoon cel shading (one shadow tone per colour) to the generator's and Claude's pick from job 1 (seed 231506246; Josh has not confirmed it yet), keeping the outlines, palette, face and plain white background."; reviewer said partly; Josh's verdict not run
- `enoch-sheet-003-symmetry`: goal "In the front view, the back view with tail and the back view without tail, make the body left-right symmetrical (arms and hands, shoulders, legs and feet, and the white hip wedges and tail-base spot on the backs); the tail is exempt and the ring count is no longer a goal. The flat style stays as it is."; reviewer said partly; Josh's verdict on-track: Josh judged the views symmetrical; the remaining problem is that the body reads too human, which is the next job.
- `enoch-sheet-004-centred-tail`: goal "A new four-view sheet (front, side, back with tail, back without tail) in which the back view with tail has the tail hanging straight down the centre, so that view is left-right symmetrical; the front view and the tailless back are also symmetrical apart from the front view's tail. Keep the C2/246 look: brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade feet."; reviewer said partly; Josh's verdict off-track: No image centred the back tail; without a guide the sheets lost the 246 look, the four-view layout and the head size.; measured head 0.139-0.178, line 0.28-0.82%

# Earlier review rounds on this job
This job has had 1 earlier review round(s); at most 3 before it goes to Josh. Earlier rounds' must-fix items were applied unless the response says otherwise. Don't reverse a change an earlier round asked for unless you say exactly why that round was wrong. Put only real blockers under Must fix; anything else is Could improve.

## Round 1: will help, must-fix 0; Claude's response not recorded
What it asked for:
none


# The job, explained

# Forge job enoch-sheet-005-less-human

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Make Enoch read as a raccoon, not a human in a raccoon suit: paw-like hands with short fingers, fuller fur at the shoulders, hips and cheeks, a softer furry silhouette and fewer interior lines, while keeping the symmetry of the front and back views and what Josh likes (four views, brown irises with solid pupils, solid navy mask with white brow stripe, bright teal and navy, white chest and belly, square lean build, smooth linework, plain white background, digitigrade hind paws).

## Why this job should do it
Josh said job 3's images are symmetrical but 'too human'. Parent: job 3 seed 248 (art/jobs/enoch-sheet-003-symmetry/out/enoch-sheet_231506248.png), the pick from that job. What reads human in it: long-fingered hands with small claw tips, a buttock shape and dark cleft with white hip wedges on the back views, many muscle and rib lines on the chest and back, and body proportions like a person's. Changes (wording and denoise only; everything else is as in job 3: img2img of the parent at its own size, Euler a, 30 steps, CFG 6, seeds 231506246-249, charsheet_lora_v1 at 0.6, the same IP-Adapter ip-adapter-plus_sdxl_vit-h with enoch_sheet_v14.png at 0.4 ending at 0.6, and the symmetry tags, tail wording and jewelry negatives are kept): (1) Positive: a new BREAK chunk of animal and fur wording, '(fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines'. A chunk of its own gives these words full weight instead of leaving them at the end of the long colour chunk. They push the cues named in the goal: paws instead of long fingers, fur at the shoulders, hips and cheeks, a softer silhouette instead of skin-tight shape, and fewer interior lines (which are mostly the muscle and rib lines). The flat style words stay (flat color, cel shading, thick outlines) and the existing negative still has 'realistic, detailed fur', so the fluffy fur stays flat-coloured fur tufts, not painted fur. 'featureless crotch', 'digitigrade' and the tail wording are untouched. (2) Negative: job 3's negative plus 'human, (human-like:1.2), human proportions, skin-tight, sketchy lines'. These are general style terms. No body-part words are added, because the style guide's known-faults table says body parts in the negative can set off the censor mark on the lower back; the human hands, buttock shape and wedges are therefore fought only through the positive wording above. (3) Denoise 0.7 (job 3 used 0.6). Job 3 showed 0.6 keeps the parent's shapes and made almost no change to hands and hips; the hands, hip shape and interior line work are shape-level things, so they need a bigger redraw. 0.7 is a heavy redraw: the layout of the four views carries over, but outlines and fills are largely redrawn. The risks are the ones to judge: the front and back views may lose some of the symmetry job 3 reached, the face and the brown pupils may drift, and the tail bands may change (the tail is exempt and its band count is no longer a goal). The symmetry tags stay in the prompt to keep the sides matched. I did not go higher than 0.7 so the face, mask and four-view layout survive. Guide: not used. The cleared 4-pose guide's own hands and arms are not mirror images, and a canny guide would also lock the very long-fingered hand outlines and human body outline this job is meant to change, so it would work against the goal. No masks, no new guides, no pixel edits. Revision: the tuft wording is split into shoulder tufts at 1.2 and hip tufts at plain weight, so the hips are not widened (square-torso rule).

## What Forge will do
Redraw `art/jobs/enoch-sheet-003-symmetry/out/enoch-sheet_231506248.png` 4 time(s). Denoise 0.7: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.4, using `art/enoch-sheet/enoch_sheet_v14.png`. Reference image, as in the parent's recipe: carries Enoch's colours and v14's four thick tail rings without copying v14's three-view layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-003-symmetry`:
- added: `BREAK (fluffy fur:1.2)`
- added: `(shoulder fur tufts:1.2)`
- added: `hip fur tufts`
- added: `fluffy cheek fur`
- added: `(raccoon paws:1.2)`
- added: `(paw-like hands with short stubby fingers:1.2)`
- added: `soft furry silhouette`
- added: `simple shapes`
- added: `minimal interior lines`
- added: `BREAK lean`
- removed: `lean`

```
charsheet, masterpiece, best quality, newest, absurdres, safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, (symmetrical:1.2), symmetry, (symmetrical pose:1.2), digitigrade, simple background, white background, plain white background, flat color, cel shading, thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail
BREAK (fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines
BREAK lean, broad shoulders, flat chest, narrow hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (asymmetrical:1.2), (asymmetrical pose:1.2), uneven body, human, (human-like:1.2), human proportions, skin-tight, sketchy lines
```

## Output
Images go to `art/jobs/enoch-sheet-005-less-human/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: df10dc0b22466e27


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