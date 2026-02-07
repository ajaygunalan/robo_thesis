---
name: organize
description: Diagnose and resolve structural issues within a folder or across the vault
---

Scan a folder or the entire vault for structural problems and resolve them interactively.

## Input

The user provides:
- A folder path (e.g., `_reinforcement_learning`) — scans that folder only
- OR "vault" — scans all folders, focusing on cross-folder issues
- Optionally: "quick" (default) or "deep"
  - Quick: filename scan + wikilink extraction. Seconds.
  - Deep: also reads content. Catches semantic duplicates, overlapping molecules. Minutes.

## Issue Categories

Scan for these issues. Report only what exists.

Quick pass catches: 3–10. Deep pass adds: 1, 2, 5. Vault scope extends 1, 2, 5, 7 across folders.
Deep pass also flags atoms >1500 words as split candidates (informational).

1. DUPLICATE ATOMS — same concept in multiple files → keep canonical, alias the other, delete duplicate
2. ORPHANED MOLECULES — content now covered by newer molecules → delete, convert to index, or clarify scope
3. ORPHANED ATOMS — no incoming wikilinks from any molecule → link from appropriate molecule or delete
4. GHOST LINKS — `[[name]]` in molecule but no `name.md` exists → create atom, remove link, or correct name
5. OVERLAPPING MOLECULES — two molecules covering same topic → merge or clarify distinction
6. MOLECULES WITHOUT ATOMS — zero outgoing wikilinks → flag for awareness, user decides
7. SHARED ATOMS — linked from multiple molecules → healthy, surface for visibility
8. UNCLASSIFIED FILES — don't follow naming conventions (`_` molecule, `__` index, none atom) → classify or flag
9. STALE INDEX — `__name.md` doesn't reflect current folder contents → rebuild
10. SUB-MOLECULE HIERARCHY — molecule links to other molecules → ensure hierarchy is clear in index

## Process

Do not start fixing before the user directs you.

PHASE 1 — SCAN

Check if `.claude/vault_graph.json` exists and is recent (< 1 hour). If so, read it — it has all nodes, edges, broken links, and orphans. Skip manual scanning.

If stale or missing, run: `python3 .claude/scripts/vault_graph.py`

Classify files by filename prefix (`_` = molecule, `__` = index, no prefix = atom). Extract `[[wikilinks]]` from molecules. For deep pass, read atom content only when names suggest duplicates.

For vault scope: scan each folder, then cross-reference for duplicate atoms and overlapping molecules across folders.

PHASE 2 — DIAGNOSE

Produce a numbered issue list. Each issue: category tag, what's wrong, recommendation. Include a summary with file counts and health score (10 = no issues, deduct 2 for critical issues like duplicates, 1 for moderate like orphans).

PHASE 3 — RESOLVE

Wait for user direction. They pick which issues to fix. For each:
- State what you'll do before doing it
- Execute the minimum change
- When renaming a file, also grep and update all wikilinks referencing the old name
- Confirm what was done

## Output

- Output only changed or created files
- For index rebuilds, produce full content
- For atom stubs (from ghost links), produce a minimal skeleton
