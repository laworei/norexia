---
name: resume
description: Resume after a pause with a short re-entry sprint built on retrieval of recent work. Use when the learner types /resume.
disable-model-invocation: true
allowed-tools: Bash(gh issue *) Bash(gh pr *) Bash(python3 scripts/*)
---

Resume the program.

1. Read `learner/profile.yaml` (`paused_since`) and the last journal entry. Compute the length of the pause.
2. Set `paused: false`. Do not penalize the pause in metrics (mark the gap as `paused` in `learner/metrics.jsonl`).
3. Plan a **short re-entry sprint** (roughly half the normal capacity): retrieval of the last 2 sprints' work (closed-book mini tasks and explain-backs), a flashcard backlog session, and one small delivery ticket. Use the `/plan-sprint` flow and show previews first.
4. Welcome the learner back warmly, and say specifically what they had mastered when they left.
