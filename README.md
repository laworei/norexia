# Norexia: a Go backend & platform engineering ultralearning program

You join **Norexia**, a fictional managed-backend company (Postgres, auth, storage, realtime, and backups with an undo button), as a new backend engineer. Over time you become the senior engineer who can design, ship, observe and operate its systems. Claude plays the company around you. You write all the code.

Design: `docs/PROGRAM.md`. Full spec: `ULTRALEARNING_BRIEF.md`. The world: `company/WORLD.md`.

## How a session works
1. Open Claude Code in this folder. The session-start summary shows your level, open work and flashcards due.
2. Work **one ticket at a time** (WIP limit 1) in 50-90 minute blocks. You write the code; Claude never does.
3. Run `make check`. Open a PR from a branch. Use the PR template.
4. `/review <PR#>` for the staff-engineer's review. Reply to every `blocking` and `should-fix` comment, then merge when `review:approved` is set.
5. Stuck? Try 30 minutes (60 from L2), then `/stuck <issue>`.

## Commands
`/status` `/plan-sprint` `/standup` `/review <pr>` `/stuck <issue>` `/give-up <id>` `/one-on-one` `/explain-back <pr>` `/retro` `/incident` `/postmortem-review <file>` `/flashcards` `/calibrate-reviewer` `/promo` `/perf-review` `/pause` `/resume`

## Rhythm
2-week sprints, Sat+Sun, ~10 h/week (14 planned hours per sprint). Sprint ritual: `/plan-sprint` -> work -> `/retro`. Weekly `/one-on-one` with an explain-back. A bad week is fine: do one drill and one flashcard session (the minimum viable week), or `/pause`.

## First steps
1. Read `handbook/` (start with `handbook/ladder.md`, `handbook/ai-policy.md`, `handbook/hint-ladder.md`).
2. Do the onboarding issue (Phase 4): set up your environment (upgrade Go to the current stable version, editor with AI autocomplete off, `gh`) and open your first PR adding yourself to `company/TEAM.md`.
3. Diagnostic sprint, then Sprint 1.

## Layout
`company/` world and state · `handbook/` how we work · `learner/` your state (progress, findings, flashcards; `brag-doc.md` is yours) · `library/` your books (never committed) · `services/ cmd/ internal/ pkg/` your code · `legacy/` inherited code · `platform/` environments · `chaos/` incident injection · `docs/` ADRs, RFCs, postmortems, sprints · `review-calibration/` reviewer tests · `reports/` dashboards · `scripts/` tooling · `.claude/` agents, skills, hooks · `.github/` CI and templates.

## Guardrails
Hooks stop Claude from writing in your code paths (`.claude/owned-paths.txt`). Run `make hooks` to see them tested.
