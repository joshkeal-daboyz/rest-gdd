# 9. UI and UX

[← Back to contents](../README.md)

All entries in this section are Draft.

## Principles

- **Minimal HUD.** The world carries the information: the current Enoch's lamp reveals, the prayer ribbons, the state of lamps, the serpent's light. On-screen UI appears only when needed.
- **A character is the interface.** In Act 1, Enoch's mentor and the temple's job postings give tutorials and objectives. From Act 2, the serpent takes over: tutorials, hints, and objectives come from it, and its glow doubles as a status indicator.
- **Diegetic where possible.** The map is Enoch's hand-drawn chart, and the journal is his own notebook.

## Onboarding: the first night

Old Solder, Enoch's mentor, stands at the offering stall at the head of Lamp Row. He teaches each step **the first time the player needs it**, never all at once, and says nothing about steps the player has already worked out. The beats are set here; their lines are written by the creative director and the Writer and pass gate G3.

| # | Moment | What it teaches |
| --- | --- | --- |
| 1 | The night opens at the feed | Raise the lamp and follow the current until it goes quiet |
| 2 | The player reaches the first dead lamp | The pulses stop here, so this is a fault: tie a ribbon |
| 3 | The first repair attempt without the part | *Needs: bulb* shows, and Solder points to salvage nearby |
| 4 | The player reaches a live fault | The prompt warns *Live line*, and Solder says to cut the power first |
| 5 | The first breaker thrown off | The street goes dark and the ribbons glow, so marking first pays off |
| 6 | The satchel is full, or a part is missing | The offering stall: offer spares for favor, draw what's needed |
| 7 | The first dawn, if it comes | The repairs held and the ribbons stayed; come back ready |

Whether this works is checked by a **cold playtest** at gate G5 (see [AI Architecture](11-ai-architecture.md#creative-control-and-review-gates)).

## HUD

| Element | When shown |
| --- | --- |
| Interaction prompt | Near something Enoch can repair, salvage, mark, or throw (a breaker or switch) |
| Satchel quick select | When choosing a part for a repair |
| Favor | Beside the satchel, and at the temple stores |
| Offering screen | At the temple stores in the Hollow: the satchel on one side, the stores on the other, with the favor each offering earns and each part costs |
| Grid capacity meter | When near a switch or when making power choices |
| Context gained | Briefly, when Enoch gains context, with a short line of what he learned |
| Level up | When the context bar fills; opens the skill choice |
| Subtitles | Always available, on by default |
| Pause screen | When the game pauses (Esc, a hidden tab, or a window that loses focus); it dims the street, and the night clock stops |

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
- The serpent can be asked for a hint about where to find a missing part (from Act 2, in Chapter One).

## Reading the lines

- Holding the lamp up shows current as pulses in cables within about 5 meters. Nothing is overlaid on screen; the information is in the world.
- Prayer ribbons mark found faults. They stay visible in the dark and across nights, and they come off when the fault is repaired.

## Accessibility

- Subtitles, with speaker names and sizes.
- Light states must never depend on color alone. Use flicker patterns, sound, and icons as well, for players with color vision differences.
- Options to reduce flicker and flashing effects, which matters in a game about failing lights.
- An option to switch click-and-hold repairs to a single click (toggle) for players who can't hold a button, and to widen the timing check's window on live repairs.
- Current pulses and sparks are always paired with sound (hum and crackle), so reading the lines never depends on sight alone.
- Remappable controls.
