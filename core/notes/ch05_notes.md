# Chapter 5 notes: Turns, Roundabouts and Railroad Crossings

Written 2026-10-27.

## Facts verified
- Signal before braking or turning; right turn as far right as possible, avoid wide turns; left turn lane positions for two way and one way combinations; wait with wheels straight; complete left turn right of center line; U-turn from left lane, not where drivers cannot see you from 500 feet, not on limited access highways, not where NO U-TURN posted; three-point turn steps: New York State Driver's Manual, Chapter 5 (https://dmv.ny.gov/new-york-state-drivers-manual-practice-tests/chapter-5-intersections-and-turns). The text gives no state number for signaling distance (New York uses 100 feet; others differ) and says "about half a block" in town.
- Lane positions on one way streets and do not assume a signaling oncoming car will turn; U-turns not allowed on railroad crossings: California Driver Handbook, Navigating the Roads (https://www.dmv.ca.gov/portal/handbook/california-driver-handbook/navigating-the-roads/).
- Roundabouts: yield to circulating traffic, enter to the right, counterclockwise, do not stop or pass, signal when exiting, go around again if you miss the exit; multi-lane: right lane for right turn, either for straight, left lane for left turn, exit from the lane you entered: California handbook, Laws and Rules of the Road. Yield to pedestrians at entry and exit crosswalks, signal right before exit, do not pass a bicycle inside: New York manual Chapter 8.
- Railroad: crossbuck, number of tracks plaque (8B.03); Crossbuck Assembly with YIELD default (8B.04); Emergency Notification System blue sign with phone number and USDOT crossing number (8B.27); RXR markings (8C.02); stop line at least 15 feet from nearest rail (8C.03); flashing light signals two red lights alternating (8D.02); gates red and white striped (8D.03): https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/part8.pdf
- Stalled vehicle: get out, move away, run toward the train at a 45 degree angle away from the tracks, call the number on the blue sign; freight train at 55 mph can need a mile or more to stop; never race a train; never drive around gates: Operation Lifesaver, https://oli.org/site/nc/safety-tips

## From general knowledge, not fetched (confirm in fact check)
- Stop 15 to 50 feet from the nearest rail when a train approaches: Uniform Vehicle Code 11-701 and most state manuals; text says "the distance most states use".
- Train overhang about three feet beyond the rails (Operation Lifesaver material); could be softened.
- Hand signals (left straight out, right bent up, slow or stop bent down), cyclist right arm out to the right: standard in all state manuals; Uniform Vehicle Code 11-605.
- Do not shift gears on the tracks (several state manuals; CDL manuals).
- School buses and hazmat vehicles must stop at all crossings: 49 CFR 392.10.
- Bike lane right turn merge where the line becomes broken: California requires it within 200 feet; other states vary, so text says "many states let you, or even require you to".
- Truck apron and emergency vehicles in roundabouts (exit, then pull over): FHWA roundabout guidance; the FHWA page fetched did not include the detail.

## Rules that vary by state (inserts)
- `u_turn`: business district limits, U-turns at signals, across double yellow, required sight distance (for example 500 feet in New York, 200 feet residential rule in California).
- Signal distance before a turn (100 feet in many states, more on highways in some): no insert key in the spec, so the text avoids a number. Flag for the spec owner: consider adding a state figure to Chapter 1 or the `vehicle_rules` insert.
- Railroad stop distance (15 to 50 feet) is close to universal but not checked in all 15 target states.

## Uncertain
- Whether all 15 target states use exactly 15 to 50 feet; question C05 on stopping asks only "at least 15 feet", which matches the MUTCD stop line minimum.
