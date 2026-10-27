# Sarah & the Buds — current status

Updated October 27, 2026. Owner: Bud. Implementation: Codex. Published and verified; no release approval is pending.

## Friends additions — published and verified, September 17, 2026

Owner: Codex. Branch: `codex/friends-additions`. Base: `57f45419d0260f05604dda02533c1f9a2950c16a`. Bud requested JJ Marrs and Georgetown Underground. Added Georgetown Underground under Venues using the established Georgetown location; JJ Marrs is listed under Musicians (category corrected at Bud’s request) without an invented biography, using the Facebook profile supplied by Bud (`https://www.facebook.com/jeremiah.marrs.7`). Spelling corrected to Marrs to match that profile URL. Bud supplied Georgetown Underground’s website (`https://www.georgetownunderground.com/`); Friends and the shared Shows venue record now use it. Cards now omit absent links/descriptions rather than render empty links. Source and copy deck match. Six-page build passed; Chrome at 320px verified both new entries, no empty links and no horizontal overflow. Published through PR #21 at `d78fda84cda23c1dbee9468638c4a26891a57eee`. Cloudflare succeeded; live Chrome verified both Friends links, both Georgetown Shows links, HTTP 200 and no mobile overflow.

## JJ category correction

Bud requested moving JJ Marrs to Musicians. Published via PR #23 at `0c7c65de79634480a9b60cd769995de14a7dfbd4`; build and rendered-section check passed. Cloudflare succeeded and live Chrome verified JJ under Musicians.

## Friends alphabetical order

Owner: Codex. Bud requested A–Z ordering within Musicians, Venues and Community friends, using displayed names. Data and copy deck reordered; preserve this ordering for future additions. Build and generated-page order checks passed. Published through PR #25 at `d8abae3476d4bb4aab78fa36939774c962c1a4a6`. Cloudflare succeeded; live Chrome verified A–Z order in all three groups.

## Published site

- Header on every page: About, Music, Shows, Press, Friends, Booking. Footer includes resource links.
- Homepage: owner-approved inward-facing microphone S&B logo; band-only AI-edited hero; matching 4:5 band/duo portraits; 12 gallery photos without captions.
- Songbook: 44 homepage artist rows in one disclosure; 146 cover/holiday selections with artist names on `/songbook/`; originals by request only. No specialty songs or named originals.
- Shows: one calendar source in `src/data/events.json`; ten dates with venue locations, available website/directions links and confirmed act labels: seven full-band shows, Midway Fall Festival solo with Bud as a wandering minstrel, the October 17 collaboration, The Lost Dogs on November 17 and Georgetown Underground’s December 16 Toys for Tots charity event. October 3 removed because it did not take place. Eastern time and automatic Upcoming/Past movement. Back to Music links at top and bottom target `/#songbook`.
- Press: approved band/duo introductions, copy buttons, four downloadable JPEGs, 16 logo/color variants in SVG/PNG/PDF, favicon assets and ZIPs. All four photos credited to Andrew Von Neida; Bud confirmed promotional-use permission.
- Friends: seven musicians, five venues, two community friends; each group is alphabetized by displayed name. Zoe Zamora’s Facebook URL supplied by Bud. Personal stories/photos are optional future additions.

## Completed releases

| Change | PR | Published implementation commit |
|---|---|---|
| Calendar | #2 | `c5577d2` |
| Autumn gigs and October 3 removal | #28 | `ff50dddd93eca681716ecd128977437ef1f6dba6` |
| Easter Egg Hunt | #29 | `ede9346f5bddc723b55bf6c6c9fa643aeb176473` |
| Style guide | #4 | `4276d44` |
| Photos and songbook | #5 | `b99f8f1` |
| Press, Friends, logo set, event details | #8 | `c0d795e` |
| Andrew Von Neida credits and permission | #10 | `85a2d1e` |
| Approved introductions | #12 | `185513b` |
| Back to Music links | #14 | `793a274` |
| Press/Friends header links | #16 | `328ace847ddbf96b19c3efc198f9c21bef213ff1` |
| Friends additions and Georgetown website | #21 | `d78fda8` |
| JJ Marrs moved to Musicians | #23 | `0c7c65d` |
| Friends A–Z within each group | #25 | `d8abae3` |
| Confirmed full-band and Midway solo lineups | #19 | `3a3b00b07f16effd03924a7c99e51a2920c0955b` |

Repository: [GitHub](https://github.com/budr-githhub/sarahandthebuds). Subsequent documentation-only commits do not change page behavior. Plan & Adapt separation is complete in its PR #23 (`b606ba5`); legacy calendars redirect to band Shows. No second calendar or sync workflow exists.

## Still needed

- **Sarah:** select featured performance video(s). This is the only Press “Coming soon” item.
- **Bud (optional):** precise festival stage/porch if useful. All current event acts are confirmed.
- Optional: Friends descriptions/photos/logos, preferred Willcutt display name, technical rider. See [owner checklist](press-friends-brand.md).

Photo permission and introductions are complete, not pending.

## Verification and maintenance

Six-page production build passed. Responsive checks at 390/1280px covered header, pages and downloads; photo layout also checked at 768px. Clipboard, ZIP integrity, preserved event fields and calendar rollover passed. Cloudflare checks and live Chrome verified released changes, including six full-band labels, one solo label and the Midway wandering-minstrel note. Plain automated text requests sometimes return 403; Chrome requests succeeded. Email delivery was not tested. No DNS changes are needed.

Keep docs aligned after every push. Current records: [copy deck](copy-deck.md), [press/brand inventory](press-friends-brand.md), [approved introductions](approved-introductions.md), [photos](photo-inventory.md), [songbook](songbook-source.md), [style](style-guide.md), [hosting](domain-and-hosting.md). Historical decisions remain in [decision log](decision-log.md).

## October calendar update

Owner: Codex. Branch: `fix/autumn-gigs`. Base: `067a7a9`. Add October 17 collaboration (2–5 PM), November 17 Lost Dogs John Prine tribute/Wolf Run benefit (6–8 PM), December 12 full-band Christmas Balloon Glow (4–7 PM), all at Wildside Winery. Remove October 3 entirely. Preserve other events, venue links and Eastern-time rollover. Published in PR #28 (`ff50ddd`) and PR #29 (`ede9346`). Six-page build passed; Cloudflare succeeded. Live Chrome verified all ten cards, four additions, October 3 removal and no horizontal overflow at 390px.

Easter Egg Hunt: Sunday, March 21, 2027, 2–5 PM Eastern at Wildside Winery, 5500 Troy Pike, Versailles, KY 40383. Sarah & the Buds — full band. Added from Bud’s October 10 follow-up; year inferred from the next March 21 falling on Sunday.

## Pages CMS trial — published, awaiting owner setup

Owner: Codex. Branch `feat/pages-cms-trial`, base `e194b60`. Scope: Shows and six existing Venues, footer Manage shows link, draft/cancelled support, validation and read-only calendar reports. Existing ten public shows retained. Six-page build, three validator tests, rendered draft/cancellation checks and configuration field coverage passed. CMS authentication/authorization and first saved edit remain untested pending Bud’s setup. Instructions: [editing shows](editing-shows.md). Current calendar content is linked from [calendar source and reports](calendar-inventory.md); previous dated release counts are historical.

Automatic main-branch documentation commits were not enabled: approval review rejected persistent workflow write access. The workflow only validates and uploads a report; it has no repository write permission.

PR #31 (`ce9bc6967e5730b4f7b3098c9be7b07243e70d19`) deployed October 10. Live browser verified all ten real show cards and the Manage shows footer link. Read-only report workflow run `38090448305` succeeded. Pages CMS sign-in is open; terms acceptance, GitHub app authorization and first save remain with Bud.

## Songbook artists and request proposal — October 16

Owner: Codex. Branch: `feat/songbook-artists`. Artist names added to all 146 cover/holiday selections; homepage remains compact. Private master used for metadata only. Source, copy deck and songbook documentation updated together. Six-page build passed; browser verified all 146 artist labels, three back-to-top links and no horizontal overflow at 319px. All existing titles and homepage samples are unchanged. Published through PR #33 at `e97df7b84b39abe05a93918b1e623e160c85f2ed`; live browser verified all 146 artist labels and no horizontal overflow on October 16, 2026. [Request and Venmo plan](song-requests-plan.md) is proposed only; no new payment or notification service is enabled. Bud needs to confirm the Venmo profile, notification inbox and optional-tip policy before integration.


## October 27 calendar check

The live Shows page was reviewed on October 27. October 17 and October 23 correctly appear under Past; October 23 is the most recent completed show. Upcoming dates are November 17, December 12, December 16 and March 21, 2027. Bud’s recent project context identifies the December 16 Georgetown Underground show as a Toys for Tots charity event. Added that confirmed event note to the calendar source; the date, time, venue and band lineup were already present. No other upcoming dates were confirmed in the available project notes. Calendar release verification is recorded in the hosting notes after deployment.
