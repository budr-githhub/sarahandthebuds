# Sarah & the Buds

Independent Astro website for Sarah & the Buds and the Sarah & Bud acoustic duo.

## Local development

Use Node 22.12 or newer and pnpm. Run `pnpm install --frozen-lockfile`, then `pnpm dev`.
Run `pnpm build` to generate `dist/`; `pnpm preview` serves the production build locally.

## Editing

- Band copy, repertoire, photo gallery and booking: `src/pages/index.astro`.
- Shows: `src/pages/shows.astro` (links to the existing calendar until performer assignments are confirmed).
- Shared design: `src/styles/global.css` and `src/components/`.
- Photos: `public/images/music/`. Only images used by this site are included.

Use a branch and pull request for changes. Review and build before merging to `main`.

## Cloudflare Pages setup

1. Workers & Pages → Create application → Pages → Import an existing Git repository.
2. Select `budr-githhub/sarahandthebuds`.
3. Production branch: `main`; framework: Astro; root directory: leave blank.
4. Build command: `pnpm build`; build output directory: `dist`.
5. Set `NODE_VERSION` to `22` if the build environment needs an explicit version.
6. After the initial pull request is reviewed and merged, deploy and inspect the assigned pages.dev URL.
7. Add sarahandthebuds.com as a Cloudflare zone on Free, review existing email/DNS records, then use the nameservers assigned specifically to this domain at IONOS.
8. In Pages → Custom domains, add sarahandthebuds.com and www.sarahandthebuds.com. Configure www to redirect to the apex and verify HTTPS.

This is a static site with no Pages Functions, database, paid media storage, or form service. Booking uses the existing email address. Preview-host noindex headers are in `public/_headers`; verify them after deployment. Domain registration/renewal remains at IONOS.

See [migration notes](docs/migration.md) for the remaining coordinated changes on Plan & Adapt.
