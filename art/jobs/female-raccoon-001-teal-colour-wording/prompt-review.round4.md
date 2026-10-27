job: female-raccoon-001-teal-colour-wording
job-hash: 3c3e50a88c605a04
assessment: partly

## Reason for the change, as I understood it
The last two jobs got the colours wrong. The fur was pale seafoam or sage instead of teal #48C2C3, the chest was cream instead of mint #D0FFFA, and the navy was near-black or purple instead of #2A4365. This job changes only the colour wording, on the same seeds and settings, to see whether wording alone can fix the three colours.

## Will this job do it?
Partly. I expect the hue to improve. I don't expect the fur to get saturated enough.

- **Navy.** Dropping `dark` from every `dark navy` and writing `navy blue` throughout is the right lever. `dark` pulls toward black, and `navy blue` gives SDXL an explicit blue token. With `(black fur:1.1)` and `purple` still in the negative, the markings should move bluer. This is the change most likely to work.
- **Fur hue.** `(teal fur:1.3), (turquoise fur:1.1)` is a sensible push toward #48C2C3, and both weights are under 1.5. Removing every `mint` word should also help. In the weight-wording outputs (20261027 and 20261028) the fur turned sage-green, greener than in the baseline-ipadapter outputs, and the three `pale mint` phrases were a likely cause, since colour words bleed across the whole figure in SDXL. Replacing `mint` with `cyan` moves any bleed toward blue-green, which is closer to teal.
- **Fur lightness, the main failure.** This job adds more pressure toward pale fur, not less:
  - `pale` now appears four times, two of them weighted 1.1 (`pale cyan muzzle`, `(pale cyan chest and belly:1.1)`, `(pale cyan patch across back of hips:1.1)`), and `white inner ears` adds a fifth light-colour word. `pale` bleeds lightness the same way `mint` bled hue.
  - `pastel colors` has been taken out of the negative, and it was the one negative term aimed squarely at the washed-out look in the last two jobs. `muted colors, desaturated` stay, but they target grey, not light.
  - `(vivid colors:1.1)` pushes the other way, but only weakly.
  - My expectation: fur bluer than last time but still light, around a pale aqua rather than #48C2C3.
- **Cream chest.** `(cream fur:1.2), beige` in the negative is the right block. The checkpoint's raccoon habit is a cream or white belly, so I expect white-ish rather than tinted mint. That passes "not cream" only loosely.
- **Seeds.** The fixed seeds (20261027, counting up) are good. They isolate the wording change from the weight-wording job.
- **Model and LoRA.** The model, the charsheet LoRA at 0.6 with its trigger, `kind: character-sheet` and the IP-Adapter `ip-adapter-plus_sdxl_vit-h` are all approved and correct for a three-view sheet.

## Risks and rule conflicts
- **Several changes at once.** About six colour levers change together: the teal weight, `turquoise`, `vivid colors`, mint→pale cyan, dark navy→navy blue, and the negative's pastel/cream/beige edits. The hip patch also moves from "lower back" to "across back of hips", which is a placement change, not a colour one. That's acceptable for a colour-only question, but if the result is mixed it won't show which word did what. If the navy fixes itself and the fur doesn't, the next job should change one word.
- **Lost guard against pale fur.** Removing `pastel colors` from the negative takes away protection against the main failure, pale fur, to protect a small area, the belly.
- **Lightness bleed.** Four `pale` tokens are likely to lighten the fur (see above).
- **Teal swallowing the belly.** `(teal fur:1.3)` against `(pale cyan chest and belly:1.1)` may make the chest come out teal or blend into it. That would be a palette failure the other way, though a smaller one.
- **No rule conflicts in the wording.** Digitigrade, four rings with a navy base and tip, calm smiling face, no clothes or props, flat style: all still asked for. Nothing locked is touched.
- **Expected faults.** Small heads and extra items around the sheet, from the IP-Adapter at 0.8 with no female edge guide, will recur. The brief says these aren't judged here.

## Recommendations
1. **Restore `pastel colors` to the negative**, at plain weight (no brackets). Expected effect: keeps pressure against the washed-out fur that made both earlier jobs off-track. The belly's light tint can come from the IP-Adapter reference rather than the prompt.
2. **Cut the `pale` tokens.** Replace `pale cyan` with `light cyan` and say it once for the front: `(light cyan chest and belly:1.1), light cyan muzzle`. For the back, use `(light cyan patch on back of hips:1.1)`. Expected effect: less lightness bleeding onto the main fur, while still asking for a cool, non-cream belly. If you'd rather keep this a pure navy and teal test, leave this one out and accept the bleed risk.
3. **Optionally raise teal to `(teal fur:1.4)`**, still under 1.5, and keep `(turquoise fur:1.1)`. Expected effect: more saturation weight on the largest area. Only do this if recommendation 1 is applied, so the two don't double-push.
4. **Keep everything else as written**: the seeds, IP-Adapter 0.8, the LoRA, `navy blue` throughout, and `(cream fur:1.2), beige`.
