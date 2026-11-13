# Review guide

How reviews work at Norexia. Written for both the learner (author) and the reviewer personas.

## Author
- Small PRs. Fill the PR template: what, why, how tested, risks, competencies, AI-use disclosure.
- Run `make check` before opening. CI is the fast feedback; the review is the detailed one.
- **Reply to every `blocking` and `should-fix` comment** before merge: `fixed in <sha>`, `disagree: <argument>`, or `won't fix: <reason>`. Disagreement is welcome when it has an argument.
- A PR cannot merge without the label `review:approved` (CI enforces it).

## Reviewer
- Read the issue first, then the whole PR (right problem? sound design?), then line by line.
- Run it. Review what it does, not only what it says.
- Labels: `blocking`, `should-fix`, `nit`, `question`, `praise`. Praise must be specific and earned.
- Every `blocking` finding: file:line, why it matters, a standard or book section, a competency subcode. Prove bugs with a failing test in the comment when possible.
- Ask questions that lead to the fix. Do not give the fix. If an issue survives a round, give one more hint level.
- Judge against the learner's current level. Stretch notes from one level up are non-blocking.
- Concede when the author is right (it is logged as a reviewer error). Hold your position, with an explanation, when they are not. At L3+ either side can escalate to the architecture panel.

## Severity guide
| Label | Meaning | Blocks merge? |
|---|---|---|
| `blocking` | Wrong, unsafe, untested, or violates the definition of done | Yes |
| `should-fix` | Real improvement likely to cause problems later | Reply required |
| `nit` | Taste or minor style | No |
| `question` | Reviewer wants to understand | Reply required if unclear |
| `praise` | Specific, earned | No |

## Definition of done (cumulative)
- **L1:** tests pass with `-race`, lint clean, complete PR description.
- **L2:** integration tests, reversible migrations, structured logs, docs/API updated.
- **L3:** metrics and traces, benchmarks for hot paths, a runbook entry, failure modes considered.
- **L4:** SLO impact stated, rollout/rollback plan, security checklist, ADR/RFC link.

## Honor code (no bot account)
Persona reviews are posted under the learner's GitHub identity with a persona header, and the approval label is set by the reviewer session. The learner does not apply `review:*` labels themselves. The explain-back in each 1:1 verifies that every merged PR is understood.
