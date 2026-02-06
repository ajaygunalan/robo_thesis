---
name: split
description: Parse distill output and create individual .md files in your vault
---

<role>
Parse raw `/vp-distill` output into separate `.md` files, directly in the vault.
</role>

<input>
User provides the path to a `distill_<source>.md` file in a target folder (e.g., `_geometric_algebra/chapter_3/distill_geo_ch3.md`).
H2 headings (`## filename`) mark file boundaries.

The target folder is inferred from the distill file's location — atoms and molecules are created in the same folder.
</input>

<process>
1) Run: `python3 .claude/scripts/split_distill.py <distill_file>`
   This parses H2 boundaries, normalizes LaTeX, checks for collisions,
   and outputs a JSON manifest.

2) Show user the file list. If collisions found:
   - Show which files already exist
   - Let them decide per file: overwrite, rename, or skip
   - Abort entirely if they want

3) If manifest shows scratch files, ask:
   "Delete scratch files from the study phase?"

4) Run: `python3 .claude/scripts/split_distill.py <distill_file> --execute [--skip=files] [--cleanup]`
   Creates files in target folder, deletes distill file (and scratch files if --cleanup).
   Note: --cleanup must be combined with --execute in one call, since --execute deletes the distill file.

5) Suggest /vp-organize if folder index may need updating.
</process>

<output>
List the created filenames with their paths. Confirm distill file was deleted.
Note if the folder's index (`__name.md`) may need updating — suggest `/vp-organize` if so.
</output>
