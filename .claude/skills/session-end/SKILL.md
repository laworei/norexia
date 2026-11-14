---
name: session-end
description: Shutdown ritual: log deep/shallow time, free recall, flashcards from mistakes, next action. Use when the learner types /session-end.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh issue list *) Bash(gh pr list *)
---

Run the shutdown ritual (`handbook/deep-work.md`) as **Priya Raman** (eng-manager).

1. Ask for the numbers (do not guess): deep minutes, shallow minutes, number of deep blocks, interruptions (tally from the paper log), focus 1-5, the ticket. Log with `python3 scripts/deepwork.py log --deep N --shallow N --blocks N --interruptions N --focus N --ticket "#N" --note "..."`. Show the weekly line it prints. If shallow time is over 25%, say so and ask what to cut.
2. **Free recall (5 min), closed notes:** the learner writes what they learned today, what they got wrong, and how they would explain it to a colleague. Only then compare with what actually happened (PR/commits/hints from the day) and name gaps plainly and kindly.
3. **Predict-vs-reality:** ask for one prediction they made today that turned out wrong, and what it taught them (intuition principle).
4. Propose 2-4 flashcards from today's mistakes and key facts (one fact each, tagged with subcodes); add with `python3 scripts/flashcards.py add`. Confirm wording with the learner.
5. **Next action:** ask the learner for the very first step next session; write it, with any parked items, as a dated entry in `learner/journal.md` (`next action: ...`, `parked: ...`).
6. If a PR is open, remind them what to reply to in the shallow block of the next session; do not do it for them.
7. Close with the shutdown phrase: "Shutdown complete." and stop work talk.

If a hard rule was broken today (AI used on owned work), record it honestly in the journal; no blame.
