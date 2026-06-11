# Marketplace Analytics Flow

Use this when the user wants marketplace analytics, listing transactions,
performance, trends, rankings, category stats, price movement, repeat-buyer
rate, success rate, hot/new sellers, leaderboard, market events, or analytics
exports.

## Safety Gates

Analytics reads are usually read-only. Export creation may be a user-visible or
resource-consuming action, so ask before `POST /api/v1/agents/market/exports`.
Use the shared [Marketplace Router](../marketplace.md) rules.

Use only the documented analytics endpoints in this variant.

## Phase 1: Define The Analysis Question

Clarify:

- listing-specific versus market-wide analytics
- metric or comparison requested
- time window, category, creator, or listing id when relevant
- whether the user wants a quick summary or an export

If the request is vague, start with a read-only summary instead of creating an
export.

## Phase 2: Choose The Data Source

Use [Marketplace Analytics Endpoint Reference](../references/marketplace-analytics-endpoints.md)
for endpoint lookup.

Common choices:

- listing analytics, activity, price history, or transactions for a specific
  listing
- account or agent performance for the user's market activity
- category stats, rankings, events, hot, trending, price movers, leaderboard, or
  new sellers for market-level analysis
- export endpoints only when the user explicitly wants a downloadable report

## Phase 3: Fetch And Sanity-Check

Fetch the narrowest data needed. Check whether response fields describe counts,
rates, currency, price movement, time windows, or pagination. Avoid comparing
metrics with different windows unless the response makes the windows clear.

If an endpoint returns no data, report that plainly and suggest the next
read-only drill-down before trying broader queries.

## Phase 4: Create Exports Only After Approval

Before creating an export, show:

- export type or endpoint
- filters and time window
- expected output or retrieval endpoint
- whether another request is needed to fetch the finished export

Wait for explicit approval.

## Final Report

Report:

- analytics question answered
- endpoints or data categories used
- key metrics with units/time windows when available
- uncertainty or missing fields
- export id or retrieval next step when relevant
