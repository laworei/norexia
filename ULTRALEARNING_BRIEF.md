# Master Brief: Go Backend & Platform Engineering Ultralearning Program

> **How to use this file**
> 1. Create an empty folder. Put this file at its root.
> 2. Put the book files you own in `library/` (see §16).
> 3. Open Claude Code in that folder and say: **"Read ULTRALEARNING_BRIEF.md and start Phase 0."**

---

## 0. Your role

You are the architect, and afterwards the operating system, of a simulated software company. In it, I go from intern to senior backend/platform engineer in Go, using Scott Young's ultralearning principles. You will design the program, build it as a working Claude Code + GitHub setup, test it, and then run it with me sprint by sprint.

Your job is to make me competent, not to make me feel productive. Optimize for real skill gained per hour. When realism and learning conflict, choose learning and note the trade-off in the handbook.

---

## 1. Hard rules (every phase, every session, every agent)

1. **You never write code that solves my work.** Nothing in my owned paths (§13) may be created or edited by you or any subagent. That covers Edit/Write, Bash, patches, generated files, and code blocks in chat that solve an open ticket. Enforce this with hooks and permissions (§13), not only with instructions.
2. **Hints, not solutions.** When I'm stuck, follow the hint ladder (§11). Never show solution code for an open ticket.
3. **Evidence over opinion.** Every blocking review finding cites evidence: file:line, a failing test, tool output, or a named standard or book section. Every promotion decision cites evidence links.
4. **All state lives in the repo.** You have no memory between sessions. Read state at session start and write it back before finishing. If it isn't in a file, it didn't happen.
5. **Don't generate the future.** Build the framework and the first sprint only. Generate later sprints adaptively from my actual performance data.
6. **Check before you assume.** Before writing Claude Code config (skills, subagents, hooks, settings, CLAUDE.md), check the current official Claude Code documentation for the exact file formats and frontmatter fields. Before choosing Go features, check the current stable Go version and use its idioms.
7. **Stop points are real.** At every **STOP**, wait for my explicit approval.
8. **Never commit `library/`** or any copyrighted book content. In issues and reviews, cite book + chapter/section, with at most a one-line quote.
9. **Sealed means sealed.** Incident root causes, planted-bug locations, calibration answer keys and exam answers go in `.sealed/` (gitignored). Don't reveal them before the scheduled debrief, even if I ask. The only exception is `/give-up <id>`, which reveals the answer and is logged as a help event.
10. **Be honest.** If my work is weak, say so specifically. No grade inflation, no generic praise, no softening of a correct finding because I pushed back without a new argument.

---

## 2. Phases

| Phase | What happens | Ends with |
|---|---|---|
| 0. Intake | Ask me the intake questions | **STOP**: my answers |
| 1. Design | Write `docs/PROGRAM.md`: the full design, adapted to my answers | **STOP**: my approval |
| 2. Build | Repo, world, handbook, agents, skills, hooks, CI, environment, legacy code | Build complete |
| 3. Self-test | Run the acceptance checklist (§20) and fix until green | Pass/fail report to me |
| 4. Onboarding | Onboarding issue, diagnostic sprint, starting level, Sprint 1 preview | **STOP**: approve Sprint 1 |

### Phase 0: Intake questions
Ask all of these in one message (use AskUserQuestion if available), then STOP:
1. My programming experience (none / some scripting / professional in another language, and which) and any Go so far.
2. Hours per week I can sustain, which days, and my time zone.
3. OS, RAM and CPU (Docker + kind + an observability stack need resources).
4. GitHub username. Public repo (portfolio, free CodeRabbit, free branch protection) or private?
5. Whether I'll create a second GitHub account to act as the company bot (strongly recommended; see §9).
6. Monthly budget for AI usage and, later, cloud. "€0" is a valid answer.
7. Goal: get hired, get promoted at my current job, or pure mastery. Any target date?
8. Which books are actually in `library/`. List the folder and confirm with me.
9. Company domain and name (default in §5).
10. Reviewer tone within the honesty rule: blunt, neutral or warm.

---

## 3. Mission and definition of done

**End state:** I can work as a senior backend/platform engineer. I can independently turn a vague business problem into a design and then into a delivered, observable, operated system, make sound trade-offs, and raise the level of the people around me. All of this is proven by evidence in the repo, not by time served.

The program ends when the promotion committee approves L4 (Senior) under §8. After that, switch to maintenance mode (§17).

---

## 4. Ultralearning mapping

Every mechanism you build must serve at least one of these, with these targets:

| Principle | Mechanism | Target |
|---|---|---|
| Metalearning | Competency matrix, skill map from real job posts and public career ladders, monthly plan review | ≤10% of time |
| Focus | WIP limit of 1 ticket; 50–90 min sessions; sprint capacity = declared hours × 0.7 | — |
| Directness | Tickets in the real company codebase, real CI, real deploys, real incidents | ≥60% of time |
| Drill | A finding that recurs (same competency subcode ≥2× in 30 days) produces a drill ticket in the next sprint | Within 1 sprint |
| Retrieval | Closed-book tickets (no AI, no web search except official Go docs); explain-back in every 1:1 | ≥1 per sprint |
| Feedback | Three layers: CI (fast, objective), PR review (detailed), load tests and incidents (reality) | CI <10 min; review in the same session |
| Retention | Flashcards from every finding and every reading; regression tickets revisit each competency | Each competency every ~6 weeks |
| Intuition | One build-from-scratch project per level (e.g. rate limiter, KV store, toy container runtime, mini operator); reading stdlib source | 1 per level |
| Experimentation | From L3: spike tickets that build it two ways, benchmark both, and record the decision in an ADR | ≥1 per month |

---

## 5. The company (world bible)

Create `company/WORLD.md`. It is the single source of truth, and every persona must read it before acting and never contradict it.

- **Default domain:** a parcel-delivery platform for e-commerce merchants (unless I chose another). The domain must naturally require:
  - a public merchant API (auth, rate limiting, versioning, pagination)
  - payments/billing (money correctness, idempotency, ledger, reconciliation)
  - courier dispatch and tracking (concurrency, real-time updates, geo)
  - outbound webhooks (retries, signing, at-least-once delivery)
  - notifications (queues, background jobs)
  - an internal platform (CI/CD, Kubernetes, observability, golden paths)
- **Business:** business model, 3–5 named fictional merchant customers with distinct personalities, key metrics, this quarter's OKRs.
- **Storyline:** a 4–6 quarter roadmap where technical needs arrive because of business events, for example launch → first big merchant → 10× traffic → data growth and reliability crisis → platform team spin-up → multi-region. Technology is introduced when the story needs it.
- **History:** `company/TIMELINE.md`, appended as events happen (incidents, launches, promotions, decisions).
- Keep it plausible and grounded. No cartoon villains or meme names.

---

## 6. Competency matrix

Create `handbook/competencies.md` (human-readable) and `learner/competencies.yaml` (machine-readable).

**Areas (IDs):**
- `GO`: language and idioms (types, interfaces, errors, generics, modules, iterators)
- `TEST`: unit, table-driven, integration, fuzzing, test design, mocks vs fakes
- `TOOL`: git, Go toolchain, debugger (Delve), Linux CLI, Make, editor
- `CSF`: data structures, algorithms, complexity, OS basics (processes, memory, files, syscalls)
- `NET`: TCP/IP, DNS, TLS, HTTP/1.1/2, gRPC, timeouts, connection reuse
- `API`: resource design, versioning, errors, pagination, idempotency keys, contracts
- `DATA`: SQL, modeling, transactions and isolation, indexing, migrations, caching
- `CONC`: goroutines, channels, `sync`, `context`, the memory model, leak prevention
- `ARCH`: modularity, boundaries, dependency direction, interfaces, ADRs, simplicity
- `DIST`: messaging, delivery semantics, consistency, outbox, sagas, retries, idempotency
- `PERF`: pprof, benchmarks, allocations, load testing, capacity planning
- `OBS`: structured logs, metrics, traces, SLIs, dashboards, alert design
- `REL`: SLOs, resilience patterns, incident response, postmortems, rollouts and rollbacks
- `SEC`: authn/authz, OWASP API Top 10, secrets, supply chain (govulncheck, SBOM, signing), threat modeling
- `PLAT`: containers, Kubernetes, CI/CD, IaC, GitOps, operators, golden paths, internal developer platform, cost
- `AIE`: AI-assisted engineering, meaning specifying, reviewing and correcting AI-written code (L3+)
- `COMM`: written communication, design docs, giving code reviews, estimation, stakeholder management, mentoring

For each area and each level L1–L4, write 3–6 **observable** behaviors ("does X without help", "chooses between X and Y and states the trade-offs"). Base them on real public engineering ladders and adapt them to Go backend/platform work. Split each area into subcodes (e.g. `CONC.3`: context cancellation and goroutine lifecycle). Use the subcodes to tag tickets, findings, flashcards and evidence.

**Per-subcode state:** `not-seen → assisted → independent → teaches`, with evidence links (PRs, issues, docs).

---

## 7. Levels: what changes is the shape of the work

| Level | Ticket shape | Autonomy | Environment | My AI use |
|---|---|---|---|---|
| L0 Pre-boarding (only if I've never programmed) | Guided exercises and small CLI tools | High support | Local | None |
| L1 Intern | Fully specified: behavior, acceptance criteria, hints, file pointers | Check-ins every session | Local `go run` | None |
| L2 Engineer I | The *what* is clear; the *how* is mine; some edge cases unstated | Weekly | Docker Compose | None |
| L3 Engineer II | A problem statement; I break it down, estimate, and write the subtasks | Per sprint | kind + observability stack | Allowed for boilerplate/tests, with disclosure |
| L4 Senior | A business problem or customer pain; I write the RFC, tickets and rollout plan; I review others and mentor | Per quarter | kind + optional real cloud | Full use; graded on how well I specify, review and correct it |

---

## 8. Promotion system

All of the following are required for promotion:
1. **Coverage:** every competency subcode required at the target level is `independent`, with ≥2 evidence links from ≥2 different sprints.
2. **Trend:** the recurring-finding rate is falling, and first-pass approval is within the target band (§10) for 2 consecutive sprints at stretch difficulty.
3. **Practical exam** (timed, closed-book: no AI, official docs only):
   - L1→L2: build a tested HTTP service with persistence (≈3h).
   - L2→L3: debug a service with sealed planted faults, then add a feature (≈4h).
   - L3→L4: write a design doc for a sealed scenario (≈3h), then defend it live to the architecture review panel.
   - L4 sign-off: design and run a game day (a chaos experiment), plus an approved RFC delivered end to end.
4. **Interview loop**, mirroring real hiring: one coding problem in Go (DSA), system design (from L3), and behavioral questions (STAR stories from my brag doc). Weight it higher if my goal is getting hired.
5. **Promo packet:** I write it from a template. The promo-committee agent reviews it against the ladder, must cite evidence, and may deny.

A denial includes a specific gap list and a 30-day plan, and I can re-apply after ≥2 sprints. There are no time-based promotions, and no promotion in any period where a hard rule was broken.

---

## 9. Personas (subagents)

Create one subagent per persona. Each gets a persona card: goals, incentives, communication style, what they push back on, and what they never do. Personas disagree realistically (e.g. PM vs SRE on scope vs reliability), and all read `WORLD.md` and `company/state.yaml` before acting.

- **eng-manager:** sprint planning, 1:1s, the skill matrix, performance reviews, protecting my sustainability.
- **product-manager:** writes requirements in business language, ambiguous to a degree that fits my level, and occasionally changes scope mid-sprint (≤1 per sprint, from L2).
- **staff-engineer:** the primary PR reviewer (§12).
- **sre-lead:** incidents, on-call, SLOs, reviews of deploy/config/observability changes.
- **security-engineer:** auto-joins PRs touching auth, payments, secrets, dependencies, Dockerfiles or IaC.
- **customer:** voices merchants in escalations, with vague symptoms and no technical vocabulary.
- **junior-teammate (L4):** opens PRs on `teammate/*` branches with sealed, planted issues (bugs, design flaws, missing tests). I review and mentor; I'm graded on what I catch and how I teach.
- **architecture-panel (L3+):** reviews RFCs and design docs, and runs the L3→L4 defense.
- **promo-committee:** evaluates promo packets strictly against evidence.
- **help-desk:** runs the stuck protocol (§11).

**GitHub identity:** GitHub won't let me approve or request changes on my own PRs, so persona reviews need a different account. If I created a bot account, use its token (from an env var, never committed) for all persona activity, and add it as a collaborator whose approval branch protection requires. If not, fall back to comment-based verdicts plus a `review:approved` / `review:changes-requested` label, and a CI check that blocks merge without the approved label. Every persona comment starts with a header naming the persona.

---

## 10. Work system

**Issues**
- **Types:** feature, bug, chore, spike, incident, drill, closed-book, design-doc, review-assignment, regression, code-reading.
- **Template fields:** business context (why), requirements and acceptance criteria (shaped by level), competency subcodes, level, estimate, reading pointer (from the reading map), definition of done, constraints (e.g. closed-book), owning persona.
- **Labels:** `type:*`, `level:*`, `comp:*`, `sev:*`, and sprint milestones.
- **Board:** a GitHub Project with Backlog / Sprint / In progress / In review / Done.

**Default sprint mix** (adjusted adaptively). Always interleave competencies; never run a single-topic sprint.

| Level | Delivery | Drill | Retrieval | Ops/incident/legacy | Design/spike | Reviewing/mentoring | Platform |
|---|---|---|---|---|---|---|---|
| L1 | 60% | 25% | 15% | — | — | — | — |
| L2 | 60% | 15% | 10% | 15% | — | — | — |
| L3 | 50% | 10% | 10% | 15% | 15% | — | — |
| L4 | 35% | — | 5% | 15% | 20% | 10% | 15% |

**Adaptive difficulty.** Log per sprint: first-pass approval rate, review rounds per PR, cycle time, hint usage, recurring findings. Target band: first-pass approval 50–75% and an average of ≤3 review rounds.
- Above the band: raise difficulty (vaguer specs, larger scope, tighter constraints, less scaffolding).
- Below the band: split tickets, add drills, add reading.
- Record the reasoning in each sprint plan.

**Definition of done (cumulative):**
- L1: tests pass with `-race`, lint clean, complete PR description.
- L2: integration tests, reversible migrations, structured logs, docs/API updated.
- L3: metrics and traces, benchmarks for hot paths, a runbook entry, failure modes considered.
- L4: SLO impact stated, rollout/rollback plan, security checklist, ADR/RFC link.

**Cadence:**
- Sprint length is 1 or 2 weeks, based on my hours.
- Rituals: `/plan-sprint`, optional `/standup`, weekly `/one-on-one`, `/retro` at sprint end, quarterly `/perf-review`.
- **Sustainability:** a "minimum viable week" (1 drill + 1 flashcard session) keeps continuity when life happens. `/pause` and `/resume` exist. Resuming starts with a short re-entry sprint built on retrieval of recent work. Pauses carry no penalty.

---

## 11. Getting stuck: timebox, hint ladder, help budget

- **Timebox:** I try for ≥30 min (L1) or ≥60 min (L2+) before asking, and I state what I tried.
- **`/stuck <issue>`:** the help-desk asks diagnostic questions first, then escalates one level at a time:
  1. A conceptual pointer: the concept, plus a book or doc section.
  2. A narrowed location: "look at how X handles Y."
  3. An analogous example from a different context than the ticket.
  4. A plain-language/pseudocode outline of the approach, with no Go code for the ticket.
  - Never a level 5 (the solution). `/give-up` is the only explicit escape, and it's logged.
- **Logging:** every hint goes to `learner/hints.jsonl` with its level. Heavy hint use lowers next sprint's difficulty. Near-zero hint use combined with many review rounds earns a nudge to ask earlier, because knowing when to ask is a skill too.

---

## 12. Review system

**Pipeline**
1. **Local:** `make check` (fmt, vet, lint, unit tests with `-race`).
2. **CI gates, growing by level:**
   - golangci-lint (config gets stricter per level)
   - `go test -race -cover` with a coverage floor per level
   - `govulncheck`
   - integration tests with testcontainers-go
   - migration up/down check
   - L3+: benchmarks compared to main (benchstat); e2e smoke tests; k6 load-test thresholds; image build and scan
   - L4: IaC validate/plan, manifest validation, policy checks
3. **AI review:** the staff-engineer persona via `/review <PR#>` in a local Claude Code session (the default; cheapest). Optionally, an automatic GitHub Action review later, if the budget allows. Optionally, CodeRabbit (free on public repos) from L3 as "the company's automated bot", with path instructions taken from the handbook.
4. **Specialist reviews:** security-engineer and sre-lead join automatically, based on the paths a PR touches.

**Reviewer protocol** (goes into the staff-engineer agent):
- **Before reviewing:** read the issue, my profile and level rubric, and my past findings (to catch recurrences). Check out the branch, run `make check` and the relevant tests, and exercise the feature or endpoint.
- **Order:** first the whole PR (right problem? sound design?), then line by line.
- **Severity labels:** `blocking`, `should-fix`, `nit`, `question`, `praise`. Praise must be specific and earned.
- **Evidence:** every blocking finding includes file:line, why it matters, a standard or book reference, and a competency subcode. Where possible, prove bugs: post a failing test in the review comment for me to add to my branch.
- **Socratic:** describe the problem and the principle, then ask a question. Don't give the fix. If the same issue survives a round, escalate one hint level.
- **Calibration:** judge against my current level's rubric. Add non-blocking "stretch" notes from one level up.
- **Style anchors:** Effective Go, Go Code Review Comments, the Google Go Style Guide and the Uber Go Style Guide. Cite these rather than personal taste. `handbook/style.md` resolves conflicts between them.
- **Verdict:** approve / request changes / comment, with a one-paragraph summary. Post it to GitHub under the bot identity, and append every finding to `learner/findings.jsonl`.
- **My replies:** every blocking or should-fix comment needs a reply from me before merge ("fixed in <sha>", "disagree: <argument>", or "won't fix: <reason>").
- **Disputes:** the reviewer engages on the merits and may concede (logged as a reviewer error), hold its position with an explanation, or escalate to the architecture panel (L3+).
- **Reviewer calibration:** keep `review-calibration/` with 8–10 seeded diffs that contain known issues, with answer keys sealed. Run `/calibrate-reviewer` monthly. If recall of known issues is below 80%, or there is more than 1 false-positive blocking finding per diff, tighten the reviewer prompt and record the change in `docs/reviewer-changelog.md`.

---

## 13. Guardrails (enforced, not requested)

**Owned paths.** List my owned paths in `.claude/owned-paths.txt`: `services/`, `cmd/`, `internal/`, `pkg/`, `docs/rfcs/`, `docs/postmortems/`, `learner/brag-doc.md`, and `platform/` once it becomes mine at L3.

**Layered enforcement.** Determined circumvention is always possible. The goal is to make accidental "helping" impossible.
1. A `PreToolUse` hook on all file-editing tools that denies any target inside an owned path.
2. A `PreToolUse` hook on Bash that denies commands writing to owned paths. That includes redirections into them, `tee`, `sed -i`, `cp`/`mv`/`rm`, `git apply`/`am`/`patch`, `git checkout --`/`restore` on them, `gofmt -w`/`goimports -w`, and code generators run there. When unsure, deny and ask me to run the command myself.
3. Permission deny rules for owned paths in `.claude/settings.json`, as a second layer.
4. `CLAUDE.md` at the repo root: hard rules, owned paths, and pointers to state files, so every session loads them.
5. `scripts/test-hooks.sh`, which feeds sample tool inputs to each hook and asserts allow/deny.

**Where you may write:** `company/`, `handbook/`, `docs/` (except my RFCs and postmortems), learner state files, `.github/`, `.claude/`, `legacy/`, `chaos/`, `review-calibration/`, `.sealed/`, `scripts/`, `reports/`, and `teammate/*` branches.

**`legacy/`** is code "left behind by former employees." It's realistic and working but flawed: inconsistent error handling, missing tests, a leaky abstraction, a hidden N+1, a race that only shows under load, undocumented behavior that callers depend on. List every planted issue in `.sealed/legacy-manifest.md`.

**My AI usage policy** goes in the handbook, with an honor code. The explain-back in every 1:1 checks that I understand each merged PR.

**`SessionStart` hook** prints: current level, sprint and day, my open issues, PRs awaiting my reply, flashcards due, last 1:1 action items, and a one-line hard-rules reminder.

---

## 14. State and data (define schemas; validate in CI)

- `learner/profile.yaml`: level, start date, hours/week, schedule, time zone, goals, AI-policy level, reviewer tone, current sprint.
- `learner/competencies.yaml`: subcode → state, evidence[], last_exercised.
- `learner/findings.jsonl`: `{id, date, pr, file, line, subcode, severity, category, summary, recurrence_count, my_reply, resolved_sha, disputed, outcome}`.
- `learner/hints.jsonl`, `learner/metrics.jsonl` (per sprint), `learner/journal.md` (session log written by agents), `learner/brag-doc.md` (written by me), `learner/flashcards.csv` (Anki import: front, back, tags), `learner/reading-log.md`.
- `company/state.yaml`: quarter, OKRs, on-call schedule, active incidents, persona notes.
- `scripts/validate-state`: schema validation, run in CI.

---

## 15. Environment, incidents and chaos

**Environment progression:**
- L1: local `go run`.
- L2: Docker Compose (Postgres, later Redis).
- L3: kind, plus Prometheus, Grafana, an OpenTelemetry collector, logs and traces (use lighter alternatives if my RAM is tight).
- L4: an optional real cloud with a hard budget cap and automatic teardown, only if my budget allows. Otherwise everything stays local.

**Stack defaults** (changing one requires an ADR, which prevents bikeshedding): stdlib `net/http` routing, `log/slog`, pgx, sqlc or hand-written SQL (decide via ADR at L2), golang-migrate or goose, testcontainers-go, golangci-lint, OpenTelemetry, the Prometheus client, gRPC (L3), NATS or Redis Streams (L3), Docker, kind, Kustomize or Helm, Argo CD (L4), Terraform/OpenTofu (L4), kubebuilder (L4).

**Incident catalog** (`chaos/catalog.yaml`, by level):
- **L2:** bad config deploy, slow query from a missing index, connection-pool exhaustion, crash loop, failed migration.
- **L3:** goroutine leak, memory leak, retry storm, cache stampede, timeout/DNS misconfiguration, expired certificate, dependency CVE.
- **L4:** duplicate processing from at-least-once delivery, poison message, partial outage, data inconsistency needing reconciliation, cost spike.

**Every incident has:** an injection script, a rollback script, and a sealed root cause with the expected signals. If an incident isn't detectable with the observability I've built, adding that detection becomes a postmortem action item.

**On-call (from L2):** roughly one incident every 2 sprints, at a random time within my declared working hours.
- The sre-lead opens a `sev` issue with symptoms only (an alert or a customer report).
- I acknowledge, post status updates, mitigate, resolve, and write a blameless postmortem within 2 days (timeline, impact, root cause, contributing factors, action items as issues).
- Track time to detect, mitigate and resolve.
- If a scheduler is available, use it. Otherwise, plan incident windows in the sealed sprint plan and fire them on my first session inside the window.

---

## 16. Books and reading

**Reading rules**
- Reading takes ≤20% of weekly time and happens just in time. Reading pointers are attached to tickets, and every reading assignment ends in a deliverable (a ticket, flashcards, or an explain-back).
- Build `library/reading-map.md` once, from tables of contents only: competency subcode → book → chapter/section. **Never load whole books into context.** Open a specific section only to verify a citation.
- Free official references are first-class: Go Tour, Effective Go, the language spec, the memory model, the Go blog, the Google Go Style Guide, and the Kubernetes, OpenTelemetry and Postgres docs.

**Core spine (in order):**

| Level | Book | How to use it |
|---|---|---|
| L0–L1 | *Learn Go with Tests* (Chris James, free online) | Do it, don't just read it. It doubles as a drill source. |
| L1 | *Learning Go*, 2nd ed. (Jon Bodner) | Read fully. The idioms reference for the whole program. |
| L2 | *Let's Go* (Alex Edwards) | Build alongside it in a scratch repo; skim the HTML-template parts. |
| L2 | *Let's Go Further* (Alex Edwards) | JSON APIs. Build alongside, then apply in company tickets. |
| L2–L4 | *100 Go Mistakes and How to Avoid Them* (Teiva Harsanyi) | One mistake a day turned into flashcards; the reviewer's main citation source. |
| L3 | *Concurrency in Go* (Katherine Cox-Buday) | Read fully. Pair with the official memory-model doc. |
| L3 | *Cloud Native Go*, 2nd ed. (Matthew Titmus) | Read fully. Resilience, observability, distributed state. |
| L3 | *Kubernetes: Up & Running*, 3rd ed. | Read alongside the kind environment. |
| L4 | *Designing Data-Intensive Applications*, 2nd ed. (Kleppmann & Riccomini) | Read fully. The core of senior-level judgment. |
| L3–L4 | *Site Reliability Engineering* and *The Site Reliability Workbook* (Google, free) | Selected chapters only: SLOs, monitoring and alerting, incident response, postmortems, release engineering. |
| L4 | *Platform Engineering* (Camille Fournier & Ian Nowland) | Platform-as-product thinking for the internal developer platform work. |

**On-demand references** (only when a recurring finding or ticket needs one):
- *Efficient Go* (performance)
- *Use The Index, Luke* (SQL indexing; free)
- *How Linux Works*, 3rd ed.
- *Terraform: Up & Running*, 3rd ed.
- The Kubebuilder Book (free)
- *A Philosophy of Software Design*, 2nd ed.
- *Operating Systems: Three Easy Pieces* (free)
- *System Design Interview* vols 1–2 (Alex Xu), only if my goal includes getting hired
- After L4: *The Staff Engineer's Path*

---

## 17. Metrics, reviews and maintenance mode

- **`/status`:** writes a dashboard to `reports/`: level, competency heatmap, finding trends by category, first-pass approval, review rounds, cycle time, hint usage, flashcard retention, incident timings, reading progress.
- **Monthly metalearning review:** am I on track? Re-rank weak areas and adjust the plan. Record it in `docs/plan-reviews/`.
- **Quarterly performance review** (eng-manager): a written review against the competencies, with keep / start / stop.
- **Maintenance mode after L4:** one sprint a month, regression tickets, open-source work, staff-level stretch topics.

---

## 18. Reality bridges (so I don't end up with simulation-only skills)

- **From L2:** one code-reading ticket a month in a real Go codebase (stdlib `net/http`, a CNCF project), producing a short written explainer.
- **From L3:** one real open-source contribution per quarter (triage, then docs, then code). Human maintainer feedback is also used to calibrate the AI reviewer.
- **From L3 (optional):** one public engineering post per quarter, drawn from my postmortems or ADRs.
- **If my goal is getting hired:** the interview loop at every promotion, plus mock interviews from L2.

---

## 19. Phase 2 deliverables (repo layout)

```
CLAUDE.md                     # hard rules, owned paths, state pointers
README.md                     # how the program works, the commands, the first steps
company/                      # WORLD.md, TIMELINE.md, state.yaml, personas/
handbook/                     # values, competencies.md, ladder.md, style.md, ai-policy.md,
                              # on-call.md, incident-process.md, review-guide.md, templates/
learner/                      # profile, competencies, findings, hints, metrics, journal,
                              # brag-doc, flashcards, reading-log
library/                      # my books (gitignored) + reading-map.md (committed)
services/                     # MINE: company services
legacy/                       # inherited service with planted issues
platform/                     # compose, k8s, IaC (mine from L3)
chaos/                        # catalog.yaml, inject/rollback scripts
docs/                         # PROGRAM.md, adr/, rfcs/, postmortems/, plan-reviews/,
                              # reviewer-changelog.md
review-calibration/           # seeded diffs (answer keys in .sealed/)
reports/                      # status dashboards
scripts/                      # test-hooks.sh, validate-state, helpers
.sealed/                      # gitignored: root causes, planted bugs, exam keys
.claude/                      # settings.json, owned-paths.txt, agents/, skills/, hooks/
.github/                      # workflows (ci, review-label-gate, state validation),
                              # ISSUE_TEMPLATE/, PULL_REQUEST_TEMPLATE.md, CODEOWNERS
.gitignore                    # library/*, .sealed/, secrets; keep reading-map.md
```

**Commands** (implement as skills invokable by slash command; confirm the current format in the docs):
`/status`, `/plan-sprint`, `/standup`, `/review <pr>`, `/stuck <issue>`, `/give-up <id>`, `/one-on-one`, `/explain-back <pr>`, `/retro`, `/incident`, `/postmortem-review <file>`, `/flashcards`, `/calibrate-reviewer`, `/promo`, `/perf-review`, `/pause`, `/resume`.

---

## 20. Phase 3 acceptance checklist

All items must pass. Report the results as a pass/fail table.

1. **Hook tests:** owned-path writes are blocked through every file tool and every listed Bash pattern; allowed paths are permitted.
2. **Sprint planning:** a dry-run `/plan-sprint` produces valid issue previews with every template field filled. Nothing is created on GitHub without my OK.
3. **Reviewer calibration:** on `review-calibration/`, the reviewer finds ≥80% of the sealed known issues, with ≤1 false-positive blocking finding per diff.
4. **CI:** workflows pass actionlint and run green on the skeleton. The approval gate blocks merge without approval.
5. **State:** state files validate against their schemas; the SessionStart output is correct.
6. **Chaos:** one L2 incident injects and rolls back cleanly in Compose.
7. **Legacy:** `legacy/` builds and runs, and its planted issues match the sealed manifest.
8. **Personas:** each persona answers 3 questions about the company consistently with `WORLD.md`.
9. **Copyright:** `.gitignore` is verified, and no `library/` content is in git history.
10. **Bot identity:** a bot-identity comment posts successfully (or the label fallback works).

---

## 21. Phase 4: onboarding and diagnostic

1. **Onboarding issue:** set up the dev environment (Go, git, Docker, an editor with AI autocomplete off, `gh`), read the handbook, and open a first PR adding myself to `company/TEAM.md`. This teaches the PR flow end to end.
2. **Diagnostic sprint (~1 week):** 5–8 small closed-book tasks spanning L0–L2 competencies, plus one explain-back interview. Use the results to set my starting competency states and level. Show me the results and your reasoning.
3. **Sprint 1:** generate it and show me the preview. **STOP.** Create the issues only after I approve.

---

## 22. Tone

Run it like a good real company: professional, direct, specific, human. Make it vivid through the storyline, the merchants and realistic issue threads, but never let narrative crowd out learning. Keep issue text tight, so it reads like a real ticket and not like a story.