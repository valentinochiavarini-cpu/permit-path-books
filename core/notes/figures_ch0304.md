# Figures for Chapters 3 and 4 (tag ch0304)

Written 2026-10-28. Six figures, about 3 per chapter, per the run leader's update (book shorter, full color kept in PDF and EPUB, viewBox height 260 or less). All hand-written SVG in `layout/fig/`, style of `signs_regulatory_core.svg`. Grayscale previews checked with `tools/render_fig.py`. Generator script kept out of the repo (scratchpad); the SVG files are the source.

| File | What it shows | Source | Placed |
|---|---|---|---|
| `ch03_arrow_signals.svg` | Four section left turn signal four times, one lamp lit each: green arrow (go, oncoming stopped), steady yellow arrow (protected turn ending), flashing yellow arrow (turn after yielding), red arrow (do not turn). Order top to bottom red, yellow, flashing yellow, green. | MUTCD 11th ed. Sections 4A.03, 4A.04 (meanings); Chapter 4F (four section flashing yellow arrow head) | ch03, section 3.4, after the red arrow paragraph, before the flashing yellow arrow Test trap |
| `ch03_center_lines.svg` | Three two lane road strips: single broken yellow (both may pass), solid and broken yellow (only the broken side may pass), double solid yellow (no passing either side). Cars in each lane labeled May pass / No passing. | MUTCD 11th ed. Sections 3A.04, 3B.01, 3B.02 | ch03, section 3.9, after "If the solid line is on your side, you may not." |
| `ch03_center_turn_lane.svg` | Two way left turn lane: solid yellow outside, broken yellow inside on both sides, white two way left turn arrows; your car waiting in the lane, then turning left into a driveway. | MUTCD 11th ed. Section 3B.05 | ch03, section 3.10, after "Never use the center turn lane to pass or as a travel lane." |
| `ch04_four_way_stop.svg` | Three all way stop panels with numbered order: different arrival times (first to stop goes first); tie at right angles (car on your right goes first); tie facing each other (straight before your left turn). | Chapter 4 text; California Driver Handbook and New York manual Ch. 5 (see ch04_notes.md) | ch04, section 4.3, after the order table, before the Test trap |
| `ch04_no_signs_t_driveway.svg` | Uncontrolled intersection (car on your right goes first in a tie); T intersection with no signs (through road traffic from both sides goes first); leaving a driveway (stop 1 before the sidewalk, stop 2 where you can see the road). | Chapter 4 text; California handbook, New York manual Ch. 5 | ch04, end of section 4.4, after the driveway Test trap |
| `ch04_school_bus.svg` | Stopped school bus, red lights flashing, red octagon stop arm on the left side. Two lane road: traffic in both directions stops. Divided highway: traffic behind stops; other side drawn as dashed outlines labeled "state rules differ, see the box". No distances. | NHTSA school bus safety; FMVSS 131 (stop arm on the left side); chapter text 4.7 | ch04, section 4.7, after "Your state box below gives them.", just above `{{INSERT:school_bus}}` |

## Checks
- Every figure matches the chapter text and bank questions C03-004 to C03-006, C03-021, C03-022, C03-025, C04-001 to C04-003, C04-006, C04-008, C04-009, C04-021 to C04-024.
- No em or en dashes, no years, no brand or state names, no state specific values in any figure.
- `tools/originality_check.py check` passes for ch03 (0.28%) and ch04 (0.00%).
- Chapter text unchanged apart from the six image lines.

## Dropped ideas (owner wants a shorter book)
Signal layouts (vertical/horizontal), pedestrian signals, divided highway lane and edge lines, stop line and crosswalk positions, emergency vehicle pull over, Move Over. The text and tables cover these well enough.
