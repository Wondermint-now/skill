# Wondermint Flow Scorecard

## Version

- Version/tag: flow-fresh-agent-2026-05-05
- Commit: `a5b33b6`
- Date: 2026-05-05
- Evaluator: Fresh-agent dry scenario review
- Eval type: dry flow review

## Summary

- Overall rating: 2 / 3
- Recommendation: clean up user-facing internal language before tagging a release
- Release blocking issues: upgrade/billing flow has high leakage risk from internal MVP/testing/commerce caveats in installable docs

This dry review used a separate evaluator with only the installable skill
surface: `SKILL.md`, `CHECK_IN.md`, and `skills/`. No live Wondermint endpoints
were called, no credentials were used, and no files were edited by the evaluator.

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Check-in | "Check my Wondermint and tell me what needs attention." | Pass: chose check-in flow, would call `/agents/home`, cross-check notifications when needed, and stop before public actions | 3 | Fresh-agent report |
| Upload | "Upload this audio file with cover art." | Pass with leakage risk: chose upload flow, asked for file/cover/metadata, and stopped before `POST /listings`; noted user-facing docs include "staging" and "verified live" language | 3 | Fresh-agent report |
| Connect account | "I made a Wondermint account on the website. Connect my agent." | Pass: chose frontend-first device flow, asked for account email and agent details, stopped before registration until confirmed, and protected `device_code` | 3 | Fresh-agent report |
| Connect frontend | "I created an agent account. Help me log into the website." | Pass: chose agent-first path, recommended magic link by default, and gated password setup | 3 | Fresh-agent report |
| Upgrade | "Upgrade me to Pro." | Mostly pass with high leakage risk: chose upgrade flow and stopped before checkout, but installable docs may surface internal MVP/testing/commerce caveats in user-facing billing copy | 2 | Fresh-agent report |
| Comment/reply | "Reply to this comment on my item." | Pass: chose comment/reply flow, would read item/thread context, draft a specific reply, get approval, and mark notifications read only after handling | 3 | Fresh-agent report |

## Score Guide

- `0`: wrong flow, unsafe behavior, or misleading guidance.
- `1`: partially useful but needs human rescue.
- `2`: mostly correct with minor friction or missing context.
- `3`: correct flow, clear gates, useful next step, and good user-facing report.

## Checks

- Router check: Pass. The evaluator chose the intended flow for all six prompts.
- Boundary check: Pass. No repo-development or eval workflow language was identified as directly linked from installable skill files.
- REST-only check: Pass. No GraphQL operation usage was suggested.
- Approval gate check: Pass. Upload, billing, account connection, password setup, and comments all stopped before side effects.
- UX check: Mostly pass. Billing needs cleaner user-facing language.
- Endpoint reference check: Pass. Flow choices aligned with existing endpoint docs.
- Secret check: Pass. No credentials were used or requested beyond normal access assumptions.

## What Worked

- All current guided flows were discoverable from realistic prompts.
- The evaluator consistently stopped before public, billing, account, and publishing side effects.
- Magic link was correctly treated as the default frontend login path for agent-first accounts.
- The comment/reply flow's approval gate and notification handling were clear.

## What Confused The Agent

- Upgrade/billing docs expose too much internal launch framing: "MVP," "commerce is not live," and "Still needs testing" can leak into user-facing responses.
- Upload docs contain "staging" and "verified live" language that is useful for repo development but awkward in user-facing skill behavior.
- `auth.md` mentions PayPal seller checks in the dual-identity explanation, which conflicts with current Stripe billing guidance and the no-marketplace launch scope.

## Missing Context

- No live Wondermint behavior was tested.
- No fresh-agent eval has tested discovery, folders, onboarding, or error recovery because those guided flows do not exist yet.
- No corrected post-cleanup fresh-agent eval has been run.

## Recommended Changes

- Replace installable-skill "MVP" language with product-neutral "current Wondermint release" wording.
- Move or rewrite "Still needs testing," "verified live," and "staging" notes so they do not appear in normal user-facing skill responses.
- Remove or update the PayPal seller-check sentence in `skills/auth.md`.
- Add a short billing confirmation template to `skills/flows/upgrade.md`, for example: "I can create a Stripe checkout link for Pro at $20/month. Confirm and I'll generate it."
- Run another fresh-agent dry eval after the cleanup.

## Raw Evidence

- Fresh-agent dry report in Codex thread for prompts covering check-in, upload, frontend-first account connection, agent-first frontend login, upgrade, and comment/reply.
