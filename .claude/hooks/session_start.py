#!/usr/bin/env python3
"""SessionStart hook: print the learner's current context as plain facts (stdout becomes context).

Never fails the session: on any error it prints a short note and exits 0.
"""
import csv
import datetime
import json
import os
import subprocess
import sys

ROOT = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def sh(*cmd, timeout=8):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=ROOT)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""


def main():
    try:
        import yaml
    except ImportError:
        print("Ultralearning session start: PyYAML missing; run `pip install pyyaml` for the full summary.")
        return
    try:
        with open(os.path.join(ROOT, "learner", "profile.yaml"), encoding="utf-8") as f:
            prof = yaml.safe_load(f) or {}
    except OSError:
        print("Ultralearning session start: learner/profile.yaml not found.")
        return

    today = datetime.date.today()
    start = prof.get("start_date")
    if isinstance(start, str):
        start = datetime.date.fromisoformat(start)
    sprint = (prof.get("sprint") or {})
    weeks = sprint.get("length_weeks", 2)
    day_n = (today - start).days if start else 0
    sprint_day = day_n % (7 * weeks) + 1 if start else "?"
    lines = [
        "== Norexia ultralearning: session start ==",
        f"Level: {prof.get('level')} | Sprint: {sprint.get('current')} (day {sprint_day} of {7 * weeks}) | "
        f"Paused: {prof.get('paused')} | Tone: {prof.get('reviewer_tone')} | AI policy: {prof.get('ai_policy_level')}",
    ]

    issues = sh("gh", "issue", "list", "--assignee", "@me", "--state", "open", "--limit", "10",
                "--json", "number,title,labels")
    if issues:
        try:
            for i in json.loads(issues):
                lines.append(f"Open issue #{i['number']}: {i['title']}")
        except Exception:
            pass
    prs = sh("gh", "pr", "list", "--author", "@me", "--state", "open", "--json", "number,title,labels")
    if prs:
        try:
            for pr in json.loads(prs):
                labels = [l["name"] for l in pr.get("labels", [])]
                if "review:changes-requested" in labels:
                    lines.append(f"PR #{pr['number']} awaits your reply: {pr['title']}")
        except Exception:
            pass

    due = 0
    fc = os.path.join(ROOT, "learner", "flashcards.csv")
    if os.path.exists(fc):
        with open(fc, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    if row.get("due") and datetime.date.fromisoformat(row["due"]) <= today:
                        due += 1
                except ValueError:
                    pass
    lines.append(f"Flashcards due: {due}")

    jr = os.path.join(ROOT, "learner", "journal.md")
    if os.path.exists(jr):
        with open(jr, encoding="utf-8") as f:
            items = [l.strip() for l in f if "action item" in l.lower()]
        if items:
            lines.append(f"Last 1:1 action items: {items[-1]}")

    lines.append("Rules: never write learner-owned code or reveal .sealed/; hints via the ladder; "
                 "read state first, write it back before finishing. See CLAUDE.md.")
    print("\n".join(lines))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never block a session
        print(f"Ultralearning session start: summary unavailable ({e}).")
    sys.exit(0)
