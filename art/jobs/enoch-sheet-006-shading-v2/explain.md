# Forge job enoch-sheet-006-shading-v2

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Add hard-edged cartoon cel shading (one shadow tone per colour) to enoch-sheet-005-less-human's seed 246 image (marked on-track by Josh), keeping its paws, heads, symmetry, bold outlines, palette and plain white background.

## Why this job should do it
Josh asked for shading in chat ("Lets add shading.", then "Yes shading" for this candidate). He is deliberately overriding the style guide's flat-colour rule; the rule and palette get updated with shadow tones if he calls this job on-track. Parent: art/jobs/enoch-sheet-005-less-human/out/enoch-sheet_231506246.png, which Josh marked on-track ('I think these are the best images so far') and which is a candidate. Base: job 005's prompt and negative, including its paw and fur chunk, so only the shading differs. (1) Prompt: 'flat color' and the old 'cel shading' are removed (flat-colour words fight shading), and '(cel shading:1.3), (simple shading:1.1)' goes early in the first chunk, right after the quality tags, where it carries most weight. 'cel shading' is the model's tag for hard-edged one-step shadow; 'simple shading' keeps it to a single shadow tone. 'thick outlines' stays. (2) Negative: adds '(painterly:1.2), (gradient:1.1), airbrush' to block soft or painted rendering, 'drop shadow' to keep shadows off the white background, and 'charcoal grey' to stop grey shadow tones on the fur. 'soft shading' and 'cast shadow' are deliberately NOT added. (3) Denoise 0.45 (job 005 used 0.7). Shading is a surface change: it needs to repaint fills with a darker tone but not redraw shapes. 0.45 should keep job 005's paws, heads, symmetry and tail while still letting Forge add shadow regions; 0.6 (job 1) redrew hands and faces too much, and below about 0.35 the shadows may not appear. Risk: too little shading shows at 0.45; the next job could raise it. (4) IP-Adapter weight 0.2, end 0.6 (was 0.4). The v14 reference is flat-coloured, so a strong reference would wash the shading out and pull the image back to flat colour. Two views: the previous reviewer (job 002) wanted to keep 0.4 so the job tests one change only; I chose 0.2 because the shading would be pulled away otherwise. Josh hasn't ruled on this. Everything else is as in job 005: img2img at the parent's size, Euler a, 30 steps, CFG 6, seeds 231506246-249, charsheet_lora_v1 at 0.6, symmetry tags, tail wording and jewelry negatives. Small job, 4 images, no hires, no masks, no guides, no pixel edits.

## What Forge will do
Redraw `art/jobs/enoch-sheet-005-less-human/out/enoch-sheet_231506246.png` 4 time(s). Denoise 0.45: a moderate change: pose and layout stay, details, colours and line can change.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.2, using `art/enoch-sheet/enoch_sheet_v14.png`. Reference image, as in the parent's recipe: carries Enoch's colours and v14's four thick tail rings without copying v14's three-view layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-005-less-human`:
- added: `(cel shading:1.3)`
- added: `(simple shading:1.1)`
- removed: `flat color`
- removed: `cel shading`

```
charsheet, masterpiece, best quality, newest, absurdres, (cel shading:1.3), (simple shading:1.1), safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, (symmetrical:1.2), symmetry, (symmetrical pose:1.2), digitigrade, simple background, white background, plain white background, thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail
BREAK (fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette, simple shapes, minimal interior lines
BREAK lean, broad shoulders, flat chest, narrow hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (asymmetrical:1.2), (asymmetrical pose:1.2), uneven body, human, (human-like:1.2), human proportions, skin-tight, sketchy lines, (painterly:1.2), (gradient:1.1), airbrush, drop shadow, charcoal grey
```

## Output
Images go to `art/jobs/enoch-sheet-006-shading-v2/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: 8e170171189672b3
