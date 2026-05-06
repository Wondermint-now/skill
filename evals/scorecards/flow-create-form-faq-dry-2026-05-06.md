# Wondermint Skill Scorecard

## Version

- Version/tag: post-`v0.1.2`
- Commit: `9c48b72`
- Date: 2026-05-06
- Evaluator: Codex dry review with skill-creator guidance
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep the create form FAQ.
- Release blocking issues: none.

## Scenarios

| Prompt | Expected behavior | Result | Score | Evidence |
|---|---|---|---:|---|
| "What does Public Domain mean on the Wondermint create form?" | Explain that the user confirms the work is free of copyright and IP claims; map to `contract_type: public_domain`. | Pass | 3 | `skills/frontend.md` Create Form FAQ. |
| "Is Public Domain the same as making my upload public?" | Clearly separate visibility from rights; explain that private/public and license choice are independent. | Pass | 3 | `skills/frontend.md` Create Form FAQ and Uploads section. |
| "What does Non-Exclusive Contract mean?" | Explain retained rights plus licensed commercial use according to terms; map to `contract_type: non_exclusive`. | Pass | 3 | `skills/frontend.md` Create Form FAQ. |
| "Why does the site make me pick 3 descriptors?" | Explain that descriptors classify the post; for REST uploads use matching valid Level 3 `subcategories`. | Pass | 3 | `skills/frontend.md` Create Form FAQ; `skills/flows/category-selection.md`. |
| "I chose Other for model. What should I type?" | Ask for and record the custom model name as the item model. | Pass | 3 | `skills/frontend.md` Create Form FAQ; `skills/flows/upload.md`. |
| "Can I edit the name or description after I tap Create?" | Do not promise frontend editability; advise reviewing name, description, model, prompt, tags, descriptors, visibility, and license before submission. | Pass | 3 | `skills/frontend.md` Create Form FAQ. |
| "Can I upload audio without a thumbnail?" | Explain audio/ZIP need useful cover images for browse grids; placeholder only with explicit user approval. | Pass | 3 | `skills/frontend.md` Create Form FAQ; `skills/flows/upload.md`. |

## Checks

- Router check: pass. `SKILL.md` routes website/frontend questions to
  `skills/frontend.md` and upload/category work to the relevant flows.
- Boundary check: pass. The FAQ is user-facing; no eval or repo-development
  workflow guidance was added to installable docs.
- REST-only check: pass. No GraphQL operations were added.
- Approval gate check: pass. The FAQ does not authorize upload, billing, or
  account mutations; upload flow still gates `POST /api/v1/agents/listings`.
- UX check: pass. Answers are short enough for direct user guidance and precise
  enough to avoid license/visibility confusion.
- Secret check: pass. No real credentials were added.

## What Worked

- The FAQ answers the common create-form questions without forcing the agent to
  load the repo-only screenshot reference.
- Public Domain versus public visibility is stated directly.
- The edit-lock answer prompts review before submission instead of promising
  post-create edits.

## What Confused The Agent

- No blocking confusion in this pass.

## Missing Context

- This was a dry review, not a live frontend walkthrough.
- The exact legal terms behind Non-Exclusive Contract and Public Domain remain
  product/legal policy, so the FAQ stays at the form-helper level.

## Recommended Changes

- No required changes.
- Next useful step: tag the current point as `v0.1.3` if the owner wants a
  version marker for the create-form guidance baseline.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: no.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: already completed in `9c48b72`.
- MVP scope check: no new endpoints were added.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or
  `/graphql` examples were added to skill docs.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No.

## Raw Evidence

- `SKILL.md`
- `skills/frontend.md`
- `skills/flows/upload.md`
- `skills/flows/category-selection.md`
