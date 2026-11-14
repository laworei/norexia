# Sprint 0 (v2, novice edition): Foundations and gentle diagnostic

**Who this is for:** you, with very basic Go. **Goal of the sprint:** by the end you have written, tested and shipped (via pull request) several small Go programs, you know the workflow, and we have an honest read on your starting level. It is **not** an exam. Stopping early is fine and tells us where to start.

**Length:** one sprint = two weekends, about 14 planned hours (9.5 h of tasks below + slack). Order matters: do them in order, one at a time.
**Weekend shape:** `/session-start`, two 90-minute deep blocks, a shallow block for the PR, `/session-end` (see `handbook/deep-work.md`). Target: 240 deep minutes for the week; do not cram.

| Weekend | Tasks |
|---|---|
| 1 | N0-1, N0-2, N0-3 (Saturday); N0-4, N0-5, N0-6 (Sunday) |
| 2 | N0-7, N0-8, N0-9 (and catch-up) |

**Rules for every task**
- **No AI help** (no Copilot, no chat assistants, no pasted code). Allowed: A Tour of Go, go.dev/doc, pkg.go.dev, `go doc`, the books in your library, and `/stuck`.
- **Type the code yourself**, even when an example is in front of you. Do not copy and paste.
- **Predict, then run:** before each run, write on paper what you expect to see. Different from expected? That gap is the lesson.
- **Timebox:** 30 minutes of honest effort before `/stuck <issue#>`. Asking is normal, and every hint is just logged to set the right difficulty.
- **Each task ends** with: the success check passing, a PR, and 2 flashcards.
- Your Go code lives in `cmd/` and `internal/` (Claude cannot touch them; that is the point).

Everything below is tagged **deep** (needs focus) or **shallow** (admin).

---

## N0-1: Set up your tools and run your first Go program [chore, L0, 1.25 h, shallow+deep] · TOOL.3
**Why.** Priya (your manager) wants your machine ready like the team's, so nothing gets in the way later.
**You will learn:** the terminal basics, what `go run` and `go build` do, how the repo is laid out.
**Steps.**
1. Upgrade Go to the current stable release (the program targets 1.27.4). Check with `go version`. If you use Homebrew: `brew upgrade go`; otherwise download the installer from go.dev/dl.
2. In your editor: turn **AI autocomplete off** (Copilot, Cursor Tab, any "ghost text"). Install the Go extension so `gopls` formats on save and shows errors.
3. Check `gh auth status` is logged in as `laworei`.
4. Clone the repo: `git clone https://github.com/laworei/norexia` and `cd norexia`. Run `make check`. (It should pass; the `0.0% coverage` line is normal.)
5. Create a scratch folder **outside** the repo (e.g. `~/go-scratch/hello`). Run `go mod init scratch/hello`, create `main.go` with a `main` function that prints "hello, Norexia", then run it with `go run .`. Then `go build` and run the produced file.
**Success check.** `go version` shows the new version; `make check` passes; your scratch program prints the greeting both with `go run .` and as a built binary.
**Reading.** A Tour of Go: the "Welcome" and "Packages, variables, and functions" intro pages; *Learning Go* ch. 1 (Setting Up Your Go Environment).
**If stuck.** Typical blocks: `command not found: go` (PATH), editor not showing errors (install `gopls`). Try 30 min, then `/stuck`.
**Deliverable.** Nothing to merge. Put a note in `learner/journal.md` of what surprised you, and 2 flashcards.

## N0-2: A Tour of Go, the basics [drill, L0, 1.5 h, deep] · GO.1
**Why.** Everything after this uses these basics: variables, functions, if/for, slices, maps, structs.
**You will learn:** the core syntax by doing small exercises in the browser.
**Steps.**
1. Do the Tour's **Basics** module (Packages, Functions, Variables, Flow control, More types) at go.dev/tour. Do the exercises; do not skip to the solutions.
2. **Test before study:** before each Tour section, jot what you already guess it means in one line; afterwards, fix your guess.
3. Close the Tour. On paper, write from memory: how you declare a variable, write a function with two return values, loop over a slice, and make a map. Then check yourself against the Tour.
**Success check.** You finish the Basics module and your paper recall is mostly right (it is fine if it is not; the gaps become flashcards).
**Reading.** *Learning Go* ch. 2 (Primitive Types and Declarations) and ch. 3 (Composite Types): skim; keep it open as a reference.
**Deliverable.** 5 flashcards from your recall gaps (`python3 scripts/flashcards.py add ...` or ask in `/session-end`).

## N0-3: Your first pull request: join the team [chore, L0, 1 h, shallow] · TOOL.1, COMM.1
**Why.** Every change at Norexia goes through a pull request and a review. Learn the loop on something harmless.
**Steps.**
1. `git switch -c onboarding/<yourname>` to make a branch.
2. Open `company/TEAM.md` and add yourself under "New joiners": name, GitHub handle (`laworei`), start date, one thing you want to get good at.
3. `git add company/TEAM.md`, `git commit -m "Add <name> to the team"`, `git push -u origin onboarding/<yourname>`.
4. Open the PR with `gh pr create` (or the GitHub page). Fill the PR template honestly (including the AI-use line).
5. In Claude Code, run `/review <PR number>`. Read each comment. Reply to every `blocking` and `should-fix` one (even "done, thanks").
6. When `review:approved` appears and CI is green, merge the PR (squash is fine). Then `git switch main && git pull`.
**Success check.** Your line is on `main` in `company/TEAM.md`.
**Reading.** `handbook/review-guide.md` (5 minutes).
**Deliverable.** The merged PR; 2 flashcards (the commands you had to look up).

## N0-4: Greeter, your first real program [feature, L0, 1 h, deep] · GO.1, GO.3
**Business context.** Support wants a tiny command that greets a customer by name when they open a ticket.
**What to build.** `cmd/greeter` (a program in your repo) that takes a name as a command-line argument and prints a greeting.
**Behaviour (examples).**
| You run | It prints | Exit code |
|---|---|---|
| `go run ./cmd/greeter Ada` | `Hello, Ada! Welcome to Norexia.` | 0 |
| `go run ./cmd/greeter` (no name) | `usage: greeter <name>` (to stderr) | 2 |
| `go run ./cmd/greeter Ada Lovelace` (two words) | `Hello, Ada Lovelace! Welcome to Norexia.` | 0 |
**Steps.** Create the folder; write `main.go`; run it for the three cases above; run `make check`; open a PR (same flow as N0-3) with the three runs pasted in the description.
**Starter pointers (ticket scaffolding).** Command-line arguments are in the `os` package (`go doc os.Args`); to join strings see the `strings` package; to write to stderr use `fmt.Fprintln` with `os.Stderr`; to exit with a code see `os.Exit`.
**Success check.** All three runs match the table exactly.
**Reading.** *Learning Go* ch. 5 (Functions), the "Command-line arguments" part is in the Go docs for `os`. Try first, read when stuck.
**Deliverable.** Merged PR; 2 flashcards.

## N0-5: Your first test [feature, L0, 1.25 h, deep] · TEST.1, GO.1
**Business context.** The greeting logic must not break when someone edits it. A test protects it.
**What to build.** Move the greeting logic out of `main` into a function `Greeting(parts []string) (string, error)` in `internal/greet` (an error when no name is given). `main` calls it. Then write tests for it.
**Behaviour.** Same rules as N0-4: a single name, a multi-word name, and no name (error).
**Steps.**
1. Before coding, write on paper 4-5 input/output examples (the table in N0-4 is a start; add an empty-string name and a name with extra spaces, then decide what is right).
2. Write the test **first** (`internal/greet/greet_test.go`): a table-driven test with one case per example, using subtests (`t.Run`).
3. Run `go test ./...` and see it fail (red). Then write the function until it passes (green).
4. Run `go test -race -cover ./...` and `make check`.
**Success check.** `go test ./...` passes; each failure message would tell a stranger which case failed and what was expected vs got.
**Starter pointers.** `go doc testing`; table-driven tests and `t.Run` are in *Learning Go* ch. 13 (Writing Tests) and *The Power of Go: Tests* ch. 1. Failure messages usually look like `Greeting(%q) = %q, want %q`.
**Deliverable.** Merged PR (reviewed via `/review`); 3 flashcards. This task is also **Experiment E0's first data point**: note in your journal how much you recalled at `/session-start`.

## N0-6: Count the words [feature, L0, 1.25 h, deep] · GO.1, CSF.1
**Business context.** Support wants to know which words appear most in customer emails. Start with the counting part.
**What to build.** A function `CountWords(text string) map[string]int` in `internal/diag` and a command `cmd/wordcount` that reads **one line** passed as arguments and prints each distinct word with its count, in alphabetical order, as `word count`.
**Rules.** Words are separated by whitespace. Case-insensitive (`Go` and `go` are the same word). Ignore punctuation attached to words (`go,` counts as `go`). Empty input prints nothing and exits 0.
**Examples.**
| Input | Output |
|---|---|
| `go is fun, Go is fast` | `fast 1`, `fun 1`, `go 2`, `is 2` (one per line) |
| (nothing) | nothing |
**Steps.** Examples on paper first; write the test first; make it pass; then the command; then `make check`; PR with the example runs pasted in.
**Starter pointers.** `go doc strings.Fields`, `go doc strings.ToLower`, `go doc strings.Trim`; sorting keys: `go doc sort.Strings` (maps have **no order**; find out why). *Learning Go* ch. 3 (maps, slices).
**Success check.** The test table covers: normal, mixed case, punctuation, empty, repeated words.
**Stretch (optional, no penalty):** read lines from standard input instead of arguments.
**Deliverable.** Merged PR; 3 flashcards.

## N0-7: Parse a setting line, with errors [feature, L0 to L1, 1.25 h, deep] · GO.2, TEST.1
**Business context.** An old tool exports settings as `key=value`. We need to read them, and reject bad lines clearly.
**What to build.** `ParseLine(line string) (key, value string, err error)` in `internal/diag`.
**Rules.** `host = db1` gives `host`, `db1` (spaces around key and value trimmed). A blank line or a line starting with `#` is an error that says it is empty or a comment (decide a good error). A line without `=` is an error. An empty key is an error. A value may be empty.
**Steps.** Write examples on paper (at least 8, including all error kinds); test first; make it pass; error messages should say what was wrong.
**Starter pointers.** `go doc strings.Cut`; creating errors: `errors.New` and `fmt.Errorf`; *Learning Go* ch. 8 (Errors), read the first half; define one **sentinel error** (`var ErrNoEquals = errors.New(...)`) and check it in a test with `errors.Is`.
**Success check.** Table-driven test with a case per example; at least one test uses `errors.Is`.
**Stretch (optional):** a function that parses many lines and reports the **line number** of the first bad line.
**Deliverable.** Merged PR; 3 flashcards.

## N0-8: Explain it back [oral, L0, 0.5 h, deep] · COMM.3
**Why.** Writing it is half the skill; explaining it shows you own it.
**What happens.** Run `/explain-back <PR#>` for two of your merged PRs (suggest N0-5 and N0-6). Without looking at the code, you explain what it does, why you built it that way, what could break, and one alternative. It is friendly; "I do not know" is a good answer when true.
**Prep.** 5 minutes of **free recall** on paper first: draw the function and its test from memory.
**Success check.** No pass/fail; the result sets which parts of the code you really understand.
**Deliverable.** The interview result in the journal; 2 flashcards for gaps.

## N0-9: Metalearning lite: what does the job ask? [chore, L0, 1 h, deep] · COMM.1
**Business context.** Before investing months, Priya wants you to look at what real employers ask for, and to say why you are doing this.
**Steps.**
1. Create `learner/metalearning.md` from `handbook/templates/metalearning.md`. Fill only the **Why** section in your own words (no AI-written text) and **3** "what I must master".
2. Find **5 real job posts** for Go backend or platform engineers (link and date seen). Write the skills that repeat. Note any that are missing from `handbook/competencies.md`.
3. Pick **one** method hypothesis to test in Sprint 1 (e.g. "tests first helps me finish faster").
**Success check.** The file exists, with at least 5 links, 3 repeating skills, and one hypothesis.
**Reading.** `handbook/learning-method.md` §1 and §9.
**Deliverable.** PR with the file. Priya reviews it in a 1:1.

---

## How the result is used
Your starting level (L0 or L1) and first competency states come from how N0-4 to N0-7 went (did you need hints, did the tests make sense, could you explain it). The rubric is sealed until then. **Not finishing everything is a normal outcome**: it tells us where Sprint 1 starts.

## What comes after
Sprint 1 preview: `docs/sprints/sprint-1-preview.md` (to be re-cut for novice level after this sprint). HTTP services, concurrency and SQL start in Sprint 1 and 2, not here.
