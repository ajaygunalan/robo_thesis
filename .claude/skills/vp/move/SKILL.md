---
name: move
description: Move completed work from working directory to vault folder
---

<purpose>
Move molecule and atoms from the working directory to their permanent home in the vault.
This is the "commit" step — you've learned, distilled, split, and reviewed. Now the
knowledge joins your permanent collection.
</purpose>

<input>
User provides:
- Topic name (matches `_working/<topic>/`)
- Target folder path (e.g., `_geometric_algebra/`)
</input>

<process>
1. Check `_working/<topic>/` exists and contains split files (molecule + atoms)
2. List files that will be moved; ask for approval
3. Move molecule (`_*.md`) and atoms (`*.md` without underscore prefix) to target folder
4. Ask user: "Delete working artifacts (learn.md, quiz.md)?"
   - If yes: delete them and remove empty directory
   - If no: leave them for reference
5. Confirm what was moved and where
</process>

<output>
Terminal output listing moved files and final locations.
</output>
