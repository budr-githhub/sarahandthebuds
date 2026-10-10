# Calendar source and reports

The current saved calendar is [events.json](../src/data/events.json), with shared locations in [venues.json](../src/data/venues.json). These files are the single source of truth; this document intentionally does not duplicate dates or counts.

Every calendar-data push to main runs **Validate calendar and generate report** in [GitHub Actions](https://github.com/budr-githhub/sarahandthebuds/actions). Download its `calendar-inventory` artifact for a readable table of non-draft records, times, acts, venues and links. A report records saved content; a successful Cloudflare deployment confirms publication.

Developers can generate the same table locally with `pnpm run calendar:docs`. The local report is written to ignored `reports/calendar-inventory.md`. The workflow has read-only repository permissions and cannot commit or push changes.
