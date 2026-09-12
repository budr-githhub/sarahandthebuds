# Sarah & the Buds Project Dashboard

Last checked: September 12, 2026. This is the changing status and coordination record; details belong in the linked documents.

## Project health

- Website: initial implementation built and tested locally; not verified live.
- Repository: [budr-githhub/sarahandthebuds](https://github.com/budr-githhub/sarahandthebuds), with initial work on `setup/band-site` in [PR #1](https://github.com/budr-githhub/sarahandthebuds/pull/1).
- Accepted source: `main`; PR #1 was open and unmerged when checked. Refresh GitHub before acting.
- Cloudflare project, assigned pages.dev address, domain connection and DNS: pending verification. No deployment or DNS change was performed in these preparation tasks.
- Existing Plan & Adapt website: unchanged by this work.

## Current task and handoff

- Owner: Codex. Next owner: Bud for review and Cloudflare setup; Claude review can be requested against PR #1.
- Status: ready for review; documentation included in the same initial PR.
- Initial base: `4df54aeaac5c455075eb5b6873a8fa5e443e50d6`.
- Site implementation reviewed locally: `5331553ecfc7ef6f9e3ecf219c278cbb978f73fe`. Documentation follow-up is in PR #1; use its current head SHA for a new review.
- Scope: independent Astro band site, referenced photos, songbook, booking/social links, interim Shows page, and shared documentation conventions.
- Acceptance: root-level build passes; links/images resolve; mobile/desktop have no horizontal overflow; clear Cloudflare instructions and agent handoff; original site remains intact.
- Validation already completed on the implementation: frozen-lockfile install; `pnpm build`; generated internal links and image alt text; Chrome at 390px and 1440px (no overflow or missing images); Shows page loads. Live headers, HTTPS and custom-domain routing remain untested.
- Documentation follow-up: relative document links and referenced paths checked; whitespace check passed. No runtime files changed; the implementation build and browser results above remain applicable.

## Next five tasks

1. Review and merge PR #1 after Bud's release decision.
2. Create the Cloudflare Pages project using [hosting instructions](domain-and-hosting.md), then record actual project URL and deployed commit.
3. Connect the IONOS domain through Cloudflare and verify HTTPS, www redirect, canonical URLs and preview noindex headers.
4. Confirm calendar performer assignments; migrate band/duo events without misclassifying solo performances.
5. Update Plan & Adapt's Music page in its own PR: band introduction/link, Midway Music Melodeon, and solo work. Confirm solo copy/listening links and specific videos before adding them.

## Open decisions

- Calendar act for each event; whether Plan & Adapt retains a solo calendar.
- Solo description/listening links, maintained in Plan & Adapt.
- Specific band videos to embed; channel link already exists.
- Final visual approval of the initial band presentation.

## Project documents

See [document index](README.md), [decisions](decision-log.md), [hosting](domain-and-hosting.md), [copy deck](copy-deck.md), [migration](migration.md), and [AI playbook](ai-playbook.md).
