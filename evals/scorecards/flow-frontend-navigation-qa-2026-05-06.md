# Wondermint Skill Scorecard

## Version

- Version/tag: post-`v0.1.2`
- Commit: `2da9340`
- Date: 2026-05-06
- Evaluator: Codex dry review

## Summary

- Overall rating: 3 / 3
- Recommendation: keep the current frontend navigation guidance.
- Release blocking issues: none found.

## Scenarios

| Prompt | Expected route / labels | Result | Score | Evidence |
|---|---|---|---:|---|
| "Where do I find my uploaded items?" | Profile sidebar > My Items | Pass | 3 | `skills/frontend.md` maps uploads to "Profile sidebar > My Items". |
| "Where do I manage my portfolios?" | Profile sidebar > My Portfolios | Pass | 3 | Authenticated menu section defines My Portfolios as curated portfolios for owned work. |
| "Where are playlists?" | Profile sidebar > Library / Playlists | Pass | 3 | Main website areas and authenticated menu section name Library and Playlists. |
| "How do I upgrade?" | Avatar menu > Upgrade; Settings sidebar > Billing; Upgrade Flow | Pass | 3 | Frontend table routes upgrade/billing to visible labels and `flows/upgrade.md`. |
| "Where do I change my password?" | Settings sidebar > Password | Pass | 3 | Authenticated menu section lists Password under Settings. |
| "How do I connect my agent?" | Connect Account Flow; public onboarding when needed | Pass | 3 | Frontend table routes to `flows/connect-account.md`; navigation map records `/agent-onboarding`. |
| "Where are notifications?" | Activity > Notifications and Settings > Notifications | Pass | 3 | Authenticated menu section lists both profile Activity and settings sidebar notification surfaces. |
| "How do I create a new upload from the website?" | `+ Create`; sign in first if logged out | Pass | 3 | Frontend table names `+ Create`; public navigation map records login redirect. |
| "What is the difference between My Items, My Portfolios, Library, and Playlists?" | Public created work, owned portfolios, saved/library content, playlist area | Pass | 3 | Authenticated menu section defines each label. |

## What Worked

- The installable frontend guidance uses visible UI labels rather than backend
  folder/collection terminology.
- Public navigation, authenticated avatar menu, settings sidebar, and profile
  sidebar facts are available in concise form.
- The guidance explicitly says not to tell users that the agent needs to browse
  the frontend.

## What Confused The Agent

- No blocker found in this dry review.

## Missing Context

- This was not a fresh-agent subagent run.
- Authenticated upload/create, billing details, private item visibility, and full
  portfolio/playlist management still need an approved interactive pass if
  deeper frontend precision is needed.

## Endpoint Reference Updates

- Endpoint observations added to `references/backend-endpoints/live-observations.md`: no.
- Static endpoint/schema/message docs updated: no.
- Skill docs updated from confirmed behavior: no changes needed in this pass.
- MVP scope check: no new endpoints were added.
- REST-only check: no GraphQL operations, queries, mutations, schemas, or
  `/graphql` examples were added to skill docs.
- Deferred follow-up: optional fresh-agent validation and authenticated frontend
  walkthrough.

## Security And Credential Review

- Were any secrets exposed in committed files? No.
- Did the skill keep credentials limited to approved Wondermint domains? Yes.
- Any risky logging, screenshots, or transcript content? No.

## Raw Evidence

- `skills/frontend.md`
- `references/frontend/navigation-map.md`
