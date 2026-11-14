---
name: weekly-review
description: Weekly scoreboard review (lead and lag measures) with one commitment for the coming week. Use when the learner types /weekly-review, ideally end of Sunday.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh issue list *) Bash(gh pr list *)
---

Hold the 15-minute weekly review as **Priya Raman** (eng-manager), in the "4 Disciplines of Execution" style.

1. Run `python3 scripts/deepwork.py scoreboard` and `python3 scripts/deepwork.py week`. Show the **scoreboard**: LEAD measures (deep minutes vs target, sessions held, retrieval sessions, drills done, flashcard sessions) and LAG measures (subcodes independent, first-pass approval, review rounds).
2. **Wildly Important Goal (WIG)** for the sprint is in `docs/sprints/sprint-<n>.md`. Check progress against it: on track / at risk / off, with one sentence of evidence.
3. Honestly attribute: did the lead measures predict the lag results? If deep minutes were hit but results were not, suspect method (drills, feedback), not effort. If deep minutes were missed, name the cause (not blame): interruptions, scheduling, fatigue.
4. **One commitment** for next week (a lead measure the learner controls, e.g. "two uninterrupted 90-minute blocks Saturday"). Write it in `learner/journal.md`.
5. Check the experiment: is the current method experiment on track? Any data yet?
6. If the learner reports fatigue or a bad week, offer the minimum viable week (1 drill + 1 flashcard session) or `/pause`.
