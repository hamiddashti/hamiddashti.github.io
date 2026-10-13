# homepage-redesign
**Started:** 2026-10-13
**Goal:** A simple, professional homepage for other academics. Within one screen a visitor should see what Hamid works on and reach the main papers, the CV and the projects in one click.
**Approach:** One page, with a short top menu (Research · Publications · Projects · CV). The order:
1. Name, position and a one-sentence research summary.
2. One row of links: Email, CV PDF, Scholar, GitHub, LinkedIn.
3. A short bio.
4. Four research themes, each with its key papers.
5. Six selected first-author papers.
6. Projects.

References: jonbarron.info (one dense page, papers as the core) and al-folio (cleaner type, a top menu, selected publications). Starts from the live `index.html` text, `data/publications.json` and `data/projects.json`.

Files:
- `index.html`: the mockup. It reads `../../data/*.json`, and the `ROOT` constant holds that path prefix.
- `style.css`: a self-contained stylesheet. Accent teal `#0f6466` (one variable), Source Serif 4 for headings, Inter for text.
- `photo-480.jpg`: square crop of `images/profile_resized.jpeg`, 480 px, 66 KB (the original is 3.1 MB). Gitignored, so regenerate it at promotion:
  `sips -c 6400 6400 --cropOffset 0 1700 images/profile_resized.jpeg --out /tmp/c.jpg && sips -Z 480 -s formatOptions 82 /tmp/c.jpg --out images/profile.jpg`

Changes from the live page:
- The CV link goes straight to the PDF.
- Added a description tag, link-preview tags and an "HD" favicon.
- The skills tag cloud became one "Models and tools" line.
- The selected-publications list is a list of DOIs in the page script. At promotion it should become a `selected` field in the JSON.
- The projects list skips the placeholder "embed" card.
- No Google Analytics tag in the mockup. Keep the tag at promotion.

Checked at 1280 px and in a 390 px frame (headless Chrome screenshots, not committed). All requests returned 200. Nothing overflows on the phone.

**Outcome:** dead end (2026-10-13). The user rejected the reference sites and this direction. They prefer to keep the current design, cleaned up and with better formatting (ROADMAP M3). The folder stays as a reference. The 480 px photo crop command above may still be useful later.
**Notebook:** lab/notebook/2026-10.md, entry 2026-10-13
