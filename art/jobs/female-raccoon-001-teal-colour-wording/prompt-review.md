job: female-raccoon-001-teal-colour-wording
job-hash: a575de196e6cf0a7
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Both earlier jobs were off-track: the fur came out sage or seafoam, the chest cream and the navy near-black, and the heads were too small (0.13–0.16). This job tests plain colour wording, and adds a canny edge guide on her own reference sheet to bring the head to 0.19–0.21 and the body proportions in line with the sheet.

## Will this job do it?
**Head size and proportions: likely yes.** The canny unit (`diffusion_pytorch_model_V2`, weight 0.6, steps 0–0.6, Balanced) runs on baseline-highres.png. That is the style guide's own fix for the small-head fault, and it uses the same settings as Enoch's working guide. On the reference's front figure the head is about 0.20 of height, so copying its outlines should land in range. The aspect ratio is almost the same (3064x2024 is 1.51, the output is 1.50), so Crop and Resize trims almost nothing and won't squash the figures. Ending at 0.6 leaves the last 12 steps to the prompt and IP-Adapter for colour and line, which is right.

**Colour: likely better, but you can't credit the wording alone.** These words aim at the earlier failures:
- Fur: `(teal fur:1.3), (turquoise fur:1.1)`, against `(green fur:1.2), mint green, (grey fur:1.2), muted colors, desaturated`, which goes after the sage and seafoam.
- Chest: `(pale cyan chest and belly:1.1)` against `(cream fur:1.2), beige`, which goes after the cream chest.
- Markings: `navy blue` is now on every marking, with `(black fur:1.1), purple` in the negative, which goes after the near-black.
- The canny guide also hands Forge the reference's region outlines: the mask band, the chest shape, the four tail rings and the hip patch. With IP-Adapter at 0.8 on the same sheet, colours should land in the right places more often.

The canny edges carry no colour, so you can read the results this way:
- A **colour miss** points at the wording or the IP-Adapter.
- A **colour hit** may come partly from the guide's region shapes, not only the words.

The brief says this openly.

**Layout: expect four figures, not three.** The guide has a front view, a back three-quarter view with the tail, a side bust, a back view and seven swatch circles. It has no full-body side view. Up to step 18 the guide decides the layout, and that is when composition is set. So `side view`, `(three views:1.2)`, and the negative's `bust, (color swatches:1.3), (color palette:1.3)` will mostly lose. The brief already says to judge only head size, proportions and colour if this happens, so it doesn't block the stated goal.

All settings are on the approved list:
- Model: Indigo Void.
- LoRA: `charsheet_lora_v1:0.6`, with the `charsheet` trigger, on a `character-sheet` job.
- ControlNet: both models are approved.

The seeds 20261027 onward are the same as the compare_to job, which is right for side-by-side reading.

## Risks and rule conflicts
- **Three changes at once compared with compare_to:** new colour wording, a new IP-Adapter reference (baseline.jpg is the same sheet at lower resolution, so it's close to neutral) and the canny guide. The goal states both questions, head size and colour, so this is a known choice. It is still bigger than "one question".
- **The guide and the prompt fight over layout.** The canny circles where the swatches are, while the negative says `(color swatches:1.3)`. The circles may get filled with something else, such as eyes, icons or tufts. That is a layout artefact, not a wording failure.
- **The guide has no full-body side view.** The middle figure is a back three-quarter view. The style guide's "side view in the centre" can't be met with this guide, whatever the prompt says.
- **The canny copies interior details**, such as the back muscle lines and the small oval mark on the right figure's hip. Those come from the approved sheet, so they aren't a rule break.
- **The female rules ask for `white chest` and `black markings` in the negative.** Neither is there; only `(black fur:1.1)` is. Round 5 raised this, and Claude chose to defer it to the next job. It's a small colour cue, not a blocker.
- **Line weight is unaddressed.** Earlier jobs measured 0.21–0.22% against a target of about 0.33%, and nothing here changes it. It isn't part of this job's goal.
- **The censor-mark fault:** the negative keeps to `nsfw` and general terms, which is fine.

## Must fix
none

## Could improve
1. Add `white chest, (black markings:1.1)` to the negative, as `female-rules.md` asks. Expected effect: the chest won't fall from cream back to pure white, and the markings get pushed further toward blue. This is only colour words, so the job's size doesn't change. Round 5 deferred it, and it is Josh's call whether to add it now.
2. `pastel colors` is not in the negative. Round 3 removed it and round 4 asked to restore it, but no response from Claude was recorded. Either restore it at plain weight, or record why it was left out, so the next round doesn't flip it again. Expected effect: a little more pressure against the washed-out seafoam fur.
3. For the next job, not this one: if the outputs show the bust and swatches, the cleanest fix is a three-view-only guide from Josh. Cutting the canny `guidance_end` to about 0.4 lowers detail copying, but it won't remove the extra figures, because the layout is fixed in the first steps. Line weight (for example `(thick outlines:1.2)`) is also a separate future job.
