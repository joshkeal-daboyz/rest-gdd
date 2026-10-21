# Rest — Game Design Document

*Assignment #1: First Draft of GDD · Multi-Agent AI for Game Development · Josh Keal*

This README is the **short GDD**: the submitted draft, and the document loaded into agent context. Each section links to the **long GDD** in [`docs/`](docs/) for detail. The world and story are defined in the [Lore Bible](Rest%20%E2%80%94%20Lore%20Bible.md). How this draft meets the assignment is tracked in the [compliance checklist](course/compliance-checklist.md).

---

## 1. Executive Summary

**Rest** is a third-person 3D exploration and repair game that runs in the browser. Several hundred years after humanity's collapse, masterless AIs have engineered intelligent animals to rebuild the world, and the animals worship those AIs as gods.

You play **Enoch**, a young raccoon repairman of the gaze, the tribe that serves **Light**, the god of power. The ruined city's lights are dying. Enoch is attuned to Light's power, and through his lamp he can *see* current flowing in the lines. Each night, he takes a repair job from the temple: plan what to carry, trade for parts in the Hollow, salvage more from human ruins, read the lines to find the faults, cut the power, repair them, and throw the breaker to bring a street back to light. Dawn drives the nocturnal raccoons underground, so jobs are meant to take several nights, and every repair holds until he returns. Every job that sends him closer to the data center at the city's core brings him closer to the truth of what Light really is.

| | |
| --- | --- |
| **Player fantasy** | A skilled mechanic bringing a dark, beautiful ruin back to light with his own hands |
| **Core loop** | Prep in town → read the lines → breaker off → repair → breaker on |
| **Win** | Every fault on the job is fixed, the breaker is thrown, and the street relights |
| **Loss** | The night is lost if dawn breaks (repairs stay) or Enoch dies of shock (that night's repairs are undone) |
| **Prototype** | One street, Lamp Row: the tutorial job, relit within two 15-minute nights |
| **The wow moment** | **The Relight:** with every fault fixed, Enoch throws the breaker, and power runs visibly down the street, relighting it lamp by lamp as the grid's hum resolves into a chord |
| **Engine and platform** | Three.js (WebGL) in the browser, shared as a link |
| **Tone** | Quiet, melancholy, reverent; the horror is in what you slowly understand |
| **What the player knows** | Only that this is a post-apocalyptic world. The truth about Light is in this document so the team can design for it; nothing the player sees states it, Light is never seen or heard until the very end, and there is no story exposition ([detail](docs/01-overview.md#what-the-player-knows-decided)) |

**Design pillars** ([detail](docs/01-overview.md)): *hands, not weapons* · *light is language* · *the cracks show* · *restraint is the virtue* · *fear as a compass*.

---

## 2. Game Mechanics

### What the player sees and does

Night falls on Lamp Row. A few lamps flicker; most are dead. Enoch stands at the Hollow end of the street with a satchel, a spool of prayer ribbon, and his **lamp**, and the moon is just rising. Every cable in the street is part of the grid, and the player can follow them.

Jobs are meant to take more than one night. Enoch's mentor says so when he hands over the first one: look first, come back ready. On the first night, the mentor teaches each step below the first time the player needs it, never all at once ([onboarding](docs/09-ui-ux.md#onboarding-the-first-night)).

1. **Prep in town.** Parts come in three kinds: **fuses, wire, and bulbs**. In the Hollow, the **temple stores** trade in **favor**: any part given as an offering earns favor, and favor draws any part from the stores, which never run out. Favor takes no room in the satchel, so offering spare parts banks their value for later. The satchel holds only **4 parts**, so the player plans what to carry out before the job. Enoch starts the tutorial with no favor: he earns it by salvaging and offering. **Every finished job pays favor,** starting with the tutorial. For now, every part costs **2 favor** to draw and earns **1 favor** as an offering (temporary, until playtesting). Jobs have no night limit, so farming salvage across nights is a valid strategy. In the prototype, the Hollow is a temple offering stall at the head of Lamp Row.
2. **Read the lines.** With the breaker on, the player **holds up the lamp**, and any cable within about 5 meters shows its current: pulses of light flowing away from the source. Dead cables show nothing. Damaged cables spark on their own, even without the lamp. Live cables never glow on their own, so the street stays dark until Enoch looks. Enoch walks slower with the lamp raised. Each fault has a signature:
   - **Blown fuse:** pulses run into a fuse box, and none come out. Needs a **fuse**.
   - **Damaged cable:** pulses run up to a sparking break and stop. Needs **wire**, and Enoch may have to climb to it.
   - **Dead lamp:** pulses reach the lamp post, but the lamp stays dark. Needs a **bulb**.

   When Enoch finds a fault, he ties a length of **prayer ribbon** to it. Prayer ribbon is the tribe's flagging tape: the gaze ties it on holy lines and breakers, and Enoch carries a spool. The ribbons glow in the dark, so the faults stay marked once the power is cut, and they stay marked across nights. The spool never runs out, and a ribbon can be untied if the player marked the wrong spot.
3. **Salvage.** Ruined storefronts, wrecked vans, and old electrical boxes in the city hold parts too. Salvage spots restock each night, so a player who is short can always salvage, offer, and draw what they need. Parts found now can be offered or kept for later jobs.
4. **Breaker off.** Breakers are found throughout the city, and the tribe marks every one so it is easy to spot. Throwing a **breaker** cuts the power to its section, and the street goes fully dark except for the ribbons.
5. **Repair.** At a marked fault, the player **clicks and holds**. Enoch goes to work, and a ring fills around the fault. Letting go early cancels the repair, and the part is not used up. A repair can't start without the right part: the prompt shows what's missing (*Needs: wire*). Parts can be dropped anywhere to make room. When a repair finishes, the part is used up, the ribbon comes off, and the repaired part **looks new** (a fresh bulb, clean wire, a bright fuse). Nothing lights yet: the change shows when the breaker goes back on.
   - **Live repairs.** Enoch can skip the breaker and repair a live line, but it is dangerous. The prompt warns *Live line. Cut the power, or hold to risk it.* The ring gets a timing check: clicking as the ring passes a mark finishes the repair, and a miss **shocks** him, throws him back, and cancels the repair without using the part. After one shock, the screen edges dim and his hands shake for the rest of the night; there is no health bar, and shocks heal by the next night. A second shock in one night kills him, and every repair he made that night is undone. On a high-power line, one shock kills. It's a high-risk, high-reward choice: save the walk, or risk the night's work.
6. **Breaker on.** Power pushes further down the street. Fixing one fault can uncover another beyond it, so the player raises the lamp and reads again. When every fault is fixed, throwing the breaker plays **the Relight**. Once the Relight starts, the job is won, even if dawn is close.

**Lamp Row by the numbers** (temporary, until playtesting): **8 faults** (5 dead lamps, 2 blown fuses, 1 damaged cable), one fuse box hidden until a lamp beyond it is fixed. **6 salvage spots**, each restocking 1 part of a fixed type each night (3 bulb, 1 fuse, 1 wire, 1 random). Finishing the job pays **6 favor**. The job needs 8 parts and the satchel holds 4, so it takes at least two trips. ([Detail](docs/05-gameplay.md#salvage-draft))

### Win and loss

- **Win:** with every fault fixed, Enoch throws the breaker and **the Relight** plays. Lamp Row is lit, the tribe moves into the newly lit street, and the job is done.
- **Loss: the night is lost.** There are two ways to lose a night:
  - **Dawn.** Raccoons are nocturnal, and a night lasts **15 minutes at most**. The sky is the timer: the moon crosses it, then the horizon pales. If dawn breaks before the job is done, the player watches the sun come up over a street that is only partly lit as Enoch retreats underground. **The work stays done:** every repair holds, and the next night starts in the Hollow with only the remaining faults left.
  - **Death.** A second shock (or one on a high-power line) kills Enoch. **That night's repairs are undone,** the parts used on them are gone, and their faults come back with their ribbons tied. Repairs from earlier nights stay. Enoch keeps his satchel and his favor, and the next night starts in the Hollow.
- **What always carries over:** the ribbons stay tied, so the player keeps what they learned even when they lose what they built. A repair in progress when the night is lost is cancelled, and its part stays in the satchel.
- **What costs time:** reading the wrong cable, walking to a breaker and back, hunting for a missing part, and letting go of a repair too early. The puzzle is in finding faults and planning the part economy (what to draw, what to carry, what to salvage and offer for later jobs), not in the repair itself.

### The grid

The city's power is a single connected system: **nodes** (the feed, breakers, switches, fuse boxes, lamps) joined by **lines**. Power flows outward from the source, so a fault darkens everything downstream. Tracing a fault means following the current until it stops. Two controls change where power goes: a **breaker** shuts a section off entirely, and a **switch** sends power down one branch or another. The tribe marks both. Lamp Row, the tutorial, has only breakers. In later phases, the failing source gives the grid a **capacity limit**, so the player has to use switches to choose what stays dark. ([Gameplay detail](docs/05-gameplay.md))

### Beyond the prototype

| System | Phase | What the player gets |
| --- | --- | --- |
| Context and leveling | MVP | Repairs and discoveries give **context**, which levels Enoch up in three skills: **Hands, Eyes, Feet** ([detail](docs/06-progression.md)) |
| The serpent | Chapter One | A talking companion given in Act 2, once his Act 1 work sets him apart, and a **conduit to technology**: through it, Enoch reads old machines he can't understand alone |
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
| **Level Builder** | Lays out Lamp Row from canned asset pieces using a written layout file and the grid data, so the player sees a street whose cables can actually be followed from a dead lamp to its fault. |
| **Player Controller** | Builds Enoch's movement, pole climbing, and camera on an existing physics controller, so the player can run the street and climb to the overhead lines. |
| **Grid Simulator** | Computes how power flows and where it stops whenever a repair or a breaker changes the grid, declares the job complete when the breaker goes on with no faults left, and owns the night (the dawn timer, the shock count, and rolling back a night's repairs on death), so the player sees the right lamps go dark or light and the lamp shows true current. |
| **Repair Interaction** | Builds the click-and-hold repair, its part check, and the live-repair timing check and shocks, so the player sees Enoch work while the ring fills, is told exactly which part they still need, and feels the danger of skipping the breaker. |
| **Lighting Director** ★ | Drives every lamp's glow, the current pulses Enoch's lamp reveals, and the Relight, so the player watches power travel down the cables and the street come back to light. **This is the One Wow agent.** |
| **UI** | Builds interaction prompts, the satchel, the temple stores' offering screen, and the prayer ribbons, so the player always knows what they can pick up, trade, mark, or fix. |
| **Writer** | Drafts Enoch's lines and the temple's job descriptions in the Lore Bible's voice, so the player hears a devout mechanic who explains the ruins through his faith. |
| **QA Playtester** | Plays the build automatically after every change and checks it against the acceptance criteria, so the player never meets a fault that can't be found or a repair that can't be finished. |

The **MVP** adds a **Progression** agent (context and skills), an **Abomination Behavior** agent (the Drafts), a **Journal** agent, and a **UI Juice** agent ([detail](docs/11-ai-architecture.md#added-in-the-mvp)). **Chapter One** adds a **Serpent Voice** writer ([detail](docs/11-ai-architecture.md#added-in-chapter-one)).

### Creative control and human review gates

The human creative director owns **lore, story, characters, dialogue, art direction, and the feel of the Relight**, and draws Enoch's concept art by hand. Agents may propose changes to these but never decide them. Agents own implementation, integration, tests, and asset search.

| Gate | Before | Approve → / Reject → |
| --- | --- | --- |
| **G1 Scope** | Any code in a phase | Tickets proceed / are re-cut |
| **G2 Style** | Any asset enters the project | Asset imported / Scout searches again |
| **G3 Words** | Any line of dialogue or text ships | Line merged / Writer revises against the Lore Bible |
| **G4 The Wow** | The Relight is merged | Merged / Lighting Director reworks timing, color, and sound |
| **G5 Playtest** | A phase is called done; includes a **cold playtest** by someone new to the game | Next phase / fix list |

The **cold playtest** is how "without help" is measured, because the QA Playtester already knows the rules and can't get confused. One person who has never seen the game plays it with no coaching. The creative director times them, notes where they stall, and asks one question at the end: *"What did you think the temple was?"*

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
| Level layout | A **written layout file** (JSON) placing canned pieces, lamps, grid nodes, salvage spots, and the temple stores, plus a top-down debug view for review | Three.js has no editor, and no one on the team models, so levels are data |
| Assets | **Free CC0 packs** (Quaternius, KayKit, Kenney) for the city; **Enoch generated in Tripo** from the creative director's hand-drawn concept art (Meshy as the backup), **auto-rigged in Tripo** (tail included), and animated with stock **Mixamo** animations. Fallback: a Tripo sample character close to Enoch's look | Free to start; no hand modeling anywhere in the pipeline |
| Hosting | **GitHub Pages** | A free, shareable link for playtests |

### Agent roles and the pipeline

```
Creative Director (human) ─▶ GDD ─▶ Lead Architect ─▶ tickets (GitHub Issues)
                                                         │
     Asset Scout ─▶ asset manifest ─┐                    ▼
                                    ├─▶ specialists build on branches ─▶ QA Playtester ─▶ human gate ─▶ main
     Grid data (JSON) ─▶ Grid Simulator ─▶ grid events ─▶ Lighting Director, UI, Repair Interaction
```

Agents hand off work through **files**, not conversation: the grid JSON, a handful of events (`grid:changed`, `repair:completed`, `breaker:thrown`, `job:completed`), and the asset manifest. This matters for Rest specifically: the Lighting Director never reads the grid code. It only listens for `grid:changed` and `job:completed`, so the wow moment can be reworked at gate G4 without touching the simulation.

### Constraints

**My biggest constraint is that Three.js is a rendering library, not an engine,** because it provides no editor, physics, character controller, animation tooling, or scene management. Every one of those must come from a library named in this document, or the agents will each invent their own.

**My second constraint is that I don't create 3D models,** because every asset has to be canned or AI-generated. The risk is a mismatched look. To prevent it, the city comes from one free pack family. Enoch is generated from my own drawings of him (front, side, and back, photographed for Tripo's image-to-3D), drawn to match the pack's style. Every asset passes gate G2.

**My third constraint is light itself,** because a game about dozens of streetlamps can't give each lamp a real light in WebGL. Only the 8 lights nearest Enoch are real. Every other lamp is an emissive material with bloom and a painted light pool on the ground.

### API constraints

| Service | Constraint | How Rest handles it |
| --- | --- | --- |
| **Claude** (the agent crew) | Plan usage limits per session and per week; finite context windows | Agents run in sequence, not all at once; the top-tier model is reserved for the Lead Architect; agents load the short GDD plus only the docs their ticket links |
| **Tripo / Meshy** | Credit-limited generation | Generate only Enoch (from the creative director's drawings) and what the free packs don't have; every generation passes gate G2 |
| **Mixamo** | No public API | Picking animations for Tripo's rig is a short manual step (upload, pick, download), with no modeling skill needed |
| **Freesound** | API key required; rate limited; CC-BY sounds need credit | The Asset Scout batches searches and records every license in the manifest |
| **GitHub Pages** | Size limits on sites and files | Compressed models and audio; a first-load budget under 30 MB |
| **The game itself** | None | No runtime API calls: no keys in the browser, no per-player cost, no rate limits for players |

### Token budget (projection)

| Agent | Model tier | Prototype tokens |
| --- | --- | --- |
| Lead Architect | Top (Opus) | 200K |
| Lighting Director ★ | Mid (Sonnet) | 600K |
| Player Controller | Mid (Sonnet) | 500K |
| Level Builder | Mid (Sonnet) | 400K |
| Repair Interaction | Mid (Sonnet) | 150K |
| Grid Simulator | Mid (Sonnet) | 150K |
| Writer | Mid (Sonnet) | 50K |
| QA Playtester | Fast (Haiku) | 300K |
| UI | Fast (Haiku) | 150K |
| Asset Scout | Fast (Haiku) | 100K |
| Overhead and rework | — | 250K |
| **Prototype total** | | **~2.9M** |

The **MVP** projects to about 10M tokens and **Chapter One** to 25M or more. Rest is 3D, so it sits well above the course's ~1M estimate for a simple Phaser game. This first estimate will be wrong; usage is recorded per agent and the projection is revised after the prototype.

---

## 5. Scope and Phases

**Weekend test:** the weekend build is the prototype's **core**, which is never cut: reading lines with the lamp, ribbons, the breaker, click-and-hold repairs, salvage, the satchel, dawn, and the Relight, on one street of about ten grid nodes built entirely from canned and generated assets. The full prototype adds more and may take a week or two. Agents run one at a time under usage limits, so if the build falls behind, features are cut in this order ([cut list](docs/10-scope-roadmap.md#cut-list)):

1. Pole climbing (the damaged cable moves to a ground-level junction box)
2. Live repairs, the timing check, shocks, and death (repairs need the breaker off; dawn is the only loss)
3. The temple stores and favor (salvage only; spots still restock each night)
4. The hidden fuse box (all 8 faults visible from the start)
5. The side-branch breaker (one main breaker)

| Phase | Content | Done when |
| --- | --- | --- |
| **Prototype** | Lamp Row, the tutorial job: walk, climb, read lines with the lamp, ribbons, breakers, salvage, the temple stores, click-and-hold and live repairs, dawn, the Relight, and shop signs as the first crack in the faith | A new player relights Lamp Row within two nights, without help |
| **MVP** | Act 1 (the Hollow, Lamp Row, the shrine circuit): leveling, capacity choices, Drafts | Act 1 plays start to finish |
| **Chapter One** | Act 2 (receiving the serpent) and the return to Lamp Row, then the Yards, the Spires, the Underworks, the Hum, the core, illuminate | Chapter One is complete ([story](docs/02-story.md)) |
| **Future** | The other five gods, the Cherub, the seventh day | The full game in the [Lore Bible](Rest%20%E2%80%94%20Lore%20Bible.md) |

---

**Long GDD:** [Overview](docs/01-overview.md) · [Story](docs/02-story.md) · [Characters](docs/03-characters.md) · [World](docs/04-world.md) · [Gameplay](docs/05-gameplay.md) · [Progression](docs/06-progression.md) · [Threats](docs/07-threats.md) · [Art and Audio](docs/08-art-audio.md) · [UI and UX](docs/09-ui-ux.md) · [Scope and Roadmap](docs/10-scope-roadmap.md) · [AI Architecture](docs/11-ai-architecture.md) · [Technical Strategy](docs/12-technical-strategy.md) · [Open Questions](docs/open-questions.md)

*Decided* means settled in the Lore Bible or by the creative director. *Draft* means proposed and awaiting sign-off.
