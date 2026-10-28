# Forge job enoch-sheet-012-shading-0.6

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Keep the shading from job 010 while carrying more of the locked parent's pose (including the back-view head facing away) and fewer stray objects, by lowering denoise from 0.7 to 0.6; this is the only change.

## Why this job should do it
Josh said: "Lets try adding shading all over again before the head turn." Job history on this track: 009 (charsheet LoRA removed from 008, denoise 0.7) was the first job with visible shading (248 and 249), but it grew stray head objects and half-closed eyes; Josh marked it on-track for #1 (seed 249) and asked for the faults to be fixed. 010 added fault negatives only and kept the shading (248 hard-edged, 249 soft), fixed the eyes and the head ratios, and Josh marked it on-track, but 248's back-view head was turned over the shoulder and 247 and 249 kept a goggle piece or strap. 011 added turn-away negatives to 010 and did not fix 248's head, and shrank the head ratios, so Josh marked it off-track; a one-time head swap was rejected, and Josh is fixing that head himself. This job is built from 010, not 011. This is one change: denoise 0.7 to 0.6. The head turn and the stray objects appeared at 0.7, where Forge redraws most of the layout. At 0.6 more of the locked parent's pose should carry over, including its back-view head facing away, and fewer objects should be invented. The charsheet LoRA stays removed, so the shading may still come through. Risk: the shading may fade at 0.6. Job 007 at 0.55 was flat, but that test still had the charsheet LoRA, which was the likely blocker, so it does not tell us what 0.6 does without it. Other risks: the grey-pink belly tint and goggle straps may remain. Everything else is exactly as in 010: the locked less-human 246 parent, no charsheet LoRA, 010's positive prompt and 010's negatives (not 011's turn negatives), the IP-Adapter ip-adapter-plus_sdxl_vit-h on the locked copy at 0.25 ending at 0.5, seeds 231506246-249 (4 images), Euler a, 30 steps, CFG 6, no hires. Each image compares with its 010 twin. Check the third-view head in every image, the shading, stray objects, eyes, head ratio and line width. No masks, guides or pixel edits.

## What Forge will do
Redraw `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png` 4 time(s). Denoise 0.6: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.25, using `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png`. Reference image: the locked less-human 246 sheet, so colours, paws and head carry over; weight kept low because the locked image is flat-coloured and would pull the result back to flat.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: none
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-010-shading-fix-faults`:
- no change to the prompt

```
masterpiece, best quality, newest, absurdres, (cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, (symmetrical:1.2), symmetry, (symmetrical pose:1.2), digitigrade, simple background, white background, plain white background, thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail
BREAK (fluffy fur:1.2), (shoulder fur tufts:1.2), hip fur tufts, fluffy cheek fur, (raccoon paws:1.2), (paw-like hands with short stubby fingers:1.2), soft furry silhouette
BREAK lean, broad shoulders, flat chest, narrow hips, featureless crotch
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, (headband:1.2), (headwear:1.2), hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (asymmetrical:1.2), (asymmetrical pose:1.2), uneven body, human, (human-like:1.2), human proportions, skin-tight, sketchy lines, (painterly:1.2), airbrush, drop shadow, charcoal grey, flat colors, eyewear, sunglasses, eyewear on head, goggles, goggles on head, strap, collar, (half-closed eyes:1.2)
```

## Output
Images go to `art/jobs/enoch-sheet-012-shading-0.6/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: 0dc37d57c9f37526
