# Decision Log

Append dated entries using Date, Decision, Reason, Alternatives considered, and Impact. Preserve previous decisions as history; explicitly mark superseded choices when needed.

## Independent band site

**Date:** 2026-09-12

**Decision:** Use a separate `sarahandthebuds` GitHub repository and Cloudflare Pages project, with the domain registered at IONOS. Retain Astro and pnpm; site source is at repository root. Keep band and acoustic-duo detail here; Plan & Adapt will retain a brief band feature, radio show, and solo work.

**Reason:** Give the band its own destination while keeping updates understandable and independent from Bud's other work.

**Alternatives considered:** Keeping all details on Plan & Adapt; maintaining two sites in one repository; another hosting provider. Bud selected Cloudflare and a separate repository.

**Impact:** Initial implementation is in PR #1. Static hosting requires no database or Pages Functions. Source, photos and contact links were adapted from Plan & Adapt. Production deployment and domain verification remain pending.

## Interim show calendar

**Date:** 2026-09-12

**Decision:** Link the band site's Shows page to the existing Plan & Adapt calendar until performer assignments are confirmed.

**Reason:** Existing entries do not distinguish solo, duo and full-band shows, despite the page describing all three.

**Alternatives considered:** Copying every event and assuming it is a band show, or redirecting the entire mixed calendar. Both could misclassify shows or create a redirect loop.

**Impact:** Confirm assignments before moving events. Preserve the original calendar during preparation; coordinate subsequent changes in both repositories.

## Shared documentation and agent coordination

**Date:** 2026-09-12

**Decision:** Follow Plan & Adapt's conventions: canonical AGENTS.md, a short CLAUDE.md importing it, a dashboard for status, dated decisions, an AI playbook and handoff template, a copy deck, and domain/hosting notes.

**Reason:** Bud requested clear, maintained documentation so Codex and Claude can collaborate without relying on chat history.

**Alternatives considered:** Copying every Plan & Adapt planning document, or keeping instructions only in README. The former brings unrelated content and stale assumptions; the latter obscures ownership and deployment status.

**Impact:** Documentation uses actual root-level paths and distinguishes tested local code from unverified hosting. This documentation-only follow-up stays in initial PR #1. No new dependencies, deployment, DNS, or Plan & Adapt changes are included.
