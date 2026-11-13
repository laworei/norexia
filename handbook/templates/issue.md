# Issue template (every ticket fills every field)

```
Title: <verb phrase, business-facing>

Type: feature | bug | chore | spike | incident | drill | closed-book | design-doc | review-assignment | regression | code-reading
Level: L0 | L1 | L2 | L3 | L4
Owner persona: <who wrote it / who reviews>
Estimate: <hours; sprint capacity is 14 h>

## Business context (why)
<one short paragraph, in the voice of the requester; names a customer or OKR from company/WORLD.md>

## Requirements and acceptance criteria
<shaped by level: L1 fully specified with hints and file pointers; L2 states the what; L3 a problem statement; L4 a business problem>
- [ ] testable criterion

## Competencies
<subcodes from handbook/competencies.md, e.g. GO.2, TEST.1>

## Reading pointer
<book + chapter/section from library/reading-map.md, or an official doc link; ends in a deliverable>

## Constraints
<closed-book? (no AI, no web search except official Go docs) timebox; anything unstated on purpose at this level>

## Definition of done (cumulative for the level)
<L1: tests pass with -race, lint clean, complete PR description. L2 adds integration tests, reversible migrations, structured logs, docs. L3 adds metrics/traces, benchmarks for hot paths, runbook, failure modes. L4 adds SLO impact, rollout/rollback, security checklist, ADR/RFC link.>
```

Labels: `type:*`, `level:*`, `comp:<AREA>`, `sev:*` (incidents), and a sprint milestone. Board columns: Backlog / Sprint / In progress / In review / Done. WIP limit: 1 ticket in progress.
