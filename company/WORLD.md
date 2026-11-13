# Norexia: World Bible

Single source of truth. Every persona reads this before acting and never contradicts it. Norexia and everything in this file are fictional. Real companies appear only as style inspiration.

## What Norexia is

Norexia is a managed backend platform ("your backend, with an undo button"). A developer creates a **project** and gets:

- a managed **Postgres** database with an auto-generated REST API,
- **auth** (API keys, JWTs for end users),
- **object storage**,
- **realtime** subscriptions,
- **backup and recovery** built in: scheduled snapshots, point-in-time recovery (PITR), cross-region restore.

The last item is the differentiator. Norexia sells confidence: a customer can break their database at 14:03 and be back at 14:02.

## The product surface (what the learner's services implement over time)

| Area | Service (working name) | Why it exists |
|---|---|---|
| Public/control-plane API | `control-api` | Projects, API keys, usage, backups. Auth, rate limiting, versioning, pagination, idempotency keys. |
| Billing | `billing` | Usage metering (storage GB, egress, backup retention), invoices, ledger, reconciliation. Money correctness. |
| Backup scheduler | `scheduler` | Decides what to back up when. Concurrency, leases, retries. |
| Backup workers | `worker` | Execute snapshots and restores from a queue. At-least-once delivery, idempotency. |
| Webhooks | `webhooks` | Outbound events: `backup.completed`, `backup.failed`, `restore.finished`, `quota.warning`. Signing, retries. |
| Notifications | `notifier` | Email and in-app alerts, retention-expiry notices. |
| Internal platform | `platform/` | CI/CD, Kubernetes, observability, golden paths. |

`legacy/` holds `snapshotd`, a backup-job daemon inherited from the founding team, with flaws (see the handbook, not the sealed manifest).

## Business

- **Model:** usage-based pricing with a free tier. Paid plans: Team and Business. Enterprise is custom.
- **Stage:** seed-funded, 24 people, one region (`eu-west`), roughly 3,100 projects, 380 paying.
- **Key metrics:** monthly recurring revenue (MRR), backup success rate (SLO target 99.9%), restore success rate (99.5%), p95 control-API latency under 300 ms, support tickets per 100 projects.
- **Quarter now (Q1 of the story): "Launch hardening."** OKRs:
  1. Backup success rate ≥ 99% for all paid projects.
  2. Self-serve billing live for Team plan, with no manual invoices.
  3. Public API v1 documented and stable.

## Customers (fictional)

"Quarter" always means the **story quarter** (Q1 now), not the calendar quarter. OKRs are listed in priority order (O1 is the top one). In Q1 the active customers are Kestrel Health, Pomelo Press, Orrin & Vale and a small Brightwater Games account. **Larkfield Logistics signs in Q2** (no SLA exists before then), and Brightwater's viral launch is Q3. Personas must not reference an event or contract before its quarter.

| Merchant | Who they are | Personality in tickets |
|---|---|---|
| **Kestrel Health** | Telehealth startup, 40 people | Anxious about compliance. Asks "can you prove it?" and wants audit trails. |
| **Pomelo Press** | Newsletter platform, 6 people | Fast-moving, informal, reports symptoms vaguely ("emails got weird"). Never reads docs. |
| **Larkfield Logistics** | Mid-size freight software firm | Contract-driven, cites the SLA, escalates by email to the CEO. |
| **Brightwater Games** | Indie studio, spiky traffic around launches | Cares about performance and cost. Loud on social media when things slow down. |
| **Orrin & Vale** | Boutique law-tech consultancy | Polite, precise, rarely complains, remembers everything. |

## People (see `company/personas/` for full cards)

CEO **Marta Eklund** (founder, product-minded). CTO **Dev Okonkwo** (sets technical direction). Engineering manager **Priya Raman**. Staff engineer **Tomasz Wrona**. SRE lead **Ines Carvalho**. Security engineer **Jonas Pettersson**. Product manager **Hana Weiss**. Customer-voice rotation: support lead **Alex Moreau**. The learner is a new backend engineer on Priya's team.

## Storyline (6 quarters; technical needs arrive from business events)

1. **Q1: Launch hardening.** Control-plane API, project provisioning, daily snapshots. Legacy `snapshotd` is shaky.
2. **Q2: First big customer.** Larkfield Logistics signs. Billing, rate limits, webhooks, and an SLA appear.
3. **Q3: 10× traffic.** A viral launch by Brightwater Games. Scheduler scaling, queue-based workers, backpressure.
4. **Q4: Data growth and a reliability crisis.** Backup storage balloons, a restore fails for a paying customer, and PITR needs to be right. SLOs and postmortems become real.
5. **Q5: Platform team spin-up.** Kubernetes, golden paths, observability standards, cost control.
6. **Q6: Multi-region.** Cross-region restore, operator-managed tenant databases, data residency for Kestrel Health.

Technology is introduced when the story needs it, never earlier.

## Engineering culture

- Blameless. Evidence over opinion. Small PRs. Boring technology first.
- "A backup you haven't restored is a rumor." Restore tests matter more than backup tests.
- Stack defaults are in `docs/PROGRAM.md` and the brief (§15). Changing one needs an ADR.
- Writing is a core skill: tickets, PRs, RFCs, postmortems.

## Constraints for persona writers

- Plausible and grounded. No cartoon villains, meme names, or invented real-world companies.
- Business language from PM and customers. Technical vocabulary only where the persona would have it.
- Customers never use engineering terms unprompted.
- History is appended to `company/TIMELINE.md`. Never rewrite it.
