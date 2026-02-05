---
name: find
description: Search the vault for a concept and locate all related notes
---

<purpose>
You are searching an Obsidian vault (a folder of markdown files, possibly nested in subdirectories) to find where a specific concept lives. The user knows they studied something but doesn't remember which file it's in.

Your job is to find every note that discusses, explains, or meaningfully relates to the concept—even if the exact phrase never appears.
</purpose>

<strategy>
Search in three passes, narrowing progressively:

1. **Map the territory.** List all subdirectories and markdown filenames in the vault. Use your understanding of the concept to identify which folders and files are likely relevant based on their names alone. This is a cheap first pass—names are clues, not answers.

2. **Read promising files.** For files and folders that look relevant, spawn multiple subagents to read them in parallel. Don't read sequentially—use subagents to cover ground fast. Also sample a few files from folders that seem unrelated, in case the concept is embedded inside a broader topic with a different name.

3. **Confirm and contextualize.** For each file that contains relevant content, note what it says about the concept—is it a central topic or a passing mention? Is it a high-level overview or a detailed explanation?
</strategy>

<what_counts_as_relevant>
Use your knowledge of the concept to search semantically, not just by keyword. For example, if the user asks for "temporal difference learning," you should also recognize:
- Related terminology (TD error, bootstrapping, value estimation, Bellman equation)
- Broader topics that contain it (reinforcement learning, model-free methods)
- Specific instances of it (SARSA, Q-learning, TD(λ))
- Descriptions of the mechanism without using the name

A file is relevant if someone reading it would learn something about the concept, even indirectly.
</what_counts_as_relevant>

<output>
Report what you found in this format:

**Direct matches** — files where the concept is a central topic:
- filepath: what the file covers and how it relates to the concept

**Related notes** — files where the concept appears as part of a broader topic:
- filepath: what the broader topic is and how the concept fits in

**Possible connections** — files that discuss closely related ideas:
- filepath: what the related idea is and why it might be useful

If you found nothing, say so clearly and suggest what search terms or related concepts the user might try instead.
</output>

<rules>
- Only read .md files. Skip PDFs, images, and other binary files.
- Use subagents to read files in parallel when scanning multiple files.
- Don't just grep for keywords. Use your understanding of the concept to find semantic matches.
- If the vault is very large, prioritize folders and filenames that signal relevance before reading contents.
- Always report filepaths relative to the vault root so the user can find them in Obsidian.
</rules>