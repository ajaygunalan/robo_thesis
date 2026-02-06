# Zettelkasten++ (Vegapunk)

Building a "second brain" in Obsidian breaks at scale. The maintenance is manual and fragile: you keep splitting notes, rewriting for clarity, deciding what belongs where, maintaining cross-links, and preventing the same idea from being rewritten in multiple places and diverging over time.

Vegapunk fixes this by using AI to distill sources into atoms (one concept per file) and generate higher-level structure — molecules that group and connect related atoms, plus index notes that map collections of molecules — all linked via `[[wikilinks]]` under a single-source-of-truth rule: each idea lives exactly once, everything else links to it. The test is simple: after months away from a topic, reading a molecule should restore your understanding without returning to the original source. If you have to re-read the textbook, the molecule failed.

The knowledge isn't static. Creation is unconstrained — entropy accumulates naturally as you learn and distill. Organize and weave restore coherence periodically. Let the garden grow, then prune. Every skill checks what exists before creating, cites what exists when testing, and reports what's missing when searching. The vault knows more than you think.

---

## Structure

| Type | Pattern | Purpose |
|------|---------|---------|
| Atom | `lowercase_name.md` | One concept, one file. Complete, standalone. Single source of truth. |
| Molecule | `_lowercase_name.md` | Groups and connects related atoms into a narrative. 2-3 min read that restores understanding. |
| Index | `__lowercase_name.md` | Maps molecules within a folder. Navigation entry point. |

Wikilinks (`[[concept]]`) are the connections. They always point to the single source of truth. When you need depth, you follow the link. When you don't, you skip it.

**Scratch files** live alongside atoms and molecules in the target folder:

| Scratch file | Created by | Purpose |
|--------------|------------|---------|
| `learn_<source>.md` | `/vp-learn` | Q&A session artifact |
| `progress_<source>.md` | `/vp-learn` | Multi-session progress tracker |
| `distill_<source>.md` | `/vp-distill` | Molecules + atoms draft |
| `quiz_<source>.md` | `/vp-quiz` | Revision session artifact |

Scratch files are temporary. `/vp-split` deletes the distill file and offers to clean up learn/progress files.

---

## Commands

All commands use the `vp-` prefix.

**Create**

| Command | Purpose | Output |
|---------|---------|--------|
| `/vp-learn` | Study source through interactive Q&A, track progress across sessions | `learn_*.md`, `progress_*.md` in target folder |
| `/vp-distill` | Transform source or learning file into molecules + atoms | `distill_*.md` in target folder |
| `/vp-split` | Parse distill output into individual .md files | atoms + molecules in target folder |

**Maintain**

| Command | Purpose | Output |
|---------|---------|--------|
| `/vp-refine` | Improve existing molecules/atoms | modifies existing files |
| `/vp-organize` | Folder-level health: duplicates, orphans, broken links, stale indexes | terminal report |
| `/vp-weave` | Discover cross-folder connections between atoms/molecules | adds wikilinks to existing files |

**Use**

| Command | Purpose | Output |
|---------|---------|--------|
| `/vp-find` | Search vault for a concept (wikilink graph + content search) | terminal report |
| `/vp-quiz` | Socratic revision grounded in your vault's atoms | `quiz_*.md` in target folder |

---

## Workflow

```
  Source (PDF, slides, chapter)
    |
    |----> /vp-learn ----> learn_*.md        [optional: skip if you already understand]
    |                        |
    v                        v
  /vp-distill ----------> distill_*.md
    |
    v
  /vp-split ------------> atoms + molecules in vault
    |
    ================ vault =================
    |
    |-- /vp-refine       improve individual files
    |-- /vp-organize     folder-level health audit
    |-- /vp-weave        cross-folder connections
    |
    |-- /vp-find         search by concept
    '-- /vp-quiz         test retention
```

**Learn** is the only optional step. If you already understand the source material, go straight to distill. Learn creates scratch files (`learn_*.md`, `progress_*.md`) that track Q&A sessions and multi-session progress.

**Distill + Split** always run together. Distill drafts molecules and atoms in a single `distill_*.md` file. You iterate — review, give feedback, refine — until satisfied. Then split parses the distill file into individual `.md` files, normalizes LaTeX delimiters, checks for filename collisions, and deletes the distill file.

**Maintain** runs periodically. Refine improves individual files after they're in the vault. Organize audits an entire folder for structural health. Weave discovers connections across folders that you wouldn't find manually.

**Use** is ongoing. Find searches the vault by concept using the wikilink graph and content matching. Quiz tests retention through Socratic questioning grounded in your atoms — it cites what your vault says, not what it knows.

---

## Script Layer

Three Python scripts handle deterministic I/O so Claude only reasons. A SessionStart hook keeps the graph fresh.

| Script | Purpose | Used by |
|--------|---------|---------|
| `vault_graph.py` | Builds wikilink graph + health report (`vault_graph.json`) | organize, find, weave |
| `split_distill.py` | Parses distill file on `##` boundaries, normalizes LaTeX, creates files | split |
| `vault_grep.py` | Parallel multi-term search with wikilink scoring | find |

The SessionStart hook runs `vault_graph.py` automatically when a new Claude Code session begins, so the graph is always current.

---

## Design Influences

Vegapunk was designed after studying 9 open-source Obsidian + Claude Code repositories and 3 blog posts:

| Source | What It Is |
|--------|-----------|
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | Obsidian markdown/canvas/bases skills by Obsidian's CEO |
| [ZanderRuss/obsidian-claude](https://github.com/ZanderRuss/obsidian-claude) | 45 commands, 48 agents, 19 skills — the largest Obsidian + Claude Code project surveyed |
| [huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain) | Self-evolving brain with weekly consolidation cycle |
| [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) | Hooks, path-specific rules, session automation |
| [ashish141199/obsidian-claude-code](https://github.com/ashish141199/obsidian-claude-code) | Clean slash commands, networked thinking, git automation |
| [heyitsnoah/claudesidian](https://github.com/heyitsnoah/claudesidian) | PARA template, Firecrawl web archiving, setup wizard |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | Reference implementation of all 13 hook events |
| [nikhilmaddirala/gtd-cc](https://github.com/nikhilmaddirala/gtd-cc) | Plugin marketplace pattern, content extraction skill |
| [gapmiss/obsidian-plugin-skill](https://github.com/gapmiss/obsidian-plugin-skill) | Obsidian plugin development skill |
| [Corti.com CI/CD blog](https://corti.com/building-an-ai-powered-knowledge-management-system-automating-obsidian-with-claude-code-and-ci-cd-pipelines/) | Treats vault as production software with automated pipelines |
| [Noah Brier (Every.to)](https://every.to/podcast/how-to-use-claude-code-as-a-thinking-partner) | "Reading > writing" — Claude as thinking partner on 1,500 notes |
| [Axton Liu roundup](https://www.axtonliu.ai/newsletters/ai-2/posts/obsidian-claude-code-workflows) | Community workflow patterns aggregated in one place |

**What we adopted:**
- **[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)** — Obsidian markdown syntax rules (LaTeX, callouts, wikilinks) integrated into skill prompts
- **[ZanderRuss/obsidian-claude](https://github.com/ZanderRuss/obsidian-claude)** — Research orchestration patterns, citation enforcement ideas
- **[COG-second-brain](https://github.com/huytieu/COG-second-brain)** — Periodic cross-domain pattern discovery concept that informed `/vp-weave`
- **[ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm)** — Hooks and session automation patterns that informed the SessionStart hook
- **[Corti.com CI/CD blog](https://corti.com/building-an-ai-powered-knowledge-management-system-automating-obsidian-with-claude-code-and-ci-cd-pipelines/)** — "Treat vault as production software" principle that drove `vault_graph.py` and automated health auditing
- **[Noah Brier](https://every.to/podcast/how-to-use-claude-code-as-a-thinking-partner)** — "Reading over writing" philosophy — Claude reads your vault, not just generates content

**What makes Vegapunk different:**
- **Zettelkasten-native** — atoms/molecules/indexes vs PARA or flat structure. The hierarchy encodes granularity, not categories.
- **Curriculum-driven** — learn-distill-split is designed for studying textbooks and courses, not braindumping or journaling.
- **Script layer** — deterministic I/O (graph building, file splitting, parallel search) offloaded to Python. Claude only reasons.
- **Quiz** — no equivalent exists in any surveyed repository. Socratic revision grounded in your own atoms, not Claude's training data.
- **Single-source-of-truth enforcement** — every concept lives in exactly one atom. Duplicate checking before creation, periodic audits after.
