# Learning method: the nine ultralearning principles, as practices

Based on Scott Young's *Ultralearning*. For each principle: what you do, where it lives in this repo, and what is measured. The review of this table happens at the monthly metalearning review.

## 1. Metalearning: map the territory first (<= 10% of time)
- **Why / what / how:** write `learner/metalearning.md` (template: `handbook/templates/metalearning.md`) in Sprint 0: why you are doing this, what concepts/facts/procedures you must master, how the skill is learned (resources, people, benchmarks).
- **Benchmark against reality:** collect 8-10 real job posts and 2-3 public career ladders for Go backend/platform roles; note the recurring skills. Compare with `handbook/competencies.md` and adjust it by evidence (edit `handbook/matrix.yaml`, regenerate with `make docs`).
- **Resource map:** `library/reading-map.md` already ties competencies to chapters. Add free resources where books are missing.
- **Cadence:** monthly review (`docs/plan-reviews/`): what is working, what is not, what to drop. Budget: no more than 10% of hours.

## 2. Focus: deep work protocol
See `handbook/deep-work.md`. Scoreboard lead measure: **deep minutes per week**.

## 3. Directness: learn by doing the real thing
- Tickets are real company work in a real repo with real CI and incidents, not toy exercises. At least 60% of time.
- **North-star project:** the learner's own `norexia` backend (API v1) grows ticket by ticket. Every sprint delivers something that runs end to end, however small. Avoid long reading-before-doing stretches.
- Diagnostic and drills are the only "artificial" work, and they feed back into real tickets.

## 4. Drill: attack your weakest sub-skill
Reactive: a competency subcode with 2 or more findings in 30 days gets a drill ticket next sprint. Proactive, from the first sprint, choose a drill type:
- **Isolate and repeat:** pull the weak part out of the whole task and practise it alone (e.g. error wrapping, table-test setup, goroutine lifecycle) in 20-minute reps.
- **Direct-Improve-Repeat-Tweak (DIRT):** do the whole task, find the weak step, drill it, redo the whole task, tweak the method.
- **Copycat:** re-implement a small piece of a well-written standard-library or CNCF function, then compare line by line with the original.
- **Time-slicing:** do just the first 20 minutes of a task repeatedly (setup, test-first skeleton) until it is automatic.
- **Cognitive component drills:** pure recall of syntax, API, or commands (flashcards).

## 5. Retrieval: test yourself before you review
- **Free recall at the start and end of every session** (5 min, closed notes, written). Compare after, fix gaps. Built into `/session-start` and `/session-end`.
- **Test before study:** before reading a chapter, write down what you already know and what you predict it says. Reading becomes error-correction.
- **Closed-book tickets:** at least one per sprint (official Go docs only).
- **Explain-back:** every 1:1, a merged PR explained from memory.
- **Flashcards** (`/flashcards`): one fact per card; card from every finding, hint and mistake.
- Measured: retrieval sessions per week (lead), flashcard retention (lag).

## 6. Feedback: seek it fast and do not dodge the punch
Three layers: **CI** (seconds-minutes, objective), **review** (same session, detailed), **reality** (load tests, incidents). Prefer *informational* feedback (here is what happened and why) combined with *corrective* feedback (what to change). Welcome blocking findings: each is the highest-value minute of the sprint. If feedback stings, write one line in the experiments log; do not argue until you have reproduced the problem.

## 7. Retention: do not leak
- Spaced repetition (Leitner boxes 1/3/7/21/60 days) for cards.
- **Spaced regression:** each competency reappears in a ticket about every 6 weeks.
- **Overlearn** the basics (error handling, tests, `context`): they hold everything else up.
- **Procedural memory:** for commands and workflows (git, Delve, Docker), repeat in real tickets, not in notes.
- Sleep and rest are part of retention; the schedule protects them.

## 8. Intuition: understand it deeply, not just use it
- **Predict before you run:** before running tests or a program, write the expected output (or failure) on paper. The gap between prediction and reality is the learning.
- **Feynman writing:** for each hard concept, explain it in plain words as to a new teammate; every gap you hit is a thing you do not understand yet. Store in `docs/explainers/`.
- **Don't give up on hard problems too early:** think for the full timebox before asking; but hint ladder steps in once it is over.
- **Build it from scratch:** one build-from-scratch project per level (rate limiter, KV store, toy container runtime, mini operator), and read standard-library source.
- **Prove it to yourself:** reproduce a claim from a book with a tiny experiment before relying on it.

## 9. Experimentation: from week one
- **Method experiments (from L0):** every sprint, choose ONE learning-method variable to test, with a hypothesis and a measure. Examples: test-first vs code-first on two similar tickets; reading chapter before vs after trying; 50-minute vs 90-minute blocks; writing a plan on paper before coding. Record in `learner/experiments.md`: hypothesis, change, measure, result, decision (keep/drop). Discussed in `/retro`.
- **Technical spikes (from L3):** build it two ways, benchmark, record an ADR (at least one per month).
- Explore outside your comfort zone occasionally (a different resource, a different tool), but keep it small.

## How the pieces connect
`/session-start` (plan + free recall) -> deep blocks (directness, focus, feedback from CI) -> `/review` (feedback) -> `/session-end` (recall, flashcards, logging) -> `/retro` (scoreboard, experiment decision, metalearning check) -> `/plan-sprint` (drills from findings, regression, next experiment).
