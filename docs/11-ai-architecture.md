# 11. AI Architecture

[← Back to contents](../README.md)

This document is the contract between the creative director and the agent crew that builds Rest. It is a living document: agents will be added, removed, and refactored as the project grows.

## Principles

- **Dev-time only.** Agents build the game. No AI runs while the game is played, so players never spend tokens, and the browser never holds an API key.
- **One agent, one job.** Each agent does one thing well and owns one area of the codebase. Broad roles are split, not merged.
- **Contracts over conversation.** Agents hand off work through files: tickets, schemas, events, and manifests. An agent never needs another agent's full context.
- **Find before you generate.** Existing human-made assets are searched for before anything is generated.
- **The Lore Bible is law.** No agent may change what the Lore Bible decides. Agents can propose changes in a ticket for the creative director.

## The crew

The model tier is a default: the top tier for reasoning across the whole project, the mid tier for focused building, and the fast tier for searching, checking, and small UI work.

### Leadership

**Creative Director (human: Josh)**
- **Role:** owns the vision. Approves every gate below.
- **Owns:** the Lore Bible, the story, characters, dialogue, art direction, and the feel of the Relight.

**Lead Architect** · top tier (Opus)
- **One sentence:** breaks each GDD feature into tickets and interfaces when a phase starts, so the player gets systems that fit together.
- **Input:** the short GDD, the relevant long GDD docs, the current codebase map.
- **Output:** GitHub Issues with acceptance criteria; TypeScript interfaces and event definitions in `src/core/`.
- **Does not:** write feature code or decide anything creative.

### Prototype specialists

**Asset Scout** · fast tier (Haiku)
- **One sentence:** finds existing licensed models, textures, and sounds when a new asset is needed, before anything is generated, so the player sees a consistent, handmade-looking ruin.
- **Input:** an asset request (what, where it's used, style notes from [Art and Audio](08-art-audio.md)).
- **Output:** entries in `assets/manifest.json`: source, license, file, and a preview. If nothing fits, a generation request for the creative director.
- **Owns:** `assets/manifest.json`, `assets/licenses/`.

**Level Builder** · mid tier (Sonnet)
- **One sentence:** lays out Lamp Row from canned asset pieces using a written layout file and the grid data when the layout changes, so the player sees the street, its cables, and its salvage spots.
- **Input:** `levels/lamp-row.layout.json` (which pack pieces go where, plus named spots such as `lamp_03`, `junction_A`, `salvage_02`), `levels/lamp-row.grid.json`, the asset manifest, and a written description of the street from [World](04-world.md).
- **Output:** the level loader and scene code; cables drawn between grid nodes; a top-down debug view and screenshots so the creative director can review the layout without opening any 3D tool.
- **Why data, not Blender:** no one on the team models or uses Blender, so the level is a file agents can read, write, and diff.
- **Owns:** `src/level/`.

**Player Controller** · mid tier (Sonnet)
- **One sentence:** builds Enoch's movement, pole climbing, and camera on Rapier's character controller, so the player can run, climb, and look around.
- **Input:** Enoch's AI-generated model and Mixamo animations (including a working animation for repairs), climbable spots from the level.
- **Output:** movement, climbing, camera follow and collision, the animation state machine.
- **Owns:** `src/player/`, `src/camera/`.
- **Does not:** write its own physics.

**Grid Simulator** · mid tier (Sonnet)
- **One sentence:** computes power flow and fault states from the grid data whenever a repair changes it, so the player sees which lamps are dead, live, or damaged.
- **Input:** the grid JSON (nodes, lines, faults), `repair:completed` events.
- **Output:** the grid state and `grid:changed` events. The test lamp's reading comes from this state.
- **Owns:** `src/grid/`. Pure logic with no rendering, so it can be unit tested.

**Repair Interaction** · mid tier (Sonnet)
- **One sentence:** builds the click-and-hold repair and its part check when a fault type is added, so the player sees Enoch work while the ring fills and is told exactly which part they still need.
- **Input:** fault definitions from the grid data (required part, hold time), satchel contents.
- **Output:** the hold interaction, the part check, and `repair:completed` and `repair:cancelled` events.
- **Owns:** `src/repair/`.

**Lighting Director** ★ One Wow agent · mid tier (Sonnet)
- **One sentence:** drives every lamp's glow, flicker, and the Relight cascade when the grid changes state, so the player sees the street come back to light.
- **Input:** `grid:changed` events, the light-state table in [Art and Audio](08-art-audio.md), the light budget (8 real lights at most).
- **Output:** emissive materials, selective bloom, real-light pooling near Enoch, flicker patterns, and the Relight: power traveling visibly along cables, lamps igniting in sequence, and the hum resolving into a chord.
- **Owns:** `src/lighting/`, `src/audio/grid-hum/`.
- **Why it's the wow:** the Relight is the moment players will remember and share, and the technical strategy is built around making it work.

**UI** · fast tier (Haiku)
- **One sentence:** builds interaction prompts, the satchel, and the test-lamp readout when a system needs to be shown, so the player knows what they can do.
- **Input:** events from the player, repair, and grid systems; the UI rules in [UI and UX](09-ui-ux.md).
- **Output:** HTML/CSS overlay components.
- **Owns:** `src/ui/`.
- **Later split:** a **UI Juice** agent for animation and polish in the MVP.

**Writer** · mid tier (Sonnet)
- **One sentence:** drafts Enoch's lines and job descriptions in the Lore Bible's voice when a scene needs words, so the player hears a consistent character.
- **Input:** the Lore Bible, [Characters](03-characters.md), a scene brief.
- **Output:** `content/lines/*.json`. Text only, never code.
- **Owns:** `content/`.

**QA Playtester** · fast tier (Haiku)
- **One sentence:** plays the build automatically after every merge and checks it against the GDD's acceptance criteria and performance budget, so the player gets a stable game.
- **Input:** acceptance criteria from tickets and [Scope and Roadmap](10-scope-roadmap.md); the built site.
- **Output:** a test report on the pull request: scripted playthroughs (Playwright), frame rate, draw calls, console errors.
- **Owns:** `tests/`.

### Added in the MVP

| Agent | One sentence |
| --- | --- |
| **Progression** | Tracks context and applies skill ranks when Enoch learns something, so the player sees him level up and get better at his work. |
| **Abomination Behavior** | Builds the Drafts' light-avoiding, scavenging behavior when a district has dark zones, so the player sees the dark held by something that flees the light. |
| **Serpent Voice** | Writes the serpent's barks and dialogue, escalating with its fear, when a scene or a forbidden place needs them, so the player hears a guide whose worry points toward the truth. |
| **Journal** | Pairs each machine's faith-filtered and conduit entries when Enoch reads a machine, so the player sees what he believed beside what the machine told him. |
| **UI Juice** | Adds animation and polish to UI components when they're functionally done, so the game feels finished. |

## Handoffs

```
Creative Director ──▶ GDD ──▶ Lead Architect ──▶ GitHub Issues (one per task, with acceptance criteria)
                                                       │
                                                       ▼
                              Specialist agent works on its own branch, in its own folder
                                                       │
                                                       ▼
                              Pull request ──▶ QA Playtester report ──▶ Human gate ──▶ main
```

### Contracts

| Contract | Written by | Read by |
| --- | --- | --- |
| `levels/*.grid.json`: grid nodes, lines, faults (with required part and hold time) | Level Builder, approved by the Creative Director |
| `levels/*.layout.json`: which asset pieces go where | Level Builder, approved by the Creative Director | Grid Simulator, Level Builder, Repair Interaction |
| `grid:changed`, `repair:completed`, `repair:cancelled` events | Lead Architect (defined in `src/core/events.ts`) | Lighting Director, UI, Repair Interaction |
| `assets/manifest.json` | Asset Scout | Level Builder, Player Controller, Lighting Director |
| `content/lines/*.json` | Writer, Serpent Voice | UI |

## Creative control and review gates

| Gate | Reviewed by the human | Before | Approve | Reject |
| --- | --- | --- | --- | --- |
| **G1 Scope** | The tickets for a phase | Any code in that phase | Tickets proceed | The Lead Architect re-cuts them |
| **G2 Style** | Every asset in the manifest; every generated model | The asset enters the project | Imported | The Asset Scout searches again, or a generation is redone |
| **G3 Words** | Every line of dialogue and text | It ships | Merged | The Writer revises against the Lore Bible |
| **G4 The Wow** | The Relight, played in the browser | It merges | Merged | The Lighting Director reworks timing, color, and sound |
| **G5 Playtest** | A full playthrough of the phase | The phase is called done | The next phase starts | A fix list is ticketed |

## Reference documents agents rely on

The more an agent generates on its own, the more it needs references.

- [Lore Bible](../Rest%20%E2%80%94%20Lore%20Bible.md): the source of truth for story, names, and tone.
- [Art and Audio](08-art-audio.md): the style guide and the light-state table.
- [Characters](03-characters.md): voices and personalities.
- The grid JSON schema in `src/core/` (created by the Lead Architect in the prototype).
