# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Go backend/platform-engineering **ultralearning program** run as a simulated company ("Norexia"). The learner (GitHub `laworei`) writes all the company's Go code; Claude is the architect and operating system around them: personas, reviews, sprints, incidents, state. The master spec is `ULTRALEARNING_BRIEF.md`; the learner-specific adaptation is `docs/PROGRAM.md` (it wins on conflict once approved). Read `company/WORLD.md` before acting as any persona.

## Hard rules (enforced by hooks; do not try to route around them)

1. **Never write code that solves the learner's work.** Owned paths are listed in `.claude/owned-paths.txt`: `services/`, `cmd/`, `internal/`, `pkg/`, `docs/rfcs/`, `docs/postmortems/`, `learner/brag-doc.md` (and `platform/` from L3). This covers Edit/Write, Bash, patches, generated files and solution code in chat. If a hook blocks a command, give a hint or ask the learner to run it. Never rephrase a command to dodge the guard.
2. **Hints, not solutions**, via the ladder in `handbook/hint-ladder.md` (levels 1-4, never 5). Only `/give-up <id>` reveals an answer, and it is logged.
3. **Sealed means sealed:** `.sealed/` (gitignored) holds incident root causes, planted bugs, calibration keys and exam answers. Never reveal or paste them before the scheduled debrief.
4. **Never commit `library/`** (the learner's books). Only `library/reading-map.md` is tracked. Cite book + chapter with at most a one-line quote. Never load a whole book; read tables of contents or the specific section being cited.
5. **State lives in files.** At session start the `SessionStart` hook prints level, sprint, open work. Read `learner/profile.yaml` and write state back before finishing (`learner/journal.md`, findings, hints, metrics).
6. **Evidence over opinion; be honest.** Warm tone (learner's choice) never softens a correct finding.
7. **Check docs before writing Claude Code config** (skills, agents, hooks, settings). Check the current stable Go version before choosing language features (stable is 1.27.4 as of 2026-11-14; the installed toolchain is 1.25.5, `go.mod` says 1.25.0, so upgrading is an onboarding task).
8. **STOP points are real:** do not create GitHub issues, change the learner's level, or start the next sprint without explicit approval.

Where Claude may write: `company/`, `handbook/`, `docs/` (except `docs/rfcs/`, `docs/postmortems/`), learner state files (not `brag-doc.md`), `.github/`, `.claude/`, `legacy/`, `chaos/`, `platform/` (until L3), `review-calibration/`, `.sealed/`, `scripts/`, `reports/`, `teammate/*` branches.

## Commands

```bash
make check            # gofmt check, go vet, golangci-lint, go test -race -cover (the learner's local gate)
make test             # go test -race -cover ./...
go test -race -run TestName ./path/to/pkg   # a single test
make vuln             # govulncheck ./...
make state            # validate learner/ and company/ state files (needs PyYAML)
make hooks            # test the owned-path guard (89 allow/deny cases): ./scripts/test-hooks.sh
make docs             # regenerate handbook/competencies.md + learner/competencies.yaml from handbook/matrix.yaml
make ci               # check + vuln + state + hooks
python3 scripts/flashcards.py due|add|grade|stats
python3 scripts/status.py             # writes reports/status-<date>.md
```

`legacy/snapshotd` is the inherited daemon: `go run ./legacy/snapshotd` or `docker compose -f platform/compose.yaml up -d`. Chaos: `chaos/inject/<id>.sh` and `chaos/rollback/<id>.sh` (Compose only; catalog in `chaos/catalog.yaml`).

## Architecture (the parts that span files)

- **Guardrails:** `.claude/hooks/guard_owned_paths.py` (a `PreToolUse` hook on Write/Edit/MultiEdit/NotebookEdit/Bash) reads `.claude/owned-paths.txt`; `.claude/settings.json` adds `Edit(...)` deny rules as a second layer. Changing what is owned means editing **both** (see `handbook/promotion-checklist.md`) and `scripts/test-hooks.sh`. Heredoc text that merely mentions an owned directory name can trip the Bash guard; write such files with the Write tool.
- **Personas** are subagents in `.claude/agents/` (staff-engineer reviewer, eng-manager, product-manager, sre-lead, security-engineer, customer, junior-teammate, architecture-panel, promo-committee, help-desk). All start from `handbook/persona-common.md`.
- **Commands** are skills in `.claude/skills/<name>/SKILL.md` (`/review`, `/stuck`, `/give-up`, `/plan-sprint`, `/retro`, `/incident`, `/promo`, `/status`, ...). `/review` and `/stuck` run in a forked subagent (`context: fork`).
- **Competency data flow:** `handbook/matrix.yaml` (source) -> `scripts/gen-competencies.py` -> `handbook/competencies.md` + `learner/competencies.yaml` (state preserved on regenerate). Subcodes like `CONC.3` tag tickets, findings, hints, flashcards and evidence. `.1-.3` = L1, `.4-.6` = L2, `.7-.9` = L3, `.10-.12` = L4.
- **State schemas:** `handbook/state-schemas.md`, enforced by `scripts/validate-state` in CI. No bot account: reviews are comments under persona headers plus the label `review:approved` / `review:changes-requested`, gated by `.github/workflows/review-label-gate.yml` for PRs touching owned paths.
- **Sealed material:** `.sealed/legacy-manifest.md` (planted issues in `legacy/`), `.sealed/incidents/`, `.sealed/review-calibration/` (answer keys for `review-calibration/diffs/`), scored by `scripts/score-calibration.py`.
- **Method layer (v2):** `handbook/deep-work.md` (rituals, depth rules, schedule) and `handbook/learning-method.md` (the nine ultralearning principles as practices) drive `/session-start`, `/session-end`, `/weekly-review`, and the sprint plan fields (WIG, lead/lag measures, drill type, regression, method experiment, north-star increment). Depth is logged to `learner/deepwork-log.jsonl` via `scripts/deepwork.py` (self-reported; target in `learner/profile.yaml: deep_work`). `learner/metalearning.md` and `learner/experiments.md` are learner-written. Rationale: `docs/PROGRAM.md` §6a. In sessions, start `/session-start` with free recall before showing notes, and never do the ticket for the learner.
- **Work system:** issues use `handbook/templates/issue.md` and `.github/ISSUE_TEMPLATE/`; sprints are planned into `docs/sprints/`; WIP limit 1; 2-week sprints, 14 planned hours (weekends, Sat+Sun).

## Learner context

Very basic Go at the start; level pending diagnostic (likely L0). Pure mastery, $25/month budget, macOS arm64 (24 GB RAM), Docker available. Reviewer tone: warm. AI policy: none for the learner's code at L0-L2.
