job: female-raccoon-001-teal-colour-wording
job-hash: a3627c743e9dc472

# Reason for the change

**What we're trying to change:** Colour-only test on the same sheet and seeds as the weight-wording job: teal #48C2C3 fur (not seafoam), a pale-cyan chest and belly (mint #D0FFFA in the style guide; not cream), a pale-cyan hip patch, and blue navy #2A4365 markings (not near-black).

**Why this job should do it:** BASE: female-raccoon-001-ipadapter-weight-wording (Josh: off-track). Only the colour wording changes; IP-Adapter stays at 0.8 and the seeds, model, LoRA, size, steps, CFG and sampler are as before. '(teal fur:1.3), (turquoise fur:1.1)' sit early; 'mint' became 'pale cyan' so the green-leaning word stops bleeding onto the fur (chest and belly 1.1, hip patch 1.1, muzzle now 'white'); '(vivid colors:1.1)' plus negative 'muted colors, desaturated, pastel colors' push toward the saturated teal; negative '(green fur:1.2), mint green, (black fur:1.1), purple' and one 'navy blue' on the mask push the markings to blue. JUDGE: fur near #48C2C3, chest pale cyan not cream, markings blue not black, pale cyan hip patch in back view. Leaks (swatches, busts, head studies) from the reference are expected at 0.8 and are not judged here; the next job tackles them. Head size is not tested.

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`

# Images to look at
- ControlNet image: `art/female-raccoon/baseline-highres.png`
- reference: `art/female-raccoon/baseline-highres.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261028.png`
- earlier output of `female-raccoon-001-ipadapter-weight-wording`: `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-ipadapter-weight-wording`: `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/female-raccoon_20261028.png`

# Earlier jobs on this track
- `female-raccoon-001-baseline-ipadapter`: goal "A fresh female raccoon base-body sheet from Indigo Void (front, side, back on off-white) that keeps the look and palette of baseline-highres.png: teal fur, navy mask/sleeves/lower legs/four tail rings, mint chest and hip patch, hourglass build, digitigrade feet."; reviewer said partly; Josh's verdict off-track: Off-track
- `female-raccoon-001-ipadapter-weight-wording`: goal "Same three-view sheet and seeds as female-raccoon-001-baseline-ipadapter, but with: teal #48C2C3 fur (not pale seafoam); a mint chest (not cream) and a mint hip patch, as in baseline-highres.png; navy that reads as blue #2A4365 (001's came out near-black/purple in all four); white inner ears; and no hourglasses, arrows, hooks, tiaras, devil tails, limb studies or logo tiles in the empty space."; reviewer said partly; Josh's verdict off-track: Off-track.

# The job, explained

# Forge job female-raccoon-001-teal-colour-wording

**Asset:** female-raccoon | **Track:** female-baseline | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Colour-only test on the same sheet and seeds as the weight-wording job: teal #48C2C3 fur (not seafoam), a pale-cyan chest and belly (mint #D0FFFA in the style guide; not cream), a pale-cyan hip patch, and blue navy #2A4365 markings (not near-black).

## Why this job should do it
BASE: female-raccoon-001-ipadapter-weight-wording (Josh: off-track). Only the colour wording changes; IP-Adapter stays at 0.8 and the seeds, model, LoRA, size, steps, CFG and sampler are as before. '(teal fur:1.3), (turquoise fur:1.1)' sit early; 'mint' became 'pale cyan' so the green-leaning word stops bleeding onto the fur (chest and belly 1.1, hip patch 1.1, muzzle now 'white'); '(vivid colors:1.1)' plus negative 'muted colors, desaturated, pastel colors' push toward the saturated teal; negative '(green fur:1.2), mint green, (black fur:1.1), purple' and one 'navy blue' on the mask push the markings to blue. JUDGE: fur near #48C2C3, chest pale cyan not cream, markings blue not black, pale cyan hip patch in back view. Leaks (swatches, busts, head studies) from the reference are expected at 0.8 and are not judged here; the next job tackles them. Head size is not tested.

## What Forge will do
Draw 4 new image(s) from the prompt, starting from noise.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.8, using `art/female-raccoon/baseline-highres.png`. Reference image: carries the female baseline's look, palette and flat style without copying its layout.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, size 1536x1024
- Seed: 20261027, counting up per image

## Prompt
Compared with job `female-raccoon-001-ipadapter-weight-wording`:
- added: `(vivid colors:1.1)`
- added: `(teal fur:1.3)`
- added: `(turquoise fur:1.1)`
- added: `navy blue raccoon mask markings`
- added: `white muzzle`
- added: `(pale cyan chest and belly:1.1)`
- added: `navy hands`
- added: `navy lower legs`
- added: `(pale cyan patch across back of hips:1.1)`
- added: `(navy tail tip:1.3)`
- removed: `teal fur`
- removed: `dark navy raccoon mask markings`
- removed: `pale mint muzzle`
- removed: `pale mint belly`
- removed: `dark navy hands`
- removed: `dark navy lower legs`
- removed: `(pale mint patch on lower back:1.1)`
- removed: `(dark navy tail tip:1.3)`

```
charsheet, masterpiece, best quality, (character reference sheet:1.3), (turnaround:1.2), front view, side view, back view, same character three times, (three views:1.2), (toon style:1.2), thick outlines, simple shapes, minimal fur detail, flat colors, (vivid colors:1.1), clean bold outlines, cartoon, full body, standing, relaxed pose, weight on one leg, arms slightly away from body, solo, furry, anthro raccoon, (teal fur:1.3), (turquoise fur:1.1), (adult woman:1.2), (female:1.4), (feminine:1.2), round face, wide friendly smile, (adult proportions:1.1), (narrow waist:1.1), (wide hips:1.1), full thighs, (narrow shoulders:1.1), big round eyes, large dark pupils, red-brown eyes, eyelashes, flat chest, (featureless body:1.3), smooth fur body, navy blue raccoon mask markings, white muzzle, white inner ears, (pale cyan chest and belly:1.1), small spiky fur tufts on shoulders, navy hands, (flat even fur edge on forearms:1.2), navy lower legs, (pale cyan patch across back of hips:1.1), big ringed striped tail, (four navy rings:1.1), navy ring at the tail base, (navy tail tip:1.3), (digitigrade legs:1.3), (standing on toes:1.2), raccoon hind paws, slender raccoon hands, plain off-white background, concept art, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
(teal tail tip:1.3), (white tail tip:1.3), (zigzag tail rings:1.2), (child:1.3), (chibi:1.3), (skinny:1.2), (thigh highs:1.4), stockings, nsfw, sexual, suggestive, seductive, (male:1.4), (masculine:1.3), square jaw, (square body:1.3), (wide shoulders:1.3), (zigzag fur edge on forearms:1.2), angry, scowling, lipstick, makeup, muscular, (color swatches:1.3), lowres, worst quality, bad anatomy, bad hands, extra fingers, extra limbs, flat feet, plantigrade, shoes, clothes, apron, bag, accessories, jewelry, tiara, human, text, watermark, signature, blurry, scenery, gradient shading, (grey fur:1.2), charcoal grey, muted colors, desaturated, pastel colors, (green fur:1.2), mint green, (black fur:1.1), purple, (realistic:1.3), (detailed fur:1.2), (color palette:1.3), (multiple heads:1.3), head studies, bust, close-up, (props:1.3), objects, (hourglass:1.3), (arrows:1.2), symbols, icons, logo, (sketches:1.2), (extra tails:1.2), (devil tail:1.2)
```

## Output
Images go to `art/jobs/female-raccoon-001-teal-colour-wording/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.
