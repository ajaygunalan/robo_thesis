name: vp-resume
description: Resume work from vault's RESUME.md

---

Resume a paused session by reading saved context.

<process>
1. Read `_working/RESUME.md`
2. Summarize to user: what was done, what's next
3. Delete the RESUME.md file (prevents stale state)
4. Ask: "Continue with [Next action]?" — let user confirm or redirect
</process>

<rules>
- Always delete `_working/RESUME.md` after reading — next pause will create fresh state
- If no RESUME.md exists in `_working/`, tell user "Nothing to resume"
- Don't start working until user confirms direction
</rules>
