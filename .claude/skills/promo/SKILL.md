---
name: promo
description: Start or evaluate a promotion: check readiness, schedule the practical exam, and review the promo packet with the promotion committee. Use when the learner types /promo.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh pr *) Bash(gh issue *)
---

Run the promotion process.

1. Compute readiness: `python3 scripts/promo-readiness.py` (coverage of required subcodes for the next level, trend over the last 2 sprints, exam status, outstanding gaps).
2. If not ready, say exactly what is missing and stop. No promotion on time served.
3. If ready for the exam, explain format and rules (timed, closed book: no AI, official docs only), generate the sealed exam under `.sealed/exams/<level>/`, and agree a time. The learner writes code in an owned path; Claude never does.
4. After the exam, grade honestly against the rubric. Then the learner writes the packet from `handbook/templates/promo-packet.md` into `learner/promo-packet.md`.
5. Delegate to the **promo-committee** (and the **architecture-panel** at L3->L4) to review the packet against the ladder, citing evidence. They may deny with a gap list and a 30-day plan.
6. On approval, follow `handbook/promotion-checklist.md` (profile, timeline, guardrails for the new level).
