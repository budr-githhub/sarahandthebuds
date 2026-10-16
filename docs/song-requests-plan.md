# Song requests and Venmo — proposed

October 16, 2026. Owner: Bud. Implementation planning: Codex. This is a recommendation, not a working request form, payment integration or notification service. Existing mailto links remain available.

## Recommended first version

1. Fan opens the songbook (including a printable QR link for shows), searches by title or artist, and selects up to three songs.
2. Fan optionally adds a name and short message and selects the show, or chooses a general request. No fan email or phone is required.
3. A server-side Cloudflare endpoint validates song IDs and lengths, checks anti-spam protection/rate limits, and sends one email with the selected titles/artists, show, message and request ID to a confirmed band inbox. Server secrets never enter browser code. Escape user content and prevent duplicate submissions.
4. Only after the email provider accepts the message, show a request receipt. On failure preserve the selection and offer retry/the existing mailto contact. Acceptance is not a guarantee of inbox delivery or performance.
5. The receipt offers an optional Venmo tip through the owner-confirmed profile link and QR code. Display a copyable note containing the request ID and song titles. Fans can request without tipping. Never interpret clicking Venmo, returning to the site, or checking a box as verified payment.

Suggested copy: “Choose a few favorites and send them our way. Tips are appreciated and optional. Requests depend on the lineup, time and set; we can’t promise every song.”

## Email first; text later

Use a Cloudflare Pages Function/Worker with Resend and a verified sender domain. Cloudflare documents this combination: [Send emails with Resend](https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/). Confirm account availability/pricing before enabling a service. Do not change DNS until setup scope is approved. No database is needed for the initial email workflow; keep submitted messages out of analytics/logs and retain only minimal anti-abuse data for a documented short period.

SMS through Twilio is a later option, requiring a private recipient number, budget and sender setup. US automated messaging involves [A2P registration](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc) or an appropriate verified alternative. Email phone notifications are an easier first trial.

## Venmo limits and decisions

Use a profile appropriate for the band’s commercial activity. [Venmo business QR codes](https://help.venmo.com/cs/articles/qr-codes-for-business-profiles-vhel305) open the business payment screen; [business-profile payments](https://help.venmo.com/cs/articles/buying-from-business-profiles-on-venmo-vhel139) support tipping. The band verifies receipts in Venmo manually. Do not invent deep-link amount/note parameters or claim payment confirmation from a profile link.

If Bud wants mandatory payment or payment-verified requests, scope a supported merchant checkout with server-side payment verification separately, including unplayed-request/refund rules. A profile link alone cannot provide this. Do not call tips charitable donations.

## Needed from Bud

- Exact Venmo profile URL/handle and preferred QR image; confirm account type.
- Confirm notification inbox (proposed: booksarahandbud@gmail.com).
- Approve optional tips vs mandatory paid requests; recommendation is optional tips.
- Approve service/account setup and sender verification; supply access through secure account setup, not committed keys.
- Optional later: private SMS recipient and budget.

## Implementation and verification once approved

Codex can build selection/search, request endpoint, email template, receipt, Venmo links/QR placement, and documentation. Bud connects/authorizes accounts and confirms payment identity. Test keyboard/mobile use, unavailable songs/show selection, validation, spam checks, duplicate clicks, provider failure/retry and real delivery to the approved inbox before release. Test Venmo handoff on phone and desktop; no payment is needed to verify navigation. Clearly keep request receipt separate from payment and performance status. Record preview, published and verified status after each push.
