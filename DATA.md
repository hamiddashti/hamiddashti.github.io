# DATA — content sources and provenance

The site has no datasets. Its data is the content visitors see. This file records where each piece comes from, so that any page can be rebuilt and any claim traced back to a source. Update the row whenever that content changes.

| Content | File in repo | Source of truth | How it's updated | Last changed |
|---|---|---|---|---|
| Publication list | `data/publications.json` | The CV's PUBLICATIONS section (same 26 entries, same order). Exceptions, where the site deliberately differs from the CV (checked against publisher records on 2026-10-13): [4] co-author is Luo, M. (bioRxiv); [13] keeps the full DOI; [18] links the final Biogeosciences paper; [24] is 2012 and its full title ends "Using a Lookup-Table Approach" (Crossref, DOI 10.1109/JSTARS.2012.2186118) | Edited from the CV. `volume` holds the CV's volume and pages | 2026-10-13, from the Sep 2026 CV (uncommitted) |
| CV | `files/CV.pdf` | Only the exported PDF is in the repo; the source document is kept elsewhere | Export a PDF, then replace `files/CV.pdf` | Sep 2026 version, replaced by the user on 2026-10-13 (uncommitted). The previous version was 706335e |
| Bio, research, skills | `index.html` | The CV (experience bullets, research interests, skills), plus two claims from the owner's earlier text that aren't in the CV: "over 400 eddy covariance sites" and "over $1M" (the CV's grants add up to about $1.36M) | Edited by hand | 2026-10-13, from the Sep 2026 CV (uncommitted) |
| Projects | `data/projects.json` | Written in the file | Edited by hand. The page is not in the nav | 067e744, 2026-03-26 |
| Profile photo | `images/headshot-480.jpg` | 480 px square crop of `images/headshot.jpeg`, which the user added on 2026-10-13 (1264×842 px). To regenerate: `sips -c 620 620 --cropOffset 50 370 images/headshot.jpeg --out /tmp/c.jpg && sips -Z 480 -s formatOptions 85 /tmp/c.jpg --out images/headshot-480.jpg` | Replace the crop | 2026-10-13 (uncommitted). The old photo `images/profile_resized.jpeg` is unused |
| Arctic–Boreal project image | `images/NASA_ABoVE.jpg` | <Image source URL and license> NASA imagery is usually public domain, but confirm the credit line | Replace the file | 2aa9097, 2024-01-19 |
| Dryland project image | `images/satellite-remote-sensing.jpg` | <Image source URL and license> Looks like stock clip-art of a satellite, not a figure from the work | Replace the file | 7f8868a, 2023-11-09 |

## External services and IDs
- **Hosting:** GitHub Pages, from the repo `hamiddashti/hamiddashti.github.io` (default branch `main`). The source is assumed to be "Deploy from a branch: `main`, `/ (root)`"; this was inferred from how the live site behaved. <Confirm in Settings → Pages>
- **Repo visibility:** public. The user made it private on 2026-10-13, which switched Pages off, then made it public again the same day. Pages still has to be re-enabled (ROADMAP M1).
- **Analytics:** Google Analytics 4, measurement ID `G-BQZPF62XD4`, in the `<head>` of all four live pages. The dashboard is at analytics.google.com, under the owner's account.
- **Fonts:** Google Fonts, Inter at weights 400, 500, 600 and 700.
- **Linked profiles:** Google Scholar `user=4PNlO6kAAAAJ`, LinkedIn `hamid-dashti-6274a4a4`, GitHub `hamiddashti`.
- **Custom domain:** none (there is no `CNAME` file).
