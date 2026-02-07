---
name: learn
description: Study source material through interactive Q&A before distilling
---

Tutor the user through source material using Socratic Q&A. All substantive content goes to a learning file (not the terminal) so LaTeX renders in Obsidian.

<input>
The user provides:
- A source file (PDF, slides, or markdown)
- A target folder (e.g., `_geometric_algebra/chapter_3/`)
- Optionally: specific sections to focus on

Create `learn_<source>.md` in the target folder. Append if it already exists.
</input>

<process>
1. On first session, create `progress_<source>.md` with a table of sections from the source (columns: Section, Status, Confidence, Key Gaps). On subsequent sessions, read it first, summarize where they left off, ask where to pick up.

2. Before each new section, grep the vault for existing atoms on the upcoming concepts. Link to them instead of re-explaining.

3. Work through material Socratic style: explain the core idea, ask the user to explain it back or answer a probing question, guide with follow-ups if wrong — don't just give the answer. Move on only when they understand.

4. Write each section to the learning file with: explanation, discussion (Q&A exchange), key takeaways, and an insight log (key insight, connections to existing atoms, open questions, confidence level).

5. When the user asks about something outside the source, use a background subagent to research it and integrate findings at natural break points.

6. At session end: summarize what was covered, update `progress_<source>.md`, note remaining sections. The learning file becomes input for `/vp-distill`.
</process>
