#!/usr/bin/env python3
"""Deep-work log and scoreboard (learner/deepwork-log.jsonl).

  deepwork.py log --deep 90 --shallow 45 --blocks 2 --interruptions 1 --focus 4 [--ticket "#3"] [--note "..."]
  deepwork.py week [YYYY-MM-DD]     summary for the ISO week containing the date (default today)
  deepwork.py scoreboard            lead and lag measures for the current sprint window

Lead measures (what you control): deep minutes, retrieval sessions, drill reps, sessions held.
Lag measures (results): subcodes at independent, first-pass approval (from learner/metrics.jsonl).
"""
import argparse
import collections
import datetime
import json
import os
import sys

import yaml

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LOG = os.path.join(ROOT, "learner", "deepwork-log.jsonl")


def rows():
    if not os.path.exists(LOG):
        return []
    with open(LOG, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def profile():
    with open(os.path.join(ROOT, "learner", "profile.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)


def week_key(d: datetime.date):
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def cmd_log(a):
    r = {
        "date": datetime.date.today().isoformat(),
        "deep_min": a.deep, "shallow_min": a.shallow, "blocks": a.blocks,
        "interruptions": a.interruptions, "focus": a.focus,
        "ticket": a.ticket, "note": a.note,
    }
    if not (1 <= a.focus <= 5):
        print("focus must be 1-5", file=sys.stderr)
        return 1
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(r) + "\n")
    print(f"logged: {a.deep} deep / {a.shallow} shallow min, focus {a.focus}")
    return cmd_week(argparse.Namespace(date=None))


def cmd_week(a):
    d = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
    key = week_key(d)
    wk = [r for r in rows() if week_key(datetime.date.fromisoformat(r["date"])) == key]
    prof = profile()
    target = (prof.get("deep_work") or {}).get("weekly_deep_minutes_target", 240)
    deep = sum(r["deep_min"] for r in wk)
    shallow = sum(r["shallow_min"] for r in wk)
    total = deep + shallow
    pct_shallow = (100 * shallow / total) if total else 0
    inter = sum(r["interruptions"] for r in wk)
    focus = [r["focus"] for r in wk]
    print(f"{key}: deep {deep}/{target} min ({100 * deep // target if target else 0}% of target), "
          f"shallow {shallow} min ({pct_shallow:.0f}%), sessions {len(wk)}, interruptions {inter}, "
          f"avg focus {sum(focus) / len(focus):.1f}" if focus else f"{key}: no sessions logged (target {target} deep min)")
    if total and pct_shallow > 25:
        print("note: shallow time is over 25%; cut something at the next retro (see handbook/deep-work.md)")
    return 0


def cmd_scoreboard(a):
    prof = profile()
    days = 7 * prof["sprint"]["length_weeks"]
    since = datetime.date.today() - datetime.timedelta(days=days)
    r = [x for x in rows() if datetime.date.fromisoformat(x["date"]) >= since]
    deep = sum(x["deep_min"] for x in r)
    per_week = collections.Counter()
    for x in r:
        per_week[week_key(datetime.date.fromisoformat(x["date"]))] += x["deep_min"]
    print(f"== Scoreboard: last {days} days ==")
    print("LEAD (you control these)")
    print(f"  deep minutes: {deep}  (by week: {dict(per_week) or 'none'})")
    print(f"  sessions held: {len(r)}")
    print("LAG (results)")
    comp_path = os.path.join(ROOT, "learner", "competencies.yaml")
    with open(comp_path, encoding="utf-8") as f:
        comp = yaml.safe_load(f)["subcodes"]
    ind = sum(1 for v in comp.values() if v["state"] in ("independent", "teaches"))
    print(f"  subcodes independent: {ind}/{len(comp)}")
    mpath = os.path.join(ROOT, "learner", "metrics.jsonl")
    last = None
    if os.path.exists(mpath):
        with open(mpath, encoding="utf-8") as f:
            ms = [json.loads(l) for l in f if l.strip()]
        last = ms[-1] if ms else None
    print(f"  last sprint first-pass approval: {last.get('first_pass_approval') if last else 'n/a'}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    l = sub.add_parser("log")
    l.add_argument("--deep", type=int, required=True)
    l.add_argument("--shallow", type=int, default=0)
    l.add_argument("--blocks", type=int, default=1)
    l.add_argument("--interruptions", type=int, default=0)
    l.add_argument("--focus", type=int, required=True)
    l.add_argument("--ticket", default=None)
    l.add_argument("--note", default="")
    w = sub.add_parser("week")
    w.add_argument("date", nargs="?")
    sub.add_parser("scoreboard")
    a = ap.parse_args()
    return {"log": cmd_log, "week": cmd_week, "scoreboard": cmd_scoreboard}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
