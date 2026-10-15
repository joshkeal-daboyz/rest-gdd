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

Every step of the loop gives Enoch **context**, which levels him up and improves his skills. Once he has the serpent, he can also draw context from the old world's technology, often from machines his repairs just brought back to life (see [Progression](06-progression.md)).

## The power grid (Draft)

The city's grid is a single connected system the player can read and reason about.

- **Nodes:** the core, substations, junctions, transformers, and endpoints (lamps, beacons, shrines, machinery).
- **Lines:** cables between nodes. Lines can be dead, live, damaged, or overloaded.
- **Flow:** power flows from the core outward. A fault anywhere upstream darkens everything downstream, so tracing a fault means following the dark back toward the light.
- **Capacity:** the source is failing, so total power is limited. This limit is the central constraint of the chapter.

### Capacity and restraint

There is never enough power to light everything. As Enoch restores districts, he must choose which circuits stay on.

- Powering more endpoints than the grid can carry causes **brownouts**: lights flicker, repairs fail, and darkened streets fall back to the abominations.
- Some endpoints matter to the tribe (shrines, homes), some to traversal (lifts, doors, bridges), and some to discovery (old machines that only the serpent can read, and only once they have power).
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
| Wire | Repairing chewed cables and rerouting junctions | Walls, conduits, wrecked vehicles |
| Fuses | Replacing blown fuses in junctions | Old electrical boxes, shops |
| Insulators | Repairing lines on poles and towers | Poles, the Yards |
| Bulbs and lenses | Relighting lamps and beacons | Storefronts, streetlights, the Spires |
| Panels | Repairing solar arrays | The Yards, rooftops |
| Components | Circuit boards and relays for complex repairs | Machines, the Underworks |

- **Washing parts.** Salvaged parts are often corroded. Enoch washes them in water before use, a nod to the raccoon's name, *Procyon lotor*, "the washer." Clean parts last longer and fail less. This builds a habit the full game's final image depends on.
- **Hands, not inventory screens.** Enoch carries a satchel with limited space, so the player chooses what to bring for each repair.
- **Trade.** Scavengers in the Hollow trade parts and rumors.

## Repairs: click and hold

Every repair uses one simple interaction. *(Decided.)*

1. **Find the fault** and stand at it. A prompt appears.
2. **Check the part.** If Enoch's satchel has the required part, the prompt reads *Hold to repair*. If not, it reads *Needs: fuse* (or whatever is missing), and the repair can't start.
3. **Click and hold.** Enoch plays a working animation, and a ring fills around the fault over a few seconds.
4. **Let go early** and the repair cancels; the part is not used up.
5. **Finish** and the part is consumed, the fault clears, and the grid updates.

The puzzle is in finding faults and planning salvage, not in the repair itself.

### Fault types

Fault types differ by the part they need, how long the hold takes, and where they are. Each district introduces new ones.

| Fault | Required part | Hold (Draft) | Introduced in |
| --- | --- | --- | --- |
| Dead lamp | Bulb | 2 s | Lamp Row (prototype) |
| Blown fuse | Fuse | 3 s | Lamp Row (prototype) |
| Chewed cable | Wire (and a climb to reach it) | 4 s | Lamp Row (prototype) |
| Dead junction (reroute) | Wire × 2 | 5 s | The shrine circuit (MVP) |
| Cracked insulator | Insulator | 4 s | The Yards |
| Damaged panel | Panel | 5 s | The Yards |
| Failed relay | Component | 6 s | The Spires, the Underworks |

Later phases can add variety without changing the interaction: repairs that need two parts, repairs that need the power cut first, or repairs on a live line that only steady hands allows.

Design goals for repairs:

- **Readable.** The player should understand why something is broken by looking at it, and the prompt always says what's needed.
- **Short.** Every hold is a few seconds.
- **Felt.** Tactile sound while the ring fills, and a clear spark and hum when the fault clears.
- **Time matters.** Each job must be finished before dawn (see [Threats and Hazards](07-threats.md#win-and-loss-draft)), so a wasted trip for a missing part is the real cost.

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

## Controls (Draft)

Rest runs in the browser, so keyboard and mouse come first. Gamepad support is planned after the MVP.

| Keyboard and mouse | Gamepad (after the MVP) | Action |
| --- | --- | --- |
| W A S D | Left stick | Move |
| Mouse | Right stick | Camera |
| Space | A / Cross | Jump, climb |
| E | X / Square | Interact, repair |
| Q | Y / Triangle | Test line (Act 1); serpent: sense current, ask (from Act 2) |
| Ctrl | B / Circle | Crouch, squeeze |
| F | LB / L1 | Lantern on and off |
| R | RB / R1 | Ability (illuminate, after the core) |
| 1–4 | D-pad | Satchel quick select |
| Tab | View / Touchpad | Grid map |
