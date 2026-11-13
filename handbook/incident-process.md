# Incident process and postmortem template

## During an incident
1. **Acknowledge** on the incident issue. State what you see and what you will check first.
2. **Triage:** user impact, scope, start time. Use the observability you have (logs, metrics, traces).
3. **Mitigate first**, diagnose second: rollback, disable, scale, restore.
4. **Communicate:** short status updates (what we know, what we are doing, next update time).
5. **Resolve:** confirm recovery with evidence, not a feeling.

## Blameless postmortem (in `docs/postmortems/YYYY-MM-DD-<slug>.md`)
- **Summary:** one paragraph, plain language.
- **Impact:** who, how many, how long, business effect.
- **Timeline:** timestamps (UTC) from first signal to resolution, including detection and decisions.
- **Root cause:** the mechanism, with evidence.
- **Contributing factors:** what made it likelier or worse. People are never the root cause.
- **What went well / what did not.**
- **Detection:** how was it noticed? If observability could not show it, adding detection is an action item.
- **Action items:** each a GitHub issue with owner and priority, linked here.

## After
`/postmortem-review <file>` compares your root cause with the sealed one and debriefs.
