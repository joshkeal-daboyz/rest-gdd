job: female-raccoon-001-teal-colour-wording
job-hash: a575de196e6cf0a7

# Reason for the change

**What we're trying to change:** Test colour wording (teal fur, pale-cyan chest/belly/muzzle/hip patch, navy blue markings) plus head size (0.19-0.21) and proportions from a canny edge guide on her own reference sheet.

**Why this job should do it:** BASE: female-raccoon-001-ipadapter-weight-wording (Josh: off-track). Colour wording is as in the prompt already here (teal fur:1.3, pale cyan, navy blue; negative blocks cream, black, purple). Two other changes from the base: the IP-Adapter reference is baseline.jpg at 0.8 (Josh), and a canny ControlNet (diffusion_pytorch_model_V2) on baseline-highres.png at weight 0.6, steps 0 to 0.6, takes her outlines from the approved sheet so the head and body proportions follow it; the high-res file is used so edges stay sharp at 1536x1024. Prompt, negative, seeds, LoRA, size, steps, CFG and sampler are unchanged. KEY RISK: canny copies the reference layout, which has four figures, colour swatches and a side bust, against the three-view goal. If the outputs show four figures, swatches or a bust, that is the guide copying the layout, not the prompt failing: judge head size, proportions and colour only, and the next job should lower the weight or end step, or Josh should supply a three-view-only guide. If the outputs are three views with a right-sized head, the guide works. Colour differences may partly come from the guide or the changed reference, not only the wording.

Judge the job against this reason.

# Rules to check
- `art/raccoon-style-guide.md`
- `art/female-raccoon/female-rules.md`

# Images to look at
- ControlNet image: `art/female-raccoon/baseline.jpg`
- ControlNet image: `art/female-raccoon/baseline-highres.png`
- reference: `art/female-raccoon/baseline-highres.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-baseline-ipadapter`: `art/jobs/female-raccoon-001-baseline-ipadapter/out/female-raccoon_20261028.png`
- earlier output of `female-raccoon-001-ipadapter-weight-wording`: `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/female-raccoon_20261027.png`
- earlier output of `female-raccoon-001-ipadapter-weight-wording`: `art/jobs/female-raccoon-001-ipadapter-weight-wording/out/female-raccoon_20261028.png`

# Earlier jobs on this track
- `female-raccoon-001-baseline-ipadapter`: goal "A fresh female raccoon base-body sheet from Indigo Void (front, side, back on off-white) that keeps the look and palette of baseline-highres.png: teal fur, navy mask/sleeves/lower legs/four tail rings, mint chest and hip patch, hourglass build, digitigrade feet."; reviewer said partly; Josh's verdict off-track: Off-track; measured head 0.129-0.162, line 0.21-0.22%
- `female-raccoon-001-ipadapter-weight-wording`: goal "Same three-view sheet and seeds as female-raccoon-001-baseline-ipadapter, but with: teal #48C2C3 fur (not pale seafoam); a mint chest (not cream) and a mint hip patch, as in baseline-highres.png; navy that reads as blue #2A4365 (001's came out near-black/purple in all four); white inner ears; and no hourglasses, arrows, hooks, tiaras, devil tails, limb studies or logo tiles in the empty space."; reviewer said partly; Josh's verdict off-track: Off-track.; measured head 0.145-0.347, line 0.21-0.22%

# Earlier review rounds on this job
This job has had 5 earlier review round(s); at most 3 before it goes to Josh. Earlier rounds' must-fix items were applied unless the response says otherwise. Don't reverse a change an earlier round asked for unless you say exactly why that round was wrong. Put only real blockers under Must fix; anything else is Could improve.

## Round 1: partly, must-fix ?; Claude's response not recorded
What it asked for:
1. **Use blue-leaning words for the pale areas instead of "mint":** `pale cyan muzzle`, `(pale cyan chest and belly:1.2)`, `(pale cyan patch across back of hips:1.1)`. Expected effect: the chest and hip patch move toward #D0FFFA without bleeding green into the main fur, so fur and chest stay distinct.
2. **Reinforce the fur hue with a second common colour tag:** `(teal fur:1.3), (turquoise fur:1.1)`, and add `(green fur:1.2), mint green` to the negative. Expected effect: pushes the fur from sage toward blue-green #48C2C3. "Turquoise" is a well-tagged colour on the checkpoint's training sources, and "teal" alone has produced sage twice.
3. **Say "blue" for the markings:** `(navy blue:1.2)` once near the markings (for example `navy blue raccoon mask markings`), and add `(black:1.1), purple` to the negative. Leave the tail-tip and ring tags as they are. Expected effect: the markings read as blue #2A4365, not black or purple.
4. **Optional, cleaner test:** keep the IP-Adapter at 0.8 and set its start later (guidance start of about 0.25–0.3, if job.json and forge_jobs.py pass it through), instead of cutting the weight to 0.6. Expected effect: the reference still carries colour and style but has less say over early layout, which is where the swatches and busts come from. If that field isn't supported, run as 0.6, but read a colour failure as "wording *or* weight" as the brief says.
5. **Optional:** add `monochrome, uncolored` to the negative to catch the line-only sketches seen in 

## Round 2: partly, must-fix ?; Claude's response not recorded
What it asked for:
1. **Make this job test colour only: set the IP-Adapter weight back to 0.8.** Keep the colour wording changes and `(color swatches:1.3)`; the negative change barely affects colour. Expected effect: any change in fur, chest or navy colour, relative to the weight-wording outputs on the same seeds, can be traced to the wording. Test the leaks in the next job.
2. **Ask for saturation, not just a hue.** Add `(vivid colors:1.1)` after `flat colors`, and add `muted colors, desaturated, pastel colors` to the negative. Expected effect: fur moves from pastel seafoam toward the strong #48C2C3, and navy away from grey-black.
3. **Cut the pale bleed.** Lower `(pale cyan chest and belly:1.2)` to `1.1`, and change `pale cyan muzzle` to `white muzzle`. White is the actual colour of the reference's muzzle area, and inner ears are already white. Expected effect: fewer "pale" tokens pulling the body colour light, while the chest still differs from cream.
4. **Optional, part of the same colour lever:** replace `(turquoise fur:1.1)` with `(teal body:1.1)`, the e621 tag form this NoobAI-based checkpoint is more likely to have learned, and write the hands, legs and rings as `dark blue` instead of `navy` (for example `dark blue hands`, `dark blue lower legs`, `(four dark blue rings:1.1)`, `(dark blue tail tip:1.3)`). Expected effect: blue markings rather than purple-black. If you'd rather keep this job smaller, leave this for the next job.
5. **For the next (leak) job, not this one:** at IP weight 0

## Round 3: partly, must-fix ?; Claude's response not recorded
What it asked for:
1. **Remove `pastel colors` from the negative** and keep `muted colors, desaturated`. Effect: the negative stops pushing against the pale-cyan chest, and the fur is still pushed toward saturated colour.
2. **Add `(cream fur:1.2), beige` to the negative.** Effect: this aims straight at the cream chest seen in all earlier outputs, without changing the off-white background word the style guide asks for.
3. **Change `navy hands`, `navy lower legs`, `(four navy rings:1.1)`, `navy ring at the tail base` and `(navy tail tip:1.3)` to use "navy blue"**, keeping the existing weights. For example: `navy blue hands`, `(navy blue tail tip:1.3)`. Effect: all markings get the same blue cue the mask gets, so the "blue, not black" test covers all of them and not only the mask. A small blue spill onto the fur would push it toward cyan, which is acceptable.
4. **Change `white muzzle` to `pale cyan muzzle`, or remove the muzzle word.** Effect: the job follows the style guide's mint muzzle and doesn't add an unrequested change. If Josh actually wants a white muzzle, as in the reference, that is his decision.
5. Optional: **change `(turquoise fur:1.1)` to `(aqua fur:1.1)`.** "aqua" is a common colour tag in Danbooru-trained models such as NoobAI and is probably read more reliably than "turquoise". Expected effect: a slightly stronger cyan-teal fur.

## Round 4: partly, must-fix ?; Claude's response not recorded
What it asked for:
1. **Restore `pastel colors` to the negative**, at plain weight (no brackets). Expected effect: keeps pressure against the washed-out fur that made both earlier jobs off-track. The belly's light tint can come from the IP-Adapter reference rather than the prompt.
2. **Cut the `pale` tokens.** Replace `pale cyan` with `light cyan` and say it once for the front: `(light cyan chest and belly:1.1), light cyan muzzle`. For the back, use `(light cyan patch on back of hips:1.1)`. Expected effect: less lightness bleeding onto the main fur, while still asking for a cool, non-cream belly. If you'd rather keep this a pure navy and teal test, leave this one out and accept the bleed risk.
3. **Optionally raise teal to `(teal fur:1.4)`**, still under 1.5, and keep `(turquoise fur:1.1)`. Expected effect: more saturation weight on the largest area. Only do this if recommendation 1 is applied, so the two don't double-push.
4. **Keep everything else as written**: the seeds, IP-Adapter 0.8, the LoRA, `navy blue` throughout, and `(cream fur:1.2), beige`.

## Round 5: partly, must-fix ?; Claude agreed: Ready to run. Reference swap to baseline.jpg confirmed as a near-neutral change. Recs 1-2 (black markings / white chest in negative, weighted mask) fit female-rules.md but are small; I'd run now and fold them into the next job if chest or markings miss. Josh may choose to apply them first.
What it asked for:
1. Add `(black markings:1.2), white chest` to the negative, as the female rules ask. Expected effect: markings pushed further toward blue, and no fall-back from cream to pure white on the chest. These are colour words only, so the job stays a single test.
2. Raise the face marking to `(navy blue raccoon mask markings:1.1)` so it matches the weighted tail and tip. Expected effect: a bluer mask, so the front view can be judged on the blue-versus-black question.
3. Optional. If Josh wants to guard the fur goal now instead of next round: reduce the pale-cyan bleed by naming it once as a contrast, e.g. `(pale cyan chest and belly:1.1)` and `pale cyan muzzle`, and changing the hip term to `(light cyan patch across back of hips:1.2)`. Expected effect: less pale wash on the body, and a stronger push for the hip patch that has never appeared. If Josh doesn't take this, run without it and judge fur lightness against chest colour on the outputs.


# The job, explained

# Forge job female-raccoon-001-teal-colour-wording

**Asset:** female-raccoon | **Track:** female-baseline | **Kind:** character-sheet | **Size:** small (4 images)

## What we're trying to change
Test colour wording (teal fur, pale-cyan chest/belly/muzzle/hip patch, navy blue markings) plus head size (0.19-0.21) and proportions from a canny edge guide on her own reference sheet.

## Why this job should do it
BASE: female-raccoon-001-ipadapter-weight-wording (Josh: off-track). Colour wording is as in the prompt already here (teal fur:1.3, pale cyan, navy blue; negative blocks cream, black, purple). Two other changes from the base: the IP-Adapter reference is baseline.jpg at 0.8 (Josh), and a canny ControlNet (diffusion_pytorch_model_V2) on baseline-highres.png at weight 0.6, steps 0 to 0.6, takes her outlines from the approved sheet so the head and body proportions follow it; the high-res file is used so edges stay sharp at 1536x1024. Prompt, negative, seeds, LoRA, size, steps, CFG and sampler are unchanged. KEY RISK: canny copies the reference layout, which has four figures, colour swatches and a side bust, against the three-view goal. If the outputs show four figures, swatches or a bust, that is the guide copying the layout, not the prompt failing: judge head size, proportions and colour only, and the next job should lower the weight or end step, or Josh should supply a three-view-only guide. If the outputs are three views with a right-sized head, the guide works. Colour differences may partly come from the guide or the changed reference, not only the wording.

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
Compared with job `female-raccoon-001-ipadapter-weight-wording`:
- added: `(vivid colors:1.1)`
- added: `(teal fur:1.3)`
- added: `(turquoise fur:1.1)`
- added: `navy blue raccoon mask markings`
- added: `pale cyan muzzle`
- added: `(pale cyan chest and belly:1.1)`
- added: `navy blue hands`
- added: `navy blue lower legs`
- added: `(pale cyan patch across back of hips:1.1)`
- added: `(four navy blue rings:1.1)`
- added: `navy blue ring at the tail base`
- added: `(navy blue tail tip:1.3)`
- removed: `teal fur`
- removed: `dark navy raccoon mask markings`
- removed: `pale mint muzzle`
- removed: `pale mint belly`
- removed: `dark navy hands`
- removed: `dark navy lower legs`
- removed: `(pale mint patch on lower back:1.1)`
- removed: `(four navy rings:1.1)`
- removed: `navy ring at the tail base`
- removed: `(dark navy tail tip:1.3)`

```
charsheet, masterpiece, best quality, (character reference sheet:1.3), (turnaround:1.2), front view, side view, back view, same character three times, (three views:1.2), (toon style:1.2), thick outlines, simple shapes, minimal fur detail, flat colors, (vivid colors:1.1), clean bold outlines, cartoon, full body, standing, relaxed pose, weight on one leg, arms slightly away from body, solo, furry, anthro raccoon, (teal fur:1.3), (turquoise fur:1.1), (adult woman:1.2), (female:1.4), (feminine:1.2), round face, wide friendly smile, (adult proportions:1.1), (narrow waist:1.1), (wide hips:1.1), full thighs, (narrow shoulders:1.1), big round eyes, large dark pupils, red-brown eyes, eyelashes, flat chest, (featureless body:1.3), smooth fur body, navy blue raccoon mask markings, pale cyan muzzle, white inner ears, (pale cyan chest and belly:1.1), small spiky fur tufts on shoulders, navy blue hands, (flat even fur edge on forearms:1.2), navy blue lower legs, (pale cyan patch across back of hips:1.1), big ringed striped tail, (four navy blue rings:1.1), navy blue ring at the tail base, (navy blue tail tip:1.3), (digitigrade legs:1.3), (standing on toes:1.2), raccoon hind paws, slender raccoon hands, plain off-white background, concept art, <lora:charsheet_lora_v1:0.6>
```

Negative:
```
(teal tail tip:1.3), (white tail tip:1.3), (zigzag tail rings:1.2), (child:1.3), (chibi:1.3), (skinny:1.2), (thigh highs:1.4), stockings, nsfw, sexual, suggestive, seductive, (male:1.4), (masculine:1.3), square jaw, (square body:1.3), (wide shoulders:1.3), (zigzag fur edge on forearms:1.2), angry, scowling, lipstick, makeup, muscular, (color swatches:1.3), lowres, worst quality, bad anatomy, bad hands, extra fingers, extra limbs, flat feet, plantigrade, shoes, clothes, apron, bag, accessories, jewelry, tiara, human, text, watermark, signature, blurry, scenery, gradient shading, (grey fur:1.2), charcoal grey, muted colors, desaturated, (cream fur:1.2), beige, (green fur:1.2), mint green, (black fur:1.1), purple, (realistic:1.3), (detailed fur:1.2), (color palette:1.3), (multiple heads:1.3), head studies, bust, close-up, (props:1.3), objects, (hourglass:1.3), (arrows:1.2), symbols, icons, logo, (sketches:1.2), (extra tails:1.2), (devil tail:1.2)
```

## Output
Images go to `art/jobs/female-raccoon-001-teal-colour-wording/out/` exactly as Forge returns them. Nothing is edited afterwards; only the job id is written into each file's PNG notes.

job-hash: a575de196e6cf0a7


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