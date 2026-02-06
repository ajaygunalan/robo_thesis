# Why Jujutsu Matters

Git is fine when all you do is `git add`, `git commit`, `git push`. The pain starts the moment you need anything beyond that: switching tasks mid-work, cleaning up messy commits before a code review, fixing something in an old commit, or recovering after you broke something. These operations exist in Git, but they're buried behind cryptic commands, special modes, and fragile state.

Jujutsu (jj) is a Git-compatible version control system built to make these painful operations simple. Your repo stays Git. Your remotes stay Git. Your teammates don't need to know you're using it. Under the hood, jj changes how you interact with commits: your working directory is always a commit, every operation is logged and undoable, and commits have stable IDs that don't change when you rewrite history.

This post walks through seven real workflow problems, shows the Git pain, and demonstrates how jj solves each one.

---

## 1. The Pointless Ceremony

You're adding a feature. You edit files, run tests, everything works.

**Git:**

```bash
git add .
git commit -m "Add feature"
```

Every single time. `git add .` then `git commit`. Two commands for one action:

```
┌─────────────┐    git add    ┌─────────────┐   git commit   ┌─────────────┐
│   Working   │ ───────────▶  │   Staging   │ ────────────▶  │   Commit    │
│  Directory  │               │    Area     │                │   History   │
└─────────────┘               └─────────────┘                └─────────────┘
     your                        limbo                          saved
    changes                      state                          
```

The staging area exists for selective commits, but almost everyone just runs `git add .` because tracking what's staged vs unstaged is extra mental overhead.

**jj:**

```bash
# Edit files...
jj describe -m "Add feature"
jj new
```

```
┌─────────────────────────────────┐   jj new    ┌─────────────┐
│   Working Directory = Commit    │ ──────────▶ │ New Empty   │
│   (always saved automatically)  │             │   Commit    │
└─────────────────────────────────┘             └─────────────┘
        your changes ARE                         ready for
         the commit                              next task
```

`jj describe` sets the commit message for what you're working on. `jj new` creates a new empty commit on top of the current one—it's how you say "I'm done with this commit, start a fresh one."

**Why this works:** In jj, your working directory *is* a commit (called the "working-copy commit"). You're not moving changes through stages. You're just naming the commit you were already editing, then starting the next one. There's no limbo state between "changed" and "committed."

What about selective commits? Use `jj split`—interactively choose what stays in the current commit and what moves to a new one. It's there when you need it, not forced on every commit.

---

## 2. The Emergency Hotfix

You're deep in feature work. Suddenly, production breaks. You need a hotfix *now*.

**Git:**

```bash
git stash
git checkout main
git checkout -b hotfix
# ...fix the bug...
git add . && git commit -m "Hotfix"
git push
git checkout feature-branch
git stash pop              # Hope nothing conflicts
```

`git stash` takes your uncommitted changes and hides them in a separate storage area, leaving your working directory clean. `git stash pop` retrieves them later. It's Git's workaround for "I need to switch branches but I'm not ready to commit."

The problem: stashes accumulate, get forgotten, and sometimes conflict when you pop them. The alternative—a "Work In Progress" commit—pollutes your history.

**jj:**

In jj, your working directory is always a commit (called the "working-copy commit"). Your half-done feature is already saved as a commit with a change ID—let's say `kxqm`.

Here's what your repo looks like:

```
○ kxqm (your feature)  ◀── you are here
│
○ C  ← "main" (this is just a label pointing to C)
│
○ B
│
○ A
```

Important: `main` is not a branch you're "on." It's a **bookmark**—just a label pointing to commit C. Think of it like a sticky note attached to that commit.

Now you need a hotfix. The hotfix should start from C (the production code), not from your feature.

```bash
jj new main
```

This says: "Create a new empty commit. Its starting point should be wherever the `main` bookmark points." 

Now your repo looks like this:

```
○ kxqm (your feature)
│
│ ○ yprt (new empty commit)  ◀── you are here now
│/
○ C  ← "main"
│
○ B
│
○ A
```

Your feature commit (`kxqm`) is still there, untouched. You've just created a new commit `yprt` that also starts from C. The graph forks—that's fine. In jj there's no "branch" to manage, just commits.

```bash
# ...fix the bug...
jj describe -m "Hotfix"
jj bookmark set hotfix -r @
jj git push --allow-new
```

Hotfix done. Now go back to your feature:

```bash
jj edit kxqm
```

```
○ kxqm (your feature)  ◀── you are here again
│
│ ○ yprt (hotfix)  ← "hotfix"
│/
○ C  ← "main"
│
○ B
│
○ A
```

You're back exactly where you were. Your feature code is there. No stash. No conflicts.

**Two things to understand:**

1. **What are these forks called?** They're just commits. No names needed. `kxqm` is a commit. `yprt` is a commit. The fork in the graph doesn't require a "branch name"—it's just the shape of history. You only add a bookmark (like `hotfix`) when you need to push somewhere.

2. **Is the hotfix code in your feature?** No. They're independent commits that both start from C. Your feature (`kxqm`) doesn't contain the hotfix. If you want the hotfix code in your feature, you'd rebase:

```bash
jj rebase -r kxqm -d yprt    # Move feature to start from hotfix (yprt) instead of C
```

Now your feature would include the hotfix changes.

**Why this works:** In Git, uncommitted work has no permanent home, so you must hide it somewhere before switching. In jj, all work lives in commits. Switching context just means creating a new commit somewhere else, then coming back later.

---

## 3. Trying Things Without Branch Clutter

You want to experiment with two different approaches to a problem.

**Git:**

```bash
git checkout -b experiment-a
# ...try approach A...
git add . && git commit -m "WIP A"
git checkout main
git checkout -b experiment-b
# ...try approach B...
git add . && git commit -m "WIP B"
# Now you have two branches to clean up later
```

Every experiment requires a branch name. Branches accumulate. You end up with `experiment-a`, `experiment-a-v2`, `experiment-final`, `experiment-final-FINAL`.

**jj:**

```bash
jj new                     # Start experimenting
# ...try approach A...
jj describe -m "Approach A"
```

Now you want to try a different approach. But you don't want to build on top of A—you want to start fresh from where you were before A.

In jj, `@` means "current commit" and `@-` means "the commit before current." So:

```bash
jj new @-                  # Create new commit based on the commit before current
# ...try approach B...
jj describe -m "Approach B"
```

This creates a new commit that starts from the same place A started, effectively giving you a parallel experiment:

```
            ○ kxqm "Approach A"
           /
○ ────── ○ (starting point)
           \
            ○ yprt "Approach B"  ◀── you are here
```

```bash
jj log                     # Both A and B are visible
```

Both experiments exist as commits. No branch names needed. Keep the one that works, abandon the other with `jj abandon <id>`.

**Why this works:** In jj, you're never "on a branch"—you're always on a commit. Git panics about "detached HEAD" because it might lose track of commits not attached to a branch. jj tracks all commits automatically, so branches (called "bookmarks" in jj) are only needed when pushing to a remote.

---

## 4. Undoing Mistakes

You ran a command and broke something.

**Git:**

```bash
git reflog
# 5a3d2f1 HEAD@{0}: rebase finished
# 8b2c4e3 HEAD@{1}: rebase: checkout main
# 1f4a6b7 HEAD@{2}: commit: Add feature
# ...50 more lines...
git reset --hard HEAD@{2}  # Hope you picked right
```

Reflog exists, but it's cryptic. It shows snapshots, not operations. Figuring out which entry to restore requires archaeology.

**jj:**

```bash
jj undo                    # Revert last operation
```

That's it. Made a bigger mess? See the full history:

```bash
jj op log                  # Every operation, labeled
jj op restore <op-id>      # Jump to any past state
```

```
jj op log shows:
┌────────────────────────────────────────┐
│ @ 3f2a  2 min ago   squash             │ ◀── current state
│ ○ 8b1c  5 min ago   describe           │
│ ○ 4d3e  10 min ago  new                │
│ ○ 1a2b  15 min ago  commit             │
└────────────────────────────────────────┘
         jj undo → goes back to 8b1c
         jj op restore 4d3e → goes back to 4d3e
```

**Why this works:** jj records atomic snapshots of every operation—not just commits, but rebases, squashes, abandons, everything. You're not searching through commit hashes; you're looking at a log of *actions*.

---

## 5. Editing an Old Commit

A reviewer points out a typo in a commit from three commits ago.

**Git:**

```bash
git rebase -i HEAD~4
# Editor opens. Mark the commit as 'edit'.
# Save and close.
# Git stops at that commit.
# ...fix the typo...
git add .
git commit --amend
git rebase --continue
# If conflicts: fix them NOW or abort everything
```

You're in a special "rebasing" state. No other work is possible until you finish or abort. If a conflict arises, you must resolve it immediately.

**jj:**

There are three ways to do this, depending on the situation:

**Option A: Go to the commit and fix it directly**

```bash
jj edit kxqm               # Switch to that commit
# ...fix the typo...
jj new                     # Done, move on
```

```
BEFORE:                           AFTER jj edit kxqm:
                                  
○ nslq (you are here)             ○ nslq
│                                 │
○ mzln                            ○ mzln
│                                 │
○ kxqm  ← typo here               ○ kxqm  ◀── you are here, fix it
│                                 │
○ main                            ○ main
```

Your edit is now part of that commit. If it conflicts with later commits, jj marks them as conflicted but doesn't block you. Resolve when you're ready.

**Option B: Fix it now, then push the fix into the right commit**

```bash
# You're working on the current commit
# ...fix the typo in the file...
jj squash --into kxqm path/to/file
```

```
Your fix in current commit → automatically moves into kxqm

○ nslq (fix here)                 ○ nslq (fix gone from here)
│                    squash       │
○ mzln               ─────▶       ○ mzln
│                                 │
○ kxqm                            ○ kxqm (fix is now here!)
```

This takes your changes to that file and moves them into the specified commit.

**Option C: Let jj figure out where the fix belongs**

```bash
# ...fix things across multiple files...
jj absorb
```

`jj absorb` looks at each changed line, finds which earlier commit last touched that line, and automatically moves the fix there. Ambiguous changes stay where they are.

**Why this works:** jj identifies commits by a "change ID" (like `kxqm`) that stays constant even when the commit's contents change. You don't need to count backwards (`HEAD~4`) or recalculate after each operation. The ID you saw in `jj log` is still valid.

---

## 6. Cleaning Up History Before Pushing

You made 10 messy commits during development. Before pushing, you want to combine them into 3 clean commits.

**Git:**

```bash
git rebase -i HEAD~10
# Editor opens. Change 'pick' to 'squash' for commits you want to combine.
# Save. Write new message. 
# History changed—commit positions shifted.
# Repeat for next group, but now HEAD~6 isn't what it was before.
```

Each interactive rebase changes the commit graph. The range for your next squash depends on what you just did. You're tracking state in your head.

**jj:**

```bash
jj log                     # Note change IDs: kxqm, yprt, mzln, nslq...
jj squash -r yprt          # Merge yprt into the commit before it
jj squash -r mzln          # Merge mzln into the commit before it
jj squash -r nslq          # Merge nslq into the commit before it
```

```
BEFORE:                      AFTER jj squash -r yprt:

○ nslq "fix tests"           ○ nslq "fix tests"
│                            │
○ mzln "cleanup"             ○ mzln "cleanup"
│                            │
○ yprt "typo"                (yprt merged into kxqm)
│                    ───▶    │
○ kxqm "add feature"         ○ kxqm "add feature" (now includes typo fix)
│                            │
○ main                       ○ main
```

`jj squash` takes a commit and folds it into the commit that came before it. The change IDs you noted at the start remain valid for all operations.

**Why this works:** Change IDs don't move when you rewrite history. Git's SHA hashes change with every rebase because they're computed from content. jj's change IDs are assigned once and never change. This makes multi-step history manipulation stateless.

---

## 7. Dealing with Conflicts Later

You rebase onto main and hit a conflict.

**Git:**

```bash
git rebase main
# CONFLICT in file.py
# Fix it NOW or:
git rebase --abort
```

```
Git: BLOCKED STATE
┌─────────────────────────────────────────┐
│  ⚠️  REBASING - repository locked       │
│                                         │
│  You cannot:                            │
│  • Switch branches                      │
│  • Work on other things                 │
│  • Leave and come back tomorrow         │
│                                         │
│  You must: resolve NOW or abort         │
└─────────────────────────────────────────┘
```

The repository is in a "rebasing" state. You can't switch to other work. You can't leave and come back tomorrow. Fix it or abort.

**jj:**

```bash
jj rebase -d main
# jj notes: commit nslq has conflicts
```

```
jj: CONFLICT IS JUST DATA

○ nslq (has conflicts)  ← marked, but exists
│
○ main

You can:
• Work on other commits
• Come back tomorrow
• Do anything else

The conflict is stored IN the commit,
not as a repository state.
```

That's it. The rebase completes. The conflicted commit is marked, but you can keep working on other things. When ready:

```bash
jj edit nslq               # Go to conflicted commit
# ...resolve conflicts...
jj new                     # Done
```

**Why this works:** jj separates *detecting* a conflict from *resolving* it. Conflicts are stored as data in the commit, not as a blocking repository state. The conflicted commit exists—it just won't compile until you fix it.

---

## Conclusion

If all you ever do is `git add`, `git commit`, `git push`, jj won't change your life. But if you ever rewrite commits for code review, juggle multiple tasks, fix mistakes in old commits, or want a real undo button—jj removes the ceremony and state-tracking that makes these operations painful in Git.

The core wins come from three design choices: your working directory is always a commit (no staging limbo), changes have stable IDs that survive rewrites (no recounting `HEAD~N`), and every operation is logged (real undo, not reflog archaeology). These aren't cosmetic improvements. They change what feels safe to attempt.

Try it on a small project. Run `jj git init --colocate` in an existing repo. Your Git history stays intact. If you don't like it, delete the `.jj` folder and you're back to pure Git. But you probably won't go back.

---

**Resources:**
- [Official docs](https://docs.jj-vcs.dev/)
- [Steve Klabnik's tutorial](https://steveklabnik.github.io/jujutsu-tutorial/)
- [Git comparison](https://docs.jj-vcs.dev/latest/git-comparison/)
