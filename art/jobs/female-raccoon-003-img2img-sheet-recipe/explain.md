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
