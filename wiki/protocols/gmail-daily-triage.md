---
type: protocol
status: active
created: 2026-06-14
updated: 2026-06-15
tags: [gmail, inbox, automation, triage, daily]
domain: personal-admin
domains: [gmail, email, automation, wiki]
confidence: high
review_cycle: monthly
verification_status: spot-checked
related:
  - ../source-summaries/gmail/index.md
  - ../../index.md
  - ../../dashboards/recent-updates.md
  - ../../ops/ingestion-registry.md
---

# Gmail Daily Triage Protocol

## Trigger / scope

Run every day at 07:00 Asia/Hong_Kong so the mailbox is already organized before 08:00 Beijing time. Cover the last 24 hours of inbox, unread, important, and still-in-inbox read mail. Exclude Spam and Trash.

## Inputs

- Gmail connector search results and labels
- The current mailbox state
- The automation memory for prior user preferences and exceptions

## Steps

1. Scan recent mail and identify likely action items, dates, bills, project updates, key contacts, and FYI.
2. Classify conservatively.
3. Apply labels for action, waiting, FYI, bills/financial, schedule, newsletters/promotions, and GitHub/CI when useful.
4. Archive only clearly low-value, already-read mail that is not personally sensitive and not about security, accounts, billing, orders, or scheduling.
5. Mark already-reviewed safe mail as read when the user has explicitly said it is okay to clear.
6. Preserve strong-reason security and account alerts unless the user explicitly asks to clear everything.
7. Write the day’s summary to `wiki/source-summaries/gmail/YYYY-MM-DD.md`.
8. Update the Gmail source index and recent-updates surface if the day introduced a meaningful change.

## Failure modes

- Gmail auth or connector failure
- Timezone drift that misses the before-08:00 Beijing window
- A security or credential alert being misclassified as normal
- Missing write access to the wiki path
- Repeated GitHub CI failures where the latest meaningful failure is unclear

## Review notes

- The user prefers not to send a daily summary email unless explicitly asked.
- If uncertainty remains, keep the item visible and explain why.
- The dated source-summary file is the canonical daily output.
- Use `wiki/source-summaries/gmail/template.md` as the default layout for new daily runs.
- Keep the latest GitHub `main` CI failure visible when no later success or fix notification exists; archive older duplicates after labeling them.

## Related pages

- [Gmail source summaries](../source-summaries/gmail/index.md)
- [Recent Updates](../../dashboards/recent-updates.md)
- [Ingestion Registry](../../ops/ingestion-registry.md)

## Sources

- /Users/moltbot/.codex/automations/gmail/automation.toml
- /Users/moltbot/.codex/automations/gmail/memory.md
