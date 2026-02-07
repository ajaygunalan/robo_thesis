---
name: distill
description: Transform source note (pdf/markdown/text) into molecule + atoms for Zettelkasten
---

## Input

The user provides:
- A topic name (e.g., "geo_ch3", "backprop")
- A source to distill:
  - PDF: research paper, lecture slides, book chapter
  - Markdown: notes, documentation, any text
  - `learn_<source>.md` in the target folder: output of `/vp-learn`
- A target folder where the material belongs (e.g., `_geometric_algebra/chapter_3/`)

Output goes to `distill_<source>.md` in the target folder.

## Molecules

Write the molecule as flowing prose with `[[wikilinks]]` to atoms embedded mid-sentence. The links offer optional depth. The molecule must make sense without clicking any links.

One molecule per coherent source or topic. If a source covers multiple distinct areas, create a top-level molecule linking to sub-molecules.

## Atoms

One atom per concept that someone might want to understand in full depth. If the molecule mentions an idea and a reader might ask "but how exactly does that work?" — that idea needs an atom.

## Process

1. Read the source and identify its core narrative: what question does it answer, and how?
2. Draft the molecule as synthesis — what does this source teach? Embed [[wikilinks]] for concepts where a reader might want depth.
3. Review your wikilinks: these are your atom candidates. Aim for 4–6. If more, your molecule may be covering too much territory (split into sub-molecules). If fewer, check whether the concepts are truly distinct.
4. Write atoms in the order they appear in the molecule. Each atom should be readable in isolation, months later.
5. Write the output to `distill_<source>.md` in the target folder and ask for feedback.
6. Iterate until satisfied:
   - User reviews distill.md and provides feedback (e.g., "split atom X", "molecule narrative is unclear", "merge these two atoms")
   - Revise and update distill.md
   - Repeat until user approves
7. When user is satisfied, remind them to run `/vp-split <topic>` to create individual files.

## Example

Example molecule fragment:

The core insight of backpropagation is that we can compute gradients efficiently by working backward through the network. Rather than computing how each weight affects the final loss directly, we use the [[chain_rule]] to decompose the problem: each layer only needs to know how its output affects the layers downstream. This requires caching [[forward_pass]] activations, which creates the memory-compute tradeoff that dominates modern training.

## Output

Write to `distill_<source>.md` in the target folder. Each note starts with `## filename` as H2 heading.

Molecule filenames: `_lowercase_name`
Atom filenames: `lowercase_name`

Write molecules as synthesis — clear, condensed, complete. Write atoms as thorough reference material.

This is an iterative process. After writing, ask: "Review distill.md. What would you like to change?" Update in place based on feedback until the user is satisfied, then prompt them to run `/vp-split <topic>`.
