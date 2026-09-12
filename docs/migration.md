# Band site separation

## Completed release — September 12, 2026

Owner: Codex; releases approved by Bud. Status: deployed and verified.

1. Repository/handoff review — complete.
2. Combined band calendar — complete; seven original events preserved in band `src/data/events.json`.
3. Band release — complete: [PR #2](https://github.com/budr-githhub/sarahandthebuds/pull/2), commit `c5577d2f48be025863ef3ec835dece2c9c2022ab`; Cloudflare success, live calendar checked at 16:45 UTC.
4. Plan & Adapt Music cleanup — complete: band introduction/photo, Midway Music Melodeon artwork/WRFL link, and solo introduction/contact link.
5. Plan & Adapt release — complete: [PR #23](https://github.com/budr-githhub/planandadapt/pull/23), commit `b606ba5678d07b4c5ed8352a547b1d93db23ef2f`; Cloudflare success, live Music page and redirects checked at 16:47 UTC.
6. Documentation — reconciled with the released implementation. These are the functional release commits; subsequent documentation commits do not change website behavior.

Both `/music/events` and `/music/events/` on Plan & Adapt return 301 to `https://sarahandthebuds.com/shows`, preserving query strings. The band calendar has no backlink to the old calendar, so there is no redirect loop. Both www band URLs and apex use valid HTTPS; www redirects to apex with path/query preserved.

Validation: both builds passed; layouts checked at 390px/1280px; calendar tested before, during and after the event schedule; original event data compared exactly; JSON-LD and seasonal Eastern offsets checked. Production contents and redirects verified after deployment.

Remaining optional content: solo listening links and specific band video embeds. Performer fields remain unknown where not supplied; do not guess them. Existing domain email records were preserved, but email delivery was not tested.

## Ownership and maintenance

Band/duo detail, repertoire, originals, gallery, social and booking links live in this repository. Plan & Adapt retains a brief band feature, radio and solo work. The copied band photos are independently stored here; original assets in Plan & Adapt were not deleted by the cleanup.

The one combined calendar renders at `/shows` from `src/data/events.json`. It includes band, duo and solo dates. Dates use YYYY-MM-DD; times use HH:MM in America/New_York. Unknown optional fields stay omitted, including performer information in JSON-LD. This supersedes the initial requirement to classify performers before moving the calendar. No sync workflow is needed.

The initial band `/shows` linked to Plan & Adapt. That link was removed before Plan & Adapt's redirect shipped. Plan & Adapt keeps `/music` and useful `#band-and-duo` and `#on-the-radio` anchors; detailed band sections are on the band site. Further image/CSS cleanup requires reference checks.

See [hosting](domain-and-hosting.md) for configuration, [copy deck](copy-deck.md) for visible language, and [decision log](decision-log.md) for dated choices.
