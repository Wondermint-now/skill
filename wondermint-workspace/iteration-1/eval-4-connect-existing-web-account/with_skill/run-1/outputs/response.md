# Adding API Access To Your Existing Wondermint Web Account

Good news: you keep your existing account, your existing username, and your existing web login. Wondermint has a built-in path for exactly this — re-register through the API with the same email, and the server starts a device-approval flow that links API access to the account you already own. No new username, no duplicate account.

Here is what I'd like to do, what I need from you first, and what to expect.

---

## The plan (RFC 8628 device authorization flow)

1. I call `POST /api/v1/agents/register` with your existing email (`ashoka@bluemorphotours.com`) and your existing username.
2. Because that email already belongs to a web account, the server responds **`202 pending_confirmation`** with a short `user_code` and a verification URL — instead of creating a new account.
3. I show you the `user_code` and a link like `https://wondermint.now/device?user_code=ABCD1234`. You open it in the same browser where you're logged into Wondermint and approve API access. That logged-in browser session is what proves to Wondermint that you own the account.
4. I poll `GET /api/v1/agents/register/status?device_code=...` every few seconds until you click Approve.
5. On `confirmed`, the server returns your `api_key` (`mk_live_...`) **once**. I save it immediately to `WONDERMINT_API_KEY` in your local `.env` (or your password manager — your call) and never echo it back to chat, logs, commits, or screenshots.

After that, the same Wondermint account works in both places: your browser session at `https://wondermint.now` *and* `X-API-Key: mk_live_...` requests from me.

---

## What I need from you before I call anything

Two quick confirmations and one piece of info:

1. **Existing username.** What username did you pick on the web signup? I need it as an identifier for the register call — I am **not** asking you to pick a new one. (Wondermint usernames are 3–30 chars, `[a-zA-Z0-9_-]`, lowercased on save.)
2. **Where should I save the API key when it comes back?** Recommended: `WONDERMINT_API_KEY=...` in a local `.env` file in this project. Alternatives: your password manager, or another approved secret store. The key is shown **exactly once** — if I don't save it before doing anything else, it's gone and you'd have to regenerate from the website. So I'd like the save location decided up front.
3. **Browser ready?** You'll need to be logged into `https://wondermint.now` as `ashoka@bluemorphotours.com` in a browser you can switch to within ~30 minutes. The device code expires in 1800 seconds (30 min).

Optionally, I can also send a short `name` and `description` for the agent (these describe *me*, the agent, not you). Defaults are fine; tell me if you want specific values.

If you'd rather not share the username in chat, just confirm "use my existing username" and tell me what it is through whatever secret-entry path your host supports.

---

## Draft API calls

### 1. Trigger the device flow

```http
POST https://api.wondermint.now/api/v1/agents/register
Content-Type: application/json
User-Agent: wondermint-skill/0.1 (agent; connect-existing-web-account)

{
  "name": "<agent name, e.g. claude-agent>",
  "email": "ashoka@bluemorphotours.com",
  "username": "<your existing wondermint username>",
  "description": "<optional, ≤500 chars>"
}
```

Expected response (`202`):

```json
{
  "status": "pending_confirmation",
  "message": "This email belongs to an existing account. The account owner must approve API access.",
  "device_code": "abc123...",        // secret — I keep this, do not display
  "user_code": "ABCD-1234",          // I display this to you
  "verification_uri": "/device",
  "verification_uri_complete": "/device?user_code=ABCD1234",
  "expires_in": 1800,
  "interval": 5
}
```

If instead I get a `201` with an `api_key`, that means the server thought this was a brand-new account — I would stop, not save the key, and ask you whether `ashoka@bluemorphotours.com` is really the email on your existing web account before going further.

### 2. Tell you what to approve

I'd send you a message like:

> **Approve API access in your browser.**
> Open: `https://wondermint.now/device?user_code=ABCD1234`
> Confirm the code shown matches: **ABCD-1234**
> You have ~30 minutes. I'll be polling and will let you know the moment it's approved.

### 3. Poll for approval

```http
GET https://api.wondermint.now/api/v1/agents/register/status?device_code=<from step 1>
```

I poll every `interval` seconds (5s by default — not faster, the server may throttle). I handle the four states:

- `pending` → keep polling.
- `confirmed` → save `api_key` to your chosen location, stop polling, move on.
- `denied` → stop. I won't retry unless you explicitly start a new flow.
- `expired` → re-run step 1 to get a fresh `device_code` (only with your okay).

### 4. Verify and report

After saving the key, I'd do a quick `GET /api/v1/agents/me` with the new key to confirm it works and report back:

- the email and username on the account,
- `is_email_verified` status,
- the rate limit (Free plan is 30 req/min),
- and where I saved the key.

I will **not** paste the key itself in the report.

---

## Edge cases I'm prepared for

- **`409 "Email is already registered"` with `is_agent: true`.** That means API access is already attached to this email — you don't actually need to re-register. If you've lost the old key, I'd switch to **Regenerate API Key**, which requires you to log into the website and hit `POST /api/v1/agents/api-key/regenerate` from that browser session (this disables any prior keys).
- **`400 "Unauthorized or invalid session"` from register.** Known quirk — registration may have silently succeeded. I'd retry once with the same email; a follow-up `409 "Email is already registered"` confirms it. Because the original key was lost, the recovery there is also the regenerate path above.
- **Cloudflare/WAF block.** I retry with an honest `User-Agent` like `wondermint-skill/0.1 (agent; connect-existing-web-account)` — already in the draft above.
- **Device flow `confirmed` but "API key delivery expired".** Means the key was held in memory only 24h and is gone. I'd route you to Regenerate API Key from the website.
- **You miss the 30-minute window.** No harm done — I just re-run step 1 with your approval and you get a fresh code.

---

## Security promises while I do this

- Your API key only ever leaves Wondermint as `X-API-Key` headers to `https://api.wondermint.now/api/v1/*`. It never goes to any other domain, tool, or log.
- I won't print the key in chat after saving it.
- I won't commit the key, screenshot it, or paste it into issue trackers, summaries, or notes.
- I won't ask you for your web-account password as part of this flow — it isn't needed. Approval happens entirely through your existing browser session.

---

## Final checklist before I make the first call

Please confirm:

1. Your existing Wondermint username on `ashoka@bluemorphotours.com`.
2. Where to save the returned API key (default: `WONDERMINT_API_KEY` in local `.env`).
3. You're logged into `https://wondermint.now` in a browser you can reach within ~30 minutes.
4. (Optional) Agent `name` and `description`, or "defaults are fine."

Reply with those and I'll kick off the device flow.
