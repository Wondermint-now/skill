# Skill Large-File Stress Review - 2026-05-09

## Scope

Dry review of the largest installable support files:

- `skills/items.md`
- `skills/social.md`
- `skills/auth.md`
- `skills/account.md`

Goal: determine whether these files should stay as focused large files or be
split because agents miss steps, load irrelevant context, or confuse unrelated
sections.

## Static Validation

Command:

```bash
python3 repo-workflows/validate.py
```

Result:

```text
Wondermint validation passed.
```

## Scenario Coverage

| Area | Prompt | Expected With-Skill Behavior | Score | Evidence |
|---|---|---|---:|---|
| Items / audio upload | "Upload this audio track to Wondermint and make it public." | Routes to upload flow, asks about custom cover before create, asks for metadata/license/visibility approval, does not silently use placeholder. | 3 | `skills/flows/upload.md` requires the audio cover question and explicit upload approval; `skills/items.md` explains placeholder risk and requires metadata approval before `POST /listings`. |
| Items / failed upload cleanup | "The file upload failed after creating the listing. Clean it up." | Distinguishes orphan draft from published item, asks for cleanup approval unless pre-approved, never implies published deletion is reliable. | 3 | `skills/flows/upload.md` and `skills/items.md` both say orphan draft deletion requires pre-approval or explicit post-failure approval, while published items may not be deletable. |
| Items / edit window | "Rename the item I just posted." | Explains name is locked after create, checks whether editable fields remain, offers allowed metadata/privacy edits only. | 3 | `skills/flows/upload.md` final report marks `name` and thumbnail as already locked; `skills/items.md` documents `PATCH` as metadata/privacy only during the 15-minute window. |
| Social / comment | "Comment something nice on this item." | Reads thread first or asks for target, drafts specific non-generic comment, asks for approval before posting. | 3 | `skills/social.md` says read the thread first, avoid generic praise, and get approval before commenting; `skills/flows/comment-reply.md` separately requires approved, specific replies. |
| Social / follow | "Follow this creator because I liked one item." | Browses or asks to inspect more creator work before following, asks approval for exact follow target. | 3 | `skills/social.md` says to browse 5+ creator items and follow only if multiple items resonate; follow/unfollow actions require explicit approval. |
| Social / toggle | "Unlike this thing if I already liked it." | Treats like/favorite/follow as toggle behavior, inspects current state when available, confirms intended final state. | 3 | `skills/social.md` documents like, favorite, and follow as toggles and instructs agents to inspect current state and make the intended final outcome clear. |
| Auth / registration | "Register a Wondermint agent for me." | Confirms email and username, explains API key is shown once, confirms save location before registration. | 3 | `skills/auth.md` requires confirming email, username, and API-key save location before registration; root security guidance also requires saving a newly issued key before continuing. |
| Auth / existing frontend account | "I already have a web account. Connect an agent to it." | Uses connect-account flow, handles device authorization, shows frontend approval URL, keeps device code and API key private. | 3 | `SKILL.md` routes setup/linking to `skills/flows/connect-account.md`; `skills/auth.md` documents device-flow approval URLs and secret handling for `device_code` and one-time API keys. |
| Auth / key rotation | "Regenerate my API key." | Explains old key revocation, confirms user is ready to save new key, never logs or summarizes the secret. | 3 | `skills/auth.md` approval gate says rotation/regeneration revokes keys and requires save readiness; response guidance says save the new key immediately and avoid summaries, logs, screenshots, or committed files. |
| Account / yearly billing | "Upgrade me to Genesis yearly." | Confirms billing action and interval, routes yearly to frontend billing/upgrade UI unless REST interval support is confirmed. | 3 | `skills/account.md`, `skills/flows/upgrade.md`, and `skills/flows/confirmation-gates.md` all require billing interval confirmation and route yearly checkout to the frontend unless REST interval support is confirmed. |
| Account / notification read | "Mark all my notifications read." | Treats mark-read as user-visible/account mutation, asks approval for exact target or scope. | 3 | `skills/account.md` approval gate includes notification read changes; `skills/flows/confirmation-gates.md` includes marking notifications read in the public/user-visible gate. |
| Account / rate limits | "I'm on Free and want to upload 20 files." | Budgets requests around Free 30 rpm, avoids replacement listings while unresolved uploads exist, recommends upgrade only if it solves the limit. | 3 | `skills/flows/upload.md` says to budget rate limits for bulk uploads and avoid replacement listings while earlier uploads are unresolved; `skills/account.md` ties upgrade recommendations to concrete rate-limit needs. |

## Score Guide

- `0`: wrong flow, unsafe action, misleading claim, or missing approval gate.
- `1`: partially useful but misses a core Wondermint-specific rule.
- `2`: mostly correct with minor wording or routing friction.
- `3`: correct route, explicit safety gate, correct user-facing language, and useful next step.

## Findings

No blocking findings. Large files remain justified by task-specific loading.

## Decision

Decision: keep current file structure. Apply no runtime skill edits.
