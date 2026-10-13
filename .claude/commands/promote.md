---
description: Move an experiment into the live site, either light (a contained change) or deep (a structural change)
argument-hint: "[light|deep] <experiment folder or slug>"
---

Arguments: $ARGUMENTS. Find the experiment under `experiments/` (match on the slug if no date was given), then read its `NOTES.md` and its files.

**Choose the mode and state it in one line, with the reason.** If the user named a mode, use it, unless it is clearly wrong; in that case, say why and ask.
- **light:** a contained change that goes into existing live files. Examples: one section's markup, a few CSS rules, a fix in the data, a wording change. Nothing new to maintain.
- **deep:** a structural change that adds something to maintain. Examples: a new page, a page rebuilt around a new layout, a shared template such as Jekyll `_includes`, a script or build step in `scripts/`.
- If the signals point both ways, ask. When in doubt, prefer light.

**light**
1. Apply the change to the live files, following the CLAUDE.md conventions:
   - Styles go in `css/style.css`, not inline.
   - Asset paths are relative to the page's real location, not `../../`.
   - If the shared head, nav or footer changes, change all four pages.
2. Don't change behavior beyond what the experiment showed. If part of the experiment was wrong, say so, and ask before fixing it some other way.
3. Preview locally at desktop width and at about 375 px. Run the `site-check` agent on the pages you touched.
4. Leave the experiment folder alone, except `NOTES.md`: set Outcome to `promoted (light) → <files>`. Note the promotion for the notebook entry.

**deep**
1. Build the change in the live tree, cleaned up to the conventions:
   - Comment any markup or JS whose purpose isn't obvious, and give every JS function a comment.
   - No inline styles.
   - Scripts follow PEP 8, have docstrings, take paths from `scripts/config.py`, write atomically and are idempotent.
2. If the change adds a dependency, add `environment.yml` and a lockfile generated where the code runs. Update the Environment section and the repo map in CLAUDE.md.
3. Verify: preview every live page locally, then run the `site-check` and `code-standards` agents.
4. If a hard-to-reverse choice is built in (templating, URL changes, removing a page), write a decision record.
5. Set the experiment's Outcome to `promoted (deep) → <path>`.

**Both modes**
- Never delete or move the experiment folder. It stays as the record of how the change was made; only its `NOTES.md` Outcome changes. Commit it along with the promotion.
- If the promotion changes what visitors see, it gets a notebook entry. Once it is pushed live, it also gets a RESULTS.md row.
- Offer to commit on the working branch (`develop`, if that is the policy). Don't push. Give the user the push or merge command, and say what will change on the live site.
