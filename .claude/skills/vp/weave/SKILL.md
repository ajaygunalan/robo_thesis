---
name: weave
description: Discover cross-folder semantic connections between atoms and molecules
---

<purpose>
You discover hidden relationships across the knowledge graph. While organize maintains structural health within a folder (and catches structurally obvious cross-folder issues like identical filenames), weave finds semantic connections that only emerge when you read content across disciplines.

Weave operates across folders, not within them. Within-folder connections are organize's territory (shared atoms, orphan atoms). Weave's value is in the bridges between disciplines — where RL meets controls, where optimization meets linear algebra, where geometric algebra provides tools for manipulation.

This is proactive discovery, not reactive cleanup. You read content, find semantic similarities, and suggest connections the user didn't see. You never create or rewrite content — you link, suggest, and hand off.
</purpose>

<input>
The user provides:
- No argument → scans entire vault (default, and the main use case)
- Two or more folder paths → scans only those folders for cross-connections
- A specific atom/molecule path → finds connections for that one note across the vault
</input>

<process>
PHASE 1 — INDEX (cheap)
Check if `.claude/vault_graph.json` exists and is recent.
If so, read it — it contains all nodes grouped by folder and all edges.
Extract:
- Cross-folder name map: atoms with similar names in different folders
- Shared atoms: nodes with incoming edges from multiple folders
- Wikilink density: which folders reference each other most

If graph is stale or missing, run:
  `python3 .claude/scripts/vault_graph.py`

This replaces manual globbing and wikilink extraction.

PHASE 2 — READ CANDIDATES (targeted)
Read content only for candidates from Phase 1:
- Atoms with similar names across folders
- Atoms referenced by molecules in multiple folders
- A sample of 2–3 atoms per folder to understand domain vocabulary and notation

The goal is to build enough understanding of each folder's "language" to spot cross-domain equivalences in Phase 3.

PHASE 3 — DISCOVER (three types)

**Type 1: SAME CONCEPT, DIFFERENT NAMES** (canonical atom resolution)
Two atoms in different folders explain the same concept using different terminology.
- Example: RL's `value_function.md` = optimal control's `cost_to_go.md`
- Example: geometric algebra's `outer_product.md` = linear algebra's `wedge_product.md`
- Recommendation: pick one as canonical (the one with richer content or more incoming links), add the other name as an alias, and add a cross-link. Do NOT delete or merge — that's organize's job if the user wants consolidation.
- This is the highest-value discovery — it unifies the knowledge graph across disciplines.

**Type 2: MISSING BRIDGES** (prerequisite/dependency links)
An atom in folder X explains something that an atom in folder Y uses or assumes without linking.
- Example: `_reinforcement_learning/_policy_gradients.md` uses gradient computation but doesn't link to `_optimization/gradient_descent.md`
- Example: `_controls/_lqr.md` assumes Bellman optimality but doesn't link to `_reinforcement_learning/bellman_equation.md`
- Recommendation: add `[[atom_name]]` wikilinks where the dependency exists. The link makes the prerequisite discoverable during revision.

**Type 3: EMERGENT MOLECULES** (cluster detection)
3+ atoms across folders share a theme but no molecule connects them.
- Example: `_rl/exploration.md`, `_optimization/stochastic_search.md`, and `_controls/system_identification.md` all deal with the explore-exploit tradeoff — but no molecule ties them together.
- Recommendation: suggest creating a new cross-cutting molecule (hand off to `/vp-distill`) or adding a section to an existing molecule (hand off to `/vp-refine`). Weave does not create the molecule itself.

PHASE 4 — PRESENT AND RESOLVE (interactive)
Present discoveries grouped by type. For each:

```
## Discovered Connections

### Same Concept, Different Names

**1.** `_reinforcement_learning/value_function.md` ↔ `optimal_control/cost_to_go.md`
  → Both define the expected cumulative reward/cost from a state. RL uses "value," controls uses "cost-to-go."
  → Recommendation: Add alias and cross-link. Keep both files (different notation/context).

### Missing Bridges

**2.** `_controls/_lqr.md` uses dynamic programming but doesn't link to `_reinforcement_learning/bellman_equation.md`
  → Add `[[bellman_equation]]` where LQR discusses the recursive cost decomposition.

### Emergent Molecules

**3.** Cluster: `_rl/exploration.md`, `_optimization/stochastic_search.md`, `_controls/system_identification.md`
  → Common theme: learning under uncertainty. Consider a cross-cutting molecule.
  → Hand off to `/vp-distill` if interested.

Which connections would you like to act on?
```

User decides per discovery:
- **Link** → weave adds the wikilink and/or alias
- **Merge** → hand off to organize (weave doesn't merge)
- **Create molecule** → hand off to distill (weave doesn't create files)
- **Skip** → move on

Execute only approved link additions.
</process>

<boundaries>
Weave CAN:
- Add `[[wikilinks]]` to existing atoms and molecules
- Add aliases to YAML frontmatter
- Suggest connections and explain reasoning

Weave CANNOT:
- Create new files (→ distill)
- Rewrite or restructure content (→ refine)
- Merge or delete atoms (→ organize)
- Operate within a single folder (→ organize)

When weave discovers something that needs action beyond linking, it names the appropriate skill and stops.
</boundaries>

<efficiency>
Weave is expensive — it reads content across the entire vault. Be strategic:

- Phase 1 (filenames + wikilinks) is cheap. Do this for all folders.
- Phase 2 (content reading) is targeted. Only read candidates, not every atom.
- Phase 3 (discovery) uses the understanding built in Phase 2.

For vault-wide scans with 4+ folders:
- Launch parallel subagents, one per folder, to index atoms/molecules and summarize domain vocabulary.
- Collect indexes centrally.
- Cross-reference names and topics across indexes.
- Read content only for cross-folder candidates identified by cross-referencing.

For a single-note scan (`/vp-weave path/to/atom.md`):
- Read the target note.
- Search all other folders for related filenames and wikilink mentions.
- Read only the candidate matches.
</efficiency>
