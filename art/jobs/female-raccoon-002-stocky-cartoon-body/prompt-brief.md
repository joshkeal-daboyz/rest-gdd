job: female-raccoon-002-stocky-cartoon-body
job-hash: 37f30b2e63c94401

# Reason for the change

**What we're trying to change:** Change only the body wording so her body matches the reference's stocky cartoon raccoon (big round head, thick (not short) limbs, simple soft torso, mild waist) instead of lanky human pin-up proportions, with the same seeds (20261027, 4 images).

**Why this job should do it:** BASE: female-raccoon-001-teal-colour-wording (Josh: off-track, 'the body is too human'). ONE change: body wording. Removed (adult proportions:1.1), (narrow waist:1.1), (wide hips:1.1), full thighs, which probably pushed the lanky curvy pin-up build, and 'slender raccoon hands'. Added (cartoon animal proportions:1.3), (stocky:1.1), big round head, thick arms, (thick legs:1.1), simple soft torso, thick raccoon hands (thick but not short: the reference's legs are about 0.44 of her height), so the body follows the reference's stocky cartoon shape. Female read kept with (mild waist:1.1), (wider hips:1.1), (narrow shoulders:1.1), (adult woman), (female:1.4), eyelashes; (featureless body:1.3) and smooth fur body stay. Negative adds (human proportions:1.3), (thin legs:1.2), (thin arms:1.1), (lanky:1.2) (replacing long legs, so thin limbs are pushed away without asking for short ones), (pin-up:1.2), (detailed anatomy:1.2), (tall:1.1) to push away the human body. Butt/backside terms were NOT put in the negative: the style guide's known faults say anatomy words in the negative set off a censor mark on the lower back. COLOUR IS DELIBERATELY UNTOUCHED this round: the teal/turquoise wording, navy, pale-cyan words and colour negatives are identical to the base even though the fur overshot to sky blue, so the body change is judged on its own. IP-Adapter (baseline.jpg, 0.8), canny (baseline-highres.png, 0.6, end 0.6), LoRA, seeds, size, steps, CFG and sampler are unchanged. Judge body shape and proportions only.

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`
- `art/female-raccoon/female-rules.md`

# Images to look at
- ControlNet image: `art/female-raccoon/baseline.jpg`
- ControlNet image: `art/female-raccoon/baseline-highres.png`
- reference: `art/female-raccoon/baseline-highres.png`
- earlier output of `female-raccoon-001-ipadapter-weight-wording`: `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-ipadapter-weight-wording`: `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/female-raccoon_20261028.png`
- earlier output of `female-raccoon-001-teal-colour-wording`: `art/jobs/female-raccoon-001-teal-colour-wording/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-teal-colour-wording`: `art/jobs/female-raccoon-001-teal-colour-wording/out/female-raccoon_20261028.png`

# Earlier jobs on this track
- `female-raccoon-001-baseline-ipadapter`: goal "A fresh female raccoon base-body sheet from Indigo Void (front, side, back on off-white) that keeps the look and palette of baseline-highres.png: teal fur, navy mask/sleeves/lower legs/four tail rings, mint chest and hip patch, hourglass build, digitigrade feet."; reviewer said partly; Josh's verdict off-track: Off-track; measured head 0.129-0.162, line 0.21-0.22%
- `female-raccoon-001-ipadapter-weight-wording`: goal "Same three-view sheet and seeds as female-raccoon-001-baseline-ipadapter, but with: teal #48C2C3 fur (not pale seafoam); a mint chest (not cream) and a mint hip patch, as in baseline-highres.png; navy that reads as blue #2A4365 (001's came out near-black/purple in all four); white inner ears; and no hourglasses, arrows, hooks, tiaras, devil tails, limb studies or logo tiles in the empty space."; reviewer said partly; Josh's verdict off-track: Off-track.; measured head 0.145-0.347, line 0.21-0.22%
- `female-raccoon-001-teal-colour-wording`: goal "Test colour wording (teal fur, pale-cyan chest/belly/muzzle/hip patch, navy blue markings) plus head size (0.19-0.21) and proportions from a canny edge guide on her own reference sheet."; reviewer said will help; Josh's verdict off-track: Body too human (lanky pin-up proportions, human buttocks/torso) vs the reference's stockier cartoon raccoon body; also fur overshot to sky blue, chest white, heads ~0.16, canny guide had little visible effect.; measured head 0.156-0.347, line 0.21-0.22%

# Earlier review rounds on this job
This job has had 1 earlier review round(s); at most 3 before it goes to Josh. Earlier rounds' must-fix items were applied unless the response says otherwise. Don't reverse a change an earlier round asked for unless you say exactly why that round was wrong. Put only real blockers under Must fix; anything else is Could improve.

## Round 1: partly, must-fix 1; Claude's response not recorded
What it asked for:
1. **Ask for thick limbs, not short ones, and push away thin limbs instead of long ones.** In `prompt`, replace `short thick limbs, short thick legs` with `thick arms, (thick legs:1.1)`, and replace `short thick raccoon hands` with `thick raccoon hands`. In `negative`, replace `(long legs:1.3)` with `(thin legs:1.2), (thin arms:1.1), (lanky:1.2)`. Expected effect: the tube-like cartoon limbs of the reference at the proportions the rules require, instead of a squat body that clashes with the `chibi`/`child` negatives and breaks "legs nearly half the body".


# The job, explained

# Forge job female-raccoon-002-stocky-cartoon-body

**Asset:** female-raccoon | **Track:** female-baseline | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Change only the body wording so her body matches the reference's stocky cartoon raccoon (big round head, thick (not short) limbs, simple soft torso, mild waist) instead of lanky human pin-up proportions, with the same seeds (20261027, 4 images).

## Why this job should do it
BASE: female-raccoon-001-teal-colour-wording (Josh: off-track, 'the body is too human'). ONE change: body wording. Removed (adult proportions:1.1), (narrow waist:1.1), (wide hips:1.1), full thighs, which probably pushed the lanky curvy pin-up build, and 'slender raccoon hands'. Added (cartoon animal proportions:1.3), (stocky:1.1), big round head, thick arms, (thick legs:1.1), simple soft torso, thick raccoon hands (thick but not short: the reference's legs are about 0.44 of her height), so the body follows the reference's stocky cartoon shape. Female read kept with (mild waist:1.1), (wider hips:1.1), (narrow shoulders:1.1), (adult woman), (female:1.4), eyelashes; (featureless body:1.3) and smooth fur body stay. Negative adds (human proportions:1.3), (thin legs:1.2), (thin arms:1.1), (lanky:1.2) (replacing long legs, so thin limbs are pushed away without asking for short ones), (pin-up:1.2), (detailed anatomy:1.2), (tall:1.1) to push away the human body. Butt/backside terms were NOT put in the negative: the style guide's known faults say anatomy words in the negative set off a censor mark on the lower back. COLOUR IS DELIBERATELY UNTOUCHED this round: the teal/turquoise wording, navy, pale-cyan words and colour negatives are identical to the base even though the fur overshot to sky blue, so the body change is judged on its own. IP-Adapter (baseline.jpg, 0.8), canny (baseline-highres.png, 0.6, end 0.6), LoRA, seeds, size, steps, CFG and sampler are unchanged. Judge body shape and proportions only.

## What Forge will do
Draw 4 new image(s) from the prompt, starting from noise.
ControlNet `CLIP-ViT-H (IPAdapter)` / `ip-adapter-plus_sdxl_vit-h` at weight 0.8, using `art/female-raccoon/baseline.jpg`. Reference image: carries the female baseline's look, palette and flat style without copying its layout.
ControlNet `canny` / `diffusion_pytorch_model_V2` at weight 0.6, using `art/female-raccoon/baseline-highres.png`. Edge guide from her own reference sheet (Josh, 2026-10-27): Forge takes the outlines at generation time to fix head size and proportions. Nothing is drawn or edited.

## Settings
- Model: `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`
- LoRAs: `charsheet_lora_v1:0.6` (approved weight 0.6, trigger `charsheet`)
- 30 steps, CFG 6, sampler Euler a, scheduler Automatic, size 1536x1024
- Fixed for every job: sd_vae Automatic, CLIP_stop_at_last_layers 1, eta_noise_seed_delta 0, randn_source GPU, token_merging_ratio 0
- Seed: 20261027, counting up per image

## Prompt
Compared with job `female-raccoon-001-teal-colour-wording`:
- added: `(cartoon animal proportions:1.3)`
- added: `(stocky:1.1)`
- added: `big round head`
- added: `thick arms`
- added: `(thick legs:1.1)`
- added: `simple soft torso`
- added: `(mild waist:1.1)`
- added: `(wider hips:1.1)`
- added: `thick raccoon hands`
- removed: `(adult proportions:1.1)`
- removed: `(narrow waist:1.1)`
- removed: `(wide hips:1.1)`
- removed: `full thighs`
- removed: `slender raccoon hands`

```
charsheet, masterpiece, best quality, (character reference sheet:1.3), (turnaround:1.2), front view, side view, back view, same character three times, (three views:1.2), (toon style:1.2), thick outlines, simple shapes, minimal fur detail, flat colors, (vivid colors:1.1), clean bold outlines, cartoon, full body, standing, relaxed pose, weight on one leg, arms slightly away from body, solo, furry, anthro raccoon, (teal fur:1.3), (turquoise fur:1.1), (adult woman:1.2), (female:1.4), (feminine:1.2), round face, wide friendly smile, (cartoon animal proportions:1.3), (stocky:1.1), big round head, thick arms, (thick legs:1.1), simple soft torso, (mild waist:1.1), (wider hips:1.1), (narrow shoulders:1.1), big round eyes, large dark pupils, red-brown eyes, eyelashes, flat chest, (featureless body:1.3), smooth fur body, navy blue raccoon mask markings, pale cyan muzzle, white inner ears, (pale cyan chest and belly:1.1), small spiky fur tufts on shoulders, navy blue hands, (flat even fur edge on forearms:1.2), navy blue lower legs, (pale cyan patch across back of hips:1.1), big ringed striped tail, (four navy blue rings:1.1), navy blue ring at the tail base, (navy blue tail tip:1.3), (digitigrade legs:1.3), (standing on toes:1.2), raccoon hind paws, thick raccoon hands, plain off-white background, concept art, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
(teal tail tip:1.3), (white tail tip:1.3), (zigzag tail rings:1.2), (child:1.3), (chibi:1.3), (skinny:1.2), (human proportions:1.3), (thin legs:1.2), (thin arms:1.1), (lanky:1.2), (pin-up:1.2), (detailed anatomy:1.2), (tall:1.1), (thigh highs:1.4), stockings, nsfw, sexual, suggestive, seductive, (male:1.4), (masculine:1.3), square jaw, (square body:1.3), (wide shoulders:1.3), (zigzag fur edge on forearms:1.2), angry, scowling, lipstick, makeup, muscular, (color swatches:1.3), lowres, worst quality, bad anatomy, bad hands, extra fingers, extra limbs, flat feet, plantigrade, shoes, clothes, apron, bag, accessories, jewelry, tiara, human, text, watermark, signature, blurry, scenery, gradient shading, (grey fur:1.2), charcoal grey, muted colors, desaturated, (cream fur:1.2), beige, (green fur:1.2), mint green, (black fur:1.1), purple, (realistic:1.3), (detailed fur:1.2), (color palette:1.3), (multiple heads:1.3), head studies, bust, close-up, (props:1.3), objects, (hourglass:1.3), (arrows:1.2), symbols, icons, logo, (sketches:1.2), (extra tails:1.2), (devil tail:1.2)
```

## Output
Images go to `art/jobs/female-raccoon-002-stocky-cartoon-body/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: 37f30b2e63c94401


# Settings a job can use

```
Top-level job fields: asset, compare_to, controlnet, count, follows, goal, hires, kind, loras, mask, mode, model, negative, parent, prompt, settings, track, upscale, why

settings:
  seed: -1 for random; a fixed number repeats an image (consecutive seeds per image)
  steps: sampling steps (default 30)
  cfg_scale: how strictly the prompt is followed (default 6)
  sampler_name: default Euler a
  scheduler: default Automatic
  width: txt2img size; for img2img/inpaint, the size Forge draws at (default: the parent's)
  height: as width
  denoising_strength: img2img/inpaint: 0 keeps the parent, 1 replaces it
  inpainting_fill: inpaint: 1 starts from the original (default), 0 fill, 2 latent noise, 3 latent nothing
  mask_blur: inpaint: soften the mask edge, in pixels (default 4)
  inpaint_full_res: inpaint: true draws only the masked area, at width x height
  inpaint_full_res_padding: inpaint with inpaint_full_res: pixels of context around the mask
  hr_denoise: hires fix: denoise of the second pass (default 0.35)
  hr_upscaler: hires fix: an approved upscaler (default the first approved)

controlnet (a list; one entry per unit):
  module: preprocessor: canny (edge guide from an image), None (image is already an edge map), CLIP-ViT-H (IPAdapter) (reference)
  model: an approved ControlNet model
  image: repo path of the guide or reference image
  weight: strength, about 0.3-1.0
  guidance_start: fraction of the steps where it starts (0-1, default 0)
  guidance_end: fraction of the steps where it stops (0-1, default 1)
  control_mode: Balanced | My prompt is more important | ControlNet is more important
  resize_mode: Crop and Resize (default) | Resize and Fill | Just Resize
  pixel_perfect: true (default) sizes the preprocessor to the image
  processor_res: preprocessor resolution, when pixel_perfect is false
  threshold_a: canny low threshold
  threshold_b: canny high threshold
  purpose: plain words: what this unit is for (shown in explain.md, not sent to Forge)

upscale (upscale mode): scale, upscaler
hires: a number such as 1.5 turns on hires fix (large job)
```