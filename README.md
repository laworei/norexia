# Norexia: a Go backend & platform engineering ultralearning program

You join **Norexia**, a fictional managed-backend company (Postgres, auth, storage, realtime, and backups with an undo button), as a new backend engineer. Over time you become the senior engineer who can design, ship, observe and operate its systems. Claude plays the company around you. You write all the code.

Design: `docs/PROGRAM.md`. Full spec: `ULTRALEARNING_BRIEF.md`. The world: `company/WORLD.md`.

## How a session works (Deep Work + Ultralearning)
1. **Start ritual** (`handbook/deep-work.md`): phone away, blocker on, then `/session-start`. It starts with 5 minutes of **free recall** of last session, before any notes.
2. **Two deep blocks of 90 minutes** on **one ticket** (WIP limit 1). You write the code; Claude never does. Breaks are for boredom, not feeds.
3. **Shallow block**: PR replies, flashcards, CI. Run `make check`; open a PR; `/review <PR#>`; reply to every `blocking` and `should-fix` comment; merge when `review:approved` is set.
4. Stuck? Try 30 minutes (60 from L2), predict what should happen, then `/stuck <issue>`.
5. **Shutdown ritual**: `/session-end` logs deep minutes, does free recall, makes flashcards, and writes the next action. Then stop.

## Commands
`/session-start` `/session-end` `/weekly-review` `/status` `/plan-sprint` `/standup` `/review <pr>` `/stuck <issue>` `/give-up <id>` `/one-on-one` `/explain-back <pr>` `/retro` `/incident` `/postmortem-review <file>` `/flashcards` `/calibrate-reviewer` `/promo` `/perf-review` `/pause` `/resume`

## Rhythm
2-week sprints, Sat+Sun, ~10 h/week (14 planned hours per sprint, about 4 deep hours per week to start, ramping). Each sprint has a **Wildly Important Goal**, **lead measures** (deep minutes, retrieval sessions, drills) and **lag measures** (competencies, approval rate), and one **method experiment**. Ritual: `/plan-sprint` -> work -> `/weekly-review` -> `/retro`. A bad week is fine: do one drill and one flashcard session (the minimum viable week), or `/pause`.

Method docs: `handbook/deep-work.md` and `handbook/learning-method.md`. Design rationale: `docs/PROGRAM.md` §6a.

## First steps
1. Read `handbook/` (start with `handbook/ladder.md`, `handbook/ai-policy.md`, `handbook/hint-ladder.md`).
2. Do the onboarding issue (Phase 4): set up your environment (upgrade Go to the current stable version, editor with AI autocomplete off, `gh`) and open your first PR adding yourself to `company/TEAM.md`.
3. Diagnostic sprint, then Sprint 1.

## Layout
`company/` world and state · `handbook/` how we work · `learner/` your state (progress, findings, flashcards; `brag-doc.md` is yours) · `library/` your books (never committed) · `services/ cmd/ internal/ pkg/` your code · `legacy/` inherited code · `platform/` environments · `chaos/` incident injection · `docs/` ADRs, RFCs, postmortems, sprints · `review-calibration/` reviewer tests · `reports/` dashboards · `scripts/` tooling · `.claude/` agents, skills, hooks · `.github/` CI and templates.

## Guardrails
Hooks stop Claude from writing in your code paths (`.claude/owned-paths.txt`). Run `make hooks` to see them tested.
