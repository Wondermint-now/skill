# Wondermint Skill Scorecard

## Version

- Version/tag:
- Commit:
- Date: 2026-05-08
- Evaluator: Codex

## Summary

- Overall rating: 3 / 3 for the scoped release-account pass, with operational upload and folder-save caveats captured
- Recommendation: Keep the test account for follow-on skill testing; installable skill docs have been updated from this pass.
- Release blocking issues: None found in the tested scope.

## Scenarios

| Scenario | Result | Score | Evidence |
|---|---|---:|---|
| Register or connect account | Passed | 3 | `evals/logs/release-account-2026-05-08/register.redacted.json` |
| Check in via home / check-in updates | Passed | 3 | `evals/logs/release-account-2026-05-08/home.redacted.json` |
| Upload item | Passed | 3 | `evals/logs/release-account-2026-05-08/image-upload-summary.json` |
| Choose categories/tags | Passed for taxonomy retrieval | 3 | `evals/logs/release-account-2026-05-08/categories.redacted.json` |
| Respond to notifications/comments | Not run |  | Not planned without explicit approval |
| Browse/discover and engage | Passed for read-only browse | 3 | `evals/logs/release-account-2026-05-08/marketplace.redacted.json` |
| Create feed and add items | Passed | 3 | `evals/logs/release-account-2026-05-08/dog-feed-summary.json` |
| Save public folders | Passed with status-code doc mismatch | 2 | `evals/logs/release-account-2026-05-08/folder-save-summary.json` |
| Bulk upload public images | Passed with operational caveats | 2 | `evals/logs/release-account-2026-05-08/bulk-image-upload-summary.json` |
| Add folders to frontend Agentic Dashboard queue | Passed | 3 | `evals/logs/release-account-2026-05-08/feed-queue-folder-summary.json` |
| Handle expected error path | Not run |  |  |

## What Worked

- New account registration returned `201 Created`; the one-time API key was saved only to ignored `.env`.
- Profile, home / check-in updates, categories, marketplace browse, and release frontend status checks all returned `200`.
- Public feed creation and adding 8 approved dog image listings worked through the documented folder endpoints.
- Public folder search found 4 folders with at least 3 items each, and all 4 save calls succeeded.
- Public-domain image upload reached `Minted`, and the source file was moved to the local `uploaded/` folder afterward.
- Bulk public-domain upload produced 6 successful `Minted` uploads while trying to satisfy a request for 5 because one initially unresolved upload later completed.
- Public folder search plus feed-queue enqueue worked for 4 folders with at least 15 items each.
- Sanitized evidence was generated without committed API keys, emails, UUIDs, device codes, passwords, tokens, or signed URLs.

## What Confused The Agent

- Local command lookup failed for bare `curl` and `python3` names inside the sourced-env shell. Absolute paths worked. This is a repo workflow/tooling issue, not a Wondermint API issue.
- Folder contents verification returned item names but did not expose `listing.listing_id` in the nested listing objects, despite prior folder docs implying that key would be present.
- Folder save returned `201` for each successful save; prior social docs said folder engagement writes return only `204 No Content`.
- Bulk upload needs more conservative orchestration: rate limits affected create/status/cleanup calls, and replacement uploads should wait for unresolved prior uploads before proceeding.
- Some confirmed uploads reached `Processing Failed` with no failure reason in the status response.
- The feed-queue agent REST enqueue endpoint is source-documented and now surfaced in installable skill docs; no agent REST read endpoint was found in the backend endpoint reference.

## Missing Context

- Still untested for this account: comments and replies, item/user likes and follows, password setup, frontend authenticated navigation, and expected error paths.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: Yes
- Static endpoint/schema/message docs updated: Not needed for this cleanup pass
- Skill docs updated from confirmed behavior: Yes, for folder-save success status, folder contents ID caveat, feed queue routing, upload rate limits, and frontend Agentic Dashboard terminology
- MVP scope check: No new endpoints added
- REST-only check: No GraphQL operations added
- Deferred follow-up: Consider hardening repo-only live-eval scripts against missing command names in `PATH`.

## Security And Credential Review

- Were any secrets exposed in committed files? No known exposure; committed evidence was scanned for API-key, email, and UUID patterns.
- Did the skill keep credentials limited to approved Wondermint domains? Yes; the API key was used only against `https://api-staging.fullstock.ai`.
- Any risky logging, screenshots, or transcript content? Raw responses stayed under ignored `.tmp/`; committed evidence is redacted.
- Validation note: `repo-workflows/validate.py` now skips ignored local `.env`
  files, so the requested local credential storage does not fail validation.

## Raw Evidence

- `evals/logs/release-account-2026-05-08/README.md`
- `evals/logs/release-account-2026-05-08/summary.json`
- `evals/logs/release-account-2026-05-08/register.redacted.json`
- `evals/logs/release-account-2026-05-08/me.redacted.json`
- `evals/logs/release-account-2026-05-08/home.redacted.json`
- `evals/logs/release-account-2026-05-08/categories.redacted.json`
- `evals/logs/release-account-2026-05-08/marketplace.redacted.json`
- `evals/logs/release-account-2026-05-08/dog-feed-summary.json`
- `evals/logs/release-account-2026-05-08/folder-save-summary.json`
- `evals/logs/release-account-2026-05-08/image-upload-summary.json`
- `evals/logs/release-account-2026-05-08/bulk-image-upload-summary.json`
