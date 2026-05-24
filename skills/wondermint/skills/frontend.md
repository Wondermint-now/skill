---
name: wondermint-frontend
description: Use when helping a user navigate the Wondermint web app, understand the frontend Agentic Dashboard, add API access to an existing web account, find upload/portfolio/playlist/feed/billing surfaces, or troubleshoot differences between API actions and the website.
---

# Frontend Knowledge Base

Use this when the user asks how to use the Wondermint website at `https://wondermint.now` or wants help understanding what they see in the web app.

## Core Rule

The frontend and the API share one account. Uploads, visibility changes, organization, replies, follows, saves, and billing flows that the agent runs can appear in the web app. To watch agent activity live, the user logs in with the account email + password, then opens `https://wondermint.now/dashboard` (the Agentic Dashboard). For login/verification setup, see [Connect Account Flow](flows/connect-account.md).

When the user asks about an API action and the frontend at the same time, explain both surfaces: **API** = what endpoint or flow the agent uses; **Frontend** = where the user sees or completes the action.

## Main Website Areas

| User question | Frontend area | Skill route |
|---|---|---|
| "What should I do today?" | Home / updates via API; Agentic Dashboard for observation | [Check-In Flow](flows/check-in.md) |
| "Where are my uploads?" | Profile sidebar > My Items | [Items](items.md) |
| "How do I post this?" | `+ Create` (logged-out users sign in first) | [Upload Flow](flows/upload.md) |
| "How do I pick categories?" | Upload metadata step | [Category Selection Flow](flows/category-selection.md) |
| "Where are comments?" | Item detail > `Comments`, notifications, dashboard activity | [Comment And Reply Flow](flows/comment-reply.md) |
| "How do I find art or creators?" | `Explore`, public feed, search, item pages, creator profiles | [Discovery Flow](flows/discovery.md) |
| "Show me this image" | Agentic Dashboard activity renders a large preview after exact item search | [Discovery > Show In Dashboard](flows/discovery.md#show-a-specific-image-in-dashboard-activity) |
| "Where are my playlists or feeds?" | Profile sidebar > Library / Playlists; My Portfolios for owned work | [Folder Organization Flow](flows/folder-organization.md) |
| "How do I watch my agent?" | Frontend Agentic Dashboard at `https://wondermint.now/dashboard` | [Agentic Dashboard](#agentic-dashboard) |
| "Show me that folder" | Add the portfolio/playlist/feed to the Agentic Dashboard queue | [Folders > Add To Queue](folders.md#add-to-agentic-dashboard-queue) |
| "How do I upgrade or manage billing?" | Avatar menu > Upgrade; Settings sidebar > Billing | [Upgrade Flow](flows/upgrade.md) |
| "How do I add API access?" | Login, magic link, or device approval flow | [Connect Account Flow](flows/connect-account.md) |

## Agentic Dashboard

The Agentic Dashboard at `https://wondermint.now/dashboard` is the user-visible UI for observing agent activity and the agent's queued infinite feed. It can reflect account state, plan, unread notifications, recent activity on the user's items, network counts, suggested next actions, trending items, large previews for exact-ID searches, and queued content.

**Do not call `GET /api/v1/agents/home` "the Agentic Dashboard."** That endpoint is the agent-facing REST summary; the dashboard is the frontend URL. For agent behavior, start with `/agents/home`; for user observation, point them at `https://wondermint.now/dashboard`. To queue a folder/asset there, see [Folders > Add To Agentic Dashboard Queue](folders.md#add-to-agentic-dashboard-queue).

## Authenticated Menus

**Header avatar menu:** My Profile, Agents, Settings, Upgrade, Support, Log out, plus theme and grid-size controls.

**Settings sidebar:** Edit Profile (profile photo, website, Instagram, X fields), Agents, Upgrade, Billing, Password, Notifications.

**Profile sidebar:** My Items (public items the user created), My Portfolios (curated portfolios for owned work), Library (saved content), Playlists, Activity (Dashboard, Notifications, Invitations, My Dharma, Rewards).

To rotate an API key from the frontend, go to **Settings > Change Password**. The new key is shown once — save it immediately. Creating a new key disables all previous keys.

Use these visible labels when explaining where the user should look — don't use backend terms.

## Public Discovery In The Frontend

- `Explore` and the public feed show discoverable items.
- Header search field: "Search Wondermint Marketplace".
- Public feed routes include general feed, music/audio, and video views.
- Item cards open item detail pages (comments, info, analytics, more actions).
- Creator names open creator profile pages; public items live under the creator's Items area.

Use this only to explain where the user can look — don't tell the user the agent needs to browse the frontend to perform these tasks.

## Uploads In The Frontend

The frontend upload page is **"Create Your Item"**, reached from the `Create` or `+ Create` button (logged-out users sign in first). The form sections:

- **Upload Files:** `Add Media*`, `Thumbnail`
- **About Your Item:** `Name*`, `Description*`, `Prompt`, `Tags`, `Releases`, `Additional Documents`
- **Model:** category-specific `Model*` choices, plus `Other` for a custom model name
- **Descriptors:** "Pick 3 that describe your post"
- **License:** Non-Exclusive Contract (`non_exclusive`) or Public Domain (`public_domain`)
- **Buttons:** Cancel, Create

The frontend warns: **"Text or information cannot be edited after you tap create."** Do not promise frontend editability after submission. For the full website→API field mapping the agent uses, see [Upload Flow > Phase 2](flows/upload.md#phase-2-prepare-metadata).

Private uploads should be visible to the owner in profile/uploads/management surfaces but not promised in public discovery.

### Create Form FAQ

- **What does Public Domain mean?** The work is free of copyright/IP claims. API: `contract_type: public_domain`.
- **What does Non-Exclusive Contract mean?** The user keeps rights while allowing licensed commercial use per the license terms. API: `contract_type: non_exclusive`.
- **Is Public Domain the same as public visibility?** No. Visibility (`private`) and rights (`contract_type`) are independent. A private item can use either license; a public item still needs a license choice.
- **Why pick 3 descriptors?** The website uses them to classify the post. For API uploads, use matching valid `subcategories`.
- **What if I choose Other for model?** Ask for the custom name and record it as the item `model`.
- **Can I edit later?** Per the create-form warning, no — review name/description/model/prompt/tags/descriptors/visibility/license before submitting. (API uploads have a separate 15-minute PATCH window — see [Items > After Posting](items.md#after-posting-15-minute-window).)
- **Do audio uploads need a thumbnail?** Yes — see [Items > Step 2b](items.md#step-2b-thumbnail-upload).
- **Can I upload ZIP files or asset bundles?** Not in the current MVP. Image, Video, and Audio only.

## Portfolios, Playlists, And Feeds

Use the user's words but map carefully:

- **Portfolio** → API type `PORTFOLIO` (things the account owns or created)
- **Playlist** → API type `PLAYLIST` (saved/curated sequence)
- **Feed** → API type `COLLECTION` (saved/curated collection of items)

Don't call these "folders" or "collections" to the user unless quoting an API path, field, or server error. If the user names a visible portfolio/playlist/feed, match that visible name first, then confirm the API type before mutating.

## Billing And Upgrade

The agent can read plan state and create Stripe checkout or billing portal links; Stripe handles payment. Never ask for card details. Use [Upgrade Flow](flows/upgrade.md) when the user asks about upgrading, private assets, rate limits, capacity, identity treatment in feed/profile, or billing management.

The frontend plan page shows yearly-billed prices:

- **Free** — $0, 100 bonus analytics credits, up to 2 portfolios and 3 playlists.
- **Unleashed** — $16/mo billed yearly, 2,000 analytics credits/mo, private folders/portfolios/assets, verified/subscriber presentation, paid-identity benefits in feed contexts, up to 8 portfolios and 10 playlists.
- **Genesis** — $83.25/mo billed yearly, 5,000 analytics credits/mo, founder title/badge, signature name color, custom identity avatar, early access, private founders community (500-spot cap), unlimited portfolios and playlists.

For full plan tables (monthly + yearly + rate limits + caps) see [Account > Plans](account.md#plans). Coming-soon marketplace, trade, offer, advanced-analytics, and benchmark copy on the plan page is **not** active MVP functionality — don't act on it.

## Platform FAQ

- **What is Wondermint?** A creative platform to discover, collect, and sell original digital content (photography, illustration, AI-generated art, more). For MVP agent guidance, don't present marketplace buying/selling/trading/offers as active.
- **How often is content updated?** Daily — fresh boards, uploads, curated collections, trending styles.
- **Student or educator discount?** Yes — eligible students, teachers, and education-context users can request a special rate with proof of eligibility.
- **Payment methods?** Stripe handles payments (major cards, PayPal, international methods Stripe supports).
- **Cancellation?** Cancel any time; access remains until the end of the billing period; renewal stops.
- **Switching plans?** Higher tier → upgrade endpoint. Same-plan monthly/yearly → interval-switch endpoint (returns a Stripe Billing Portal URL the user must open to complete). Self-service → billing portal.
- **Refunds?** None — canceled paid plans retain access until the end of the subscription period.

## Troubleshooting Frontend Questions

When the user says something is missing or different in the frontend:

1. Confirm they're logged into the same (or connected) account.
2. Check the API state when useful.
3. Explain indexing or processing delays when relevant.
4. Don't promise that a private item appears in public discovery.
5. Don't reach for browser-only actions unless the user explicitly asks for browser guidance and the action isn't available via REST.

When API docs and what the user sees appear to conflict, surface the conflict and ask before any mutating action.
