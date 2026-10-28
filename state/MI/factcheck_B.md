# Michigan fact check B

Scope: `state/MI/inserts.md` (all 28 keys, read in context in `out/MI/Permit_Path_Michigan.md`) and every `bank/MI.json` question with ch 2 to 13 (MI-038 to MI-160). Checked 2026-10-28.

Sources: MAN = What Every Driver Must Know (Michigan SOS, Oct. 2025), Drive file 1cHIqQJlfm6bpVbKbz3dgGNZm1Wx-4gzf. MCL sections read at https://www.legislature.mi.gov/documents/mcl/pdf/mcl-257-NNN.pdf (257.602b, 257.320a, 257.710d, 257.710e, 257.653a, 257.612, 257.648, 257.627a, 257.636, 257.625, 257.319, 257.700, 257.709) and https://www.legislature.mi.gov/documents/mcl/pdf/mcl-500-3009.pdf. MSP: https://www.michigan.gov/msp/divisions/ohsp/safety-programs/Impaired-Driving/impaired-driving-law. DST: https://www.michigan.gov/documents/ROAD_SKILLS_TEST_STUDY_GUIDE_05-02_21935_7.pdf.

## Legal errors fixed

| Key or ID | Old | New | Reason and source |
|---|---|---|---|
| turn_on_red | "A steady red arrow means stop, and you may not turn until the signal changes." | Red arrow follows the same rules for its turn; facing one for a left onto a two-way street, wait for the signal. | MCL 257.612(1): red arrow indications "have the same meaning as the corresponding circular indications" for the arrowed movement, so turn on red after a stop is legal on a red arrow where it would be on a red ball. MAN Ch. 5 states "cannot turn until the signal changes" only for the left-turn (flashing yellow arrow) signal head, where a left onto a two-way street is never allowed on red. New wording fits both. Paragraph 2 trimmed to stay under 90 words. |
| MI-069 (ch 3 quiz) | Right red arrow; keyed C "Wait; do not turn" | Left red arrow at a left turn signal, cross street two-way; keyed C | Old key was wrong under MCL 257.612(1) and (1)(c)(ii) (a right turn after a full stop is legal on a red arrow unless a sign forbids it), so the old item had two defensible answers. New item has one answer under both statute and manual. Options A, B, D rewritten to match the new stem; src adds MCL 257.612. |
| child_restraints | "A child in a car seat rides in the back if the car has one." | "A child under 13 rides in the back seat if the car has one." | MCL 257.710d(2) and (4) as amended by 2024 PA 21 (effective April 2, 2025): car seat children and belted children under 13 must sit in a rear seat if the vehicle has one. |
| vehicle_rules (tint) | Top 4 in of windshield "and none of the front side windows" | Top 4 in of the windshield and the front side windows | MCL 257.709(1)(a): the same top 4 inch strip is allowed on the front side windows. |
| MI-150 exp | "none is allowed on the front side windows" | "top 4 inches of the windshield and of the front side windows" | MCL 257.709(1)(a). Key unchanged. |
| bac_limits | Under 21 limit "0.02" | "0.02, or any alcohol from drinking" | MCL 257.625(6): any bodily alcohol content means 0.02 to under 0.08 or any presence of alcohol from drinking (religious service excepted). |
| MI-121 (ch 11 quiz) | Option A "0.00" | Option A "0.10" | With the any-presence rule, "0.00" could be argued as correct. Key D 0.02 unchanged; exp now mentions any alcohol. MCL 257.625(6). |

## Other fixes (accuracy or clarity)

| Key or ID | Change | Source |
|---|---|---|
| vehicle_rules (insurance) | "Liability limits start at $250,000..." (read as a minimum) rewritten: injury liability $250,000/$500,000 unless you choose lower limits, at least $50,000/$100,000; property damage $10,000 | MCL 500.3009(1), (5) |
| phone_laws | Kelsey's Law line adds "except to report an emergency" | MAN Ch. 4, Cell phone use (emergency exceptions apply to all teens); MCL 257.602c |
| underage_alcohol | "Any drug conviction ... 6 months" changed to "A first drug conviction" | MAN Ch. 2: 6 months with no prior drug violations, 1 year with a prior in 7 years |
| headlight_dimming | Adds "do not flash yours" before "look toward the right edge" | MAN Ch. 7: illegal to use or even flash high beams within 500 feet of an oncoming vehicle; counters the core advice below |
| seat_belts | "may stop you only for a missing belt" changed to "just for" | Ambiguity fix (could read as the only reason). MCL 257.710e(7) primary enforcement |
| MI-146 | Option A "only for" changed to "just for"; key A unchanged | Same ambiguity |
| speed_limits | Freeways "70 mph (minimum 55); 75 where posted" | MDOT, Speed limits, https://www.michigan.gov/mdot/travel/safety/road-users/speed-limits (2016 PA 445: 75 mph on 614 freeway miles; statutory default 70 under MCL 257.627/628); MAN Ch. 4 gives 70/55 unless posted |

## Verified, no change

- Hands-free (MCL 257.602b(4), (6), (8)): $100 first, $250 second or later (Bridge Michigan's $200 is wrong), or community service; fine doubles if at fault in a crash; course after 3 violations in 3 years. Points (MCL 257.320a(1)(x), (y)): none first, 1 second, 2 third or later. MI-123, MI-138 to MI-141 correct.
- Child seats (MCL 257.710d): rear-facing to 2 or outgrown, harness to 5 or outgrown, booster to 8 or 4 ft 9 in, airbag off for rear-facing in front, no points (710d(8)). MI-143, MI-145, MI-147 correct.
- Seat belts (MCL 257.710e): driver and front seat; under 16 all seats (710e(5) with 710d); primary unless compliance falls below 80 percent; physician exemption; no points (710e(13)). MI-142, MI-146, MI-148 correct.
- Move Over (MCL 257.653a): red, blue, white or amber; 10 mph below; move a lane or 2 vehicle widths; felony for injury or death of emergency personnel. MAN Ch. 4 covers waste, utility, maintenance vehicles. MI-075, MI-083 correct.
- School bus: 20 ft, divided highway exception, yellow overhead = prepare, double fine, 3 points (MAN Ch. 4; Ch. 2). MI-074, MI-077 to MI-079 correct.
- Turn on red (MCL 257.612(1)(c)(ii)): right on red from one-way or two-way; left on red only onto a one-way street, from a one-way or two-way street. MI-068, MI-070, MI-071 correct.
- Michigan Left: MAN Ch. 5, Michigan Lefts (unmarked crossover is single lane); freeway crossovers authorized vehicles only (sign 24). MI-053, MI-084, MI-085, MI-087 correct.
- OWI (MCL 257.625(1), (9), (12); 257.319(8)): 0.08 (no sunset in effect), 0.17 high BAC, first offense up to 93 days / $100 to $500 / 360 h; high BAC up to 180 days / $200 to $700; 180-day suspension, no restricted license first 30 days; high BAC 1 year, restricted after 45 days only with interlock; under 21: up to $250, 360 h, 30 days (restricted allowed). Points 6 / 4 (MCL 257.320a). MI-124 to MI-133 correct.
- Implied consent: 1 year, 2 years for a second within 7 years (MSP); 6 points (MCL 257.320a(8)); PBT refusal under 21: 2 points (320a(1)(v)). MI-122, MI-133 correct.
- Open container: banned in passenger area, 2 points (MCL 257.624a; 320a(1)(s)). MI-137 correct.
- Speed: 15/25/45/55/70 min 55 (MAN Ch. 4); points 1/2/3/4, work zone 3/4/5 (MCL 257.320a). School zone up to 20 below, not under 25, up to 30 min before and after (MCL 257.627a). MI-038 to MI-042, MI-089, MI-091 to MI-095 correct.
- Points system: 2 years from conviction; reexamination at 12 points in 2 years, 3 crashes in 2 years, restriction violations; 6 points reckless, OWI, leaving crash; 3 careless, signal/stop sign (MAN Ch. 2). MI-144, MI-152 to MI-155 correct.
- Signal distance: MCL 257.648 sets none. MI-086 correct.
- Bicycles: 3 ft, impracticable clause, no-passing zone pass when safe (MCL 257.636(2), (3)); 5 ft in some cities, bike lane not required (MAN Ch. 6). MI-108, MI-109, MI-111 correct.
- Headlights: half hour after sunset to half hour before sunrise; 500 ft visibility; low beams in fog, rain, snow; 500 ft dimming (MAN Ch. 7; MCL 257.700). MI-112, MI-113, MI-115, MI-120 correct.
- Crashes: move drivable cars when no serious injury; police for injury or damage over $1,000; deer reporting and "do not veer" (MAN Ch. 7). MI-114, MI-116, MI-117 correct.
- Parking, following distance, HOV, freeway lanes, passing distances, funeral processions, emergency vehicles, sign colors and sign challenge answers: all match MAN Ch. 4 to 7. Sign picture items (MI-043, 050, 052, 054 to 066) checked against `layout/fig/sq_*.svg`; each picture matches its key.
- Road test (DST): forward stop within 2 ft, 6 errors max, 25 points max on road, automatic fail at 10 mph or more over; inspection list. MI-156 to MI-160 correct.
- Every quiz-flagged state question in ch 2 to 13 is taught in its chapter's Michigan box (checked one by one; MI-069 now taught by the revised turn_on_red box).
- No em or en dashes, no years in inserts; every insert 90 words or fewer.

## Core sentences that contradict Michigan (core is out of scope; not edited)

1. `core/ch10.md` 10.1: "If an oncoming driver keeps high beams on, flash your own high beams once, quickly, as a reminder." Michigan (MAN Ch. 7) says it is illegal to use or even flash high beams within 500 feet of an oncoming vehicle. The insert now says "do not flash yours", but the core sentence right after it still advises flashing. Needs a `[[generic]]` hedge or a state-neutral rewrite.
2. `core/ch06.md` 6.7: "Aim your eyes about 12 to 15 seconds ahead" (also the Quick Review and core quiz Q4, keyed 12 to 15). The Michigan box in the same chapter and MI-096 say 20 to 30 seconds (MAN Ch. 7). Reader sees two numbers; consider "at least 12 to 15 seconds; your state manual may say more".
3. `core/ch12.md` 12.6: "Under primary enforcement, an officer can stop you only for not wearing a belt." Reads as "only for that reason". Suggest "just for" or "for that alone".
4. `core/ch13.md` 13.5 lists a rolling stop as "the classic fail". In the Michigan DST, running a stop sign is an automatic fail; an incomplete stop is scored with points. Minor; "usually" hedging would fix it.

## Open items

- Mock exam intro (`core/90_mocks.md` default size note) says each 25-question mock is "the same number as the Michigan knowledge test". The SOS does not publish the question count (sources.md, Not verified). `state/MI/mocks.json` does not exist, so the default note is used. Add a `size_note` for MI (owner or state builder).
- MCL 257.710d as amended no longer contains a nursing clause; MAN (older text) still says removing a child to nurse in a moving car is prohibited. The insert keeps "Never take a child out of a car seat in a moving car" as safe-driving advice; it is not stated as a statute.
- MCL 257.320a(1)(q) gives 1 point for "more than 1 but not more than 5 mph" over; the box and MI-095 say "1 to 5 mph". Left as is (common phrasing).
- MAN describes the pre-April 2025 child seat rules; the statute is used throughout.
