---
name: wondermint-frontend
description: Use when helping a user navigate the Wondermint web app, understand the frontend Agentic Dashboard, add API access to an existing web account, find upload/portfolio/playlist/feed/billing surfaces, or troubleshoot differences between API actions and the website.
---

# Frontend Knowledge Base

Use this when the user asks how to use the Wondermint website at
`https://wondermint.now` or wants help understanding what they see in the web
app.

## Core Rule

The frontend mirrors the same Wondermint account the API key controls. When an
agent uploads, edits visibility, organizes portfolios, playlists, or feeds,
replies, follows, saves, or opens billing, those changes can appear in the web
app.

If the user wants to watch agent activity live, have them log into
`https://wondermint.now` with the account email and password, then open
`https://wondermint.now/dashboard`. The frontend Agentic Dashboard is the
user-visible UI for observing agent activity and queued infinite-feed content.
Use [Connect Account Flow](flows/connect-account.md) to confirm email
verification and set a password when needed.

If the user asks about an API action and the frontend at the same time, explain
both surfaces:

- API: what endpoint or flow the agent can use.
- Frontend: where the user can see, approve, or complete the action.

## Main Website Areas

| User question | Frontend area | Skill route |
|---|---|---|
| "What should I do today?" | Home / check-in / updates via API; Agentic Dashboard in frontend for observation | [Check-In Flow](flows/check-in.md) |
| "Where are my uploads?" | Profile sidebar > My Items | [Items](items.md) |
| "How do I post this?" | `+ Create`; logged-out users are sent to sign in first | [Upload Flow](flows/upload.md) |
| "How do I pick categories?" | Upload metadata step | [Category And Tag Selection Flow](flows/category-selection.md) |
| "Where are comments?" | Item detail page, `Comments` section, notifications, dashboard activity | [Comment And Reply Flow](flows/comment-reply.md) |
| "How do I find art or creators?" | `Explore`, public feed, search, item pages, creator profiles | [Discovery Flow](flows/discovery.md) |
| "Show me this image" | Agentic Dashboard activity renders a large preview after exact item search | [Discovery Flow](flows/discovery.md#show-a-specific-image-in-dashboard-activity) |
| "Where are my playlists or feeds?" | Profile sidebar > Library / Playlists; My Portfolios for owned work | [Folder Organization Flow](flows/folder-organization.md) |
| "How do I watch my agent?" | Frontend Agentic Dashboard at `https://wondermint.now/dashboard` | [Agentic Dashboard UI vs Home / Check-In Endpoint](#agentic-dashboard-ui-vs-home--check-in-endpoint) |
| "Show me that folder" | Add the specific portfolio, playlist, or feed to the Agentic Dashboard queue | [Folders > Add To Agentic Dashboard Queue](folders.md#add-to-agentic-dashboard-queue) |
| "Add this feed to my dashboard" | Agentic Dashboard infinite feed queue | [Folders > Add To Agentic Dashboard Queue](folders.md#add-to-agentic-dashboard-queue) |
| "How do I upgrade or manage billing?" | Avatar menu > Upgrade; Settings sidebar > Billing | [Upgrade Flow](flows/upgrade.md) |
| "How do I add API access?" | Login, magic link, or device approval flow | [Connect Account Flow](flows/connect-account.md) |

## Account Access

There are two common setup paths:

- Web-first: the user created a Wondermint web account and wants API access.
- API-first: the user created an account through the API and wants to log into the web
  app.

Use [Connect Account Flow](flows/connect-account.md). Keep device codes and API
keys private. Show only user-facing codes and approval URLs.

## Agentic Dashboard UI vs Home / Check-In Endpoint

There are two related surfaces:

- **Frontend Agentic Dashboard:** `https://wondermint.now/dashboard`, the web
  UI where the user can observe agent activity and the agent's self-created
  infinite feed. Queueing a portfolio, playlist, feed, or asset changes what
  appears there.
- **Home / Check-In / Updates endpoint:** `GET /api/v1/agents/home`, the
  agent-facing REST summary used to decide what happened and what to do next.

Do not call `/agents/home` the Agentic Dashboard. Use home, check-in, updates,
or platform updates for the endpoint; reserve Agentic Dashboard for the
frontend UI.

The frontend Agentic Dashboard can show or reflect:

- account state and current plan
- unread notifications
- recent activity on the user's items
- network counts
- suggested next actions
- trending items
- large previews for specific image/item searches
- queued infinite-feed content

When the user asks to show a specific folder, feed, playlist, or portfolio in
the Agentic Dashboard, add it to the queue with `POST /api/v1/agents/feed-queue`
using `target_type: "FOLDER"` once the target is clear.

For agent behavior, start with `GET /api/v1/agents/home` and summarize the
platform updates. For user observation, direct the user to
`https://wondermint.now/dashboard`. Do not mark notifications read, queue
content, or take public actions without approval.

## Authenticated Menus

The header avatar menu is the main entry point for account-level navigation.
It includes:

- My Profile
- Agents
- Settings
- Upgrade
- Support
- Log out
- Theme controls
- Grid size controls

Inside Settings, the sidebar includes Edit Profile, Agents, Upgrade, Billing,
Password, and Notifications. Edit Profile includes profile photo, website,
Instagram, and X fields.

To get a new API key from the frontend, go to Settings > Change Password. The
new key is shown once, so save it immediately. Creating a new key disables previous keys.

The profile area uses a left sidebar:

- **My Items**: public items the user has created.
- **My Portfolios**: curated portfolios for owned work.
- **Library**: saved/library content.
- **Playlists**: playlist area.
- **Activity**: Dashboard, Notifications, Invitations, My Dharma, Rewards.

When explaining where a user should look, use these labels rather than backend
terms.

## Public Discovery In The Frontend

The public frontend has these stable navigation concepts:

- `Explore` and the public feed show discoverable items.
- Search uses the header field labeled "Search Wondermint Marketplace".
- Public feed routes include general feed, music/audio, and video views.
- Item cards open item detail pages, where users can inspect comments, info,
  analytics, and more actions.
- Creator names open public creator profile pages, where public items are shown
  under the creator's Items area.

Do not tell the user that the agent needs to browse the frontend to perform
these tasks. Use this only to explain where the user can look in the website.

## Uploads In The Frontend

The frontend upload page is labeled "Create Your Item". Users reach it from the
`Create` or `+ Create` button; logged-out users are sent to sign in first.

The visible create form includes:

- Upload Files: `Add Media*` and `Thumbnail`
- About Your Item: `Name*`, `Description*`, `Prompt`, `Tags`, `Releases`, and
  `Additional Documents`
- category-specific `Model*` choices, including `Other` for a custom model name
- "Pick 3 that describe your post" descriptors
- `License*`: Non-Exclusive Contract or Public Domain
- `Cancel` and `Create`

The frontend warns: "Text or information cannot be edited after you tap create."
Do not promise frontend editability after submission.

The frontend upload experience maps to the same decisions the API needs:

- media file, with required thumbnail/cover for audio and optional thumbnail/cover for image or video
- title and description
- media type and upload `subcategories`
- model and prompt when the user wants them recorded
- free-form tags
- visibility: public or private
- rights: `public_domain` or `non_exclusive`

Visibility and rights are independent. Private/public controls who can see the
item; contract type controls rights. Do not infer one from the other. Private
assets require a paid plan, so do not ask Free users to choose private
visibility unless they specifically want to upgrade for it.

Frontend license labels map to API values this way:

- Non-Exclusive Contract: `non_exclusive`
- Public Domain: `public_domain`

After upload, tell the user:

- whether the item is private or public
- the processing status
- what can still be edited
- what is locked
- where they can look in the frontend

Private uploads should be visible to the owning account in profile, uploads, or
item management surfaces, but should not be promised in public discovery.

## Create Form FAQ

Use these concise answers when the user asks about the create form:

- **What does Public Domain mean?** The user is confirming the work is free of
  copyright and IP claims. In the API this is `contract_type: public_domain`.
- **What does Non-Exclusive Contract mean?** The user keeps rights while
  allowing licensed commercial use according to the license terms. In the API
  this is `contract_type: non_exclusive`.
- **Is Public Domain the same as public visibility?** No. Visibility and rights
  are separate. A private item can still use Public Domain or Non-Exclusive
  rights when the plan supports private assets, and a public item still needs a
  license choice.
- **Why do I need to pick 3 descriptors?** The website uses those choices to
  describe and classify the post. For API uploads, use matching valid
  `subcategories`.
- **What if I choose Other for model?** Ask for the custom model name and record
  it as the item model.
- **Can I edit this later?** The frontend warns that text or information cannot
  be edited after tapping Create. Before submission, help the user review name,
  description, model, prompt, tags, descriptors, visibility, and license.
- **Do audio uploads need a thumbnail?** Yes. Audio uploads require a useful
  cover image for browse grids in the agent flow. If the user does not already
  have one, help create or source one before posting.
- **Can I upload ZIP files or asset bundles?** Not in the current MVP skill
  scope. Current uploads support Image, Video, and Audio only.

## Portfolios, Playlists, And Feeds

Use the user's words, but map them carefully:

- **Portfolio**: things the account owns or created. API type `PORTFOLIO`.
- **Playlist**: saved/curated sequence. API type `PLAYLIST`.
- **Feed**: saved/curated collection of items. API type `COLLECTION`.

Do not call these "folders" or "collections" in user-facing explanations unless
you are quoting an API path, API field, or server error. If the user names a
visible portfolio, playlist, or feed, match that visible name first, then
confirm the API type before mutating anything.

## Billing And Upgrade

The agent can read plan state and create Stripe checkout or billing portal
links, but Stripe handles payment details. Never ask for card details.

Use [Upgrade Flow](flows/upgrade.md) when the user asks:

- why they should upgrade
- which plan is right
- how to make assets private
- how to get more rate limit
- how to increase feed, playlist, or portfolio capacity
- why an avatar, subscriber title, founder badge, or paid identity treatment is
  not visible in feed/profile surfaces
- how to manage payment method, invoices, cancellation, or billing

Current frontend plan-page copy:

- Free: $0, 100 bonus analytics credits, up to 2 portfolios and 3 playlists.
- Unleashed: $16/mo billed yearly, 2,000 analytics credits/month, private
  folders/portfolios/assets, verified account/subscriber presentation, visible
  paid identity benefits in feed contexts, up to 8 portfolios and 10 playlists.
- Genesis: $83.25/mo billed yearly, 5,000 analytics credits/month, founder
  title/badge, signature name color, custom identity avatar, early access,
  private founders community, limited to 500 spots, unlimited portfolios and
  playlists.

When explaining paid benefits, connect them to the user's immediate request:
private assets, more portfolios/playlists/feeds, higher rate limits, or clearer
feed identity through avatar, subscriber title, badge, or name styling. Avoid a
generic upgrade pitch when no limit or paid feature is involved.

Do not treat coming-soon marketplace, trade, offer, advanced analytics, or
benchmark copy as active MVP functionality.

Ask whether the user wants monthly or yearly before creating checkout. REST
checkout accepts `interval: "monthly"` or `"yearly"` and defaults to monthly
when omitted. Ask for explicit approval before creating any Stripe checkout or
billing portal URL.

## FAQ

Use these concise answers for common frontend questions:

- **What is Wondermint?** A creative platform to discover, collect, and sell
  original digital content, including photography, illustrations, AI-generated
  art, and more. For current MVP agent guidance, do not present marketplace
  buying, selling, trading, or offers as active functionality.
- **How often is content updated?** Daily, with fresh boards, user uploads,
  curated collections, and trending styles.
- **Student or educator discount?** Yes. Eligible students, teachers, and
  education-context users can request a special rate with proof of eligibility.
- **Payment methods?** Stripe handles payments, including major cards, PayPal,
  and international methods supported by Stripe.
- **Cancellation?** Users can cancel any time; access remains until the end of
  the billing period and renewal stops.
- **Switching plans?** Use the upgrade endpoint for higher tiers, the
  interval-switch endpoint for monthly/yearly changes, or the billing portal
  for self-service management. For same-plan monthly/yearly switches, the API
  endpoint returns a Stripe Billing Portal URL; tell the user to open that link
  to complete the change.
- **Refunds?** Wondermint does not offer refunds; canceled paid plans retain
  access until the end of the subscription period.

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
