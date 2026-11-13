---
name: stuck
description: Start the stuck protocol for an open issue. Diagnostic questions first, then one hint at a time. Use when the learner types /stuck <issue>.
argument-hint: <issue-number>
disable-model-invocation: true
context: fork
agent: help-desk
allowed-tools: Bash(gh issue view *) Bash(git log *) Bash(git diff *)
---

The learner is stuck on issue **$ARGUMENTS** in `laworei/norexia`. Run the stuck protocol from `handbook/hint-ladder.md`.

1. Read the issue (`gh issue view $ARGUMENTS`), the learner's profile, and prior hints for this issue in `learner/hints.jsonl` (start from the next level up from the last hint).
2. Check the timebox. Ask the diagnostic questions. If the learner has already answered them in the invoking message, skip to the hint.
3. Give exactly one hint at the lowest level that could unblock. Cite a book section from `library/reading-map.md` when available. Stop.
4. Log it in `learner/hints.jsonl`.

No solution code for the ticket. No level 5.
