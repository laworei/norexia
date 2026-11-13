# Reviewer changelog

Every change to `.claude/agents/staff-engineer.md` (and specialist reviewers) is recorded here with the calibration numbers before and after. Calibrate monthly with `/calibrate-reviewer`. Targets: recall of seeded issues >= 80%, <= 1 false-positive blocking finding per diff.

| Date | Change | Recall before -> after | FP blocking before -> after |
|---|---|---|---|
| 2026-11-14 | Initial persona and protocol | n/a | n/a |
| 2026-11-14 | Baseline run (general-purpose agent following the staff-engineer card, 9 diffs). Reviewer found every seeded issue class but reported lines counted from the top of the .diff file (+5 header lines), so raw recall was 25%. With the offset corrected: recall 92% (23/25), max 1 false-positive blocking per diff (02 and 03: valid blocking findings located outside the key's tolerance). Change: the persona and the calibrate skill now require new-file line numbers. | 25% raw / 92% corrected -> re-run pending | 1 -> pending |
