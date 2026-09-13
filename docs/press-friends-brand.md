# Press, Friends, branding and event details

September 13, 2026. Owner: Bud. Implementation: Codex. Published through [PR #8](https://github.com/budr-githhub/sarahandthebuds/pull/8), merge `c0d795eaad3179b22715b964b803e445bcb7b6c3`. Cloudflare production succeeded; live homepage, Press, Friends and Shows verified in Chrome. Bud approved publication with Coming soon notices and will ask Sarah to help complete remaining material.

## Published

- `/press/`: separate full-band and duo introductions, copy buttons, four individual JPEG downloads, 16 logo/color previews with SVG/PNG/PDF downloads, complete logo and press ZIPs, booking contacts, social/video links and section return links.
- `/friends/`: musicians, venues, community friends in Bud’s requested order. Text-first cards; no invented endorsements or borrowed logos. Zoe’s Facebook URL was supplied by Bud.
- Homepage: portrait S&B with microphones aligned to the lettering’s vertical center, round heads inward, no act name inside the logo. Existing page heading remains separate. Photography and songbook retained.
- Events: reusable venue directory; location, venue link where verified, directions where address is known, and act labels. All seven `act` values are null pending Bud. Original dates/times/names preserved. Existing optional event URLs and performer text remain supported. Eastern time and client-side Upcoming/Past movement remain.
- Footer resource links; sitemap includes both new pages; compact S&B favicon and Apple icon.

## Logo production

Source: `public/images/brand/sb-mark.png`, extracted from Bud’s supplied style guide. No original vector exists. `scripts/build-logo-set.py` traces the white silhouettes into vector polygon paths, preserving S&B rather than substituting a font. Isolated scan specks are discarded. Edge irregularities in the raster remain in the tracing; these are reconstructed production assets, not original designer masters.

Shared primary, portrait and compact marks; full-band and acoustic-duo horizontal and stacked arrangements; black and warm-white transparent versions; dark/light social avatars. 16 SVGs, 16 PNGs and 16 PDFs. The portrait master is 1000 × 1250; its homepage frame crops only empty canvas. PDF output preserves vector shapes and act-name text; no font files are distributed. Favicon: SVG, 16/32 PNG, ICO, Apple 180 PNG.

Regenerate SVGs with Python + Pillow + NumPy using `python3 scripts/build-logo-set.py`. Export PNG/PDF with `node scripts/export-logo-set.cjs` (local Playwright/Chrome; `PLAYWRIGHT_MODULE` can point to the installed module). Regenerate icon PNGs from `public/favicon.svg`, then ICO from the 32px PNG. Package checked-in exports with `python3 scripts/build-press-kit.py`. No runtime dependency was added.

## Photo inventory

Four existing prepared JPEGs copied to `public/downloads/photos/`; source metadata is in `src/data/press-photos.json`. Web previews reuse existing WebP files.

- Full band: barn portrait; Georgetown Underground portrait (photo 10, not 11); wine-barrel-room performance.
- Duo: guitar-and-microphone portrait.
- AI-edited homepage hero is excluded from the press kit.
- ZIP has separate full-band/acoustic-duo folders, logos, icons, promotional copy and a read-me. All four photographs are by Andrew Von Neida; Bud confirmed promotional-use permission. The page and ZIP read-me carry attribution and permission guidance.

## Bud’s remaining inputs

- [ ] Confirm full-band / duo / solo for Aug 1, Aug 22, Sep 19, Sep 20, Oct 3, Oct 23 and Dec 16, 2026. If solo, confirm Bud Ratliff is the appropriate public performer name.
- [ ] Confirm exact stage/porch for Kenwick Porch Fest and Midway Fall Festival if useful. General festival locations are used until then.
- [ ] Supply Georgetown Underground’s preferred official website/social link; address has documentary support but no official artist-facing URL was confidently identified.
- [x] Bud approved both introductions; applied to `src/data/press.json` and regenerated downloads.
- [x] All four photographs: Andrew Von Neida. Promotional-use permission confirmed by Bud.
- [ ] Sarah will select the featured performance video; optional technical rider can follow later.
- [ ] Confirm “Willcutt Guitars” (official website branding) is the intended display name for “Willcutt Music.”
- [ ] Optional: personal connection descriptions and permissioned Friends photos/logos. Current short factual descriptions are sufficient if preferred.
- [x] Bud approved release with Coming soon notices September 13. Further logo refinements can follow.

Bud approved the existing materials for publication with “Coming soon” notices replacing internal review notes. Expanded descriptions and Friends stories/photos will follow; Sarah will select the video. Photo credits and promotional-use permission are confirmed. Update the ZIP read-me alongside these additions.

## Verified link sources (September 13)

Musicians:
- [Bryce Ernest Taylor](https://www.brycetaylormusic.com/): official site and biography.
- [Jason Kyle Smith](https://jasonkylesmith.bandcamp.com/): artist Bandcamp, Georgetown KY.
- [Mo Bell](https://mobellmusic.com/home): official music site.
- [Mela B](https://melabmusic.com/): official singer-songwriter site.
- [Zoe Zamora](https://www.facebook.com/ZoeZamoraMusic/about): exact link supplied by Bud; Facebook fetch unavailable, so owner-confirmed rather than independently fetched.
- [Reb Butler](https://music.apple.com/us/artist/reb-butler/1422069885): artist music catalog. Local activity corroborated by [Wildside’s event page](https://www.wildsidewinery.com/event-details/open-mic-night-at-wildside-wine-bar-2026-11-18-19-00). Preferred social profile may replace the music link later.

Venues and community:
- [Wildside Winery](https://www.wildsidewinery.com/): 5500 Troy Pike, Versailles KY 40383.
- [Ghost Fox Winery](https://ghostfoxwinery.com/): 2385 Chrisman Mill Road, Nicholasville KY 40356.
- [Equus Run Vineyards](https://www.equusrunvineyards.com/).
- [Kenwick Table](https://www.kenwicktable.com/).
- [WRFL 88.1 FM](https://wrfl.fm/).
- [Willcutt Guitars](https://willcuttguitars.com/).
- [Shaker Village contact](https://shakervillageky.org/contact-us/): 3501 Lexington Road, Harrodsburg KY 40330.
- [Midway Fall Festival](https://www.midwayfallfestival.com/): Downtown Midway. Festival schedule does not replace the band’s set time.
- [Kenwick Porch Fest FAQ](https://www.kenwickporchfest.com/faqs): Kenwick neighborhood, Lexington.
- Georgetown Underground: [city tourism shopping guide](https://georgetownky.com/images/PDF/NEW%20Downtown%20Shopping%20Guide%202025%20111725.pdf) and [published business notice](https://kypublicnotice.com/KYLegals/2025/70151-2025-12-05_1001.pdf), 152 E Main Street, Georgetown KY 40324.

Research informing the press framework: [Merle Marlow Band](https://merlemarlowband.com/presskit/), [Dusky Waters](https://www.duskywaters.com/epk), [Southbound](https://www.southbound-band.co.uk/press-kit.html). Adapted the straightforward combination of introductions, direct media downloads and booking contact to this Astro site.

## Maintenance

Edit event dates/times and `act` in `src/data/events.json`. Valid acts: `full-band`, `duo`, `solo`, or null. Reused venue facts belong in `src/data/venues.json`; keep a source URL and verify before changing them. `url` on an event is for event-specific details. Never infer an act from a venue or date. Build and review both Upcoming and Past, including mobile, before pushing. Keep the band repository as the calendar source.

Press text: `src/data/press.json`; photo download metadata: `press-photos.json`; Friends: `friends.json`. Update packages and documentation together. After every push, verify GitHub docs reflect that exact branch/release state. Merging main triggers Cloudflare; no merge/deploy occurs before release approval.

## Validation

Six-page production build passed. Browser checks at 390 and 1280px: no horizontal overflow or failed images, logo frames contain artwork, internal download links return successfully. Copy-to-clipboard verified. Advancing the browser clock to October 24 moves completed shows to Past and leaves December 16 upcoming. Seven event dates/times/names match base exactly. Both ZIPs pass integrity checks (59 press files, 54 logo files). External Facebook fetch unavailable; Zoe URL is owner-provided. No email delivery tested. Production Cloudflare success and Chrome page content verified after release.


September 13 photo-credit release: PR #10 merged as `85a2d1e7028a67097d19a885eb1e9e7ad414820a`; Cloudflare succeeded. Live `/press/` returned 200 in Chrome with four Andrew Von Neida credits and promotional-use guidance, without the old credit placeholder. Introduction drafts remain for review; Sarah will select video.
