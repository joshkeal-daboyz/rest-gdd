job: enoch-sheet-005-less-human
job-hash: b9e31c0aeb62cac1
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Josh judged job 3's sheet symmetrical but "too human". This job should make Enoch read as a raccoon: paw-like short-fingered hands, fuller fur at the shoulders, hips and cheeks, a softer furry outline and fewer muscle and rib lines. It must keep the job 3 symmetry and the C2/246 look (four views, brown irises with solid pupils, navy mask with white brow stripe, teal and navy, white chest, square lean build, digitigrade feet, white background).

## Will this job do it?
Mostly yes. Its levers point at the things that read as human in the parent:

- **Hands.** In the parent (seed 248) the hands are long, bony and five-fingered, with claw tips. `(raccoon paws:1.2)` and `(paw-like hands with short stubby fingers:1.2)` are the right push. `paws` is a strong e621 tag on this checkpoint, and the plain-language phrase backs it up.
- **Interior lines.** The parent has many rib, spine and shoulder-blade lines on the chest and both back views. `simple shapes, minimal interior lines` should cut them, along with `flat color`. The IP-Adapter on v14 at 0.4 also helps here, since v14's body has very few interior lines. `minimal interior lines` is not a tag, so expect only a mild effect from that phrase.
- **Outline.** `(fluffy fur:1.2)`, `(fur tufts on shoulders and hips:1.2)`, `fluffy cheek fur` and `soft furry silhouette` give a broken fur outline instead of the parent's smooth, skin-tight one.
- **Its own BREAK chunk.** Putting these words in a chunk of their own is sound. Added to the end of the 75-token colour chunk, they would have been diluted.
- **Negative additions.** `human` is a real e621 species tag and a standard furry negative, so it should work. `(human-like:1.2)` and `human proportions` are weaker but harmless. `skin-tight` and `sketchy lines` are fine.
- **Denoise 0.6 → 0.7.** This is justified. Job 3 showed that 0.6 keeps the parent's hand and hip shapes, and hand shape can't change at low denoise. At 0.7 with Euler a, the four-view layout, head size and colour blocks should mostly carry over from the parent. That parent has heads of about 0.2 and the line weight Josh liked. Job 4 had no parent image and lost the head size and layout (0.139–0.178), but that doesn't apply to img2img at 0.7.

Model, LoRA (0.6 with the `charsheet` trigger, on a true four-view sheet job), IP-Adapter model and weights are all approved and correct. Every weight is at or below 1.3. No body-part words were added to the negative, which follows the censor-mark rule. The fixed seeds 231506246–249 match job 3, so the comparison is fair.

One limit: the job changes the positive, the negative and the denoise at once. All three serve the same single goal, and job 3 already showed that wording alone at 0.6 wouldn't move the shapes. So I accept the bundle as one test. If the result drifts, though, it won't show whether the drift came from the denoise or the words.

## Risks and rule conflicts
- **Hip tufts against the male build.** `(fur tufts on shoulders and hips:1.2)` adds width at the hips. Enoch's main rule is a square torso with narrow, straight hips. Fluffy hips can read as a flare toward the female silhouette. `narrow hips` and the negative's `(wide hips:1.2)` push back, but check the front view's hip line.
- **Fluffy fur against the flat style.** `(fluffy fur:1.2)` and `soft furry silhouette` pull against the negative's `detailed fur, realistic` and the flat rule. Most likely you get spikier, rougher outlines, which is fine. You might also get painted fur strands, which breaks the flat style.
- **Symmetry and face at 0.7.** The front and back views may lose some of job 3's symmetry. The brown irises with solid pupils may drift, possibly toward hollow pupils (a known fault). The symmetry tags and eye wording stay in to resist this.
- **Back-view marks the job doesn't address.** The parent's tailless back view has a dark circular "X" spot and a buttock cleft between white wedges. That spot looks like the model's censor-style mark, and it's one of the human cues named in the reason. Only the positive fur words fight it here, and at 0.7 it may survive.
- **`(human-like:1.2)` and anthro.** In principle this could push toward a more feral stance. That's unlikely with `anthro, standing`, the parent image and IP-Adapter in place.
- **`stubby fingers`.** This leans a little toward cute or chibi hands. `chibi` is in the negative, so the risk is small.

## Must fix
none

## Could improve
1. Drop the hip tuft weight. Change `(fur tufts on shoulders and hips:1.2)` to `(shoulder fur tufts:1.2), hip fur tufts`. This keeps the style guide's shoulder tufts at full strength and makes the hip fur a light touch, so it's less likely to widen the hips against the square-torso rule.
2. Fight the buttock cleft and back spot without naming body parts. Add `featureless` (a general term, already used as part of `featureless crotch`) or `smooth back` to the last positive chunk. The aim is a plain cartoon back, in line with the base-body rule "no anatomical detail".
3. If the heads or layout drift at 0.7, the next job could add the cleared `shoulder_guide_4pose.png` as a canny unit (`diffusion_pytorch_model_V2`) at low weight (about 0.3) ending early (`guidance_end` about 0.3). That holds the overall outline and head size, and frees the hands and fur edges in the later steps where detail is drawn. Leave it out of this run so the wording and denoise test stays clean.
