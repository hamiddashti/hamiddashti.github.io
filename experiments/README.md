# experiments/

These are sandboxes for design and content trials, one folder each: `YYYY-MM-DD-slug/` with a `NOTES.md` (Goal, Approach, Outcome, Notebook). Create one with `/new-experiment <slug>`.

- Scratch work stays in its folder. Nothing here is linked from the live site, and `_config.yml` keeps the whole folder off it.
- Reference site assets by relative path (`../../images/…`, `../../data/…`) instead of copying them in.
- To try out a page, copy it here together with its own copy of `style.css`, so the live stylesheet stays untouched. While `python3 -m http.server 8000` runs from the repo root, preview it at `http://localhost:8000/experiments/<folder>/`.
- Screenshots and exports in this folder are gitignored, so git stays text-only.
- `/promote` moves a working trial into the live site. The folder is **kept** afterwards: its `NOTES.md` is marked promoted, and it is committed. Never delete an experiment.
