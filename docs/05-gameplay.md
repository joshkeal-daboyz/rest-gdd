# 5. Gameplay

[← Back to contents](../README.md)

Chapter One is about repair. Enoch's goal is to make repairs to the city's power grid and lights. The systems below are drafts unless they restate the Lore Bible.

## Core loop (Draft)

```
Read the dimming → Trace the fault → Salvage parts → Repair → Restore power → The city changes
        ↑                                                                              │
        └──────────────── New district opens, new fault appears ←──────────────────────┘
```

1. **Read the dimming.** The priests, the serpent, and the state of the lights point Enoch to a failing section of the grid.
2. **Trace the fault.** He follows dead lines through the district to find what is broken.
3. **Salvage parts.** He scavenges the ruins for the components the repair needs.
4. **Repair.** He fixes the fault through hands-on repair interactions.
5. **Restore power.** He brings the section back online and decides how much to draw from the grid.
6. **The city changes.** Lights come on, the tribe moves into the lit ground, the priests respond, and the next problem appears.

Along the way, Enoch finds **context fragments** that level up the serpent (see [Progression](06-progression.md)).

## The power grid (Draft)

The city's grid is a single connected system the player can read and reason about.

- **Nodes:** the core, substations, junctions, transformers, and endpoints (lamps, beacons, shrines, machinery).
- **Lines:** cables between nodes. Lines can be dead, live, damaged, or overloaded.
- **Flow:** power flows from the core outward. A fault anywhere upstream darkens everything downstream, so tracing a fault means following the dark back toward the light.
- **Capacity:** the source is failing, so total power is limited. This limit is the central constraint of the chapter.

### Capacity and restraint

There is never enough power to light everything. As Enoch restores districts, he must choose which circuits stay on.

- Powering more endpoints than the grid can carry causes **brownouts**: lights flicker, repairs fail, and live lines draw abominations.
- Some endpoints matter to the tribe (shrines, homes), some to traversal (lifts, doors, bridges), and some to discovery (old machines that hold fragments).
- The priests have opinions about which lights are holy, and they are not always the useful ones.

This is the chapter's quiet version of the game's theme. The original sin is a lack of self-control, and the grid makes the player feel the cost of wanting everything.

## Fault tracing (Draft)

- **Following the lines.** Cables are visible in the world: overhead, along walls, and under grates. Enoch can follow them on foot.
- **Reading the glow.** Live lines hum and glow faintly; dead ones are dark and silent. Damaged lines spark.
- **Testing by hand (Act 1).** Before the serpent, Enoch tests lines the way the gaze's mechanics always have: a salvaged test lamp touched to a line, sparks, and educated guesses. It works, but it is slow and sometimes earns him a shock.
- **The serpent's sense (from Act 2).** The serpent can feel current. Holding it near a line tells Enoch whether it is live, dead, or damaged, faster and more safely than his test lamp. This is the serpent's first role as a teaching tool, and it makes the gift feel like a real upgrade.
- **The grid map.** A hand-drawn map that fills in as Enoch traces lines. It shows known nodes, their state, and the path of power (see [UI and UX](09-ui-ux.md)).

## Salvage (Draft)

The raccoons' offering to Light is salvage from the ruins. Enoch scavenges for the parts he needs.

| Part | Use | Where it's found |
| --- | --- | --- |
| Wire | Splicing and replacing damaged lines | Walls, conduits, wrecked vehicles |
| Fuses | Replacing blown fuses in junctions | Old electrical boxes, shops |
| Insulators | Repairing lines on poles and towers | Poles, the Yards |
| Bulbs and lenses | Relighting lamps and beacons | Storefronts, streetlights, the Spires |
| Panels | Repairing solar arrays | The Yards, rooftops |
| Components | Circuit boards and relays for complex repairs | Machines, the Underworks |

- **Washing parts.** Salvaged parts are often corroded. Enoch washes them in water before use, a nod to the raccoon's name, *Procyon lotor*, "the washer." Clean parts last longer and fail less. This builds a habit the full game's final image depends on.
- **Hands, not inventory screens.** Enoch carries a satchel with limited space, so the player chooses what to bring for each repair.
- **Trade.** Scavengers in the Hollow trade parts and rumors.

## Repair interactions (Draft)

Repairs are short, tactile interactions focused on Enoch's hands. Each district introduces one new type.

| Repair | How it plays | Introduced in |
| --- | --- | --- |
| Replace | Remove a dead bulb, fuse, or component and seat a new one | The Hollow |
| Splice | Strip, twist, and bind damaged wire | Lamp Row |
| Reroute | Connect inputs to outputs on a junction board within its capacity | Lamp Row |
| Switch | Reset breakers and switches in the right order to avoid surges | The Yards |
| Align | Turn panels, mirrors, or lenses to direct light or power | The Yards, the Spires |
| Restart | A multi-step sequence to bring a large machine back online | The Spires, the Core |

Design goals for repairs:

- **Readable.** The player should understand why something is broken by looking at it.
- **Short.** Most repairs take under a minute. The puzzle is in finding the fault, not in the repair itself.
- **Physical.** Close camera on Enoch's hands, with tactile sound and feedback.
- **Failure is safe but felt.** A wrong connection sparks, shocks, or causes a brief brownout. No game over.

## Traversal (Draft)

- **Climbing.** Raccoons are agile climbers. Enoch climbs poles, drainpipes, fences, and building faces.
- **Squeezing.** Small enough to slip through vents, gaps, and collapsed passages.
- **Powered traversal.** Restored power opens new paths: lifts, gates, lit bridges, and doors. Restoring the grid is also how the city opens up.
- **Darkness as a barrier.** Unlit areas are dangerous and hard to navigate, which gives the player a reason to bring the light with them.

## The serpent as teacher

In Act 1, before Enoch earns the serpent, his mentor teaches the basics: movement, repairs, testing lines, and salvage. Once the serpent arrives, it takes over as the teacher, explaining the world and the new mechanics it unlocks. In both cases, tutorials are delivered as a character's guidance, not as on-screen pop-ups.

- **Exploration barks:** lines trigger when the player leaves the intended path. The more anxious the serpent gets, the closer the player is to something it does not want found. Its fear becomes a compass toward the truth.
- **Withholding:** the serpent sometimes refuses to explain what Enoch is looking at, changes the subject, or gives an answer that the environment later contradicts.

## Avoidance and danger

Enoch is not a fighter. See [Threats and Hazards](07-threats.md) for abominations and environmental danger.

## Controls (Draft, controller layout)

| Input | Action |
| --- | --- |
| Left stick | Move |
| Right stick | Camera |
| A / Cross | Jump, climb |
| X / Square | Interact, repair |
| Y / Triangle | Test line (Act 1); serpent: sense current, ask (from Act 2) |
| B / Circle | Crouch, squeeze |
| LB / L1 | Lantern on and off |
| RB / R1 | Ability (illuminate, after the core) |
| D-pad | Satchel quick select |
| View / Touchpad | Grid map |
