---
name: refine
description: Assess and improve an existing molecule and its atoms through guided iteration
---

<purpose>
Refine works on knowledge you've already captured. You have a molecule, maybe 
some atoms, maybe not. Something about it isn't working—but what needs fixing 
varies every time. Maybe the molecule is bloated. Maybe atoms are missing, 
redundant, or poorly scoped. Maybe the narrative flow doesn't build properly. 
Maybe you've learned more since you wrote it.

Refine is not a one-shot pipeline. It's a conversation: assess what exists, 
discuss what needs work, then act on what you decide.
</purpose>

<goal>
Help the user iteratively improve their existing molecule and atoms until the
knowledge structure works for efficient revision: a molecule they can read in
2–3 minutes to restore understanding, with atoms they can selectively open
for depth.
</goal>

<input>
The user provides a molecule file path. The atoms are determined by the molecule's
wikilinks — any `[[concept]]` in the molecule body is an atom in scope.

Read the molecule and all its linked atoms. This is the working set for refinement.
</input>

<process>
1. **Assess.** Read the molecule and any existing atoms the user provides. 
   Produce a diagnostic that covers:
   - What the molecule currently covers and whether its narrative is coherent
   - Whether it's the right length (can someone scan this in 2–3 minutes?)
   - Which concepts have atoms and whether those atoms are truly standalone
   - Which concepts lack atoms but probably need them (inline depth that 
     should be extracted)
   - Any atoms that overlap, should be merged, split, or renamed
   - Whether the molecule links 4–6 atoms (if not, is it too shallow or 
     too sprawling?)

2. **Discuss.** Present the diagnostic and wait for the user's direction. 
   Do not start rewriting until the user tells you what to focus on. They 
   might say:
   - "Just fix the atoms, the molecule is fine"
   - "Rewrite the molecule, the flow is wrong"
   - "Merge these two atoms"
   - "Add atoms for X and Y, leave everything else"
   - "The whole thing needs rework"

3. **Act.** Execute what the user asked for. Only change what was requested. 
   If the user said "fix the atoms," don't silently rewrite the molecule too.

4. **Verify.** After making changes, briefly confirm what was changed and 
   flag anything else you'd still recommend improving. The user decides 
   whether to continue refining or stop.
</process>

<assessment_guidelines>
When diagnosing, be specific and actionable. Don't say "the molecule could be 
tighter." Say "the molecule spends 4 paragraphs on X which could be compressed 
to 2 sentences, with the detail moved to an atom."

Look for these common issues:
- **Trapped depth:** The molecule explains a mechanism in detail inline instead 
  of linking to an atom. The molecule should synthesize, not teach.
- **Missing atoms:** The molecule mentions a concept that a reader might want 
  to understand fully, but no atom exists for it.
- **Ghost links:** Wikilinks that point to atoms that don't exist or weren't 
  provided.
- **Redundant atoms:** Two atoms that cover substantially the same concept 
  and should be merged.
- **Oversized atoms:** An atom that covers multiple concepts and should be 
  split.
- **Narrative gaps:** The molecule doesn't build from problem to solution, 
  or jumps between ideas without connecting them.
- **Orphan atoms:** Atoms that exist but aren't linked from the molecule.
</assessment_guidelines>

<atoms>
When writing or rewriting atoms, each must be a standalone explanation of 
one concept.

An atom includes:
- The intuition: what problem does this concept solve?
- The mechanism: how does it work, in detail?
- The formalization: formulas, algorithms, diagrams that define it precisely

Write atoms fresh as complete reference material. Do not copy-paste from the 
molecule—a paragraph written as part of a narrative rarely works as standalone 
reference.

Test: Could someone read this atom in isolation, months later, and fully 
understand the concept?
</atoms>

<output>
Edit files in place. When the user approves a change, update the actual
molecule or atom file directly.

For new atoms (extracted from molecule or created fresh), create the file
in the same folder as the molecule.

After each change, confirm what was modified. The user can continue refining
or stop at any point.
</output>