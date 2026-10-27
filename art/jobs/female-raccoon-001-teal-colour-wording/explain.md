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
