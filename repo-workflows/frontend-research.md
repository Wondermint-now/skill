# Frontend Research Workflow

Use this repo-only workflow to inspect Wondermint frontend navigation and turn
observed UI facts into skill reference material. Do not copy this workflow into
the installable skill package.

## Boundary

- Use browser exploration only as repo research.
- Do not teach the installable skill that agents should browse or click through
  the frontend for users.
- Distill stable user-facing facts into `references/frontend/` first, then copy
  only concise guidance into `skills/frontend.md` when it helps normal user
  support.
- Do not commit screenshots, browser traces, cookies, local storage, credentials,
  or raw transcripts that include private account data.

## Safe Public Pass

1. Open the release frontend or production frontend.
2. Record visible labels, route paths, search fields, primary buttons, public
   feed filters, public item-detail tabs, public creator profile sections, and
   login/onboarding entry points.
3. Save disposable screenshots or JSON captures under `.tmp/frontend-research/`.
4. Add stable findings to `references/frontend/navigation-map.md`.

## Authenticated Pass

Run this only with explicit owner approval for the account/session.

1. Log in with a test account or owner-provided session.
2. Inspect the dashboard, create/upload, profile, owned item management,
   portfolios/playlists/feeds, notifications, account settings, and billing
   surfaces.
3. Avoid paid, mutating, or public actions unless the owner explicitly approves
   the exact action.
4. Redact private data before committing any notes.

## Output

Update these files as information becomes stable:

- `references/frontend/navigation-map.md` for route and label facts.
- `references/terminology-backlog.md` for frontend/backend wording mismatches.
- `skills/frontend.md` only for concise, user-facing guidance that agents should
  use when answering frontend questions.
