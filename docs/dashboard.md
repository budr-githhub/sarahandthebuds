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

## Expanded collapsible songbook — 2026-09-12

Bud requested more songs from artists with multiple entries. Expanded to 70 songs / 44 artists using the August master song list. Whole-songbook and multi-song artist disclosures use native details/summary without JavaScript. See [source inventory](songbook-source.md). Prepared in PR #5; not released.

Songbook validation: build and diff checks passed. Chromium at 390px and 1280px confirmed initially collapsed state, Enter to open the songbook, Space to expand the Beatles' seven titles, click to collapse, and no horizontal overflow.

## Full songbook reference and compact rows — 2026-09-12

Bud requested no artist disclosures, compact multi-song rows inside the overall collapsible songbook, a full reference page and section back-to-top links. `/songbook` now lists 184 deduplicated entries from the August master TOC: 137 covers, 41 originals, five holiday entries and one specialty song. Covers are title-only because the source does not consistently identify artists. The future-suggestions section is excluded. `src/data/songbook.json` holds metadata only. Homepage links to the full reference; both pages have section return links. This supersedes nested artist disclosures. Release pending in PR #5.

Validation: four-page Astro build and diff checks passed. Browser checks at 390/1280px verify the overall disclosure opens with Enter, no nested disclosures remain, all 184 reference entries render, all reference anchors resolve, seven homepage back links exist, back-to-top navigation works, and neither page overflows horizontally.

## Artist examples and owner additions — 2026-09-12

Bud requested exactly one homepage row per artist: roughly two examples, with a third for short titles and natural wrapping. Added owner-supplied With or Without You, One and Acrobat (U2); Into the Mystic (Van Morrison); Falling Slowly and Song of Good Hope (Glen Hansard & Markéta Irglová). Newly requested examples are prioritized. The full reference now contains 189 unique entries (Into the Mystic was already present); these additions are authorized by Bud beyond the August document. A second full-list link follows the collapsible section. Supersedes earlier row/count notes; release pending in PR #5.

Latest verification: build and diff checks pass. At 390/1280px, browser checks confirm exactly 44 artist rows, two full-list links, 189 reference entries, working back-to-top anchors and no horizontal overflow.

## Original songs by request — 2026-09-12

Bud requested removal of the specialty section and no named originals yet. Both public pages now say “Original songs available by request” with a contact link. Removed original/specialty arrays from public songbook metadata and removed Merry Mary from the holiday listing and homepage copy. The source document remains unchanged. The reference displays 146 covers/seasonal entries (142 covers, four holiday selections), plus the request-only originals section. This supersedes earlier public counts and original-title lists. PR #5 remains pending release.
