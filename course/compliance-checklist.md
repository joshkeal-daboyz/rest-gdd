# Course Compliance Checklist

How this GDD meets the [Capstone GDD Guidelines](GDD_Guidelines.md) for Assignment #1.

**Submission:** the GitHub repo link, https://github.com/joshkeal-daboyz/rest-gdd, to Google Classroom by **October 20**. The short GDD is the [README](../README.md).

## Draft checklist

| Requirement | Where it's met | Status |
| --- | --- | --- |
| Summary section | [README §1](../README.md#1-summary) | Done |
| Game Mechanics section | [README §2](../README.md#2-game-mechanics) | Done |
| AI Architecture section | [README §3](../README.md#3-ai-architecture), detail in [docs/11](../docs/11-ai-architecture.md) | Done |
| Technical Strategy section | [README §4](../README.md#4-technical-strategy), detail in [docs/12](../docs/12-technical-strategy.md) | Done |
| Every section specific to the game, describing what the player sees and does | README §2 opens with what the player sees; every agent sentence ends with what the player sees | Done |
| Scope passes the weekend test; future features in later phases | [README §5](../README.md#5-scope-and-phases), [docs/10](../docs/10-scope-roadmap.md) | Done |
| "Wow" moment and One Wow agent identified | The Relight; the Lighting Director (README §1 and §3) | Done |
| Each agent: name + one sentence (does X when Y, player sees Z) | README §3 crew table | Done |
| Human review gates and creative-control boundaries | README §3, gates G1–G5 | Done |
| Engine, tools, asset sources, and biggest constraints | README §4 | Done |
| Token budget projection | README §4, detail in docs/12 | Done |
| 5 pages or less, with longer detail in linked docs | The README is the short GDD; `docs/` is the long GDD | Check page count before submitting |
| Submitted by Oct 20 | Google Classroom | To do |

## The three-pillar checkpoint

1. **Pipeline:** "The Grid Simulator takes the grid JSON and repair events, produces grid state and `grid:changed` events, and the player sees lamps go dead, flicker, or light. The Lighting Director takes those events and produces the Relight, and the player sees the street come back to light."
2. **Constraints:** "My biggest constraint is that Three.js is a rendering library, not an engine, because it provides no editor, physics, character controller, or animation tooling, so each must come from a named library, or agents will invent their own."
3. **Budget:** about 3M tokens for the prototype, about 10M for the MVP.

## Rubric notes

| Rubric point | How the GDD addresses it |
| --- | --- |
| Game specificity | Every agent is defined by a Rest system (the grid, repairs, the Relight), not a generic role |
| Player experience clarity | README §2 is written from the player's point of view; acceptance criteria are player-facing |
| Agent role definitions | Ten prototype agents and five MVP agents, each with one sentence, an input, an output, and a folder it owns |
| Technical feasibility | A prototype of one street; named libraries; validation steps; risks with plans |
| Presentation | Short GDD as an index to the long GDD; tables over prose |
