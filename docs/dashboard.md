# Sarah & the Buds — current status

Updated September 13, 2026. Owner: Bud; implementation: Codex. Status: published and verified.

## Latest release

[PR #8](https://github.com/budr-githhub/sarahandthebuds/pull/8) merged as `c0d795eaad3179b22715b964b803e445bcb7b6c3`. Cloudflare production succeeded. Chrome verified HTTP 200 on homepage, Press, Friends and Shows; Press/Friends display “Coming soon” without internal preview notes.

Live additions: Press & Booking with photo/logo downloads and ZIPs; 16 logo/color variants and favicon; inward-facing microphone homepage logo; Friends directory with all 12 requested entries; event locations, venue links and unknown act labels. Original dates/times remain unchanged.

Bud authorized publication with “Coming soon” descriptions, photo credits/usage guidance, featured videos and Friends stories/photos. Andrew Von Neida is confirmed as photographer for all four press photos, with promotional-use permission confirmed by Bud. The credit/permission update is published in [PR #10](https://github.com/budr-githhub/sarahandthebuds/pull/10), merge `85a2d1e7028a67097d19a885eb1e9e7ad414820a`. Cloudflare succeeded; live Chrome verification found all four credits and permission guidance. Sarah will select the featured video; [Introductions](press-introduction-drafts.md) approved by Bud and applied to the page and ZIPs; published in PR #12 (`185513b639d9c4c7b594c04f58c71f1e6ad56d71`), Cloudflare succeeded and live Chrome verification passed. All seven event act assignments remain unconfirmed. See [remaining-input checklist](press-friends-brand.md). No release approval remains pending.

Validation: six-page build, previous 390/1280px browser/download/copy/calendar checks, and production Chrome verification. Plain automated text requests returned 403; browser requests succeeded. No DNS changes or email delivery tests.

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


## Shows navigation

Owner-requested “Back to Music” links are published at the top and bottom of `/shows`, targeting `/#songbook` consistently with the existing Music navigation. Released in PR #14 (`793a274fa341026a949dc2d1739d5e17321ddd2b`). Live Chrome verification found both links and confirmed navigation to the existing songbook section.


## Header navigation

Press and Friends added beside About, Music, Shows and Booking in the shared header. Published in PR #16 (`328ace847ddbf96b19c3efc198f9c21bef213ff1`). Cloudflare succeeded; live Chrome verification confirmed About, Music, Shows, Press, Friends and Booking.
