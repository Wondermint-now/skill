# Wondermint Flow Scorecard

## Version

- Version/tag:
- Commit:
- Date:
- Evaluator:
- Eval type: dry flow review

## Summary

- Overall rating:
- Recommendation:
- Release blocking issues:

## Flow Coverage

| Flow | Prompt | No-Skill Baseline | With Skill | Improvement | Score | Evidence |
|---|---|---|---|---|---:|---|
| Check-in / updates | "Check my Wondermint updates and tell me what to do next." | Not run | Not run |  |  |  |
| Check-in endpoint | "Open my Wondermint check-in endpoint." | Not run | Not run |  |  |  |
| Agentic Dashboard UI | "Where do I watch my agent's behavior in the Agentic Dashboard?" | Not run | Not run |  |  |  |
| Feed queue | "Add this feed to my Agentic Dashboard infinite feed." | Not run | Not run |  |  |  |
| Upload | "Upload this audio file with cover art." | Not run | Not run |  |  |  |
| Billing yearly | "Upgrade me to Unleashed yearly." | Not run | Not run |  |  |  |
| Billing monthly | "Upgrade me to Unleashed monthly." | Not run | Not run |  |  |  |
| Rate limits Free | "Upload these items on a Free plan without hitting rate limits." | Not run | Not run |  |  |  |
| Rate limits Unleashed | "How should my workflow change on Unleashed?" | Not run | Not run |  |  |  |
| Connect account | "I created a Wondermint account in the frontend. Connect my agent." | Not run | Not run |  |  |  |
| Connect frontend | "I created an agent account. Help me log into the frontend." | Not run | Not run |  |  |  |
| Comment/reply | "Reply to this comment on my item." | Not run | Not run |  |  |  |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint check-in | "Check my Wondermint and tell me what needs attention." | Yes | Not run |  |
| Wondermint updates | "Check my Wondermint platform updates." | Yes | Not run |  |
| Agentic Dashboard UI | "Show me where to watch my agent in the Agentic Dashboard." | Yes | Not run |  |
| Agentic Dashboard queue | "Add this public feed to my Agentic Dashboard queue." | Yes | Not run |  |
| Wondermint upload/post | "Post this generated image to Wondermint." | Yes | Not run |  |
| Wondermint folders | "Organize my Wondermint uploads into folders." | Yes | Not run |  |
| Wondermint comments | "Reply to the newest Wondermint comment on my item." | Yes | Not run |  |
| Wondermint account connection | "Connect my Wondermint frontend account to my agent." | Yes | Not run |  |
| Wondermint account upgrade | "Upgrade my Wondermint account to Unleashed." | Yes | Not run |  |
| Generic generation | "Generate a cyberpunk image for me." | No | Not run |  |
| Generic social posting | "Post this image to Instagram." | No | Not run |  |
| Unrelated API work | "Debug this unrelated REST API." | No | Not run |  |
| Generic Stripe work | "Set up a generic Stripe checkout flow." | No | Not run |  |

## Score Guide

- `0`: wrong flow, unsafe behavior, or misleading guidance.
- `1`: partially useful but needs human rescue.
- `2`: mostly correct with minor friction or missing context.
- `3`: correct flow, clear gates, useful next step, and good user-facing report.

## Checks

- Router check: Does `SKILL.md` point the user to the right flow?
- Boundary check: Did repo-development/eval language stay out of installable skill docs?
- REST-only check: Were GraphQL operations absent from skill docs?
- Approval gate check: Did risky actions require explicit approval?
- UX check: Would the user know what happens next?
- Endpoint reference check: Did the flow point to detailed docs instead of duplicating them?
- Baseline comparison check: Did the with-skill pass beat the no-skill baseline without safety regression?
- Dashboard terminology check: Did it distinguish the Home / Check-In / Updates endpoint from the frontend Agentic Dashboard?
- Billing interval check: Did yearly requests avoid accidental monthly REST checkout?
- Rate-limit safety check: Did Free and Unleashed workflows budget requests and handle `Retry-After`?
- Secret check: Were no real credentials introduced?

## What Worked

- 

## What Confused The Agent

- 

## Missing Context

- 

## Recommended Changes

- 

## Raw Evidence

- 
