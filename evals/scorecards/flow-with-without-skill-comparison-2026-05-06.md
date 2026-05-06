# Wondermint With-Skill Versus Without-Skill Comparison

## Version

- Version/tag: with-without-skill-comparison-2026-05-06
- Commit: `15373c2`
- Date: 2026-05-06
- Evaluator: paired dry reviewers
- Eval type: with-skill versus no-skill dry comparison

## Summary

- Overall rating: 3 / 3
- Recommendation: the Wondermint skill materially improves routing, safety, and
  product-specific decisions versus a generic agent baseline
- Release blocking issues: no

The no-skill baseline understood broad user intent but missed Wondermint's
specific API routing, account-linking flow, folder-cap recovery details, upload
metadata/licensing conventions, ZIP post-MVP scope, and approval boundaries.
The with-skill review routed those same prompts to focused files with explicit
approval gates and scope handling.

## Scenario Comparison

| Prompt | No-skill baseline | With Wondermint skill | Improvement |
|---|---|---|---|
| "Check my Wondermint and tell me what needs attention." | Likely asks for credentials, screenshots, or vague access; does not know the `/home` dashboard priority model. | Routes to `GET /api/v1/agents/home`, Check-In Flow, `what_to_do_next`, and notification cross-checks. | Clear read-only start point and triage order. |
| "Upload this audio file with cover art." | Treats as generic upload; may miss cover, metadata, visibility, license, taxonomy, and public-post approval. | Routes to Upload Flow; requires cover handling, metadata draft, visibility/rights separation, taxonomy, and explicit approval. | Prevents accidental public or under-specified upload. |
| "Upgrade me to Unleashed." | Gives generic subscription guidance; may not know current plan check, Wondermint plan codes, or Stripe handoff. | Routes to Upgrade Flow and Account plans; checks current state and confirms before checkout. | Correct paid-action gate and plan context. |
| "I created a Wondermint account in the frontend. Connect my agent." | Likely asks for secrets or generic login details; does not know device-flow connection. | Routes to Connect Account Flow; confirms email/username, starts frontend-first registration, shows only user-facing approval values. | Safe account-linking convention. |
| "I created an agent account. Help me log into the frontend." | Gives generic login troubleshooting; may confuse agent key with browser login. | Routes to agent-first connect flow; defaults to magic link, gates optional password setup. | Separates API identity from frontend login. |
| "Reply to this comment on my item." | May draft a reply without knowing item/comment lookup or public approval expectations. | Routes to Comment And Reply Flow; reads context first, asks for unresolved identifiers, and requires exact approval. | Preserves public-action safety. |
| "The API returned FOLDER_CAP_REACHED. What should I do?" | Guesses delete or upgrade; may miss plan details, shared caps, `next.options[]`, and approval before deletion/checkout. | Routes to Error Recovery/Folders; reads `details` and `next.options[]`, explains delete/reuse/upgrade, and gates all mutations. | Product-specific recovery without destructive shortcuts. |
| "Upload this ZIP asset bundle to Wondermint." | Treats ZIP as a generic upload and may attempt to process or upload hidden/bundled files. | Routes to upload scope and refuses ZIP as post-MVP; no API call. | Prevents unsupported upload. |

## Negative Trigger Comparison

| Prompt | No-skill baseline | With Wondermint skill | Result |
|---|---|---|---|
| "Generate a cyberpunk image for me." | Generic image-generation task. | Root description excludes generic generation unless Wondermint posting/management is requested. | Pass |
| "Post this image to Instagram." | Generic social/Instagram task. | Root description excludes generic social posting unless Wondermint is target. | Pass |
| "Debug this unrelated REST API." | Generic API debugging. | Root description excludes unrelated API tasks. | Pass |
| "Set up a generic Stripe checkout flow." | Generic Stripe integration. | Root description excludes unrelated Stripe work. | Pass |

## Checks

- With-skill behavior routes to focused flow/reference files: pass
- No-skill baseline lacks Wondermint object model and workflow details: confirmed
- Approval gates are a material skill benefit: confirmed
- Negative trigger space remains useful: confirmed
- Static validation: pass

## What Worked

- The tightened root still teaches the highest-value first moves: start with
  `/home`, route uploads through approval, use device-flow account connection,
  trust structured error recovery, and refuse unsupported ZIP uploads.
- The skill adds concrete safety boundaries that a generic agent would likely
  apply inconsistently.

## What Confused The Agent

- No blocker. Baseline evaluator overestimated possible generic knowledge around
  "folder-feed queue" and manual website actions, which reinforces that the
  skill-specific object model is needed.

## Missing Context

- This is a dry comparison. It does not prove live endpoint availability or
  credential behavior.

## Recommended Changes

- None from this comparison.

## Raw Evidence

- No-skill baseline reviewer predicted missing routing, metadata, account-linking,
  folder-cap, ZIP-scope, and approval behavior.
- With-skill reviewer found all core prompts routed correctly with no release
  blockers.
- `python3 repo-workflows/validate.py`: passed.
- `git diff --check`: passed.
