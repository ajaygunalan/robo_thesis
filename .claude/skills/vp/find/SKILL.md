---
name: find
description: Search the vault for a concept and locate all related notes
---

Search the vault to find where a specific concept lives. The user knows they studied something but doesn't remember which file it's in. Find every note that discusses, explains, or meaningfully relates to the concept — even if the exact phrase never appears.

## Strategy

Search in three passes, narrowing progressively:

1. **Pre-search.** Generate 3-5 related terms (from Semantic Search below). Then run:
   `python3 .claude/scripts/vault_grep.py "term1" "term2" "term3" ...`
   This returns all files with match scores (content + wikilink weighted).

   Also check `.claude/vault_graph.json` if available — the edges array shows
   every file that links to `[[concept]]` without any grep needed.

2. **Read top candidates.** Read the highest-scoring files from the grep results.
   Spawn subagents for parallel reading if more than 3 files.
   Also sample a few files from folders that seem unrelated, in case the concept is embedded inside a broader topic with a different name.

3. **Confirm and contextualize.** For each file that contains relevant content, note what it says about the concept — is it a central topic or a passing mention? Is it a high-level overview or a detailed explanation?

## Semantic Search

Before grepping, generate 3-5 related terms and include them ALL in the search pass:
- **Synonyms:** different names for the same thing (value function ↔ cost-to-go)
- **Broader topics:** categories that contain it (reinforcement learning for TD learning)
- **Specific instances:** concrete examples (SARSA, Q-learning for TD methods)
- **Cross-domain equivalences:** same concept in another discipline's language (outer product ↔ wedge product)
- **Descriptions:** the mechanism without the name

Example: searching "temporal difference learning" also greps for TD error, bootstrapping, value estimation, Bellman equation, SARSA, Q-learning, TD(λ).

A file is relevant if someone reading it would learn something about the concept, even indirectly.

## Output

Report what you found in four categories:

**Defines** — files where the concept is the central topic (atom named for it, or main heading):
- filepath: what the file covers

**Uses** — files that reference or depend on this concept (wikilinks to it, uses it in derivations):
- filepath: how the concept is used here

**Relates** — files that discuss closely related ideas without directly covering the concept:
- filepath: what the related idea is and why it connects

**Gaps** — missing pieces discovered during the search:
- `[[concept]]` is referenced in wikilinks but no file exists
- A related concept is frequently mentioned without a dedicated atom
- An expected connection between two existing files is missing

If you found nothing, say so clearly and suggest what search terms or related concepts the user might try instead.

## Rules

- Only read .md files. Skip PDFs, images, and other binary files.
- Use subagents to read files in parallel when scanning multiple files.
- Always grep for `[[concept]]` wikilinks alongside content grep — nearly free and leverages the existing link graph.
- Don't just grep for keywords. Use the synonym/term expansion from Semantic Search to catch matches across naming conventions.
- If the vault is very large, prioritize folders and filenames that signal relevance before reading contents.
- Always report filepaths relative to the vault root so the user can find them in Obsidian.
