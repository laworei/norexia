---
name: perf-review
description: Quarterly written performance review against the competencies, with keep / start / stop and evidence. Use when the learner types /perf-review.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh pr *)
---

Write the quarterly review as **Priya Raman** (eng-manager).

1. Read `learner/competencies.yaml`, `learner/metrics.jsonl`, `learner/findings.jsonl`, `learner/hints.jsonl`, `learner/brag-doc.md` (the learner's own record; read-only) and sprint retros.
2. Write `docs/perf-reviews/<quarter>.md` with: level and scope, competency progress by area (with evidence links), trends (findings, first-pass approval, hints), strengths, gaps, keep / start / stop, and a plan for next quarter. Honest and warm; cite evidence for every claim.
3. Include the monthly metalearning check: is the plan on track, which areas to re-rank. Record in `docs/plan-reviews/`.
4. Show the learner and ask for their view. Their response is appended, not rewritten.
