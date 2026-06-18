# Wondermint Marketplace Skill

This repository now focuses on the Wondermint Marketplace agent skill. The
active installable package is `skills/wondermint-marketplace`.

The archived core Wondermint skill copies live under `archive/` for historical
reference only. Do not treat archived files as release candidates or active
installable packages.

## Install

Install the Marketplace skill with:

```bash
npx skills add Wondermint-now/skill --skill wondermint-marketplace -g
```

To install for a specific agent:

```bash
npx skills add Wondermint-now/skill --skill wondermint-marketplace -g --agent codex
npx skills add Wondermint-now/skill --skill wondermint-marketplace -g --agent claude-code
npx skills add Wondermint-now/skill --skill wondermint-marketplace -g --agent cursor
```

Or without npm:

```bash
curl -fsSL https://raw.githubusercontent.com/Wondermint-now/skill/main/install.sh | bash
```

The fallback installer follows the Claude-style install path:
`~/.claude/skills/wondermint-marketplace`. Use `npx skills` when installing for
Codex, Cursor, or another supported agent.

## Scope

Wondermint Marketplace covers Wondermint check-ins, uploads, discovery, social
actions, folders, account flows, and documented REST-only marketplace workflows
such as buying, publishing, access, downloads, estimates, listing transactions,
and non-auction analytics.

Excluded marketplace scope remains explicit: no GraphQL, auctions, bids,
offers, operator workflows, account-linking endpoints, payouts, settlements, or
earnings workflows unless they are deliberately re-scoped later.

## Validation

```bash
python3 repo-workflows/validate.py --variant all
```

`--variant all` currently means all active variants, which is Marketplace only.

## Security

Store Wondermint API keys only in environment variables, local `.env` files,
password managers, or the host agent's approved secret store. Never commit
credentials.

## Website

Wondermint: https://wondermint.now
