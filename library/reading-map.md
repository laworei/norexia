# Reading map

This file is committed. The books in `library/` are not (gitignored), and no book text is copied here beyond titles and chapter numbers.

- Cite as: `Book, ch. N (title)`. Quotes are at most one line.
- Chapter numbers below come from each book's own table of contents (first pages of the PDF, or the EPUB nav file). Where a book's TOC showed no chapter numbers, it is cited by title and marked "(by title)".

## Reading rules

1. Reading is at most 20% of weekly time. The rest is building, reviewing and fixing.
2. Just in time: read the chapter for the competency a ticket needs this sprint, not ahead of it.
3. Every reading ends in a deliverable: a ticket (or ticket comment), flashcards in `learner/flashcards.csv`, or an explain-back to the relevant persona. A reading with no deliverable did not happen.
4. Books are references, not a syllabus. Skim the chapter, build the thing, then return to the text to check your understanding.

## Library

Level fit uses L0 (before first sprint) to L4. "Spine" is the intended core list.

| Book | Author (if visible) | Format | Level fit | How to use | Notes / gap |
|---|---|---|---|---|---|
| Learning Go (O'Reilly, 2021) | Jon Bodner | PDF | L0-L2 | Spine language text. Read by chapter alongside GO and CONC tickets. | Spine. 2021 edition; ch. 15 on generics is a preview of 1.18, so check the Go release notes for current generics, iterators and `slices`/`maps`. |
| Let's Go | Alex Edwards | PDF | L1-L2 | Build-along for HTTP, middleware, forms, sessions, auth, testing. Use as reference for NET, API, SEC basics. | Spine. Uses a server-rendered app, not a JSON API. Go version may be dated. |
| Let's Go Further (2022) | Alex Edwards | PDF | L1-L3 | JSON API, Postgres, migrations, rate limiting, graceful shutdown, auth, metrics, deploy. Closest match to the program's service stack. | Spine. Uses `httprouter`/older idioms; stack defaults (stdlib `net/http`, `log/slog`, pgx) need an ADR when you diverge. |
| Concurrency in Go | Katherine Cox-Buday | PDF | L2-L4 | Read for CONC patterns and runtime. Predates `errgroup` and `context` ubiquity, so pair with Learning Go ch. 12. | Spine. |
| Cloud Native Go (O'Reilly, 2021) | Matthew A. Titmus | PDF | L2-L4 | Reliability patterns, observability, manageability. Best single book for DIST, REL, OBS. | Spine. |
| Shipping Go | Not visible in TOC (see duplicates) | EPUB | L1-L3 | CI/CD, testing pyramid, containers, config, integration tests, Kubernetes deploy. Use for PLAT and TOOL. | Not in the spine, but covers the PLAT gap well. Toc header in the file reads oddly ("Effective Concurrency in Go") but the chapter list is that of Shipping Go. |
| The Power of Go: Tests | Not visible in TOC | PDF | L1-L3 | TEST habits: failing test first, fuzzing, mutation, testing the untestable. | Partly fills the missing Learn Go with Tests. |
| The Power of Go: Tools | Not visible in TOC | PDF | L1-L3 | Idiomatic CLI and tool building: flags, files, filesystems, commands, pipelines. | Supports TOOL.9. |
| Know Go (Go 1.23 edition) | Not visible in TOC | PDF | L2-L3 | Generics, iterators, constraints. Use for GO.7 and GO.8. | Chapter 4 not seen in the TOC extract. |
| Effective Go Recipes | Miki Tebeka | PDF | L1-L3 | Task-sized recipes: I/O, serialisation, HTTP, concurrency, testing, building, shipping. Lookup reference. | Not in the spine. |
| Powerful Command-Line Applications in Go | Ricardo Gerardi | PDF | L1-L3 | Cobra, files, processes, REST clients, distribution. Use for TOOL.9 tickets. | Not in the spine. |
| Go Systems Programming | Mihalis Tsoukalos | PDF | L2-L3 | Files, processes, signals, goroutines. Use for CSF.5/CSF.7 and REL.1 (signals). | TOC read to ch. 11; may have later chapters. Not in the spine. |
| Go Programming Cookbook | Not visible in TOC | PDF | L1-L3 | Lookup recipes for APIs, gRPC, microservices, DB, performance. | Chapters 1-9 seen. Quality uneven; verify against official docs. |
| Go Design Patterns | Not visible in TOC | PDF | L2-L3 | Classic GoF patterns in Go. Read critically; many are not idiomatic. | TOC text is mis-encoded in the PDF; chapter titles were decoded but have no visible numbers. Cited by title only. |
| Object-based Programming with Go | Christian Maurer | PDF | L3-L4 | Large project walkthroughs. Low priority. | Not in the spine. Mostly off-program. |
| Domain-Driven Design with Golang | Not visible in TOC | EPUB | L3-L4 | ARCH.8 domain modelling (entities, value objects, aggregates). | Not in the spine. |
| Go with Domain (Three Dots Labs) | Miłosz Smółka, Robert Laszczak | PDF | L3-L4 | Clean architecture, repository pattern, DB integration tests, CQRS, test architecture. | Strong on ARCH and TEST.10. Free-ware origin. |
| Event-Driven Architecture in Golang | Michael Stack | EPUB | L3-L4 | Event sourcing, async messaging, transactional messaging, testing, observability. | Fills DIST.7 (outbox). |
| Building Distributed Systems with Go and NATS | Not visible in TOC | PDF | L3-L4 | NATS fundamentals, sync vs async systems, DDD for systems. | Fits DIST.6. |
| gRPC Microservices in Go | Hüseyin Babal | PDF | L3-L4 | gRPC services, resilience, testing, deployment, observability. | Fits NET.7. |
| Kubernetes Programming with Go | Philippe Martin | PDF | L4 (L3 optional) | client-go and operators. | Only for PLAT.11. TOC read to ch. 6 only. Not a replacement for Kubernetes Up & Running. |
| Build an Orchestrator in Go (From Scratch) | Tim Boring | PDF | L3-L4 | Build a mini orchestrator: worker, manager, scheduler, store. Stretch project for PLAT and CONC. | Not in the spine. |
| Build Your Own Database From Scratch | James Smith | PDF | L3-L4 | B-tree, persistence, free list, transactions. Use for CSF.7, CSF.11 and DATA.7. | Language-agnostic; written in Go. Not in the spine. |

### Spine check

| Spine item | In library? | Substitute (free or official) |
|---|---|---|
| Learn Go with Tests | Missing | Partial: The Power of Go: Tests. Free: https://quii.gitbook.io/learn-go-with-tests. Also A Tour of Go (go.dev/tour) for L0. |
| Learning Go | Present | None needed. |
| Let's Go | Present | None needed. |
| Let's Go Further | Present | None needed. |
| 100 Go Mistakes | Missing | Effective Go (go.dev/doc/effective_go), Go Code Review Comments (go.dev/wiki/CodeReviewComments), Go FAQ, and Go blog posts. 100go.co has the free summary list. |
| Concurrency in Go | Present | Go memory model (go.dev/ref/mem) for CONC.7. |
| Cloud Native Go | Present | None needed. |
| Kubernetes Up & Running | Missing | Kubernetes docs (kubernetes.io/docs, "Concepts" and "Tasks"), plus Shipping Go ch. 7 and 10. |
| Designing Data-Intensive Applications | Missing | Postgres docs (Concurrency Control, Indexes, EXPLAIN), Jepsen consistency map, Build Your Own Database From Scratch for storage-engine internals, EDA in Golang for messaging. |
| SRE book / workbook | Missing | Google SRE book and workbook online (sre.google/books). Free. |
| Platform Engineering | Missing | Partial: Shipping Go; CNCF Platforms White Paper; Kubernetes docs. |

## Competency -> reading

Only chapters seen in a TOC are cited. "Free ref" means official or free documentation to use where books are weak. Subcode ranges: .1-.3 L1, .4-.6 L2, .7-.9 L3, .10-.12 L4.

| Area | Best book + chapter | Key subcodes | Free ref |
|---|---|---|---|
| GO | Learning Go, ch. 2 (Primitive Types and Declarations), ch. 3 (Composite Types), ch. 5 (Functions), ch. 6 (Pointers), ch. 7 (Types, Methods, and Interfaces), ch. 8 (Errors), ch. 9 (Modules, Packages, and Imports), ch. 15 (A Look at the Future: Generics in Go). Know Go, ch. 1 (Interfaces), ch. 2 (Type parameters), ch. 3 (Constraints), ch. 11 (Iterators). | GO.1-2: Learning Go ch. 3, 8. GO.3: ch. 1 (Setting Up Your Go Environment), ch. 9. GO.4-5: ch. 7, ch. 6. GO.6: ch. 8. GO.7: Know Go ch. 2-3. GO.8: Know Go ch. 11. GO.9: Learning Go ch. 9. | Tour of Go, Effective Go, Go spec, Go release notes, Go Code Review Comments. |
| TEST | The Power of Go: Tests, ch. 1 (Programming with confidence), ch. 2 (Tools for testing), ch. 3 (Communicating with tests), ch. 6 (Fuzzy thinking), ch. 8 (Testing the untestable), ch. 10 (Dependence day), ch. 11 (Suite smells). Learning Go, ch. 13 (Writing Tests). Shipping Go, ch. 3 (Introducing continuous testing), ch. 6 (Testing frameworks, mocking, and dependencies). | TEST.1-3: Power of Go: Tests ch. 2-4; Learning Go ch. 13. TEST.5: Shipping Go ch. 6 (stubs, mocks, fakes). TEST.7: Power of Go: Tests ch. 6. TEST.4: Go with Domain, ch. 8 (High-Quality Database Integration Tests). TEST.10: Go with Domain, ch. 12 (Tests Architecture); Shipping Go ch. 3.4 (Testing pyramid). | `go.dev/doc/fuzz`, `testing` package docs, testcontainers-go docs. TEST.8 and TEST.9: no precise chapter seen; use the `testing` docs and Concurrency in Go ch. 4. |
| TOOL | The Power of Go: Tools, ch. 7 (Commands), ch. 8 (Shells), ch. 9 (Pipelines). Powerful CLI Applications in Go, ch. 7 (Using the Cobra CLI Framework), ch. 11 (Distributing Your Tool). Shipping Go, ch. 5 (Code quality enforcement). | TOOL.3: Shipping Go ch. 5. TOOL.9: Powerful CLI ch. 1-2, 7, 11; Power of Go: Tools ch. 3-4. TOOL.7: Shipping Go ch. 5 (lint, static analysis). | Pro Git (git-scm.com/book), Delve docs, golangci-lint docs, `go help` pages. TOOL.4, TOOL.6, TOOL.8: no good chapter in the library. |
| CSF | Build Your Own Database From Scratch, ch. 01 (Files vs Databases), ch. 03 (B-Tree: The Ideas), ch. 06 (Persist to Disk). Go Systems Programming, ch. 4 (Go Packages, Algorithms, and Data Structures), ch. 5 (Files and Directories), ch. 6 (File Input and Output), ch. 8 (Processes and Signals). | CSF.5: Go Systems Programming ch. 8. CSF.7: Build Your Own Database ch. 01, 06; Go Systems Programming ch. 6. CSF.11: Build Your Own Database ch. 03-05. | CSF.1-4, 6, 8-10: no strong book in the library. Use the Go spec, `container/*` and `sort` docs, a free algorithms course, and Go GC guide (go.dev/doc/gc-guide) for CSF.9. |
| NET | Let's Go Further, ch. 12 (Graceful Shutdown). Let's Go, ch. 6 (Middleware), ch. 10 (Security improvements). gRPC Microservices in Go, ch. 3 (Getting up and running with gRPC and Golang), ch. 5 (Interservice communication), ch. 6 (Resilient communication). Effective Go Recipes, ch. 3 (Utilizing HTTP), ch. 11 (Working with Sockets). | NET.3: Effective Go Recipes ch. 3. NET.7: gRPC Microservices ch. 3, 5, 6. NET.5: Let's Go ch. 3 and Further ch. 12 give practical server setup; verify timeouts in the `net/http` docs. | `net/http` docs, Cloudflare and Go blog posts on timeouts, MDN HTTP, `dig`/`curl`/`openssl` man pages, Wireshark docs. NET.1, 2, 4, 6, 8-12: no chapter seen. |
| API | Let's Go Further, ch. 3 (Sending JSON Responses), ch. 4 (Parsing JSON Requests), ch. 9 (Filtering, Sorting, and Pagination), ch. 11 (Rate Limiting), ch. 10 (Structured Logging and Error Handling). | API.1-2: Further ch. 3-4. API.4: Further ch. 9. API.8: Further ch. 11. API.7 and API.11: gRPC Microservices ch. 1-2 for gRPC vs REST framing. | OpenAPI spec, Google API Design Guide (cloud.google.com/apis/design), RFC 9110, Stripe idempotency docs. API.5, 6, 9, 10, 12: no chapter seen. |
| DATA | Let's Go Further, ch. 5 (Database Setup and Configuration), ch. 6 (SQL Migrations), ch. 7 (CRUD Operations), ch. 8 (Advanced CRUD Operations). Let's Go, ch. 4 (Database-driven responses). Go with Domain, ch. 7 (The Repository Pattern), ch. 8 (High-Quality Database Integration Tests), ch. 13 (Repository Secure by Design). Build Your Own Database From Scratch, ch. 11 (Atomic Transactions), ch. 12 (Concurrent Readers and Writers). | DATA.2-4: Further ch. 5-7. DATA.5, DATA.7: Build Your Own Database ch. 11-12 for mechanics; Postgres docs for isolation. DATA.6: Further ch. 8-9 for queries; Postgres docs for EXPLAIN. | Postgres docs (SQL commands, Concurrency Control, Using EXPLAIN, Indexes), pgx docs, Use The Index, Luke. DATA.8-12: no chapter seen (DDIA is missing). |
| CONC | Concurrency in Go, ch. 2 (Modeling Your Code: Communicating Sequential Processes), ch. 3 (Go's Concurrency Building Blocks), ch. 4 (Concurrency Patterns in Go), ch. 5 (Concurrency at Scale), ch. 6 (Goroutines and the Go Runtime). Learning Go, ch. 10 (Concurrency in Go), ch. 12 (The Context). | CONC.1: Learning Go ch. 10. CONC.3: Learning Go ch. 12; Concurrency in Go ch. 4 (preventing goroutine leaks). CONC.4: Concurrency in Go ch. 3 (sync package). CONC.5, CONC.6, CONC.9: Concurrency in Go ch. 4-5. CONC.11: Concurrency in Go ch. 4 (pipelines). | Go memory model (go.dev/ref/mem) for CONC.7, `go.dev/doc/articles/race_detector`, `golang.org/x/sync/errgroup` docs, Go blog "Pipelines and cancellation". CONC.8: pprof docs. |
| ARCH | Go with Domain, ch. 5 (When to stay away from DRY), ch. 6 (Domain-Driven Design Lite), ch. 9 (Clean Architecture), ch. 11 (Combining DDD, CQRS, and Clean Architecture). Domain-Driven Design with Golang, ch. 3 (Entities, Value Objects, and Aggregates), ch. 5 (Applying Domain-Driven Design to a Monolithic Application), ch. 6 (Building a Microservice Using DDD). Shipping Go, ch. 6 (Testing frameworks, mocking, and dependencies) for dependency injection. | ARCH.5: Shipping Go ch. 6.3 (Dependency injection). ARCH.8: DDD with Golang ch. 3. ARCH.9: DDD with Golang ch. 5-6; Distributed Systems with Go and NATS ch. 9 (A Whole System vs. a Bunch of Services). | ADR practice (adr.github.io), Go blog on package names, Google design doc and RFC guides. ARCH.1-4, 6, 7, 10-12: no precise chapter; use Go Code Review Comments and your own ADRs. Treat Go Design Patterns (by title: Structural, Behavioral patterns) as optional and critical reading. |
| DIST | Cloud Native Go, ch. 4 (Cloud Native Patterns), ch. 8 (Loose Coupling), ch. 9 (Resilience). Event-Driven Architecture in Golang, ch. 1 (Introduction to Event-Driven Architectures), ch. 6 (Asynchronous Connections), ch. 8 (Message Workflows), ch. 9 (Transactional Messaging). Building Distributed Systems with Go and NATS, ch. 1 (Overview of Distributed Systems), ch. 3 (NATS Fundamentals), ch. 12 (Asynchronous Systems). | DIST.2, DIST.4: Cloud Native Go ch. 4, 9. DIST.6: NATS book ch. 3, EDA in Golang ch. 6. DIST.7: EDA in Golang ch. 9. DIST.9: EDA in Golang ch. 8 (workflows and sagas). | NATS docs, Jepsen consistency map, AWS Builders' Library (retries with backoff and jitter), Google SRE book "Addressing Cascading Failures". DIST.1, 3, 5, 8, 10-12: no precise chapter seen in a TOC; DDIA is missing. |
| PERF | Concurrency in Go, ch. 6 (Goroutines and the Go Runtime). Go Programming Cookbook, ch. 9 (Enhancing Performance and Best Practices in Go). Effective Go Recipes, ch. 5 (Working with Functions) is not performance-specific; skip. | PERF.2: Learning Go and Go Programming Cookbook ch. 9 as a start. PERF.7: Concurrency in Go ch. 6 for scheduler context. | Official only: `go.dev/doc/diagnostics`, pprof and `runtime/trace` docs, Go GC guide, benchstat docs, k6 docs. Books in the library are weak here. |
| OBS | Cloud Native Go, ch. 11 (Observability). Let's Go Further, ch. 10 (Structured Logging and Error Handling), ch. 19 (Metrics). gRPC Microservices in Go, ch. 9 (Observability). Event-Driven Architecture in Golang, ch. 12 (Monitoring and Observability). | OBS.1: Further ch. 10 (check against `log/slog`). OBS.5: Further ch. 19; Cloud Native Go ch. 11. OBS.7: Cloud Native Go ch. 11; gRPC Microservices ch. 9. | `log/slog` docs, OpenTelemetry Go docs, Prometheus docs, Google SRE book chapters "Monitoring Distributed Systems" and "Service Level Objectives". OBS.8-12: SRE book. |
| REL | Cloud Native Go, ch. 6 (It's All About Dependability), ch. 9 (Resilience), ch. 10 (Manageability). Let's Go Further, ch. 12 (Graceful Shutdown). Shipping Go, ch. 10 (Advanced deployment). | REL.1: Further ch. 12; Go Systems Programming ch. 8 (Processes and Signals). REL.5, REL.6, REL.9: Shipping Go ch. 10. REL.8: Cloud Native Go ch. 9. | Google SRE book and workbook online (incident response, postmortem culture, SLOs). Kubernetes docs on probes. REL.3, 4, 7, 10-12: SRE books only; none in library. |
| SEC | Let's Go, ch. 10 (Security improvements), ch. 11 (User authentication). Let's Go Further, ch. 16 (Authentication), ch. 17 (Permission-based Authorization), ch. 18 (Cross Origin Requests). | SEC.4, SEC.5: Further ch. 16-17; Let's Go ch. 11. SEC.2: Let's Go ch. 8 (Processing forms), ch. 10. SEC.3: Further ch. 7 (parameterised queries in CRUD). | OWASP API Security Top 10 and Cheat Sheets, `govulncheck` docs, Go security best practices (go.dev/security/best-practices), Sigstore/cosign docs, NIST SSDF. SEC.1, 6-12: no chapter seen. |
| PLAT | Shipping Go, ch. 7 (Containerized deployment), ch. 8 (Configuration management and stable releases), ch. 10 (Advanced deployment), ch. 4 (Introducing continuous deployment), ch. 2 (Introducing continuous integration). Let's Go Further, ch. 21 (Deployment and Hosting). Kubernetes Programming with Go, ch. 1 (Kubernetes API Introduction), ch. 6 (The Client-go Library). Build an Orchestrator in Go, Part 1 (ch. 1-3). | PLAT.1, PLAT.4: Shipping Go ch. 7. PLAT.2, PLAT.5: Shipping Go ch. 2. PLAT.3: Shipping Go ch. 8.2 (Advanced configuration). PLAT.7, PLAT.9: Shipping Go ch. 10. PLAT.11: Kubernetes Programming with Go ch. 1-6. | Kubernetes docs, kind docs, Dockerfile best practices, Twelve-Factor App, Terraform/OpenTofu docs, CNCF Platforms White Paper. PLAT.6, 8, 10, 12: no chapter seen. |
| AIE | None in the library. | AIE.1-12 | Anthropic prompt and Claude Code docs, plus course artefacts. Keep the AI log in `learner/` state. |
| COMM | Shipping Go, ch. 5 (Code quality enforcement; section 5.1 Reviewing code). | COMM.5: Shipping Go ch. 5.1. | Google Engineering Practices (code review guide), Conventional Commits, Write the Docs, Google design doc guidance. COMM.1-4, 6-12: no book chapter seen. |

## Suggested reading order by level

Only books actually present. Everything is just in time, tied to the sprint's tickets.

**L0 (before Sprint 1, orientation)**
1. A Tour of Go (free).
2. Learning Go, ch. 1-8 (skim ch. 1-3 fast; read ch. 8 Errors properly).
3. The Power of Go: Tests, ch. 1-2.

**L1**
1. Learning Go, ch. 9 (Modules, Packages, and Imports), ch. 10 (Concurrency in Go), ch. 13 (Writing Tests).
2. The Power of Go: Tests, ch. 3-5.
3. Let's Go, ch. 1-8 as the first HTTP build; then Let's Go Further, ch. 1-4 (JSON in and out).
4. Shipping Go, ch. 1-4 (CI, testing, deployment basics).
5. Effective Go Recipes as lookup.

**L2**
1. Let's Go Further, ch. 5-12 (Postgres, migrations, CRUD, filtering, logging, rate limiting, graceful shutdown).
2. Learning Go, ch. 12 (The Context).
3. Concurrency in Go, ch. 2-4.
4. Shipping Go, ch. 5-7 (quality enforcement, mocking and DI, containers).
5. Powerful CLI Applications in Go, ch. 1-2, 7 for the first tooling ticket.
6. Go Systems Programming, ch. 8 (Processes and Signals) when a signal or process ticket appears.

**L3**
1. Let's Go Further, ch. 13-21 (auth, authorisation, CORS, metrics, build and deploy).
2. Concurrency in Go, ch. 5-6.
3. Cloud Native Go, ch. 4 (Cloud Native Patterns), ch. 6-9 (dependability, scalability, loose coupling, resilience).
4. Shipping Go, ch. 8-10.
5. Know Go, ch. 2-3 and 11 (generics and iterators).
6. The Power of Go: Tests, ch. 6-8 (fuzzing, mutation, testing the untestable).
7. gRPC Microservices in Go, ch. 3-6, and Go with Domain, ch. 6-9 for ARCH and DATA work.
8. Build Your Own Database From Scratch, ch. 01-06 for CSF.7.
9. Free: Postgres docs, Go memory model, pprof docs, Google SRE book online.

**L4**
1. Cloud Native Go, ch. 10-11 (manageability, observability).
2. Event-Driven Architecture in Golang, ch. 1, 6, 8, 9, 12; Building Distributed Systems with Go and NATS, ch. 1-3, 9-14.
3. Go with Domain, ch. 9-12; Domain-Driven Design with Golang, ch. 3, 5-7.
4. Kubernetes Programming with Go, ch. 1-6 for PLAT.11.
5. Build an Orchestrator in Go and Build Your Own Database From Scratch (ch. 07-14) as optional stretch projects.
6. Free: Google SRE workbook, OWASP API Top 10, Jepsen, AWS Builders' Library.

## Duplicates and notes

- `Shipping Go.epub` and `Shipping Go (1).epub` are byte-identical (confirmed with `cmp`). Treat them as one book and delete the copy locally.
- The Shipping Go EPUB's TOC page carries a stray title ("Effective Concurrency in Go") but the chapter list is Shipping Go's (ch. 1-11, plus appendices A-D on Kotlin, Python, JavaScript and Terraform). Appendix D (Using Terraform) is relevant to PLAT.12.
- Go Design Patterns: the PDF's text layer is shifted, so its TOC was decoded by hand; chapter numbers were not visible. Cite by title.
- Know Go: the TOC extract skipped ch. 4. The Power of Go: Tests and Tools show no author in the TOC pages. Author names are given only where seen.
- Go Systems Programming: TOC read to ch. 11. Kubernetes Programming with Go: TOC read to ch. 6. Later chapters probably exist but were not verified.
- Version risk: several books predate `log/slog`, generics maturity, the 1.22 `net/http` mux, `slices`/`maps`, iterators and Go 1.23+. Check the Go release notes before copying a pattern, and record any divergence in an ADR.
- Gaps with no book at all: AIE, SRE-style REL (SLOs, incident command), most of DIST theory and DATA at L4, PERF (pprof/trace/GC), SEC beyond web auth, and COMM. Use the free references listed above.
- No scanned or unreadable books were found. All 24 files (23 distinct) had a readable TOC.
