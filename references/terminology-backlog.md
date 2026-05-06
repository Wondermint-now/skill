# Terminology Backlog

Use this repo-development reference to track wording mismatches between the
Wondermint frontend language and backend/API language. This file is not part of
the installable skill surface.

## Current Frontend Terms

| Frontend term | Current API/backend term | Notes |
|---|---|---|
| Portfolio | `folder` path/resource, `PORTFOLIO` type | For things the user owns or created. |
| Playlist | `folder` path/resource, `PLAYLIST` type | For playlist-style saved/curated item groups. |
| Feed | `folder` path/resource, `COLLECTION` type | Frontend no longer says collection for this concept. |

## Skill Wording Rule

Installable skill docs should use **portfolio**, **playlist**, and **feed** in
normal user-facing explanations. They may use **folder**, **collection**,
`COLLECTION`, or `/api/v1/agents/folders` only when quoting API paths, API enum
values, request/response fields, or server messages.

## Backend/API Wording To Review

These are candidates for product/backend cleanup when the codebase is ready.
Some may remain as technical API terms for compatibility, but they should be
reviewed intentionally.

| Current wording | Preferred wording | Where observed |
|---|---|---|
| `folders` route/resource | portfolio/playlist/feed where user-facing | REST paths, endpoint docs, server `next.options[]`, frontend route labels if exposed. |
| `COLLECTION` enum | feed | Folder creation, folder search, cap details, validation messages. |
| "Folder cap reached for your plan" | "Portfolio, playlist, or feed cap reached for your plan" | `FOLDER_CAP_REACHED` message and related hints. |
| "Delete a folder of this type" | "Delete a portfolio, playlist, or feed of this type" | Error recovery hint for cap recovery. |
| "Collection + Playlist cap" | "Feed + Playlist cap" | Plan tables, upgrade explanations, billing copy. |
| "Search Public Folders" | "Search Public Portfolios, Playlists, And Feeds" | Discovery docs and any frontend/API labels exposed to users. |
| "Folder engagement" | "Portfolio/playlist/feed engagement" | Social docs and any user-facing endpoint descriptions. |

## Review Notes

- Keep REST compatibility in mind. API paths and enum names may need to remain
  stable even if user-facing copy changes.
- If API responses keep technical terms, the skill should translate them before
  responding to users.
- When backend messages change, update `references/backend-endpoints/` and then
  update the installable skill docs only where the changed behavior affects user
  guidance.
