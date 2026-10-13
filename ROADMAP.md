# ROADMAP

**Goal:** a simple, professional academic site for other academics. Within one screen a visitor should grasp what Hamid works on, and reach the main papers, the CV and the projects in one click. The user's priority is the design (2026-10-13). Each item names the file and the fix. Tick items here and log the work in the notebook.

## M0 — Workflow setup ✔ (2026-10-13)
File-based memory, plus a `_config.yml` that keeps the notes off the live site. See [[0001-file-based-memory-workflow]].

## M1 — Get the site back online
- [x] Repo made public again (2026-10-13).
- [ ] Re-enable Pages. The API still reports `has_pages: false`, and the site returns 404. In Settings → Pages, choose Deploy from a branch: `main`, `/ (root)`.

## M1b — Update the text from the new CV (Sep 2026) ✔ (2026-10-13, uncommitted)
- [x] `index.html`: new title (Geospatial Computational Scientist), tags, About, Research and Skills text taken from the CV.
- [x] `data/publications.json`:
  - Annual Review is now published, with a DOI.
  - Two titles corrected.
  - The food-systems paper is now a bioRxiv preprint.
  - Volume and pages added from the CV.
- [x] `publications.html`: shows the volume and pages. The filters are now All / Published / Preprints, since nothing is "in press" or "submitted" any more.
- [x] Footer email is hdashti@uchicago.edu on all four pages.

## M2 — Clean up
- [x] Removed the old site (`_backup/`, `pages/`, `styles/`), plus `images/tmp.jpg` and `files/Resume.pdf` (2026-10-13, on `develop`, not committed yet).
- [x] Untracked `.DS_Store` (2026-10-13, same change).
- [x] Footer email unified to hdashti@uchicago.edu (M1b).
- [x] Bio typos fixed by the CV-based rewrite (M1b).
- [ ] `README.md` is two lines. Say what the repo is and how to preview it.

## M3 — Clean up and format the current design (the user's priority)
The user keeps the current design (2026-10-13). They rejected the reference sites and the mockup in `experiments/2026-10-13-homepage-redesign/` (dead end). The formatting items are still to be agreed with the user:
- [ ] Inline `style=` attributes into classes in `css/style.css`.
- [ ] Publications:
  - the owner's name in bold
  - a badge only for preprints, maybe
  - no renumbering when filtered (`publications.html:103`)
- [ ] Projects: real content from the user, then put Projects back in the nav.
- [ ] Page description, link-preview (Open Graph) tags and a favicon.
- [x] Photo: replaced with the user's headshot, cropped to a 480 px square (`images/headshot-480.jpg`, 42 KB). The original `images/headshot.jpeg` is kept. The old `images/profile_resized.jpeg` (3.1 MB) is now unused (2026-10-13).
- [ ] Shared head, nav and footer: copied into each page vs. Jekyll `_includes`. Needs a decision record.

## M4 — Content accuracy (website only; the user doesn't want CV details pursued)
- [x] One Earth paper is now a bioRxiv 2025 preprint, matching the CV (M1b).
- [x] Annual Review of Plant Biology is published: 77, 529–560, with a DOI (M1b).
- [x] "Unrevealing…" title now matches the CV (M1b).
- [x] JSTARS paper corrected from Crossref: year 2012, full title, DOI. Preprint co-author corrected to Luo, M. from bioRxiv (2026-10-13).
- [ ] The author-list style is mixed: some use "&" before the last author, some use "et al.".
- [ ] `data/projects.json`:
  - "Interactive Map — Example" is a placeholder card.
  - The dryland card's "View Paper" URL is empty, though the paper is in publications.json (10.3390/rs11182141).
  - The "GitHub" buttons point to the profile, not to repos.
- [ ] Project images: `images/satellite-remote-sensing.jpg` looks like stock clip-art, and its source and license are unknown (DATA.md).

## M5 — Speed and discoverability
- [ ] The publication lists appear only after JavaScript runs. Crawlers that don't run JS, and visitors with JS off, see none. Option: put the lists in the HTML at build time (Jekyll) or with a small script.
- [ ] None of the 8 `target="_blank"` links (2 of them in the JS templates) have `rel="noopener"`. The mockup avoids new tabs.
- [ ] There is no `404.html`.
