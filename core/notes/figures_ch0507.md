# Figures: Chapters 5, 6 and 7 (tag ch0507)

Drawn 2026-10-28 by hand in SVG, original work. Per the run leader's update: full color, every color named in a label or caption, viewBox 460 wide and 260 or less tall, 2 to 3 figures per chapter. The CSS classes in each file have a figure prefix (for example `rb_lbl`), because the PDF inlines every SVG and a shared `.lbl` rule from another figure would override these (it did in the first build).

| File | What it shows | Source | Placed |
|---|---|---|---|
| `turn_lane_paths.svg` (460 x 252) | Three top-down panels: right turn from the right lane into the right lane; left turn ending in the lane just right of the double yellow center line; left turn from a two way street onto a one way street, ending in the far left lane | Ch 5 text 5.2, 5.3, 5.4 table; bank C05-003, C05-005, C05-009; NY manual Ch 5, CA handbook (see ch05_notes.md) | ch05.md, end of 5.4 Turns on One Way Streets |
| `roundabout_two_lane.svg` (460 x 260) | Two lane roundabout: (1) yield to the crosswalk, (2) look left at the yield line (white triangles), circling traffic goes first, (3) counterclockwise flow; right lane takes the first exit to the right (dashed path), left lane goes around to the left exit (solid path); straight ahead either lane as signs show. Truck apron drawn around the island | Ch 5 text 5.7 and its table; bank C05-016, C05-017, C05-019, C05-020; yield line markings MUTCD 11th ed. Part 3 (section number not rechecked) | ch05.md, end of Multi-Lane Roundabouts |
| `hand_signals.svg` (460 x 196) | Rear view of a car with the driver's left arm: straight out (left turn), bent up (right turn), bent down (slow down or stop) | Ch 5 text 5.8 table; bank C05-023 to C05-025; Uniform Vehicle Code 11-605 | ch05.md, end of 5.8 Hand Signals |
| `stopping_distance.svg` (460 x 200) | Two bars to scale: perception (yellow), reaction (orange), braking (red striped). At twice the speed, perception and reaction double and braking is four times as long. Example speeds 30 and 60 mph as in the text; no feet values | Ch 6 text 6.4; bank C06-005 to C06-007 | ch06.md, after "Braking Distance and Speed" paragraph |
| `following_count.svg` (460 x 210) | Two steps: start counting when the back of the car ahead passes a fixed point; stop when your front bumper reaches it. No number of seconds (the state insert gives it) | Ch 6 text 6.5; bank C06-011, C06-012 | ch06.md, How to Count It, just before `{{INSERT:following_distance}}` |
| `blind_spots.svg` (460 x 250) | Top-down: light blue mirror views (inside and both side mirrors), orange striped blind spots beside and behind each shoulder, a car hidden in the left one; head check note | Ch 6 text 6.8; bank C06-025, C06-026, C06-028 | ch06.md, end of Set Your Mirrors to Help |
| `passing_two_lane.svg` (460 x 170) | Passing on a two-lane road with a broken yellow center line: (1) check, signal left, (2) fully in the left lane, speed up, never over the limit, (3) signal right and return when both headlights of the passed car show in your inside mirror | Ch 7 text 7.3; bank C07-007, C07-008, C07-011 | ch07.md, end of How to Pass steps |
| `freeway_merge.svg` (460 x 200) | On-ramp (look for a gap, signal), acceleration lane (speed up to match traffic), merge area (head check, move into the gap in the right lane). Freeway left edge yellow, lane line broken white, acceleration lane separated by a dotted white line | Ch 7 text 7.6; bank C07-018 to C07-020; lane line types MUTCD 11th ed. Part 3 (section numbers not rechecked) | ch07.md, end of How to Merge steps |

## Not drawn (on purpose)
- Railroad crossing with the 15 foot stop line, three-point turn, multiple turn lanes, HOV diamond: dropped to keep 2 to 3 figures per chapter. The railroad signs are already covered in Chapter 2 and the diamond in Chapter 3.

## Checks
- Grayscale previews and the built core PDF (pages 49, 53, 54, 65, 66, 70, 78, 81) inspected; no clipped text or overlaps.
- `python3 tools/originality_check.py check core/ch05.md core/ch06.md core/ch07.md`: passed (0.14 percent). Core build QA passed.
- No em or en dashes, years, brand or state names in the figures or captions.
