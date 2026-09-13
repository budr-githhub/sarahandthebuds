# Sarah & the Buds

Independent Astro website for Sarah & the Buds and the Sarah & Bud acoustic duo.

## Local development

Use Node 22.12 or newer and pnpm. Run `pnpm install --frozen-lockfile`, then `pnpm dev`.
Run `pnpm build` to generate `dist/`; `pnpm preview` serves the production build locally.

## Editing

- Band copy, photo gallery and booking: `src/pages/index.astro`.
- Songbook metadata: `src/data/songbook.json`; full reference: `src/pages/songbook.astro`.
- Shows: `src/pages/shows.astro`, rendering the combined calendar from `src/data/events.json`.
- Shared design: `src/styles/global.css` and `src/components/`.
- Photos: `public/images/music/`. Only images used by this site are included.

Use a branch and pull request for changes. Review and build before merging to `main`.

## Cloudflare Pages setup

Follow [Domain & Hosting Notes](docs/domain-and-hosting.md) for the exact setup, domain connection, verification and rollback sequence. Production uses `main`, root directory blank, `pnpm build`, output `dist`. The initial site and calendar are deployed.

## Documentation and collaboration

Start with the [dashboard](docs/dashboard.md) and [document index](docs/README.md). Shared rules live in [AGENTS.md](AGENTS.md); [CLAUDE.md](CLAUDE.md) imports them. The [AI playbook](docs/ai-playbook.md) defines task ownership and handoff. Keep the [copy deck](docs/copy-deck.md) synchronized with visible source text and record choices in the [decision log](docs/decision-log.md).

GitHub `main` is the accepted source of truth. Temporary working copies are not canonical. Source is at repository root, unlike Plan & Adapt's `site/` folder. Hosting status is recorded in the dashboard; do not infer deployment from a successful local build.

See [migration notes](docs/migration.md) for the completed separation and ongoing ownership.

## Editing shows

Edit `src/data/events.json` for the combined calendar. Dates use YYYY-MM-DD and times HH:MM in America/New_York. Preserve unknown fields as omitted. Run `pnpm build` and review before release. See [dashboard](docs/dashboard.md) for current deployment status.

## Visual identity

Follow [the S&B style guide](docs/style-guide.md) for colors, typography, logo artwork, photography and promotional materials. Its original DOCX is archived in docs/assets.


Press, Friends, branding and event-detail additions are approved for publication; see [the implementation and owner checklist](docs/press-friends-brand.md) for downloads, maintenance, sources and pending inputs. See the dashboard for verified deployment status.
