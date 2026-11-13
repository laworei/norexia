---
name: give-up
description: Explicit escape hatch. Reveals the answer for an issue or sealed item, logs it as a help event, and schedules a retrieval card. Use only when the learner types /give-up <id>.
argument-hint: <issue-or-sealed-id>
disable-model-invocation: true
context: fork
agent: help-desk
allowed-tools: Bash(gh issue view *) Bash(gh issue comment *)
---

The learner explicitly invoked `/give-up $ARGUMENTS`. This is allowed; hiding it is not.

1. Confirm in one line what will happen: the answer is revealed, it is logged, the related subcodes become `assisted`, and a retrieval card is created. Proceed only if the invocation was explicit (it was).
2. Reveal the answer:
   - for an open ticket, explain the solution approach and the reasoning in prose and pseudocode. **Do not write Go into any owned path.** Showing the solution in chat is the sanctioned exception, and the learner implements it themselves;
   - for a sealed item, read `.sealed/` for that id and explain it.
3. Append to `learner/hints.jsonl`: `{"level":"give-up", ...}`. Mark the related subcodes in `learner/competencies.yaml` at most `assisted`.
4. Add 1-3 flashcards to `learner/flashcards.csv` for the concept.
5. Be kind. Say what to practise next.
