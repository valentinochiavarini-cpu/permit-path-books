# Figures for Chapter 2, second pass (tag signs2)

Written 2026-10-28. Four new panels plus a fix to `signs_regulatory_more.svg`. Hand-written SVG in the style of `signs_regulatory_core.svg`, CSS classes prefixed with the figure name, Inter, MUTCD colors from `briefs/FIGURES_BRIEF.md`, viewBox width 460 and height 260 or less. Every color is named in a label, sub-label or caption. Generator script kept in the scratchpad; the SVG files are the source. Grayscale and color previews checked with `tools/render_fig.py`.

| File | What it shows | Source | Placed |
|---|---|---|---|
| `signs_colors.svg` (460 x 242) | One sign per color with the color name and meaning: red Stop (stop, yield, not allowed), white Speed Limit (rules), yellow curve (general warning), fluorescent yellow-green pedestrian (school, walkers, bikes), orange ROAD WORK (work zone), green destination sign (direction, guide), blue H (motorist services), brown camping (recreation, parks), fluorescent pink INCIDENT AHEAD (incident), black One Way (one way, night speed). | MUTCD 11th ed. Section 2A.06 / Table 2A-2 colors; 2C.02 (yellow-green allowed for pedestrian, bicycle, playground); Part 6 (orange, pink) | 2.3, after the Test trap callout |
| `signs_regulatory_extra.svg` (460 x 256) | No Parking R8-3 (black P, red circle and slash, white square), No Right Turn R3-1, No Turn on Red R10-11a (word message), Slower Traffic Keep Right R4-3, Stop with ALL WAY plaque R1-3P (white legend and border on red), accessible reserved parking R7-8 (green legend on white, white wheelchair symbol on blue). | MUTCD 11th ed. 2B.04 (R1-3P colors), 2B.26, 2B.38, 2B.52 to 2B.53, 2B.60; FHWA figure long descriptions 2B-10, 2B-24, 2B-25, 2B-27 | 2.4, after the passing signs paragraph, with a one-sentence lead-in |
| `signs_warning_more.svg` (460 x 238) | Pedestrian W11-2 (yellow-green), Bicycle W11-1, Deer W11-3, Winding Road W1-5, Sharp Turn W1-1, Hill W7-1 (truck on downgrade), Added Lane W4-3, Low Clearance W12-2 with 12'-6", Yield Ahead W3-2, Advisory Exit Speed W13-2 (EXIT 25 MPH, yellow vertical rectangle). | MUTCD 11th ed. 2C.07, 2C.12, 2C.14, 2C.25, 2C.35, 2C.46, 2C.55; FHWA long descriptions 2C-1, 2C-4, 2C-5, 2C-6, 2C-8, 2C-10, 2C-11 | 2.5, after People and animals, with a one-sentence lead-in |
| `signs_guide.svg` (460 x 236) | Interstate shield (red top, blue body, white number), U.S. route (white shield, black number on black square), generic state route marker labeled as varying by state, green mile marker, green exit sign with EXIT 47 tab, blue H, gas, food, lodging, brown camping and picnic area. | MUTCD 11th ed. Chapter 2D (M1-1, M1-4), 2H (D10 reference location signs), 2E exit numbering, 2I/2J (services), 2M (recreation) | 2.8, after the blue and brown paragraph, with a one-sentence lead-in on U.S. and state markers |
| `signs_regulatory_more.svg` (fixed) | Keep Right redrawn to R4-7: island nose at the top left, upward arrow starting low left and curving to pass right of the nose. Sub-label now "White rectangle, pass right". | FHWA Figure 2B-10 (2009) and 2B-8 (2003) long descriptions of R4-7 | unchanged (2.4) |

## Text changes in ch02
- Four image lines, three one-sentence lead-ins (2.4, 2.5, 2.8).
- 2.5 Road surface: "12 FT 6 IN" changed to `12'-6" (12 feet 6 inches)` to match the W12-2 legend drawn in the panel. No C02 question tests the format.
- No paragraph shortened; every fact tested by C02-001 to C02-030 is still in the text. Bank not edited.

## Checks
- `tools/originality_check.py check core/ch02.md`: passed (0.20%, 0 copied runs). Core preview build: QA passed.
- No em or en dashes, years, brand or state names in the figures.

## Unsure
- W12-2 legend format: FHWA's 2009 figure shows 12'-6"; the 11th edition text gives no example. W12-2a (rectangle) uses 14 FT 4 IN.
- Black color meaning "night speed" refers to the R2-3P NIGHT plaque style per Table 2A-2; not taught elsewhere in ch02.
- Symbol artwork (deer, hill truck, service and recreation pictographs) is simplified, not to Standard Highway Signs dimensions.
- U.S. route shield outline is an approximation of M1-4.
