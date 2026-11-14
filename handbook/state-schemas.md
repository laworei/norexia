# State file schemas

Validated by `scripts/validate-state` (run in CI). All dates are ISO `YYYY-MM-DD`. Subcodes look like `CONC.3` and must exist in `learner/competencies.yaml`.

## `learner/profile.yaml`
Required keys: `github_user`, `repo`, `level` (`pending-diagnostic|L0|L1|L2|L3|L4`), `start_date`, `hours_per_week` (number), `schedule`, `sprint`, `goal`, `ai_policy_level` (`none|boilerplate-with-disclosure|full`), `reviewer_tone` (`warm|neutral|blunt`), `paused` (bool).

## `learner/competencies.yaml`
`subcodes:` map `CODE -> {area, level (L1-L4), behaviour, state, evidence[], last_exercised}`. `state` is `not-seen|assisted|independent|teaches`. `independent` and above require `evidence` with >= 2 items from >= 2 distinct `sprint` values. Each evidence item: `{link, sprint, date, note}`.

## `learner/findings.jsonl` (one JSON object per line)
`id`, `date`, `pr` (int), `file`, `line` (int), `subcode`, `severity` (`blocking|should-fix|nit|question|praise`), `category`, `summary`, `recurrence_count` (int >= 0), `my_reply` (string or null), `resolved_sha` (string or null), `disputed` (bool), `outcome` (`open|fixed|wont-fix|disagree-upheld|reviewer-error`).

## `learner/hints.jsonl`
`date`, `issue`, `level` (`1|2|3|4|give-up`), `subcode`, `note`.

## `learner/metrics.jsonl` (per sprint)
`sprint` (int), `date`, `first_pass_approval` (0-1), `avg_review_rounds`, `avg_cycle_time_hours`, `hints_total`, `recurring_findings`, `flashcard_retention`, `paused` (bool, optional), `notes`.

## `learner/deepwork-log.jsonl` (one line per session; written by `scripts/deepwork.py log`)
`date`, `deep_min`, `shallow_min`, `blocks`, `interruptions` (non-negative ints), `focus` (int 1-5), `ticket` (string or null), `note`. `learner/profile.yaml` must have `deep_work.weekly_deep_minutes_target` (int).

## `learner/experiments.md` and `learner/metalearning.md`
Free-form, written by the learner (templates: `handbook/templates/metalearning.md`; experiments table described in `handbook/learning-method.md` §9). Not schema-validated.

## `learner/flashcards.csv`
Header `id,front,back,tags,box,due`. `box` 1-5, `due` is a date. Anki-importable (`front`, `back`, `tags`).

## `company/state.yaml`
Required: `quarter` (int), `okrs` (list), `on_call` (map), `active_incidents` (list), `persona_notes` (map), `last_updated`.

## Journal and reading
`learner/journal.md` (agents append), `learner/reading-log.md` (learner appends), `learner/brag-doc.md` (**learner only**).
