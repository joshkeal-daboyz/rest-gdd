job: enoch-sheet-009-shading-no-lora
job-hash: aad0763d64e6ca37
assessment: will help
must-fix: 0

## Reason for the change, as I understood it
Jobs 006–008 never gave visible cel shading on the locked less-human 246 sheet. This job checks one suspect: whether the charsheet LoRA (0.6) is flattening every fill. It removes the LoRA and its trigger word and changes nothing else from 008, as Josh asked ("run without charsheet", "one change at a time").

## Will this job do it?
As a test, yes. It changes exactly one thing: `<lora:charsheet_lora_v1:0.6>` and `charsheet` are gone, and the prompt, negative, denoise 0.7, IP-Adapter (0.25, ending at 0.5), seeds 231506246–249, sampler, steps and CFG are all the same as 008. Because the seeds are fixed, each image can be compared with its 008 twin, so any shading that shows up can be credited to the LoRA's removal.

The words that should produce shading are still `(cel shading:1.3)`, `(anime coloring:1.1)`, `(simple shading:1.1)`, `shaded, shadow, sidelighting`, plus `flat colors` in the negative. Indigo Void is NoobAI-based and knows these Danbooru tags well. Without a LoRA trained on flat sheets, they have a fair chance of producing shadow shapes for the first time.

The one thing that can still defeat the test is the parent. I viewed the locked 246 sheet and the 007 and 008 outputs. All of them are pure flat fills, with only interior line strokes and no tonal second colour. At denoise 0.7, img2img still starts from a flat latent, and the IP-Adapter pulls toward the same flat image for the first half of the steps. If 009 comes out flat too, the parent and reference are the next suspects, not the wording. That is a finding, not a flaw in this job.

Layout risk is low. The 008 outputs at 0.7 kept all four views, the head sizes (0.191–0.200) and the line weight, and img2img holds layout far more than the LoRA does. Losing the trigger word shouldn't break the sheet.

## Risks and rule conflicts
- Flat-colour rule: the style guide says "flat colours … no painted shading". Josh has explicitly overridden this for shading, and the brief says the rule gets updated if this job is on-track. This is not a blocker.
- Charsheet LoRA missing on a `character-sheet` job: the reason is given (it's the variable under test, at Josh's request), so this is acceptable.
- Stray objects: in 008, three of four images grew stray objects at 0.7. The 008 seed-247 image I viewed has a headband, a black ear device or headphone on the back view, a collar on the tailless back, and heavier-lidded eyes. That breaks the "no accessories" rule. With the LoRA gone the model has less sheet prior, and this could get worse. `headband, headwear` are already in the negative, but `collar`, `headphones` and `goggles` are not.
- Expression: the narrowed, smug eyes in 008-247 lean away from "calm, slight smile". Watch for this.
- `shadow` and `sidelighting` can produce cast or floor shadows. `drop shadow` in the negative mostly covers this. If shading appears, check the background stays plain.
- The parent already has a dark X-marked spot on the tailless back view (the tail-base spot or censor-like mark). The negative still lists `breasts`, a body-part word, which the style guide links to the censor mark. This carries over from 005–008 and isn't new.
- Palette: once shading appears, check the base teal stays `#48C2C3`-ish and doesn't turn grey. `(grey fur:1.3)` and `charcoal grey` in the negative help here. Expect a new darker teal or navy shadow tone, which is the intended change.

## Must fix
none

## Could improve
1. Add `collar, headphones, goggles, accessories` to the negative. This should cut the stray objects 008 grew at the same denoise and seeds. It doesn't touch the shading words, so the LoRA test stays readable. If the strict one-change rule matters more, keep it for the next job.
2. If 009 is still flat, don't weight the shadow words up straight away. Test the flat pull first, one change at a time: either drop the IP-Adapter unit (or end it at 0.3), or keep it and remove `drop shadow` from the negative. The parent and reference are the remaining flat sources.
3. In the run notes, compare each output with its 008 twin seed for seed, so Josh can see what removing the LoRA changed beyond shading (layout, line weight, head size, extra objects).
