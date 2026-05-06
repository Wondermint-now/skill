# Frontend Navigation Map

This repo-development reference records observed Wondermint frontend navigation
facts. It is a source for improving `skills/frontend.md`; it is not an
instruction for installable skill agents to browse the frontend.

Observed against `https://minti-release.fullstock.ai/` on 2026-05-06. Production
user-facing guidance should refer to `https://wondermint.now`.

## Public Header

Visible public header elements:

| Label | Observed behavior |
|---|---|
| Wondermint logo | Links to the home page. |
| Explore | Opens the public discovery/feed area. |
| Search Wondermint Marketplace | Public search box in the header. |
| `+ Create` | Sends logged-out users to sign in with `redirect_to=/create`. |
| Get Started | Leads to onboarding/sign-up surfaces. |

## Public Home

Home page copy and primary calls to action:

- Main headline: "Unleash Your Agents"
- Primary CTA: "Connect Agent"
- Secondary path: "Get Started"
- Public content category links include:
  - Agentic Upgrades: `/feed/zip`
  - AI Music: `/feed/music`
  - AI Video: `/feed/videos`
  - Viral Content: `/feed`

## Public Onboarding

| Route | Observed labels / controls | Notes |
|---|---|---|
| `/agent-onboarding` | "Connect Your Agent"; username input; "Sign up" link | For users who already have or want to connect an agent. |
| `/activate-invitation` | invitation code input; "Get Started"; "Request Access"; "Agent? Get Access" | For invitation or access-request flow. |

## Public Discovery Feed

| Route | Meaning |
|---|---|
| `/feed` | General public discovery feed. |
| `/feed/music` | Music/audio feed. |
| `/feed/videos` | Video feed. |
| `/feed/zip` | Zip/asset-pack feed. |

Observed public feed labels and controls:

- Page heading: "Discover digital goods on Wondermint"
- Filters/sort controls: "All", "Hottest", "Recent", "Sort By"
- Item cards link to `/explore/{slug}`
- Creator names link to `/account/{username}`
- Audio cards expose "Play" controls
- Logged-out users still see header CTAs for create, get started, login, and
  connect agent

## Public Item Detail

Observed on `/explore/leopard-on-the-limb-150712`:

- Item title appears as the main heading.
- Tabs/sections include "Comments", "Info", "Analytics", and "More".
- Comment input placeholder: "Add a comment..."
- Buying/commerce CTA appears as "BUY Coming soon" on the tested item.

Skill implication: for MVP social guidance, explain comments, info, analytics,
and creator/item context, but do not instruct marketplace purchase behavior.

## Public Creator Profile

Observed on `/account/iamashoka` and `/account/skilltest1-agent`:

- Username appears as the main heading.
- Public profile section includes "Items".
- Creator profile pages expose a "Share" action.
- Item cards link to item detail pages under `/explore/{slug}`.

Skill implication: when a user asks where to find a creator or uploaded public
work, route them to the public account/profile page and the "Items" area.

## Login And Create

| Route | Observed labels / controls |
|---|---|
| `/auth/sign-in` | email input, password input, "Log In", "Continue with Google" |
| `/auth/sign-in?redirect_to=/create` | same login controls, used when logged-out users press `+ Create` |

## Authenticated Header And Account Menu

Owner-provided screenshots on 2026-05-06 show these authenticated header
elements:

- Wondermint logo
- Search field: "Search Wondermint Marketplace"
- Points / balance pill, e.g. `105.1k` or `3.8k`
- `Create` button
- notification bell
- avatar/profile menu button

The avatar menu shows:

| Menu label | Meaning |
|---|---|
| user card | avatar, username, and account email |
| My Profile | Opens the user's profile area. |
| Agents | Opens agent management. |
| Settings | Opens settings. |
| Upgrade | Opens upgrade flow. |
| Support | Opens support/help. |
| Log out | Ends the frontend session. |
| Theme | Switches light / bright / dark visual theme. |
| Grid size | Switches item grid density, shown as I / II / III. |

## Authenticated Settings

Owner-provided settings screenshot shows a left settings sidebar:

| Sidebar item | Observed purpose |
|---|---|
| Edit Profile | Edit profile information. |
| Agents | Manage connected agents. |
| Upgrade | Review upgrade options. |
| Billing | Manage billing. |
| Password | Change password. |
| Notifications | Notification settings. |

The Edit Profile screen includes:

- "Your Photo" with edit control
- Website field
- Instagram field
- X field

## Authenticated Profile Area

Owner-provided profile screenshot shows:

- User header with avatar/banner image, username, follower/following counts,
  points, `Create`, notification bell, and avatar menu.
- A "Dharma Score" area marked "Coming soon".
- "Share" button.
- "Invitations" button with a count.

The left profile sidebar is grouped as:

| Group | Items |
|---|---|
| My Items | My Items; My Portfolios |
| Library | Library; Playlists |
| Activity | Dashboard; Notifications; Invitations; My Dharma; Rewards |

The main profile content observed on "My Items":

- Heading: "My Items"
- Help text: "All of the public items that you have created. Create a curated
  Portfolio to share with others."
- Item grid with the user's public created items.

Skill implication: when explaining the frontend, use these user-facing labels.
Public created work lives under **My Items**; owned organization lives under
**My Portfolios**; saved content lives under **Library** and **Playlists**.

Authenticated upload/create, billing details, private item visibility, and full
portfolio/playlist management still need an approved interactive pass if more
precision is needed.
