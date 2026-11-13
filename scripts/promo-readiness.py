#!/usr/bin/env python3
"""Check promotion readiness for the learner's next level (coverage + trend). Exam and packet are tracked by /promo."""
import json
import os
import sys

import yaml

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ORDER = ["L0", "L1", "L2", "L3", "L4"]


def main():
    with open(os.path.join(ROOT, "learner", "profile.yaml"), encoding="utf-8") as f:
        level = yaml.safe_load(f)["level"]
    if level in ("pending-diagnostic", "L4"):
        print(f"No promotion to evaluate from level {level}.")
        return 0
    # Promotion from Lk requires every subcode at levels <= k+1... the brief: target level subcodes. L0->L1 needs none of the matrix.
    current = ORDER.index(level)
    if current == 0:
        print("L0 -> L1 is decided by the diagnostic and exercises, not the matrix.")
        return 0
    target = f"L{current}"  # required to LEAVE level Lk: all subcodes up to and including Lk
    with open(os.path.join(ROOT, "learner", "competencies.yaml"), encoding="utf-8") as f:
        comp = yaml.safe_load(f)["subcodes"]
    req = {c: v for c, v in comp.items() if v["level"] <= target}
    missing = []
    for c, v in req.items():
        sprints = {e["sprint"] for e in v["evidence"]}
        if v["state"] not in {"independent", "teaches"} or len(v["evidence"]) < 2 or len(sprints) < 2:
            missing.append((c, v["state"], len(v["evidence"]), len(sprints)))
    print(f"Level {level} -> L{current + 1}: {len(req) - len(missing)}/{len(req)} required subcodes ready.")
    for c, s, n, k in missing[:40]:
        print(f"  gap {c}: state={s}, evidence={n}, sprints={k}")
    if len(missing) > 40:
        print(f"  ... and {len(missing) - 40} more")
    mpath = os.path.join(ROOT, "learner", "metrics.jsonl")
    last = []
    if os.path.exists(mpath):
        with open(mpath, encoding="utf-8") as f:
            last = [json.loads(l) for l in f if l.strip()][-2:]
    ok = len(last) == 2 and all(m.get("first_pass_approval") is not None and 0.5 <= m["first_pass_approval"] <= 0.75
                                for m in last)
    print(f"Trend: first-pass approval in band for the last 2 sprints: {ok}")
    return 0 if not missing and ok else 1


if __name__ == "__main__":
    sys.exit(main())
