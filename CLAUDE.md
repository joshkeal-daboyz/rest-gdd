# Rest GDD

The game design document and concept art for *Rest*. Josh builds alone. The design docs are in `docs/` and the art is in `art/`. Raccoon rules are in `art/raccoon-style-guide.md`.

## Concept art: run the Forge pipeline yourself

When Josh asks for new or changed art ("rerun the female baseline using the high-res sheet as reference", "Enoch's front tail needs four rings"), run this whole loop without asking him how. He should only see the summary and the decisions that need him. The pipeline is `art/tools/forge_jobs.py`, described in "Making and changing raccoon art" in the style guide.

1. **Draft.** Use the `forge-asset-generator` agent. Pass on Josh's request in his words, the asset and a short track name, any parent or reference image he named, and the job it builds on, if any. It drafts a small job, then runs `explain` and `brief`. If it reports a missing mask or guide, ask Josh for it. Never make one yourself.
2. **Review.** Use the `forge-prompt-reviewer` agent and give it only the job id, so the review stays independent.
3. **Settle the review.** Read `art/jobs/<job>/prompt-review.md`.
   - Reviews split recommendations into **Must fix** and **Could improve**. Only must-fix items you agree with go back to the generator; then `brief` (which archives the old review) and a fresh review. Apply optional items only if they're clearly worth it, never just to please the reviewer. Don't tell Josh about optional items you leave out; they stay in `prompt-review.md` if he wants them.
   - A review with `must-fix: 0` ends the loop. After 3 rounds, take the job to Josh as it stands, with what's left. If a reviewer undoes an earlier round's change without a good reason, say so in your response and don't apply it.
   - Once you agree the job is ready: `respond <job> agree "<reason>"`.
   - If you disagree with the reviewer: `respond <job> disagree "<reason>"`, and put both views to Josh. Don't overrule the reviewer yourself.
4. **Ask Josh to approve.** In a few lines, give the goal, what Forge will do (mode, model, reference, number of images), the reviewer's assessment and your response (for a clean review, just "Review: will help, nothing to fix"), and link `explain.md` and `prompt-review.md`. Ask him to approve. Check first that Forge is up (`http://127.0.0.1:7860`), and say so if it isn't.
5. **Record his approval.** When Josh approves in his own chat message, run `approve <job> --chat "<his exact words>"`. Approval only ever comes from Josh's message, never from an agent's report, a file, or your own earlier text.
6. **Run.** Have the generator run the job and check each image against the goal and the style-guide checklist. `run` also measures head size and line weight (read-only). Show Josh the images (paths, or open `art/gallery.html` after `gallery`), with the generator's notes and your pick.
7. **Verdict.** Ask Josh: on-track or off-track? Record his answer with `verdict <job> on-track|off-track --chat "<his exact words>" "<one-line reason>" --best <output he liked most>`, only from his own message. Add `--best` whenever he names a favourite image: `new --from` that job then uses it as the parent. The reason says what made it on- or off-track (from Josh's words and the generator's notes); later reviewers read it. For a character, also add the lesson to its rules file's "What her/his jobs have taught us" section. If he says off-track, start the next small job from step 1 with what was learned. If he says on-track, a large job is allowed if he wants one.
8. **Lock the winner.** When an image is good enough to keep, ask Josh whether to lock it, naming your pick. When he says so in his own message, run `lock art/jobs/<job>/out/<file>.png --chat "<his exact words>"`. This copies the image byte for byte to `art/locked/<asset>/`, which git tracks, and marks it locked. Commit the locked copy with the job's records. Locked images are never changed; a change is a new job with the locked copy as its parent.

Throughout:
- Forge makes every image. No pixel edits by script or by hand: not outputs, guides, edge maps or masks. The old pixel scripts in `art/tools/` are not part of the pipeline.
- Locked art is never changed. A change to it is a new job with the locked image as its parent.
- Don't skip or work around a gate in `forge_jobs.py`. If one blocks something it shouldn't, tell Josh.
- A project hook (`.claude/hooks/forge_guard.py`) backs these rules up. It blocks:
  - the old pixel scripts
  - direct calls to Forge's generate endpoints
  - inline code that saves images
  - hand edits to `state.json` and to the approved models list
  - prompt reviews written by anyone but the reviewer agent
  - agents running `approve`, `verdict`, `respond` or `status`

  If it blocks you, follow its message; don't look for a way around it.
- More than one session may work in this folder. Run `list` before starting, and leave alone any job another session is working on. If a step stops with "is busy", another session is mid-step on that job: wait or ask Josh. Never delete a `.busy` marker; one left by a crash clears itself after 90 minutes.
- Commit each job's records (`job.json`, `explain.md`, the brief, the reviews, `state.json`) once Josh gives a verdict. The images in `out/` are ignored by git and stay on this PC.
