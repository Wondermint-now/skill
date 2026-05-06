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

Authenticated dashboard, upload/create, billing, private item visibility, and
owned portfolio/feed/playlist management still need an approved authenticated
research pass.
