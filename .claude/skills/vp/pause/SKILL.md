name: vp-pause
description: Save session state to vault's RESUME.md

---

Pause the current session by saving context for a future agent.

<location>
Write `RESUME.md` inside the working directory: `_working/RESUME.md`
Create `_working/` if it doesn't exist.
</location>

<format>
```markdown
# Resume: [Brief task description]

## Done
What was accomplished this session. Bullet points.

## State
Current status — file changes, structure, anything the next agent needs to see.

## Next
The single immediate next action. One sentence. Not a task list.

## Context
Decisions made, user preferences, gotchas, or guidelines that affect how to continue.
```
</format>

<rules>
- Keep it short. If a section needs more than 5 lines, you're over-explaining.
- "Next" must be singular and actionable.
- Don't include reasoning or history — just what's needed to continue.
- If RESUME.md already exists, overwrite it completely.
</rules>
