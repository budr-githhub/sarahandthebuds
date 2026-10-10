# Editing shows with Pages CMS

Status: trial prepared October 10, 2026. Hosted sign-in, GitHub app authorization and the first real CMS save still require Bud. No CMS account or collaborator invitation has been created by Codex.

## One-time setup (Bud)

1. Open https://app.pagescms.org/ (also linked as **Manage shows** in the website footer).
2. Sign in with GitHub. Review the service terms and GitHub authorization prompts yourself.
3. Install/authorize the Pages CMS GitHub app for **only `budr-githhub/sarahandthebuds`**, then open that repository and select **main**. Saving on main triggers production publication after a successful Cloudflare build.
4. The repository's `.pages.yml` supplies **Shows — all dates** and **Venues — existing locations**. Do not replace this configuration with a generated starter.
5. For the first trial, add a clearly named draft, save it, reopen it to check the fields survived, and confirm it is absent from the public Shows page. Then remove the trial draft. Do not change real gig dates just to test.
6. Sarah can be added later through Pages CMS collaborator settings. Bud should review access and provide her preferred email; no invitations have been sent.

## Add or edit a show

Open **Shows — all dates**, then add an entry or open an existing one. Fill in event name, date, start/end time, venue and performing act. Time fields use **24-hour Eastern time**: 14:00 = 2 PM, 18:00 = 6 PM. For overnight/multi-day events, set the end date; otherwise leave it blank.

Choose **Other act / collaboration** for acts such as The Lost Dogs and enter the performer names. Add description, event/ticket URL and admission information when known. Venue selection supplies the shared address and links on the public page. If the event name differs from the venue, include the venue in the event name, for example “Christmas Balloon Glow — Wildside Winery.”

- **Draft:** hidden from the website. Draft data still lives in this public GitHub repository; do not enter private notes or contact information.
- **Published:** shown on the website after the Cloudflare deployment succeeds.
- **Cancelled:** remains visible with a cancellation notice and cancelled structured data.

Save the file and wait for deployment. The full calendar is one file: avoid editing it simultaneously with another person. Removing an entry removes it entirely, including from Past. Normal completed shows move to Past automatically; keep those records.

## Venues and trial limits

**Venues — existing locations** edits the six current venue records. Changes affect every show using that venue. Name and city are required; address and website are optional. Adding a brand-new venue currently needs a small configuration update by Codex so it appears in the dropdown. This trial does not include poster uploads, a custom preview panel or editing other site content. The CMS menu limits editing convenience; it is not a security boundary for GitHub users with wider repository access.

## Validation and recovery

Required fields and time/URL patterns are checked in the editor. The build additionally rejects impossible dates, end-before-start times, unknown venues and missing custom performer names. Cross-field errors are reported by the build, not an inline CMS notification. If a save produces a failed deployment, the previous successful site remains live: correct the fields and save again, or ask Codex to restore the previous Git version. “Saved” in the CMS does not prove the site has deployed.

## Documentation and maintenance

`src/data/events.json` and `src/data/venues.json` remain the source of truth. `node scripts/calendar.mjs --write` generates a local calendar inventory. The read-only GitHub **Validate calendar and generate report** workflow runs after data changes on main and uploads the current inventory as a downloadable Actions artifact. The checked-in [calendar reference](calendar-inventory.md) links to source and reports rather than duplicating dates. Local reports are written to ignored `reports/calendar-inventory.md`. It does not certify deployment. Deployment status remains in [dashboard](dashboard.md) and [hosting](domain-and-hosting.md). The copy deck links to the calendar reference rather than duplicating changing calendar entries.

Developer checks: `pnpm run test:calendar`, `pnpm build`, `pnpm run calendar:docs`, `git diff --check`. Keep `.pages.yml` dropdowns and venue fields in sync when adding venues. The file uses JSON syntax, which is valid YAML. Whole-file delete/rename operations are disabled; adding/removing list rows is still supported.

References: [Pages CMS quick start](https://pagescms.org/docs/quick-start/), [top-level arrays](https://pagescms.org/docs/configuration/content/list/), [field configuration](https://pagescms.org/docs/configuration/content/fields/), [collaborators](https://pagescms.org/docs/configuration/collaborators/).
