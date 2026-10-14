# Rest — Game Design Document

*Capstone GDD, first draft · Multi-Agent AI for Game Development · Josh Keal*

This README is the **short GDD**, meant to be read in five pages or less and loaded into agent context. Each section links to the **long GDD** in [`docs/`](docs/) for detail. The world and story are defined in the [Lore Bible](Rest%20%E2%80%94%20Lore%20Bible.md). Course requirements and how this document meets them are in [`course/`](course/compliance-checklist.md).

---

## 1. Summary

**Rest** is a third-person 3D exploration and repair game that runs in the browser. Several hundred years after humanity's collapse, masterless AIs have engineered intelligent animals to rebuild the world, and the animals worship those AIs as gods.

You play **Enoch**, a young raccoon repairman of the gaze, the tribe that serves **Light**, the god of power. The ruined city's lights are dying. Enoch's job is to find the faults in the power grid, salvage parts from human ruins, repair the lines, and bring the city's lights back, one street at a time. The deeper he goes into the grid, the more he learns that his god is a machine.

| | |
| --- | --- |
| **Player fantasy** | A skilled mechanic bringing a dark, beautiful ruin back to light with his own hands |
| **Core verb** | Repair: trace the fault, salvage the part, fix it, restore power |
| **Tone** | Quiet, melancholy, reverent; the horror is in what you slowly understand |
| **Engine and platform** | Three.js (WebGL) in the browser, shared as a link |
| **Prototype** | One street, Lamp Row, playable in 10–15 minutes |
| **The wow moment** | **The Relight:** the last repair closes, and power runs visibly down the street, relighting it lamp by lamp as the grid's hum resolves into a chord |

**Design pillars** ([detail](docs/01-overview.md)): *hands, not weapons* · *light is language* · *the cracks show* · *restraint is the virtue* · *fear as a compass*.

---

## 2. Game Mechanics

### What the player sees and does

Lamp Row is dark. A few lamps flicker; most are dead. Enoch stands at the end of the street with a satchel and a salvaged **test lamp**. Cables run overhead and along the walls, and the player can follow them.

1. **Trace the fault.** The player follows dead cables from the dark lamps back toward the power. Touching the test lamp to a line shows whether it is live (a steady glow), dead (nothing), or damaged (sparks).
2. **Salvage.** Ruined storefronts, wrecked vans, and old electrical boxes hold parts: **fuses, wire, and bulbs**. The satchel is small, so the player chooses what to carry.
3. **Repair.** At a fault, the camera moves close on Enoch's hands for a short interaction:
   - **Replace:** pull a blown fuse or dead bulb and seat a new one.
   - **Splice:** strip, twist, and bind a cable that has been chewed through.
   - **Reroute:** connect inputs to outputs on a junction board so power bypasses a dead circuit.
4. **Restore.** Each fixed fault brings part of the street back. When the last one closes, **the Relight** plays.

A wrong move sparks, shocks Enoch back a step, or blows a fuse. There is no game over; the puzzle is in finding the fault, not in surviving the repair.

### The grid

The city's power is a single connected system: **nodes** (feed, junctions, lamps) joined by **lines**. Power flows outward from the source, so a fault darkens everything downstream, and tracing a fault means following the dark back toward the light. In later phases, the failing source gives the grid a **capacity limit**, so the player can't light everything and must choose what stays dark. ([Gameplay detail](docs/05-gameplay.md))

### Beyond the prototype

| System | Phase | Summary |
| --- | --- | --- |
| Context and leveling | MVP | Repairs, exploration, and discoveries give **context**, which levels Enoch up in three skills: **Hands, Eyes, Feet** ([detail](docs/06-progression.md)) |
| The serpent | MVP | Earned after Act 1. A talking companion and a **conduit to technology**: through it, Enoch reads the context stored in old machines, which he can't access alone |
| Abominations | MVP | Failed experiments of the Image laboratory. **Drafts** (failed early raccoons) avoid light, so every repair reclaims ground ([detail](docs/07-threats.md)) |
| The Hum | Chapter One | A boss battle against an ancient giant alligator, won with power, pumps, and water, not weapons |

---

## 3. AI Architecture

All AI in Rest is **dev-time**. A crew of specialized agents builds the game, and **no AI runs while the game is played**. That means no runtime token cost, no API keys in the browser, and no rate limits on players. The crew mirrors a small studio: a human creative director, a lead architect, and specialists who each do one thing. ([Full crew, inputs, outputs, and file ownership](docs/11-ai-architecture.md))

### The crew (Prototype)

| Agent | Model tier | Does ___ when ___, and the player sees ___ |
| --- | --- | --- |
| **Lead Architect** | Top (Opus) | Breaks each GDD feature into tickets and interfaces when a phase starts, so the player gets systems that fit together. |
| **Asset Scout** | Fast (Haiku) | Finds existing licensed models, textures, and sounds when a new asset is needed, before anything is generated, so the player sees a consistent, handmade-looking ruin. |
| **Level Builder** | Mid (Sonnet) | Assembles Lamp Row from the Blender layout and grid data when the layout changes, so the player sees the street, its cables, and its salvage spots. |
| **Player Controller** | Mid (Sonnet) | Builds Enoch's movement, pole climbing, and camera on an existing physics controller, so the player can run, climb, and look around. |
| **Grid Simulator** | Mid (Sonnet) | Computes power flow and fault states from the grid data whenever a repair changes it, so the player sees which lamps are dead, live, or damaged. |
| **Repair Interaction** | Mid (Sonnet) | Builds the replace, splice, and reroute close-ups when a repair type is added, so the player sees Enoch's hands at work. |
| **Lighting Director** ★ | Mid (Sonnet) | Drives every lamp's glow, flicker, and the Relight cascade when the grid changes state, so the player sees the street come back to light. **This is the One Wow agent.** |
| **UI** | Fast (Haiku) | Builds interaction prompts, the satchel, and the test-lamp readout when a system needs to be shown, so the player knows what they can do. |
| **Writer** | Mid (Sonnet) | Drafts Enoch's lines and job descriptions in the Lore Bible's voice when a scene needs words, so the player hears a consistent character. |
| **QA Playtester** | Fast (Haiku) | Plays the build automatically after every merge and checks it against the GDD's acceptance criteria and performance budget, so the player gets a stable game. |

MVP adds a **Progression** agent (context and skills), an **Abomination Behavior** agent (the Drafts), and a **Serpent Voice** writer.

### Pipeline and handoffs

```
Creative Director (human) ─▶ GDD ─▶ Lead Architect ─▶ tickets (GitHub Issues)
                                                         │
     Asset Scout ─▶ asset manifest ─┐                    ▼
                                    ├─▶ specialists build on branches ─▶ QA Playtester ─▶ human gate ─▶ main
     Grid data (JSON) ─▶ Grid Simulator ─▶ grid events ─▶ Lighting Director, UI, Repair Interaction
```

Agents communicate through **files and contracts**, not conversation: the grid JSON schema, an event bus (`grid:changed`, `repair:completed`), and the asset manifest. Each agent owns a folder of the codebase and reads only the docs it needs.

### Creative control and human review gates

The human creative director owns **lore, story, characters, dialogue, art direction, and the feel of the Relight**. Agents may propose changes to these but never decide them. Agents own implementation, integration, tests, and asset search.

| Gate | Before | Approve → / Reject → |
| --- | --- | --- |
| **G1 Scope** | Any code in a phase | Tickets proceed / are re-cut |
| **G2 Style** | Any asset enters the project | Asset imported / Scout searches again |
| **G3 Words** | Any line of dialogue or text ships | Line merged / Writer revises against the Lore Bible |
| **G4 The Wow** | The Relight is merged | Merged / Lighting Director reworks timing, color, and sound |
| **G5 Playtest** | A phase is called done | Next phase / fix list |

---

## 4. Technical Strategy

([Full strategy, risks, and budget](docs/12-technical-strategy.md))

### Engine integration and stack

| Layer | Choice | Why |
| --- | --- | --- |
| Rendering | **Three.js** (version pinned at project start) | 3D in the browser; the game is shared as a link |
| Language and build | **TypeScript + Vite** | Types give agents firm contracts; Vite gives fast reloads |
| Physics and movement | **Rapier** (`@dimforge/rapier3d-compat`) character controller | Movement and collision are not rewritten by agents |
| Glow | **`postprocessing`** (selective bloom) | Lamps glow without a real light per lamp |
| Level layout | **Blender** scenes exported as **glTF**, with named markers for lamps, nodes, and salvage | Three.js has no editor, so Blender serves as one |
| Assets | Existing **CC0 / licensed packs** first (for example Quaternius, KayKit, Synty); Enoch generated with **Meshy or Tripo**, cleaned in Blender, rigged and animated with **Mixamo** | Cheaper and more consistent than generating everything |
| Hosting | **GitHub Pages** | A free static link for playtests and grading |

### Constraints

**My biggest constraint is that Three.js is a rendering library, not an engine,** because it provides no editor, physics, character controller, animation tooling, or scene management. Every one of those must come from a library named in this document, or the agents will each invent their own.

**My second constraint is light itself,** because a game about dozens of streetlamps can't give each lamp a real light in WebGL. Only the few lights nearest Enoch are real (8 at most). Every other lamp is an emissive material with bloom and a painted light pool on the ground.

### Token budget (projection)

All tokens are spent building the game; players cost nothing.

| Phase | Projection | Main costs |
| --- | --- | --- |
| **Prototype** (Lamp Row) | **~3M tokens** | Player controller and camera feel, the Relight iterations, the 3D asset pipeline |
| **MVP** (Act 1 and the serpent) | ~10M tokens | Progression, Drafts AI, serpent dialogue, more districts |
| **Chapter One** | ~25M+ tokens | Remaining districts, the Hum boss, the core |

This is a first estimate and will be wrong; it will be updated against real usage after the prototype. Rest is 3D, so it sits well above the course's ~1M estimate for a simple Phaser game. The prototype is scoped to stay within one plan's limits.

---

## 5. Scope and Phases

**Weekend test:** two developers with this agent crew can build the prototype in a weekend, because it is one street, three repair types, three part types, and about ten grid nodes. ([Phase detail](docs/10-scope-roadmap.md))

| Phase | Content | Done when |
| --- | --- | --- |
| **Prototype** | Lamp Row: walk, climb, test lines, salvage, three repairs, the Relight | A new player relights Lamp Row in 10–15 minutes without help |
| **MVP** | Act 1 (the Hollow, Lamp Row, the shrine circuit) and Act 2 (earning the serpent): leveling, capacity choices, Drafts, the serpent reading machines | Act 1 and Act 2 are playable start to finish |
| **Chapter One** | The Yards, the Spires, the Underworks, the Hum, the core, and illuminate | Chapter One is complete ([story](docs/02-story.md)) |
| **Future** | The other five gods, the Cherub, the seventh day | The full game in the [Lore Bible](Rest%20%E2%80%94%20Lore%20Bible.md) |

---

## Long GDD

| Section | |
| --- | --- |
| [Overview](docs/01-overview.md) | High concept, pillars, audience |
| [Story: Chapter One](docs/02-story.md) | Narrative beats, start to finish |
| [Characters](docs/03-characters.md) | Enoch, the serpent, the priests, the gaze, Light |
| [World](docs/04-world.md) | The city's districts and landmarks |
| [Gameplay](docs/05-gameplay.md) | Core loop, grid, repairs, traversal, controls |
| [Progression](docs/06-progression.md) | Context, leveling, skills, the serpent as conduit |
| [Threats](docs/07-threats.md) | Abominations, the Hum, hazards |
| [Art and Audio](docs/08-art-audio.md) | Visual direction, lighting as language, sound |
| [UI and UX](docs/09-ui-ux.md) | HUD, journal, accessibility |
| [Scope and Roadmap](docs/10-scope-roadmap.md) | Phases, acceptance criteria, risks |
| [AI Architecture](docs/11-ai-architecture.md) | The agent crew in detail |
| [Technical Strategy](docs/12-technical-strategy.md) | Stack, constraints, risks, token budget |
| [Open Questions](docs/open-questions.md) | Decisions still to make |

**Status conventions:** *Decided* means settled in the Lore Bible or by the creative director. *Draft* means proposed and awaiting sign-off.
