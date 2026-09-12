# Sarah & the Buds Project Dashboard

## Calendar consolidation — September 12, 2026

Review links: [Band PR #2](https://github.com/budr-githhub/sarahandthebuds/pull/2) → [Plan & Adapt draft PR #23](https://github.com/budr-githhub/planandadapt/pull/23). Release in this order.

Owner: Codex. Status: implemented locally, awaiting review and release. Band branch `feat/band-calendar` (base `1a17f24`); Plan & Adapt branch `feat/music-separation` (base `1601ae4`).

1. Handoff and current repositories reviewed — complete.
2. Band calendar implemented and locally tested — complete. Seven events preserved in `src/data/events.json`; optional performers remain unknown.
3. Release band calendar and verify `/shows` live — pending Bud review. The existing band homepage/domain already works; that alone does not prove the new calendar is deployed.
4. Plan & Adapt Music cleanup and old-calendar redirect prepared — complete locally, held behind step 3.
5. Release Plan & Adapt and verify the live redirect — pending step 3 and Bud review.
6. Record deployed commits and final smoke checks — pending release.

Validation: both Astro builds pass; browser checks at 390px and 1280px; calendar classification checked September 12, September 19 after the show, December 17 after all shows, and July 1 before all shows. Redirect tests cover both slash variants and query preservation; preview noindex remains. No new dependencies or DNS changes. Solo copy is a factual introduction/contact link; recordings have not been supplied.

## Verified hosting

Initial site released at `1a17f24` after GitHub reconnection. User screenshots show apex and www active with SSL; live HTTPS checks confirmed apex 200 and www 301 to apex, preserving path/query. Registrar remains IONOS, nameservers dax.ns.cloudflare.com and samara.ns.cloudflare.com. Mail records were preserved; email delivery is not tested.

## Documents

See [migration](migration.md), [hosting](domain-and-hosting.md), [copy deck](copy-deck.md), and [decisions](decision-log.md).
