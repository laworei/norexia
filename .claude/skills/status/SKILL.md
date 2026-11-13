---
name: status
description: Write a status dashboard to reports/ (level, competency heatmap, findings trends, first-pass approval, review rounds, cycle time, hints, flashcards, incidents, reading). Use when the learner types /status.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh issue list *) Bash(gh pr list *)
---

Build the learner's dashboard.

1. Run `python3 scripts/status.py`; it computes the numbers from `learner/*` and writes `reports/status-<date>.md`.
2. Open the generated file and add a short "What this says" section in plain language: 3 strengths, 3 gaps, and one recommended focus for the next sprint. Be honest.
3. Show the learner the summary in chat (not the whole file) and link the report.

Do not edit any owned path.
