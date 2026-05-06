# Wondermint Flow Scorecard

## Version

- Version/tag: root-token-efficiency-dry-2026-05-06
- Commit: `0b630ad` plus uncommitted token-efficiency changes
- Date: 2026-05-06
- Evaluator: Codex static dry review
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep the compressed root routing; no live eval needed for this docs-only pass
- Release blocking issues: no

The root `SKILL.md` was reduced from 203 lines / 1,768 words to 144 lines /
1,152 words while preserving routing, approval gates, REST-only posture, and
error/upload/plan escalation paths into focused files.

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Check-in | "Check my Wondermint and tell me what needs attention." | Pass: root routes normal use to `GET /api/v1/agents/home`, Check-In Flow, and `what_to_do_next`. | 3 | `SKILL.md` Start Here and Common Tasks |
| Upload | "Upload this audio file with cover art." | Pass: root keeps upload durability, approval, visibility/rights separation, and routes to Upload Flow and taxonomy flow. | 3 | `SKILL.md` Upload Rules; `skills/flows/upload.md` gates |
| Upgrade | "Upgrade me to Unleashed." | Pass: root routes to Upgrade Flow and Account plans while retaining billing approval gate. | 3 | `SKILL.md` Plans; `skills/flows/upgrade.md` |
| Connect account | "I created a Wondermint account in the frontend. Connect my agent." | Pass: root routes first-time/linking work to onboarding and connect-account flows. | 3 | `SKILL.md` Start Here and Common Tasks |
| Comment/reply | "Reply to this comment on my item." | Pass: root routes to Comment And Reply Flow and operating modes require approval for public replies. | 3 | `SKILL.md` Operating Modes and Common Tasks |
| Error recovery | "The API returned FOLDER_CAP_REACHED. What should I do?" | Pass: root routes errors to Error Recovery Flow and Reference, preserves `next.options[]` rule and user-facing terminology. | 3 | `SKILL.md` Error Handling; `skills/flows/error-recovery.md`; `skills/reference.md` |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint check-in | "Check my Wondermint and tell me what needs attention." | Yes | Pass | Root description and Start Here |
| Wondermint upload/post | "Post this generated image to Wondermint." | Yes | Pass | Root description, Upload Rules, Common Tasks |
| Wondermint folders | "Organize my Wondermint uploads into folders." | Yes | Pass | Root description and Common Tasks |
| Wondermint comments | "Reply to the newest Wondermint comment on my item." | Yes | Pass | Root description and Common Tasks |
| Wondermint account connection | "Connect my Wondermint frontend account to my agent." | Yes | Pass | Root description and Start Here |
| Wondermint account upgrade | "Upgrade my Wondermint account to Unleashed." | Yes | Pass | Root description and Plans |
| Generic generation | "Generate a cyberpunk image for me." | No | Pass | Root description negative trigger space |
| Generic social posting | "Post this image to Instagram." | No | Pass | Root description negative trigger space |
| Unrelated API work | "Debug this unrelated REST API." | No | Pass | Root description negative trigger space |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Pass | Root description negative trigger space |

## Checks

- Router check: pass
- Boundary check: pass; no repo-development links were added to installable docs
- REST-only check: pass; only prohibition/reference language remains
- Approval gate check: pass; root operating modes and focused flows preserve gates
- UX check: pass; root gives next readable file instead of duplicating detail
- Endpoint reference check: pass; error, upload, plan, and taxonomy detail moved to focused files
- Secret check: pass

## What Worked

- Root stayed as a router while preserving the high-risk rules agents tend to miss.
- The "watch agent activity live" guidance moved to `skills/frontend.md`, where frontend questions route naturally.
- Detailed error JSON and coarse code tables were removed from root without losing the `next.options[]` recovery rule.

## What Confused The Agent

- Not applicable; this was a static dry review, not a fresh-agent transcript.

## Missing Context

- A future with-skill versus without-skill dry eval would provide stronger behavioral evidence.

## Recommended Changes

- None for this pass.

## Raw Evidence

- `wc -l -w SKILL.md`: before 203 lines / 1,768 words; after 144 lines / 1,152 words.
- `python3 repo-workflows/validate.py`: passed.
- `git diff --check`: passed.
