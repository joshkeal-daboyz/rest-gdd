# Forge job enoch-sheet-003-symmetry

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
In the front view, the back view with tail and the back view without tail, make the body left-right symmetrical (arms and hands, shoulders, legs and feet, and the white hip wedges and tail-base spot on the backs); the tail is exempt and the ring count is no longer a goal. The flat style stays as it is.

## Why this job should do it
Josh's request: images 1, 3 and 4 (front, back with tail, back without tail) should be symmetrical apart from the tail. Where the parent (job 2 seed 231506246) is lopsided: in the front view the two hands hang and curl differently, and the tail sits behind one leg; in the back view with tail the white hip wedge on one side of the tail is a different size and shape from the other (Josh's crop shows a pointed wedge on one side and a rounder, bigger one on the other, with the tail between); in the tailless back the white wedge and the cleft are a little off-centre and the spot has a mark inside it. What I chose: prompt tags plus the same whole-sheet img2img as job 2, and NOT the canny guide. I looked at art/enoch-sheet/shoulder_guide_4pose.png: it is not symmetrical itself. The front view's two hands are drawn differently, the front tail is drawn only on one side, the arms are not mirror images, and the back view with tail has the tail covering one side, so using it would lock those lopsided edges in. Its tail bands don't matter, but its hands and arms do. It would also fight the parent's layout (a 2048x1024 edge map against a 2304x1152 image). So no ControlNet guide is added; the IP-Adapter is unchanged. Positive: '(symmetrical:1.2), symmetry, (symmetrical pose:1.2)' added after 'arms at sides'. These are Danbooru-style tags the model knows, and they sit in the first 75-token chunk so they carry full weight. Nothing in the job 2 prompt contradicts them ('arms at sides' and 'standing' already ask for a straight, even pose). Negative: job 2's negative plus '(asymmetrical:1.2), (asymmetrical pose:1.2), uneven body'. The tail wording, the jewelry negatives and everything else are exactly as job 2, and the flat style is not touched (a separate job adds shading). Denoise stays at 0.6, size, seeds 231506246-249, LoRA 0.6 and IP-Adapter as in job 2. 0.6 is high enough for the model to redraw hands and the hip wedges toward a symmetric shape instead of tracing the parent's, while the init image keeps the layout. A lower value would likely trace the lopsided shapes again; a higher one risks losing the face. Wording is the only change from job 2 apart from the parent image, which is job 2's pick. Honest expectation: tags alone often give only a modest symmetry gain, and with no mask or mirror guide I don't expect perfect symmetry. The hands are the most likely to stay different. If so, the next job probably needs a symmetrical guide or mask from Josh.

## What Forge will do
Redraw `art/jobs/enoch-sheet-001-tail-wording/out/enoch-sheet_231506246.png` 4 time(s). Denoise 0.6: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.4, using `art/enoch-sheet/enoch_sheet_v14.png`. Reference image, as in the parent's recipe: carries Enoch's colours and v14's four thick tail rings without copying v14's three-view layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, size parent's size
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-001-tail-wording`:
- added: `(symmetrical:1.2)`
- added: `symmetry`
- added: `(symmetrical pose:1.2)`

```
charsheet, masterpiece, best quality, newest, absurdres, safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, (symmetrical:1.2), symmetry, (symmetrical pose:1.2), digitigrade, simple background, white background, plain white background, flat color, cel shading, thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail, lean, broad shoulders, flat chest, narrow hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (asymmetrical:1.2), (asymmetrical pose:1.2), uneven body
```

## Output
Images go to `art/jobs/enoch-sheet-003-symmetry/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.
