# Sarah & the Buds Project Dashboard

## Style guide application

Owner: Codex. Branch: `feat/brand-style-guide`. Status: merged in PR #4 (`4276d44`). Bud supplied visual identity v1.0; its original and text transcription are stored in this repository. The site now uses the guide’s monochrome palette, sans-serif typography, original S&B logo and uppercase AM/PM. Event data is unchanged.

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

## Photo additions — September 12, 2026

Owner: Codex. Branch: `feat/approved-photo-gallery`. Status: prepared for review; not deployed. Seven approved additions preserve the existing hero and six gallery photos. Photo 10 replaces photo 11 in the selection. See [photo inventory](photo-inventory.md). Release awaits Bud’s preview approval.

Validation: `pnpm --config.verify-deps-before-run=false run build` passed. This disables pnpm's dependency freshness preflight for the shared local dependency directory; it runs the normal Astro build. Chromium checks at 390px and 1280px found no horizontal overflow or broken images; counts verified two new introduction portraits, five new gallery photos and six existing gallery photos. Desktop screenshot reviewed. No production deployment performed.

PR #5 revision: captions removed; band-only AI-edited barn portrait used as hero, with Bud’s likeness review pending. Former hero moved to gallery. No release performed.

Revised validation: Astro build and git diff --check passed; Chromium at 390px/1280px reported no broken images or overflow, with two introduction photos, five added gallery photos and seven preserved gallery images including the former hero. No visible figcaptions remain.

## Symmetric portraits and continuous gallery — 2026-09-12

Bud requested matching band/duo image dimensions and removal of empty gallery spaces. Photo 10 now pairs with the duo in matching 4:5 frames, retaining all four band members. The original barn portrait moves into the gallery. All 12 gallery photos flow in responsive columns (three desktop, two tablet, one phone) at natural aspect ratios, eliminating separate grids and tall-row gaps. No captions; hero unchanged. Supersedes earlier placement notes.

Latest validation: build and diff checks passed. Chromium at 390/768/1280px confirms 12 gallery images, no broken images or horizontal overflow, and equal portrait dimensions at every size. Desktop portrait and gallery screenshots visually reviewed.
