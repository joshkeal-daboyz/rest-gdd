# Forge job female-raccoon-001-baseline-ipadapter

**Asset:** female-raccoon | **Track:** female-baseline | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
A fresh female raccoon base-body sheet from Indigo Void (front, side, back on off-white) that keeps the look and palette of baseline-highres.png: teal fur, navy mask/sleeves/lower legs/four tail rings, mint chest and hip patch, hourglass build, digitigrade feet.

## Why this job should do it
txt2img with the required Indigo Void checkpoint and charsheet_lora_v1 at 0.6 (trigger 'charsheet' first in the prompt) lays out the three-view sheet, the way Enoch's v14 was made. The look comes from two things: (1) ControlNet ip-adapter-plus_sdxl_vit-h (module CLIP-ViT-H (IPAdapter)) fed baseline-highres.png at weight 0.5, Balanced, which carries her colours, face and flat cartoon style over without copying the reference's layout; (2) the existing female.prompt.txt with the added trigger, plus the toon words from Enoch's charsheet-toon prompt ('(toon style:1.2)', 'thick outlines', 'simple shapes', 'minimal fur detail'), because Indigo Void drifts to a realistic furry style on sheets without them. The layout words ('same character three times', '(three views:1.2)') and the style words ('(toon style:1.2), thick outlines, simple shapes, minimal fur detail, flat colors, clean lineart, cartoon') sit right after the charsheet trigger and sheet words, so they fall in the first 75-token chunk and carry full weight. 'white inner ears' and 'red-brown eyes' match the palette and eye rules (inner ears white, red-brown iris with large dark pupils). The negative's '(color palette:1.3)', '(color swatch:1.2)', '(multiple heads:1.3)', 'head studies', 'bust', 'close-up' stop it copying the reference's colour swatches and the extra side-view bust, which the sheet-layout rule forbids. The negative is female.negative.txt trimmed to general terms per enoch-rules.md's censor-mark rule ('keep the negative to nsfw and general terms'): all anatomy words ('(anus:1.5)', '(butt focus:1.5)', 'genitals', 'nipples', '(breasts:1.3)', '(cleavage:1.4)') and 'nude' are removed, and no 'censored'/'mosaic censoring' is used, since on NoobAI models a 'censored' negative on an unclothed figure pushes toward explicit anatomy. 'nsfw', 'sexual', 'suggestive' and 'clothes' stay; the plain body is carried by the positive '(featureless body:1.3)' and 'flat chest'. Added to the negative: 'grey fur', 'charcoal grey' (the model's known grey-raccoon drift), plus 'realistic', 'detailed fur'. '(big head:1.2)' is removed, because without an edge guide this model draws heads too small (about 0.13 of height against the 0.19-0.21 rule), and 'chibi'/'child' already guard the other side; head size is not expected to pass without a guide, so judge this job on colours and look. Size 1536x1024 is the sheet size of Enoch's v14 and close to the reference's 3:2 shape. Fixed seed 20261027 (counting up over 4 images) so the next job on this track can change one thing against the same seeds.

## What Forge will do
Draw 4 new image(s) from the prompt, starting from noise.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.5, using `art/female-raccoon/baseline-highres.png`. Reference image: carries the female baseline's look, palette and flat style without copying its layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, size 1536x1024
- Seed: 20261027, counting up per image

## Prompt

```
charsheet, masterpiece, best quality, (character reference sheet:1.3), (turnaround:1.2), front view, side view, back view, same character three times, (three views:1.2), (toon style:1.2), thick outlines, simple shapes, minimal fur detail, flat colors, clean lineart, cartoon, full body, standing, relaxed pose, weight on one leg, arms slightly away from body, solo, furry, anthro raccoon, (adult woman:1.2), (female:1.4), (feminine:1.2), round face, wide friendly smile, (adult proportions:1.1), (hourglass figure:1.2), (narrow waist:1.1), (wide hips:1.1), full thighs, (narrow shoulders:1.1), big round eyes, large dark pupils, red-brown eyes, eyelashes, flat chest, (featureless body:1.3), (no clothes, no accessories:1.2), smooth fur body, teal fur, dark navy raccoon mask markings, pale mint muzzle, white inner ears, pale mint belly, small spiky fur tufts on shoulders, dark navy hands, (flat even fur edge on forearms:1.2), dark navy lower legs, (pale mint patch on lower back:1.1), big ringed striped tail, (four navy rings:1.1), navy ring at the tail base, (dark navy tail tip:1.3), (digitigrade legs:1.3), (standing on toes:1.2), raccoon hind paws, slender raccoon hands, plain off-white background, concept art, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
(teal tail tip:1.3), (white tail tip:1.3), (zigzag tail rings:1.2), (child:1.3), (chibi:1.3), (skinny:1.2), (thigh highs:1.4), stockings, nsfw, sexual, suggestive, seductive, (male:1.4), (masculine:1.3), square jaw, (square body:1.3), (wide shoulders:1.3), (zigzag fur edge on forearms:1.2), angry, scowling, lipstick, makeup, muscular, (color swatch:1.2), lowres, worst quality, bad anatomy, bad hands, extra fingers, extra limbs, flat feet, plantigrade, shoes, clothes, apron, bag, human, text, watermark, signature, blurry, scenery, gradient shading, (grey fur:1.2), charcoal grey, (realistic:1.3), (detailed fur:1.2), (color palette:1.3), (multiple heads:1.3), head studies, bust, close-up
```

## Output
Images go to `art/jobs/female-raccoon-001-baseline-ipadapter/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.
