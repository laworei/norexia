#!/usr/bin/env python3
"""Leitner flashcards over learner/flashcards.csv (Anki-importable: front, back, tags).

  flashcards.py due                     list due cards
  flashcards.py add <front> <back> <tags>
  flashcards.py grade <id> <right|partly|wrong>
  flashcards.py stats                   retention summary
"""
import csv
import datetime
import os
import sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PATH = os.path.join(ROOT, "learner", "flashcards.csv")
FIELDS = ["id", "front", "back", "tags", "box", "due"]
INTERVALS = {1: 1, 2: 3, 3: 7, 4: 21, 5: 60}


def load():
    if not os.path.exists(PATH):
        return []
    with open(PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "due"
    rows = load()
    today = datetime.date.today()
    if cmd == "due":
        due = [r for r in rows if datetime.date.fromisoformat(r["due"]) <= today]
        for r in due:
            print(f"{r['id']}\t[{r['tags']}]\t{r['front']}")
        print(f"{len(due)} due of {len(rows)}")
    elif cmd == "add":
        front, back, tags = argv[2], argv[3], argv[4] if len(argv) > 4 else ""
        nid = str(max([int(r["id"]) for r in rows] + [0]) + 1)
        rows.append({"id": nid, "front": front, "back": back, "tags": tags, "box": "1", "due": today.isoformat()})
        save(rows)
        print(f"added card {nid}")
    elif cmd == "grade":
        cid, result = argv[2], argv[3]
        for r in rows:
            if r["id"] == cid:
                box = int(r["box"])
                box = min(5, box + 1) if result == "right" else box if result == "partly" else 1
                r["box"] = str(box)
                r["due"] = (today + datetime.timedelta(days=INTERVALS[box])).isoformat()
                save(rows)
                print(f"card {cid}: box {box}, next {r['due']}")
                return 0
        print(f"no card {cid}", file=sys.stderr)
        return 1
    elif cmd == "stats":
        if not rows:
            print("no cards")
        else:
            boxes = [int(r["box"]) for r in rows]
            print(f"cards={len(rows)} mature(box>=4)={sum(b >= 4 for b in boxes)} "
                  f"retention_proxy={sum(b >= 3 for b in boxes) / len(rows):.2f}")
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
