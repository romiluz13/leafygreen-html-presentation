# LeafyGreen HTML Presentation

A [Cursor Agent Skill](https://cursor.com/docs/context/skills) for building **MongoDB LeafyGreen–branded HTML slide decks** with [reveal.js](https://revealjs.com/).

Single-file output. No build step for viewers. Speaker notes built in.

## Features

- MongoDB design tokens (`@leafygreen-ui/palette` mapped to CSS)
- Euclid Circular A + MongoDB Value Serif fonts
- reveal.js: fragments, overview, speaker view (**S**), fullscreen
- JSON → HTML builder script
- Plain-language content guidelines for mixed audiences
- Bridge to `setup-leafygreen` + `leafygreen-authoring` for React decks

## Install (Cursor)

### Personal skill (all projects)

```bash
git clone https://github.com/romiluz13/leafygreen-html-presentation.git \
  ~/.cursor/skills/leafygreen-html-presentation
```

### Project skill (repo-specific)

```bash
git clone https://github.com/romiluz13/leafygreen-html-presentation.git \
  .cursor/skills/leafygreen-html-presentation
```

Restart Cursor or start a new chat, then invoke:

```
/leafygreen-html-presentation Create a 10-slide deck about [topic]
```

## Quick build (no agent)

```bash
git clone https://github.com/romiluz13/leafygreen-html-presentation.git
cd leafygreen-html-presentation

python scripts/build-reveal.py examples/sample-slides.json my-deck.html
open my-deck.html
```

## Presenter shortcuts

| Key | Action |
|-----|--------|
| ← → | Previous / next slide |
| **O** | Overview grid |
| **S** | Speaker notes window |
| **F** | Fullscreen |

## Repository structure

```
leafygreen-html-presentation/
├── SKILL.md                 # Agent instructions
├── README.md
├── examples.md
├── examples/
│   └── sample-slides.json
├── references/
│   ├── design-tokens.md     # palette.* → CSS (required reading)
│   ├── leafygreen-theme.css # Drop-in theme
│   ├── template.html
│   ├── slide-patterns.md
│   ├── content-voice.md
│   ├── react-deck-setup.md
│   └── mongodb-logomark.svg
└── scripts/
    └── build-reveal.py      # JSON → branded HTML
```

## Related skills

- **setup-leafygreen** — Vite + React + LeafyGreen provider setup
- **leafygreen-authoring** — React component conventions

Use this skill for **shareable HTML**. Use the React skills for **interactive decks**.

## License

MIT — see [LICENSE](LICENSE).

MongoDB, LeafyGreen, and related marks are trademarks of MongoDB, Inc.
