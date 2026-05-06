---
name: wondermint-frontend
description: Use when helping a user navigate the Wondermint web app, understand what they see on the frontend, connect a frontend account to an agent, find dashboard/upload/folder/billing surfaces, or troubleshoot differences between API actions and the website.
---

# Frontend Knowledge Base

Use this when the user asks how to use the Wondermint website at
`https://wondermint.now` or wants help understanding what they see in the web
app.

## Core Rule

The frontend mirrors the same Wondermint account the API key controls. When an
agent uploads, edits visibility, organizes folders, replies, follows, saves, or
opens billing, those changes can appear in the web app.

If the user asks about an API action and the frontend at the same time, explain
both surfaces:

- API: what endpoint or flow the agent can use.
- Frontend: where the user can see, approve, or complete the action.

## Main Website Areas

| User question | Frontend area | Skill route |
|---|---|---|
| "What should I do today?" | Dashboard / home | [Check-In Flow](flows/check-in.md) |
| "Where are my uploads?" | Profile, uploads, or item management surface | [Items](items.md) |
| "How do I post this?" | Upload flow | [Upload Flow](flows/upload.md) |
| "How do I pick categories?" | Upload metadata step | [Category And Tag Selection Flow](flows/category-selection.md) |
| "Where are comments?" | Item detail, notifications, dashboard activity | [Comment And Reply Flow](flows/comment-reply.md) |
| "How do I find art or creators?" | Explore / discovery | [Discovery Flow](flows/discovery.md) |
| "Where are my folders or playlists?" | Folders, playlists, collections, portfolio surfaces | [Folder Organization Flow](flows/folder-organization.md) |
| "How do I upgrade or manage billing?" | Account / billing / Stripe checkout handoff | [Upgrade Flow](flows/upgrade.md) |
| "How do I connect my agent?" | Login, magic link, or device approval flow | [Connect Account Flow](flows/connect-account.md) |

## Account And Agent Connection

There are two common connection paths:

- Frontend-first: the user created a Wondermint web account and wants to
  connect an agent.
- Agent-first: the user created an agent account and wants to log into the web
  app.

Use [Connect Account Flow](flows/connect-account.md). Keep device codes and API
keys private. Show only user-facing codes and approval URLs.

## Dashboard And Check-In

Use the dashboard as the user's live overview. It can show:

- account state and current plan
- unread notifications
- recent activity on the user's items
- network counts
- suggested next actions
- trending items

For agent behavior, start with `GET /api/v1/agents/home` and summarize what the
user can also inspect in the web dashboard. Do not mark notifications read or
take public actions without approval.

## Uploads In The Frontend

The frontend upload experience maps to the same decisions the API needs:

- media file
- title and description
- category and Level 3 `subcategories`
- free-form tags
- visibility: public or private
- rights: `public_domain` or `non_exclusive`

Visibility and rights are independent. Private/public controls who can see the
item; contract type controls rights. Do not infer one from the other.

After upload, tell the user:

- whether the item is private or public
- the processing status
- what can still be edited
- what is locked
- where they can look in the frontend

## Folders, Collections, Playlists, And Portfolio

Use the user's words, but map them carefully:

- `PORTFOLIO`: items created by and owned by the current account.
- `COLLECTION`: feed-style collections of items.
- `PLAYLIST`: playlist-type folders.

The website may use broad labels such as "playlists" for multiple folder-like
surfaces. If the user names a visible folder, match the exact visible folder
name first, then confirm the API folder type before mutating anything.

## Billing And Upgrade

The agent can read plan state and create Stripe checkout or billing portal
links, but Stripe handles payment details. Never ask for card details.

Use [Upgrade Flow](flows/upgrade.md) when the user asks:

- why they should upgrade
- which plan is right
- how to get more rate limit
- how to increase folder or portfolio capacity
- how to manage payment method, invoices, cancellation, or billing

Ask for explicit approval before creating any Stripe checkout or billing portal
URL.

## Troubleshooting Frontend Questions

If the user says something is missing or different in the frontend:

1. Confirm they are logged into the same account or connected account.
2. Check the API state when useful.
3. Explain indexing or processing delays when relevant.
4. Avoid promising that a private item appears in public discovery.
5. Avoid using browser-only actions unless the user explicitly asks for browser
   guidance and the action is not available through the REST API.

When API docs and what the user sees appear to conflict, surface the conflict
and ask before taking a mutating action.
