# AGENTS.md

Shared guidance for Codex, Claude Code, and other coding agents. Adapted from Plan & Adapt's conventions; paths and deployment status here apply to this repository.

## Project context and stack

Sarah & the Buds is an independent Astro static site for the full band and Sarah & Bud acoustic duo. Source lives at the repository root (`src/`, `public/`, `package.json`), unlike Plan & Adapt's `site/` subdirectory. Use pnpm; Node must satisfy `package.json`. Cloudflare Pages is the live host; IONOS remains the registrar. Read [dashboard](docs/dashboard.md) for verified current status.

## Hard constraints

Unless authorized by Bud in the current conversation, do not commit, push, deploy, modify DNS, delete files, or add significant dependencies/services. Explain replacements before overwriting existing content. Existing authorization in the conversation remains valid within its scope; do not ask again for the same action. Repository preparation does not itself authorize a production release or DNS cutover.

## Visual identity memory

Read [the S&B style guide](docs/style-guide.md) before visual or promotional changes. It supersedes the original Plan & Adapt palette and serif typography. Use supplied logo artwork, never retyped S&B. Preserve natural performer photos and unknown lineup assignments.

## Project principles

Prefer simple, accessible, fast, static solutions with minimal JavaScript and no database. Keep changes small and reviewable. Do not invent biographies, recordings, testimonials, performance dates, performer assignments, or booking terms. Preserve the existing band and duo distinction. Bud's radio show and solo work belong on Plan & Adapt.

## Source of truth

- GitHub `main` is the canonical accepted source: `budr-githhub/sarahandthebuds`. Unmerged branches are proposals, not accepted production state.
- Temporary clones, screenshots and chat messages are not durable project records. Use this repository's docs and PRs.
- Code is observed implementation; docs and decisions explain intended behavior. Flag disagreements and reconcile them rather than silently redesigning.
- Once Cloudflare is connected, merging to `main` is the release step; even a docs-only merge can trigger a build. Verify the deployed commit before marking work live.

## Documentation conventions

- Durable shared rules: this file. Claude-specific guidance: [CLAUDE.md](CLAUDE.md), which imports this file.
- Changing status and task ownership: [dashboard](docs/dashboard.md).
- Dated choices and reasons: [decision log](docs/decision-log.md).
- Rendered language: [copy deck](docs/copy-deck.md). Update source and the matching copy together; documentation alone does not change the site.
- Hosting configuration and verification: [domain and hosting](docs/domain-and-hosting.md).
- Cross-site migration: [migration notes](docs/migration.md).

## Coordination and checks

Read this file, the dashboard, recent decision-log entries, open PRs, and the [AI playbook](docs/ai-playbook.md) before work and at handoff. Use one implementation owner per task, separate branches/checkouts for concurrent work, and never change another agent's branch. Review current contents before editing; preserve uncommitted owner work.

Run `pnpm build` for source/configuration changes; check generated links and relevant browser behavior. For documentation-only changes, check links, paths, commands, factual status and `git diff --check`; no build is needed unless runtime inputs changed. Report exact validation and limits. Keep PR descriptions current and use the playbook handoff template. Documentation does not notify or automatically synchronize agents.
