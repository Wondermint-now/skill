# Free Upload Rate-Limit Guidance Review - 2026-05-09

## Scope

Dry review for making uploads smoother for Free users under the 30 requests per
minute plan limit.

## Prompts

- "Upload these 10 items on my Free plan as smoothly as possible."
- "I hit the request limit while uploading. What now?"

## Expected Behavior

- Check `GET /api/v1/agents/rate-limit` before batches.
- Treat Free as 30 requests/minute.
- Prefer one active upload at a time when reliability matters.
- Reserve budget for create, confirm, and status checks.
- Avoid tight status polling.
- Wait for `Retry-After` or `resets_at` instead of starting risky create calls
  when budget is low.
- If a Free user hits the limit, explain the pause and mention that upgrading
  raises plan-level request limits: Unleashed to 120 rpm, Genesis to 600 rpm.
- Do not turn upgrade messaging into a generic pitch when pacing is sufficient.

## Result

Pass.

## Evidence

- `skills/flows/upload.md` now gives a Free-user upload rhythm and explains what
  to do on `429 RATE_LIMITED`.
- `skills/reference.md` now has a `Free Upload Pacing` section.
- `skills/flows/error-recovery.md` now says how to explain Free-plan rate-limit
  pauses and when to mention upgrade limits.

## Validation

Command:

```bash
python3 repo-workflows/validate.py
```

Result:

```text
Wondermint validation passed.
```
