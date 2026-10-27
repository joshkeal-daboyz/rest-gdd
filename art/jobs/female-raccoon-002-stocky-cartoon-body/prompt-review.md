job: female-raccoon-002-stocky-cartoon-body
job-hash: 37f30b2e63c94401
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh called 001-teal-colour-wording off-track because "the body is too human": long pin-up legs, a curvy human torso and backside. This job changes only the body wording, with the same seeds, to see whether wording alone moves her toward the reference's simpler cartoon raccoon build (big head, tube-like limbs, soft torso, mild waist). Colour is left alone on purpose.

## Will this job do it?
Mostly yes, as a test of the wording. It answers one clear question.

- **What should help.** The words that most likely drove the pin-up build are gone: `(narrow waist:1.1)`, `(wide hips:1.1)`, `full thighs`, `(adult proportions:1.1)` and `slender raccoon hands`. In the 001 outputs I viewed, the result was strong hourglasses, thigh gaps and a detailed human rear in every back view, so removing those words is the right lever. In the negative, `(human proportions:1.3)`, `(lanky:1.2)`, `(pin-up:1.2)` and `(thin legs:1.2)` push against what Josh rejected. In the positive, `(cartoon animal proportions:1.3)`, `simple soft torso`, `thick arms` and `(thick legs:1.1)` describe the reference fairly well. Its limbs are even, tube-like and fairly thick, and its torso is a simple rounded shape with only a slight waist.
- **Round 1's fix is in place.** The job asks for thick limbs without `short`, and `(long legs)` is replaced by thin/lanky negatives. That keeps the rule "legs nearly half the body".
- **The female read is still there.** `(mild waist:1.1)`, `(wider hips:1.1)`, `(narrow shoulders:1.1)`, `eyelashes` and `(female:1.4)` keep a gentle hourglass. That matches the reference, which has only a slight waist pinch.
- **Settings.** The fixed seed 20261027 (×4) matches the base job, so a change in body shape can be put down to the wording. No weight goes above 1.4. The model, the LoRA at 0.6 with the `charsheet` trigger and `kind: character-sheet` are all correct and approved.
- **What it won't fix: head size.** `big round head` is a prompt-only change. The style guide says a prompt alone doesn't fix the small-head fault, and heads were 0.129–0.162 across the track (the 0.347 readings are the stray head-study tiles, not figures). The canny unit is unchanged (0.6, end 0.6), and the rules say it "barely shaped the figures" last time: layout followed the seed, not the reference. So expect heads around 0.16 again and the same seed-driven layouts. That's acceptable for a wording test, but nobody should expect this job to reach 0.19–0.21.
- **Partly from the reference.** The human-looking rear may partly come from the IP-Adapter reference itself. The reference's back view has a visible rounded rear with the mint patch. Wording can soften it, but probably won't remove it.

## Risks and rule conflicts
- **`stocky` plus `(tall:1.1)` in the negative may squash her.** Even without `short`, these lean toward a short, squat body, and `big round head` adds a chibi pull. The `(child:1.3)` and `(chibi:1.3)` negatives work against that, but watch the leg length (reference about 0.44 of height) and fingertips at mid-thigh.
- **Softer than the written rules.** female-rules.md still requires "wide hips and full thighs" and a clear hourglass. This job deliberately softens that after Josh's verdict. It's consistent with the reference image, but the rules file should be updated if Josh accepts the softer build.
- **`(detailed anatomy:1.2)` in the negative contains "anatomy".** The style guide warns that anatomy words in the negative set off the lower-back censor mark. It's a general term, not a body part, and `bad anatomy` was already in the base job, so the risk is low. Check the back views for a censor mark.
- **`(cartoon animal proportions:1.3)` is not a tag** NoobAI/Indigo Void was trained on. CLIP will mostly read it as "cartoon" and "animal", which could pull slightly toward a feral, four-legged build at 1.3. `(digitigrade legs:1.3)`, `standing` and `anthro raccoon` should hold the upright pose.
- **Colours will still be off.** The fur will probably be sky-blue again and the chest white. That's deliberate this round, so don't judge this run on colour.
- **Line weight isn't addressed.** The track measured 0.21–0.22% against a target of about 0.33%, and nothing here changes it. That's fine for a one-change job.

## Must fix
none

## Could improve
1. **Add `toony`** (an e621 tag NoobAI-based checkpoints know well, for big-headed, simple-bodied cartoon furries) next to `(cartoon animal proportions:1.3)`, for example as `(toony:1.2)`. Expected effect: the model is more likely to understand the stocky cartoon build than with an invented phrase. This is still body wording, so it stays within the one change.
2. **Drop `(tall:1.1)` from the negative.** `(lanky:1.2)` and `(human proportions:1.3)` already cover the pin-up build. Expected effect: less pull toward short legs, helping legs stay near half her height.
3. **Test the canny guide in a separate job, not this one.** The track's head-size and proportion problem most likely needs the edge guide to actually take hold. A later one-change job could raise canny to weight 0.9–1.0 with `guidance_end` 0.8–1.0 and `control_mode` "ControlNet is more important". If the layout still doesn't follow baseline-highres.png, the unit probably isn't being applied, which Josh should know.

## Pipeline notes
These are for the pipeline-test part of my task, not for job.json:
- The IP-Adapter source disagrees between files. The job and brief use `baseline.jpg`, but female-rules.md says to run IP-Adapter on `baseline-highres.png`. For CLIP's 224 px input it hardly matters, but the docs and the job should agree.
- The brief lists `baseline-highres.png` twice: once as the ControlNet image and once as the reference.
- Round 1 shows "Claude's response not recorded" (`response: null` in state.json). The instructions say to assume earlier fixes were applied unless the response says otherwise, but with no response I had to check job.json myself to confirm round 1's change went in. It had.
- Measured head ranges such as "0.156-0.347" mix in stray head-study tiles. The upper number is meaningless and could mislead a reviewer. Reporting figure heads only would help.
- female-rules.md still asks for a full hourglass with "wide hips and full thighs", while its "What her jobs have taught us" section and this job move away from that. When the rules and the latest verdict disagree, it's unclear which one the reviewer should hold the job to.
- Earlier rounds' full review text isn't in the brief, only the must-fix list. That was enough here.
