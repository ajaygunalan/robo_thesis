---
name: distill
description: Transform source note (pdf/markdown/text) into molecule + atoms for Zettelkasten
---


<purpose>
This system exists for efficient revision. After months away from material, you should be able to read only the molecule and have your understanding restored—without returning to the source. Atoms exist for selective depth: if you need to refresh a specific concept, you read that atom alone. If not, you skip it entirely.

The goal is to minimize re-reading while maximizing retention.
</purpose>


<input>
The user provides:
- A topic name (e.g., "geo_ch3", "backprop")
- A source to distill:
  - PDF: research paper, lecture slides, book chapter
  - Markdown: notes, documentation, any text
  - `learn_<source>.md` in the target folder: output of `/vp-learn`
- A target folder where the material belongs (e.g., `_geometric_algebra/chapter_3/`)

Output goes to `distill_<source>.md` in the target folder.
</input>

<goal>
Transform the source into molecules and atoms.

The molecule captures the essence of the source—what it teaches, synthesized. The atoms provide detailed reference for specific concepts when deeper understanding is needed.

Someone should be able to read only the molecule and understand what the source document conveys. The atoms exist for when they want more depth on a particular concept.
</goal>

<molecules>
A molecule is the synthesized essence of a topic. If the source is a lecture, chapter, or paper, the molecule is what that source teaches, distilled into readable prose.

A molecule conveys:
- What problems or questions the topic addresses
- What the key ideas are and why they matter
- How the ideas relate to each other
- The narrative arc—how the topic builds from problem to solution

Write the molecule as flowing prose with `[[wikilinks]]` to atoms embedded mid-sentence. The links offer optional depth. The molecule must make sense without clicking any links.

Test: Can someone read this molecule and understand what the source teaches, without reading the source or clicking any links?
</molecules>

<atoms>
An atom is a detailed, self-contained explanation of one concept. It exists for readers who want full depth on something the molecule mentions.

An atom includes:
- The intuition: what problem does this concept solve?
- The mechanism: how does it work, in detail?
- The formalization: formulas, algorithms, diagrams that define it precisely

An atom should be complete. Someone reading it should fully understand and be able to apply the concept.

Test: Could someone learn this concept thoroughly from this atom alone?
</atoms>

<process>
1. Read the source and identify its core narrative: what question does it answer, and how?
2. Draft the molecule as synthesis—what does this source teach? Embed [[wikilinks]] for concepts where a reader might want depth.
3. Review your wikilinks: these are your atom candidates. Aim for 4–6. If more, your molecule may be covering too much territory (split into sub-molecules). If fewer, check whether the concepts are truly distinct.
4. Write atoms in the order they appear in the molecule. Each atom should be readable in isolation, months later.
5. Write the output to `distill_<source>.md` in the target folder and ask for feedback.
6. Iterate until satisfied:
   - User reviews distill.md and provides feedback (e.g., "split atom X", "molecule narrative is unclear", "merge these two atoms")
   - Revise and update distill.md
   - Repeat until user approves
7. When user is satisfied, remind them to run `/vp-split <topic>` to create individual files.
</process>

<structure>
One molecule per coherent source or topic. If a source covers multiple distinct areas, create a top-level molecule linking to sub-molecules.

One atom per concept that someone might want to understand in full depth. If the molecule mentions an idea and a reader might ask "but how exactly does that work?"—that idea needs an atom.

A molecule links 4–6 atoms. This range reflects cognitive scope: fewer atoms often means the molecule is too shallow or atoms too broad; more atoms usually means the molecule covers too much territory and should split.
</structure>

<example>
Example molecule fragment:

The core insight of backpropagation is that we can compute gradients efficiently by working backward through the network. Rather than computing how each weight affects the final loss directly, we use the [[chain_rule]] to decompose the problem: each layer only needs to know how its output affects the layers downstream. This requires caching [[forward_pass]] activations, which creates the memory-compute tradeoff that dominates modern training.
</example>

<output>
Write to `distill_<source>.md` in the target folder. Each note starts with `## filename` as H2 heading.

Molecule filenames: `_lowercase_name`
Atom filenames: `lowercase_name`

Write molecules as synthesis—clear, condensed, complete. Write atoms as thorough reference material.

This is an iterative process. After writing, ask: "Review distill.md. What would you like to change?" Update in place based on feedback until the user is satisfied, then prompt them to run `/vp-split <topic>`.
</output>