# Forge job enoch-sheet-001-tail-wording

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
On the C2 candidate sheet, remove the gold finger rings and grey tail-base disc that job 1 introduced, and get thicker, cleaner tail bands (ideally nearer four) on the side and back tails, by changing only the tail wording and the negative; the ring count is not expected to reach exactly four without a mask or guide.

## Why this job should do it
What job 1 (enoch-sheet-001-tail-rings, denoise 0.6, same parent) showed: the side and back tails stayed at about 5-6 bands with ragged zigzag edges; gold finger rings appeared on the hands in all four images, likely from the loose 'rings' phrases ('four thick dark navy rings on tail', 'between the rings', 'ring at the tail base') being read as jewelry; and the tail-base spot on the tailless back turned into a grey disc or hollow ring. This job changes only the tail wording and the negative, so the wording is the only difference from job 1. Everything else is as in job 1: img2img of art/enoch-sheet/eyetest/C2/enoch_231506246.png at the parent's size, denoise 0.6, Euler a, 30 steps, CFG 6, seed 231506246 counting up over 4 images, charsheet_lora_v1 at 0.6, and the same IP-Adapter (ip-adapter-plus_sdxl_vit-h, enoch_sheet_v14.png, weight 0.4, end 0.6, Resize and Fill). Positive: job 1's tail phrases are all replaced by 'raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail'. No standalone 'ring' or 'rings' word is left in the prompt, which should stop the jewelry reading ('ringed tail' is the model's own tag for a banded tail). '(thick tail stripes:1.2)' asks for wide bands, which should give fewer, cleaner bands than before; '(dark blue tail tip:1.2)' and 'teal tail' keep a dark tip on a teal tail. Negative: job 1's negative plus 'jewelry, (gold ring:1.2), finger ring, gold', which directly blocks the gold rings on the hands; '(many thin tail bands:1.3)' and '(light tail tip:1.1)' are kept, and no bare 'ring' or 'rings' is added. Plainly: the reviewer expects the ring count to stay near 5-6 without a mask or a four-band guide. Josh chose no mask, so this job tests whether the wording removes the jewelry and gives thicker, cleaner bands, not whether it reaches exactly four. The grey tail-base disc is not addressed by any new word here; this job will show whether it goes away once the jewelry words are gone.

## What Forge will do
Redraw `art/enoch-sheet/eyetest/C2/enoch_231506246.png` 4 time(s). Denoise 0.6: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.4, using `art/enoch-sheet/enoch_sheet_v14.png`. Reference image, as in the parent's recipe: carries Enoch's colours and v14's four thick tail rings without copying v14's three-view layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, size parent's size
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-001-tail-rings`:
- added: `raccoon tail`
- added: `(thick tail stripes:1.2)`
- added: `(dark blue tail tip:1.2)`
- added: `teal tail`
- removed: `(four thick dark navy rings on tail:1.3)`
- removed: `(wide teal bands between the rings:1.2)`
- removed: `(dark navy ring at the tail base:1.2)`
- removed: `(dark navy tail tip:1.3)`

```
charsheet, masterpiece, best quality, newest, absurdres, safe, solo, male, anthro, furry, raccoon, multiple views, reference sheet, turnaround, front view, side view, rear view, back view, full body, standing, arms at sides, digitigrade, simple background, white background, plain white background, flat color, cel shading, thick outlines
BREAK (brown eyes:1.3), (red eyes:0.6), black pupils, (large pupils:1.1), eye shine, white sclera
BREAK (teal body:1.3), (teal fur:1.2), (wide solid dark navy raccoon mask band across both eyes:1.3), (navy mask directly touching the eyes:1.2), (thin white stripe above the mask:1.2), smile, closed mouth
BREAK white countershading, white muzzle, white belly, dark blue inner ears, gloves \(marking\), socks \(marking\), dark blue hands, dark blue lower legs, raccoon tail, ringed tail, big fluffy tail, (thick tail stripes:1.2), (dark blue tail tip:1.2), teal tail, lean, broad shoulders, flat chest, narrow hips, featureless crotch, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold
```

## Output
Images go to `art/jobs/enoch-sheet-001-tail-wording/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.
