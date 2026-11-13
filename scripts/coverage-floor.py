#!/usr/bin/env python3
"""Enforce the per-level coverage floor on the learner's packages. Skips when there is nothing to measure.

Floors: L0/L1 50%, L2 65%, L3 75%, L4 80%. Measured over the learner-owned Go packages only.
"""
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FLOORS = {"L0": 50, "L1": 50, "L2": 65, "L3": 75, "L4": 80, "pending-diagnostic": 0}
OWNED_PKG_DIRS = ("services", "cmd", "internal", "pkg")


def main():
    with open(os.path.join(ROOT, "learner", "profile.yaml"), encoding="utf-8") as f:
        level = yaml.safe_load(f)["level"]
    pkgs = [d for d in OWNED_PKG_DIRS if os.path.isdir(os.path.join(ROOT, d))]
    if not pkgs:
        print("coverage floor: no learner packages yet, skipping")
        return 0
    prof = os.path.join(ROOT, ".coverage.out")
    r = subprocess.run(["go", "test", "-race", f"-coverprofile={prof}", *[f"./{d}/..." for d in pkgs]], cwd=ROOT)
    if r.returncode != 0:
        return r.returncode
    out = subprocess.run(["go", "tool", "cover", f"-func={prof}"], cwd=ROOT, capture_output=True, text=True).stdout
    os.remove(prof)
    m = re.search(r"total:\s+\(statements\)\s+([\d.]+)%", out)
    total = float(m.group(1)) if m else 0.0
    floor = FLOORS.get(level, 50)
    print(f"coverage {total:.1f}% (floor {floor}% for {level})")
    return 0 if total >= floor else 1


if __name__ == "__main__":
    sys.exit(main())
