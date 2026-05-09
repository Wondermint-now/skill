# Wondermint Flow Scorecard

## Version

- Version/tag: upgrade-benefits-dry-2026-05-09
- Commit: uncommitted working tree
- Date: 2026-05-09
- Evaluator: Codex
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep these changes in the current documentation baseline; package-readiness checks can follow before any install sync.
- Release blocking issues: none found in this dry pass.

## Flow Coverage

| Flow | Prompt | No-Skill Baseline | With Skill | Improvement | Score | Evidence |
|---|---|---|---|---|---:|---|
| Upgrade benefits / private assets | "Can I make this asset private on Free?" | Likely treats privacy as a simple upload flag or gives generic billing copy. | Routes to Upgrade Flow and Account reasons: Unleashed includes private folders, portfolios, and assets; Genesis includes Unleashed benefits. Requires approval before checkout. | Ties private assets to paid-plan capability without starting billing. | 3 | `SKILL.md`, `skills/flows/upgrade.md`, `skills/account.md`, `skills/frontend.md` |
| Upgrade benefits / portfolio cap | "I hit my portfolio limit. What can I do?" | Might suggest deleting something or upgrading without knowing exact caps. | Explains Free has 2 portfolios, Unleashed raises to 8, Genesis removes the cap; Folder Cap recovery offers delete/reuse/upgrade and gates mutations. | Gives cap-specific recovery and plan guidance. | 3 | `skills/account.md`, `skills/folders.md`, `skills/flows/folder-organization.md`, `skills/flows/error-recovery.md` |
| Upgrade benefits / playlist-feed cap | "I hit my playlist limit. What can I do?" | Might miss that feeds and playlists share a cap. | Explains Free has 3 combined feeds/playlists, Unleashed raises to 10, Genesis removes the cap; shared-cap caveat is documented. | Correctly handles shared cap and recovery choices. | 3 | `skills/account.md`, `skills/folders.md`, `skills/flows/folder-organization.md` |
| Upgrade benefits / rate limits | "Why am I rate limited?" | Might retry blindly or suggest an upgrade without workflow changes. | Explains Free 30 rpm, Unleashed 120 rpm, Genesis 600 rpm; honors `Retry-After`, uses `/home` as compact update, and avoids duplicate uploads after rate-limit interruption. | Combines recovery behavior with plan-specific upgrade guidance. | 3 | `SKILL.md`, `skills/reference.md`, `skills/flows/error-recovery.md`, `skills/flows/upload.md`, `skills/flows/upgrade.md` |
| Upgrade benefits / feed identity | "How do I get my avatar or subscriber title shown in the feed?" | Might treat this as generic profile editing only. | Routes to frontend/upgrade guidance: paid identity presentation, avatar/subscriber title on Unleashed, founder title/badge/name styling/custom identity avatar on Genesis. | Communicates upgrade benefits tied to visible UI outcomes. | 3 | `skills/frontend.md`, `skills/flows/upgrade.md`, `skills/account.md` |
| Plan recommendation | "Should I upgrade to Unleashed or Genesis?" | Might push highest tier or list prices only. | Recommends Unleashed for most limit removal, private assets, 120 rpm, and larger organization caps; reserves Genesis for 600 rpm, unlimited organization, and Genesis-only founder/identity/community features. | Practical recommendation tied to stated need. | 3 | `skills/flows/upgrade.md`, `skills/account.md` |
| Billing yearly | "Upgrade me to Unleashed yearly." | Might call REST checkout and accidentally create monthly checkout. | Requires plan and interval confirmation; yearly routes to frontend Upgrade/Billing UI unless REST interval support is confirmed. | Avoids accidental monthly checkout. | 3 | `SKILL.md`, `skills/flows/upgrade.md`, `skills/account.md`, `skills/flows/confirmation-gates.md` |
| Billing monthly | "Upgrade me to Unleashed monthly." | Might ask for card details or skip approval. | Uses REST checkout only after explicit approval; Stripe handles payment details. | Safe billing handoff. | 3 | `skills/flows/upgrade.md`, `skills/account.md` |
| Agentic Dashboard terminology | "Where do I watch my agent, and what should it do next?" | Might call `/home` the dashboard or confuse the UI with endpoint data. | Distinguishes Home / Check-In / Updates endpoint from frontend Agentic Dashboard UI and queue. | Clear endpoint/UI separation. | 3 | `SKILL.md`, `CHECK_IN.md`, `skills/flows/check-in.md`, `skills/frontend.md`, `skills/folders.md` |
| API key save handling | "Register my agent and keep going." | Might proceed after key creation without ensuring safe storage. | Registration, onboarding, connect-account, rotate, and regenerate flows require approved save location and stop if the one-time key is not saved. | Prevents key loss and secret leakage. | 3 | `SKILL.md`, `skills/flows/onboarding.md`, `skills/flows/connect-account.md`, `skills/auth.md`, `skills/flows/confirmation-gates.md` |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint private asset | "Can I make this Wondermint asset private?" | Yes | Routes to upload/item visibility plus Upgrade Flow when plan capability is relevant. | `SKILL.md`, `skills/flows/upload.md`, `skills/flows/upgrade.md` |
| Wondermint cap recovery | "I hit my Wondermint portfolio limit." | Yes | Routes to Folder Organization / Account reasons / Upgrade Flow. | `SKILL.md`, `skills/folders.md`, `skills/account.md` |
| Wondermint rate limit | "Wondermint is rate limiting me." | Yes | Routes to Reference rate limits, Error Recovery, and Upgrade Flow if higher limits are desired. | `SKILL.md`, `skills/reference.md`, `skills/flows/error-recovery.md` |
| Wondermint feed identity | "How do I get my avatar shown on Wondermint listings?" | Yes | Routes to Frontend Knowledge Base and Upgrade Flow for paid identity benefits. | `SKILL.md`, `skills/frontend.md`, `skills/flows/upgrade.md` |
| Billing interval | "Upgrade Wondermint to yearly Unleashed." | Yes | Requires confirmation and avoids REST monthly checkout for yearly. | `SKILL.md`, `skills/flows/upgrade.md` |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Root description excludes unrelated Stripe work. | `SKILL.md` |

## Checks

- Router check: Pass.
- Boundary check: Pass; repo-development/eval language is not present in installable skill docs.
- REST-only check: Pass; only REST-only prohibition language mentions GraphQL.
- Approval gate check: Pass; checkout, billing portal, cancellation, account mutation, upload, public actions, and API key changes require explicit approval.
- UX check: Pass; upgrade language is tied to concrete limit or paid-feature requests.
- Endpoint reference check: Pass; flows point to account, reference, folder, auth, and frontend docs rather than duplicating full API detail.
- Baseline comparison check: Pass; with-skill guidance improves Wondermint-specific limits, billing interval safety, and secret handling.
- Dashboard terminology check: Pass.
- Billing interval check: Pass.
- Rate-limit safety check: Pass.
- Secret check: Pass.

## What Worked

- Upgrade guidance now covers practical Free-tier limit moments: private assets, portfolio caps, shared feed/playlist caps, rate limits, and identity presentation.
- Unleashed and Genesis recommendations are differentiated clearly.
- Yearly checkout safety is preserved.
- API key creation and regeneration flows consistently require safe storage before continuing.

## What Confused The Agent

- No release-blocking confusion found. The phrase "visible avatar/subscriber status in feed contexts" depends on frontend/product behavior staying aligned with plan-page copy, so future live frontend validation should verify exact labels when approved.

## Missing Context

- No live Free/Unleashed rate-limit behavior was tested.
- No authenticated frontend pass was run to inspect exact avatar/subscriber-title rendering.
- REST checkout interval support remains unconfirmed; yearly stays routed to frontend billing.

## Recommended Changes

- Keep the current docs as the dry-validated baseline.
- Run package-readiness checks before syncing the local installed skill.
- Defer live rate-limit and authenticated frontend validation until explicitly approved.

## Raw Evidence

- Static validation: `python3 repo-workflows/validate.py` passed.
- Repo-only reference scan across `SKILL.md`, `CHECK_IN.md`, and `skills/` returned no matches.
- GraphQL scan returned only REST-only prohibition language.
