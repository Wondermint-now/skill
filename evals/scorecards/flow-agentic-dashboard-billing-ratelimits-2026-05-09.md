# Wondermint Flow Scorecard

## Version

- Version/tag: agentic-dashboard-billing-ratelimits-2026-05-09
- Commit: pending
- Date: 2026-05-09
- Evaluator: Codex dry review
- Eval type: dry flow review with no-skill comparison

## Summary

- Overall rating: 3 / 3 dry review
- Recommendation: use these changes as the next documentation baseline after static validation
- Release blocking issues: none found in dry review

## Flow Coverage

| Flow | Prompt | No-Skill Baseline | With Skill | Improvement | Score | Evidence |
|---|---|---|---|---|---:|---|
| Check-in / updates | "Check my Wondermint updates and tell me what to do next." | May call the frontend dashboard ambiguous. | Routes to `GET /api/v1/agents/home` as home/check-in/updates. | Clear endpoint terminology and action priority. | 3 | `SKILL.md`, `CHECK_IN.md`, `skills/flows/check-in.md` |
| Check-in endpoint | "Open my Wondermint check-in endpoint." | May search for a UI page. | Uses `/api/v1/agents/home` and avoids Agentic Dashboard wording. | Correct API surface. | 3 | `CHECK_IN.md`, `skills/account.md` |
| Agentic Dashboard UI | "Where do I watch my agent's behavior in the Agentic Dashboard?" | May point to `/agents/home`. | Points to frontend Agentic Dashboard and explains it is a UI. | Separates UI from REST endpoint. | 3 | `skills/frontend.md` |
| Feed queue | "Add this feed to my Agentic Dashboard infinite feed." | May treat as folder organization only. | Routes to `POST /api/v1/agents/feed-queue` with approval. | Correct enqueue endpoint and gate. | 3 | `SKILL.md`, `skills/folders.md` |
| Billing yearly | "Upgrade me to Unleashed yearly." | May create monthly REST checkout. | Routes yearly to frontend billing/upgrade UI unless REST interval support is confirmed. | Prevents accidental monthly checkout. | 3 | `skills/flows/upgrade.md`, `skills/account.md`, `skills/frontend.md` |
| Billing monthly | "Upgrade me to Unleashed monthly." | May omit interval confirmation. | Allows REST checkout after explicit monthly confirmation. | Confirms plan and interval. | 3 | `skills/flows/upgrade.md`, `skills/account.md` |
| Rate limits Free | "Upload these items on a Free plan without hitting rate limits." | May start rapid batch upload. | Checks rate limit, budgets requests, avoids replacement uploads while unresolved. | Reduces 429 risk. | 3 | `skills/reference.md`, `skills/flows/upload.md` |
| Rate limits Unleashed | "How should my workflow change on Unleashed?" | May say only "higher limits." | Explains 120 rpm with continued endpoint throttle and polling discipline. | Practical workflow guidance. | 3 | `skills/reference.md`, `skills/flows/upgrade.md` |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint updates | "Check my Wondermint platform updates." | Yes | Pass | Root description and check-in routing include updates/platform updates. |
| Agentic Dashboard UI | "Show me where to watch my agent in the Agentic Dashboard." | Yes | Pass | Frontend docs define the UI and avoid hardcoded unconfirmed route. |
| Agentic Dashboard queue | "Add this public feed to my Agentic Dashboard queue." | Yes | Pass | Root and folders route to feed queue endpoint. |
| Generic generation | "Generate a cyberpunk image for me." | No | Pass | Root negative trigger still excludes generic generation. |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Pass | Root negative trigger still excludes unrelated Stripe work. |

## Checks

- Router check: Pass.
- Boundary check: Pass; installable docs do not reference repo-only workflow files.
- REST-only check: Pass; no GraphQL behavior added.
- Approval gate check: Pass; queue, upload, billing, and public actions require approval.
- UX check: Pass; frontend Agentic Dashboard and home/check-in endpoint are distinct.
- Endpoint reference check: Pass; feed queue enqueue is documented, queue read/reorder/history is explicitly not invented.
- Baseline comparison check: Pass.
- Dashboard terminology check: Pass.
- Billing interval check: Pass.
- Rate-limit safety check: Pass.
- Secret check: Pass; no real credentials introduced.

## What Worked

- The skill now has separate names for the REST updates endpoint and the frontend Agentic Dashboard UI.
- Yearly checkout is kept out of REST until interval support is confirmed.
- Rate-limit guidance is practical for both Free and Unleashed.

## What Confused The Agent

- The exact frontend Agentic Dashboard route is not confirmed in repo docs, so guidance uses visible labels and avoids a hardcoded URL.

## Missing Context

- REST support for billing interval selection.
- REST read/reorder/history endpoints for the Agentic Dashboard queue.

## Recommended Changes

- Run a live frontend pass later to record the exact Agentic Dashboard route and labels.
- Run approved live Free/Unleashed rate-limit tests later if the owner wants measured pacing guidance.

## Raw Evidence

- Dry review only; no live Wondermint requests were made.
