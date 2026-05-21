# Marketplace Variant

## Identity

- Variant: `marketplace`
- Package names: `wondermint-marketplace`, `skills/wondermint-marketplace`
- Version tag prefix: `marketplace-v`
- Current version: `marketplace-v0.1.0`
- Plugin name: `wondermint-marketplace`

## Scope

The marketplace variant starts from the core Wondermint skill and adds a
separate boundary for transactional marketplace workflows.

Marketplace workflows may include:

- buying or purchasing items
- selling items or configuring sale terms
- order lookup and order management
- seller analytics and marketplace analytics
- payouts, balances, earnings, or settlement workflows

## Release Gate

Do not treat a marketplace package as release-ready until it has:

- endpoint references for each marketplace workflow being exposed
- explicit approval gates for financial, public, or irreversible actions
- error and recovery guidance for each marketplace endpoint
- a matching scorecard under `evals/scorecards/`
- passing `python3 repo-workflows/validate.py --variant marketplace`

Marketplace releases use tags such as `marketplace-v0.1.0`.
