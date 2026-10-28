# Forge job enoch-sheet-009-shading-no-lora

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Test whether removing the charsheet LoRA lets visible anime-style cel shading (hard-edged shadow shapes, one shadow tone per colour) appear on the locked less-human 246 sheet; this is the only change from job 008.

## Why this job should do it
Josh asked for shading ("Lets add shading.", "I would like you to apply anime style cell shading"). After job 008 he marked it off-track ("There is no shading") and said: "Maybe the right word is shadow, yes run without charsheet". Then he corrected the plan: "No, one change at a time". Shading overrides the style guide's flat-colour rule; the rule and palette get updated with shadow tones if he calls this job on-track. Jobs 006, 007 and 008 were all flat: 12 images, no visible shadow tones, even with flat-colour wording removed, 'flat colors' in the negative, denoise up to 0.7 and a locked reference. The reviewer's remaining suspect is the charsheet LoRA, which was likely trained on flat character sheets and so pushes every fill flat. This job changes ONE thing from 008: the charsheet LoRA (charsheet_lora_v1 at 0.6) is removed from the job and the 'charsheet' trigger word is removed from the prompt. Kind stays character-sheet; the sheet layout is still asked for by the existing words 'multiple views, reference sheet, turnaround, front view, side view, rear view, back view', but without the LoRA the layout may drift, which is a risk to check. Everything else is exactly as in 008: the prompt (shadow wording not weighted up: 'shaded, shadow, sidelighting' and '(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1)'), the negative with 'flat colors', denoise 0.7, IP-Adapter ip-adapter-plus_sdxl_vit-h on the locked copy at weight 0.25 ending at 0.5, seeds 231506246-249 (4 images), Euler a, 30 steps, CFG 6, no hires, Indigo Void. Weighting the shadow words (Josh's idea) is a possible later job. Risks to check: at 0.7 job 008 grew headbands, goggles, a collar and face changes on 3 of 4 images, and with no LoRA the style may drift more. Check shading, no grey teal, paws and heads, symmetry, four views and layout, pupils and mask, stray objects. No masks, guides or pixel edits.

## What Forge will do
Redraw `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png` 4 time(s). Denoise 0.7: a heavy redraw: only the rough layout carries over.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.25, using `art/locked/enoch-sheet/enoch-sheet-005-less-human_enoch-sheet_231506246.png`. Reference image: the locked less-human 246 sheet, so colours, paws and head carry over; weight kept low because the locked image is flat-coloured and would pull the result back to flat.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: none
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size parent's size
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-008-shading-wording`:
- removed: `charsheet`
- removed: `<lora:charsheet_lora_v1:0.6>`

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
nsfw, worst quality, low quality, lowres, old, early, (text:1.3), english text, arrow \(symbol\), speech bubble, signature, watermark, color swatch, female, breasts, (wide hips:1.2), (hourglass figure:1.2), child, chibi, (grey fur:1.3), realistic, detailed fur, plantigrade, clothes, 3d, empty eyes, no pupils, blank eyes, hollow eyes, ringed eyes, white pupils, (blue eyes:1.3), (color palette:1.2), (multiple views of face:1.1), eye study, close-up, head only, disembodied hand, inset, pink background, grey background, blush, headband, headwear, hairband, (many thin tail bands:1.3), (zigzag tail rings:1.2), (light tail tip:1.1), jewelry, (gold ring:1.2), finger ring, gold, (asymmetrical:1.2), (asymmetrical pose:1.2), uneven body, human, (human-like:1.2), human proportions, skin-tight, sketchy lines, (painterly:1.2), airbrush, drop shadow, charcoal grey, flat colors
```

## Output
Images go to `art/jobs/enoch-sheet-009-shading-no-lora/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: aad0763d64e6ca37
