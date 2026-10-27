job: female-raccoon-003-img2img-sheet-recipe
job-hash: 5107922f751eb76d
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Four txt2img jobs drew a human woman's body (lanky pin-up in 001, chubby in 002) with a raccoon head. This job stops asking the model to invent her body from words. It redraws her own approved sheet with img2img at denoise 0.65, so her cartoon body, palette and head size carry over, and the Enoch-style fur-and-paws chunk softens the fur and hands.

## Will this job do it?
Mostly yes. It is the first job on this track that attacks the cause the 002 verdict named (the body coming from the model, LoRA and IP-Adapter) and not the wording.

- **The parent does the body work.** I looked at baseline-highres.png. Its figures already have the target shape: a simple tube torso, a mild waist with flared hips, navy sleeves and legs, and heads of about 0.20 of figure height (front figure: head about 255 px of about 1,255 px). At denoise 0.65 with Euler a, roughly the first third of the noise schedule is kept, so silhouettes, poses and the big colour areas usually survive. The fur edges, hands and line work get redrawn. That should also fix head size, which the canny unit failed to do in 001 and 002 (0.13–0.17). The 0.65 setting is a sensible middle: low enough to keep the body, high enough for `(raccoon paws:1.2)` and `(paw-like hands with short stubby fingers:1.2)` to reshape her rather human hands.
- **Anti-human words.** `soft furry silhouette, simple shapes, minimal interior lines` together with `human, (human-like:1.2), human proportions, skin-tight, realistic` in the negative push against the spine lines, buttock crease and torso detail that 001 and 002 added. The negative keeps no anatomy words, which avoids the censor-mark fault seen in 002. `featureless crotch` is a positive tag, so it doesn't trigger that fault.
- **Colours.** The parent's flat teal, navy and mint start in the latent, so colour mostly comes from the image, not the words. `navy blue` on hands, legs, mask and rings matches what fixed the navy in 001. `pale cyan` chest, belly, muzzle and hip patch, plus `cream` and `white chest` in the negative, target 001's white-chest drift.
- **Removing the hourglass and curvy wording** is right given 001 and 002: those words added a human body. The female hourglass rule is still met by the parent's own silhouette, not by the prompt.
- **Model, LoRA and kind are all correct.** Indigo Void, `charsheet_lora_v1:0.6` with the `charsheet` trigger, and kind `character-sheet` (it redraws a full multi-view sheet). The size, 1536x1016, keeps the parent's aspect (1.512 against 1.514) and should fit in 8 GB VRAM. New fixed seeds suit this job, because the whole recipe changed, so comparing with 002's seeds tells us nothing.

## Risks and rule conflicts
- **Teal overshoot.** `(teal body:1.3), (teal fur:1.2)` together with four `pale cyan` phrases and `mint countershading` is at least as strong a cyan push as 001's `(teal fur:1.3)` plus `(turquoise fur:1.1)`, which turned the fur sky blue. The parent's colours should hold most of it at 0.65, but the fur may drift lighter and bluer than `#48C2C3`.
- **The parent's own human cues will carry over.** Both back views in the parent show a buttock crease, spine and shoulder-blade lines, and a glute curve. img2img keeps whatever the parent has, and Josh's 002 complaint included a "human backside". `minimal interior lines` and `human-like` are the only counter-weights, and anatomy words can't go in the negative. Expect the backside to soften, but not disappear.
- **Layout mismatch with the prompt.** The prompt asks for `side view`, but the parent has no full-body side view, only a bust. The negative has `close-up, head only`. At 0.65, the bust may be redrawn as a malformed half-figure. The brief accepts this, so I'm judging body and colour only.
- **Swatch dots in the parent** may survive or turn into small blobs despite `color swatch, (color palette:1.2)`. This is accepted in the brief, but it will still fail checklist item 8 ("nothing extra on the sheet").
- **`hip fur tufts`** isn't in her reference or the style guide (only shoulder tufts and a chest flick are). It could put spiky fluff on her hips that changes the hourglass outline.
- **`(blue eyes:1.3)` in the negative while `navy blue` appears five times in the positive.** These are usually separate enough in SDXL. If the navy comes out greyish or purple, this is a likely cause.
- **This is more than one change compared with 002**: mode, IP-Adapter and canny removed, the prompt and negative rewritten, new seeds and size. The brief frames it as one recipe swap. If it works, the recipe is proven. If it fails, the results won't show which part failed. Given four off-track jobs, I think testing the whole recipe at once is reasonable.
- No breaks of locked art, the clothes and props rule, digitigrade feet, or calm expression. `friendly smile, open smile` is calm, though the parent's smile is closed.

## Must fix
none

## Could improve
1. Lower `(teal body:1.3)` to `(teal body:1.1)`, or drop it and keep `(teal fur:1.2)`. The parent already supplies teal at 0.65, and the extra weight is the main risk of a repeat of 001's sky-blue overshoot.
2. Drop `hip fur tufts` from the fur chunk. It isn't one of her markings, and tufts at the hips can break the clean hourglass outline the parent gives her. Keep `(shoulder fur tufts:1.2)`, which is a rule.
3. Add `charcoal grey` to the negative next to `(grey fur:1.3)`, as the style guide's grey-fur fault entry says. This is a cheap guard. It matters less in img2img, since the parent is already teal.
4. When reading results: if the bodies still read as human, the next small job is denoise 0.55 (keeps more of the parent's body). If the fur and hands barely changed, try 0.7. Change only that one setting, with the same seeds.
