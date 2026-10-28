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

# Third pass (tag signs, core upgrade, 2026-10-28)

Four new panels and 45 single-sign files, closing the sign gaps in the Pennsylvania coverage QA (33 of 95 manual signs missing). Generated from one hand-written script (`gen_signs.py` in the scratchpad: each sign is drawn once in base units where the warning diamond half-diagonal is 34, then placed in panels at scale 0.82 or less and in single files scaled to fit 0 0 100 100). Same colors, outlines, label classes and Inter text as `signs_regulatory_core.svg`. Every panel sign has a label (name), a sub-label (shape and color in words) and a second sub-label (meaning). Color and grayscale previews checked with `tools/render_fig.py` (panels, all 45 single signs on a contact sheet, and the core preview pages 12, 16, 17, 20, 23, 24, 156 at 70 dpi).

| File | What it shows | Source (MUTCD 11th ed.) | Placed |
|---|---|---|---|
| `signs_regulatory_lanes.svg` (460 x 240) | Divided Highway Crossing (white, DIVIDED / HIGHWAY, upper arrow left, lower arrow right, vertical line above and below), green guide sign with yellow EXIT ONLY panel and down arrow, LEFT TURN YIELD ON with green ball, Stop with EXCEPT RIGHT TURN plaque, Yield with TO ONCOMING TRAFFIC plaque, two way left turn only (two opposite turn arrows, ONLY) | 2B.50 R6-3 (layout from FHWA long description of R6-3); 2E EXIT ONLY panel E11-1; 2B.59 R10-12; 2B.04 R1-10P; 2B.18 R1-2aP; 2B.32 R3-9b | 2.4, new subsection "Crossings, Plaques and Exit Lanes" |
| `signs_warning_extra.svg` (460 x 240) | Large Arrow (yellow horizontal rectangle), Two-Direction Large Arrow, Reverse Curve, Reverse Turn, Side Road, Y Intersection, Circular Intersection (three counterclockwise arrows), Truck Rollover (curved arrow over a truck tipped left 45 degrees) | 2C.10 W1-6; 2C.43 W1-7; Chapter 2C W1-3, W1-4 (turn vs curve: turn where advisory speed is 30 mph or less); 2C.41 W2-2, W2-5; Chapter 2C W2-6; 2C.11 W1-13 | 2.5, new subsection "Road Shape and Intersections" |
| `signs_warning_road.svg` (460 x 240) | ROAD NARROWS, NARROW BRIDGE, ONE LANE BRIDGE, LOW SHOULDER, Shoulder Drop-Off symbol with SHOULDER DROP-OFF plaque, Horse-Drawn Vehicle, DEAD END, NO OUTLET | 2C.17 W5-1; 2C.18 W5-2; 2C.19 W5-3; 2C.29 W8-9 (3 in or less) and W8-17 / W8-17P (more than 3 in); 2C.54 W11-14; Chapter 2C W14-1, W14-2 | 2.5, new subsection "Narrow Roads, Shoulders and Dead Ends" |
| `signs_work_zone_more.svg` (460 x 240) | Flagger symbol, Worker symbol, RIGHT LANE CLOSED AHEAD, DETOUR AHEAD, DETOUR with arrow, END ROAD WORK | Part 6: W20-7, W21-1, W20-5, W20-2, M4-9, G20-2 | 2.7, after Arrow boards, before Incident signs |
| `ch03_arrow_signals.svg` (edited) | Red arrow sub-label changed from "Do not make this turn" to "Stop for this turn" | some states allow a turn on a steady red arrow after a stop (PA, FL, IL inserts) | unchanged (3.4) |

## Single-sign files for picture questions (`sq_<name>.svg`, viewBox 0 0 100 100, no labels)
New signs (28): large_arrow, two_direction_arrow, reverse_curve, reverse_turn, side_road, y_intersection, circular_intersection, truck_rollover, road_narrows, narrow_bridge, one_lane_bridge, low_shoulder, shoulder_drop_off, horse_drawn, dead_end, no_outlet, divided_highway_crossing, exit_only, left_turn_yield_green, stop_except_right, yield_to_oncoming, center_lane_left_only, flagger_ahead, workers, lane_closed_ahead, detour_ahead, detour_arrow, end_road_work.
Older signs redrawn as singles (17): stop, yield, do_not_enter, wrong_way, one_way, no_u_turn, rr_advance, crossbuck, no_passing_zone, school, merge, lane_ends, two_way_traffic, divided_highway_ends, signal_ahead, slippery, road_work_ahead (symbols copied from the existing panels so they match).
39 Chapter 2 questions use one (bank `img` field); the build prints it at 0.85 in above the options (`.fig.sq`).

## Dropped or changed on purpose
- SHARE THE ROAD plaque (W16-1P): not drawn. In the 11th edition W16-1P is the IN ROAD plaque and Chapter 2C has no SHARE THE ROAD legend. Note: `core/ch09.md` line 120 still teaches a SHARE THE ROAD plaque (not my chapter; flagged to the run leader).
- Weave area, road entering curve, parallel track railroad and route plates (JCT, TO, cardinal direction): left out to keep Chapter 2 near budget; lower test frequency in the coverage report.
- LEFT TURN YIELD ON FLASHING YELLOW ARROW (R10-12a): mentioned in Chapter 3 text only, not drawn.

## Unsure
- Symbol artwork for the truck, horse and buggy, flagger, worker and tilted car is simplified, not to Standard Highway Signs dimensions.
- W20-7 is drawn with the flagger holding a paddle; older versions show a flag.
- EXIT ONLY panel drawn on one overhead guide sign with an invented destination ("Oak Road"); 11th edition lane-arrow layouts vary.
- Word legends on the diamonds print at about 6 to 7 px in the panels (small but readable at 4.6 in wide); the single-sign versions are larger.
