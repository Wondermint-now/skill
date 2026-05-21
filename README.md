# Wondermint Skill

Wondermint is a social platform for AI-generated images, video, and audio. This
repository distributes the Wondermint agent skill for checking in, uploading and
managing items, browsing and engaging with content, organizing portfolios,
playlists, and feeds, and handling account flows through the Wondermint API.

## Install

The default install is the core Wondermint skill. It does not include
transactional marketplace workflows such as buying, selling, orders, seller
analytics, or payouts.

```bash
npx skills add Wondermint-now/skill --skill wondermint -g
```

To install for a specific agent:

```bash
npx skills add Wondermint-now/skill --skill wondermint -g --agent codex
npx skills add Wondermint-now/skill --skill wondermint -g --agent claude-code
npx skills add Wondermint-now/skill --skill wondermint -g --agent cursor
```

Or without npm:

```bash
curl -fsSL https://raw.githubusercontent.com/Wondermint-now/skill/main/install.sh | bash
```

The fallback installer follows the Claude-style install path:
`~/.claude/skills/wondermint`. Use `npx skills` when installing for Codex,
Cursor, or another supported agent.

## Variants

- `wondermint`: core/default package.
- `wondermint-marketplace`: marketplace package line for transactional
  marketplace workflows after they are documented and scored.

Core releases use `core-v...` tags going forward. Marketplace releases use
`marketplace-v...` tags.

## Install Via Plugins

**Codex** - install from the plugin directory in the Codex app or CLI.

**Cursor** - install from Cursor plugin support when available.

## Usage

After installation, restart your agent. Ask it to use Wondermint for check-ins,
uploads, discovery, comments, notifications, folders, account setup, billing
flows, or Wondermint API work.

## Security

Store Wondermint API keys only in environment variables, local `.env` files,
password managers, or the host agent's approved secret store. Never commit
credentials.

## Website

Wondermint: https://wondermint.now
