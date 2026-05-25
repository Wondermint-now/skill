# Adding API access to your existing Wondermint account

Good news: you don't need to create a new account or change your username to give your agent upload access. The standard pattern on platforms like this is to add an **API key (or OAuth app credential)** to your existing account — your username, profile, followers, and existing posts stay exactly as they are. The key is just a second way for *you* to authenticate.

Below is the plan I'd follow, what I need from you before touching anything, and the rough shape of the calls I'd make.

---

## What I want to confirm before doing anything

A couple of small but important things, because I don't want to accidentally create a duplicate account or burn your existing handle:

1. **Confirm the account email.** You said `ashoka@bluemorphotours.com` — is that the same email you signed up with on the web? If you used a social login (Google / Apple), the API key flow usually still works, but the path is slightly different (you'd link a password or a personal access token from the web dashboard first).
2. **Confirm your username (handle).** Just so I can sanity-check that I'm operating against the right account once a token is issued — I'll read it back to you after first auth.
3. **Scope.** You said "upload stuff." Do you want the agent limited to:
   - upload / create posts only (recommended, least privilege), or
   - upload + edit + delete its own posts, or
   - full account access (post, comment, DM, follow, profile edits)?

   I'd default to **upload-only** unless you tell me otherwise. You can always widen scopes later.

4. **Where the key should live.** I'll store it in a local `.env` (e.g. `WONDERMINT_API_KEY=...`) and never log it or commit it. If you'd rather use a secrets manager (1Password, macOS Keychain, etc.), tell me which and I'll wire that up instead.

I'll wait for those four answers before running anything.

---

## The plan (once you confirm)

### Step 1 — Get credentials from your existing account, don't make a new one

There are three common patterns platforms use. I'd try them in this order, stopping at whichever Wondermint actually supports:

**(a) Personal API key from the web dashboard (most likely).**
You log in to wondermint.com → Settings → **Developers / API / Integrations** → "Create API key" or "New personal access token." You give it a name like `my-agent`, pick scopes (`uploads:write` or similar), and copy the token. Paste it to me and I'll save it to `.env`. No new account, no username change.

**(b) OAuth app + user authorization.**
If Wondermint only exposes OAuth (no raw personal tokens), the flow is:
   1. You register a small "app" in the developer settings (name: "Ashoka's agent").
   2. You get a `client_id` and `client_secret`.
   3. I run a one-time authorization URL — you click "Allow" while logged into your existing account — and Wondermint returns a `refresh_token` tied to your existing user.
   4. The agent uses that token from then on.

   Same outcome: your existing identity, just authorized for programmatic access.

**(c) Device code flow.**
If they support it (good for CLI/agent use), I'd request a device code, show you a short URL + code, you approve it in the browser while logged in, and we get a token back. Again, bound to your existing account.

In all three cases: **your username does not change. You are not signing up again.** You're just minting a credential against the account that already exists.

### Step 2 — Verify the token is bound to the right account

Before doing any uploads, I'd call the equivalent of `GET /v1/me` and read back the username and email so we both confirm it's *your* account and not a fresh one. Draft:

```http
GET https://api.wondermint.com/v1/me
Authorization: Bearer $WONDERMINT_API_KEY
```

Expected response shape (guessing — will adapt to whatever the real API returns):

```json
{
  "id": "usr_...",
  "username": "<your existing handle>",
  "email": "ashoka@bluemorphotours.com",
  "created_at": "2025-04-..."
}
```

I'll paste the `username` and `created_at` back to you so you can eyeball that it matches the account you signed up with ~a month ago. If anything looks off (different handle, recent `created_at`), we stop and figure out why before uploading.

### Step 3 — Do a dry-run upload

First real call would be a single small test upload so we can confirm:
- the post lands on your existing profile, and
- the visibility / author shows your existing username.

Draft (shape is illustrative):

```http
POST https://api.wondermint.com/v1/uploads
Authorization: Bearer $WONDERMINT_API_KEY
Content-Type: multipart/form-data

file=@./test.jpg
caption="agent upload test — please ignore"
visibility="private"   # or "draft" if supported, so it doesn't fan out to followers
```

I'd default the test post to **private / draft** so your followers don't get pinged by a test. You delete it (or I delete it via `DELETE /v1/posts/{id}`) once you've confirmed it appeared on the right account.

### Step 4 — Normal operation

After the dry run passes, the agent uploads using the same key. I'd also:
- set up token refresh if it's OAuth (refresh tokens typically rotate),
- add a small retry/backoff for rate limits,
- log only `request_id` / status codes — never the token, never the payload contents beyond filenames.

---

## What I'd send you right now (draft user-facing message)

> Hey — quick check before I wire this up:
>
> 1. Is `ashoka@bluemorphotours.com` the email you used to sign up on wondermint.com? And did you use a password or social login (Google/Apple)?
> 2. What's your Wondermint username/handle? I'll read it back after auth to make sure we're on the right account.
> 3. Scope — okay if I limit the agent to **upload-only** for now? You can widen it later.
> 4. Can you go to wondermint.com → Settings and look for a section called **Developers**, **API**, or **Integrations**? If you see "Create API key" or "Personal access token," create one named `agent` with upload permission and paste it here. If you don't see that section, tell me what *is* there under Settings and I'll figure out the right path (OAuth app or device flow).
>
> I won't touch your account or upload anything until you confirm 1–3 and send the token (or tell me the dashboard doesn't have one).

---

## Decisions I'm making without asking (so you can override)

- **Least-privilege scope by default** (upload-only). Override: tell me to go broader.
- **Test upload will be private/draft**, not public. Override: tell me to post it publicly.
- **Token stored in `.env`**, gitignored, never logged. Override: tell me to use Keychain / 1Password / something else.
- **No new account created under any circumstance.** If the only path Wondermint offers turns out to require a separate "developer account," I'll stop and ask you before proceeding — I won't silently create one.

---

## Things I genuinely don't know and would need to check

- The exact name of Wondermint's developer settings page and whether they offer personal API keys vs. OAuth-only.
- Whether scopes are named `uploads:write`, `media.write`, `post:create`, or something else.
- The actual API base URL and auth header format (Bearer vs. `X-API-Key` vs. signed requests).
- Rate limits and upload size caps.

I'd resolve all of these by reading Wondermint's developer docs once we know the dashboard has a Developers section — or by inspecting the response of the first `/me` call.

Send me answers to the four questions above and I'll take it from there.
