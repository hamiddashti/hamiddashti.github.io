# banner
**Started:** 2026-10-13
**Goal:** Make the homepage banner closer to Hamid's work: an Earth-observing satellite and an old-style Earth-system diagram, drawn like an electrical schematic, over the forested ridges.
**Approach:** `index.html` is a copy of the root page. It uses `../../css/style.css` plus `banner.css`, which only overrides `.banner`.
- `banner.css` shows the banner at full height. It crops left and right around 57%, because the content sits slightly right of the middle.
- `banner-earth.svg` is the banner in use. **The user hand-edited it in Inkscape, so this file is the master copy.** User edits: the sun, diagram and satellite moved, the satellite tilted, the sky gradient angled.
- The diagram is group `g17` in that file. Its contents come from `diagram_svg()` in `make_banner.py` and are spliced in, so the group's position (set by the user) stays as it is.
- `make_banner.py` reproduces the user's layout closely (sun at 1353,46; diagram at 1435,28; satellite at 2286,28, tilted 25.7°). It draws `banner-boreal.svg`, the green version. Don't rerun it over `banner-earth.svg`, because that would drop any Inkscape-only edits.

Diagram:
- **ESM frame** ("ESM · CESM / E3SM", dashed) around Atmosphere, Ocean, Vegetation and Soil.
- **IAM frame** ("IAM · GCAM") around Human Systems.
- **Coupling between them:** "food, water" (ESM → IAM) and "emissions" (IAM → ESM).
- **Inside the ESM:** the sun as the source, CO₂ exchange, heat, litter through a resistor, and a ground symbol for respiration.
- **Text:** box labels at 16 units bold, other labels at 14 units upright, dark teal `#24515c`.

To view: open this folder's `index.html` in VS Code.

**Outcome:** promoted (deep), live in commit 24bb249 on 2026-10-13.
- `banner-earth.svg` → `images/banner-earth.svg` (identical copy)
- the `.banner` rule → `css/style.css`
- `make_banner.py` → `scripts/make_banner.py` (default output `images/`)

This folder was deleted by mistake right after promotion and rebuilt the same day from the promoted copies, so its files are identical to what was promoted. Experiments are kept after promotion from now on.

**Animated version (temporary):** the user made `banner-earth-animated.svg` from their re-saved `banner-earth.svg` (13:53). It moves a dot along a 12 s looping path with a fade, using plain SVG animation (no scripts). It was promoted to `images/banner-earth-animated.svg` and put live on the site temporarily. The static line is kept commented out in `css/style.css`. The re-saved static `banner-earth.svg` was copied to `images/` as well.

**Notebook:** lab/notebook/2026-10.md, entry 2026-10-13
