# Forge job enoch-sheet-013-back-head-inpaint

**Asset:** enoch-sheet | **Track:** c2-refine | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Repaint only the head in view 3 (back view with tail) of 010's seed 248 so it faces away like view 4 (back of the head and ears, no face, muzzle or eye), keeping everything outside the mask exactly as it is.

## Why this job should do it
Josh said: "I have given you permission to create masks, lets try and use inpaint to fix the problem with the side ways head". Job 010 (on-track) has good shading, but in seed 248 the head in view 3 (back view with tail) is turned over the shoulder with the mask and eye showing. Job 011 (turn-away negatives, img2img) did not fix it, and 012 (denoise 0.6) fixed the head but lost all the shading, so a whole-image redraw cannot do both. Inpainting only the head leaves the shading elsewhere unchanged. Parent: art/jobs/enoch-sheet-010-shading-fix-faults/out/enoch-sheet_231506248.png (2304x1152). Mask, made with forge_jobs.py mask: one ellipse centred (1368,170), radii 150x125, grown by 16 px, so about x 1202-1534, y 29-311 (about 2.9% of the sheet). Josh looked at the first mask preview (a 118x97 ellipse grown by 8) and said: "Its going to need to be larger". View 3's head spans about x 1253-1482, y 67-262, the narrowest neck is y 262 and the shoulders start around y 290, so this mask has generous margins beyond the ears, the top and the muzzle side, and reaches down over the neck onto the top of the shoulders so the new head can blend in. It stays in view 3: its right edge (x 1534) is well short of view 4's head (x 1744 and up) and its left edge (x 1202) is clear of view 2. Prompt (a plain string, written for the back of a head): 'rear view, back view, from behind, facing away, (back of head:1.3), teal fur, teal head fur, fur tufts, rounded ears with navy outer tips and white inner rim', plus the sheet's shading words '(cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, thick outlines' and the white background, so the new head matches the shaded style; no eye, mask or smile words. Negative: '(face:1.4), (eyes:1.3), (muzzle:1.3), (snout:1.3), nose, mouth, (looking back:1.3), looking over shoulder, (head turned:1.3), profile, three-quarter view, front view, (mask:1.2), raccoon mask' against any face, plus 010's stray-object negatives (headband, headwear, eyewear, sunglasses, goggles, strap, collar), 'grey fur, charcoal grey', 'flat colors' and the general style negatives. The known-faults table warns against body-part words in the negative because of the lower-back censor mark; here every word names the head, and the lower back is outside the mask and so cannot change. Settings: inpaint, no charsheet LoRA (as in 010), seeds 231506246-249 over 4 images, Euler a, 30 steps, CFG 6. Denoise 0.9: a pose change (face turned to face away) needs most of the masked area to be redrawn, and 0.75-0.9 is the usual range; 0.9 still starts from the original, so the teal, outlines and neck join carry over. inpainting_fill is 1 (original); if a face survives, the next job can try fill 2 (latent noise). inpaint_full_res is on with 64 px of padding, so Forge draws the crop (a crop of head, neck and top of the shoulders) at 1024x1024 for detail and sees the neck and shoulders for context. Mask blur 8 softens the seam so the new head blends into the old neck. The IP-Adapter is left out on purpose: the locked reference's front and side heads show faces and could pull the new head to face forward. Everything outside the mask is kept as it is. Check: is the head facing away, with no face, muzzle or eye; do the ears, fur and outline match view 4's head; is the seam at the neck clean; is the rest of the sheet unchanged. No guides, no pixel edits.

## What Forge will do
Redraw only the white area of `art/jobs/enoch-sheet-013-back-head-inpaint/mask.png` on `art/jobs/enoch-sheet-010-shading-fix-faults/out/enoch-sheet_231506248.png`, 4 time(s). Everything outside the mask is kept. Denoise 0.9: close to a fresh image: very little of the parent survives.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: none
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size 1024x1024 (the masked area is drawn at this size)
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 231506246, counting up per image

## Prompt
Compared with job `enoch-sheet-010-shading-fix-faults`:
- added: `from behind`
- added: `facing away`
- added: `back of head`
- added: `(back of head:1.3)`
- added: `teal fur`
- added: `teal head fur`
- added: `fur tufts`
- added: `rounded ears with navy outer tips and white inner rim`
- removed: `male`
- removed: `multiple views`
- removed: `reference sheet`
- removed: `turnaround`
- removed: `front view`
- removed: `side view`
- removed: `full body`
- removed: `standing`
- removed: `arms at sides`
- removed: `(symmetrical:1.2)`
- removed: `symmetry`
- removed: `(symmetrical pose:1.2)`
- removed: `digitigrade`
- removed: `BREAK (brown eyes:1.3)`
- removed: `(red eyes:0.6)`
- removed: `black pupils`
- removed: `(large pupils:1.1)`
- removed: `eye shine`
- removed: `white sclera`
- removed: `BREAK (teal body:1.3)`
- removed: `(teal fur:1.2)`
- removed: `(wide solid dark navy raccoon mask band across both eyes:1.3)`
- removed: `(navy mask directly touching the eyes:1.2)`
- removed: `(thin white stripe above the mask:1.2)`
- removed: `smile`
- removed: `closed mouth`
- removed: `BREAK white countershading`
- removed: `white muzzle`
- removed: `white belly`
- removed: `dark blue inner ears`
- removed: `gloves \(marking\)`
- removed: `socks \(marking\)`
- removed: `dark blue hands`
- removed: `dark blue lower legs`
- removed: `raccoon tail`
- removed: `ringed tail`
- removed: `big fluffy tail`
- removed: `(thick tail stripes:1.2)`
- removed: `(dark blue tail tip:1.2)`
- removed: `teal tail`
- removed: `BREAK (fluffy fur:1.2)`
- removed: `(shoulder fur tufts:1.2)`
- removed: `hip fur tufts`
- removed: `fluffy cheek fur`
- removed: `(raccoon paws:1.2)`
- removed: `(paw-like hands with short stubby fingers:1.2)`
- removed: `soft furry silhouette`
- removed: `BREAK lean`
- removed: `broad shoulders`
- removed: `flat chest`
- removed: `narrow hips`
- removed: `featureless crotch`

```
masterpiece, best quality, newest, absurdres, safe, solo, anthro, furry, raccoon, rear view, back view, from behind, facing away, back of head, (back of head:1.3), teal fur, teal head fur, fur tufts, rounded ears with navy outer tips and white inner rim, (cel shading:1.3), (anime coloring:1.1), (simple shading:1.1), shaded, shadow, sidelighting, thick outlines, simple background, white background, plain white background
```

Negative:
```
nsfw, worst quality, low quality, lowres, (text:1.3), watermark, signature, (face:1.4), (eyes:1.3), (muzzle:1.3), (snout:1.3), nose, mouth, (looking back:1.3), looking over shoulder, (head turned:1.3), profile, three-quarter view, front view, (mask:1.2), raccoon mask, (grey fur:1.3), charcoal grey, (headband:1.2), (headwear:1.2), eyewear, sunglasses, goggles, strap, collar, jewelry, (painterly:1.2), airbrush, flat colors, human, 3d, realistic
```

## Output
Images go to `art/jobs/enoch-sheet-013-back-head-inpaint/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: a52573cce528c90e
