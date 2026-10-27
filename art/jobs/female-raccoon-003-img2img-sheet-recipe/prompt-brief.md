job: female-raccoon-003-img2img-sheet-recipe
job-hash: 5107922f751eb76d

# Reason for the change

**What we're trying to change:** Redraw her approved sheet (baseline-highres.png) in Forge as a soft, furry cartoon raccoon with paw hands and a simple body instead of a chubby woman with a raccoon head, keeping her teal, navy and mint palette.

**Why this job should do it:** Four txt2img jobs failed because the model, LoRA and IP-Adapter bring a human body that body wording alone could not remove. Enoch's on-track jobs 003 and 005 instead used img2img from a sheet that already had the right body, at denoise 0.6-0.7, with the fur-and-paws chunk. Here the parent is her own reference sheet, so img2img at denoise 0.65 keeps her body shape, pose and palette as the starting point, and the redraw is strong enough for the prompt to change the fur and hands. Prompt (Enoch 005 structure in BREAK chunks): charsheet trigger plus style/layout; eyes chunk (red-brown eyes, black pupils, eyelashes); colours chunk (teal body 1.3, teal fur 1.2, navy mask, mint/pale-cyan countershading on muzzle, chest, belly and back-of-hips patch, white inner ears, navy gloves/socks/hands/lower legs); tail chunk (four navy rings, navy tip, not zigzag); Enoch's anti-human chunk unchanged ((fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines), which does the work against human hands and body detail; light build chunk (mild waist, soft rounded body, wider hips, featureless crotch) with no pin-up or curvy terms and no hourglass, since earlier curvy wording made the body more human. Negative: Enoch 005's with female, breasts, wide hips and hourglass removed and male added; keeps human, (human-like:1.2), human proportions, skin-tight, sketchy lines and the swatch/palette/head-study terms; no body-part words (censor-mark fault); plus the grey/cream/white-chest/purple/black-marking colour guards from female-rules.md. IP-Adapter: left out. The parent already carries her look and colours at denoise 0.65, and an IP-Adapter on the same image as the parent would mostly duplicate it while adding a second influence from the same source; Enoch's used a different image (v14) from the parent, which is not the case here. Leaving it out keeps this job to one change (img2img from her sheet). If colours drift, adding it at 0.4 ending at 0.6 is the next small job. No canny guide: it did not visibly shape her figures in earlier jobs, and img2img already holds the layout. Size 1536x1016 keeps the parent's aspect (3064x2024) as multiples of 8, within 8 GB VRAM. Fixed seeds 331506246-249, 4 images, no hires. Known trade-off: img2img keeps the parent's layout, which has four figures, colour swatches and a side bust. The negative (color swatch, color palette, close-up, head only, eye study) pushes against the swatches and bust, but the layout will mostly stay. This job is judged on body and colour, not layout.

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`
- `art/female-raccoon/female-rules.md`

# Images to look at
- parent: `art/female-raccoon/baseline-highres.png`
- earlier output of `female-raccoon-001-teal-colour-wording`: `art/jobs/female-raccoon-001-teal-colour-wording/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-teal-colour-wording`: `art/jobs/female-raccoon-001-teal-colour-wording/out/female-raccoon_20261028.png`
- earlier output of `female-raccoon-002-stocky-cartoon-body`: `art/jobs/female-raccoon-002-stocky-cartoon-body/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-002-stocky-cartoon-body`: `art/jobs/female-raccoon-002-stocky-cartoon-body/out/female-raccoon_20261028.png`

# Earlier jobs on this track
- `female-raccoon-001-baseline-ipadapter`: goal "A fresh female raccoon base-body sheet from Indigo Void (front, side, back on off-white) that keeps the look and palette of baseline-highres.png: teal fur, navy mask/sleeves/lower legs/four tail rings, mint chest and hip patch, hourglass build, digitigrade feet."; reviewer said partly; Josh's verdict off-track: Off-track; measured head 0.129-0.162, line 0.21-0.22%
- `female-raccoon-001-ipadapter-weight-wording`: goal "Same three-view sheet and seeds as female-raccoon-001-baseline-ipadapter, but with: teal #48C2C3 fur (not pale seafoam); a mint chest (not cream) and a mint hip patch, as in baseline-highres.png; navy that reads as blue #2A4365 (001's came out near-black/purple in all four); white inner ears; and no hourglasses, arrows, hooks, tiaras, devil tails, limb studies or logo tiles in the empty space."; reviewer said partly; Josh's verdict off-track: Off-track.; measured head 0.145-0.347, line 0.21-0.22%
- `female-raccoon-001-teal-colour-wording`: goal "Test colour wording (teal fur, pale-cyan chest/belly/muzzle/hip patch, navy blue markings) plus head size (0.19-0.21) and proportions from a canny edge guide on her own reference sheet."; reviewer said will help; Josh's verdict off-track: Body too human (lanky pin-up proportions, human buttocks/torso) vs the reference's stockier cartoon raccoon body; also fur overshot to sky blue, chest white, heads ~0.16, canny guide had little visible effect.; measured head 0.156-0.347, line 0.21-0.22%
- `female-raccoon-002-stocky-cartoon-body`: goal "Change only the body wording so her body matches the reference's stocky cartoon raccoon (big round head, thick (not short) limbs, simple soft torso, mild waist) instead of lanky human pin-up proportions, with the same seeds (20261027, 4 images)."; reviewer said will help; Josh's verdict off-track: Stocky/cartoon body wording made her a chubby human woman with a raccoon head (breasts, belly, human backside), not the reference's cartoon raccoon body; canny guide still not visibly shaping figures; censor mark on 20261027.; measured head 0.175-0.216, line 0.20-0.23%

# Earlier review rounds on this job
- none: this is the first review of this job

# The job, explained

# Forge job female-raccoon-003-img2img-sheet-recipe

**Asset:** female-raccoon | **Track:** female-baseline | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Redraw her approved sheet (baseline-highres.png) in Forge as a soft, furry cartoon raccoon with paw hands and a simple body instead of a chubby woman with a raccoon head, keeping her teal, navy and mint palette.

## Why this job should do it
Four txt2img jobs failed because the model, LoRA and IP-Adapter bring a human body that body wording alone could not remove. Enoch's on-track jobs 003 and 005 instead used img2img from a sheet that already had the right body, at denoise 0.6-0.7, with the fur-and-paws chunk. Here the parent is her own reference sheet, so img2img at denoise 0.65 keeps her body shape, pose and palette as the starting point, and the redraw is strong enough for the prompt to change the fur and hands. Prompt (Enoch 005 structure in BREAK chunks): charsheet trigger plus style/layout; eyes chunk (red-brown eyes, black pupils, eyelashes); colours chunk (teal body 1.3, teal fur 1.2, navy mask, mint/pale-cyan countershading on muzzle, chest, belly and back-of-hips patch, white inner ears, navy gloves/socks/hands/lower legs); tail chunk (four navy rings, navy tip, not zigzag); Enoch's anti-human chunk unchanged ((fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines), which does the work against human hands and body detail; light build chunk (mild waist, soft rounded body, wider hips, featureless crotch) with no pin-up or curvy terms and no hourglass, since earlier curvy wording made the body more human. Negative: Enoch 005's with female, breasts, wide hips and hourglass removed and male added; keeps human, (human-like:1.2), human proportions, skin-tight, sketchy lines and the swatch/palette/head-study terms; no body-part words (censor-mark fault); plus the grey/cream/white-chest/purple/black-marking colour guards from female-rules.md. IP-Adapter: left out. The parent already carries her look and colours at denoise 0.65, and an IP-Adapter on the same image as the parent would mostly duplicate it while adding a second influence from the same source; Enoch's used a different image (v14) from the parent, which is not the case here. Leaving it out keeps this job to one change (img2img from her sheet). If colours drift, adding it at 0.4 ending at 0.6 is the next small job. No canny guide: it did not visibly shape her figures in earlier jobs, and img2img already holds the layout. Size 1536x1016 keeps the parent's aspect (3064x2024) as multiples of 8, within 8 GB VRAM. Fixed seeds 331506246-249, 4 images, no hires. Known trade-off: img2img keeps the parent's layout, which has four figures, colour swatches and a side bust. The negative (color swatch, color palette, close-up, head only, eye study) pushes against the swatches and bust, but the layout will mostly stay. This job is judged on body and colour, not layout.

## What Forge will do
Redraw `art/female-raccoon/baseline-highres.png` 4 time(s). Denoise 0.65: a heavy redraw: only the rough layout carries over.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size 1536x1016
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 331506246, counting up per image

## Prompt

```
charsheet, masterpiece, best quality, newest, absurdres, safe, solo, female, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, digitigrade, simple background, white background, plain white background, flat color, cel shading, thick outlines
BREAK (red-brown eyes:1.2), black pupils, (large pupils:1.1), eyelashes, eye shine, white sclera, friendly smile, open smile
BREAK (teal body:1.3), (teal fur:1.2), (wide solid navy blue raccoon mask band across both eyes:1.3), (thin pale stripe above the mask:1.1), mint countershading, pale cyan muzzle, pale cyan chest, pale cyan belly, pale cyan patch across back of hips, white inner ears
BREAK gloves \(marking\), socks \(marking\), navy blue hands, navy blue lower legs, raccoon tail, ringed tail, big fluffy tail, (four navy blue tail rings:1.2), (navy blue tail tip:1.2), teal tail
BREAK (fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines
BREAK mild waist, soft rounded body, wider hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, male, child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, cream, white chest, black markings, purple, (many thin tail bands:1.3), (zigzag tail rings:1.2), props, objects, symbols, icons, extra drawings, human, (human-like:1.2), human proportions, skin-tight, sketchy lines
```

## Output
Images go to `art/jobs/female-raccoon-003-img2img-sheet-recipe/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: 5107922f751eb76d


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