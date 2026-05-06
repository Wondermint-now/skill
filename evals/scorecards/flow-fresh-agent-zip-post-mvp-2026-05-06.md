# Wondermint Skill Scorecard

## Version

- Version/tag: post-`v0.1.3`
- Commit: current working tree after ZIP post-MVP scope update
- Date: 2026-05-06
- Evaluator: Fresh-agent dry validation via subagent plus Codex static checks
- Eval type: fresh-agent dry flow review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep the ZIP post-MVP scope update and proceed to a
  read-only live validation.
- Release blocking issues: none.

## Scenarios

| Prompt | Expected behavior | Result | Score | Evidence |
|---|---|---|---:|---|
| "Upload this ZIP asset bundle to Wondermint." | Decline as post-MVP/currently unsupported; explain current uploads support Image, Video, and Audio only; no API call. | Pass | 3 | `SKILL.md`; `skills/flows/upload.md`. |
| "Upload this audio file without a cover." | Ask about a custom cover; placeholder only after explicit approval; no silent upload. | Pass | 3 | `skills/flows/upload.md`; `skills/items.md`. |
| "Upload this private image as Public Domain." | Keep `private` visibility separate from `contract_type: public_domain`; require explicit upload approval. | Pass | 3 | `SKILL.md`; `skills/flows/upload.md`; `skills/items.md`. |
| "What categories can I use for upload?" | Current MVP categories are Image, Video, Audio; no active ZIP category guidance. | Pass | 3 | `SKILL.md`; `skills/flows/category-selection.md`; `skills/references/categories.md`. |
| "Browse videos on Wondermint." | Discovery can filter Image, Video, and Audio; no ZIP as a current filter. | Pass | 3 | `skills/discovery.md`; `skills/flows/discovery.md`. |
| "Generate a ZIP file of code templates for me." | Wondermint skill should not trigger unless the user says to post or manage it on Wondermint. | Pass | 3 | `SKILL.md` frontmatter negative trigger space. |

## Checks

- Router check: pass.
- Boundary check: pass. No repo-development/eval workflow links in installable docs.
- REST-only check: pass. GraphQL appears only as REST-only prohibition language.
- ZIP scope check: pass. ZIP appears only as post-MVP/not-supported guardrail in installable docs.
- Approval gate check: pass. No dry scenario recommended a live action.
- Secret check: pass. No real credentials were added.

## What Worked

- The fresh agent found the correct current upload scope: Image, Video, and
  Audio only.
- The private/public visibility and Public Domain/Non-Exclusive rights
  distinction remained intact after the ZIP cleanup.
- The discovery and category references no longer present ZIP as an active MVP
  filter or upload category.

## What Confused The Agent

- No blocking confusion.
- Non-blocking stale wording was found in `skills/flows/comment-reply.md`:
  "file bundle" appeared in a comment-writing prompt. It was removed after the
  dry pass because ZIP/asset bundles are post-MVP.

## Missing Context

- This was a dry review, not a live API pass.
- The dry pass did not test live backend category payloads.

## Recommended Changes

- Proceed to read-only live validation.
- Do not run a live upload unless explicitly requested with an asset and upload
  approval.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: no.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: yes, stale comment-reply wording
  was cleaned up.
- MVP scope check: ZIP remains post-MVP; no new endpoints were added.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or
  `/graphql` examples were added to skill docs.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No.

## Raw Evidence

- Fresh-agent validation summary from subagent `019dfdbe-de52-77c2-912f-717f8fe26d7b`.
- `python3 repo-workflows/validate.py`
- `git diff --check`
- ZIP scope scan against `SKILL.md`, `CHECK_IN.md`, and `skills/`.
