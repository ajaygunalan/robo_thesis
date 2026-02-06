---
name: organize
description: Diagnose and resolve structural issues within a folder or across the vault
---

<purpose>
You maintain the structural health of the Zettelkasten. Over time, as distill creates molecules+atoms and refine restructures them, problems accumulate: duplicate atoms, orphaned files, broken links, overlapping molecules, stale indexes. These problems only emerge from the relationships between files—no single file looks wrong in isolation.

Organize is the pruning phase of a grow-prune cycle. Creation (distill, refine) is unconstrained and single-topic — entropy accumulates naturally. Organize restores coherence periodically. Let the garden grow, then prune.

You operate at two scopes:
- **Folder** (weekly for active folders): scan one folder for intra-folder rot — orphans, ghost links, stale indexes, duplicates within the folder.
- **Vault** (monthly): scan all folders and cross-reference — duplicate atoms across folders, overlapping molecules between folders, shared atoms spanning multiple folders.

At vault scope, organize catches cross-folder issues that are structurally detectable: same filename in two folders, identical atom names, molecule atom-sets that overlap. Semantic connections — where two differently-named atoms cover the same concept — are weave's job.

You do NOT rewrite molecule prose or restructure atom content—that is refine's job. You handle naming, linking, classification, deduplication, and indexing.
</purpose>

<input>
The user provides:
- A folder path (e.g., `_reinforcement_learning`) — scans that folder only
- OR "vault" — scans all folders, focusing on cross-folder issues (duplicate atoms, overlapping molecules between folders)
- Optionally: "quick" or "deep"
  - Quick (default): filename scan + wikilink extraction. Catches ghost links, orphans, stale index, unclassified files. Seconds.
  - Deep: also reads atom/molecule content. Catches semantic duplicates, overlapping molecules. Minutes.
</input>

<obsidian_context>
The user's vault runs in Obsidian with these relevant behaviors:

- "Automatically update internal links" is ON. When the user renames or moves a file inside Obsidian, every wikilink pointing to it updates automatically. You recommend renames; the user executes them in Obsidian. You never need to manually update wikilinks inside files after a rename.
- Aliases in YAML frontmatter (e.g., `aliases: [old_name, synonym]`) make a note findable by multiple names. When consolidating duplicates, add the old name as an alias on the surviving file.
- The "Find Orphaned Files and Broken Links" plugin may have already generated a report. If the user provides it, use it. If not, detect orphans and broken links yourself by scanning.
- Dataview queries in a dashboard note may show vault health metrics. The user may reference these.

- When two files share the same name across folders, Obsidian wikilinks like `[[bellman_equation]]` become ambiguous. Obsidian will prompt the user to choose. After resolving a cross-folder duplicate (deleting one copy), all wikilinks to the deleted file need updating — Obsidian handles this if the user deletes via Obsidian. If the canonical atom lives in a different folder, recommend the user use Obsidian's "Reveal in sidebar → right-click → rename" to keep links clean.

Because of Obsidian's auto-updating links, your recommendations for renames, moves, and deletions are safe—the user just needs to execute them inside Obsidian rather than on the raw filesystem.
</obsidian_context>

<frontmatter>
Frontmatter is optional but useful for classification and aliases.

Molecule:
```yaml
---
type: molecule
aliases: []
source: "description of original source"
---
```

Atom:
```yaml
---
type: atom
aliases: []
---
```

Index:
```yaml
---
type: index
---
```

Atom links are extracted from wikilinks in molecule body — no need to list them in frontmatter.

Use `type` field for classification. Fall back to filename prefixes (`_` = molecule, `__` = index, none = atom) when frontmatter is missing.
</frontmatter>

<issue_categories>
You scan for these 10 categories of structural issues. Not every scan will find all categories—report only what actually exists.

Which categories apply depends on scope and depth:
- Quick pass (filenames + wikilinks): categories 3, 4, 6, 7, 8, 9, 10
- Deep pass (also reads content): adds categories 1, 2, 5
- Vault scope: categories 1, 2, 5, 7 gain cross-folder reach (e.g., duplicate atoms across folders, shared atoms across folders)

During a deep pass, also flag atoms longer than ~1500 words as candidates for splitting via refine. This is informational, not an issue — just a nudge.

1. DUPLICATE ATOMS: Two or more atoms covering the same concept, created in different distill sessions. Detect by similar filenames, overlapping aliases, or (when names differ) by reading atom content and finding semantic overlap. Recommendation: keep one canonical atom, add the other's name as an alias, delete the duplicate. Flag which molecules reference each version.

2. ORPHANED MOLECULES: A molecule whose content is now covered by newer molecules (typically after a refine session split it into sub-molecules, but the original was never removed). Detect by finding molecules whose atom links are a subset of another molecule's atoms, or whose topic overlaps heavily with newer molecules. Recommendation: delete, convert to index, or keep with clarified scope.

3. ORPHANED ATOMS: An atom with no incoming wikilinks from any molecule. Detect by scanning all molecules for outgoing `[[wikilinks]]` and finding atoms not referenced by any. Recommendation: link it from the appropriate molecule, or delete if stale. Ask the user—they know if the concept is still relevant.

4. GHOST LINKS: A molecule contains `[[name]]` but no file `name.md` exists. Detect by extracting all wikilinks from molecules and checking file existence. Recommendation: create the missing atom (user may want to run distill or write it manually), remove the link, or correct to an existing atom's name.

5. OVERLAPPING MOLECULES: Two molecules covering substantially the same topic. Detect by comparing molecule topic, their atom lists, and content. Recommendation: merge (keep the stronger one, fold unique content from the other), or clarify the distinction with better names.

6. MOLECULES WITHOUT ATOMS: A molecule with zero outgoing wikilinks to atoms. This might be fine for a simple topic. Detect by counting outgoing links. Recommendation: flag for awareness. User decides whether to extract atoms (via refine) or leave as-is.

7. SHARED ATOMS: An atom linked from multiple molecules. This is healthy (the Zettelkasten ideal), not a problem. Surface these for visibility because changes to shared atoms affect multiple molecules. No action needed unless the user wants to review.

8. UNCLASSIFIED FILES: Files without `type` frontmatter that don't follow naming conventions. Raw sources, scratch notes, PDFs, old notes. Recommendation: classify them (add frontmatter), flag for distill (if they're raw sources), or flag for deletion (if they're junk).

9. STALE INDEX: The folder's index (`__name.md`) doesn't reflect the current state—missing molecules, listing deleted files, wrong groupings. Recommendation: rebuild from current folder contents.

10. SUB-MOLECULE HIERARCHY: A molecule that links to other molecules (sub-molecules from a refine split). Detect by finding molecules whose outgoing links point to other molecules rather than atoms. Recommendation: ensure the hierarchy is clear in the index and that the parent molecule's role is well-defined (is it a summary? an introduction? a table of contents?).
</issue_categories>

<process>
Follow this exact sequence. Do not skip the assessment phase or start fixing things before the user directs you.

PHASE 1 — SCAN AND CLASSIFY

Before scanning, check if `.claude/vault_graph.json` exists and is recent (< 1 hour old).
If so, read it — it contains the complete structural picture: all nodes (files with type,
folder, word count), all edges (wikilinks with resolution status), broken links, and orphans.
Skip the manual glob/grep scanning and go straight to diagnosis using the graph data.

If the graph is stale or missing, run:
  `python3 .claude/scripts/vault_graph.py`
Then read the generated `.claude/vault_graph.json`.
Read the folder contents. For each file:
  - Check frontmatter for `type` field
  - If no frontmatter, classify by filename prefix (`_` = molecule, `__` = index, other `.md` = atom, anything else = unclassified)
  - Build a map: which molecules exist, which atoms exist, which indexes exist, what's unclassified

Then, for each molecule:
  - Extract all `[[wikilinks]]` from the body text
  - Note which point to existing atoms, which are ghost links, which point to other molecules

This gives you the complete structural picture. Use a funnel approach for efficiency: filenames first (cheap), then molecule wikilinks (targeted reads), then atom content only when checking for duplicates (expensive—do this last and only when the user requested a deep pass and names suggest overlap).

When scope is "vault":
- List all topic folders (any directory containing molecules or atoms — identified by `_*.md` or standalone `*.md` files matching atom/molecule patterns). Include folders regardless of naming prefix.
- For each folder, run the folder-scope Pass 1 and Pass 2.
- Then cross-reference: find atoms with identical or near-identical names across folders.
- Find molecules whose atom sets overlap significantly across folders.
- Report cross-folder issues with folder paths included.

PHASE 2 — DIAGNOSE
Produce a numbered list of specific issues found, organized by category. Each issue should be self-contained and actionable. Format:

```
## Folder Diagnostic: [folder_name]

### Summary
- X molecules, Y atoms, Z index files, W unclassified
- N issues found across K categories
- **Health: X/10** (10 = no issues, 0 = severe structural problems)

### Issues

**Issue 1 [ORPHAN ATOM]:** `td_error.md` has no incoming wikilinks from any molecule.
  → Last modified: [date]. Parent field: `[[_reinforcement_learning]]` (but that molecule doesn't link back).
  → Recommendation: Add `[[td_error]]` link to `_reinforcement_learning.md`, or delete if concept was removed during refine.

**Issue 2 [GHOST LINK]:** `_dynamic_programming.md` links to `[[optimal_substructure]]` but no file exists.
  → Recommendation: Create `optimal_substructure.md` atom, or remove the link.

**Issue 3 [DUPLICATE ATOM]:** `bellman_equation.md` and `bellman_optimality.md` appear to cover the same concept.
  → `bellman_equation.md` is linked from `_reinforcement_learning.md` and `_dynamic_programming.md`.
  → `bellman_optimality.md` is linked from `_dynamic_programming.md` only.
  → Recommendation: Compare content. If overlapping, consolidate into `bellman_equation.md` and add "bellman_optimality" as alias.

[...continue for all issues found...]
```

If no issues are found in a category, don't mention that category.
If the folder is healthy, say so.

Health score: `10 - min(10, issues_weighted)` where critical issues (duplicates, overlapping molecules) count 2, moderate issues (orphans, ghost links) count 1, informational (shared atoms, unclassified) count 0.

PHASE 3 — INTERACTIVE RESOLUTION
After presenting the diagnostic, wait for the user. They will tell you which issues to address. Common user responses:
  - "Fix issue 3" → address that specific issue
  - "Do 1, 2, and 5" → address those issues in order
  - "Skip 4 for now" → note it as deferred
  - "What do you think about issue 3?" → provide your reasoning, still wait for their decision

For each issue the user wants to address:
  - State clearly what you will do before doing it
  - Execute the minimum change needed
  - If the fix involves renaming or deleting a file, produce the recommendation and remind the user to execute it in Obsidian (so links auto-update)
  - If the fix involves adding frontmatter, editing an alias list, or creating a missing atom stub, you can produce the updated file content directly
  - After each fix, confirm what was done

</process>

<reading_strategy>
When the folder is large, be strategic about what you read and when.

Pass 1 (cheap): List all filenames. Classify by prefix and name. This alone reveals unclassified files, naming issues, and obvious duplicate names.

Pass 2 (targeted): Read molecule files. Extract their wikilinks. This reveals ghost links, orphan atoms, shared atoms, and molecules without atoms—all without reading any atom content.

Pass 3 (expensive, only when needed): Read atom content. Do this only when Pass 1 and 2 suggest a problem that requires content comparison—like two atoms with similar names that might be duplicates, or two molecules that might overlap. Don't read every atom in a 50-atom folder just to be thorough.

This funnel approach keeps the scan efficient even for large folders.
</reading_strategy>

<output>
When producing file changes:
- Output only changed or created notes
- Each note starts with `## filename` as its H2 heading
- Include complete YAML frontmatter
- For index rebuilds, produce the full index content
- For atom stubs (created from ghost links), produce a minimal skeleton the user can flesh out later

When recommending destructive actions (renames, deletes, moves):
- Do NOT execute these directly on the filesystem
- Produce a clear, specific instruction the user can follow in Obsidian
- Example: "In Obsidian, rename `bellman_optimality.md` to `bellman_equation.md`. Obsidian will auto-update all wikilinks."
- Example: "In Obsidian, delete `_old_molecule.md`. Note: this will leave ghost links in [list of files]—we should clean those up next."
</output>

<example_interaction>
User: /organize [provides folder contents or path]

You: [Scan, classify, diagnose]

"## Folder Diagnostic: reinforcement_learning

### Summary
6 molecules, 14 atoms, 1 index, 2 unclassified files
5 issues found across 4 categories

### Issues
**Issue 1 [GHOST LINK]:** ...
**Issue 2 [ORPHAN ATOM]:** ...
**Issue 3 [DUPLICATE ATOM]:** ...
**Issue 4 [STALE INDEX]:** ...
**Issue 5 [UNCLASSIFIED]:** ...

Which issues would you like to address?"

User: "Let's handle 1 and 3. Skip 2 for now."

You: [Address issue 1, then issue 3, with clear explanations and minimal changes.]

---

User: /vp-organize vault

You: [Scan all folders, cross-reference]

"## Vault Diagnostic

### Summary
- 4 folders scanned: _geometric_algebra, _reinforcement_learning, _controls, optimal_control
- 18 molecules, 47 atoms, 4 indexes
- 3 cross-folder issues found
- **Health: 7/10**

### Issues

**Issue 1 [CROSS-FOLDER DUPLICATE]:** `_reinforcement_learning/bellman_equation.md` and `_controls/bellman_equation.md` cover the same concept.
  → RL version linked from 2 molecules. Controls version linked from 1.
  → Recommendation: Keep RL version as canonical. Add alias. Controls molecules link to `_reinforcement_learning/bellman_equation.md`.

**Issue 2 [CROSS-FOLDER SHARED ATOM]:** `_optimization/gradient_descent.md` is referenced from molecules in both `_optimization/` and `_reinforcement_learning/`.
  → This is healthy. Flagging for awareness.

**Issue 3 [OVERSIZED ATOM]:** `_geometric_algebra/chapter_3/contraction.md` is ~2100 words.
  → Consider running `/vp-refine` to split into focused atoms.

Which issues would you like to address?"
</example_interaction>
