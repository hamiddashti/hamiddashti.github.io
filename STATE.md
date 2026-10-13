# STATE — rolling status
**Last updated:** 2026-10-13 · **Commit:** 34593ec (backup on develop, not pushed) + uncommitted homepage change · **Branch:** develop

## Current focus
Published today's homepage work: banner, maroon palette, Selected Publications, no "Published" labels. Next: the remaining formatting items (ROADMAP M3).

## Next session — start here
1. Run `/catch-up`. Check the site: `curl -s -o /dev/null -w "%{http_code}\n" https://hamiddashti.github.io/` should print 200. If it doesn't, the user needs to re-enable Pages in Settings → Pages (branch `main`, folder `/ (root)`).
2. Commit the homepage change (Skills → Selected Publications, `js/pubs.js`) on `develop` if the user is happy with it.
3. To publish: `git checkout main && git merge develop && git push origin main develop`. The user runs this. Afterwards, `https://hamiddashti.github.io/STATE.md` should print 404.
4. Agree the M3 formatting items with the user, then do them in the live files (the user doesn't want a redesign).

## What changed this session
- Added the workflow files: [[0001-file-based-memory-workflow]]. Created `develop`. Removed the legacy site, `images/tmp.jpg` and `files/Resume.pdf`.
- Homepage mockup in `experiments/2026-10-13-homepage-redesign/`: the user rejected it (dead end). The current design stays.
- The user replaced `files/CV.pdf` with the Sep 2026 CV and made the repo public again.
- Text from the CV:
  - `index.html`: title, tags, About, Research, Skills.
  - `data/publications.json`: Annual Review published, 2 titles, bioRxiv preprint, `volume` field added.
  - `publications.html`: volume shown, filters now All / Published / Preprints.
  - Footer email is the UChicago address on all 4 pages.
- Checked locally in headless Chrome: both pages render, and every request returned 200 except `/favicon.ico` (404; there is no favicon yet).
- `content-check` agent: 27 of 29 claims match the CV.
  - Text fixed: NEON AOP is airborne; the CLM5 assimilation work is credited as co-authored; the duplicate CESM2 sentence is removed; Remote Sensing 2019 and GMD 2019 citations added; tense now matches the CV.
  - Records fixed from publisher data (bioRxiv, Crossref): [4] Luo, M.; [24] JSTARS 2012, full title, DOI.
- Banner: built in `experiments/2026-10-13-banner/`, hand-edited by the user in Inkscape, then promoted. `images/banner-earth.svg` is the Inkscape master (don't regenerate it). `scripts/make_banner.py` draws the green version and the diagram code.
- Homepage photo is now the user's headshot: `images/headshot-480.jpg`, a 480 px square crop (42 KB) of `images/headshot.jpeg`. The old `images/profile_resized.jpeg` is unused.
- The user doesn't want CV details pursued: the goal is the website. CV-error items were dropped from ROADMAP.
- Committed 34593ec as a backup on `develop`.
- Then, uncommitted: removed Skills from the homepage and added Selected Publications. It shows the records with `"selected": true` (6 first-author papers), using card markup shared with the publications page in `js/pubs.js`. Checked locally: the homepage has 6 cards, the publications page 26, unchanged.

## Open decisions (the user's)
- Delete the unused `images/profile_resized.jpeg` (3.1 MB)?
- What to put under Projects.
- Which M3 formatting items to do.

## Backlog
ROADMAP.md: M1 re-enable Pages → M3 cleanup and formatting → M4 content accuracy (remaining) → M5 speed and discoverability.

## Open threads / caveats
- Headless Chrome won't go below about 500 px wide. To check phone layouts, screenshot a page that puts the site in a 390 px iframe. Port 8765 is taken by another local app.
- To read the CV text, use the PDFKit command in CLAUDE.md → Environment (poppler isn't installed).

## Where things are
- Live site: https://hamiddashti.github.io (404 until Pages is re-enabled)
- CV: files/CV.pdf (Sep 2026). Content sources: DATA.md
- Dead-end mockup: experiments/2026-10-13-homepage-redesign/NOTES.md
- Notebook: lab/notebook/2026-10.md (no entries yet; add one at /wrap-up)
- Decisions: lab/decisions/README.md · [[0001-file-based-memory-workflow]]
- Live-change manifest: results/RESULTS.md (header only) · Fix list: ROADMAP.md
