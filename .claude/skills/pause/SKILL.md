---
name: pause
description: Pause the program without penalty. Use when the learner types /pause.
argument-hint: "[reason / expected return]"
disable-model-invocation: true
---

Pause the program.

1. Set `paused: true` and `paused_since: <today>` in `learner/profile.yaml`. Note the reason from `$ARGUMENTS` if given.
2. Note open work (issue in progress, PRs awaiting reply) in `learner/journal.md` so `/resume` can rebuild context. Tell the learner exactly where they left off.
3. Add a line to `company/TIMELINE.md`. No incidents or planned scope changes fire while paused.
4. Remind the learner that pauses carry no penalty and `/resume` starts with a short re-entry sprint.
