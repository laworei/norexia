# Sprint 0: Onboarding and diagnostic (PREVIEW, nothing created on GitHub yet)

**Length:** one weekend (Sat + Sun, ~10 h). Not a normal sprint: it sets your starting level and competency states. **No AI help, closed book** (official Go docs only: go.dev/doc, pkg.go.dev, A Tour of Go, `go help`, `go doc`). Use `/stuck` if blocked; hints are logged and lower the score honestly, they are not a penalty.

**Rules:** one ticket at a time. Write your code under `cmd/` and `internal/` (Claude cannot touch them). `make check` must pass before each PR (CI also runs it). PRs go through `/review` as usual, so you also learn the flow.

---

## ONB-1: Set up your engineering environment and join the team [chore, L0]
**Persona:** Priya Raman (eng-manager) · **Estimate:** 2 h

**Business context.** Welcome to Norexia. Before you touch the product, Priya wants your machine set up the way the team's is, and one small change merged so the whole PR flow is familiar.

**Requirements / acceptance criteria (fully specified).**
- [ ] Go is the current stable release (`go version`; the program targets 1.27.4 as of 2026-11-14; you have 1.25.5, so upgrade with the official installer or `brew upgrade go`). `go.mod` stays as is for now.
- [ ] Editor has **AI autocomplete off** (Copilot, Cursor Tab, etc.), with `gopls` working: go-to-definition and format-on-save with `gofmt`.
- [ ] `gh auth status` is green; `make check` passes in a fresh clone of `laworei/norexia`.
- [ ] Read `README.md`, `handbook/ladder.md`, `handbook/ai-policy.md`, `handbook/hint-ladder.md`.
- [ ] On a branch `onboarding/<yourname>`, add yourself to `company/TEAM.md` (name, handle, start date, one thing you want to get good at). Open a PR using the template and run `/review <PR#>`. Reply to any comment, then merge.
- [ ] Create your own `learner/brag-doc.md` (Claude cannot) with one line: today's date and what you did.

**Competencies:** TOOL.1, TOOL.3, COMM.1, AIE.1 · **Reading:** `README.md`; Learning Go, ch. 1 (Setting Up Your Go Environment) and ch. 9 (Modules, Packages, and Imports) · **Deliverable:** merged PR, 2 flashcards.
**Constraints:** not closed-book (setup task). **Definition of done (L1):** PR description complete, review replied to.

---

## Diagnostic tasks (closed-book, ~1 h each, in any order after ONB-1)

Each task has a **timebox**: if it is not working at the end, stop, write what you tried in the PR, and move on. Partial work is useful data. Tests are part of every task; write them.

### DIAG-1: Word frequency CLI [closed-book, L0-L1] · GO.1, GO.3, TOOL.3
Business context: Support wants to see which words appear most in customer emails.
- [ ] `cmd/diag-wordfreq` reads text from stdin and prints the top N words (default 10, flag `-n`), one per line as `count word`, most frequent first, ties alphabetical, case-insensitive, punctuation ignored.
- [ ] Empty input prints nothing and exits 0. Invalid `-n` exits with status 2 and a message on stderr.
- [ ] Logic lives in a function in `internal/diag` that is unit tested.

### DIAG-2: Config line parser [closed-book, L1] · GO.2, TEST.1
Business context: A legacy tool exports settings as `key=value` lines.
- [ ] `internal/diag` exposes a parser from lines to a map; blank lines and lines starting with `#` are skipped; whitespace around keys and values is trimmed.
- [ ] A malformed line returns an error that says which line number and why; duplicate keys are an error.
- [ ] Table-driven tests with subtests cover valid and each invalid case; `errors.Is`/`errors.As` usage is visible in at least one test.

### DIAG-3: Find duplicates [closed-book, L1] · CSF.1, CSF.2, CSF.3
Business context: Billing found duplicate invoice IDs in an export.
- [ ] Write a function returning the IDs that appear more than once, in first-seen order, for `[]string` input.
- [ ] Write a second version that sorts first. Add a short comment on each stating time and memory complexity, and a benchmark comparing both on 10k, 100k, 1M items.
- [ ] One paragraph in the PR: which would you ship and why.

### DIAG-4: Git, from a conflict [closed-book, L1] · TOOL.1
- [ ] In a scratch repo (not Norexia), create two branches that edit the same lines, merge one into `main`, resolve the conflict from the markers by hand, then rebase the other branch onto `main`. Put the exact commands you ran and what each did in the PR description. No GUI.

### DIAG-5: Tiny HTTP service [closed-book, L1-L2] · API.1, API.2, NET.3, TEST.1
Business context: Pomelo Press wants a health and echo endpoint to wire into their monitoring.
- [ ] `cmd/diag-http` serves `GET /healthz` (200, body `ok`) and `POST /echo` accepting `{"message": "..."}` and replying with the same JSON.
- [ ] Bad JSON, missing `message`, or a body over 1 KB gets a JSON error response with a sensible status code. Wrong method gets 405.
- [ ] The server sets read/write/idle timeouts. Handlers are tested with `net/http/httptest`.

### DIAG-6: Parallel sum with cancellation [closed-book, L1-L2] · CONC.1, CONC.2, CONC.3
Business context: A job totals usage numbers across 100 files in parallel.
- [ ] A function `Sum(ctx context.Context, files []string) (int64, error)` reads each file (one integer per line) with at most 4 goroutines at once.
- [ ] It stops early when the context is cancelled or any file errors, and leaves no goroutines running after it returns.
- [ ] Tests pass with `-race`, including a test for cancellation.

### DIAG-7: SQL on paper [closed-book, L1-L2] · DATA.1, DATA.3
Schema: `projects(id, name, owner_id, plan, created_at)`, `backups(id, project_id, status, bytes, started_at)`.
- [ ] Write queries in `docs/sprints/diag-sql.md` for: (a) the number of failed backups per project in the last 7 days, only projects with >= 3; (b) projects with no backup ever; (c) total bytes per plan; (d) the latest successful backup per project. Add one sentence on which index you would add for (a) and why.

### DIAG-8: Explain-back interview [oral, 30 min] · COMM.3, GO.1
Priya picks two of your merged diagnostic PRs. You explain, without looking at the code, how it works, why this design, what breaks, and one alternative. (Use `/explain-back <PR#>`.)

---

## How the result is used
Starting level (L0 or L1), initial states for the covered subcodes (`assisted` if hints were needed, otherwise provisional), and the calibration of Sprint 1 difficulty. A small number of results can lower or raise the level. You will see the rubric and my reasoning after the diagnostic (rubric sealed until then).
