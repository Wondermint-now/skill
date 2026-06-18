# Marketplace Variant

## Identity

- Variant: `marketplace`
- Package name: `skills/wondermint-marketplace`
- Version tag prefix: `marketplace-v`
- Current version: `marketplace-v0.1.0`
- Plugin name: `wondermint-marketplace`

## Scope

The marketplace package is the only active installable skill in this repo. It
includes the broader Wondermint workflows plus a separate boundary for direct
REST marketplace workflows.

Marketplace workflows may include only REST API endpoints for:

- publishing or unpublishing owned listings
- direct buying and purchase-status polling
- purchase history
- access, download, and estimate checks
- listing transaction history
- non-auction market analytics

## Structure

Marketplace uses this active package structure:

- `SKILL.md` routes high-level user intent.
- `skills/marketplace.md` is the direct marketplace router and shared boundary.
- `skills/flows/marketplace-buy.md` handles direct buying and purchase polling.
- `skills/flows/marketplace-publish.md` handles publish, unpublish, pricing,
  and estimates.
- `skills/flows/marketplace-access.md` handles purchase history, access,
  downloads, and metadata.
- `skills/flows/marketplace-analytics.md` handles analytics, transactions,
  performance, trends, rankings, and exports.
- `skills/references/marketplace-endpoints.md` is endpoint lookup for
  non-analytics marketplace routes.
- `skills/references/marketplace-analytics-endpoints.md` is endpoint lookup for
  analytics routes.

## Release Gate

Do not treat a marketplace package as release-ready until it has:

- endpoint references for each marketplace workflow being exposed
- explicit approval gates for financial, public, or irreversible actions
- error and recovery guidance for each marketplace endpoint
- marketplace analytics kept in its own flow and endpoint reference
- a matching scorecard under `evals/scorecards/`
- passing `python3 repo-workflows/validate.py --variant marketplace`

## Explicit Exclusions

Do not add these to the marketplace variant:

- GraphQL operations, queries, mutations, or `/graphql`
- auctions
- bids
- offers, counter-offers, accepts, rejects, or offer cancellation
- operator workflows
- account-linking, claim-link, or agent-link endpoints
- payout, settlement, or earnings workflows until explicitly re-scoped

Marketplace releases use tags such as `marketplace-v0.1.0`.
