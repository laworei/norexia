# On-call (from L2)

- About one incident every two sprints, at a random time inside the declared working window (Sat-Sun, 09:00-19:00 Europe/Berlin).
- The SRE lead opens an issue with **symptoms only**.
- You are the primary. Steps: **acknowledge** (comment within 15 min of seeing it), **post status** every 30 min, **mitigate**, **resolve**, then write a **blameless postmortem within 2 days** in `docs/postmortems/`.
- Tracked: time to detect, mitigate, resolve (`learner/metrics.jsonl`).
- A scheduler is optional. Without one, incidents are planned inside the sealed sprint plan and fired on your first session inside the window.
- You may ask for help with `/stuck`, as in any ticket; a level-4 hint on an incident is logged as such.
- Not on call while the program is paused.
