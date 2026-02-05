---
name: split
description: Parse distill output and create individual .md files in your vault
---

# split notes

<role>
Parse raw `/vp-distill` output into separate `.md` files.
</role>

<input>
User provides a topic name. Reads `_working/<topic>/distill.md` (output of `/vp-distill`).
H2 headings (`## filename`) mark file boundaries.

Files are created IN the working directory (`_working/<topic>/`), not in the final destination.
Use `/vp-move` later to move them to their permanent location.
</input>

<process>
1) Parse boundaries and list files that would be created in `_working/<topic>/`; ask for approval.
2) On approval, normalize LaTeX:
   - inline math: `$...$` (not `\(...\)`)
   - display math: `$$...$$` (not `\[...\]`)
3) Create the files in `_working/<topic>/`.
4) Delete `distill.md` from `_working/<topic>/`.
5) Remind user to run `/vp-move <topic> <target_folder>` when ready to commit.
</process>

<output>
List the created filenames in `_working/<topic>/`. Confirm `distill.md` was deleted.
Remind user: "Run `/vp-move <topic> <target_folder>` to move files to their permanent home."
</output>
