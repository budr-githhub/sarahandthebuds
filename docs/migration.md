# Band site separation — September 12, 2026

## Calendar consolidation — September 12, 2026

Owner: Codex. Status: implemented locally, awaiting review and release. Band branch `feat/band-calendar` (base `1a17f24`); Plan & Adapt branch `feat/music-separation` (base `1601ae4`).

1. Handoff and current repositories reviewed — complete.
2. Band calendar implemented and locally tested — complete. Seven events preserved in `src/data/events.json`; optional performers remain unknown.
3. Release band calendar and verify `/shows` live — pending Bud review. The existing band homepage/domain already works; that alone does not prove the new calendar is deployed.
4. Plan & Adapt Music cleanup and old-calendar redirect prepared — complete locally, held behind step 3.
5. Release Plan & Adapt and verify the live redirect — pending step 3 and Bud review.
6. Record deployed commits and final smoke checks — pending release.

Validation: both Astro builds pass; browser checks at 390px and 1280px; calendar classification checked September 12, September 19 after the show, December 17 after all shows, and July 1 before all shows. Redirect tests cover both slash variants and query preservation; preview noindex remains. No new dependencies or DNS changes. Solo copy is a factual introduction/contact link; recordings have not been supplied.

The setup notes below preserve the initial preparation history. Their pending deployment/domain statements are superseded by the current dashboard.


Status at initial preparation: implementation for review; no deployment or DNS changes performed. See [dashboard](dashboard.md) for current status and [hosting notes](domain-and-hosting.md) for the release procedure.

## Source and scope

Adapted from budr-githhub/planandadapt: site/src/pages/music.astro and the referenced band photos. Original repository and history remain intact. Band, acoustic duo, repertoire, originals, gallery, social and booking links move here. Only referenced images are copied. The starter README is replaced with project-specific maintenance and deployment instructions.

## Plan & Adapt follow-up

Keep /music as a three-section page: Sarah & the Buds (short intro/photo/link), Midway Music Melodeon (existing radio art and WRFL link), and Bud’s solo work. Confirm solo description and listening links with Bud; do not invent recordings or reclassify the band's originals as solo recordings.

The current /music/events page says it covers band, duo and solo shows, but its entries lack performer assignments. This initial site links to that calendar. Before migrating event data, confirm each show's act, migrate only band/duo entries, and decide whether the original page stays as a solo calendar. Do not redirect a mixed calendar wholesale or create a circular redirect to /shows while /shows links back to it.

Keep Plan & Adapt’s /music URL accessible. Old fragment links cannot be redirected separately by the server; preserve useful anchors when rewriting that page. Update band references elsewhere and retire unused photos only after checking all references.

## Release sequence

Review/build this repository → merge the initial PR → configure Cloudflare Pages → verify pages.dev → connect domain and verify HTTPS → update Plan & Adapt in its own PR. Test mobile navigation, photos, booking, canonical URLs, sitemap, preview noindex headers and both domain variants. The existing sites and DNS are untouched by this PR.

## Pending content

- Performer assignments for calendar entries.
- Specific video URLs if embeds are desired (existing YouTube channel link is retained).
- Bud’s solo-work description and listening links for Plan & Adapt.
