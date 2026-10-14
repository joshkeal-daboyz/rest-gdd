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
| Level layout | **Blender** | Three.js has no editor, so levels are built in Blender with named empties as markers, then exported to GLB |
| Character pipeline | **Meshy or Tripo** → Blender cleanup → **Mixamo** rig and animations | Enoch is humanoid enough to use Mixamo's humanoid rig |
| Audio | Web Audio API, through Three.js `PositionalAudio` | The grid hum is positional, so live lines sound alive near Enoch |
| Testing | **Vitest** (logic), **Playwright** (scripted playthroughs) | Run by the QA Playtester on every pull request |
| Hosting | **GitHub Pages** | The playable build lives at a shareable link |
| Input | Keyboard and mouse | Gamepad support after the MVP |

## Assets

**Find before you generate.** The Asset Scout searches in this order:

1. **CC0 packs** (Quaternius, KayKit, Kenney) for prototype buildings, props, poles, and vehicles.
2. **Licensed packs** (for example Synty's POLYGON City) if CC0 can't hit the art direction for the MVP.
3. **Freesound** (CC0 or CC-BY) for hums, sparks, and ambience.
4. **Generation** (Meshy or Tripo) only for what doesn't exist, starting with Enoch himself. Every generated asset passes gate G2.

Every asset's source and license is recorded in `assets/manifest.json`.

## Constraints

1. **Three.js is a rendering library, not an engine.** It provides no editor, physics, character controller, animation tools, or scene management. Each of those comes from a library named above, or from a small module owned by one agent. Agents must not introduce new libraries without a ticket approved at gate G1.
2. **The light budget.** WebGL forward rendering can't afford a real light for every lamp. The rule is **8 real lights at most**, the ones nearest Enoch. Every other lamp is emissive, with bloom and a painted light pool on the ground. The Lighting Director swaps real lights onto the nearest lamps as Enoch moves.
3. **Performance budget.** 60 fps on a mid-range laptop with integrated graphics; under 300 draw calls; first load under 30 MB.
4. **Browser only.** Everything must work in current Chrome, Edge, and Firefox with no install.
5. **Dev-time AI only.** No API calls from the game.

## Technical risks

| Risk | Why it's a risk | Plan |
| --- | --- | --- |
| **The 3D character pipeline** | A generated raccoon must be cleaned up, rigged, and animated, with hands good enough for close-up repairs | Validate it first: generate, rig, and animate Enoch before any gameplay. If the hands fail, the repair close-ups use first-person hand models instead. |
| **Many lights** | A street of lamps can tank performance | Prove the 8-light rule and bloom in the first validation step, with 20+ lamps on screen |
| **No level editor** | Agents can't "see" a level they lay out | Blender is the editor; markers are named so agents work with data, not guesses |
| **Camera and climbing feel** | Third-person cameras in tight streets clip and frustrate | Use Rapier for collision; a camera that pulls in near walls; playtest at G5 |
| **Never used Three.js for a game** | Unknown pitfalls | Validation steps keep each risk small and visible |
| **Token overrun** | 3D work costs far more tokens than 2D | Track usage per agent; cut scope before the budget runs out |

## Validation steps (Prototype)

Each step must work before the next starts.

1. Enoch's model is generated, rigged, and walking in an empty Three.js scene.
2. Enoch runs and climbs a pole on Rapier, with a working camera.
3. Lamp Row loads from Blender with 20+ lamps at 60 fps under the light budget.
4. The grid simulator lights and darkens lamps from JSON.
5. One repair (replace) works end to end.
6. Splice and reroute are added; salvage and the satchel work.
7. The Relight passes gate G4.

## Token budget

### Projection by agent (Prototype)

| Agent | Tokens (estimate) | Why |
| --- | --- | --- |
| Lead Architect | 200K | Planning, interfaces, ticket writing, reviews |
| Asset Scout | 100K | Searches and manifest entries |
| Level Builder | 300K | Loader, cables, marker handling |
| Player Controller | 500K | Movement and camera feel take many iterations |
| Grid Simulator | 150K | Pure logic with tests |
| Repair Interaction | 400K | Three interactions with close-up cameras |
| Lighting Director | 600K | The wow moment; the most iteration |
| UI | 150K | Small overlay |
| Writer | 50K | A few dozen lines |
| QA Playtester | 300K | Runs on every pull request |
| Overhead | 250K | Context loading, rework after rejected gates |
| **Total** | **~3M** | |

### Projection by phase

| Phase | Projection |
| --- | --- |
| Prototype | ~3M |
| MVP | ~10M |
| Chapter One | ~25M+ |

### Keeping the budget

- Agents load the short GDD (the README) plus only the long-GDD docs their ticket links to.
- Fast-tier models do searching, checking, and UI; the top tier is reserved for the Lead Architect.
- Usage is recorded per agent after each validation step, and these numbers are updated after the prototype.
