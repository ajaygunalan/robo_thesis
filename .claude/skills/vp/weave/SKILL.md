---
name: weave
description: Discover cross-folder semantic connections between atoms and molecules
---

Discover semantic connections across folders that only emerge when you read content across disciplines. Weave adds links and suggests connections — it never creates, rewrites, or deletes files.

<input>
The user provides:
- No argument → scans entire vault (default)
- Two or more folder paths → scans only those folders
- A specific atom/molecule path → finds connections for that one note
</input>

<process>
PHASE 1 — INDEX (cheap)

Read `.claude/vault_graph.json` (run `python3 .claude/scripts/vault_graph.py` if stale/missing). Extract cross-folder name overlaps, shared atoms, and wikilink density between folders.

PHASE 2 — READ CANDIDATES (targeted)

Read content only for: atoms with similar names across folders, atoms referenced from multiple folders, and 2–3 atoms per folder to learn each domain's vocabulary. For 4+ folders, use parallel subagents.

PHASE 3 — DISCOVER

Three types of connection:

**SAME CONCEPT, DIFFERENT NAMES** — Two atoms in different folders explain the same thing (e.g., `value_function.md` ↔ `cost_to_go.md`). Pick one as canonical, add alias and cross-link. Highest-value discovery.

**MISSING BRIDGES** — An atom uses or assumes a concept from another folder without linking to it. Add `[[wikilinks]]` where the dependency exists.

**EMERGENT MOLECULES** — 3+ atoms across folders share a theme but no molecule connects them. Suggest creating one via `/vp-distill`.

PHASE 4 — RESOLVE (interactive)

Present discoveries grouped by type. User decides per discovery: link it, skip it, or hand off to another skill. Execute only approved link additions.
</process>
