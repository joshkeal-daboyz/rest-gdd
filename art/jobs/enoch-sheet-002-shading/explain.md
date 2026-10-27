# Forge job enoch-sheet-002-shading

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Josh asked for this in chat ("Lets add shading."), deliberately overriding the style guide's flat-colour rule: add hard-edged cartoon cel shading (one shadow tone per colour) to the generator's and Claude's pick from job 1 (seed 231506246; Josh has not confirmed it yet), keeping the outlines, palette, face and plain white background.

## Why this job should do it
Josh asked for this in chat ("Lets add shading."). He is deliberately overriding the style guide's flat-colour rule; the rule and palette will be updated with shadow tones if he calls this job on-track. This job changes only the shading wording. 'flat color, cel shading' becomes '(cel shading:1.3), (simple shading:1.1)'; 'flat color' is removed because it contradicts shading, and 'cel shading' is the model's tag for hard-edged, one-step shadow. Everything else is as in job 1: img2img denoise 0.6, seed 231506246 counting up over 4 images, Euler a, 30 steps, CFG 6, charsheet_lora_v1 at 0.6, the same IP-Adapter (v14 sheet, end 0.6) but with its weight lowered from 0.4 to 0.2, because the flat v14 reference would pull the image back to flat colour, the same tail wording and the same jewelry negatives. Negative additions: '(painterly:1.2), (soft shading:1.2), (gradient:1.2)' keep shadows hard-edged; 'drop shadow, cast shadow' stop shadows on the white background; 'charcoal grey' stops grey shadow tones on the fur. No symmetry change; tail band count is not a goal. The parent is the generator's and Claude's pick from job 1 (seed 231506246); Josh has not confirmed it yet.

## What Forge will do
Redraw `art/jobs/enoch-sheet-001-tail-wording/out/enoch-sheet_231506246.png` 4 time(s). Denoise 0.6: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.2, using `art/enoch-sheet/enoch_sheet_v14.png`. Reference image, as in the parent's recipe: carries Enoch's colours and v14's four thick tail rings without copying v14's three-view layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-001-tail-wording`:
- added: `(cel shading:1.3)`
- added: `(simple shading:1.1)`
- removed: `flat color`
- removed: `cel shading`

```
charsheet, masterpiece, best quality, newest, absurdres, safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, digitigrade, simple background, white background, plain white background, (cel shading:1.3), (simple shading:1.1), thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail, lean, broad shoulders, flat chest, narrow hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (painterly:1.2), (soft shading:1.2), (gradient:1.2), drop shadow, cast shadow, charcoal grey
```

## Output
Images go to `art/jobs/enoch-sheet-002-shading/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.
