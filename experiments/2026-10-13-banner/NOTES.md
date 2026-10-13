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

**Version 3 (trial, not live):** the user's wife found the banner "too 90s". The boxed diagram with labels inside a banner is what dates it.
- `banner-earth-animated3.svg`: the user's `banner-earth-animated2.svg` with the diagram groups and the dashed sun-satellite line removed, and nothing else changed. It keeps the ridges, sun, sunbeam, canopy scattering, the photon (still hidden when motion is turned off) and the satellite. Cropped at 70%, so the sun and satellite sit either side of the page centre, and phones show the satellite and photon.
- `esm-iam-figure.svg`: the diagram as a figure under the Research heading. Soft tinted panels instead of dashed frames: teal for the ESM, maroon for the IAM. Sentence-case labels, the groups spelled out, coupling arrows in maroon, and the resistor and ground symbol kept, with "respiration" labelled. On phones it scrolls sideways at a readable size.
- The `banner.css` rules for both are trial-only. At promotion they move into `css/style.css`.

**Version 4 (trial, not live):** the user uploaded their own `banner-earth-animated3.svg` (14:19), which has a new, modern diagram in the banner: labels on soft translucent ESM/IAM panels and curved flow arrows, with no boxes. They asked to stop the animation and drop the photon paths, keeping the remote sensing and the new diagram.
- `banner-earth-rs.svg`: their animated3 with the photon, sunbeam, canopy scatter lines and dots, the line up to the sensor, and the dashed sun-satellite line and its dot removed. It has no animation. It keeps the diagram, sun, orbit, satellite, swath cone and footprint glow. Centred crop.
- Width note: everything fits from about 1200 px wide up. Narrower windows (e.g. a VS Code pane, about 1000 px) cut off "Human systems" and the satellite. Phones show the ESM part and the sun.
- `esm-iam-figure.svg` is still in the Research section of the trial page. With the diagram back in the banner it duplicates it, so decide whether to keep it.

**Version 5, current (trial, not live):** the user tidied this folder at 14:24. They deleted the animated, animated2, animated3, rs and boreal SVGs and saved their latest static banner as `banner-earth.svg` (14:25). It has the modern diagram (moved right), the sun moved in closer, and the satellite with its swath and footprint moved in closer. There is no animation. `banner.css` now uses it at a 54% crop, and the whole composition fits from about 1000 px wide upward. The deleted animated2, animated3 and rs files had never been committed. The animated and boreal ones are in git (commit 8d4eb0e).

**Research figure dropped:** the user removed the ESM/IAM figure from the Research section (the diagram is in the banner instead). `esm-iam-figure.svg` stays in this folder as a record; it was never on the live site.

**Notebook:** lab/notebook/2026-10.md, entry 2026-10-13
