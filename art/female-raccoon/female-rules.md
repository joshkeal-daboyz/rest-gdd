# Female raccoon: character rules

**Approved reference sheet:** [baseline-highres.png](baseline-highres.png). Every new image of the female raccoon should match it. It also sets the palette and art style for every raccoon.

The rules shared by every raccoon are in the [raccoon style guide](../raccoon-style-guide.md). This file adds what's specific to her, and what her Forge jobs have taught us so far. When an image breaks a rule, it gets regenerated in Forge, never patched by hand or by a script.

## Body

- **Hourglass torso:** the waist pinches in and the hips flare out wider than the waist. This is the main thing that makes her read as female.
- Wide hips and full thighs. Shoulders narrower than the hips.
- Adult proportions, as in the style guide: head about 0.19–0.21 of her height, fingertips at mid-thigh, legs nearly half her height.
- **Height:** the baseline. Enoch is about 5% taller.
- **Stance:** a softer pose; her weight can shift to one side.
- Digitigrade: on her toes, with raccoon hind paws. Never flat feet.

## Face and eyes

- A rounder face with a wide, friendly smile. Never angry or scowling.
- Big round eyes with large dark pupils and eyelashes on the upper lids.
- The lower half of each pupil is red-brown `#8D3F4C`, with a small white shine at the top.

## Colours and markings

Her sheet is where the style guide's palette was sampled, so she uses it exactly.

| Part | Colour |
| --- | --- |
| Fur | Teal `#48C2C3` |
| Mask, hands, lower legs, tail rings and tip | Navy `#2A4365` (a clear blue, not near-black or purple) |
| Muzzle, chest, belly, and the patch across the back of the hips | Mint `#D0FFFA` (pale cyan, not cream or white) |
| Inner ears, eye whites | White |
| Iris | Red-brown `#8D3F4C` |

- **Sleeves:** the navy on her forearms starts with a **flat, even edge**, not a zigzag.
- **Back view:** a mint patch across the back of the hips, and a visible curve at the small of the back.
- Tail: exactly four navy rings from a navy base to a navy tip, as in the style guide.

## Making new images of her

Every new image goes through the Forge job pipeline in the [style guide](../raccoon-style-guide.md#making-and-changing-raccoon-art). Use asset names starting with `female-raccoon` so the brief finds this file.

- **Model:** `indigoVoidFurryFusedXL_noobaiV35_fp16.safetensors`, as for every character.
- **Character sheets:** add `charsheet_lora_v1` at 0.6 with the trigger word `charsheet`. Start from [female.prompt.txt](female.prompt.txt) and [female.negative.txt](female.negative.txt).
- **Reference:** IP-Adapter (`ip-adapter-plus_sdxl_vit-h`, module `CLIP-ViT-H (IPAdapter)`) on [baseline-highres.png](baseline-highres.png) carries her overall look. On its own it doesn't hold the colours (see below).
- **Edge guide:** her own reference sheet (Josh's decision, 2026-10-27). Run the canny ControlNet (`diffusion_pytorch_model_V2`, module `canny`) on [baseline-highres.png](baseline-highres.png), so Forge takes her outlines from it at generation time. Nothing is drawn or edited. Start around weight 0.6, ending at 0.6, as for Enoch's guide. This should fix head size and proportions; it also copies the reference's layout and poses, so it suits reruns of her sheet rather than new poses. Not yet tested in a job. Never use Enoch's guide: it's male-shaped and pushes her toward a square torso.

## What her jobs have taught us

From the `female-raccoon-001` jobs (IP-Adapter at 0.5 and 0.8, no edge guide), all marked off-track:

- **Colours drift even with the reference.** Teal came out pale seafoam, the chest cream, and the navy near-black or purple. Name the colours plainly in the prompt (teal fur; pale cyan or mint chest; navy blue markings) and put `cream`, `white chest`, `black markings` and `purple` in the negative.
- **Stray objects fill the empty space** around the figures: hourglasses, arrows, hooks, tiaras, devil tails, limb studies, logo tiles. The hourglasses are probably the prompt's `hourglass figure` being drawn literally. Describe her shape instead ("narrow waist, wide hips, full thighs"), and put `props`, `objects`, `symbols`, `icons` and `extra drawings` in the negative.
- **Head size** hasn't been tested yet. The next job should add the canny edge guide on her reference sheet.

From `female-raccoon-001-teal-colour-wording` (IP-Adapter 0.8 on baseline.jpg, canny 0.6 ending at 0.6 on baseline-highres.png), off-track. Josh: "the body is too human."

- **Body too human.** Lanky pin-up proportions, long human legs and a detailed human backside and torso, far from the reference's stockier cartoon raccoon body. The curvy wording (`narrow waist`, `wide hips`, `full thighs`) probably pushes this.
- **Colour overshoots.** `(teal fur:1.3)` plus `(turquoise fur:1.1)` turned the fur sky or cyan blue. `navy blue` on every marking fixed the navy. The chest came out white rather than mint.
- **The canny guide barely shaped the figures.** Forge recorded the canny unit as applied, but the poses and layout followed the seed, not the reference, and heads stayed about 0.16. Why is still unknown.

From `female-raccoon-002-stocky-cartoon-body` (only the body wording changed: stocky, thick limbs, mild waist; `human proportions`, `pin-up`, `lanky`, `detailed anatomy` in the negative), off-track. Josh: "it looks like a chubby woman with a raccoon head."

- **Body wording alone doesn't make her a cartoon raccoon.** The stocky words added flesh to a human body: breasts, a belly and a human backside. They didn't give her the reference's simple cartoon shape. The human body probably comes from the model, the LoRA or the IP-Adapter, not the prompt alone.
- **`detailed anatomy` in the negative** probably drew the lower-back censor mark on one image. Keep anatomy words out of the negative.
- The canny guide at 0.6 (ending at 0.6) still didn't visibly shape the figures.

Add a line here after each verdict on her jobs, so the next job starts from what was learned.

## Review checklist

Check every image of her against the style guide's checklist, plus:

1. Hourglass torso: waist pinched in, hips wider than the waist, shoulders narrower than the hips.
2. Flat, even sleeve edges.
3. Eyelashes, large dark pupils with a red-brown lower half.
4. Mint (not cream) chest, belly, muzzle and back-of-hips patch; navy that reads as blue.
5. Nothing in the empty space around the figures.
