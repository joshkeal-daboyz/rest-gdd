# 10. Scope and Roadmap

[← Back to contents](../README.md)

Rest is built in phases. The core loop is proven first, at its most basic, and each phase adds only what the one before has earned. Big ideas stay in the document, in later phases, but are not built yet.

## Phase 1: Prototype — Lamp Row

**The weekend test:** two developers with the agent crew can build this in a weekend.

### In scope

- One street: Lamp Row ([World](04-world.md)), with about 20 lamps.
- Enoch walks, runs, and climbs poles, with a third-person camera.
- A grid of about 10 nodes: a feed from the Hollow, junctions, and lamp circuits.
- The **test lamp**, which reads a line as live, dead, or damaged.
- **Salvage:** three part types (fuses, wire, bulbs) from about six salvage spots, with a small satchel.
- **Three faults**, one for each repair type: a blown fuse (**replace**), a chewed cable (**splice**), and a dead circuit to bypass (**reroute**).
- **The Relight:** the wow moment when the street comes back to light.
- Placeholder lines for Enoch and a job description from the temple.

### Out of scope for the prototype

The serpent, leveling, abominations, capacity choices, other districts, washing parts, the journal, and the grid map.

### Acceptance criteria

- [ ] A new player relights Lamp Row in 10–15 minutes without outside help.
- [ ] Every fault can be found by following cables and using the test lamp.
- [ ] A failed repair is safe and clearly readable.
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
| The grid is hard to read | Clear cable visuals and the test lamp in the prototype; the grid map in the MVP |
| The story's reveals arrive too fast or too slow | Pace reveals through machines read by the serpent; curious players find more, but nothing is required |
| Ending Chapter One at the core gives away too much | Keep the reveal to "Light is a machine"; hold back humanity's fate and the Cherub |

Technical risks are in [Technical Strategy](12-technical-strategy.md).
