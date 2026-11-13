#!/usr/bin/env python3
"""Compute sprint metrics from learner/*.jsonl and print one JSON line (the retro appends it to metrics.jsonl).

Usage: sprint-metrics.py [--since YYYY-MM-DD]   (default: last 14 days)
"""
import collections
import datetime
import json
import os
import sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def rows(name):
    path = os.path.join(ROOT, "learner", name)
    out = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
    return out


def main(argv):
    since = datetime.date.today() - datetime.timedelta(days=14)
    if "--since" in argv:
        since = datetime.date.fromisoformat(argv[argv.index("--since") + 1])

    def recent(r):
        return datetime.date.fromisoformat(str(r["date"])) >= since

    findings = [r for r in rows("findings.jsonl") if recent(r)]
    hints = [r for r in rows("hints.jsonl") if recent(r)]
    by_pr = collections.defaultdict(list)
    for r in findings:
        by_pr[r["pr"]].append(r)
    # review rounds = distinct dates with findings per PR (approximation until reviews are tracked separately)
    rounds = [len({f["date"] for f in fs}) for fs in by_pr.values()]
    first_pass = [not any(f["severity"] in {"blocking"} for f in fs) for fs in by_pr.values()]
    subcodes = collections.Counter(f["subcode"] for f in findings if f["severity"] in {"blocking", "should-fix"})
    out = {
        "sprint": None,
        "date": datetime.date.today().isoformat(),
        "first_pass_approval": round(sum(first_pass) / len(first_pass), 2) if first_pass else None,
        "avg_review_rounds": round(sum(rounds) / len(rounds), 2) if rounds else None,
        "avg_cycle_time_hours": None,  # fill from gh when PRs exist
        "hints_total": len(hints),
        "recurring_findings": sorted(c for c, n in subcodes.items() if n >= 2),
        "flashcard_retention": None,
        "notes": "computed by scripts/sprint-metrics.py; fill sprint, cycle time and retention in the retro",
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
