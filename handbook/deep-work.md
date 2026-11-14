# Deep work protocol

Based on Cal Newport's *Deep Work*: professionally useful work done in distraction-free concentration that stretches your ability, is hard to replicate, and creates the skill you are here for. Everything else is **shallow**. This program is mostly deep work. Protect it.

## What counts
| Deep (counts toward the scoreboard) | Shallow (capped at ~25% of session time) |
|---|---|
| Writing code for a ticket, with no distractions | PR descriptions, replying to review comments, labels |
| Reading a chapter *to build something now*, notes closed afterwards | Setup, installing, config, git chores |
| Closed-book drills and retrieval | Flashcard admin, logging, journal |
| Debugging a failing test, design thinking on paper | Waiting for CI, checking GitHub, planning |
| Explain-back and Feynman write-ups | Email, chat, social media (not during sessions at all) |

Rule of thumb: if you could do it while half-listening to a podcast, it is shallow. Log it as shallow; do not pretend.

## Your schedule: rhythmic and fixed
You work **Saturday and Sunday** (the rhythmic philosophy: same slots, no daily decision). Fixed-schedule productivity: you stop at the end of the day's slot, even if a task is unfinished. The deadline forces focus, and rested learners remember more.

Default day (~5 h; adjust the start time to yours, keep it constant):

| Slot | What | Depth |
|---|---|---|
| 0:00-0:10 | **Start ritual** (below), `/session-start` | shallow |
| 0:10-1:40 | **Deep block A**: hardest work first, on the one open ticket | deep |
| 1:40-1:55 | Break: walk, water, no screen, no phone | rest |
| 1:55-3:25 | **Deep block B**: continue, or a closed-book drill / retrieval ticket | deep |
| 3:25-3:40 | Break (same rules) | rest |
| 3:40-4:40 | **Shallow block**: PR replies, reviews, CI, flashcards (`/flashcards`), notes | shallow |
| 4:40-5:00 | **Shutdown ritual**, `/session-end` | shallow |

Newport: a trained professional manages about 4 deep hours a day; beginners 1-2. So the **target ramps**: week 1-2, 4 deep hours/week; +30 min each sprint; cap about 7 h/week. A day with 2 honest deep blocks is a success. Do not add a third deep block to "catch up".

## Start ritual (5-10 min, the same every time)
1. Same place, same chair. Phone in another room (not on the desk, not face down). Close mail, chat, social, and the browser except documentation.
2. Turn on a website blocker for news/social (the "internet Sabbath for sessions"). Notifications off.
3. Water, tea or coffee, a notebook and pen for the **paper log**.
4. Run `/session-start`: it shows today's one ticket, your scoreboard, and starts with a 5-minute **free recall** of last session.
5. Write on paper: "In block A I will finish: ____" (one specific, checkable outcome).

## During a block
- One ticket. One screen layout. No tabs you do not need.
- Distraction **capture, do not obey**: an urge to check something goes on a paper list ("parking lot") and is handled in the shallow block.
- If you hit a wall: apply the timebox and ladder (30 min at L0/L1, then `/stuck`). Switching tasks to avoid difficulty is the failure mode being trained away.
- Count interruptions (including self-interruptions) with tally marks.

## Embrace boredom (attention training)
Breaks are for **boredom, not stimulation**. No phone, no podcast, no feed. Walk and think about the problem you are on (productive meditation: pick one problem, notice when your mind wanders, bring it back). Attention is a trained muscle; checking your phone in every gap untrains it.

## Shutdown ritual (10-15 min, `/session-end`)
1. Log the session: `python3 scripts/deepwork.py log ...` (deep and shallow minutes, interruptions, focus 1-5).
2. **Free recall** (closed notes, 5 min): write what you learned today, what you got wrong, what you would explain to a colleague.
3. Add 2-4 flashcards from today's mistakes and key facts.
4. Write the **next action** for the open ticket (the very first step), so the next start has zero friction.
5. Say "shutdown complete" (Newport's phrase) and stop thinking about work until the next session.

## Drain the shallows
- Batch all admin into the shallow block. Do not reply to review comments in the middle of a deep block.
- Quantify: `deepwork.py week` shows deep vs shallow minutes. If shallow exceeds 25%, the next retro must cut something (a ceremony, a tool setup, a notification).
- Say no: do not add new learning projects mid-sprint. Park them in the backlog.

## Between sessions (Mon-Fri)
Nothing required. The program is designed for rest: sleep consolidates learning. Optional and tiny: a 10-minute flashcard run, a walk thinking about the open ticket. Never code on weekdays as "catch up" unless you choose to; if you do, it counts and is logged.

## Why this works
Skill is attention x time. Distraction residue means a single glance at a feed taxes the next 10-20 minutes. Two protected 90-minute blocks beat five fragmented hours. The ritual removes the decision to start, the shutdown removes the open loops, and the scoreboard makes depth visible, because what is measured gets protected.
