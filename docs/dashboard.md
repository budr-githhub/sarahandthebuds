# Sarah & the Buds Project Dashboard

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

See [hosting](domain-and-hosting.md), [migration](migration.md), [copy deck](copy-deck.md), and [decisions](decision-log.md).
