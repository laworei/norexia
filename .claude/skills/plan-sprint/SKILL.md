---
name: plan-sprint
description: Plan the next sprint with the eng-manager and product-manager. Dry-run first; creates GitHub issues only after the learner approves. Use when the learner types /plan-sprint.
argument-hint: "[--create]"
disable-model-invocation: true
allowed-tools: Bash(gh issue *) Bash(gh label *) Bash(gh api *) Bash(python3 scripts/*)
---

Plan the next sprint.

1. Read `learner/profile.yaml`, `learner/competencies.yaml`, `learner/metrics.jsonl`, `learner/findings.jsonl`, `learner/hints.jsonl`, `learner/journal.md`, `company/state.yaml`, the previous sprint's retro, and `library/reading-map.md`.
2. Delegate to the **eng-manager** for capacity (declared hours x 0.7), the sprint mix for the learner's level (`docs/PROGRAM.md`), adaptive difficulty, and the drill rule (subcode with >= 2 findings in 30 days gets a drill ticket). Delegate to the **product-manager** for business-language framing (and, from L2, at most one planned mid-sprint scope change, sealed in `.sealed/sprint-<n>.md`).
3. Produce **issue previews** with every field of `handbook/templates/issue.md` filled: type, level, business context, requirements and acceptance criteria shaped by level, competency subcodes, estimate, reading pointer (book + chapter from the reading map), definition of done, constraints (closed-book?), owning persona. Interleave competencies; never a single-topic sprint. Respect WIP limit 1.
3b. Add the method layer (`handbook/learning-method.md`): a **Wildly Important Goal** for the sprint (one sentence, a lag measure with a number); **lead measures** (deep minutes target from `learner/profile.yaml`, retrieval sessions, drills, flashcard sessions); at least one **drill** chosen proactively or from findings (name the drill type); a **spaced-regression** item (a competency not exercised for ~6 weeks); a **free-recall / test-before-study** step on every reading pointer; a **north-star project** increment that runs end to end; and ONE **method experiment** (hypothesis, change, measure) to record in `learner/experiments.md`. Metalearning stays under 10% of hours. Mark each ticket **deep** or **shallow** and keep shallow under 25%.
4. Save the plan to `docs/sprints/sprint-<n>.md` including the difficulty reasoning and the items above.
5. Show the previews. **Create nothing on GitHub** unless the learner approves. With `--create` AND an explicit "yes", create the issues, labels, milestone and board entries with `gh`.

Never write an issue's solution or Go code into a ticket.
