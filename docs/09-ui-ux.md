# 9. UI and UX

[← Back to contents](../README.md)

All entries in this section are Draft.

## Principles

- **Minimal HUD.** The world carries the information: the current Enoch's lamp reveals, the neon ribbons, the state of lamps, the serpent's light. On-screen UI appears only when needed.
- **A character is the interface.** In Act 1, Enoch's mentor and the temple's job postings give tutorials and objectives. From Act 2, the serpent takes over: tutorials, hints, and objectives come from it, and its glow doubles as a status indicator.
- **Diegetic where possible.** The map is Enoch's hand-drawn chart, and the journal is his own notebook.

## HUD

| Element | When shown |
| --- | --- |
| Interaction prompt | Near something Enoch can repair, salvage, mark, or throw (a breaker or switch) |
| Satchel quick select | When choosing a part for a repair |
| Scrip | Beside the satchel, and at the vendor |
| Vendor screen | At the vendor in the Hollow: the satchel on one side, the vendor's stock on the other, with buy and sell prices |
| Grid capacity meter | When near a switch or when making power choices |
| Context gained | Briefly, when Enoch gains context, with a short line of what he learned |
| Level up | When the context bar fills; opens the skill choice |
| Subtitles | Always available, on by default |

There is no health bar. Enoch's condition is shown through his animation and the screen's edges: after one shock, the edges dim and his hands shake for the rest of the night, which tells the player a second shock will kill him.

## The grid map

- Enoch's hand-drawn map of the city, which he fills in as he traces lines.
- Shows known nodes, their state (dead, live, damaged, overloaded), and which districts are powered.
- Doubles as the interface for the capacity choices: which circuits to keep on.
- Districts the player hasn't visited are blank or sketched from rumor.

## The journal

- **Context:** what Enoch has learned, in his own words. Entries from his own experience are written through his faith. Entries read from technology through the serpent are written plainly, and when both exist for the same place, they appear side by side.
- **Scripture:** the priests' teachings as Enoch remembers them. Context entries can be placed beside the scripture they contradict (Draft).
- **Skills:** Enoch's level, his context toward the next level, and his ranks in Hands, Eyes, and Feet.
- **Tasks:** current repair jobs, written as a work list.
- **Relics:** the serpent's shed skins.

## Repair interface

- Click and hold: a ring fills around the fault while Enoch works. The camera stays in its normal third-person view.
- The prompt names the part needed (*Needs: fuse*) when it isn't in the satchel.
- At a live fault, the prompt warns: *Live line. Cut the power, or hold to risk it.*
- During a live repair, a mark appears on the ring; clicking as the ring passes it completes the repair. A miss is a shock.
- The serpent can be asked for a hint about where to find a missing part (from the MVP).

## Reading the lines

- Holding the lamp up shows current as pulses in cables within about 5 meters. Nothing is overlaid on screen; the information is in the world.
- Neon ribbons mark found faults. They stay visible in the dark and across nights, and they come off when the fault is repaired.

## Accessibility

- Subtitles, with speaker names and sizes.
- Light states must never depend on color alone. Use flicker patterns, sound, and icons as well, for players with color vision differences.
- Options to reduce flicker and flashing effects, which matters in a game about failing lights.
- An option to switch click-and-hold repairs to a single click (toggle) for players who can't hold a button, and to widen the timing check's window on live repairs.
- Current pulses and sparks are always paired with sound (hum and crackle), so reading the lines never depends on sight alone.
- Remappable controls.
