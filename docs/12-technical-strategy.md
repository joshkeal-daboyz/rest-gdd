# 12. Technical Strategy

[← Back to contents](../README.md)

## Stack

| Layer | Choice | Notes |
| --- | --- | --- |
| Rendering | **Three.js** | Version pinned at project start and never upgraded mid-phase |
| Language | **TypeScript** (strict) | Interfaces in `src/core/` are the agents' shared contract |
| Build and dev server | **Vite** | Fast reloads; static output for hosting |
| Physics and character movement | **Rapier** (`@dimforge/rapier3d-compat`) | Its kinematic character controller handles movement, slopes, and collision |
| Post-processing | **`postprocessing`** (pmndrs) | Selective bloom on emissive lamp materials |
| Models | **glTF / GLB** via `GLTFLoader`, Draco-compressed | One format for every asset |
| Level layout | **Written layout files** (`levels/*.layout.json`) | Three.js has no editor and no one on the team models, so levels are data: which pack piece goes where. A top-down debug view and screenshots let the creative director review layouts without a 3D tool |
| Character pipeline | Hand-drawn concept art → **Tripo** image-to-3D (Meshy as backup) → **Mixamo** auto-rig and animations | No hand modeling: the creative director draws Enoch (front, side, back), photographs the drawings, and Tripo generates the model; Mixamo's humanoid rig adds stock animations (walk, run, climb, a working loop for repairs) |
| Asset processing | **glTF-Transform** (command line) | Agents compress and resize models with scripts, not by hand |
| Audio | Web Audio API, through Three.js `PositionalAudio` | The grid hum is positional, so live lines sound alive near Enoch |
| Testing | **Vitest** (logic), **Playwright** (scripted playthroughs) | Run by the QA Playtester on every pull request |
| Hosting | **GitHub Pages** | The playable build lives at a shareable link |
| Input | Keyboard and mouse | Gamepad support after the MVP |

## Assets

**Find before you generate.** The Asset Scout searches in this order:

1. **Free CC0 packs** (Quaternius, KayKit, Kenney) for buildings, props, poles, and vehicles. *(Decided: free first.)*
2. **Paid packs** (for example Synty's POLYGON City) only if the free packs can't hit the art direction, and only after the prototype.
3. **Freesound** (CC0 or CC-BY) for hums, sparks, and ambience.
4. **Generation** (Tripo, with Meshy as backup) only for what doesn't exist, starting with Enoch himself. Enoch is generated from the creative director's own drawings, photographed front, side, and back, and drawn to match the pack's low-poly style. Every generated asset passes gate G2.

**No hand modeling.** The creative director does not create 3D models, so every asset in the game is either canned or AI-generated. If a generated model doesn't work, it is regenerated, not fixed by hand.

Every asset's source and license is recorded in `assets/manifest.json`.

## Constraints

1. **Three.js is a rendering library, not an engine.** It provides no editor, physics, character controller, animation tools, or scene management. Each of those comes from a library named above, or from a small module owned by one agent. Agents must not introduce new libraries without a ticket approved at gate G1.
2. **The light budget.** WebGL forward rendering can't afford a real light for every lamp. The rule is **8 real lights at most**, the ones nearest Enoch. Every other lamp is emissive, with bloom and a painted light pool on the ground. The Lighting Director swaps real lights onto the nearest lamps as Enoch moves.
3. **No hand-made models.** Every asset is canned or AI-generated (see Assets). The main risk is a mismatched look, handled by using one pack family and style-referenced generation.
4. **Performance budget.** 60 fps on a mid-range laptop with integrated graphics; under 300 draw calls; first load under 30 MB.
5. **Browser only.** Everything must work in current Chrome, Edge, and Firefox with no install.
6. **Dev-time AI only.** No API calls from the game.

## API constraints

| Service | Constraint | How Rest handles it |
| --- | --- | --- |
| **Claude** (the agent crew) | Plan usage limits per session and per week; finite context windows | Agents run in sequence, not all at once; the top-tier model is reserved for the Lead Architect; agents load the short GDD plus only the docs their ticket links; each agent owns one folder, so files stay small |
| **Tripo / Meshy** | Credit-limited generation | Generate only Enoch (from the creative director's drawings) and what the free packs don't have; every generation passes gate G2 |
| **Mixamo** | No public API | Auto-rigging and picking animations is a short manual step (upload, place markers, download), with no modeling skill needed |
| **Freesound** | API key required; rate limited; CC-BY sounds need credit | The Asset Scout batches searches and records every license in the manifest |
| **GitHub Pages** | Size limits on sites and files | Draco-compressed models, compressed audio, and a first-load budget under 30 MB |
| **The game itself** | None | No runtime API calls: no keys in the browser, no per-player cost, no rate limits for players |

## Technical risks

| Risk | Why it's a risk | Plan |
| --- | --- | --- |
| **The AI-generated character** | A generated raccoon may come out with a broken mesh, a bad rig, or a style that doesn't match the city pack, and no one on the team can fix it by hand | Validate it first: generate, auto-rig, and animate Enoch before any gameplay. Redraw or regenerate until it passes gate G2; clean, front-facing turnaround drawings give image-to-3D the best results. Fallback: a stock animal character from a pack, re-textured as a raccoon. Repairs use a third-person working animation, so no close-ups of his hands are needed |
| **A mismatched look** | Canned and generated assets come from different sources | One free pack family for the city; Enoch drawn in that pack's style; gate G2 |
| **Many lights** | A street of lamps can tank performance | Prove the 8-light rule and bloom in the first validation step, with 20+ lamps on screen |
| **No level editor** | Agents can't "see" a level they lay out, and the team doesn't use 3D tools | Levels are written layout files; the QA Playtester captures screenshots and a top-down view for the creative director to review |
| **Camera and climbing feel** | Third-person cameras in tight streets clip and frustrate | Use Rapier for collision; a camera that pulls in near walls; playtest at G5 |
| **Never used Three.js for a game** | Unknown pitfalls | Validation steps keep each risk small and visible |
| **Token overrun** | 3D work costs far more tokens than 2D | Track usage per agent; cut scope before the budget runs out |

## Validation steps (Prototype)

Each step must work before the next starts.

1. Enoch's model is generated in Tripo from the creative director's drawings, auto-rigged in Mixamo, and walking in an empty Three.js scene.
2. Enoch runs and climbs a pole on Rapier, with a working camera.
3. Lamp Row loads from its layout file, built from canned pieces, with 20+ lamps at 60 fps under the light budget.
4. The grid simulator lights and darkens lamps from JSON.
5. One click-and-hold repair (a dead lamp needing a bulb) works end to end, including the part check.
6. The blown fuse and the chewed cable are added; salvage, the satchel, and the 15-minute night work.
7. The Relight passes gate G4.

## Token budget

### Projection by agent (Prototype)

| Agent | Tokens (estimate) | Why |
| --- | --- | --- |
| Lead Architect | 200K | Planning, interfaces, ticket writing, reviews |
| Asset Scout | 100K | Searches and manifest entries |
| Level Builder | 400K | Layout files, loader, cables, the debug view; more iteration because layouts are reviewed from screenshots |
| Player Controller | 500K | Movement and camera feel take many iterations |
| Grid Simulator | 150K | Pure logic with tests |
| Repair Interaction | 150K | One click-and-hold interaction and a part check |
| Lighting Director | 600K | The wow moment; the most iteration |
| UI | 150K | Small overlay |
| Writer | 50K | A few dozen lines |
| QA Playtester | 300K | Runs on every pull request |
| Overhead | 250K | Context loading, rework after rejected gates |
| **Total** | **~2.9M** | |

### Projection by phase

| Phase | Projection |
| --- | --- |
| Prototype | ~2.9M |
| MVP | ~10M |
| Chapter One | ~25M+ |

### Keeping the budget

- Agents load the short GDD (the README) plus only the long-GDD docs their ticket links to.
- Fast-tier models do searching, checking, and UI; the top tier is reserved for the Lead Architect.
- Usage is recorded per agent after each validation step, and these numbers are updated after the prototype.
