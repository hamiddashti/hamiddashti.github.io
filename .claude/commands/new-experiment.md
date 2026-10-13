---
description: Create a dated sandbox in experiments/ for a design or content trial
argument-hint: "<slug>"
---

Create `experiments/<today as YYYY-MM-DD>-$ARGUMENTS/`. If no slug was given, ask for one: 2–4 lowercase words joined by hyphens, such as `homepage-layout`.

Write a `NOTES.md` in the new folder:

    # <slug>
    **Started:** YYYY-MM-DD
    **Goal:** <what this trial should show or decide>
    **Approach:** <what will be tried; which live files it starts from>
    **Outcome:** in progress
    **Notebook:** lab/notebook/YYYY-MM.md, entry YYYY-MM-DD

Later, Outcome becomes `worked → promote`, `dead end` or `parked`, with one line on why.

If the trial reworks a page, offer to copy that page and `css/style.css` into the folder. In the copy:
- Rewrite the asset paths to `../../images/…`, `../../data/…` and `../../js/…`.
- Point the stylesheet link at the local copy of `style.css`.

Then remind the user:
- Scratch work stays in this folder. Live files aren't touched until `/promote`.
- Site assets are referenced by path, not copied in. Screenshots and exports here are gitignored.
- To preview, run `python3 -m http.server 8000` from the repo root and open `http://localhost:8000/experiments/<folder>/`.
- `/promote` moves the parts that work into the live site.
