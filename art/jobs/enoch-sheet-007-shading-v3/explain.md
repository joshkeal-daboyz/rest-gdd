# Forge job enoch-sheet-007-shading-v3

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Get visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour, as in anime screencaps) on enoch-sheet-005-less-human's seed 246 image at denoise 0.55, keeping its paws, heads, symmetry, bold outlines, palette and plain white background.

## Why this job should do it
Josh asked for shading in chat ("Lets add shading.", "Yes shading"), then said: "I would like you to apply anime style cell shading". This overrides the style guide's flat-colour rule; the rule and palette get updated with shadow tones if he calls a shading job on-track. Job enoch-sheet-006-shading-v2 (denoise 0.45) gave no visible shading: all four images stayed flat colour, with only the paw pads drifting browner, and Josh marked it off-track and said 'Retry'. Changes against job 006 (same parent art/jobs/enoch-sheet-005-less-human/out/enoch-sheet_231506246.png, seeds 231506246-249, IP-Adapter v14 at weight 0.2 end 0.6, LoRA, sampler, negative): (1) denoise 0.45 to 0.55, so Forge has room to repaint fills with a shadow tone. (2) Prompt adds '(anime coloring:1.1)' between '(cel shading:1.3)' and '(simple shading:1.1)'. 'anime coloring' is the danbooru tag for the flat-fill, hard-edged shadow-shape look of anime screencaps, which is what Josh described. I weighed adding it: it names his look directly and '(cel shading:1.3)' stays the strongest term, so the tag helps with the shadow style without taking over. It is set at 1.1, level with '(simple shading:1.1)' and below cel shading, because anime tags can also nudge faces and proportions toward human anime, and the face, eyes and mask must stay as they are. I did NOT add 'anime screencap': it is a whole-image tag that pulls toward screen-grab faces, lighting and backgrounds, which would risk the character style, the pupils and the plain white background. The existing negative '(painterly:1.2), (gradient:1.1), airbrush, drop shadow, charcoal grey' keeps shading hard-edged and off the background. Risks to check at 0.55: paws and heads first (job 001 at 0.6 redrew hands and faces too much), then pupils, mask, symmetry, four views, tail, teal shadows going grey or navy merging into the lines, and any anime-face drift from the new tag. No masks, guides or pixel edits. Small job, 4 images, no hires.

## What Forge will do
Redraw `art/jobs/enoch-sheet-005-less-human/out/enoch-sheet_231506246.png` 4 time(s). Denoise 0.55: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.2, using `art/enoch-sheet/enoch_sheet_v14.png`. Reference image, as in the parent's recipe: carries Enoch's colours and v14's four thick tail rings without copying v14's three-view layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-006-shading-v2`:
- added: `(anime coloring:1.1)`

```
charsheet, masterpiece, best quality, newest, absurdres, (cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, (symmetrical:1.2), symmetry, (symmetrical pose:1.2), digitigrade, simple background, white background, plain white background, thick outlines
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
Images go to `art/jobs/enoch-sheet-007-shading-v3/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: 5d7b1f14b254a66a
