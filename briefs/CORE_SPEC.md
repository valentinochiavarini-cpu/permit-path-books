# Permit Path core: chapter plan

The book is a state edition: Chapter 1 is written per state; Chapters 2 to 13 are the universal core, written once and filled with state inserts at build time. The order and headings below are Permit Path's own and must stay different from any other DMV series.

| Ch | File | Title | Must cover | Insert keys (state fills these) |
|---|---|---|---|---|
| 1 | state/XX/ch01.md | Your Path to a {{STATE}} License | permit eligibility and age, documents, fees, knowledge test format and pass mark, vision test, graduated license stages and limits, supervised hours, road test, adult first-timers, foreign license holders, new residents (only where a test applies), where to find the official manual | (whole chapter is state-specific) |
| 2 | core/ch02.md | Road Signs: Read Them at a Glance | shapes, colors (in words), regulatory, warning, guide, service, work zone, school zone signs, channeling devices, signs that confuse test takers | school_zone, work_zone |
| 3 | core/ch03.md | Signals, Lights and Pavement Markings | steady, flashing and arrow signals, dark or broken signals, lane control and ramp meters, pedestrian signals, yellow vs white lines, edge lines, stop lines, crosswalks, arrows and words on pavement, reversible lanes, shared center turn lanes | turn_on_red |
| 4 | core/ch04.md | Right-of-Way: Who Goes First | controlled and uncontrolled intersections, four-way stops, T intersections, entering from driveways, pedestrians and the blind, emergency vehicles and Move Over, school buses, transit buses, funeral processions, yielding vs giving up the right of way | move_over, school_bus |
| 5 | core/ch05.md | Turns, Roundabouts and Railroad Crossings | turn steps, right and left turns, one-way streets, multiple turn lanes, U-turns and three-point turns, bike lanes at turns, roundabouts (single and multi-lane), hand signals, railroad crossings and stalled vehicles | u_turn |
| 6 | core/ch06.md | Speed and Space | basic speed law, posted limits, too slow, stopping distance, following distance, space cushion, scanning, blind spots | speed_limits, following_distance |
| 7 | core/ch07.md | Lanes, Passing and Highway Driving | lane choice, changing lanes, passing rules and no-passing zones, being passed, entering and leaving a freeway, merging, HOV and express lanes, highway breakdowns | hov |
| 8 | core/ch08.md | Parking, Backing and Leaving the Curb | parallel, angle and perpendicular parking, hills and curbs, curb colors, where not to park, backing, pulling into traffic | parking_rules |
| 9 | core/ch09.md | Sharing the Road | pedestrians, bicycles, motorcycles, large trucks and no-zones, buses, farm and slow vehicles, animals, work zone workers | bicycle_passing |
| 10 | core/ch10.md | Night, Weather and Emergencies | headlights and dimming, fog, rain, hydroplaning, snow and ice, wind, skids, brake or tire failure, stuck accelerator, what to do after a crash | crash_reporting |
| 11 | core/ch11.md | Alcohol, Drugs, Distraction and Fatigue | how alcohol affects driving, BAC, zero tolerance, implied consent, DUI penalties (via insert), drugs and medicines, open container, phones and texting, other distractions, drowsy driving, road rage | bac_limits, implied_consent, dui_penalties, phone_laws |
| 12 | core/ch12.md | Your Car, Seat Belts and Passengers | pre-drive checks, dashboard warning lights, tires, lights, mirrors, seat belts, airbags, child seats, unattended children, insurance and registration basics, equipment rules | seat_belts, child_restraints, vehicle_rules |
| 13 | core/ch13.md | Test Day: Knowledge Test and Road Test | how to study the last week, test-taking tactics, what to bring, the road test route and what examiners score, common fails, after you pass | road_test |

After Chapter 13: `core/90_mocks.md` (assembled: Mock Exam 1, Mock Exam 2, Mock Answer Key) and `core/95_driving_log.md` (supervised driving log; the state's hour requirement comes from the `supervised_hours` insert).

## Chapter template
1. `# Chapter N: Title`
2. Opening: 2 or 3 short paragraphs on why the chapter matters on the test and on the road. No "In this chapter we will".
3. `> **On the test**` box: 3 to 6 bullets of what the knowledge test asks about this topic.
4. Numbered sections `## N.1 ...`, subsections `###`.
5. Tables where two or more things get confused (max 3 columns, short cells: the trim is 6 x 9).
6. Callouts, at most 8 per chapter, only these types: `> **On the test**`, `> **Test trap:**`, `> **Road tip:**`, `> **Remember it:**`.
7. Insert markers: a line containing only `{{INSERT:key}}` where the state rule belongs. Write the national rule around it; the insert adds the state's exact figure. Never print a figure that varies by state outside an insert.
8. `## Quick Review`: 6 to 10 one-line bullets.
9. `## Chapter N Quiz`: the line `{{QUIZ}}` (the build prints the 10 bank questions flagged `quiz: true` for this chapter, then `### Chapter N Quiz Answers`).
10. Practice line: `**Practice this chapter online:** scan the code or go to [APP-LINK:N] for more Chapter N questions.`

Length: 2,200 to 3,500 words per chapter before the quiz (the 6 x 9 page holds about 300 words).

## Insert file format (`state/XX/inserts.md`)
One section per key: `## key` followed by 1 to 4 short paragraphs or a small table, written as a callout-ready block (the build wraps it in a "{{STATE}} rule" box). Use `OMIT` as the whole body if the state has no special rule; the build then removes the marker. Every key in this list must exist in every state file; the build fails otherwise:
school_zone, work_zone, turn_on_red, move_over, school_bus, u_turn, speed_limits, following_distance, hov, parking_rules, bicycle_passing, crash_reporting, bac_limits, implied_consent, dui_penalties, phone_laws, seat_belts, child_restraints, vehicle_rules, road_test, supervised_hours.

## Question bank (`bank/`)
- `bank/core.json`: universal questions. `bank/XX.json`: state questions (chapter 1 topics and every insert topic).
- Record: `{"id": "C02-001", "ch": 2, "quiz": true, "q": "...", "a": "...", "b": "...", "c": "...", "d": "...", "correct": "B", "exp": "1 to 2 sentences", "src": "manual section or URL"}`. State IDs: `PA-001`.
- Core: 30 questions per chapter (2 to 13), exactly 10 flagged `quiz: true`. State: 120 to 160 per state.
- Correct letters spread about 25 percent each across every file. Exactly one defensible answer. No "all of the above" or "none of the above". No trick wording. Every question taught in the chapter it belongs to.
- Core questions must be true in every state. Anything that varies goes in the state bank.
