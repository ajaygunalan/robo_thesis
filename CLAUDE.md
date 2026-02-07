# Overview

This Obsidian vault uses VegaPunk — AI skills that decompose sources (textbooks, lectures, videos) into reusable knowledge. Each concept gets one atom, one place, one source of truth. Related atoms compose into molecules through `[[wikilinks]]`. The vault grows through unconstrained creation and stays coherent through periodic maintenance.

# Structure

| Prefix | Type | Purpose |
|--------|------|---------|
| `__` | Index | Entry point for a discipline, maps its molecules |
| `_` | Molecule | Captures one source as a standalone narrative |
| (none) | Atom | One concept, fully explained |

Molecules are the primary unit — each one captures what a chapter, lecture, or video teaches as a 2–3 minute narrative. Atoms provide progressive disclosure: instead of explaining every concept inline, the molecule links to atoms via `[[wikilinks]]` for depth. This keeps molecules concise while the full explanation lives in the atom. Each concept lives in exactly one atom — no duplicates. Everything else links to it.

# Content Standards

**Atom** — a self-contained explanation of one concept:
- Intuition: what problem does this solve?
- Mechanism: how does it work?
- Formalization: formulas, algorithms, diagrams
- Test: readable in isolation with full understanding
- Oversized: >1500 words → split candidate

**Molecule** — the narrative essence of one source:
- What problems the source addresses and why they matter
- How the ideas connect and build from problem to solution
- Links 4–6 atoms for progressive disclosure
- Target: 2–3 minute standalone read
- Test: understand what the source teaches without reading it or clicking any links

# Knowledge Evolution

Knowledge isn't static. Molecules break apart when inline depth needs its own atom (fission). Atoms combine into new molecules when patterns emerge across sources (fusion). Molecules connect across folders when concepts bridge disciplines. Every skill checks what exists before creating, cites what exists when testing, and reports what's missing when searching.

# Two Repos, One Disk

`.claude/` is a nested git repo pointing at `github.com/ajaygunalan/vegapunk`. The parent repo (`robo_thesis`) tracks everything including `.claude/` files. Push each independently:

- **robo_thesis** (vault + tooling): `cd /media/ajay/gdrive/_robo_thesis` — push here for vault content changes
- **vegapunk** (tooling only): `cd /media/ajay/gdrive/_robo_thesis/.claude` — push here when skills, scripts, or settings change

When a change touches both vault files and `.claude/` files, commit and push from both directories.
