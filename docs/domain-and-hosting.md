# Domain & Hosting Notes

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


Last checked: September 12, 2026. This document owns detailed configuration and verification. Planned values are not proof of a completed setup.

## Current state

| Item | State |
|---|---|
| Registrar | IONOS, reported by Bud |
| Domain | sarahandthebuds.com |
| GitHub repository | budr-githhub/sarahandthebuds |
| Initial PR | #1; open at last check |
| Host | Cloudflare Pages, planned |
| Pages project / assigned URL | Not yet verified |
| Deployed commit | Not yet verified |
| Cloudflare nameservers | Record values assigned to this domain during setup |
| DNS / HTTPS / www redirect | Not yet verified |
| Domain email | Unknown; preserve any existing records |
| Booking | Existing booksarahandbud@gmail.com mailto link |

## 1. Merge the initial site

Review [PR #1](https://github.com/budr-githhub/sarahandthebuds/pull/1), including documentation, then merge when Bud approves. At the last check, `main` contained only the starter README. Creating a production deployment from it before the merge will not build this site. Refresh PR state before acting.

## 2. Create Cloudflare Pages

1. Sign into the Cloudflare account used for Plan & Adapt.
2. Open Workers & Pages → Create application → Pages → Import an existing Git repository.
3. Connect GitHub and select `budr-githhub/sarahandthebuds`. If missing, grant the Cloudflare GitHub integration access to this new private repository and retry.
4. Enter the settings below. Source is at repository root, unlike Plan & Adapt's `site/` folder.

| Setting | Value |
|---|---|
| Project name | sarahandthebuds, if available; record actual name |
| Production branch | main |
| Framework preset | Astro |
| Root directory | Leave blank |
| Build command | pnpm build |
| Build output directory | dist |
| NODE_VERSION | 22 (must resolve to 22.12 or newer) |

Use the current Pages build image. The repository includes a pnpm lockfile. Record Node/pnpm versions from the successful build log; the initial local build used pnpm 11.9.0. If installation fails, inspect the actual error rather than changing dependencies or the lockfile blindly. Cloudflare supports a `PNPM_VERSION` override if needed.

5. Select Save and Deploy. Wait for success and open the URL Cloudflare actually assigns.
6. Check homepage, photos, navigation, booking address and Shows page on phone and desktop. Verify the deployment points to the merged commit.

## 3. Connect the domain

1. Add `sarahandthebuds.com` as a domain/zone in the same Cloudflare account and choose Free.
2. Review imported DNS records. Save the original IONOS nameservers and DNS records before changing them. Preserve any email records; do not copy Plan & Adapt's Workspace records into this unrelated domain.
3. Copy the two nameservers assigned specifically to sarahandthebuds.com. Do not assume Plan & Adapt's pair applies.
4. In IONOS, select this domain → Actions/gear → Name Server → Use Custom Name Servers. Enter the two assigned values and save.
5. Wait for Cloudflare to show the zone as active; nameserver changes can take up to 48 hours globally.
6. Open the band's Pages project → Custom domains → Set up a domain. Add `sarahandthebuds.com`, then `www.sarahandthebuds.com`, completing the provided DNS setup. Add domains in Pages, not just as standalone CNAME records.
7. Wait for domain activation and valid HTTPS certificates.

If IONOS shows existing DNSSEC enabled, follow Cloudflare's nameserver migration guidance before cutover so an old DS record does not invalidate the new DNS service.

## 4. Make www redirect to the main address

After both hostnames work, use Cloudflare Bulk Redirects to create a list entry with source `www.sarahandthebuds.com`, target `https://sarahandthebuds.com`, and status 301. Enable Preserve query string, Subpath matching and Preserve path suffix. Create/enable a bulk redirect rule using that list. Keep the www record proxied; if Pages has already configured it, do not add a conflicting A record.

Verify that `https://www.sarahandthebuds.com/shows?source=test` redirects to `https://sarahandthebuds.com/shows?source=test`. The intended canonical address is the non-www domain.

## 5. Verify and record

- [ ] Cloudflare build succeeded; record deployment URL, commit, time, Node and pnpm versions.
- [ ] Apex and www HTTPS certificates valid; www redirects with path/query preserved.
- [ ] `/`, `/shows`, and a missing page render appropriately (missing page returns 404).
- [ ] Photos and booking/social/calendar links work on phone and desktop.
- [ ] Canonical and social URLs use sarahandthebuds.com.
- [ ] `/sitemap.xml` and `/robots.txt` use the band domain.
- [ ] pages.dev responses have `X-Robots-Tag: noindex, nofollow`; custom domain does not. The rules are static `public/_headers`, not middleware.
- [ ] Any existing email service still works, if one is configured.
- [ ] Update this document's current-state table, the dashboard, and dated decisions with observed results.

Keep the existing Plan & Adapt content until this verification is complete. See [migration notes](migration.md) for calendar and Music-page follow-up.

## Cost and ongoing deployments

This project is a static site with no database, Pages Functions, paid media storage or form provider. It is intended to fit Pages Free; IONOS domain renewal is separate. Recheck pricing before adding services. Once Git integration is connected, merges to main publish builds; documentation-only merges can also rebuild. PR preview deployments are also public URLs unless access restrictions are configured; noindex is not access control.

## Rollback

For a later bad release, select the last verified production deployment in Pages and use its rollback action, then reconcile GitHub through a corrective PR. Before the first successful release there is no known-good band deployment to restore. For DNS trouble, use the recorded pre-change nameservers/records to restore the previous service if appropriate. Never change Plan & Adapt's zone as part of band-site rollback. Record what was changed and verified; keep credentials out of the repository.

## Official references

- [Astro on Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/)
- [Build image and runtime overrides](https://developers.cloudflare.com/pages/configuration/build-image/)
- [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)
- [IONOS custom nameservers](https://www.ionos.com/help/domains/using-your-own-name-servers/using-your-own-name-servers-for-a-domain/)
- [www redirect](https://developers.cloudflare.com/pages/how-to/www-redirect/)
- [Static headers](https://developers.cloudflare.com/pages/configuration/headers/)
- [Pages limits](https://developers.cloudflare.com/pages/platform/limits/)
