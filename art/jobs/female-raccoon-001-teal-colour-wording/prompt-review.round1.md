job: female-raccoon-001-teal-colour-wording
job-hash: 54c6ad342a23cd9e
assessment: partly

## Reason for the change, as I understood it
The last two sheets came out pale sage/seafoam with cream chests and near-black/purple navy, and at IP-Adapter 0.8 the reference's own swatch column and side bust leaked in as swatches, busts, head studies and extra figures. This job tries to stop the leaks by lowering IP-Adapter to 0.6, and to fix the colours by rewording them (teal moved early at 1.3; "pale mint" changed to "mint"; "dark navy" changed to "navy").

## Will this job do it?
**Leaks: probably yes, partly.** The reference itself (`baseline-highres.png`) has a palette-swatch column and a side bust between the views. The weight-wording outputs at 0.8 copied exactly those: a swatch cluster in seed 20261027, and busts and head studies in both seeds. That points at the IP-Adapter rather than at the prompt, so dropping `weight` from 0.8 to 0.6 is the right lever. `(color swatches:1.3)` sitting next to `(color palette:1.3)`, `head studies`, `bust` and `(multiple heads:1.3)` in the negative is reasonable. The 1536x1024 canvas with only three figures leaves wide empty gaps, though. In all four earlier images the model filled them with something: props, arrows and hooks at the baseline, and limbs and heads at 0.8. Some leftover clutter at 0.6 is likely.

**Colour: uncertain, and parts of the change could make it worse.**
- `(teal fur:1.3)` early in the prompt is the right move: the old single unweighted `teal fur` sat in a later chunk.
- The visible failure in the earlier outputs is fur that reads as **mint/sage green**, not grey. The prompt still says "mint" three times (`mint muzzle`, `(mint chest and belly:1.2)`, `(mint patch across back of hips:1.1)`), and two of those are now *stronger* than before (1.2 instead of unweighted, and "pale" removed). SDXL readily bleeds a colour word onto the whole body. The likely result is greener fur, or chest and fur merging into one mint tone, rather than #48C2C3 teal with a pale chest. "Mint" is a green-leaning word to the model; the target #D0FFFA is a very pale cyan.
- `dark navy` -> `navy` helps a little, but "navy" alone still tends to render near-black. Nothing in the prompt says *blue*.
- Lowering IP-Adapter to 0.6 also weakens the reference's colour pull, which is the only thing in the job that "knows" the exact teal.

**Size.** The brief separates the two changes by what each is judged on, but they aren't independent: the IP-Adapter weight affects colour as well as layout. If colour gets worse, you can't tell whether the cause is the wording or the 0.6 weight. The brief admits this ("blame the wording or too-low weight"). Leak counts are clean to judge; colour is confounded.

Model, LoRA (`charsheet_lora_v1:0.6` with the `charsheet` trigger on a `character-sheet` job, which is correct), IP-Adapter model and module are all approved. Fixed seeds 20261027-30 are right for comparing against the parent job.

## Risks and rule conflicts
- Colour bleed from three "mint" tags (one at 1.2) may turn the fur greener, which goes against palette rule 1 and is the main thing this job wants to fix.
- "navy" with no "blue" may stay near-black/purple, again against the palette (#2A4365).
- Lower IP weight plus colour rewording in one job means a colour failure can't be pinned on either change.
- Leftover clutter in the empty canvas space is still likely (checklist 8). An earlier review's suggestion to add `monochrome`/uncoloured-sketch terms was held back, and the uncoloured line sketches it targeted (baseline seed 20261028) aren't covered except by `(sketches:1.2)`.
- Small heads (~0.13) will persist without a female edge guide. The brief knows this and isn't testing it.
- No rule conflicts in wording: digitigrade, four navy rings with a navy tip, calm smile, no clothes or props, and flat sleeve edge are all asked for correctly. Nothing locked is touched.

## Recommendations
1. **Use blue-leaning words for the pale areas instead of "mint":** `pale cyan muzzle`, `(pale cyan chest and belly:1.2)`, `(pale cyan patch across back of hips:1.1)`. Expected effect: the chest and hip patch move toward #D0FFFA without bleeding green into the main fur, so fur and chest stay distinct.
2. **Reinforce the fur hue with a second common colour tag:** `(teal fur:1.3), (turquoise fur:1.1)`, and add `(green fur:1.2), mint green` to the negative. Expected effect: pushes the fur from sage toward blue-green #48C2C3. "Turquoise" is a well-tagged colour on the checkpoint's training sources, and "teal" alone has produced sage twice.
3. **Say "blue" for the markings:** `(navy blue:1.2)` once near the markings (for example `navy blue raccoon mask markings`), and add `(black:1.1), purple` to the negative. Leave the tail-tip and ring tags as they are. Expected effect: the markings read as blue #2A4365, not black or purple.
4. **Optional, cleaner test:** keep the IP-Adapter at 0.8 and set its start later (guidance start of about 0.25–0.3, if job.json and forge_jobs.py pass it through), instead of cutting the weight to 0.6. Expected effect: the reference still carries colour and style but has less say over early layout, which is where the swatches and busts come from. If that field isn't supported, run as 0.6, but read a colour failure as "wording *or* weight" as the brief says.
5. **Optional:** add `monochrome, uncolored` to the negative to catch the line-only sketches seen in the baseline outputs. Expected effect: fewer outline-only extras in the empty space. Don't add `lineart`: it may fight `thick outlines`.
