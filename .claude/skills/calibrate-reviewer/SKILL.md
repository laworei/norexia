---
name: calibrate-reviewer
description: Run the staff-engineer reviewer over the seeded diffs in review-calibration/ and compare to the sealed answer keys. Monthly. Use when the learner types /calibrate-reviewer.
disable-model-invocation: true
allowed-tools: Bash(python3 scripts/*) Bash(git *)
---

Calibrate the reviewer.

1. For each diff in `review-calibration/diffs/`, run the **staff-engineer** (as a fresh subagent that has **not** read `.sealed/`) over the diff and capture its findings as structured JSON (file, line, severity, summary).
2. Tell the reviewer explicitly that line numbers are **new-file lines (not offsets within the .diff text)**; check one finding against its diff before scoring and use `--line-offset N` only to report a convention slip, never to hide it. Compare to the sealed key `.sealed/review-calibration/<diff>.yaml` with `python3 scripts/score-calibration.py`. Compute recall of known issues and false-positive blocking findings per diff.
3. Pass criteria: recall >= 80% and <= 1 false-positive blocking finding per diff.
4. If failing, tighten `.claude/agents/staff-engineer.md` (concrete, targeted changes) and record each change, with the metric before and after, in `docs/reviewer-changelog.md`. Re-run to confirm.
5. Report the numbers honestly. Do not reveal the sealed keys to the learner.
