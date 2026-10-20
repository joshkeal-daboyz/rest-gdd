# 5. Gameplay

[← Back to contents](../README.md)

Chapter One is about repair. Enoch's goal is to make repairs to the city's power grid and lights. The systems below are drafts unless they restate the Lore Bible.

## Core loop (Draft)

```
Read the dimming → Prep in town → Read the lines → Breaker off → Repair → Breaker on → The city changes
        ↑                                    ↑                                    │          │
        │                                    └──────── a new fault shows ─────────┘          │
        └──────────────────── New district opens, new fault appears ←────────────────────────┘
```

1. **Read the dimming.** The priests, the serpent, and the state of the lights point Enoch to a failing section of the grid. The job names the street, not the faults.
2. **Prep in town.** He offers spare parts to the temple stores in the Hollow, draws what he expects to need with his favor, then packs his satchel.
3. **Read the lines.** With the power on, he raises his lamp to see current in the cables, finds where it stops, and ties a prayer ribbon on each fault. He salvages parts along the way.
4. **Breaker off.** He throws the breaker for the section so he can work safely.
5. **Repair.** He fixes each marked fault, with the right part, through a click-and-hold repair.
6. **Breaker on.** Power pushes further. Fixing one fault can uncover another beyond it, so the loop returns to reading the lines until the section is lit.
7. **The city changes.** Lights come on, the tribe moves into the lit ground, the priests respond, and the next problem appears.

**Jobs take more than one night.** A job is not meant to be finished on the first visit. The first night is usually for reading the lines and learning what the job needs; later nights are for coming back prepared. Repairs and ribbons stay between nights. Enoch's mentor says this when he gives Enoch his first job: *"No one relights a street in one night. Look first. Come back ready."*

Every step of the loop gives Enoch **context**, which levels him up and improves his skills. Once he has the serpent, he can also draw context from the old world's technology, often from machines his repairs just brought back to life (see [Progression](06-progression.md)).

## The power grid (Draft)

The city's grid is a single connected system the player can read and reason about.

- **Nodes:** the core, substations, transformers, fuse boxes, breakers, switches, and endpoints (lamps, beacons, shrines, machinery).
- **Lines:** cables between nodes. Lines can be dead, live, damaged, or overloaded.
- **Flow:** power flows from the core outward. A fault anywhere upstream darkens everything downstream, so tracing a fault means following the current until it stops.
- **Every cable is a grid cable.** If the player can see a cable, it is part of the grid. Decorative wires in the ruins look clearly different: thin, rusted, and ending in frayed stubs that connect to nothing.
- **Capacity:** the source is failing, so total power is limited. This limit is the central constraint of the chapter.

### Breakers and switches

Breakers and switches are found throughout the city. The tribe marks every one with paint and prayer ribbons, so they are easy to spot from down the street.

| Control | What it does | First appears |
| --- | --- | --- |
| **Breaker** | Shuts a section off entirely, so faults in it can be repaired safely | Lamp Row (prototype) |
| **Switch** | Sends power down one branch or another | The shrine circuit (MVP) |

Lamp Row has two breakers: the main breaker at the head of the street, beside the temple's offering stall, and one on a side branch. Walking to a breaker and back is a real cost in time, so where breakers sit is part of each district's puzzle. Switches arrive with capacity: they are how the player chooses which branch gets power.

### Capacity and restraint

There is never enough power to light everything. As Enoch restores districts, he must use switches and breakers to choose which circuits stay on.

- Powering more endpoints than the grid can carry causes **brownouts**: lights flicker, repairs fail, and darkened streets fall back to the abominations.
- Some endpoints matter to the tribe (shrines, homes), some to traversal (lifts, doors, bridges), and some to discovery (old machines that only the serpent can read, and only once they have power).
- The priests have opinions about which lights are holy, and they are not always the useful ones.

This is the chapter's quiet version of the game's theme. The original sin is a lack of self-control, and the grid makes the player feel the cost of wanting everything.

## Fault tracing (Draft)

Enoch is attuned to Light's power (see [Characters](03-characters.md)), and his lamp lets him see it.

- **The street stays dark.** Live cables do not glow on their own. In the dark, every cable looks the same, so the atmosphere is never lost. Only two things give a line away: **damaged cables spark** on their own, and **live cables hum**, louder as Enoch gets closer.
- **Raising the lamp (Act 1).** While the player holds the lamp up, any cable within about 5 meters shows its current: slow **pulses of light** flowing *away* from the source, fading at the edge of the lamp's reach. Dead cables show nothing. Enoch walks slower with the lamp raised, so it is for reading lines, not for walking around.
- **Fault signatures.** The player finds a fault by seeing where the current stops:

  | Fault | What the lamp shows | Part |
  | --- | --- | --- |
  | Blown fuse | Pulses run into a fuse box, and none come out | Fuse |
  | Damaged cable | Pulses run up to a sparking break and stop | Wire |
  | Dead lamp | Pulses reach the lamp post, but the lamp stays dark | Bulb |

  Each fault always needs the same part, so a correct reading tells the player exactly what to carry.
- **Faults hide faults.** Everything past a fault is dead, so a second fault further down can't be seen until the first is fixed and the power is back on. Each round of repairs reveals the next layer.
- **Prayer ribbons.** Prayer ribbon is the gaze's flagging tape: a bright, glowing tape the tribe ties wherever the grid needs marking, from holy lines to breakers. Enoch carries a spool of it. Tying a length to a fault marks it, and the ribbon glows in the dark, so the fault stays visible after the power is cut and across nights. A ribbon comes off when its fault is repaired, and it can be untied if the player marked the wrong spot. The spool never runs out. One color is enough.
- **Repaired parts look new.** A fresh bulb, clean wire, or a bright new fuse shows that a repair held, even while the line is still dead.
- **The serpent's sense (from Act 2).** The serpent feels current at a distance, through walls and the ground, without raising the lamp, and it can tell how much is flowing, which matters once capacity arrives. It makes the lamp feel crude by comparison.
- **The grid map.** A hand-drawn map that fills in as Enoch traces lines (MVP). It shows known nodes, their state, and the path of power (see [UI and UX](09-ui-ux.md)).

### Making the grid readable

The cables must read as the game, not as background:

- **Every cable is a grid cable** (see above).
- **The tribe marks the grid.** Holy lines carry prayer ribbons, and breakers, switches, and fuse boxes are painted with the gaze's symbols.
- **Lines at eye level.** Fuse boxes, breakers, and most cables run along walls and at street level, where the third-person camera sees them. Overhead runs are kept for cables Enoch has to climb to, and their sparks are visible from the ground.
- **The first 30 seconds teach it.** The first night opens at the Hollow's feed. Enoch raises his lamp, and the line lights up with pulses running off down Lamp Row. His mentor says: *"Follow it until it goes quiet."*

## Salvage (Draft)

The raccoons' offering to Light is salvage from the ruins. Parts come from two places, the town and the city, and parts are the economy that connects them. *(Decided.)*

- **The temple stores (town).** The priests keep the temple's stores in the Hollow, and **Brother Wick** runs them (Draft). Any part can be given as an **offering** and earns **favor**, and favor draws any part from the stores. The stores never run out. In the prototype, the Hollow is a **temple offering stall** at the head of Lamp Row.
- **Favor is faith on the surface and a ledger underneath.** To the tribe, favor is Light's blessing on a devout mechanic. To the player, it works exactly like money, and the priests keep careful accounts. It quietly supports *the cracks show*.
- **Salvage (city).** Ruined storefronts, wrecked vans, and old electrical boxes on the job hold parts. Salvage spots restock each night.
- **Parts as currency.** Any part can be offered, and the favor draws any other part. Favor takes no room in the satchel, so offering banks a part's value. An offering earns less favor than drawing the same part costs, so a part that's already in the satchel is worth more than its favor.
- **Prices (temporary).** Every part costs **2 favor** to draw and earns **1 favor** as an offering. These are placeholders until playtesting.
- **Prep for the future.** Salvage turns up parts the current job doesn't need. The player can sell them, or keep them for a later job. In the MVP and beyond, the city holds parts for districts the player hasn't reached yet, so exploring pays off later.
- **Where favor comes from.** Enoch starts the tutorial (Lamp Row) with no favor, so his first parts come from salvage, and offering spares is how he learns the temple stores. **Every finished job pays favor:** the temple blesses the work. The tutorial's payment is his first stake for the jobs ahead. Between jobs, favor comes from offering salvage. *(Decided.)*
- **Farming is allowed.** Jobs have no night limit, and salvage restocks each night, so a player can spend nights salvaging and offering to build up favor. That is a valid strategy, not an exploit: it trades time for preparation. *(Decided.)*
- **No dead ends.** The temple stores always hold every part, and salvage spots restock each night, so a player who is short can always salvage, offer, and draw what they need.
- **Dropping parts.** Parts can be dropped anywhere to make room in the satchel and picked up again later.

| Part | Use | Where it's salvaged |
| --- | --- | --- |
| Wire | Repairing damaged cables and rerouting junctions | Walls, conduits, wrecked vehicles |
| Fuses | Replacing blown fuses in junctions | Old electrical boxes, shops |
| Insulators | Repairing lines on poles and towers | Poles, the Yards |
| Bulbs and lenses | Relighting lamps and beacons | Storefronts, streetlights, the Spires |
| Panels | Repairing solar arrays | The Yards, rooftops |
| Components | Circuit boards and relays for complex repairs | Machines, the Underworks |

- **Hands, not inventory screens.** Enoch carries a satchel with limited space, so the player chooses what to bring out for each job.
- **Rumors.** Scavengers in the Hollow trade rumors about where good salvage lies (MVP).

## Repairs: click and hold

Every repair uses one simple interaction. *(Decided.)*

1. **Find the fault** and stand at it. A prompt appears.
2. **Check the part.** If Enoch's satchel has the required part, the prompt reads *Hold to repair*. If not, it reads *Needs: fuse* (or whatever is missing), and the repair can't start.
3. **Click and hold.** Enoch plays a working animation, and a ring fills around the fault over a few seconds.
4. **Let go early** and the repair cancels; the part is not used up.
5. **Finish** and the part is consumed, the fault clears, and the ribbon comes off. Nothing lights yet: the change shows when the breaker goes back on.

The puzzle is in finding faults, planning what to carry, and deciding when to cut the power, not in the repair itself.

### Cutting the power

The safe way to repair is with the section's breaker off: read the lines with the power on, throw the breaker, make the repairs, then throw it back on. The prompt at a live fault says so: *Live line. Cut the power, or hold to risk it.*

### Live repairs and shocks

Enoch can skip the breaker and repair a live line. It saves the walk, but it can kill him. *(Decided.)*

- **The timing check.** On a live line, a mark appears on the ring as it fills. The player must click again as the ring passes it. A hit finishes the repair normally.
- **A miss shocks Enoch.** He is thrown back, the repair cancels, and the part is not used up. The screen edges dim and his hands shake for the rest of the night, which shows he is hurt. There is no health bar.
- **Two shocks kill.** A second shock in the same night kills Enoch. The night is lost, and **every repair he made that night is undone** (see [Threats and Hazards](07-threats.md#win-and-loss-draft)). This makes a live repair a high-risk, high-reward choice: it saves the walk to the breaker, but it gambles the whole night's work.
- **High-power lines kill in one.** Lines from substations and the main lines from the core (from the Yards onward) are marked by the tribe as deadly. One shock on them kills. Lamp Row has none.
- **Shocks heal by the next night.**
- **Later relief.** Insulated gloves (a tool) and the serpent's *steady hands* make live repairs safe (see [Progression](06-progression.md)).

### Fault types

Fault types differ by the part they need, how long the hold takes, and where they are. Each district introduces new ones.

| Fault | Required part | Hold (Draft) | Introduced in |
| --- | --- | --- | --- |
| Dead lamp | Bulb | 2 s | Lamp Row (prototype) |
| Blown fuse | Fuse | 3 s | Lamp Row (prototype) |
| Damaged cable | Wire (and sometimes a climb to reach it) | 4 s | Lamp Row (prototype) |
| Dead junction (reroute) | Wire × 2 | 5 s | The shrine circuit (MVP) |
| Cracked insulator | Insulator | 4 s | The Yards |
| Damaged panel | Panel | 5 s | The Yards |
| Failed relay | Component | 6 s | The Spires, the Underworks |

Later phases can add variety without changing the interaction: repairs that need two parts, or faults that can only be reached from a high-power line.

Design goals for repairs:

- **Readable.** The player should understand why something is broken by looking at it, and the prompt always says what's needed.
- **Short.** Every hold is a few seconds.
- **Felt.** Tactile sound while the ring fills, and a clear spark and hum when the fault clears.
- **Time matters.** Each night ends at dawn (see [Threats and Hazards](07-threats.md#win-and-loss-draft)), so a wasted trip, for a missing part or to a breaker and back, is the real cost. A finished repair survives dawn, but not Enoch's death.

## Traversal (Draft)

- **Climbing.** Raccoons are agile climbers. Enoch climbs poles, drainpipes, fences, and building faces.
- **Squeezing.** Small enough to slip through vents, gaps, and collapsed passages.
- **Powered traversal.** Restored power opens new paths: lifts, gates, lit bridges, and doors. Restoring the grid is also how the city opens up.
- **Darkness as a barrier.** Unlit areas are dangerous and hard to navigate, which gives the player a reason to bring the light with them.

## The serpent as teacher

In Act 1, before Enoch earns the serpent, his mentor teaches the basics: movement, reading lines with the lamp, breakers, repairs, and salvage. Once the serpent arrives, it takes over as the teacher, explaining the world and the new mechanics it unlocks. In both cases, tutorials are delivered as a character's guidance, not as on-screen pop-ups.

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
| E | X / Square | Interact, repair, throw a breaker or switch |
| Left click (during a live repair) | X / Square | Timing check |
| Q | Y / Triangle | Tie or untie a prayer ribbon |
| C | Right stick click | Serpent: sense current, ask (from Act 2) |
| Ctrl | B / Circle | Crouch, squeeze |
| F (hold) | LB / L1 (hold) | Raise the lamp to see current |
| R | RB / R1 | Ability (illuminate, after the core) |
| 1–4 | D-pad | Satchel quick select |
| Tab | View / Touchpad | Grid map |
