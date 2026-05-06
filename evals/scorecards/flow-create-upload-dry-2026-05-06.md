# Wondermint Skill Scorecard

## Version

- Version/tag: post-`v0.1.2`
- Commit: `c235bb4`
- Date: 2026-05-06
- Evaluator: Codex dry review with skill-creator guidance
- Eval type: dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep the updated create/upload frontend guidance.
- Release blocking issues: none.

## Scenarios

| Prompt | Expected behavior | Result | Score | Evidence |
|---|---|---|---:|---|
| "I am on Create Your Item. I uploaded an image, picked Public Domain, and the site asks me to Pick 3. What should I do?" | Route to frontend/upload/category guidance; explain `Add Media*`, `License*` -> `public_domain`, and "Pick 3" as Level 3 descriptors. Keep public/private separate. | Pass | 3 | `skills/frontend.md`; `skills/flows/upload.md`; `skills/flows/category-selection.md`. |
| "Upload this image privately, but choose Public Domain for the license." | Treat `private` and `contract_type=public_domain` as separate settings; require approval before `POST /listings`. | Pass | 3 | `SKILL.md` Before You Upload; `skills/flows/upload.md` Phase 2 and Phase 3. |
| "I selected Video and chose Other for the model. The model was Veo 3. Help me upload it." | Capture custom model name, gather/validate descriptors, show approval summary with model before upload. | Pass | 3 | `skills/flows/upload.md` frontend mapping and Phase 3 approval summary. |
| "I am uploading audio from the website. It asks for a thumbnail. Can we skip it?" | Explain audio needs a custom cover for browse grids; can proceed with placeholder only if user explicitly approves. | Pass | 3 | `skills/flows/upload.md` Non-Negotiable Gates and Phase 1. |
| "The frontend says text cannot be edited after create. Can we change the title later?" | Do not promise frontend editability; report that title/name is locked after upload and warn before submission. | Pass | 3 | `skills/frontend.md` upload section; `skills/flows/upload.md` frontend warning and final report. |
| "The descriptor list says Mood. Should I send Mood as a subcategory?" | Reject Level 2 group headings; send only valid Level 3 values. | Pass | 3 | `skills/flows/category-selection.md`; `SKILL.md` Upload Taxonomy Rule. |

## Checks

- Router check: pass. `SKILL.md` routes upload and category questions to
  `skills/flows/upload.md` and `skills/flows/category-selection.md`.
- Boundary check: pass. Full screenshot extraction stays in
  `references/frontend/create-upload.md`; installable docs contain concise
  user-facing guidance.
- REST-only check: pass. No GraphQL operations were added.
- Approval gate check: pass. Upload still requires explicit approval before
  `POST /api/v1/agents/listings`.
- UX check: pass. The user can map frontend labels to API decisions without
  being told to browse the frontend through the agent.
- Endpoint reference check: pass. Detailed endpoint behavior stays in existing
  item/category docs.
- Secret check: pass. No real credentials were added.

## What Worked

- The frontend labels are now available where users naturally ask about them:
  `Create Your Item`, `Add Media*`, `Thumbnail`, `License*`, and "Pick 3 that
  describe your post".
- The upload flow explicitly captures custom `Other` model names.
- The rights/visibility distinction is preserved for the common case where a
  private upload still uses Public Domain or Non-Exclusive rights.

## What Confused The Agent

- No blocking confusion in this pass.
- There is a small product-language tension: the frontend asks for exactly 3
  descriptors, while the REST API guidance allows 1 to 5 Level 3
  `subcategories`. Current guidance resolves this by following frontend picks
  when provided and using approved Level 3 values for REST uploads.

## Missing Context

- This was a dry review, not a live upload.
- The screenshot set did not include ZIP model/descriptor behavior.
- The screenshot set did not show the private/public control, so this pass
  validates the existing skill rule rather than new frontend copy for that
  control.

## Recommended Changes

- No required changes before the next dry or live upload test.
- Optional future improvement: add a short user-facing frontend create FAQ for
  Public Domain vs Non-Exclusive, "Pick 3", custom model names, and edit locks.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: no.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: already completed in `c235bb4`.
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
- `references/frontend/create-upload.md`
