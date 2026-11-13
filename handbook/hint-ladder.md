# Getting stuck: timebox, hint ladder, help budget

## Timebox

Try for at least **30 minutes (L0/L1)** or **60 minutes (L2+)** before asking. State what you tried and what you observed. If you have not tried, the first question is "what have you tried?".

## `/stuck <issue>`

The help-desk asks diagnostic questions first, then escalates **one level at a time**, only when the previous level did not unblock you:

| Level | Hint | Example shape |
|---|---|---|
| 1 | Conceptual pointer | The concept, plus a book or docs section. |
| 2 | Narrowed location | "Look at how X handles Y." |
| 3 | Analogous example | A worked example from a **different** context than the ticket. |
| 4 | Plain-language or pseudocode outline | The approach in words. **No Go code for the ticket.** |

There is **no level 5**. `/give-up <id>` is the only explicit escape: it reveals the answer, is logged as a help event, and the ticket is marked `assisted` (it cannot count as `independent` evidence).

## Logging

Every hint is appended to `learner/hints.jsonl`:

```json
{"date":"2026-11-14","issue":"#12","level":2,"subcode":"CONC.3","note":"pointed at context cancellation in net/http server shutdown"}
```

## What the numbers do

- Heavy hint use lowers next sprint's difficulty.
- Near-zero hint use together with many review rounds earns a gentle nudge to ask earlier. Knowing when to ask is a skill.
- A level-4 hint on a competency counts as `assisted` for that subcode.
