# Promotion checklist (what changes when the learner levels up)

Run by the promo-committee on approval. Record each step in `company/TIMELINE.md`.

## Any promotion
- [ ] `learner/profile.yaml`: `level`, `ai_policy_level`, `environment`, and `sprint.current` updated.
- [ ] Sprint mix switched to the new row in `handbook/ladder.md`.
- [ ] Brag-doc entry (learner writes it; Claude does not).
- [ ] Guardrail review: `./scripts/test-hooks.sh` still passes.

## To L2
- [ ] Docker Compose environment becomes standard; on-call (`company/state.yaml: on_call.enabled: true`) starts.
- [ ] Monthly code-reading ticket begins.

## To L3
- [ ] `platform/` becomes learner-owned: uncomment `platform/` in `.claude/owned-paths.txt` **and** add `"Edit(/platform/**)"` to `permissions.deny` in `.claude/settings.json`; add cases to `scripts/test-hooks.sh`. Re-run it.
- [ ] kind + observability stack; CI gets benchmarks, e2e smoke and k6 thresholds.
- [ ] AI policy: boilerplate/tests with disclosure.
- [ ] Architecture panel and open-source quarterly contribution start.

## To L4
- [ ] Junior-teammate PRs start. Adjust the guardrail: the hook allows writes only while the current git branch matches `teammate/*` and only for the junior-teammate flow; update `scripts/test-hooks.sh` accordingly and re-run it.
- [ ] Optional cloud with a hard budget cap and automatic teardown (only if the budget allows).
- [ ] CI gets IaC validate/plan, manifest validation, policy checks.
- [ ] Full AI use, graded on specification and review.
