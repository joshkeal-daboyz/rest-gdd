job: enoch-sheet-007-shading-v3
job-hash: 5d7b1f14b254a66a
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Job 006 at denoise 0.45 gave no visible shading. I viewed its seeds 246 and 247, and both are as flat as the 005/246 parent. Josh wants anime-style cel shading (hard shadow shapes, one shadow tone per colour) on the 005/246 sheet, and asked for a retry at 0.55. The paws, heads, symmetry, outlines, palette and white background must stay as they are.

## Will this job do it?
Probably yes, at least partly. The main lever is `denoising_strength` 0.45 → 0.55. The parent is perfectly flat (I checked 005/246: one fill per colour, no shadow anywhere). At 0.45, SDXL img2img with Euler a mostly re-renders the parent's fills. Going to 0.55 gives the sampler enough noise to add new tonal shapes. It should still keep the layout, because the parent is a clean, high-contrast sheet. The fixed seeds 231506246–249 match job 006, so the outputs compare one-to-one with 006's flat results. That is the right choice.

The shading words are sound. `(cel shading:1.3)` is the strongest term and a real danbooru tag that NoobAI-based Indigo Void knows. `(anime coloring:1.1)` is also a real tag, for hard-edged two-tone fills, and it suits Josh's "anime style cell shading". At 1.1, under cel shading, it is unlikely to take over. `(simple shading:1.1)` pushes toward one shadow tone per colour. Nothing in the prompt asks for flat colour, and the negative doesn't name shading or shadow, apart from `drop shadow`, which is the right exclusion. `(painterly:1.2), (gradient:1.1), airbrush` push the new shading toward hard edges rather than soft rendering, which is what the goal asks for. All weights stay at 1.3 or below. Model, LoRA (0.6 with the `charsheet` trigger) and IP-Adapter model are all approved, and `kind: character-sheet` matches a four-view sheet.

Two settings work against the change, mildly:
- IP-Adapter on `enoch_sheet_v14.png` (weight 0.2, end 0.6) carries a fully flat, posterised reference for the first 60% of steps, which pulls toward flat fills. At 0.2 this is a gentle pull, and the 006 response deliberately kept it, so I don't move it here. If 007 also comes out flat, this is the next lever (see Could improve).
- `simple shapes, minimal interior lines` (from job 005) could suppress small shadow shapes. These words protect what Josh liked in 005, so they should stay.

Heads and line weight: job 006 measured head 0.192–0.194 and line 0.38%, and 005 measured 0.190–0.196. At 0.55 the parent still carries the layout, so heads should stay near 0.19. Job 001 at 0.6 showed that hands and faces can drift at this range, so check paws and faces first.

## Risks and rule conflicts
- **Flat-colour rule.** The style guide ("Flat colours … No gradients or painted shading") is overridden by Josh's own words in chat. The brief says the rule and palette get updated if he calls the result on-track. This isn't a blocker, but every shaded output will fail checklist item 8 until the rule changes.
- **Two changes at once** (denoise and the `anime coloring` tag). Both push the same way, so the job still answers "does shading appear?" It can't tell which of the two caused it, or which caused any face drift.
- **Anime-face drift** from `anime coloring` at 0.55: human-like anime eyes or a smaller muzzle. The negatives `human, (human-like:1.2)` help.
- **Shadow colour.** Teal shadows may go grey (the known Indigo Void fault). `(grey fur:1.3)` and `charcoal grey` in the negative guard against it. Navy shadows may merge into the near-black outlines.
- **Changes at 0.55 in general.** The parent's existing faults (the X-shaped mark on the tailless back view, white hip wedges) may change shape. Seed 247's family has already produced a headband, black neck band and stray arrows (005/247), and higher denoise makes these more likely to come back. The negative already covers `headband`, `arrow \(symbol\)` and `text`.
- **Background.** The prompt asks for pure white while the palette says off-white `#FAF7EF`. This is inherited from the parent and is not this job's question.

## Must fix
none

## Could improve
1. **Keep only one change.** Optionally drop `(anime coloring:1.1)` so the job tests only denoise 0.55, which is what Josh asked to retry. Then shading, or face drift, can be traced to one setting. Keep the tag if the goal is simply the best chance of visible shading this round.
2. **If 007 still comes out flat, change the reference next.** Lower the IP-Adapter `guidance_end` from 0.6 to about 0.3, or its weight from 0.2 to about 0.1. Shading has to appear in the middle steps, where v14's flat look is currently still applied. This should change one thing at a time in its own job.
3. **If shading appears but is faint, raise `cfg_scale` from 6 to 7** in a later job, rather than raising denoise past 0.55. Denoise was already shown at 0.6 (job 001) to redraw hands and faces.
