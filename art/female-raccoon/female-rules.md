# Female raccoon: character rules

**Approved reference sheet:** [female-raccoon-003-img2img-sheet-recipe_female-raccoon_331506249.png](../locked/female-raccoon/female-raccoon-003-img2img-sheet-recipe_female-raccoon_331506249.png) (locked 2026-10-27, Josh's pick from job `female-raccoon-003-img2img-sheet-recipe`). Every new image of the female raccoon should match it. A change to it is a new job with this locked copy as its parent.

The earlier sheet, [baseline-highres.png](baseline-highres.png), stays as history. The style guide's palette was sampled from it, and the proven sheet recipe below was first run on it.

The rules shared by every raccoon are in the [raccoon style guide](../raccoon-style-guide.md). This file adds what's specific to her, and what her Forge jobs have taught us so far. When an image breaks a rule, it gets regenerated in Forge, never patched by hand or by a script.

## Body

- **A mild hourglass, as on her sheet:** the waist pinches in gently and the hips are a little wider than the waist. This is the main thing that makes her read as female.
- A soft, simple cartoon raccoon body with tube-like limbs and no anatomical detail. Shoulders narrower than the hips.
- **In prompts, say `mild waist, soft rounded body, wider hips`.** `hourglass figure`, `wide hips`, `full thighs`, `narrow waist` and `stocky` all gave her a human pin-up or chubby human body (see "What her jobs have taught us").
- Adult proportions, as in the style guide: head about 0.19–0.21 of her height, fingertips at mid-thigh, legs nearly half her height.
- **Height:** the baseline. Enoch is about 5% taller.
- **Stance:** a softer pose; her weight can shift to one side.
- Digitigrade: on her toes, with raccoon hind paws. Never flat feet.

### Reference measurements

Measured 2026-10-27 on her front (leftmost) figure, with the pipeline's read-only scripts `art/tools/measure_head.py` and `art/tools/line_width.py` (the same ones `run` and `measure` use on job outputs):

| Image | Size | Head (ears to neck ÷ ears to feet) | Line weight (outline ÷ figure height) |
| --- | --- | --- | --- |
| [baseline-highres.png](baseline-highres.png) | 3064×2024 | **0.210** | **0.33%** (6.3 px on a 1943 px figure) |
| [baseline.jpg](baseline.jpg) | 766×506 | **0.210** | 0.41% (2.0 px on a 486 px figure) |
| [Locked sheet](../locked/female-raccoon/female-raccoon-003-img2img-sheet-recipe_female-raccoon_331506249.png) (the approved reference) | 1536×1016 | **0.210** | 0.20% (from `run`'s measurement) |

- **Head:** 0.21 on both, and about 0.20 by eye. Outputs should land at 0.19–0.21. This is a measurement of the reference's front figure only; on sheets with loose head studies the script can pick the wrong figure.
- **Line weight depends on image size.** Outlines can't get much thinner than about 2 px, so small images read heavier. 0.33% is the target for outputs about 1536 px wide and larger (a 6.3 px line at 3064 px is about 3 px at 1536 px). The 0.41% on the 766 px jpg comes from its small size, so don't use it as a target. The locked sheet's lines are thinner, at 0.20%. The pipeline still targets 0.33% and flags anything under 0.25% as thin. Josh hasn't decided whether the thinner lines are acceptable.

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
### Character sheets: the proven recipe

Job [`female-raccoon-003-img2img-sheet-recipe`](../jobs/female-raccoon-003-img2img-sheet-recipe/job.json) is the first of her jobs Josh marked on-track ("this is wonderful", 2026-10-27). Start every new sheet of her from it (`new female-raccoon <track> <slug> --from female-raccoon-003-img2img-sheet-recipe`) and change one thing at a time.

- **img2img, not txt2img.** Parent: her approved sheet, at denoise **0.65**, size 1536×1016 (her sheet's aspect ratio). The recipe was proven with [baseline-highres.png](baseline-highres.png) as the parent. For changes to her sheet from now on, the parent is the locked sheet above. The parent carries her cartoon body, head size and palette. All four txt2img jobs gave her a human body whatever the prompt said.
- **Prompt:** [female-sheet.prompt.txt](female-sheet.prompt.txt) and [female-sheet.negative.txt](female-sheet.negative.txt). The prompt is short tags in BREAK chunks, built like Enoch's on-track job `enoch-sheet-005-less-human`: style and layout, eyes, colours, markings and tail, fur and paws, build. The fur-and-paws chunk and the negative's `human, (human-like:1.2), human proportions, skin-tight` keep her a raccoon. There are no body-part words in the negative.
- **Model and LoRA:** Indigo Void with `charsheet_lora_v1` at 0.6, trigger `charsheet` first. Euler a, 30 steps, CFG 6.
- **No IP-Adapter and no canny guide.** The parent already carries her look, so an IP-Adapter on the same image only adds a second pull from one source.
- The old [female.prompt.txt](female.prompt.txt) and [female.negative.txt](female.negative.txt) are the long txt2img prompts that failed. Don't start from them.

### Other tools, and how they did

- **Reference (IP-Adapter)** `ip-adapter-plus_sdxl_vit-h`, module `CLIP-ViT-H (IPAdapter)`. In txt2img at 0.5 and 0.8 it didn't hold her colours, and at 0.8 it copied the sheet's swatches, bust and extra figures. If one is needed, use Enoch's settings: 0.4, ending at 0.6, resize mode "Resize and Fill".
- **Edge guide:** canny (`diffusion_pytorch_model_V2`, module `canny`) on her own sheet, at weight 0.6 ending at 0.6. Tested in two txt2img jobs, it didn't visibly shape the figures, and why is still unknown. The proven recipe doesn't use it. Never use Enoch's guide: it's male-shaped and pushes her toward a square torso.

## What her jobs have taught us

From the `female-raccoon-001` jobs (IP-Adapter at 0.5 and 0.8, no edge guide), all marked off-track:

- **Colours drift even with the reference.** Teal came out pale seafoam, the chest cream, and the navy near-black or purple. Name the colours plainly in the prompt (teal fur; pale cyan or mint chest; navy blue markings) and put `cream`, `white chest`, `black markings` and `purple` in the negative.
- **Stray objects fill the empty space** around the figures: hourglasses, arrows, hooks, tiaras, devil tails, limb studies, logo tiles. The hourglasses are probably the prompt's `hourglass figure` being drawn literally. Put `props`, `objects`, `symbols`, `icons` and `extra drawings` in the negative. *(Superseded: this lesson first suggested "narrow waist, wide hips, full thighs" instead; those words gave her a human body. Use the body words under Body above.)*
- *(Superseded: head size was untested here, and the plan was a canny guide. Job 003's img2img recipe fixed head size instead; see below.)*

From `female-raccoon-001-teal-colour-wording` (IP-Adapter 0.8 on baseline.jpg, canny 0.6 ending at 0.6 on baseline-highres.png), off-track. Josh: "the body is too human."

- **Body too human.** Lanky pin-up proportions, long human legs and a detailed human backside and torso, far from the reference's stockier cartoon raccoon body. The curvy wording (`narrow waist`, `wide hips`, `full thighs`) probably pushes this.
- **Colour overshoots.** `(teal fur:1.3)` plus `(turquoise fur:1.1)` turned the fur sky or cyan blue. `navy blue` on every marking fixed the navy. The chest came out white rather than mint.
- **The canny guide barely shaped the figures.** Forge recorded the canny unit as applied, but the poses and layout followed the seed, not the reference, and heads stayed about 0.16. Why is still unknown.

From `female-raccoon-002-stocky-cartoon-body` (only the body wording changed: stocky, thick limbs, mild waist; `human proportions`, `pin-up`, `lanky`, `detailed anatomy` in the negative), off-track. Josh: "it looks like a chubby woman with a raccoon head."

- **Body wording alone doesn't make her a cartoon raccoon.** The stocky words added flesh to a human body: breasts, a belly and a human backside. They didn't give her the reference's simple cartoon shape. The human body probably comes from the model, the LoRA or the IP-Adapter, not the prompt alone.
- **`detailed anatomy` in the negative** probably drew the lower-back censor mark on one image. Keep anatomy words out of the negative.
- The canny guide at 0.6 (ending at 0.6) still didn't visibly shape the figures.

From `female-raccoon-003-img2img-sheet-recipe` (img2img of baseline-highres.png at denoise 0.65, Enoch 005's tag recipe, no ControlNet), **on-track**. Josh: "this is wonderful."

- **Start from a sheet that already has the right body.** img2img kept her cartoon body and head size (0.206–0.210). The fur-and-paws chunk gave paw hands, and the plain colour tags held teal, mint and navy blue with no overshoot. This is the recipe above.
- **What's left:** the back views drew a heart-shaped rump with a cleft line, more human than her sheet, and a small dark mark at the tail base (her sheet has a similar oval there). Lines measured about 0.20%, against her 0.33%. The swatches turned brown. The eyes and smile are a little more glamorous than her sheet's. Fix these one at a time, starting from this job.

Add a line here after each verdict on her jobs, so the next job starts from what was learned.

## Review checklist

Check every image of her against the style guide's checklist, plus:

1. Cartoon raccoon body, not a human one: a mild waist, hips a little wider than the waist, shoulders narrower than the hips, paw hands, and a back view without a human-shaped rump.
2. Flat, even sleeve edges.
3. Eyelashes, large dark pupils with a red-brown lower half.
4. Mint (not cream) chest, belly, muzzle and back-of-hips patch; navy that reads as blue.
5. Nothing in the empty space around the figures.
