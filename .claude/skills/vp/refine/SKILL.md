---
name: refine
description: Assess and improve an existing molecule and its atoms through guided iteration
---

Assess and improve an existing molecule and its linked atoms through conversation.

<input>
The user provides a molecule file path. The atoms are determined by the molecule's
wikilinks — any `[[concept]]` in the molecule body is an atom in scope.

Read the molecule and all its linked atoms. This is the working set for refinement.
</input>

<process>
1. **Assess.** Read the molecule and its atoms. Produce a diagnostic covering:
   - Narrative coherence and length (2–3 minute read?)
   - Which concepts have atoms and whether they're standalone
   - Which concepts lack atoms but need them (inline depth that should be extracted)
   - Atoms that overlap, should be merged, split, or renamed
   - Whether the molecule links 4–6 atoms

2. **Discuss.** Present the diagnostic and wait for the user's direction.
   Do not start rewriting until the user tells you what to focus on.

3. **Act.** Execute only what the user asked for.

4. **Verify.** Confirm what was changed, flag anything else you'd recommend.
</process>

<assessment_guidelines>
Be specific and actionable. Look for:
- **Trapped depth:** molecule explains a mechanism inline instead of linking to an atom
- **Missing atoms:** concept a reader would want to understand fully, but no atom exists
- **Ghost links:** wikilinks pointing to non-existent atoms
- **Redundant atoms:** two atoms covering the same concept → merge
- **Oversized atoms:** covers multiple concepts → split
- **Narrative gaps:** molecule doesn't build from problem to solution
- **Orphan atoms:** atoms that exist but aren't linked from the molecule
</assessment_guidelines>

<output>
Edit files in place. Write new atoms fresh as standalone reference — don't copy-paste
from the molecule. Create new atoms in the same folder as the molecule.
</output>
