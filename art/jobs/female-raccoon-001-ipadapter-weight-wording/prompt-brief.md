job: female-raccoon-001-ipadapter-weight-wording
job-hash: 648832c8a3dee4fb

# Reason for the change

**What we're trying to change:** Same three-view sheet and seeds as female-raccoon-001-baseline-ipadapter, but with: teal #48C2C3 fur (not pale seafoam); a mint chest (not cream) and a mint hip patch, as in baseline-highres.png; navy that reads as blue #2A4365 (001's came out near-black/purple in all four); white inner ears; and no hourglasses, arrows, hooks, tiaras, devil tails, limb studies or logo tiles in the empty space.

**Why this job should do it:** BASE: female-raccoon-001-baseline-ipadapter (Josh: off-track). Same model, charsheet_lora_v1:0.6, 1536x1024, 30 steps, CFG 6, Euler a, seeds 20261027-20261030, so images compare one to one. TWO CHANGES, judged on different parts of the image (figure colours vs. empty background). CHANGE 1, COLOUR: IP-Adapter weight 0.5 -> 0.8 (same ip-adapter-plus_sdxl_vit-h, CLIP-ViT-H, same reference). At 0.5, 001 got pale seafoam fur, cream chest, near-black/purple navy and no hip patch. At 0.8 the reference's saturated teal, blue navy and mint (and the hip patch in its back view) weigh much more in the conditioning. The weight is not the only colour lever: replacing 'clean lineart' (change 2c) may also improve colour, since 'lineart' pulls toward uncoloured, washed-out images on this model. So better colour can't be credited to 0.8 alone. The colour words are left as they were; if fur stays seafoam or the chest cream, suspect the 'pale mint'/'off-white' wording next. LAYOUT: 'Balanced' control mode likely has little effect on an IP-Adapter in Forge (it works through attention, not ControlNet residuals). Only the prompt guards against copying the reference's four-figure layout: '(three views:1.2)', 'same character three times', and the negatives '(color swatch:1.2)', '(color palette:1.3)', 'bust', 'head studies'. CHANGE 2, STRAY OBJECTS (wording only): (a) '(hourglass figure:1.2)' removed from the positive; it drew literal hourglasses in 3 of 4. The build stays on '(narrow waist:1.1), (wide hips:1.1)', unchanged from 001. (b) '(no clothes, no accessories:1.2)' removed (CLIP reads 'no X' as X, likely the tiara). 'accessories, jewelry, tiara' added to the negative beside 'clothes'; '(featureless body:1.3)' keeps the plain body (001 review rec 3). (c) 'clean lineart' -> 'clean bold outlines' (style guide wording; 'thick outlines' stays). 'lineart' tags uncoloured line drawings, matching 001's outline figures and studies. '(sketches:1.2)' is added to the negative by this job to back this up. (d) New negatives for what the LoRA drew in the empty space: '(props:1.3), objects, (hourglass:1.3), (arrows:1.2), symbols, icons, logo, (sketches:1.2), (extra tails:1.2), (devil tail:1.2)'. No anatomy words in the negative (enoch-rules.md censor-mark rule). WHY BUNDLED: props wording alone at 0.5 would just repeat the colour failure; weight alone would repeat the hourglasses on these seeds. Overlap: a stronger IP-Adapter may also tidy the background (the reference has no clutter), so a clean background can't be credited fully to the wording. RISKS: at 0.8 the reference's swatches (incl. the yellow dot), side bust or fourth figure may leak; read that as the weight too high. NOT TESTED: head size (needs a female edge guide from Josh), stronger '(teal fur)' wording, and 001 review recs 1-2 (layout).

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`

# Images to look at
- ControlNet image: `art/female-raccoon/baseline-highres.png`
- reference: `art/female-raccoon/baseline-highres.png`
- reference: `art/enoch-sheet/enoch_character_sheet.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261028.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261029.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261030.png`

# Earlier jobs on this track
- `female-raccoon-001-baseline-ipadapter`: goal "A fresh female raccoon base-body sheet from Indigo Void (front, side, back on off-white) that keeps the look and palette of baseline-highres.png: teal fur, navy mask/sleeves/lower legs/four tail rings, mint chest and hip patch, hourglass build, digitigrade feet."; reviewer said partly; Josh's verdict off-track: Off-track

# The job, explained

# Forge job female-raccoon-001-ipadapter-weight-wording

**Asset:** female-raccoon | **Track:** female-baseline | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Same three-view sheet and seeds as female-raccoon-001-baseline-ipadapter, but with: teal #48C2C3 fur (not pale seafoam); a mint chest (not cream) and a mint hip patch, as in baseline-highres.png; navy that reads as blue #2A4365 (001's came out near-black/purple in all four); white inner ears; and no hourglasses, arrows, hooks, tiaras, devil tails, limb studies or logo tiles in the empty space.

## Why this job should do it
BASE: female-raccoon-001-baseline-ipadapter (Josh: off-track). Same model, charsheet_lora_v1:0.6, 1536x1024, 30 steps, CFG 6, Euler a, seeds 20261027-20261030, so images compare one to one. TWO CHANGES, judged on different parts of the image (figure colours vs. empty background). CHANGE 1, COLOUR: IP-Adapter weight 0.5 -> 0.8 (same ip-adapter-plus_sdxl_vit-h, CLIP-ViT-H, same reference). At 0.5, 001 got pale seafoam fur, cream chest, near-black/purple navy and no hip patch. At 0.8 the reference's saturated teal, blue navy and mint (and the hip patch in its back view) weigh much more in the conditioning. The weight is not the only colour lever: replacing 'clean lineart' (change 2c) may also improve colour, since 'lineart' pulls toward uncoloured, washed-out images on this model. So better colour can't be credited to 0.8 alone. The colour words are left as they were; if fur stays seafoam or the chest cream, suspect the 'pale mint'/'off-white' wording next. LAYOUT: 'Balanced' control mode likely has little effect on an IP-Adapter in Forge (it works through attention, not ControlNet residuals). Only the prompt guards against copying the reference's four-figure layout: '(three views:1.2)', 'same character three times', and the negatives '(color swatch:1.2)', '(color palette:1.3)', 'bust', 'head studies'. CHANGE 2, STRAY OBJECTS (wording only): (a) '(hourglass figure:1.2)' removed from the positive; it drew literal hourglasses in 3 of 4. The build stays on '(narrow waist:1.1), (wide hips:1.1)', unchanged from 001. (b) '(no clothes, no accessories:1.2)' removed (CLIP reads 'no X' as X, likely the tiara). 'accessories, jewelry, tiara' added to the negative beside 'clothes'; '(featureless body:1.3)' keeps the plain body (001 review rec 3). (c) 'clean lineart' -> 'clean bold outlines' (style guide wording; 'thick outlines' stays). 'lineart' tags uncoloured line drawings, matching 001's outline figures and studies. '(sketches:1.2)' is added to the negative by this job to back this up. (d) New negatives for what the LoRA drew in the empty space: '(props:1.3), objects, (hourglass:1.3), (arrows:1.2), symbols, icons, logo, (sketches:1.2), (extra tails:1.2), (devil tail:1.2)'. No anatomy words in the negative (enoch-rules.md censor-mark rule). WHY BUNDLED: props wording alone at 0.5 would just repeat the colour failure; weight alone would repeat the hourglasses on these seeds. Overlap: a stronger IP-Adapter may also tidy the background (the reference has no clutter), so a clean background can't be credited fully to the wording. RISKS: at 0.8 the reference's swatches (incl. the yellow dot), side bust or fourth figure may leak; read that as the weight too high. NOT TESTED: head size (needs a female edge guide from Josh), stronger '(teal fur)' wording, and 001 review recs 1-2 (layout).

## What Forge will do
Draw 4 new image(s) from the prompt, starting from noise.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.8, using `art/female-raccoon/baseline-highres.png`. Reference image: carries the female baseline's look, palette and flat style without copying its layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, size 1536x1024
- Seed: 20261027, counting up per image

## Prompt
Compared with job `female-raccoon-001-baseline-ipadapter`:
- added: `clean bold outlines`
- removed: `clean lineart`
- removed: `(hourglass figure:1.2)`
- removed: `(no clothes`
- removed: `no accessories:1.2)`

```
charsheet, masterpiece, best quality, (character reference sheet:1.3), (turnaround:1.2), front view, side view, back view, same character three times, (three views:1.2), (toon style:1.2), thick outlines, simple shapes, minimal fur detail, flat colors, clean bold outlines, cartoon, full body, standing, relaxed pose, weight on one leg, arms slightly away from body, solo, furry, anthro raccoon, (adult woman:1.2), (female:1.4), (feminine:1.2), round face, wide friendly smile, (adult proportions:1.1), (narrow waist:1.1), (wide hips:1.1), full thighs, (narrow shoulders:1.1), big round eyes, large dark pupils, red-brown eyes, eyelashes, flat chest, (featureless body:1.3), smooth fur body, teal fur, dark navy raccoon mask markings, pale mint muzzle, white inner ears, pale mint belly, small spiky fur tufts on shoulders, dark navy hands, (flat even fur edge on forearms:1.2), dark navy lower legs, (pale mint patch on lower back:1.1), big ringed striped tail, (four navy rings:1.1), navy ring at the tail base, (dark navy tail tip:1.3), (digitigrade legs:1.3), (standing on toes:1.2), raccoon hind paws, slender raccoon hands, plain off-white background, concept art, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
(teal tail tip:1.3), (white tail tip:1.3), (zigzag tail rings:1.2), (child:1.3), (chibi:1.3), (skinny:1.2), (thigh highs:1.4), stockings, nsfw, sexual, suggestive, seductive, (male:1.4), (masculine:1.3), square jaw, (square body:1.3), (wide shoulders:1.3), (zigzag fur edge on forearms:1.2), angry, scowling, lipstick, makeup, muscular, (color swatch:1.2), lowres, worst quality, bad anatomy, bad hands, extra fingers, extra limbs, flat feet, plantigrade, shoes, clothes, apron, bag, accessories, jewelry, tiara, human, text, watermark, signature, blurry, scenery, gradient shading, (grey fur:1.2), charcoal grey, (realistic:1.3), (detailed fur:1.2), (color palette:1.3), (multiple heads:1.3), head studies, bust, close-up, (props:1.3), objects, (hourglass:1.3), (arrows:1.2), symbols, icons, logo, (sketches:1.2), (extra tails:1.2), (devil tail:1.2)
```

## Output
Images go to `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.
