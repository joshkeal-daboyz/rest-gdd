# AI-Era GDD Guidelines — Capstone First Draft

*Requirements and guidance from ELVTR "Multi-Agent AI for Game Development," Class #2. Paraphrased notes, not a transcript. Timestamps point to the recording.*

---

## 1. Assignment #1 at a glance (≈ 56:54)

| Item | Requirement |
|---|---|
| **Deliverable** | First draft of your capstone GDD, for the game you actually plan to build |
| **Due** | October 20 (one week after Class #2) |
| **Submit via** | Google Classroom |
| **Format** | GitHub repo link (recommended, since you can keep updating the same link all course), or a PDF, README or HTML file |
| **Length** | About 3–5 pages, **5 pages max** for the submitted version |
| **Required sections** | **Summary**, **Game Mechanics**, **AI Architecture**, **Technical Strategy** |
| **Other sections** | Add whatever your game needs. Leave out what it doesn't (e.g. no narrative section for a game with no story) |

### Rubric points
- **Game specificity**: every section describes *your* game, not a generic pipeline
- **Player experience clarity**: what the player sees and does, not only what the system computes
- **Agent role definitions**: each agent named, with its role in one plain-English sentence
- **Technical feasibility**
- **Presentation**

> ⚠️ Drafts that describe a generic or placeholder game, or that use course concepts without tying them to specific player-facing mechanics, lose credit on several sections.

---

## 2. Scoping rule: "One Agent, One Wow" (≈ 4:50)

- **Weekend test:** could two developers build a rough but playable version in a weekend (a week or two at most)? If not, cut scope.
- Build the **core gameplay loop first**. Add extra mechanics only after the prototype works.
- Use **phases** in the GDD (Prototype → MVP → future expansion) so the big ideas are kept but not built yet.
- **Each agent does one thing extremely well**, not many things adequately. Split broad roles (e.g. several UI agents, or a separate "UI juice" agent for animation and polish).
  - Agents with too many responsibilities get long files, cost more tokens per call, and produce unpredictable output.
- **Name your "wow" moment:** the single AI-driven moment the player will notice most. Build your technical strategy around making that moment work.
- The core game should be fun at its most basic, without leaning on "one more feature" to fix it (Minecraft's early versions focused on mining and crafting only).
- Prototype in validation steps, e.g. a character can walk around → buildings can be generated or imported → and so on.

---

## 3. The three new pillars of an AI GDD (≈ 12:58)

Beyond a traditional GDD, an AI GDD also acts as a **contract with your agent team** and the source of truth they work from.

### Pillar 1: AI Dev Pipeline
- Which agents are on the team, what each one does, and how they hand off work and communicate.
- It's a **living document**: expect to add, remove and refactor agents as you go.
- **Draw the line on creative control.** Decide which decisions need human approval.
- **Human review gates** are the simplest way to stop drift from your creative vision (approve → continue, reject → rework).
- The more content you let AI generate on its own, the more you need consistent style guides, a lore bible and other reference docs.

### Pillar 2: Technical Requirements & Constraints
- Name the technical risks **before** you hit them: an engine you haven't used, 3D model pipeline, asset sourcing, etc.
- Decide on engine, frameworks, and generated vs. existing assets (examples mentioned: Synty Studios asset packs, Meshy, Tripo, Blender + AI).
- **Constraints direct the agents.** If you don't specify tools and frameworks, agents will pick their own, and the result won't be what you pictured.
- Beginner advice: start small, with a browser engine like **Phaser** or with **Godot**, rather than Unreal on a $20 plan. Unreal works, but expect roughly 10× the complexity and token use. Use the class-provided subscription first.

### Pillar 3: Token Budgets & Projections
- Money (tokens), not time, is now the bottleneck. Estimate your token spend early.
- Your first estimate will be wrong. That's expected; the point is to stay cost-aware.
- Rough scale: a simple Phaser browser game might fit in about 1M tokens. A full 3D game with AI-assisted modeling can hit plan limits every session.
- Keep the scope **sustainable and viable**, and validate ideas before spending heavily.

### Checkpoint: answer all three for your game
1. *Pipeline:* "Agent X takes input A, produces output B, and the player sees C."
2. *Constraints:* "My biggest constraint is X because Y."
3. *Budget:* a ballpark token projection.

If you can't answer all three yet, keep working on the Technical Strategy.

---

## 4. Defining the Dev Crew (≈ 25:55)

- Each kind of generation gets a **dedicated, specialized agent**, not one generalist that knows the whole codebase.
- Mirroring a **real studio hierarchy** (director/orchestrator → leads → specialists) works well because models recognize that structure. Organizing by task or goal is also fine.
- Roles range from **high-level reasoning** (e.g. a Lead Architect on a top-tier model that hands tasks down to cheaper, faster models) to **low-level utility** (e.g. an inventory agent that knows where the inventory code and UI style docs live).
- Consider an **Asset Scraper agent** that finds existing human-made music, art and asset packs before you generate anything. It's cheaper, faster and often better quality.
- Build a crew **specific to your game** instead of downloading a generic 38-agent "studio" repo.

### What to write for each agent
- **Name**, plus **one sentence**: *"This agent does ___ when ___ happens, and the player sees ___."*
- Mark which agent is your **"One Wow" agent**.

### Example technical strategy (dungeon-crawler roguelike, Phaser + Claude)
| Agent | Input | Output |
|---|---|---|
| Floor Generator | seed, difficulty | JSON room layout |
| Enemy Behavior | enemy type/config | in-game enemy AI code (attack, flee, etc.) |
| Loot Narrator | item name, rarity | item description (or, reversed: description → stats and effects) |

Plus a **token budget** (e.g. ~1,200 tokens per floor × 10 floors per session) and **API constraints** (e.g. rate limits on room generation).

---

## 5. Structure & templates (≈ 36:17)

- **No template is provided on purpose.** Shape the GDD around your own game and voice.
- Order and include sections by what matters most for *your* game. If art is the core, give it real depth; if it's secondary, keep it brief.
- Suggested sections:
  - **Constraints**
  - **Engine Integration**: state the engine (Godot, Unity, Unreal, Phaser, custom). Default to an existing engine; building your own needs a strong reason, since it adds work like rendering and animation.
  - **Technical Strategy**: token budgets, agent role definitions, pipeline
- Use existing tools, plugins and assets wherever you can (e.g. don't rewrite character movement just because AI can).

---

## 6. Two-tier document strategy

| Short GDD (submit this) | Long GDD (optional, in your repo) |
|---|---|
| 3–5 pages, readable and pitch-like | Detailed mechanics, specific moments, effects, systems |
| Loaded into agent context, so it saves tokens | Split into linked docs per feature (e.g. `enemies.md`) |
| Works as a **roadmap/index** to the detailed docs | Referenced only when a feature needs it |

---

## 7. Mindset reminders
- The GDD is a foundation, not a one-shot prompt that builds the whole game for you. Expect iteration and human review throughout.
- A **5-page GDD is harder to write than a 100-page one**. Resist letting AI pad the document.
- If something worries you technically, **put it in the GDD now** so you can research it early.
- People judge a pipeline by the games it ships. Focus on the game.

---

## Draft checklist
- [ ] Summary, Game Mechanics, AI Architecture and Technical Strategy sections present
- [ ] Every section is specific to my game and describes what the player sees and does
- [ ] Scope passes the weekend test; future features moved into later phases
- [ ] "Wow" moment and One Wow agent identified
- [ ] Each agent: name + one plain-English sentence (does X when Y, player sees Z)
- [ ] Human review gates / creative-control boundaries defined
- [ ] Engine, tools, asset sources and biggest constraints stated
- [ ] Token budget projection included
- [ ] 5 pages or less (longer detail moved to linked docs)
- [ ] Submitted to Google Classroom by **Oct 20** (GitHub link, PDF, README or HTML)
