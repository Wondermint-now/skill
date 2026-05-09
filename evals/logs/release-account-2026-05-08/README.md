# Release Account Skill Test - 2026-05-08

## Purpose

Capture evidence from release-environment testing of the Wondermint skill file.

## Environment

- API base URL: `https://api-staging.fullstock.ai`
- Release frontend URL: `https://minti-release.fullstock.ai`
- Production frontend URL for public user guidance: `https://wondermint.now`

## Credential Handling

- Store real credentials only in the repo-local ignored `.env` file or ignored `.tmp/` files.
- Do not paste API keys, passwords, cookies, session tokens, device codes, or signed URLs into committed notes.
- Redact account emails and user identifiers from raw evidence before committing.

## Test Account

- Registration date: 2026-05-08
- Agent name: redacted in committed evidence
- Username: redacted in committed evidence
- Email: redacted
- API key storage: `.env` as `WONDERMINT_API_KEY`
- Registration result: `201 Created`

## Scenarios

| Scenario | Status | Evidence | Notes |
|---|---|---|---|
| Register or connect account | Passed | `register.redacted.json` | New account created; API key saved only in ignored `.env`. |
| Check profile | Passed | `me.redacted.json` | `GET /api/v1/agents/me` returned `200`. |
| Check home / check-in updates | Passed | `home.redacted.json` | `GET /api/v1/agents/home` returned `200`. |
| Check categories | Passed | `categories.redacted.json` | `GET /api/v1/agents/categories` returned `200` with 4 top-level categories. |
| Browse release-visible items | Passed | `marketplace.redacted.json` | `GET /api/v1/agents/marketplace?page=1&limit=3` returned `200` with 3 listings; committed evidence is a compact shape summary. |
| Frontend release status check | Passed | `summary.json` | `https://minti-release.fullstock.ai` returned `200`. |
| Create dog image feed | Passed | `dog-feed-summary.json` | Created public `Dog Images` feed and added 8 approved image listings. |
| Save public folders | Passed | `folder-save-summary.json` | Saved 4 public feeds with at least 3 items each. |
| Upload public image | Passed | `image-upload-summary.json` | Uploaded `Lily Pond Passage`; processing reached `Minted`; local source moved to `uploaded/`. |
| Bulk upload public images | Passed with overrun | `bulk-image-upload-summary.json` | Requested 5 more successful uploads; 6 reached `Minted` because one initially unresolved upload later completed. |
| Add folders to frontend Agentic Dashboard queue | Passed | `feed-queue-folder-summary.json` | Added 4 public feeds with 15+ items each to the feed queue. |

## Findings And Inconsistencies

- Registration, profile, home / check-in updates, categories, marketplace browse, and
  release frontend availability all passed.
- Observed response shapes matched current skill guidance for the tested
  read-only endpoints.
- Mutating feed flow worked: `POST /api/v1/agents/folders` returned `201`,
  each `POST /api/v1/agents/folders/:id/listings` returned `201`, and
  `GET /api/v1/agents/folders/:id/listings?limit=20` returned `200` with 8
  items.
- Folder item response nuance: the feed contents response returned item names
  under `listing`, but not `listing.listing_id` in this pass.
- Folder save status-code mismatch: `POST /api/v1/agents/folders/:id/save`
  returned `201` for all 4 saves, while prior skill docs said folder
  engagement writes return only `204 No Content`.
- Public-domain image upload worked end-to-end: create returned `201`, R2 PUT
  returned `200`, upload confirmation returned `200`, and status polling
  reached `Minted`.
- Bulk image upload found two operational edge cases: rapid multi-image
  workflows can hit `429 RATE_LIMITED`, and some confirmed image uploads can
  later reach `Processing Failed` without an exposed failure reason in the
  status response. One status check was rate-limited, but the item later
  reached `Minted`, which caused the run to produce 6 successful uploads rather
  than the requested 5.
- Frontend Agentic Dashboard queue behavior: `POST /api/v1/agents/feed-queue` accepted
  `target_type: "FOLDER"` and returned `201` with an `entry` object containing
  rank and a hydrated folder target. No agent REST queue-read endpoint was
  found in the backend endpoint reference.
- Local workflow issue: after sourcing `.env` in zsh, command lookup by bare
  name failed for `curl` and later `python3` in this test shell. Re-running
  with absolute paths (`/usr/bin/curl`, `/opt/homebrew/bin/python3`) worked.
  This did not affect Wondermint API behavior, but future repo scripts should
  avoid assuming those names are available through `PATH`.

## Skill Follow-Ups

- Installable skill docs were updated for the folder item ID caveat, observed
  folder-save `201`, bulk-upload rate-limit workflow, feed queue guidance, and
  frontend Agentic Dashboard terminology.
- Keep the operational bulk-upload guidance: throttle create/confirm/status
  calls, use longer backoff after `429`, and re-check unresolved statuses
  before launching replacement uploads to avoid accidental overrun.
- Keep the queue distinction explicit: `POST /api/v1/agents/feed-queue` is the
  REST enqueue action, while the frontend Agentic Dashboard is the user-visible
  UI that shows the queued infinite-feed content.
- Consider updating repo-only live-eval tooling to use discovered absolute
  command paths or to assert `PATH` before running.
