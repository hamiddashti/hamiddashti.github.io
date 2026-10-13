---
description: Start of session. Read STATE, the notebook and git status, then report where things stand without changing anything
argument-hint: "[keyword or #tag]"
---

Get oriented for this session without changing any file. Optional focus: $ARGUMENTS

1. Read `STATE.md`. CLAUDE.md is already loaded.
2. Read the current month's notebook, `lab/notebook/YYYY-MM.md`. If it is missing or has no entries, read the latest month that does. If the user gave a keyword or tag, grep for it first: `grep -rn "<keyword>" lab/notebook/`.
3. If the next steps refer to a milestone, skim `ROADMAP.md`. If today's work touches content sources (CV, publications, images), skim `DATA.md`.
4. Paths: the site has no config module. The path rules are in CLAUDE.md (relative asset paths, exact case, the `_config.yml` excludes). If `scripts/config.py` exists, read it.
5. Run `git status` and `git log --oneline -5`. Note the branch and any uncommitted changes. Check whether HEAD matches the SHA in STATE.md. If it doesn't, say so: work happened that isn't in the record.
6. Before relying on any path STATE.md points to, check that it still exists.
7. Report in 15 lines or fewer:
   - where things stand
   - which open decisions are waiting on the user
   - what you plan to do first

   Then wait, unless the user has already said what to do.
