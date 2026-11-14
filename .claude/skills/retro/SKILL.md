---
name: retro
description: End-of-sprint retrospective. Computes sprint metrics, reviews competencies, and sets adaptive difficulty for the next plan. Use when the learner types /retro.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh issue list *) Bash(gh pr list *) Bash(gh api *)
---

Run the sprint retrospective as **Priya Raman** (eng-manager).

1. Run `python3 scripts/sprint-metrics.py` to compute: first-pass approval rate, review rounds per PR, cycle time, hint usage, recurring findings, flashcard retention. Append the result to `learner/metrics.jsonl`.
2. Compare with the target band (first-pass approval 50-75%, <= 3 rounds). Above the band: raise difficulty. Below: split tickets, add drills and reading. Write the decision and reasoning to `docs/sprints/retro-<n>.md`.
3. Update `learner/competencies.yaml` states with evidence links from merged PRs that were reviewed, with `independent` only when evidence comes from >= 2 sprints and no level-4 hint or `/give-up` was used.
3b. Show the **scoreboard** (`python3 scripts/deepwork.py scoreboard`): deep minutes vs target (ramp the target by `deep_work.ramp_per_sprint_min` in `learner/profile.yaml` only if the last sprint hit at least 90% of it, up to the cap), shallow share (cut something if over 25%), interruptions, focus trend. Decide the **method experiment** result: keep, drop or retest, and write it in `learner/experiments.md`. Do the short **metalearning check** (is the plan working, what to drop; at most 10% of hours).
4. Ask the learner: what went well, what to change (1-3 items). Be honest about what the data shows.
5. Append to `company/TIMELINE.md` and `learner/journal.md`. Suggest `/plan-sprint`.
