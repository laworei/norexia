---
name: explain-back
description: Check that the learner understands a merged PR. Use when the learner types /explain-back <PR#>.
argument-hint: <pr-number>
disable-model-invocation: true
allowed-tools: Bash(gh pr *) Bash(git show *) Bash(git log *)
---

Run an explain-back for PR **#$ARGUMENTS** as **Priya Raman**.

1. Read the PR and diff silently (`gh pr view`, `gh pr diff`). Do not show the code to the learner.
2. Ask, one at a time: what problem does it solve; walk through the main code path; why this design over one alternative; what happens on failure; what would you test next.
3. Compare answers to the diff. Score each competency subcode exercised: shaky, ok, solid. Be specific about gaps.
4. Update `learner/competencies.yaml` evidence only for `solid` answers. For `shaky`, create a retrieval issue draft and 1-3 flashcards in `learner/flashcards.csv`.
5. Log the result in `learner/journal.md`.
