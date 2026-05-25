# Response: Missing badge and colored name on Wondermint

Short version: profile badges and colored/“gradient” usernames on most social platforms are tied to one (or more) of these things — a paid subscription/membership tier, a verification status, a special role (creator, early adopter, mod), or an opt-in cosmetic setting that has to be toggled on. Your friend almost certainly has one of those active and you don’t — or you have it but the display toggle is off.

I don’t have Wondermint-specific documentation in front of me, so I can’t point at the exact menu name. But here’s how I’d walk through it with you, and what I’d want to confirm before changing anything on your account.

---

## What I’d send to the user

> Hey! That badge + colored name combo on Wondermint is almost always one of three things — and they’re things that get applied to her account, not yours, so it’s not a bug on your side.
>
> The usual suspects:
>
> 1. **A paid subscription or membership tier.** A lot of platforms (and Wondermint looks like one of them based on what you’re describing) give subscribers a little badge next to their handle and a colored/gradient username. If she’s on a paid plan and you’re on the free tier, that’s the difference.
> 2. **Verification.** Some platforms give a badge for verified creators / verified accounts. If she applied for and got verified, she’d have the badge; you wouldn’t until you applied.
> 3. **A cosmetic toggle that’s off.** Even when you *are* eligible, some platforms require you to turn the badge/name color on in profile settings. It’s worth checking your profile or appearance settings for something like “Show subscriber badge” or “Username color.”
>
> Couple of quick questions so I can give you a more confident answer:
>
> - Do you know if she’s paying for a Wondermint subscription (sometimes called Pro, Plus, Premium, Gold — varies)?
> - Is her badge a checkmark (verification) or more of a colored shape/symbol (subscription/role)?
> - When you go into your own profile settings, do you see any toggle for badges, name color, or appearance?
>
> Once I know which of those it is, I can tell you exactly how to get the same thing — or confirm it’s a paid feature you’d need to subscribe for.

---

## My internal reasoning / plan

### What I’m fairly confident about
- The combination of **a badge + a colored name** is a strong fingerprint for a subscriber/membership tier on most social platforms. Discord Nitro, YouTube Memberships, Twitch subs, X Premium, Reddit Premium, etc. all follow this exact pattern: small icon next to the name plus a color/gradient on the handle.
- Verification alone usually gives a badge but does *not* recolor the username — so the fact that her **name is also colored** pushes me toward “paid tier or special role” rather than plain verification.
- “Mine doesn’t show up” has two possible meanings I should disambiguate:
  - (a) I don’t have the feature at all (not subscribed / not eligible).
  - (b) I should have it but it’s not displaying (toggle off, caching, app needs update).

### What I don’t know without Wondermint docs
- The exact name of Wondermint’s paid tier(s), if any.
- Whether Wondermint has multiple badge types (creator, early access, OG, mod, staff) that look similar.
- Whether badge display is automatic or opt-in.
- Whether there’s a known bug where badges disappear after profile edits or app updates.

Because of that, I want to ask before I tell the user to “just subscribe” — they might already be paying and just have a display toggle off, in which case telling them to pay would be wrong and annoying.

### What I would confirm before taking action
If this were a real support-style interaction and I had tools, I would *not* take any irreversible action (e.g., starting a subscription, changing account settings) without the user explicitly asking. I’d only:
- Read their current profile/subscription status.
- Read their display/appearance settings.
- Compare against the friend’s public profile (only public-visible fields).

I would **not**:
- Initiate a paid subscription on their behalf.
- Toggle settings without confirmation.
- Make any assumption about which tier they want.

### Draft API calls (hypothetical — I’m inventing reasonable shapes)

If Wondermint exposes an agent/API surface similar to other social platforms, the calls I’d want to make to diagnose this — read-only first — would look roughly like:

```http
GET /v1/me
Authorization: Bearer <user_token>
```
Expected interesting fields: `subscription_tier`, `badges[]`, `verified`, `display_preferences.show_badge`, `display_preferences.name_color`.

```http
GET /v1/users/{friend_handle}
Authorization: Bearer <user_token>
```
Expected interesting fields (public subset): `badges[]`, `verified`, `subscription_tier_public` (if exposed).

Then, **only after the user confirms** what they want:

```http
PATCH /v1/me/display_preferences
Authorization: Bearer <user_token>
Content-Type: application/json

{
  "show_badge": true,
  "name_color": "default"
}
```

And **only if** the user explicitly said “yes, sign me up for the paid tier”:

```http
POST /v1/me/subscriptions
Authorization: Bearer <user_token>
Content-Type: application/json

{
  "tier": "<tier_id>",
  "confirm_payment": true
}
```

I’d flag the subscription call as paid/irreversible and require an explicit confirmation step in the chat before sending it, per the “ask before costly/paid choices” rule.

### Questions I’m asking the user (and why)
1. **Is she on a paid plan?** Distinguishes “you need to subscribe” from “you should already have this.”
2. **Checkmark vs. colored symbol?** Distinguishes verification badge from subscription/role badge.
3. **Do you see a toggle in your appearance settings?** Distinguishes “feature missing” from “feature off.”

If they answer those, I can either (a) walk them through enabling a toggle, (b) walk them through applying for verification, or (c) explain what the paid tier gets them and let them decide whether to subscribe — without ever pulling the trigger on a paid action for them.

### If they don’t want to answer questions
Fallback advice I’d give: “Check Settings → Profile / Appearance for a ‘badge’ or ‘name color’ toggle. If there isn’t one, the badge is almost certainly tied to a paid plan or verification — open her profile and tap/hover the badge; on most platforms that tells you which program it represents.”
