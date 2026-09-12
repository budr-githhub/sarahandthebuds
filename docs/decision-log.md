# Decision Log

Append dated entries using Date, Decision, Reason, Alternatives considered, and Impact. Preserve previous decisions as history; explicitly mark superseded choices when needed.

## Independent band site

**Date:** 2026-09-12

**Decision:** Use a separate `sarahandthebuds` GitHub repository and Cloudflare Pages project, with the domain registered at IONOS. Retain Astro and pnpm; site source is at repository root. Keep band and acoustic-duo detail here; Plan & Adapt will retain a brief band feature, radio show, and solo work.

**Reason:** Give the band its own destination while keeping updates understandable and independent from Bud's other work.

**Alternatives considered:** Keeping all details on Plan & Adapt; maintaining two sites in one repository; another hosting provider. Bud selected Cloudflare and a separate repository.

**Impact:** Initial implementation is in PR #1. Static hosting requires no database or Pages Functions. Source, photos and contact links were adapted from Plan & Adapt. Production deployment and domain verification remain pending.

## Interim show calendar (superseded)

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

## Calendar implementation and release order

**Date:** 2026-09-12

**Decision:** Keep one combined calendar in the band repository, with all seven existing events preserved. Unknown performers are omitted from structured data as well as visible copy; do not assume every date is the full band. No synchronization service or second event dataset.

**Reason:** Bud selected the band as the source of truth. This supersedes the interim calendar backlink and the earlier performer-tagging prerequisite for moving the combined list.

**Impact:** Publish and verify band `/shows` first, then release the Plan & Adapt Music cleanup and permanent redirect. Implementation is prepared on separate branches; no release is implied by this record. Plan & Adapt retains radio and solo work. A simple solo introduction/contact link is used until listening links are supplied.

## Separation and calendar release completed

**Date:** 2026-09-12

**Decision and outcome:** Bud approved both releases. Band PR #2 deployed at `c5577d2`; Plan & Adapt PR #23 deployed afterward at `b606ba5`. Live contents and redirects verified. Earlier pending-domain, unimplemented-cleanup and performer-tagging prerequisites are historical and superseded. See the dashboard for the completed sequence and maintenance ownership. No new dependency, sync service or DNS change was needed for the calendar release.

## Apply supplied S&B visual identity

Bud supplied Sarah-and-the-Buds-Style-Guide.docx version 1.0 (September 2026) and requested it be retained as project memory and applied to the site. It replaces the inherited green/cream serif design with Stage Black/Warm White and Avenir Next/Montserrat. Preserve the original logo as artwork, keep existing events and natural photos, and use uppercase AM/PM. Source document and text transcription are archived in docs; release remains subject to review.

## Add approved natural photography

**Date:** 2026-09-12

**Decision:** Add seven prepared photos while keeping existing images. Use photo 10 instead of photo 11. Two introduction portraits distinguish the full band and acoustic duo; five gallery additions show performances, community and a past venue appearance.

**Reason:** Bud approved these selections and requested additions to the existing site.

**Alternatives considered:** Replacing existing photos or displaying all 15; neither matches the selected scope.

**Impact:** WebP assets and descriptive captions added; no dependency, calendar or DNS change. Release pending review.

## Hero and caption revision — 2026-09-12

Bud requested pictures without visible captions and a band-only version of photo 4 at the top. Move the former hero into the gallery; preserve the original barn portrait in the introduction. A dark-background AI-edited hero is prepared for likeness review. Accessible alt text remains. This supersedes the earlier visible-caption plan; release remains pending.

## Symmetric portraits and continuous gallery — 2026-09-12

Bud requested matching band/duo image dimensions and removal of empty gallery spaces. Photo 10 now pairs with the duo in matching 4:5 frames, retaining all four band members. The original barn portrait moves into the gallery. All 12 gallery photos flow in responsive columns (three desktop, two tablet, one phone) at natural aspect ratios, eliminating separate grids and tall-row gaps. No captions; hero unchanged. Supersedes earlier placement notes.
