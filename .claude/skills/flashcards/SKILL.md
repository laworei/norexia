---
name: flashcards
description: Run a spaced-repetition flashcard session from learner/flashcards.csv, and add cards from recent findings and readings. Use when the learner types /flashcards.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*)
---

Run a flashcard session.

1. Run `python3 scripts/flashcards.py due` to list due cards (Leitner boxes 1-5, intervals 1, 3, 7, 21, 60 days).
2. Present one card at a time, front only. Wait for the learner's answer. Compare to the back honestly (right, partly, wrong). Do not reveal the back first.
3. Record each result with `python3 scripts/flashcards.py grade <id> <right|partly|wrong>`. Wrong cards go back to box 1.
4. At the end, offer to add cards from new findings and readings: front/back/tags, one fact per card, tagged with the subcode. Never include book text beyond a one-line citation.
5. Report retention for the session.
