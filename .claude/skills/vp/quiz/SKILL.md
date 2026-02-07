---
name: quiz
description: Socratic revision — test understanding on existing molecules and atoms
---

Test the user's understanding of material they've already distilled. All output goes to a quiz file so LaTeX renders in Obsidian.

## Evidence Grounding

Every question must trace to a specific atom or molecule. Read the target material before generating questions. Never quiz on material not in the vault — flag it as a gap instead.

When giving feedback, cite the source:
- **Correct:** "Confirmed — this matches [[atom]], which states..."
- **Partial:** "You've got the direction right. [[atom]] clarifies that..."
- **Wrong:** "Let's revisit. According to [[atom]]..."
- **Gap:** "Your vault doesn't cover this yet — consider creating an atom."

## Input

The user provides:
- A molecule or folder path
- Optionally: specific concepts to focus on, difficulty level (conceptual, computational, edge cases)

Create `quiz_<source>.md` in the same folder. Overwrite if it exists (each session is fresh).

## Process

One question at a time, Socratic style:
1. State the concept being tested
2. Ask a question that requires understanding, not recall
3. Wait for the user's answer
4. If correct: confirm, probe deeper. If partial: acknowledge what's right, guide toward what's missing. If wrong: ask guiding questions — don't give the answer.
5. Move on only when they understand or ask for the answer

Write each question to the quiz file with: question, source atom, user's answer, feedback, and status (understood / partial / needs review).

At session end: write a summary (concepts tested, strong areas, review areas, gaps found, suggested next steps).
