# 10. Scope and Roadmap

[← Back to contents](../README.md)

Rest is built in phases. The core loop is proven first, at its most basic, and each phase adds only what the one before has earned. Big ideas stay in the document, in later phases, but are not built yet.

## Phase 1: Prototype — Lamp Row

Lamp Row is the tutorial job: short enough that a walk from the head of the street to its far end and back takes about a minute.

**The weekend test:** two developers with the agent crew can build this in a weekend.

### In scope

- One street: Lamp Row ([World](04-world.md)), with about 20 lamps.
- Enoch walks, runs, and climbs poles, with a third-person camera.
- A grid of about 10 nodes: a feed from the Hollow, two breakers (the main one beside the vendor, one on a side branch), fuse boxes, and lamp circuits. No switches.
- **The lamp:** held up, it shows current as pulses in cables within about 5 meters. Damaged cables spark and live ones hum without it.
- **Neon ribbons** to mark found faults; they stay across nights.
- **The part economy:** three part types (fuses, wire, bulbs). About six salvage spots on Lamp Row that restock each night, and a vendor stall at the head of the street, standing in for the Hollow, that buys and sells any part for scrip and never runs out. Enoch starts with no scrip, and finishing Lamp Row pays him scrip. A small satchel; parts can be dropped. No night limit.
- **Click-and-hold repairs** that can't start without the required part, across three fault types: dead lamps (bulb), a blown fuse (fuse), and a damaged cable up a pole (wire).
- **Live repairs:** a timing check on the ring; a miss is a shock, and two shocks in a night kill Enoch and undo that night's repairs.
- **The Relight:** the wow moment when the street comes back to light. This is the win.
- **Losing a night:** a night lasts 15 minutes at most, shown by the sky. If dawn breaks first, the night is lost, but completed repairs stay. If Enoch dies of shock, the night is lost and that night's repairs are undone.
- **Assets:** canned packs for the city and AI-generated models for Enoch and anything missing. No hand modeling.
- Placeholder lines for Enoch and a job description from the temple.

### Out of scope for the prototype

The serpent, leveling, abominations, capacity choices, other districts, washing parts, the journal, and the grid map.

### Acceptance criteria

- [ ] A new player relights Lamp Row within two nights without outside help, and understands from the mentor that more than one night is expected.
- [ ] The player always knows which part a fault needs.
- [ ] A player who loses to dawn understands why, sees that their repairs held, and finishes the job on the next night.
- [ ] A player can never be left without a way to finish: the vendor always stocks every part, and salvage restocks each night.
- [ ] Every fault can be found by following cables with the lamp raised, and players recognize cables as part of the game within the first minute.
- [ ] A player who dies from a live repair understands why the night's repairs were lost and that the breaker was the safe choice.
- [ ] Letting go of a repair early is clearly readable and costs only time.
- [ ] The Relight passes gate G4.
- [ ] 60 fps on a mid-range laptop; first load under 30 MB.
- [ ] The build is playable at a GitHub Pages link.

## Phase 2: MVP — Act 1 and the serpent

- **Districts:** the Hollow (tutorial), Lamp Row, and the shrine circuit.
- **Story:** Act 1 (the repairman) and Act 2 (the chosen), ending with the return to Lamp Row ([Story](02-story.md)).
- **Progression:** context from experience; levels; Hands, Eyes, and Feet ([Progression](06-progression.md)).
- **The serpent:** the gift, sense current, reading powered machines as a conduit, and escalating fear barks.
- **The journal:** faith-filtered and conduit entries side by side.
- **Grid capacity:** choosing which circuits stay on.
- **Abominations:** the Drafts, which avoid light.
- **Washing parts.**

**Done when:** Act 1 and Act 2 are playable start to finish, and a playtester can explain why Enoch was chosen.

## Phase 3: Chapter One — Light

- The Yards, the Spires, the Underworks, and the core ([World](04-world.md)).
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
