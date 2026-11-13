#!/usr/bin/env python3
"""Score reviewer findings against sealed calibration keys.

Usage: score-calibration.py <findings.json> [--keys .sealed/review-calibration]

findings.json: {"<diff-name>": [{"file": "...", "line": 12, "severity": "blocking", "summary": "..."}]}
Key file .sealed/review-calibration/<diff-name>.yaml: issues: [{id, file, line, tolerance (default 3)}]
A finding matches a known issue if same file and |line - key line| <= tolerance.
Prints recall, and false-positive blocking findings per diff. Exit 0 iff recall >= 0.8 and FP <= 1 on every diff.
"""
import json
import os
import sys

import yaml

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def main(argv):
    findings = json.load(open(argv[1], encoding="utf-8"))
    if "--line-offset" in argv:  # subtract N from reported lines (e.g. 5 if the reviewer counted diff header lines)
        off = int(argv[argv.index("--line-offset") + 1])
        for fs in findings.values():
            for g in fs:
                g["line"] -= off
    keys_dir = os.path.join(ROOT, ".sealed", "review-calibration")
    if "--keys" in argv:
        keys_dir = argv[argv.index("--keys") + 1]
    total = found = 0
    ok = True
    for name in sorted(findings.keys() | {f[:-5] for f in os.listdir(keys_dir) if f.endswith(".yaml")}):
        kp = os.path.join(keys_dir, f"{name}.yaml")
        if not os.path.exists(kp):
            continue
        issues = yaml.safe_load(open(kp, encoding="utf-8"))["issues"]
        got = findings.get(name, [])
        hit, matched = 0, set()
        for it in issues:
            tol = it.get("tolerance", 3)
            if any(g["file"].endswith(it["file"]) and abs(g["line"] - it["line"]) <= tol for g in got):
                hit += 1
        for i, g in enumerate(got):
            if any(g["file"].endswith(it["file"]) and abs(g["line"] - it["line"]) <= it.get("tolerance", 3)
                   for it in issues):
                matched.add(i)
        fp = sum(1 for i, g in enumerate(got) if g["severity"] == "blocking" and i not in matched)
        total += len(issues)
        found += hit
        if fp > 1:
            ok = False
        print(f"{name}: found {hit}/{len(issues)}, false-positive blocking: {fp}")
    recall = found / total if total else 0
    print(f"recall={recall:.2f} (need >= 0.80)")
    return 0 if ok and recall >= 0.8 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
