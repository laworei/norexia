#!/usr/bin/env python3
"""Write reports/status-<date>.md: level, competency heatmap, findings by category, hints, flashcards."""
import collections
import datetime
import json
import os
import subprocess
import sys

import yaml

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ICON = {"not-seen": "·", "assisted": "◔", "independent": "●", "teaches": "★"}


def jl(name):
    path = os.path.join(ROOT, "learner", name)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    with open(os.path.join(ROOT, "learner", "profile.yaml"), encoding="utf-8") as f:
        prof = yaml.safe_load(f)
    with open(os.path.join(ROOT, "learner", "competencies.yaml"), encoding="utf-8") as f:
        comp = yaml.safe_load(f)["subcodes"]
    findings, hints, metrics = jl("findings.jsonl"), jl("hints.jsonl"), jl("metrics.jsonl")

    out = [f"# Status {datetime.date.today()}", "",
           f"Level **{prof['level']}** | sprint {prof['sprint']['current']} | goal {prof['goal']}", "",
           "## Competency heatmap", "", "`·` not-seen  `◔` assisted  `●` independent  `★` teaches", "",
           "| Area | L1 | L2 | L3 | L4 |", "|---|---|---|---|---|"]
    areas = collections.OrderedDict()
    for code, v in comp.items():
        areas.setdefault(v["area"], {}).setdefault(v["level"], []).append(ICON[v["state"]])
    for area, lv in areas.items():
        out.append(f"| {area} | " + " | ".join("".join(lv.get(l, [])) for l in ("L1", "L2", "L3", "L4")) + " |")

    by_cat = collections.Counter(f["category"] for f in findings)
    out += ["", "## Findings by category", ""] + ([f"- {c}: {n}" for c, n in by_cat.most_common()] or ["- none yet"])
    out += ["", "## Hints", "", f"- total: {len(hints)} (level 4 or give-up: "
            f"{sum(str(h['level']) in {'4', 'give-up'} for h in hints)})"]
    out += ["", "## Metrics (latest sprint)", "", "```json",
            json.dumps(metrics[-1], indent=2) if metrics else "none yet", "```"]
    fc = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "flashcards.py"), "stats"],
                        capture_output=True, text=True).stdout.strip()
    out += ["", "## Flashcards", "", fc]
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    path = os.path.join(ROOT, "reports", f"status-{datetime.date.today()}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(path)


if __name__ == "__main__":
    main()
