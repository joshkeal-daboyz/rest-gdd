# 10. Scope and Roadmap

[← Back to contents](../README.md)

Rest is built in phases. The core loop is proven first, at its most basic, and each phase adds only what the one before has earned. Big ideas stay in the document, in later phases, but are not built yet.

## Phase 1: Prototype — Lamp Row

Lamp Row is the tutorial job: short enough that a walk from the head of the street to its far end and back takes about a minute.

**The weekend test:** the course's benchmark is two developers in a weekend. Rest has one developer, the creative director, with the agent crew, so the prototype's core (below) is the weekend build. The full scope may take a week or two, the course's limit. Agents run one at a time under usage limits, so the [cut list](#cut-list) says what goes first if the build falls behind.

### In scope

- One street: Lamp Row ([World](04-world.md)), with about 20 lamps.
- Enoch walks, runs, and climbs poles, with a third-person camera.
- A grid of about 10 nodes: a feed from the Hollow, two breakers (the main one beside the offering stall, one on a side branch), fuse boxes, and lamp circuits. No switches.
- **The lamp:** held up, it shows current as pulses in cables within about 5 meters. Damaged cables spark and live ones hum without it.
- **Prayer ribbons** to mark found faults; they stay across nights.
- **The part economy:** three part types (fuses, wire, bulbs). Six salvage spots on Lamp Row, each holding one part of a fixed type that restocks each night (3 bulb, 1 fuse, 1 wire, 1 random), and a temple offering stall at the head of the street, standing in for the Hollow's temple stores, that trades any part for favor and never runs out. Enoch starts with no favor, and finishing Lamp Row pays him 6 favor. A 4-part satchel; parts can be dropped. No night limit. All values are temporary ([Gameplay](05-gameplay.md#salvage-draft)).
- **Click-and-hold repairs** that can't start without the required part, across eight faults of three types: five dead lamps (bulb), two blown fuses (fuse), one hidden until a lamp beyond it is fixed, and a damaged cable up a pole (wire).
- **Live repairs:** a timing check on the ring; a miss is a shock, and two shocks in a night kill Enoch and undo that night's repairs.
- **The Relight:** the wow moment when the street comes back to light. This is the win.
- **Losing a night:** a night lasts 15 minutes at most, shown by the sky. If dawn breaks first, the night is lost, but completed repairs stay. If Enoch dies of shock, the night is lost and that night's repairs are undone.
- **Assets:** canned packs for the city and AI-generated models for Enoch and anything missing. No hand modeling.
- **The crack in the faith:** a few shop signs and advertisements on Lamp Row's storefronts showing people using light for ordinary things. They are decals or textures on pieces the Level Builder already places, and no one comments on them ([World](04-world.md#lamp-row)).
- Placeholder lines for Enoch and a job description from the temple. No story exposition ([Overview](01-overview.md#what-the-player-knows-decided)).

### Cut list

If the build falls behind, features are cut in this order. Each cut leaves a working game, and none touches the core loop. *(Decided.)*

| Cut order | Feature | What replaces it |
| --- | --- | --- |
| 1 | Pole climbing | The damaged cable moves to a ground-level junction box |
| 2 | Live repairs, the timing check, shocks, and death | Repairs need the breaker off; dawn is the only loss |
| 3 | The temple stores and favor | Salvage only. Spots restock each night, so there are still no dead ends |
| 4 | The hidden fuse box | All 8 faults are visible from the start |
| 5 | The side-branch breaker | One main breaker |

**Never cut (the core):** reading lines with the lamp, ribbons, the breaker, click-and-hold repairs, salvage, the satchel, dawn, and the Relight.

A cut also cuts its acceptance criteria and the onboarding beat that teaches it (see [UI and UX](09-ui-ux.md#onboarding-the-first-night)).

### Out of scope for the prototype

The serpent, leveling, abominations, capacity choices, other districts, the journal, and the grid map.

### Acceptance criteria

- [ ] A new player relights Lamp Row within two nights without outside help, and understands from the mentor that more than one night is expected. Measured by the cold playtest at gate G5 ([AI Architecture](11-ai-architecture.md#creative-control-and-review-gates)).
- [ ] The player always knows which part a fault needs.
- [ ] A player who loses to dawn understands why, sees that their repairs held, and finishes the job on the next night.
- [ ] A player can never be left without a way to finish: the temple stores always hold every part, and salvage restocks each night.
- [ ] Every fault can be found by following cables with the lamp raised, and players recognize cables as part of the game within the first minute.
- [ ] A player who dies from a live repair understands why the night's repairs were lost and that the breaker was the safe choice.
- [ ] Letting go of a repair early is clearly readable and costs only time.
- [ ] The Relight passes gate G4.
- [ ] 60 fps on a mid-range laptop; first load under 30 MB.
- [ ] The build is playable at a GitHub Pages link.

## Phase 2: MVP — Act 1

- **Districts:** the Hollow (tutorial), Lamp Row, and the shrine circuit.
- **Story:** Act 1 (the repairman) ([Story](02-story.md)).
- **Progression:** context from experience; levels; Hands, Eyes, and Feet ([Progression](06-progression.md)).
- **The journal:** faith-filtered and conduit entries side by side.
- **Switches:** rerouting power around a dead junction in the shrine circuit. No capacity limit yet.
- **Abominations:** the Drafts, which avoid light.

**Done when:** Act 1 is playable start to finish.

## Phase 3: Chapter One — Light

- **Act 2 (the chosen)** and the return to Lamp Row ([Story](02-story.md)). The serpent arrives: the gift, sense current, reading powered machines as a conduit, and escalating fear barks. A playtester can explain why Enoch was chosen.
- The Yards, the Spires, the Underworks, and the core ([World](04-world.md)).
- **Grid capacity**, from the Yards: choosing which circuits get power once a job's faults are fixed, and repairing power sources to raise capacity ([Gameplay](05-gameplay.md#capacity-and-restraint)).
- The Gnawers, and the Hum boss battle ([Threats](07-threats.md)).
- Serpent abilities: steady hands, carry charge, illuminate.
- The first temptation at the core, and the epilogue.

**Done when:** Chapter One is complete as written in [Story](02-story.md).

## Phase 4: Future — the full game

- The other five gods and their realms, in any order.
- The Cherub and the dog tribe.
- The seventh day, the Convergence, and both endings.
- Other playable tribes as expansions.

See the [Lore Bible](../Rest%20%E2%80%94%20Lore%20Bible.md).

## Design risks

| Risk | Mitigation |
| --- | --- |
| The core loop isn't fun on its own | The prototype has no progression or story systems to lean on; if relighting one street isn't satisfying, fix that before anything else |
| Repair gameplay becomes repetitive | A new repair type per district; short repairs; finding the fault is the main puzzle |
| The grid is hard to read | Every cable is a grid cable, the tribe marks breakers, the lamp shows current, and ribbons mark faults in the prototype; the grid map in the MVP |
| The story's reveals arrive too fast or too slow | Pace reveals through machines read by the serpent; curious players find more, but nothing is required |
| Ending Chapter One at the core gives away too much | Keep the reveal to "Light is a machine"; hold back humanity's fate and the Cherub |

Technical risks are in [Technical Strategy](12-technical-strategy.md).
