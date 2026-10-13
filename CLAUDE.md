# hamiddashti.github.io: project guide

This is Hamid Dashti's personal academic website, live at https://hamiddashti.github.io. It holds a short bio, research areas, skills, a publication list and the CV. The audience is other academics. Within one screen a visitor should grasp what Hamid works on, and reach the main publications, the CV and the projects in one click. The design should be simple, professional and attractive, in that order.

**Pipeline.** The site is hand-written HTML with one stylesheet and a little plain JavaScript. There is no framework and no build step of its own.
1. Edit a page, a data file or an asset.
2. Preview it locally.
3. Push to `main`. GitHub Pages then runs its default Jekyll build. The HTML pages have no front matter, so Jekyll copies them unchanged. It skips anything whose name starts with `_` or `.`, plus everything listed under `exclude:` in `_config.yml`.

The change is live a minute or two after the push. `publications.html` and `projects.html` fetch `data/*.json` in the browser and build their lists with JavaScript. That fetch fails on a page opened straight from disk (`file://`), so always preview through a local server (see Environment).

## Repo map

**Live site.** Everything here is public at `hamiddashti.github.io/<path>`.

| Path | What it is |
|---|---|
| `index.html` | About page: bio, research, skills, contact links |
| `publications.html` | Publication list rendered from `data/publications.json`, with status filters |
| `cv.html` | Embeds `files/CV.pdf` |
| `projects.html` | Project cards from `data/projects.json`. Removed from the nav in 96155d0 ("will add later"), but still live at its URL |
| `css/style.css` | The only stylesheet the live pages use |
| `js/nav.js` | Highlights the active nav link and opens the mobile menu |
| `data/` | `publications.json`, `projects.json`. Page content kept as data; sources are in DATA.md |
| `files/` | `CV.pdf`, the only copy of the CV in the repo. It is exported from a source document kept elsewhere (see DATA.md) |
| `images/` | Profile photo and project thumbnails |
| `_config.yml` | Lists the repo files that the Pages build must not publish. It does nothing else |

**Legacy.** The pre-2026 site (`_backup/`, `pages/`, `styles/`), `images/tmp.jpg` and `files/Resume.pdf` were removed on 2026-10-13. To recover any of them, use git history before that commit, e.g. `git show 96155d0:pages/projects.html`.

**Workflow.** `_config.yml` keeps these files off the website, which stays public whatever the repo's visibility. Whether they can also be read on github.com depends on that visibility (see DATA.md).

| Path | What it is |
|---|---|
| `CLAUDE.md`, `STATE.md` | This guide and the rolling status. Both are auto-loaded |
| `ROADMAP.md` | Milestones and the fix list |
| `DATA.md` | Where each piece of content comes from: CV source, photos, publication list, analytics |
| `experiments/YYYY-MM-DD-slug/` | One trial at a time. Each has its own `index.html` (assets via `../../`, plus a small CSS override), which the user opens in VS Code. Promote to root when approved. **Never delete an experiment folder, even after promotion.** Mark it promoted in its `NOTES.md` and commit it |
| `lab/notebook/` | Monthly session log, append-only |
| `lab/decisions/` | Numbered decision records and their index |
| `results/RESULTS.md` | Manifest of changes that went live |
| `scripts/` | Helper scripts. `make_banner.py` draws `images/banner-*.svg`; `config.py` holds default paths |
| `.claude/commands/`, `.claude/agents/` | Slash commands and the read-only check agents |

## Session protocol

- **Start: `/catch-up`.**
- **End: `/wrap-up`:**
  1. Update STATE.md.
  2. Append a notebook entry to `lab/notebook/YYYY-MM.md`.
  3. Write a decision record if a hard-to-reverse choice was made.
  4. Add a RESULTS.md row for any change that went live.
  5. Offer to commit.
- At a milestone in ROADMAP.md, run **`/milestone`**.
- Other commands: `/new-experiment <slug>`, `/promote [light|deep] <experiment>`, `/code`.

## Conventions

**HTML, CSS and JS (the live site)**
- The four live pages share the same `<head>` block, nav and footer, copied into each page by hand. When you change one, change all four in the same commit. There is no shared template yet, which is how the footer email got out of sync.
- Styles go in `css/style.css`. Don't add new inline `style=""` attributes. When you touch a page, move its existing ones into the stylesheet.
- Keep the existing section markers (`<!-- ===== NAV ===== -->`, `// ── Render cards ──`). Add a comment to any markup, CSS or JS whose purpose isn't obvious.
- JS is plain browser JS with no libraries. Every function gets a one-line comment saying what it does.
- Local assets use relative paths (`images/x.jpg`, not `/images/x.jpg`), and the case must match exactly. GitHub Pages is case-sensitive; macOS is not.
- If a page already reads some content from `data/*.json`, that content stays in the JSON. Don't hard-code a publication into the HTML.
- Images: resize before committing. The 160 px avatar needs about 480 px. Keep each image under about 300 KB, and give every `<img>` a real `alt` text.
- Links that open a new tab use `target="_blank" rel="noopener"`.

**Helper scripts (`scripts/`)**
- Python and PEP 8, with a docstring on every function and comments on non-trivial logic.
- Paths are function arguments, and their defaults live in one module, `scripts/config.py`. Nothing is hard-wired.
- Writes are atomic: write to `.tmp`, then rename. Entrypoints are idempotent: skip if the output exists.
- Record any dependency under Environment below.

**Notebooks.** None are expected. If one is added, it lives in `experiments/`, and every code cell has a markdown cell above it saying what the cell does.

**Images and screenshots.** Site images in `images/` and `files/` are content, so they are committed. Screenshots and exports made during experiments are not committed (see `.gitignore`).

**Git.** Work on `develop`. `main` is what GitHub Pages publishes, so merging `develop` into `main` and pushing means going live. Commit at logical stops. Record the SHA in the notebook entry, and also in RESULTS.md for anything that went live.

**Reproducibility chain.** Every live change must be reconstructable from these six things. Never break the chain.
1. The notebook entry.
2. The decision record, if one applies.
3. The git SHA.
4. The DATA.md source for the content.
5. The live URL.
6. The environment lockfile, once one exists.

There is no lockfile yet because the site has no dependencies. If a script or build step adds dependencies, add `environment.yml` plus a lockfile generated where it runs.

## Environment

- Nothing to install or activate. You only need a browser, plus Python 3 for the local server.
- **How the user reviews changes:** they open an `index.html` in VS Code and view it rendered. For visual changes, work in one `experiments/` folder with its own `index.html` and promote to root when the user approves. Small text or data fixes can go straight into the root files. Don't make several variants to choose between, and don't put screenshots in replies. A quick check of your own is fine.
- Local server, if you need one for your own check: `python3 -m http.server 8000` from the repo root, then http://localhost:8000. Pages that fetch JSON need a server.
- Publish: merge `develop` into `main` and push `main`. The change is live in about 1–2 minutes. If it isn't, look at the repo's Actions tab ("pages build and deployment").
- Small, reversible steps. Commit on `develop` when the user is happy, so a change can be undone. Run the `site-check` agent before publishing.
- Local preview ignores `_config.yml`, so excluded files open locally even though they aren't published.
- The CV (`files/CV.pdf`) is the source for the site's text. poppler isn't installed, so extract its text with macOS PDFKit:
  `osascript -l JavaScript -e 'ObjC.import("PDFKit"); var d=$.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath("files/CV.pdf")); var o=[]; for (var i=0;i<d.pageCount;i++) o.push(d.pageAtIndex(i).string.js); o.join("\n")'`

## Standing behaviors

- Push to `main` (publish) only when the user explicitly asks in that conversation. Otherwise prepare the commit, the push command and a one-line note on what will change on the live site.
- While `/code` is active, hand back cells and don't apply them.
- Treat the external tools and services the user names as accepted (none named yet). Don't propose auditing or replacing them.
- Before acting on a recalled note, verify that the file or function it names still exists.
- Use plain words in files and replies. Name the actual thing.

@STATE.md
