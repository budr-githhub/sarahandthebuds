# AI Playbook

## Roles and ownership

Codex and Claude Code can implement assigned changes; the other can review when Bud requests collaboration. Claude can also review language and content structure. Bud owns content decisions and release approval. Assign one implementation owner per task; roles are workflow assignments, not fixed capability limits.

## Working together

1. Read [AGENTS.md](../AGENTS.md), [dashboard](dashboard.md), recent [decisions](decision-log.md), and open PRs. Record the base commit and check for uncommitted changes.
2. Record owner, scope, acceptance criteria, branch and PR in the dashboard. Use that and the PR as the shared coordination record, not a second tracker.
3. Use separate branches/checkouts for concurrent tasks. Serialize edits to shared layouts, CSS, page copy and asset files. Never switch the branch under another agent.
4. Update implementation and matching docs in the same PR. Preserve owner edits in the copy deck; do not regenerate over pending edits.
5. Review the exact commit and state findings on that revision. Before merge, compare with current `main` and rerun relevant checks if implementation changes.
6. Bud approves release. Once connected to Cloudflare, `main` merges can deploy, including documentation-only changes. A successful local build is not proof of live deployment.
7. After a confirmed deployment or DNS change, record the observed commit, URL, date and result in the dashboard and hosting notes; add a dated decision where appropriate.

For a cross-site task, inspect both repositories' current instructions and PRs, use one PR per repository, and link their dependencies. Do not remove Plan & Adapt's band details before the new domain is verified. The combined calendar may move without performer tags under the September 12 decision; never invent assignments. Verify the band calendar live before activating Plan & Adapt redirects.

## Handoff template

```text
Task:
Owner / next owner:
Status: proposed | approved | in progress | ready for review | merged | deployed
Base commit:
Branch / PR / reviewed commit:
Goal and acceptance criteria:
Files or sections in scope:
Dependencies / overlapping work:
Changes and decisions:
Checks performed and results:
Remaining questions or work:
Deployment status:
```

## Documentation maintenance

Update the dashboard at each meaningful milestone or handoff. Append decisions with Date, Decision, Reason, Alternatives considered, and Impact. Keep detailed setup instructions in the hosting document and link to them from README. Update the copy deck whenever visible text changes. Use explicit “pending” or “not verified” states instead of guessing deployment, nameserver, or email values.

Documentation is a coordination convention, not a lock or notification service. Neither agent automatically reads the other's chat or watches GitHub. A handoff needs an explicit task or review request; send no messages to others without Bud's authorization.
