# Course Compliance Checklist

How this GDD meets **Assignment #1: First Draft of GDD**, and the [Capstone GDD Guidelines](GDD_Guidelines.md).

**Submission:** the GitHub repo link, https://github.com/joshkeal-daboyz/rest-gdd. The short GDD is the [README](../README.md), in Markdown (the instructor confirmed a PDF is not required). **Due:** 20 October 2026, 11:59 PM ET.

## Required sections

| Section required by the assignment | Where it's met |
| --- | --- |
| Executive Summary | [README §1](../README.md#1-executive-summary) |
| Game Mechanics (player-facing actions and loop) | [README §2](../README.md#2-game-mechanics) |
| AI Architecture (what each agent does, described through its effect on gameplay) | [README §3](../README.md#3-ai-architecture); detail in [docs/11](../docs/11-ai-architecture.md) |
| Technical Strategy (agent roles, token budget, API constraints) | [README §4](../README.md#4-technical-strategy); detail in [docs/12](../docs/12-technical-strategy.md) |

## Rubric

| Criterion | Points | How the GDD addresses it |
| --- | --- | --- |
| **Game Specificity**: named game, identifiable core loop, stated win/loss condition | 3.0 | Named game (*Rest*) and character (Enoch); core loop stated in §1 and played out in §2; **win** (the street relights) and **loss** (dawn breaks first) stated in §1 and §2 |
| **Player Experience Clarity**: what the player sees and does; agent behavior through gameplay effect | 2.5 | §2 is written from the player's point of view, starting on the dark street; every agent sentence in §3 ends with what the player sees or feels |
| **Agent Role Clarity**: each agent named, its development role in one sentence; abstract terms only where specific | 2.0 | Ten prototype agents in §3, one sentence each; coordination terms in §4 are tied to Rest (why the Lighting Director only listens for `grid:changed`) |
| **Technical Feasibility**: realistic scope; at least one constraint named and explained; plausible token budget | 1.5 | Prototype scoped to one street (§5); two constraints named and explained, plus an API constraints table (§4); token budget by agent and phase (§4) |
| **Presentation**: required sections present, free of major errors | 1.0 | Required sections use the assignment's names; tables over prose; long detail moved to `docs/` |

## Anti-slop gate

Every course concept is tied to a specific mechanic in Rest:

| Concept | Rest's version |
| --- | --- |
| One Wow moment | The Relight: power traveling down Lamp Row as the lamps ignite |
| One Wow agent | The Lighting Director |
| Weekend test | One street, three repairs, three parts, about ten grid nodes |
| Human review gates | G4 reviews the Relight itself; G3 reviews every line against the Lore Bible |
| Constraints direct agents | Three.js has no engine features, so every library is named; the 8-light rule is a rule agents must follow |

## The three-pillar checkpoint

1. **Pipeline:** "The Grid Simulator takes the grid JSON and repair events, produces grid state and `grid:changed` events, and the player sees lamps go dead, flicker, or light. The Lighting Director takes those events and produces the Relight, and the player sees the street come back to light."
2. **Constraints:** "My biggest constraint is that Three.js is a rendering library, not an engine, because it provides no editor, physics, character controller, or animation tooling, so each must come from a named library, or agents will invent their own."
3. **Budget:** about 3M tokens for the prototype, about 10M for the MVP.

## Before submitting

- [ ] Confirm whether the assignment's "provided template" exists. These guidelines say no template is provided; if one is, the README's sections may need to be reordered to match it.
- [ ] Read the README start to finish as it renders on GitHub.
- [ ] Submit the repo link to Google Classroom by 20 October, 11:59 PM ET.
