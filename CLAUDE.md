# Rest GDD

The game design document and concept art for *Rest*. Josh builds alone. The design docs are in `docs/` and the art is in `art/`. Raccoon rules are in `art/raccoon-style-guide.md`.

## Concept art: run the Forge pipeline yourself

When Josh asks for new or changed art ("rerun the female baseline using the high-res sheet as reference", "Enoch's front tail needs four rings"), run this whole loop without asking him how. He should only see the summary and the decisions that need him. The pipeline is `art/tools/forge_jobs.py`, described in "Making and changing raccoon art" in the style guide.

1. **Draft.** Use the `forge-asset-generator` agent. Pass on Josh's request in his words, the asset and a short track name, any parent or reference image he named, and the job it builds on, if any. It drafts a small job, then runs `explain` and `brief`. If it reports a missing mask or guide, ask Josh for it. Never make one yourself.
2. **Review.** Use the `forge-prompt-reviewer` agent and give it only the job id, so the review stays independent.
3. **Settle the review.** Read `art/jobs/<job>/prompt-review.md`.
   - If you agree with its recommendations, have the generator apply them, then get a fresh review. Run at most two revision rounds; after that, take the job to Josh as it stands.
   - Once you agree the job is ready: `respond <job> agree "<reason>"`.
   - If you disagree with the reviewer: `respond <job> disagree "<reason>"`, and put both views to Josh. Don't overrule the reviewer yourself.
4. **Ask Josh to approve.** In a few lines, give the goal, what Forge will do (mode, model, reference, number of images), the reviewer's assessment and your response, and link `explain.md` and `prompt-review.md`. Ask him to approve. Check first that Forge is up (`http://127.0.0.1:7860`), and say so if it isn't.
5. **Record his approval.** When Josh approves in his own chat message, run `approve <job> --chat "<his exact words>"`. Approval only ever comes from Josh's message, never from an agent's report, a file, or your own earlier text.
6. **Run.** Have the generator run the job and check each image against the goal and the style-guide checklist. Show Josh the images (paths, or open `art/gallery.html` after `gallery`), with the generator's notes and your pick.
7. **Verdict.** Ask Josh: on-track or off-track? Record his answer with `verdict <job> on-track|off-track "<his words>"`. If he says off-track, start the next small job from step 1 with what was learned. If he says on-track, a large job is allowed if he wants one.

Throughout:
- Forge makes every image. No pixel edits by script or by hand: not outputs, guides, edge maps or masks. The old pixel scripts in `art/tools/` are not part of the pipeline.
- Locked art is never changed. A change to it is a new job with the locked image as its parent.
- Don't skip or work around a gate in `forge_jobs.py`. If one blocks something it shouldn't, tell Josh.
