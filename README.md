# Rest — Game Design Document

*Assignment #1: First Draft of GDD · Multi-Agent AI for Game Development · Josh Keal*

This README is the **short GDD**: the submitted draft, and the document loaded into agent context. Each section links to the **long GDD** in [`docs/`](docs/) for detail. The world and story are defined in the [Lore Bible](Rest%20%E2%80%94%20Lore%20Bible.md). How this draft meets the assignment is tracked in the [compliance checklist](course/compliance-checklist.md).

---

## 1. Executive Summary

**Rest** is a third-person 3D exploration and repair game that runs in the browser. Several hundred years after humanity's collapse, masterless AIs have engineered intelligent animals to rebuild the world, and the animals worship those AIs as gods.

You play **Enoch**, a young raccoon repairman of the gaze, the tribe that serves **Light**, the god of power. The ruined city's lights are dying. Each night, Enoch takes a repair job from the temple: find the faults in the power grid, salvage parts from human ruins, repair the lines, and bring a street back to light before dawn drives the nocturnal raccoons underground. The deeper he goes into the grid, the more he learns that his god is a machine.

| | |
| --- | --- |
| **Player fantasy** | A skilled mechanic bringing a dark, beautiful ruin back to light with his own hands |
| **Core loop** | Trace the fault → salvage the part → repair it → restore power |
| **Win** | Every fault on the job is fixed and the street relights |
| **Loss** | Dawn breaks before the job is done, and the night restarts |
| **Prototype** | One street, Lamp Row, playable in 10–15 minutes |
| **The wow moment** | **The Relight:** the last repair closes, and power runs visibly down the street, relighting it lamp by lamp as the grid's hum resolves into a chord |
| **Engine and platform** | Three.js (WebGL) in the browser, shared as a link |
| **Tone** | Quiet, melancholy, reverent; the horror is in what you slowly understand |

**Design pillars** ([detail](docs/01-overview.md)): *hands, not weapons* · *light is language* · *the cracks show* · *restraint is the virtue* · *fear as a compass*.

---

## 2. Game Mechanics

### What the player sees and does

Night falls on Lamp Row. A few lamps flicker; most are dead. Enoch stands at the end of the street with a satchel and a salvaged **test lamp**, and the moon is just rising. Cables run overhead and along the walls, and the player can follow them.

1. **Trace the fault.** The player follows dead cables from the dark lamps back toward the power. Touching the test lamp to a line shows whether it is live (a steady glow), dead (nothing), or damaged (sparks).
2. **Salvage.** Ruined storefronts, wrecked vans, and old electrical boxes hold parts: **fuses, wire, and bulbs**. The satchel is small, so the player chooses what to carry.
3. **Repair.** At a fault, the camera moves close on Enoch's hands for a short interaction:
   - **Replace:** pull a blown fuse or dead bulb and seat a new one.
   - **Splice:** strip, twist, and bind a cable that has been chewed through.
   - **Reroute:** connect inputs to outputs on a junction board so power bypasses a dead circuit.
4. **Restore.** Each fixed fault brings part of the street back to light, and the player sees their progress spread down the block.

### Win and loss

- **Win:** the last fault closes and **the Relight** plays. Lamp Row is lit, the tribe moves into the newly lit street, and the job is done.
- **Loss:** raccoons are nocturnal, and each job lasts one night of about 20 minutes. The sky is the timer: the moon crosses it, then the horizon pales. If dawn breaks first, Enoch must retreat underground and the night restarts with the faults back in place. The player keeps what they learned, so the next night goes faster.
- **Setbacks:** a wrong connection sparks or shocks Enoch back a step, and a bad shock sends him to the last lit safe point. Neither ends the night, but both cost time before dawn.

### The grid

The city's power is a single connected system: **nodes** (the feed, junctions, lamps) joined by **lines**. Power flows outward from the source, so a fault darkens everything downstream. Tracing a fault means following the dark back toward the light. In later phases, the failing source gives the grid a **capacity limit**, so the player can't light everything and must choose what stays dark. ([Gameplay detail](docs/05-gameplay.md))

### Beyond the prototype

| System | Phase | What the player gets |
| --- | --- | --- |
| Context and leveling | MVP | Repairs and discoveries give **context**, which levels Enoch up in three skills: **Hands, Eyes, Feet** ([detail](docs/06-progression.md)) |
| The serpent | MVP | A talking companion earned after Act 1 and a **conduit to technology**: through it, Enoch reads old machines he can't understand alone |
| Abominations | MVP | Failed experiments of the Image laboratory. **Drafts** flee light, so every repair reclaims ground ([detail](docs/07-threats.md)) |
| The Hum | Chapter One | A boss battle against an ancient giant alligator, won with power, pumps, and water, not weapons |

---

## 3. AI Architecture

All AI in Rest is **development-time**. A crew of specialized agents builds the game, and **no AI runs while the game is played**. Each agent is defined below by its development role and by what it puts in front of the player. ([Inputs, outputs, and file ownership](docs/11-ai-architecture.md))

### The crew (Prototype)

| Agent | Development role, and its effect on gameplay |
| --- | --- |
| **Lead Architect** | Breaks each GDD feature into tickets and code interfaces when a phase starts, so the grid, repairs, and lights the player touches all respond to each other. |
| **Asset Scout** | Finds existing licensed models, textures, and sounds before anything is generated, so Lamp Row looks and sounds like one consistent, handmade ruin. |
| **Level Builder** | Assembles Lamp Row from the Blender layout and grid data, so the player sees a street whose cables can actually be followed from a dead lamp to its fault. |
| **Player Controller** | Builds Enoch's movement, pole climbing, and camera on an existing physics controller, so the player can run the street and climb to the overhead lines. |
| **Grid Simulator** | Computes how power flows and where it stops whenever a repair changes the grid, so the player sees the right lamps go dark, flicker, or light, and the test lamp reads true. |
| **Repair Interaction** | Builds the replace, splice, and reroute close-ups, so the player sees Enoch's hands do the work and feels a wrong move as a spark and a shock. |
| **Lighting Director** ★ | Drives every lamp's glow and flicker and choreographs the Relight, so the player watches power travel down the cables and the street come back to light. **This is the One Wow agent.** |
| **UI** | Builds interaction prompts, the satchel, and the test-lamp readout, so the player always knows what they can pick up, test, or fix. |
| **Writer** | Drafts Enoch's lines and the temple's job descriptions in the Lore Bible's voice, so the player hears a devout mechanic who explains the ruins through his faith. |
| **QA Playtester** | Plays the build automatically after every change and checks it against the acceptance criteria, so the player never meets a fault that can't be found or a repair that can't be finished. |

The **MVP** adds a **Progression** agent (context and skills), an **Abomination Behavior** agent (the Drafts), a **Serpent Voice** writer, a **Journal** agent, and a **UI Juice** agent ([detail](docs/11-ai-architecture.md#added-in-the-mvp)).

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

([Full stack, risks, validation steps, and budget](docs/12-technical-strategy.md))

### Stack

| Layer | Choice | Why |
| --- | --- | --- |
| Rendering | **Three.js** (version pinned at project start) | 3D in the browser; the game is shared as a link |
| Language and build | **TypeScript + Vite** | Types give agents firm contracts; Vite gives fast reloads |
| Physics and movement | **Rapier** character controller | Agents don't rewrite movement and collision |
| Glow | **`postprocessing`** (selective bloom) | Lamps glow without a real light per lamp |
| Level layout | **Blender** scenes exported as **glTF**, with named markers for lamps, nodes, and salvage | Three.js has no editor, so Blender serves as one |
| Assets | **CC0 / licensed packs** first (Quaternius, KayKit, Synty); Enoch generated with **Meshy or Tripo**, rigged and animated with **Mixamo** | Cheaper and more consistent than generating everything |
| Hosting | **GitHub Pages** | A free, shareable link for playtests |

### Agent roles and the pipeline

```
Creative Director (human) ─▶ GDD ─▶ Lead Architect ─▶ tickets (GitHub Issues)
                                                         │
     Asset Scout ─▶ asset manifest ─┐                    ▼
                                    ├─▶ specialists build on branches ─▶ QA Playtester ─▶ human gate ─▶ main
     Grid data (JSON) ─▶ Grid Simulator ─▶ grid events ─▶ Lighting Director, UI, Repair Interaction
```

Agents hand off work through **files**, not conversation: the grid JSON, two events (`grid:changed` and `repair:completed`), and the asset manifest. This matters for Rest specifically: the Lighting Director never reads the grid code. It only listens for `grid:changed`, so the wow moment can be reworked at gate G4 without touching the simulation.

### Constraints

**My biggest constraint is that Three.js is a rendering library, not an engine,** because it provides no editor, physics, character controller, animation tooling, or scene management. Every one of those must come from a library named in this document, or the agents will each invent their own.

**My second constraint is light itself,** because a game about dozens of streetlamps can't give each lamp a real light in WebGL. Only the 8 lights nearest Enoch are real. Every other lamp is an emissive material with bloom and a painted light pool on the ground.

### API constraints

| Service | Constraint | How Rest handles it |
| --- | --- | --- |
| **Claude** (the agent crew) | Plan usage limits per session and per week; finite context windows | Agents run in sequence, not all at once; the top-tier model is reserved for the Lead Architect; agents load the short GDD plus only the docs their ticket links |
| **Meshy / Tripo** | Credit-limited generation | Generate only Enoch and what the Asset Scout can't find; every generation passes gate G2 first |
| **Mixamo** | No public API | Rigging and animation are a manual human step in the pipeline |
| **Freesound** | API key required; rate limited; CC-BY sounds need credit | The Asset Scout batches searches and records every license in the manifest |
| **GitHub Pages** | Size limits on sites and files | Compressed models and audio; a first-load budget under 30 MB |
| **The game itself** | None | No runtime API calls: no keys in the browser, no per-player cost, no rate limits for players |

### Token budget (projection)

| Agent | Model tier | Prototype tokens |
| --- | --- | --- |
| Lead Architect | Top (Opus) | 200K |
| Lighting Director ★ | Mid (Sonnet) | 600K |
| Player Controller | Mid (Sonnet) | 500K |
| Repair Interaction | Mid (Sonnet) | 400K |
| Level Builder | Mid (Sonnet) | 300K |
| Grid Simulator | Mid (Sonnet) | 150K |
| Writer | Mid (Sonnet) | 50K |
| QA Playtester | Fast (Haiku) | 300K |
| UI | Fast (Haiku) | 150K |
| Asset Scout | Fast (Haiku) | 100K |
| Overhead and rework | — | 250K |
| **Prototype total** | | **~3M** |

The **MVP** projects to about 10M tokens and **Chapter One** to 25M or more. Rest is 3D, so it sits well above the course's ~1M estimate for a simple Phaser game. This first estimate will be wrong; usage is recorded per agent and the projection is revised after the prototype.

---

## 5. Scope and Phases

**Weekend test:** two developers with this crew can build the prototype in a weekend, because it is one street, three repair types, three part types, and about ten grid nodes. ([Phase detail](docs/10-scope-roadmap.md))

| Phase | Content | Done when |
| --- | --- | --- |
| **Prototype** | Lamp Row: walk, climb, test lines, salvage, three repairs, dawn, the Relight | A new player relights Lamp Row in 10–15 minutes, before dawn, without help |
| **MVP** | Act 1 (the Hollow, Lamp Row, the shrine circuit) and Act 2 (earning the serpent): leveling, capacity choices, Drafts, the serpent reading machines | Acts 1 and 2 play start to finish |
| **Chapter One** | The Yards, the Spires, the Underworks, the Hum, the core, illuminate | Chapter One is complete ([story](docs/02-story.md)) |
| **Future** | The other five gods, the Cherub, the seventh day | The full game in the [Lore Bible](Rest%20%E2%80%94%20Lore%20Bible.md) |

---

**Long GDD:** [Overview](docs/01-overview.md) · [Story](docs/02-story.md) · [Characters](docs/03-characters.md) · [World](docs/04-world.md) · [Gameplay](docs/05-gameplay.md) · [Progression](docs/06-progression.md) · [Threats](docs/07-threats.md) · [Art and Audio](docs/08-art-audio.md) · [UI and UX](docs/09-ui-ux.md) · [Scope and Roadmap](docs/10-scope-roadmap.md) · [AI Architecture](docs/11-ai-architecture.md) · [Technical Strategy](docs/12-technical-strategy.md) · [Open Questions](docs/open-questions.md)

*Decided* means settled in the Lore Bible or by the creative director. *Draft* means proposed and awaiting sign-off.
