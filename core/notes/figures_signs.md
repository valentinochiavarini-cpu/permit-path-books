# Figures for Chapter 2, Road Signs (tag signs)

Written 2026-10-28. Six panels in ch02 in total, including the existing `signs_regulatory_core.svg`, per the run leader's update (shorter book, full color kept, viewBox height 260 or less for new panels). Hand-written SVG in `layout/fig/`, style of `signs_regulatory_core.svg`; every sign carries a label and a sub-label naming its color or meaning. Grayscale previews checked with `tools/render_fig.py`. The generator script stayed in the scratchpad; the SVG files are the source.

| File | What it shows | Source | Placed |
|---|---|---|---|
| `signs_shapes.svg` (460 x 250) | Nine shapes with meaning and color: octagon (Stop, red), triangle point down (Yield, red and white), circle (railroad ahead, yellow), pennant (No Passing Zone, yellow), pentagon (school, yellow-green), crossbuck (white), diamond (warning, yellow), vertical rectangle (regulatory, white), horizontal rectangle (mostly guide, green). | MUTCD 11th ed. Section 2A.05, Table 2A-1; Table 2A-2 colors | 2.2, after "If you see an upside down triangle, you must yield." |
| `signs_regulatory_core.svg` (existing, not redrawn) | Stop, Yield, Speed Limit, Do Not Enter, Wrong Way, One Way | existing | 2.4, after the opening paragraph of the section |
| `signs_regulatory_more.svg` (460 x 244) | No Left Turn, No U-Turn (red circle and slash on white), Keep Right (R4-7: island nose, arrow passing right), Left Turn Only lane use sign with ONLY, Do Not Pass (white, right side), No Passing Zone pennant (yellow, left side). | MUTCD 2B (R3-2, R3-4, R3-5L, R4-1, R4-7; 2009 Figure 2B-10 description); W14-3 Section 2C.45 area, Figure 2C-8 description | 2.4, end of Passing Signs |
| `signs_warning.svg` (460 x 260) | 12 yellow warning signs: curve with 25 MPH advisory plaque, chevron, Merge (W4-1), Lane Ends (W4-2), Divided Highway (W6-1), Divided Highway Ends (W6-2), Two Way Traffic (W6-3), Slippery When Wet, crossroad, T, Stop Ahead, Signal Ahead. | MUTCD 2C (2C.08 chevron vertical rectangle, no border; 2C.59 plaque); symbol layouts from FHWA figure long descriptions 2C-3 and 2C-8 (2003/2009 editions, unchanged symbols) | 2.5, end of Road Surface and Clearance |
| `signs_school.svg` (460 x 156) | School pentagon (S1-1, fluorescent yellow-green, two children); school crossing with diagonal downward arrow plaque (W16-7P); School Speed Limit assembly (SCHOOL plaque S4-3P yellow-green, white R2-1 with 20, WHEN FLASHING S4-4P white); END SCHOOL ZONE (S5-2, white). | MUTCD Part 7, 7B; FHWA Figure 7B-1 long description | 2.6, after the bullet list, before the crossing guard paragraph |
| `signs_work_zone.svg` (460 x 240) | ROAD WORK AHEAD (orange diamond), flagger paddle both faces (STOP white on red, SLOW black on orange), cone and drum, vertical panel with arrow on the low side of the stripes, barricade with ROAD CLOSED, arrow board flashing left, arrow board caution mode (four corner lights), INCIDENT AHEAD (fluorescent pink). | MUTCD Part 6 (6D.02 paddle, 6H.01, 6H.02, 6K channelizing devices, arrow board caution mode) | 2.7, after Incident Signs, before the Remember it callout |

## Checks
- Figures match ch02 text and bank questions C02 (shapes, pennant, pentagon, orange diamond, advisory plaque vs Speed Limit, Merge vs Lane Ends, two arrows up and down, Divided Highway Ends, WHEN FLASHING plaque, diagonal down arrow plaque, SLOW paddle, arrow board left, channeling devices, slippery when wet).
- No em or en dashes, years, brand or state names in any figure. School speed limit shows 20 as the MUTCD example value; the caption does not give a number.
- `tools/originality_check.py check core/ch02.md`: passed (0.13%).
- Chapter text unchanged apart from the six image lines.

## Unsure
- Low Clearance legend format (12 FT 6 IN vs 12'-6"): not drawn, so no conflict.
- Barricade rail stripe direction for a full road closure: drawn as a symmetric pattern; it is decorative here and the text's stripe rule is shown on the vertical panel only.
- Chevron drawn without border per 2C.08.

## Dropped (owner wants a shorter book)
Guide signs panel (Interstate and U.S. shields, exit, blue services, brown recreation, mile marker), Y and side road, sharp turn, winding road, hill, low clearance, added lane, crossbuck with track plaque. The shapes panel and the color table already cover guide signs and the crossbuck.
