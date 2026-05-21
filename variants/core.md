# Core Variant

## Identity

- Variant: `core`
- Package names: `wondermint`, `skills/wondermint`
- Version tag prefix: `core-v`
- Current version: `core-v0.1.7`
- Plugin name: `wondermint`

## Scope

The core variant is the default Wondermint skill. It covers account setup,
check-ins, uploads, discovery, social actions, portfolios, playlists, feeds,
rate-limit recovery, billing plan management, and webhooks.

The core variant may use existing browse/search route names such as
`/marketplace` for public content discovery. It must not include transactional
marketplace workflows:

- buying or purchasing items
- selling items or configuring sale terms
- order management
- seller or marketplace analytics
- payouts, balances, earnings, or settlement workflows

## Release Evidence

Core releases require a matching scorecard under `evals/scorecards/` with:

- `Variant: core`
- `Marketplace transactions included: no`
- the exact tag or intended tag
- static validation evidence

Use tags such as `core-v0.1.7` for new core releases. Existing historical tags
`v0.1.0` through `v0.1.6` belong to the core line.
