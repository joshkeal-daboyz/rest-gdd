job: female-raccoon-001-teal-colour-wording
job-hash: a3627c743e9dc472
assessment: partly

## Reason for the change, as I understood it
This is a colour-only follow-up to the off-track weight-wording job, using the same seeds and settings. The fur should be saturated teal #48C2C3 instead of sage or seafoam. The chest, belly and back-of-hips patch should be pale cyan or mint instead of cream. The markings should read as blue navy #2A4365 instead of near-black or purple. Leaks and head size are not judged in this job.

## Will this job do it?
The setup is sound for this question. The seeds (20261027 and up), model, LoRA, IP-Adapter 0.8, size, steps, CFG and sampler all match the weight-wording job, so any difference in the outputs comes from the wording. The model is correct. `charsheet_lora_v1:0.6` with the `charsheet` trigger fits, because this is a real three-view sheet job.

What I saw in the outputs. Both weight-wording outputs I viewed have sage-green fur, a cream chest, near-black or purple-black markings and no hip patch. The two baseline-ipadapter outputs I viewed were a little more teal but had the same chest and marking problems. The reference image is a strongly saturated teal, so IP-Adapter alone isn't carrying its colour across. The prompt has to do the work.

Changes that should help:
- **Fur.** `(teal fur:1.3)` placed early, together with `(turquoise fur:1.1)`, `(vivid colors:1.1)`, and `muted colors, desaturated, (green fur:1.2), mint green` in the negative. Together these should push the fur from sage toward cyan-teal. This is the most likely part of the goal to improve.
- **Chest.** Changing "mint" to `(pale cyan chest and belly:1.1)` removes the green-leaning word, which is a fair theory for why the fur went sage.
- **Markings.** `navy blue raccoon mask markings` and the negative `(black fur:1.1), purple` should help the mask turn blue.

Changes that work against the goal or are too weak:
- **`pastel colors` in the negative fights the chest.** A pale-cyan chest is a pastel colour. The model may push the chest toward saturated cyan, which would merge it into the fur and lose the two-tone look. It may also push the chest toward white or cream.
- **Nothing targets cream directly.** The chest has come out cream in every earlier output. `plain off-white background` is a likely source, since the cream matches the background tone. There is no `cream` or `beige` in the negative.
- **"navy" on its own is still the word for hands, lower legs, rings and tail tip.** Only the mask says "navy blue". On a NoobAI-based checkpoint, bare "navy" tends to come out near-black, which is exactly the failure being fixed. So the hands, legs and tail will probably stay near-black even if the mask turns blue.
- **The hip patch probably won't appear.** `(pale cyan patch across back of hips:1.1)` is a long natural-language phrase, and this tag-trained model tends to ignore those. No earlier output showed any hip patch. Expect it to stay missing; a prompt alone may not fix it.

Job size: about ten colour words change at once. That's acceptable, because the job asks a single question (can wording alone fix the colours?). But if the result is mixed, it won't show which word did the work, and the next job should split them.

## Risks and rule conflicts
- **`white muzzle` breaks the palette table.** The style guide says the muzzle is mint #D0FFFA. The goal doesn't mention the muzzle, so this is also an unrequested extra change. (The reference's muzzle does look close to white, so Josh may want to settle this.)
- **`pastel colors` (negative) against `pale cyan chest` (prompt)**, as described above.
- **The cyan words may spread.** "pale cyan" and "turquoise" could bleed into each other, giving a fur and chest of nearly the same colour with weak contrast.
- **Expect the leaks.** IP-Adapter at 0.8 will probably bring back the busts, head studies and swatches seen in both weight-wording images. The brief excludes them from judging, but they will make the sheet harder to read for colour.
- **The hip patch will probably still be missing**, so one of the four things being judged will likely fail no matter how the rest goes.
- Model, LoRA, kind, ControlNet model and count all follow the rules and the approved list. Weights all stay at 1.4 or below. No locked art is involved.

## Recommendations
1. **Remove `pastel colors` from the negative** and keep `muted colors, desaturated`. Effect: the negative stops pushing against the pale-cyan chest, and the fur is still pushed toward saturated colour.
2. **Add `(cream fur:1.2), beige` to the negative.** Effect: this aims straight at the cream chest seen in all earlier outputs, without changing the off-white background word the style guide asks for.
3. **Change `navy hands`, `navy lower legs`, `(four navy rings:1.1)`, `navy ring at the tail base` and `(navy tail tip:1.3)` to use "navy blue"**, keeping the existing weights. For example: `navy blue hands`, `(navy blue tail tip:1.3)`. Effect: all markings get the same blue cue the mask gets, so the "blue, not black" test covers all of them and not only the mask. A small blue spill onto the fur would push it toward cyan, which is acceptable.
4. **Change `white muzzle` to `pale cyan muzzle`, or remove the muzzle word.** Effect: the job follows the style guide's mint muzzle and doesn't add an unrequested change. If Josh actually wants a white muzzle, as in the reference, that is his decision.
5. Optional: **change `(turquoise fur:1.1)` to `(aqua fur:1.1)`.** "aqua" is a common colour tag in Danbooru-trained models such as NoobAI and is probably read more reliably than "turquoise". Expected effect: a slightly stronger cyan-teal fur.
