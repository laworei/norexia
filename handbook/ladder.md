# Ladder: levels, ticket shape and promotion

| Level | Ticket shape | Autonomy | Environment | AI use |
|---|---|---|---|---|
| L0 Pre-boarding | Guided exercises and small CLI tools | High support | Local | None |
| L1 Intern | Fully specified: behavior, acceptance criteria, hints, file pointers | Check-ins every session | Local `go run` | None |
| L2 Engineer I | The *what* is clear; the *how* is the learner's; some edge cases unstated | Weekly | Docker Compose | None |
| L3 Engineer II | A problem statement; the learner breaks it down, estimates and writes subtasks | Per sprint | kind + observability stack | Boilerplate/tests with disclosure |
| L4 Senior | A business problem; the learner writes the RFC, tickets and rollout plan, reviews others, mentors | Per quarter | kind (cloud optional, budget-capped) | Full, graded |

Level definitions are the **required subcodes** in `handbook/competencies.md` (a subcode at level N is required for level N and above).

## Sprint mix by level (adjusted adaptively)
| Level | Delivery | Drill | Retrieval | Ops/incident/legacy | Design/spike | Review/mentor | Platform |
|---|---|---|---|---|---|---|---|
| L0/L1 | 60% | 25% | 15% | - | - | - | - |
| L2 | 60% | 15% | 10% | 15% | - | - | - |
| L3 | 50% | 10% | 10% | 15% | 15% | - | - |
| L4 | 35% | - | 5% | 15% | 20% | 10% | 15% |

## Promotion (all required)
1. **Coverage:** every required subcode `independent` with >= 2 evidence links from >= 2 sprints.
2. **Trend:** recurring-finding rate falling; first-pass approval within 50-75% for 2 consecutive sprints at stretch difficulty.
3. **Practical exam** (closed-book): L1->L2 tested HTTP service with persistence (~3h); L2->L3 debug planted faults then add a feature (~4h); L3->L4 design doc (~3h) and live defense; L4 sign-off: game day plus an approved RFC delivered.
4. **Interview loop** (light weight for a pure-mastery goal).
5. **Promo packet** reviewed by the promotion committee, which cites evidence and may deny.

A denial includes a gap list and a 30-day plan; re-apply after >= 2 sprints. No time-based promotions.
