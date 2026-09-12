# Domain & Hosting Notes

Last verified: September 12, 2026. Functional release: `c5577d2f48be025863ef3ec835dece2c9c2022ab` ([PR #2](https://github.com/budr-githhub/sarahandthebuds/pull/2)).

## Current configuration

| Item | Verified state |
|---|---|
| Registrar | IONOS |
| Host / project | Cloudflare Pages / sarahandthebuds |
| Repository / production branch | budr-githhub/sarahandthebuds / main |
| Source / output | Repository root / dist |
| Build command | pnpm build |
| Runtime requirement | Node >=22.12.0; actual successful build runtime versions not retained |
| Public domain | https://sarahandthebuds.com |
| www | Active with SSL; permanent redirect to apex |
| Pages hostname | sarahandthebuds.pages.dev |
| Nameservers | dax.ns.cloudflare.com; samara.ns.cloudflare.com |
| Apex and www DNS | Proxied CNAME to sarahandthebuds.pages.dev |
| Booking email | booksarahandbud@gmail.com |

Git integration is connected. Merges to main trigger production builds, including documentation-only changes. PR branches create previews. Do not recreate this project or repeat the original nameserver cutover.

## Routing and indexing

The active Single Redirect rule is named “Redirect www to main band site”. It matches `https://www.sarahandthebuds.com/*`, targets `https://sarahandthebuds.com/${1}`, returns 301 and preserves query strings. This was implemented as a Single Redirect, not the earlier proposed Bulk Redirect. HTTP www first upgrades to HTTPS. Both custom domains are associated with the Pages project and show active SSL.

Static `public/_headers` applies `X-Robots-Tag: noindex, nofollow` to pages.dev. The production domain does not receive that header. Canonical URLs, robots and sitemap use the band domain. No Pages Functions are used by the band site.

## Preserved IONOS service records

| Type/name | Target/value | Proxy |
|---|---|---|
| CNAME autodiscover | adsredir.ionos.info | DNS only |
| CNAME _dmarc | dmarc.ionos.com | DNS only |
| CNAME _domainconnect | _domainconnect.ionos.com | DNS only |
| MX @, priority 10 | mx00.ionos.com | DNS only |
| MX @, priority 10 | mx01.ionos.com | DNS only |
| TXT @ | v=spf1 include:_spf-us.ionos.com ~all | DNS only |

Email delivery has not been tested. This is a record of the supplied DNS screenshot, not a complete backup or instruction to replace current DNS.

## Setup history and verification

Initial attempts built README-only commit `4df54ae` and failed because pnpm was unavailable. The Cloudflare project also reported disconnected Git access. After access was restored, Bud approved trigger commit `1a17f24`; the initial site deployed successfully. PR #1 had merged at `3656ddf`.

IONOS nameservers were changed from ns1052.ui-dns.com, ns1053.ui-dns.org, ns1061.ui-dns.de and ns1103.ui-dns.biz to the assigned Cloudflare pair. Pages domain setup replaced the old apex/www A and AAAA website records. A temporary 522 was observed during setup; subsequent site loading and active SSL were verified.

PR #2 deployed the real calendar. Live `/shows` contained all seven event cards at 16:45 UTC, with no old-calendar backlink. The www `/shows?source=test` request returned 301 to the matching apex URL. Plan & Adapt PR #23 subsequently deployed its redirect at 16:47 UTC. See [dashboard](dashboard.md).

## Future releases and rollback

Use a reviewed branch/PR, run `pnpm build`, merge only with release authorization, and verify the Cloudflare check plus actual production content. Keep the deployed commit in the dashboard. For a bad release, restore a known-good Pages deployment and reconcile Git through a corrective PR. Restoring the old pre-calendar `/shows` after Plan & Adapt redirects are live would create a loop: coordinate that rollback across both sites. Do not modify Plan & Adapt DNS as part of band rollback.

No database or new hosting service was added. IONOS domain renewal remains separate. Recheck provider pricing before adding services.

## Current release — September 12, 2026

Bud approved publication. [PR #5](https://github.com/budr-githhub/sarahandthebuds/pull/5) merged as `b99f8f14fa54306b6f864a4cdce9365f35decd2f`; Cloudflare reported a successful production deployment. Fresh production responses verified the band-only hero and its image asset, full songbook with 146 cover/holiday entries, request-only originals, and corrected inline spacing. Earlier pending-release notes below are historical and superseded. Initial cached songbook requests returned 404 immediately after deployment; fresh requests succeeded.

Live pages: [Homepage](https://sarahandthebuds.com/) and [Songbook](https://sarahandthebuds.com/songbook).

