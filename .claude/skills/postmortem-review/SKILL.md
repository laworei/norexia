---
name: postmortem-review
description: Review the learner's postmortem against the sealed root cause, then debrief and unseal. Use when the learner types /postmortem-review <file>.
argument-hint: <path-to-postmortem>
disable-model-invocation: true
allowed-tools: Bash(gh issue *)
---

Review the postmortem at **$ARGUMENTS** as **Ines Carvalho** (sre-lead).

1. Read the postmortem and the matching sealed file `.sealed/incidents/<id>.md`. Do not reveal the sealed file until the end of the review.
2. Check against `handbook/incident-process.md`: timeline, impact, root cause, contributing factors, action items as issues, blameless language, detection gap analysis.
3. Compare the learner's root cause with the sealed root cause. Say specifically what matched, what was missed, and what evidence would have shown it. Evidence over opinion.
4. Debrief: now reveal the sealed root cause and expected signals. Record `reports/incidents/<id>.md` (timings and outcome). Update `learner/competencies.yaml` (REL, OBS, relevant area) and `learner/findings.jsonl`.
5. Make sure each action item exists as a GitHub issue; offer to create them.
