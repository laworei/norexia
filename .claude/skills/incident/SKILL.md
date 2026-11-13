---
name: incident
description: Fire a scheduled incident from the chaos catalog (from L2), with symptoms only. Use when the learner types /incident, or on session start when an incident window is due.
argument-hint: "[catalog-id]"
disable-model-invocation: true
allowed-tools: Bash(gh issue *) Bash(docker compose *) Bash(bash chaos/*) Bash(python3 scripts/*)
---

Run an incident as **Ines Carvalho** (sre-lead) with **customer** voices.

1. Check `learner/profile.yaml`: only from L2. Pick an entry from `chaos/catalog.yaml` for the learner's level (or the id given in `$ARGUMENTS`), skipping any recently used. It must be inside the learner's working window.
2. Read `.sealed/incidents/<id>.md` for the root cause and expected signals. **Never reveal them.**
3. Run the injection script `chaos/inject/<id>.sh` against the local environment.
4. Open a `type:incident` GitHub issue with symptoms only, as an alert or a customer report in the customer's voice. Label severity.
5. Record the start time in `company/state.yaml` (`active_incidents`) and `learner/metrics.jsonl`. The learner acknowledges, posts status, mitigates, resolves, and writes a blameless postmortem in `docs/postmortems/` within 2 days.
6. When resolved, run `chaos/rollback/<id>.sh`, record time to detect/mitigate/resolve, then `/postmortem-review`.

If injection fails, run the rollback immediately and report.
