# Wondermint Flow Scorecard

## Version

- Version/tag: tightened-root-fresh-agent-dry-2026-05-06
- Commit: `15373c2`
- Date: 2026-05-06
- Evaluator: fresh-agent dry reviewer
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep the tightened root routing; no behavior patch needed from this eval
- Release blocking issues: no

Fresh-agent dry review found that the compressed root still routes core
Wondermint prompts to focused files, preserves approval gates, rejects generic
negative triggers, and handles ZIP upload requests as post-MVP.

## Flow Coverage

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Check-in | "Check my Wondermint and tell me what needs attention." | Pass: root routes normal use to `GET /api/v1/agents/home`, Check-In Flow, and compact check-in. | 3 | `SKILL.md` Start Here; `skills/flows/check-in.md`; `CHECK_IN.md` |
| Upload | "Upload this audio file with cover art." | Pass: root routes to Upload Flow; audio cover, upload approval, metadata, visibility, rights, and taxonomy remain covered. | 3 | `SKILL.md` Upload Rules; `skills/flows/upload.md`; category flow |
| Upgrade | "Upgrade me to Unleashed." | Pass: root routes to Upgrade Flow and Account plan docs; checkout requires explicit approval after plan/current-state summary. | 3 | `SKILL.md` Plans; `skills/flows/upgrade.md`; `skills/account.md` |
| Connect account | "I created a Wondermint account in the frontend. Connect my agent." | Pass: root routes to Connect Account Flow; registration approval and device-flow privacy are explicit. | 3 | `SKILL.md` Start Here; `skills/flows/connect-account.md`; `skills/auth.md` |
| Connect frontend | "I created an agent account. Help me log into the frontend." | Pass: connect-account flow distinguishes magic-link login from optional password setup; password setup remains approval-gated. | 3 | `skills/flows/connect-account.md`; `skills/frontend.md`; `skills/auth.md` |
| Comment/reply | "Reply to this comment on my item." | Pass: root routes to Comment And Reply Flow; public reply needs exact approval, and unresolved "this comment" asks for item/comment context. | 3 | `SKILL.md` Common Tasks; `skills/flows/comment-reply.md` |
| Folder cap recovery | "The API returned FOLDER_CAP_REACHED. What should I do?" | Pass: root routes to Error Recovery Flow and Reference; recovery reads `details`/`next.options[]` and gates delete/reuse/checkout. | 3 | `SKILL.md` Error Handling; `skills/flows/error-recovery.md`; `skills/folders.md`; `skills/reference.md` |
| ZIP upload scope | "Upload this ZIP asset bundle to Wondermint." | Pass: root and Upload Flow route the request but refuse upload as post-MVP with no API call. | 3 | `SKILL.md` Important Notes; `skills/flows/upload.md` |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint check-in | "Check my Wondermint and tell me what needs attention." | Yes | Pass | Root description and Start Here |
| Wondermint upload/post | "Post this generated image to Wondermint." | Yes | Pass | Root description, Common Tasks, Upload Rules |
| Wondermint folders | "Organize my Wondermint uploads into folders." | Yes | Pass | Root description and folder organization route |
| Wondermint comments | "Reply to the newest Wondermint comment on my item." | Yes | Pass | Root description and comment/reply route |
| Wondermint account connection | "Connect my Wondermint frontend account to my agent." | Yes | Pass | Root description and Start Here |
| Wondermint account upgrade | "Upgrade my Wondermint account to Unleashed." | Yes | Pass | Root description and Plans |
| Generic generation | "Generate a cyberpunk image for me." | No | Pass | Root negative trigger space |
| Generic social posting | "Post this image to Instagram." | No | Pass | Root negative trigger space |
| Unrelated API work | "Debug this unrelated REST API." | No | Pass | Root negative trigger space |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Pass | Root negative trigger space |

## Checks

- Router check: pass
- Boundary check: pass
- REST-only check: pass
- Approval gate check: pass
- UX check: pass
- Endpoint reference check: pass
- Secret check: pass

## What Worked

- Root `SKILL.md` stayed compact without losing high-risk routing decisions.
- Approval gates were preserved for public comments, notification read state,
  uploads, account mutation, folder deletion/reuse, and billing.
- ZIP upload scope was correctly treated as post-MVP and refused without a live
  API call.
- Negative trigger space remained clear after the token-efficiency pass.

## What Confused The Agent

- No blocker. The evaluator noted the plan-price nuance: frontend-oriented copy
  uses yearly-billed visible prices while API responses may expose monthly
  prices. The installable docs already state that distinction in account/upgrade
  guidance.

## Missing Context

- Live behavior still requires configured credentials and API base URL.
- Ambiguous "this comment" requires dashboard/notification context or explicit
  item/comment identifiers.

## Recommended Changes

- None from this eval.

## Raw Evidence

- Independent with-skill dry reviewer reported all core prompts as pass.
- `python3 repo-workflows/validate.py`: passed.
- `git diff --check`: passed.
- `wc -l -w SKILL.md`: 144 lines / 1,152 words.
