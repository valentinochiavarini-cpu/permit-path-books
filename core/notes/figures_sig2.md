# Figures: signals, railroad crossing, slow moving vehicle (tag sig2)

Drawn 2026-10-28 by hand in SVG, original work, style of `signs_regulatory_core.svg`. Full MUTCD colors, every meaningful color named in a label or caption, viewBox 460 wide and 260 or less tall, CSS classes prefixed with the figure name. Grayscale previews checked with `tools/render_fig.py`. Generator script kept in the session scratchpad; the SVG files are the source.

| File | What it shows | Source | Placed |
|---|---|---|---|
| `signals_basic.svg` (460 x 196) | Five vertical three lamp signals, one lamp lit each (lit lamp circled in white, short rays for flashing): steady red (stop), steady yellow (red is next, stop if you safely can), steady green (go, but yield to anyone crossing), flashing red (treat it like a stop sign), flashing yellow (slow down, go with caution) | MUTCD 11th ed. 4A.03 (steady), 4A.04 (flashing), 4E.04 (vertical order red, yellow, green) | ch03, end of 3.3 Flashing Lights, before 3.4 and the arrow signals figure |
| `signals_ped_lane.svg` (460 x 246) | Pedestrian signals: white walking person (may start to cross), flashing orange hand with countdown 12 (do not start, finish crossing, seconds left), steady orange hand (do not enter). Lane control signals on a gantry over three lanes: green down arrow (lane open), steady yellow X (lane closing, move out safely), steady red X (lane closed). The flashing yellow X (some states only) and white two way left turn arrow are not drawn | MUTCD 11th ed. 4I.02 (walking person white, upraised hand Portland orange), 4I.04 (countdown while the hand flashes), 4T.02 and 4T.03 (lane use control signals, rectangular faces) | ch03, end of 3.7 Pedestrian Signals, before the countdown Road tip (3.6 table has no room for a figure without two back to back elements; this is the first place after both topics are taught) |
| `railroad_crossing.svg` (460 x 258) | Top-down approach, numbered: (1) round yellow W10-1 sign beside the X of the marking, (2) RXR marking with transverse lines, (3) white stop line, dimension arrow "at least 15 ft from the nearest rail", (4) crossbuck on the mast with two flashing red lights and red and white gate arm across your lane. Double yellow center line (no passing zone) | MUTCD 11th ed. 8C.02 (RXR, X opposite the W10-1 sign), 8C.03 (stop line about 8 ft before the gate, no closer than 15 ft from the nearest rail), 8B.03 (crossbuck white, black letters), 8D.02 (two red lights alternating), 8D.03 (gate arm red and white striped) | ch05, 5.9 Where to Stop, after the overhang sentence |
| `smv_emblem.svg` (460 x 200) | Rear of a buggy with the slow moving vehicle emblem (fluorescent orange triangle, red reflective border, point up); school bus from behind with flashing yellow lights (about to stop), then flashing red lights and stop arm out on its left side (you must stop) | ASABE S276 via Ohio State Ag Safety and Mich. Admin. Code R 408.13721; school bus sequence from ch04 4.7 text and NHTSA school bus safety; stop arm on the left (FMVSS 131) | ch09, 9.6, after the farm vehicle bullets, before the horse paragraph |

## Checks
- Matches chapter text and bank C03-001 to C03-003, C03-012 to C03-014, C03-016 to C03-018, C03-029, C05-026, C05-030, C09-026.
- School bus part included because ch04 4.7 teaches yellow then red with the stop arm.
- No em or en dashes, years, brand or state names, or state values in any figure. `--core-only` build: QA passed. `originality_check.py` passes ch03 (0.34%), ch05 (0.30%), ch09 (0.10%).
- Chapter text unchanged apart from the four image lines.

## Unsure
- The SMV emblem is drawn with slightly cut corners on the red border; ASABE S276 dimension drawing not seen directly.
- The countdown digit is shown in orange (as on most real heads); 4I.04 sets the countdown color as Portland orange, not rechecked in the 11th edition text.
