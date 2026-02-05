---
name: weave
description: Discover non-obvious connections between atoms and molecules
---

<purpose>
You discover hidden relationships in the knowledge graph. While organize maintains structural health (fixing broken links, removing duplicates), weave grows the structure by finding connections that aren't yet explicit.

This is proactive discovery, not reactive cleanup. You look at content, find semantic similarities, and suggest connections the user didn't see.
</purpose>

<input>
The user provides:
- A folder path (or "vault" for cross-folder discovery)
- Optionally: a specific atom/molecule to find connections for
- Optionally: a scope (within folder, across folders, specific folders)
</input>

<process>
1. **Scan content** — Read atoms and molecules in scope. Understand what each one is about.

2. **Find semantic relationships** — Look for:
   - Same concept, different names (RL's "value function" = optimal control's "cost-to-go")
   - Related concepts not yet linked (bellman equation relates to dynamic programming)
   - Patterns across atoms (these 3 atoms together form a higher concept)
   - Cross-folder connections (this RL atom connects to this controls atom)

3. **Present discoveries** — Show what you found:
   ```
   ## Discovered Connections

   **1. Semantic match across folders:**
   `_reinforcement_learning/value_function.md` ↔ `_controls/cost_to_go.md`
   → These describe the same concept. Consider merging or cross-linking.

   **2. Missing link:**
   `bellman_equation.md` discusses optimality but doesn't link to `_dynamic_programming.md`
   → Add [[_dynamic_programming]] reference?

   **3. Emerging pattern:**
   These atoms share a common theme: [list]
   → Consider creating a molecule that connects them.
   ```

4. **User decides** — For each discovery:
   - Add a wikilink
   - Merge atoms (hand off to organize)
   - Create new molecule (hand off to distill/refine)
   - Skip

5. **Execute** — Apply only what user approves.
</process>

<what_to_look_for>
- **Same concept, different names** — Especially across folders where topics overlap
- **Implicit relationships** — An atom explains something that another atom uses without linking
- **Hierarchical connections** — Atoms that should be grouped under a molecule
- **Cross-domain bridges** — Concepts from one field that apply to another
- **Prerequisite chains** — Atom A assumes knowledge from atom B, but doesn't link to it
</what_to_look_for>

<output>
Terminal output for the discovery list and interaction.

If new links are added, the atoms/molecules are edited in place to include the wikilinks.

If new atoms or molecules are suggested, hand off to distill or refine — weave doesn't create content, it discovers connections.
</output>

<efficiency>
Weave is expensive — it reads content, not just structure. For large folders:
- Start with filenames and frontmatter (cheap)
- Read content only for promising candidates
- Use subagents for parallel reading when scanning across folders
</efficiency>
