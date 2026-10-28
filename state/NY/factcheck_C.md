# New York fact check C (state upgrade since cb15098)

Scope: 5 new inserts (emergency_vehicles, headlight_use, police_stop, underage_alcohol, driver_record), the 23 rewritten inserts (meaning vs cb15098), newly quiz-flagged state questions, new questions NY-154 to NY-170 (bank compared by ID). Date: 2026-10-28.

## Verified (no change needed)

| Item | Source |
|---|---|
| Points from Feb 16, 2026: alcohol/drug 11, school bus 8, work zone speeding 8, due care 5; phone 5 unchanged; look-back 18 to 24 months | https://dmv.ny.gov/news/dmv-reminds-new-yorkers-of-updated-point-values-for-driving-violations |
| Full schedule (speeding 3/4/6/8/11, following too closely 4, signal/STOP/YIELD 3, under-16 restraint 3); 11 in 24 months; counted from violation date; PIRP 4 points; DRA 6 in 18 months | https://dmv.ny.gov/points-and-penalties/the-new-york-state-driver-point-system |
| ABC 65-c: up to $50, up to 30 hours community service, alcohol awareness program; not a conviction | https://www.nysenate.gov/legislation/laws/ABC/65-C |
| ABC 65-b(3)(a): a violation; first up to $100 and/or up to 30 hours | https://www.nysenate.gov/legislation/laws/ABC/65-B |
| Emergency vehicle: right edge, either edge of one-way roadway 3+ lanes, clear of intersection, stop until passed | https://www.nysenate.gov/legislation/laws/VAT/1144 ; MV-21 Ch. 5 (any direction, opposite lane, siren unseen) |
| Fire vehicle with lights: no closer than 200 ft | https://www.nysenate.gov/legislation/laws/VAT/1217 |
| Registration: photostatic copy allowed | https://www.nysenate.gov/legislation/laws/VAT/401 (4) |
| Failure to exhibit license: presumptive evidence of no license | https://www.nysenate.gov/legislation/laws/VAT/507 (2) |
| Headlights half hour after sunset to half hour before sunrise, under 1,000 ft, wipers; DRL do not qualify; insurance card shown after a crash | MV-21 (Drive 1ltO6DCUT3mMDRSa7gG2yLBbuOIvKKNkD) Ch. 10, Ch. 12 crash section |
| Rewritten inserts: meaning unchanged | diff vs cb15098 |
| All 33 quiz-flagged state questions (ch 2 to 13) are taught in their chapter's state box | out/NY/Permit_Path_New_York.md |

## Changes

| Where | Old | New | Reason |
|---|---|---|---|
| inserts underage_alcohol | "your license is suspended for 3 months. A repeat means 1 year or until you turn 21" | "the court can suspend it: 3 months the first time, 6 months the second, then 1 year or until you turn 21, whichever is longer" | ABC 65-b(6): first 3 months (court may), second 6 months, third or later 1 year or until 21. The repeat penalty was wrong. Also trimmed the first sentence to stay at 90 words. |
| NY-164 key | B (One year or until age 21) | D (Six months) | Wrong key: second violation is a 6-month suspension, 65-b(6)(b). exp and src updated. |
| NY-162 stem and option A | "What happens to the license the first time?"; A "Nothing; only a fine applies" | "What can the court do to the license the first time?"; A "Revoke it for life" | First-violation suspension is discretionary (65-b(6) "may"), so "only a fine" was also defensible. Key stays D. exp and src updated. |
| inserts driver_record | 96 words | 88 words | Over the 90-word limit; "Points count from the violation date for 24 months"; "takes up to 4 points off the suspension count". Same meaning. |
| inserts dui_penalties | 92 words | 90 words | Over limit; dropped two "for". Same meaning. |

## Open items
- None on facts. Build: NY QA and originality pass; the remaining "mocks print app_only" error (C08-008, C07-028, C08-026, C06-027) is the lead's item.
