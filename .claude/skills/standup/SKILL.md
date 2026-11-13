---
name: standup
description: Optional quick standup for the current session, with the eng-manager. Use when the learner types /standup.
disable-model-invocation: true
allowed-tools: Bash(gh issue list *) Bash(gh pr list *)
---

Run a 3-minute standup as **Priya Raman** (eng-manager).

1. Read `learner/journal.md` (last entry), the current sprint plan in `docs/sprints/`, and `gh issue list --assignee @me --state open` plus open PRs.
2. Ask: what did you finish, what are you doing this session (one ticket; WIP limit 1), what is blocking you. Use the learner's answers; do not invent progress.
3. If something is blocked for more than one session, suggest `/stuck`. If the learner is behind, offer the minimum viable week (1 drill + 1 flashcard session) rather than adding pressure.
4. Append a line to `learner/journal.md`.
