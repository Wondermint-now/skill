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

| Flow | Prompt | Result | Score | Evidence |
|---|---|---|---:|---|
| Check-in | "Check my Wondermint and tell me what needs attention." | Not run |  |  |
| Upload | "Upload this audio file with cover art." | Not run |  |  |
| Upgrade | "Upgrade me to Unleashed." | Not run |  |  |
| Connect account | "I created a Wondermint account in the frontend. Connect my agent." | Not run |  |  |
| Connect frontend | "I created an agent account. Help me log into the frontend." | Not run |  |  |
| Comment/reply | "Reply to this comment on my item." | Not run |  |  |

## Trigger Coverage

| Trigger | Prompt | Should Load | Result | Evidence |
|---|---|---:|---|---|
| Wondermint check-in | "Check my Wondermint and tell me what needs attention." | Yes | Not run |  |
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
