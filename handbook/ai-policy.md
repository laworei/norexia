# AI usage policy (and honor code)

The goal is skill, not output. AI is allowed to explain and to review; it is not allowed to write the learner's code until the learner can do without it.

| Level | Rule |
|---|---|
| L0-L2 | **No AI on owned work.** No AI autocomplete in the editor. No pasting code into chat for a fix. AI may be used to explain a concept or to review code **after** the learner has written it, via the persona flow. Closed-book tickets: official Go docs only. |
| L3 | AI is allowed for boilerplate and tests, with **disclosure** in the PR (what, which tool, what you changed). You must be able to explain every line. |
| L4 | Full use, graded on how well you specify, review and correct it. |

## Enforcement
- Claude and subagents never write code in owned paths (hooks and permissions enforce it).
- Each 1:1 includes an **explain-back** of a merged PR.
- Breaking the rules is not punished with shame; it is recorded as a help event and the related subcodes cannot count as `independent` for that work.
- Honor code: you do not turn off AI autocomplete only when it is convenient. If you slipped, say so in the PR; the tickets will adapt.

## Why
Typing and debugging are where understanding forms. A solution you did not struggle to build rarely survives the exam.
