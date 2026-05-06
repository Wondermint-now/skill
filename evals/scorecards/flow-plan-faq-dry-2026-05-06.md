# Wondermint Skill Scorecard

## Version

- Version/tag: post-`v0.1.2`
- Commit: `f094ee8` plus local fixes in this pass
- Date: 2026-05-06
- Evaluator: Codex dry review with skill-creator guidance

## Summary

- Overall rating: 3 / 3 after fixes.
- Recommendation: keep current plan/FAQ/frontend guidance.
- Release blocking issues: none after updating root plan prices and FAQ MVP
  commerce caveat.

## Scenarios

| Prompt | Expected behavior | Result | Score | Evidence |
|---|---|---|---:|---|
| "What is Wondermint?" | Use FAQ copy, but do not imply active MVP buy/sell/trade agent behavior. | Pass after fix | 3 | `skills/frontend.md` FAQ now includes MVP caveat. |
| "How often is content updated?" | Answer daily with fresh boards, uploads, curated collections, and trending styles. | Pass | 3 | `skills/frontend.md` FAQ. |
| "Do students get a discount?" | Say yes; eligible students/teachers/education users can request special rate with proof. | Pass | 3 | `skills/frontend.md` FAQ. |
| "What payment methods do you accept?" | Say Stripe handles major cards, PayPal, and supported international methods. | Pass | 3 | `skills/frontend.md` FAQ. |
| "Can I cancel my subscription?" | Say yes; remains active until end of billing period; renewal stops. | Pass | 3 | `skills/frontend.md` FAQ and `skills/account.md`. |
| "How do I switch plans?" | Say upgrade from subscription settings; switch by canceling current plan and subscribing to new one. | Pass | 3 | `skills/frontend.md` FAQ. |
| "Do you offer refunds?" | Say no refunds; access remains through paid period after cancellation. | Pass | 3 | `skills/frontend.md` FAQ. |
| "Why should I upgrade to Unleashed?" | Mention concrete reasons: 2,000 analytics credits/month, 120 rpm, private assets, verified account, 8 portfolios, 10 playlists. | Pass | 3 | `skills/flows/upgrade.md`, `skills/account.md`. |
| "Why would I choose Genesis?" | Mention 5,000 analytics credits/month, 600 rpm, unlimited portfolios/playlists, founder/identity/community features. | Pass | 3 | `skills/flows/upgrade.md`, `skills/account.md`. |
| "Can you buy and sell on Wondermint right now?" | Explain plan/FAQ copy may mention selling, but MVP agent guidance must not treat marketplace transactions/offers as active. | Pass after fix | 3 | `skills/frontend.md`, `skills/flows/upgrade.md`. |

## What Worked

- FAQ answers are concise and directly available in the installable frontend
  guidance.
- Upgrade guidance uses visible frontend yearly prices and active plan benefits.
- Coming-soon marketplace/trade/advanced-analytics copy is recorded but not
  converted into active MVP skill behavior.

## What Confused The Agent

- Before the fix, root `SKILL.md` still had old compact plan prices (`$20`,
  `$99`), which could conflict with the visible frontend prices.
- The FAQ phrase "sell original digital content" needed a nearby MVP caveat so
  agents do not infer active marketplace transaction support.

## Missing Context

- This was a dry review, not a fresh-agent subagent run.
- The exact frontend billing checkout screen was not interactively tested.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: no.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: yes, `SKILL.md` root plan table
  and `skills/frontend.md` FAQ caveat.
- MVP scope check: no new endpoints were added.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or
  `/graphql` examples were added to skill docs.
- Deferred follow-up: optional fresh-agent validation for plan/FAQ prompts.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No.

## Raw Evidence

- `SKILL.md`
- `skills/frontend.md`
- `skills/account.md`
- `skills/flows/upgrade.md`
- `references/frontend/navigation-map.md`
