# Sprint 1 (PROVISIONAL PREVIEW, nothing created on GitHub)

**Provisional because** your starting level is set by the Sprint 0 diagnostic. This preview assumes the likely outcome (**L1**, with some L0 support). After the diagnostic I adjust sizes and swap tickets, and show you the final version before creating anything.

**Dates:** the two weekends after Sprint 0 · **Capacity:** 10 h/week x 2 x 0.7 = **14 h planned** · **WIP limit:** 1 · **Quarter:** Q1, Launch hardening (OKR O1: backup success >= 99%; O3: API v1)

## Method layer (Ultralearning + Deep Work)
- **Wildly Important Goal:** "By the end of Sprint 1, a running `norexia-api` serves `GET /projects/{id}` with validated names and a tested report CLI, all merged with first-pass approval at 50% or better." (lag: merged tickets, approval rate)
- **Lead measures:** 240 deep minutes in each of the two weeks (the target ramps +30 per sprint from Sprint 2 if you hit 90% of it); 2 retrieval sessions per week (free recall at start and end of each session counts); 6 flashcards added per week; at least 2 uninterrupted 90-minute blocks per weekend.
- **Drill:** S1-4 uses the proactive types: *isolate-and-repeat* on the weakest sub-skill from the diagnostic, in 20-minute reps.
- **Spaced regression:** a 20-minute re-do of DIAG-2's error-handling idea inside S1-2 (no looking at old code).
- **Test before study:** before each reading pointer, write down what you expect it says (5 min), then read; the gap is the lesson.
- **North-star increment:** S1-1 to S1-3 together are the first end-to-end slice of your API v1.
- **Method experiment (E1):** *test-first vs code-first.* Do S1-1 test-first and S1-2 code-first (or the reverse, your choice up front). Measure: review rounds, time to green, number of bugs found in review. Decision at the retro.
- **Depth tagging:** S1-1, S1-2, S1-3, S1-4, S1-5 are deep. PR replies and flashcard sessions are shallow; keep them under 25%.

## Mix (L1: 60% delivery, 25% drill, 15% retrieval) and difficulty reasoning
| Slice | Hours | Tickets |
|---|---|---|
| Delivery | 8.0 | S1-1, S1-2, S1-3 |
| Drill | 3.5 | S1-4 (slot; topic chosen from diagnostic gaps) |
| Retrieval | 2.5 | S1-5 (closed-book) |

No performance data exists yet, so difficulty starts at the default (fully specified L1 tickets with hints). The retro adjusts it: first-pass approval above 75% means vaguer specs next sprint, below 50% means smaller tickets and more drills. Competencies are interleaved: GO, TEST, API, NET, CONC, DATA, TOOL, COMM.

---

### S1-1: Backup success report for support [feature, L1, 2.5 h] · owner: Hana Weiss (product-manager)
**Business context.** Support needs to see which projects are below the 99% backup success target (OKR O1) without asking an engineer for a query.
**Requirements / acceptance criteria.**
- [ ] `cmd/backup-report` reads JSON Lines from a file path argument or stdin. Each line: `{"project":"...","status":"ok|failed","at":"RFC3339"}`.
- [ ] Output, sorted by success rate ascending then project name: `project  total  failed  success%` with one decimal. A final line lists projects under 99%.
- [ ] A malformed line is reported with its line number on stderr, processing continues, and the exit code is 1 at the end. A missing file exits 2.
- [ ] Logic is in `internal/report` and covered by table-driven tests (including an empty file and a project with a single record).
**Competencies:** GO.1, GO.2, TEST.1, TOOL.3 · **Reading:** Learning Go, ch. 8 (Errors), ch. 13 (Writing Tests); The Power of Go: Tests, ch. 1 · **Deliverable:** merged PR + 3 flashcards.
**Hints available:** location (which std packages), then structure. **DoD (L1):** `make check` clean, `-race`, PR description complete.

### S1-2: Validate project names [feature, L1, 2.5 h] · owner: Hana Weiss
**Business context.** Pomelo Press created a project named with trailing spaces and emoji and broke their dashboard. We need rules on the API before v1 (OKR O3).
**Requirements / acceptance criteria.**
- [ ] `internal/project` exposes `ValidateName(string) error`. Rules: 3 to 40 characters after trimming; letters, digits, space, `-` and `_` only; must start with a letter; no two consecutive spaces.
- [ ] Errors identify the rule that failed and can be checked with `errors.Is` against exported sentinel errors.
- [ ] Table-driven subtests list each rule's passing and failing boundary (2, 3, 40, 41 characters, unicode, emoji).
- [ ] Add a short `Example` function that shows usage and appears in `go doc`.
**Competencies:** GO.2, GO.3, TEST.1, API.2 · **Reading:** Learning Go, ch. 8; Let's Go Further, ch. 4 (validation ideas, not the code) · **Deliverable:** PR + flashcards.

### S1-3: Project lookup endpoint [feature, L1, 3 h] · owner: Tomasz Wrona (staff-engineer)
**Business context.** The console needs to show a project's details. API v1 starts with one read endpoint over an in-memory store.
**Requirements / acceptance criteria.**
- [ ] `cmd/norexia-api` serves `GET /projects/{id}` using only `net/http` routing, with an in-memory store behind a small interface defined in the handler package.
- [ ] 200 with JSON `{"id","name","plan","created_at"}`; 404 with `{"error":{"code":"not_found","message":"..."}}`; 405 for other methods; consistent error shape for all errors.
- [ ] Server has read-header, read, write and idle timeouts, and shuts down cleanly on SIGINT/SIGTERM.
- [ ] Handler tests with `net/http/httptest`; a fake store, not a mock framework.
**Competencies:** API.1, NET.3, GO.4, REL.1, TEST.1 · **Reading:** Let's Go Further, ch. 3 (Sending JSON Responses); Learning Go, ch. 12 (The Context) · **Deliverable:** PR + explain-back in the 1:1.

### S1-4: Drill slot [drill, L1, 3.5 h] · owner: Priya Raman
Topic chosen after the diagnostic from the weakest area (recurring-finding rule does not apply yet). Likely candidates: errors and `%w` (GO.2), table tests (TEST.1), goroutine lifecycle (CONC.3), SQL basics (DATA.1). Format: 3-4 small closed-book exercises of 45 min each, one PR, one explain-back.

### S1-5: Closed-book retrieval [closed-book, L1, 2.5 h] · owner: Priya Raman
**Business context.** Priya wants proof you kept what you learned, not that you can find it again.
**Requirements.**
- [ ] Without opening your Sprint 0 code, re-implement the diagnostic task you found hardest, within the original timebox. No AI, no web except official Go docs.
- [ ] PR description: compare your two versions and write down three differences.
**Competencies:** per task (likely CONC.1-3 or GO.2) · **Constraints:** closed-book · **Deliverable:** PR + flashcards for anything you forgot.

---

## Not in this sprint (and why)
- **Code-reading of `legacy/snapshotd`:** Sprint 2 (you need more Go first; the daemon has real flaws to find).
- **On-call and incidents:** from L2.
- **Docker, Postgres, migrations:** L2.
- **Scope changes from the product-manager:** from L2.

## Approval flow
1. You approve **Sprint 0** (ONB-1 and DIAG-1..8): I create those issues, the milestone and labels.
2. After the diagnostic I confirm your level and update this preview. You approve again; only then do I create Sprint 1 issues.
