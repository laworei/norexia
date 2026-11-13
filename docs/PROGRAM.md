# PROGRAM.md: Go Backend & Platform Engineering Ultralearning Program

Status: **DRAFT, awaiting learner approval (Phase 1 STOP)**. Source of truth for the design is `ULTRALEARNING_BRIEF.md`. This file records how the brief is adapted to the learner's intake answers. Where the two differ, this file wins after approval.

## 1. Learner profile (from intake)

| Item | Answer | Design consequence |
|---|---|---|
| Experience | "Basic" programming, "very basic" Go | The diagnostic sprint (§21 of the brief) decides L0 vs L1, and **L0 is the likely outcome**. L0 content comes from *Learn Go with Tests* and *Learning Go*. |
| Time | 10 h/week | 2-week sprints = 20 h declared, **14 h planned** (×0.7). Session length 50–90 min. |
| Days | Weekends (confirmed) | **Sat + Sun, about 5 h each, CET.** Each day is split into 50–90 min focus blocks with breaks. Sprint days are therefore fixed: Sat/Sun pairs. |
| Machine | MacBook, Apple M4 Pro, 14 cores, 24 GB RAM, 140 GB free, macOS 26, arm64 | Full local stack is feasible: Docker Compose at L2, kind + Prometheus/Grafana/OTel at L3. Go 1.25.5, kind, gh and git are installed. Docker daemon still to be verified. |
| GitHub | `github.com/laworei` (gh CLI already logged in) | Repo `laworei/norexia`, **public** (confirmed): portfolio, free CodeRabbit, free branch protection. |
| Bot account | None | Use the **label fallback** (§3 below). |
| Budget | $25/month | No automatic AI-review GitHub Action, no real cloud. Reviews run in local Claude Code sessions. CodeRabbit free tier from L3 if the repo is public. |
| Goal | Pure mastery, no date | Interview loop stays but is weighted low. Depth over speed, no deadline pressure, and pauses are free. |
| Books | Learner will upload to `library/` | Reading map built from tables of contents only, after upload. |
| Company | Norexia, a fictional company in the space of Supabase and Commvault | See §2. |
| Reviewer tone | Warm | Encouraging delivery. Findings stay specific and honest, with no softening of correct blocking findings. |

## 2. The company: Norexia

**Norexia** is a fictional managed backend platform. It gives developers a Postgres database with an auto-generated REST API, authentication, object storage and realtime subscriptions (Supabase-like). Every project also comes with backup, point-in-time recovery, and cross-region restore (Commvault-like). The tagline is "your backend, with an undo button."

This domain covers every area in the brief:

| Brief requirement | Norexia feature |
|---|---|
| Public API (auth, rate limiting, versioning, pagination) | Control-plane API for projects, API keys, usage |
| Payments, billing, idempotency, ledger | Usage metering and invoices (storage GB, egress, backup retention) |
| Dispatch and tracking, concurrency, real-time | Backup/restore job scheduler, job progress streaming |
| Outbound webhooks | Backup completed/failed, restore finished, quota alerts |
| Notifications, queues, background jobs | Alert emails, retention-expiry notices, job workers |
| Internal platform | CI/CD, Kubernetes, observability, golden paths for service teams |

Customers: 3–5 fictional named tenants with distinct personalities, defined in `company/WORLD.md` in Phase 2. Roadmap of 4–6 quarters, with technical needs arriving through business events:

1. Launch: control-plane API, project provisioning, daily snapshots.
2. First large customer: billing, rate limits, webhooks.
3. 10× traffic: backup scheduler scaling, queue-based workers.
4. Data growth and a reliability crisis: PITR, restore correctness, SLOs.
5. Platform team spin-up: Kubernetes, golden paths, observability.
6. Multi-region: cross-region restore, operator-managed tenant databases.

Domain names and facts in the world bible must be fictional. Real companies are referenced only as style inspiration, never impersonated.

## 3. Adaptations to the brief

1. **No bot account.** Persona reviews are posted under the learner's GitHub identity with a header naming the persona. A `review:approved` / `review:changes-requested` label plus a CI check blocks merge without the approved label. Limitation: the learner could apply the label themselves. This is covered by the honor code in `handbook/ai-policy.md`, and the explain-back in each 1:1 verifies understanding. If the learner later creates a bot account, switching is a config change.
2. **Budget $25/month.** The AI cost sits mostly in Claude Code sessions. Keep skills lean, never load books whole, and prefer local review. No cloud at L4 unless the budget changes. Everything stays on the laptop.
3. **Warm tone.** Reviewer persona cards use warm phrasing, and severity labels and evidence rules are unchanged.
4. **Pure mastery.** The promotion exams and the packet stay (they are the proof). The interview loop is optional and lighter-weight.
5. **Reality bridges** are kept: the monthly code-reading ticket from L2, and open-source work from L3.

## 4. Levels, sprints and promotion

Unchanged from the brief (§7, §8, §10). Concretely for this learner:

- **Sprint:** 2 weeks, 14 planned hours, about 5–7 tickets. WIP limit 1.
- **Sprint mix:** per the brief's table. At L1, 60% delivery, 25% drill, 15% retrieval.
- **Minimum viable week:** 1 drill + 1 flashcard session (about 2 h).
- **Promotion gates:** coverage (every required subcode `independent` with ≥2 evidence links from ≥2 sprints), trend, timed closed-book exam, promo packet. There are no time-based promotions.
- **Expected pace (guidance, not a deadline):** at 10 h/week, each level likely takes several months, so L4 is a multi-year program. The adaptive system and evidence gates decide, not the calendar.

## 5. Phase 2 build plan

Order of work, after approval. Each step ends with its own verification.

1. **Check docs first (hard rule 6):** current Claude Code docs for skills, subagents, hooks, settings and CLAUDE.md formats, and the current stable Go version.
2. **Repo init:** `git init`, `.gitignore` (`library/*`, `.sealed/`, secrets; keep `library/reading-map.md`), create `laworei/norexia` via `gh` only after the learner confirms visibility.
3. **Guardrails first:** `.claude/owned-paths.txt`, PreToolUse hooks (file tools and Bash), deny rules in `settings.json`, and `scripts/test-hooks.sh`. Nothing else is built until hook tests pass.
4. **World and handbook:** `company/WORLD.md`, `TIMELINE.md`, `state.yaml`, personas. Handbook: values, competencies (matrix with 3–6 observable behaviors per area per level), ladder, style, AI policy, templates.
5. **State and validation:** `learner/` files with schemas, and `scripts/validate-state`.
6. **Agents and skills:** 10 personas and the slash commands listed in the brief (§19).
7. **CI and GitHub:** workflows (ci, review-label-gate, state validation), issue and PR templates, CODEOWNERS, labels, project board.
8. **Legacy service** with planted issues, and the sealed manifest in `.sealed/`.
9. **Chaos catalog**, with one L2 incident that injects and rolls back in Compose.
10. **Reading map** after the books are uploaded.

Phase 3 then runs the 10-item acceptance checklist and reports a pass/fail table. Phase 4 does onboarding, the diagnostic sprint and a Sprint 1 preview, with issues created only after approval.

## 6. Resolved items and notes

All Phase 1 open items are resolved: weekends (Sat+Sun), public repo, very basic Go, username `laworei`, Docker daemon running, and 24 books uploaded to `library/`.

Notes:
- **Go version:** the current stable release is Go 1.27.4 (1.26.11 is also supported). The installed toolchain is 1.25.5, so upgrading to the current stable version is an onboarding step.
- **Books:** the library differs from the brief's core spine (it has no *100 Go Mistakes* and no *DDIA*, but has *Concurrency in Go*, *Cloud Native Go*, *Let's Go Further*, *Learning Go* and others). The reading map is built from what exists, and gaps are filled with free official references.
- **Duplicates:** `Shipping Go.epub` and `Shipping Go (1).epub` are the same size and look identical. Keep one.
