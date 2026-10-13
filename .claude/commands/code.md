---
description: Code mode, on for the rest of the session. You write one short numbered cell per turn and the user applies or runs it
argument-hint: "[what to build]"
---

Code mode is on until the user turns it off. In this mode you write the code, and the user applies or runs it.

If the user described a task ($ARGUMENTS), give a 1–2 line outline of the steps, then write `#cell1`. If they didn't, wait for the task. Write no code until asked.

Rules for every cell:
- One cell per turn. Then stop and wait for the user's result.
- Open every cell with a numbered comment saying what it does, in the file's comment style:
  - shell or Python: `#cell1: what it does`
  - HTML: `<!-- cell1: what it does -->`
  - CSS: `/* cell1: what it does */`
  - JS: `// cell1: what it does`

  The numbers continue through the whole session.
- Say where the cell goes: the exact file and place (for example "`index.html`, replace lines 110–118"), or "run in a terminal from the repo root".
- Keep each cell short, one step only.
- Use relative asset paths. If a script needs paths, take them from `scripts/config.py`.
- Follow the CLAUDE.md conventions: comments on non-obvious logic, a comment on every JS function, docstrings in Python, no inline styles.
- If a cell fails, re-issue it under the same number as `#cell3 (revised)`. Don't renumber the cells that follow.
- You may read repo files directly. For anything only the user's browser or the live site can show (console errors, the layout at a given width, a live HTTP status), write a cell that prints or shows it.
- The `#cellN:` comment is the first draft of that step's line in the commit message or notebook entry.
- Never apply the edits or run the commands yourself unless the user asks you to.
