# 0001 — File-based memory workflow
**Date:** 2026-10-13 · **Status:** active

## Context
Work on the site happens in separate sessions, and each time the owner and an AI assistant pick it up again. With no written state, every session starts by re-reading the repo, and the reasons behind earlier changes get lost.

The owner uses a standard file-based memory setup written for research-code repos (Python `src/`, conda environments, batch jobs, theory notes). This repo is different. It is a static website that GitHub Pages publishes straight from the repo. That has two consequences:
- Every committed file is public on github.com.
- Every file the Jekyll build doesn't exclude is served on hamiddashti.github.io. For example, `/README.md` returns 200 today.

## Decision
Use the file-based memory workflow, adapted to a static site:
- CLAUDE.md and STATE.md are auto-loaded, and STATE stays at 150 lines or fewer of pointers. The notebook, decisions, RESULTS, ROADMAP and DATA files are read only when needed.
- `lab/notebook/YYYY-MM.md` is append-only. Hard-to-reverse choices get numbered records in `lab/decisions/`. `results/RESULTS.md` lists the changes that went live.
- The session commands live in `.claude/commands/`: `/catch-up`, `/wrap-up`, `/new-experiment`, `/promote`, `/code` and `/milestone`. Five read-only check agents live in `.claude/agents/`.
- `_config.yml` excludes every workflow file from the published site.

What changed from the research template:

| Template piece | Here | Why |
|---|---|---|
| `src/` as the clean line | The live site files | The site is the product |
| `src/reproducibility/` notebooks | Dropped | There are no analyses to reproduce |
| `src/_archive/` | `_backup/`, `pages/`, `styles/`, marked legacy and read-only | These old copies already exist |
| `environment.yml` and lockfile | None for now | No dependencies. Add both if a script or build step needs packages |
| `slurm/` | `scripts/`, created when first needed | There are no batch jobs |
| `lab/theory/`, `lab/literature/` | Dropped | No method derivations. The publication list is site content, tracked in DATA.md |
| RESULTS rows for figures | RESULTS rows for changes that went live | For a website, the result is what visitors see |
| One config module for paths | Relative paths in the pages; `scripts/config.py` once scripts exist | No code reads paths yet |
| `.gitignore` of `*.html *.pdf *.png …` | Only inside `experiments/` | Site pages, the CV and images are tracked content |
| "The human submits costly jobs" | "The human pushes to `main`" | Pushing `main` publishes the site |
| `repro-check`, `math-review` agents | `site-check`, `content-check` | Here, what breaks is links, assets, the build and consistency of the content |
| `/promote light` = a reproducibility notebook | light = a contained change to an existing page; deep = a structural change (new page, shared template, script) | Same purpose: move a trial from its sandbox into the live site cleanly |

## Alternatives considered
- **The template exactly as written.** It would add `src/`, `slurm/`, `environment.yml`, theory notes and a math-review agent, none of which would have anything in them. Its `.gitignore` would also silently ignore new HTML pages, PDFs and images.
- **Notes outside this repo** (a private repo, or local only). The notes would stay private, but the SHA links in the reproducibility chain would break, and the notes would be lost with the machine.
- **No `_config.yml`.** Every root `.md` file and all of `lab/` would be published on the site.

## Consequences
- `_config.yml` keeps the notes off the website. Whether they can be read on github.com depends on the repo's visibility. The repo was public when this record was written; the user made it private the same day, which took the site offline (see STATE.md). If the repo goes public again, the notes will be visible on github.com, so don't write anything private in them.
- Any new root-level workflow file must be added to `exclude:` in `_config.yml`. `continuity-check` verifies this.
- If the site moves to a generator (Jekyll layouts, Hugo, Quarto), revisit the table above in a new record that amends this one.
