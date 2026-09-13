# Sarah & the Buds — current status

Updated September 13, 2026. Owner: Bud; implementation: Codex. Existing site is published and verified. New Press/Friends/logo/events work is prepared for review on `feat/press-friends-brand`, not merged or published.

## Current work

See [implementation and owner checklist](press-friends-brand.md). Scope: Press & Booking downloads, complete traced logo set and favicon, owner-specified portrait home logo, Friends directory, and event locations/links/act labels. Base: `243db66`. Implementation: `2b0ec1a`; pushed in draft [PR #8](https://github.com/budr-githhub/sarahandthebuds/pull/8). Documentation is on the review branch, not main. Bud supplied Zoe Zamora’s Facebook link. All seven event act assignments remain unknown. Photo credits, usage, promotional copy, featured video and release review are pending.

Validation: six-page Astro build passed. Phone (390px) and desktop (1280px) browser checks passed for overflow, loaded images and internal downloads; copy buttons and calendar rollover passed. Both ZIP integrity checks passed, and all seven original event records retain their dates/times/names. No DNS or hosting changes.

## Releases

- Calendar: band PR #2, `c5577d2`; combined seven-event calendar in `src/data/events.json`.
- Plan & Adapt separation: PR #23, `b606ba5`; `/music` contains band, radio and solo introductions. Both old calendar URL forms redirect to band `/shows`, preserving query strings.
- Style guide: band PR #4, `4276d44`; supplied monochrome identity and original logo artwork.
- Photos and songbook: band [PR #5](https://github.com/budr-githhub/sarahandthebuds/pull/5), `b99f8f14fa54306b6f864a4cdce9365f35decd2f`; approved by Bud, merged and Cloudflare production succeeded.
- Release documentation: band PR #6, `a5756ba`; merged. Subsequent documentation changes do not change page behavior.

## Live behavior

- New band-only AI-edited barn hero, approved as part of release. Former hero retained in gallery.
- Photo 10 and the duo portrait share 4:5 frames. Twelve gallery photos flow in responsive columns; no visible captions. Alt text remains.
- Homepage: one collapsible songbook, one row per artist (44 artists), approximately two examples or three short titles. Natural wrapping. Full-list links above and below.
- `/songbook`: 146 named selections (142 covers, four holiday entries). Original songs available by request only. No named originals or specialty section.
- Explicit owner additions: U2 — With or Without You, One, Acrobat; Van Morrison — Into the Mystic; Glen Hansard & Markéta Irglová — Falling Slowly, Song of Good Hope.
- Each homepage and songbook section has Back to top links. Inline link spacing is fixed.

## Verification

Four-page Astro build and diff checks passed before release. Browser checks at 390/768/1280px covered photo layout; 390/1280px covered disclosures, links, counts and overflow. Live fresh responses verified hero asset, reference page, request-only originals and inline spacing after Cloudflare success. Initial cached requests briefly returned 404 during propagation.

## Remaining optional work

Specific band video embeds and Plan & Adapt solo listening links remain optional, not handoff blockers. Do not invent performer assignments, songs, dates or biographies. No DNS/email changes are needed; email delivery was not tested.

Read [Claude handoff](claude-handoff.md), [style guide](style-guide.md), [photo inventory](photo-inventory.md), [songbook source](songbook-source.md), [copy deck](copy-deck.md) and [hosting](domain-and-hosting.md). Decision-log entries preserve historical changes; this dashboard is current status.
