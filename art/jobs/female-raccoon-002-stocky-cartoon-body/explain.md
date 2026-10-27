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
