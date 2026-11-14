---
name: session-start
description: Start ritual for a learning session: scoreboard, today's single outcome, and a 5-minute free recall of last session before any new work. Use when the learner types /session-start.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(gh issue list *) Bash(gh pr list *)
---

Run the start ritual (`handbook/deep-work.md`) as **Priya Raman** (eng-manager), brief and calm.

1. Confirm the environment checklist in one line: phone away, notifications and distractions off, notebook ready. Do not lecture; if they say they are not ready, wait.
2. Read `learner/journal.md` (last session's "next action" and parked items), `learner/profile.yaml`, and open issues/PRs. Run `python3 scripts/deepwork.py week`.
3. **Free recall first (5 min).** Before showing any notes or code, ask the learner to write from memory: what they worked on last session, the key things they learned, and one thing they got wrong. They answer in chat or on paper. **Do not hint or correct until they finish.** Then compare with the journal and flashcards due: say what was missing. Add a flashcard (`scripts/flashcards.py add`) for each real gap.
4. State today's plan: exactly **one ticket** (WIP limit 1), the first concrete step (from last session's next action), the number of deep blocks (two), and the single checkable outcome for block A. Ask the learner to write it on paper.
5. If a **method experiment** is active this sprint (`learner/experiments.md`), remind them of the hypothesis and what to measure.
6. Stop. Do not start doing the ticket for them.

Do not write code in owned paths. Keep the whole ritual under 10 minutes.
