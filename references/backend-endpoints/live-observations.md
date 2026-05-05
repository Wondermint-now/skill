# Live Endpoint Observations

This file accumulates facts learned from real Wondermint testing. Use it to
close the gap between static backend source review and the actual responses,
messages, formatting, and edge cases observed in staging or production.

Do not paste secrets, full API keys, passwords, cookies, private user data, or
raw signed upload/download URLs. Redact sensitive values before committing.

## How To Add An Observation

Add one entry per endpoint behavior that changes what the skill should know.
Keep entries short and link to raw evidence under `evals/logs/` when available.

```markdown
## YYYY-MM-DD - METHOD /api/v1/path

- Environment:
- Evidence:
- Request shape confirmed:
- Response shape confirmed:
- Success message / status:
- Error message / hint / next observed:
- Formatting notes:
- Skill docs to update:
- Confidence: observed once | observed multiple times | source-confirmed
```

## 2026-05-05 - Initial Live Eval Findings

- Environment: staging, `https://api-staging.fullstock.ai`
- Evidence: `evals/scorecards/live-2026-05-05.md`, `evals/logs/live-2026-05-05/`
- Endpoints touched: registration, profile, home, notifications, categories,
  marketplace browse, item detail.
- Response shape confirmed: basic read-only agent flows worked with API-key
  auth after registration.
- Error message / hint / next observed: `GET /api/v1/agents/marketplace` with
  unsupported `first` pagination returned `400`; corrected `limit/page`
  pagination returned `200`.
- Formatting notes: committed live evidence redacts `api_key`.
- Operational note: Python's default HTTP client was blocked by Cloudflare
  1010, while `curl` succeeded.
- Skill docs to update: live-eval flow, marketplace pagination guidance.
- Confidence: observed once.

