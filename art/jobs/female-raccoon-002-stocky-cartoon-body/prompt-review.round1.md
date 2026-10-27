job: female-raccoon-002-stocky-cartoon-body
job-hash: 0eb7540efadc0530
assessment: partly
must-fix: 1

## Reason for the change, as I understood it
Josh marked female-raccoon-001-teal-colour-wording off-track because "the body is too human": lanky pin-up build, long thin legs and a detailed human backside. This job changes only the body wording, with the same seeds, so her body moves toward the reference's simple cartoon raccoon build. Colour is deliberately left as it was.

## Will this job do it?
Partly. The direction is right, but some of the new words describe a different body from the reference.

What should help:
- Removing `(narrow waist:1.1)`, `(wide hips:1.1)`, `full thighs` and `(adult proportions:1.1)`. In the earlier outputs I viewed (teal-colour-wording 20261027/28, ipadapter-weight-wording 20261027/28), the bodies have wasp waists, flared hips and a detailed backside. Those words fit that result, so taking them out goes to the cause.
- `(human proportions:1.3)`, `(pin-up:1.2)` and `(skinny:1.2)` in the negative, and `(cartoon animal proportions:1.3)`, `simple soft torso` and `big round head` in the prompt. These are sensible pushes toward the reference.
- Keeping the seed fixed (20261027 to 20261030) and leaving IP-Adapter, canny, the LoRA, CFG and steps alone. Any change can then be credited to the wording. This is the right kind of small job.

What works against it:
- **The reference isn't short-legged or chubby.** In baseline-highres.png the head is about a fifth of her height and the legs are about 0.44 of it. What separates her from the earlier outputs is **thick, tube-like limbs, a plain torso with only a mild waist, and no anatomical detail**, not short legs. `short thick limbs`, `short thick legs`, `(stocky:1.2)` and `(chubby soft body:1.1)`, together with `(long legs:1.3)` in the negative, ask for a squat, chubby body. That breaks the "legs nearly half the body, fingertips at mid-thigh" rule.
- **The prompt contradicts the negative.** A big round head, short limbs and a chubby body add up to the "chibi/child" look on NoobAI-based checkpoints, and the negative pushes `(chibi:1.3)` and `(child:1.3)` away at the same time. With both in play, Forge will likely split the difference unpredictably from seed to seed. Seed 20261030 already produced a 0.347 head in the base job.
- **Head size and overall proportions won't come from wording alone.** The style guide says a prompt alone doesn't fix small heads (base heads were 0.156 to 0.21, one outlier at 0.347). The canny unit, the lever meant to fix this, is unchanged at 0.6, Balanced, ending at 0.6, and female-rules.md records that it "barely shaped the figures" last time. Expect the heads to stay off target. That's acceptable, because this job only tests wording, but don't read a small head in this run as a failure of the wording.

## Risks and rule conflicts
- Rule (style guide, Body, and female-rules.md): legs nearly half her height, fingertips at mid-thigh. Asking for `short thick legs` while pushing away `(long legs:1.3)` works against this. See Must fix 1.
- Rule (female-rules.md, Body): hourglass, wide hips, full thighs. `(mild waist:1.1)`, `(wider hips:1.1)` and `(narrow shoulders:1.1)` keep a weak female shape. Next to `(stocky:1.2)` and `(chubby soft body:1.1)`, the waist may disappear, and the body can drift toward the square, male-looking silhouette. The reference does still have a visible, mild hourglass.
- `(detailed anatomy:1.2)` in the negative: it isn't a body-part word, but it's close to what the known-faults table warns about (anatomy words in the negative set off the lower-back censor mark). Low risk, but watch the back views.
- The canny reference has four figures (front, back, side bust, back) and colour swatches, while the prompt asks for `three views` and the negative has `bust`, `head studies`, `(color swatches:1.3)` and `(color palette:1.3)`. The prompt and the edge guide are fighting over the layout. That may be part of why canny has had little effect. This isn't new to this job, so it's not a blocker here.
- Colour is untouched by design, so the sky-blue fur and white chest are expected to come back. Judge body shape only, as the brief says.
- The model, the LoRA (0.6, `charsheet` trigger present, `kind: character-sheet` matches a three-view sheet) and both ControlNet models are approved. No locked art is involved.

## Must fix
1. **Ask for thick limbs, not short ones, and push away thin limbs instead of long ones.** In `prompt`, replace `short thick limbs, short thick legs` with `thick arms, (thick legs:1.1)`, and replace `short thick raccoon hands` with `thick raccoon hands`. In `negative`, replace `(long legs:1.3)` with `(thin legs:1.2), (thin arms:1.1), (lanky:1.2)`. Expected effect: the tube-like cartoon limbs of the reference at the proportions the rules require, instead of a squat body that clashes with the `chibi`/`child` negatives and breaks "legs nearly half the body".

## Could improve
1. Drop `(chubby soft body:1.1)` and lower `(stocky:1.2)` to `(stocky:1.1)` or swap it for `(toony:1.2)`, a common tag on NoobAI-based models for simplified cartoon anatomy. The reference isn't chubby. This also reduces the risk of losing the female waist.
2. Replace `(detailed anatomy:1.2)` in the negative with `(realistic anatomy:1.1)`, or remove it, since `(realistic:1.3)` and `(human proportions:1.3)` already cover it. This keeps the negative clear of the censor-mark warning.
3. For the next job, not this one: test the canny unit by itself, with the wording fixed. For example, `control_mode: "ControlNet is more important"` or weight 0.8 to 0.9 with `guidance_end` 0.8. Also stop the prompt and negative from fighting the guide's four-figure layout (drop `three views`/`bust` or accept the bust). Head size has only ever moved with the edge guide, and it hasn't moved yet.
4. Avoid e621 tags such as `shortstack` or `thick thighs` if more body wording is tried later. On this checkpoint they push toward a sexualised body, the opposite of the goal.
