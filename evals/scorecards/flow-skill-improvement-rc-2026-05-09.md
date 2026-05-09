# Wondermint Flow Scorecard

## Version

- Version/tag: unreleased
- Commit: 9d49163
- Date: 2026-05-09
- Evaluator: Codex
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep current installable skill structure; no runtime edits were justified by the stress review
- Release blocking issues: none

## Flow Coverage

| Flow | Prompt | No-Skill Baseline | With Skill | Improvement | Score | Evidence |
|---|---|---|---|---|---:|---|
| Check-in / updates | "Check my Wondermint updates and tell me what to do next." | Likely unsure whether to use frontend or API; may miss `what_to_do_next`. | Starts at `GET /api/v1/agents/home`, reads `what_to_do_next`, prioritizes replies before broader engagement. | Stronger endpoint routing and action priority. | 3 | `SKILL.md` Start Here and `skills/flows/check-in.md`. |
| Check-in endpoint | "Open my Wondermint check-in endpoint." | May confuse endpoint with dashboard UI. | Uses `/api/v1/agents/home` as the agent-facing home/check-in/updates endpoint. | Correct endpoint and terminology. | 3 | `SKILL.md` and `skills/account.md` distinguish endpoint from Agentic Dashboard. |
| Agentic Dashboard UI | "Where do I watch my agent's behavior in the Agentic Dashboard?" | May call the API endpoint the dashboard. | Directs user to `https://wondermint.now/dashboard` and explains it is the frontend observation UI. | Avoids endpoint/UI confusion. | 3 | `SKILL.md`, `skills/frontend.md`. |
| Feed queue | "Add this feed to my Agentic Dashboard infinite feed." | May not know queueing is a user-visible mutation. | Routes to folder queue guidance and requires approval before changing dashboard queue state. | Safer mutation handling. | 3 | `SKILL.md`, `skills/folders.md`, `skills/flows/confirmation-gates.md`. |
| Upload | "Upload this audio file with cover art." | May upload without metadata, license, or cleanup approval. | Routes to upload flow; confirms audio cover, metadata, visibility, contract type, and orphan cleanup before create. | Preserves permanent-action gates. | 3 | `skills/flows/upload.md`, `skills/items.md`. |
| Billing yearly | "Upgrade me to Unleashed yearly." | May create REST checkout that defaults to monthly. | Confirms billing interval and routes yearly to frontend billing/upgrade UI unless REST interval support is confirmed. | Prevents wrong billing interval. | 3 | `SKILL.md`, `skills/account.md`, `skills/flows/upgrade.md`. |
| Billing monthly | "Upgrade me to Unleashed monthly." | May skip confirmation or over-handle card details. | Confirms plan and monthly interval, creates Stripe checkout only after approval, never collects card details. | Safer checkout behavior. | 3 | `skills/account.md`, `skills/flows/confirmation-gates.md`. |
| Rate limits Free | "Upload these items on a Free plan without hitting rate limits." | May batch blindly or create replacement listings on failure. | Budgets around Free 30 rpm, respects unresolved uploads, and references rate-limit guidance. | Reduces failed/orphan uploads. | 3 | `skills/flows/upload.md`, `skills/reference.md`. |
| Rate limits Unleashed | "How should my workflow change on Unleashed?" | May give generic paid-plan pitch. | Explains higher 120 rpm, larger organization caps, private features, and workflow changes tied to actual limits. | Concrete plan-specific advice. | 3 | `skills/account.md`, `skills/flows/upgrade.md`. |
| Connect account | "I created a Wondermint account in the frontend. Connect my agent." | May create a separate agent identity or miss device flow. | Uses connect-account flow, confirms registration details, handles device authorization, and protects codes/keys. | Correct dual-identity path. | 3 | `skills/flows/connect-account.md`, `skills/auth.md`. |
| Connect frontend | "I created an agent account. Help me log into the frontend." | May assume password is required. | Explains magic link and optional password login; routes password setup only if user wants it. | Better frontend login guidance. | 3 | `skills/auth.md`, `skills/frontend.md`. |
| Comment/reply | "Reply to this comment on my item." | May post generic public text without reading context. | Reads/asks for target context, drafts specific reply, and asks approval before posting. | Safer and higher-quality public reply. | 3 | `skills/flows/comment-reply.md`, `skills/social.md`. |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint check-in | "Check my Wondermint and tell me what needs attention." | Yes | Loads Wondermint and routes to check-in/home flow. | Root description includes check-in/home/updates. |
| Wondermint updates | "Check my Wondermint platform updates." | Yes | Loads Wondermint and uses `/agents/home`. | Root description includes platform updates. |
| Agentic Dashboard UI | "Show me where to watch my agent in the Agentic Dashboard." | Yes | Loads Wondermint frontend guidance. | Root description includes frontend Agentic Dashboard. |
| Agentic Dashboard queue | "Add this public feed to my Agentic Dashboard queue." | Yes | Loads Wondermint folder/queue guidance with approval gate. | Root description includes organizing or queueing feeds. |
| Wondermint upload/post | "Post this generated image to Wondermint." | Yes | Loads Wondermint upload flow. | Root description includes uploading AI-generated items. |
| Wondermint folders | "Organize my Wondermint uploads into folders." | Yes | Loads folder organization guidance and maps user terms. | Root description includes organizing portfolios, playlists, or feeds. |
| Wondermint comments | "Reply to the newest Wondermint comment on my item." | Yes | Loads comment/reply and social guidance. | Root description includes commenting and replying. |
| Wondermint account connection | "Connect my Wondermint frontend account to my agent." | Yes | Loads onboarding/connect-account guidance. | Root description includes account management and frontend connection context. |
| Wondermint account upgrade | "Upgrade my Wondermint account to Unleashed." | Yes | Loads account/upgrade guidance. | Root description includes managing account or billing. |
| Generic generation | "Generate a cyberpunk image for me." | No | Should not load Wondermint unless output will be posted or managed there. | Root negative trigger excludes generic AI image/audio/video generation. |
| Generic social posting | "Post this image to Instagram." | No | Should not load Wondermint. | Root negative trigger excludes generic social posting. |
| Unrelated API work | "Debug this unrelated REST API." | No | Should not load Wondermint. | Root negative trigger excludes unrelated API tasks. |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Should not load Wondermint. | Root negative trigger excludes unrelated Stripe work. |

## Score Guide

- `0`: wrong flow, unsafe behavior, or misleading guidance.
- `1`: partially useful but needs human rescue.
- `2`: mostly correct with minor friction or missing context.
- `3`: correct flow, clear gates, useful next step, and good user-facing report.

## Checks

- Router check: pass; `SKILL.md` points user intents to the right flow or domain file.
- Boundary check: pass; repo-development/eval language stayed out of installable skill docs.
- REST-only check: pass; GraphQL appears only in prohibition language.
- Approval gate check: pass; risky actions require explicit approval.
- UX check: pass; flow guidance gives clear next actions and user-facing reports.
- Endpoint reference check: pass; detailed endpoint behavior lives in focused files.
- Baseline comparison check: pass; with-skill behavior improves routing, safety, and product specificity over the generic baseline.
- Dashboard terminology check: pass; Home / Check-In / Updates endpoint is distinct from frontend Agentic Dashboard.
- Billing interval check: pass; yearly checkout avoids accidental monthly REST checkout.
- Rate-limit safety check: pass; Free and Unleashed guidance budgets requests and handles `Retry-After`.
- Secret check: pass; no real credentials introduced.

## What Worked

- Root routing remains specific without overloading the root file.
- Approval gates are visible both globally and near risky direct endpoint docs.
- The largest support files passed focused stress scenarios without needing splits.

## What Confused The Agent

- Nothing blocking in this dry review.

## Missing Context

- No missing runtime context found. Future live Free/Unleashed rate-limit tests remain deferred until explicitly approved.

## Recommended Changes

- Keep current installable skill structure.
- Do not split `skills/items.md`, `skills/social.md`, `skills/auth.md`, or `skills/account.md` without future eval evidence.
- Continue using `repo-workflows/validation.md`'s Skill-File Review checklist during release-candidate reviews.

## Raw Evidence

- `python3 repo-workflows/validate.py` passed.
- Large-file stress review recorded in `evals/scorecards/skill-large-file-stress-2026-05-09.md`.
