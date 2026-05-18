---
name: leafygreen-html-presentation
description: >-
  Builds MongoDB-branded HTML presentations using reveal.js and LeafyGreen design
  tokens (Euclid Circular A, Value Serif, green dark palette). Use when the user
  asks for slides, a deck, a presentation, HTML slides, reveal.js, LeafyGreen
  slides, MongoDB-branded talks, speaker notes, or a shareable file for colleagues.
  Default output is a single .html file — no npm required for viewers.
disable-model-invocation: true
---

# LeafyGreen HTML Presentation

Build **single-file, shareable HTML slide decks** with MongoDB LeafyGreen branding — powered by [reveal.js](https://revealjs.com/) via CDN.

## Quick start

```
Task Progress:
- [ ] Step 1: Confirm audience and format
- [ ] Step 2: Write slide content (plain language if mixed room)
- [ ] Step 3: Generate HTML from template + theme
- [ ] Step 4: Add speaker notes to every slide
- [ ] Step 5: Open in browser and verify controls
```

**Step 1 — Confirm audience and format**

| Audience | Content guide | Default format |
|----------|---------------|----------------|
| Mixed / non-technical | [content-voice.md](references/content-voice.md) | reveal.js HTML |
| Engineering deep-dive | Technical detail OK | reveal.js HTML |
| Interactive demo needed | — | `setup-leafygreen` + `leafygreen-authoring` (React) |

**Default:** reveal.js single `.html` unless the user explicitly wants React.

**Step 2 — Structure slides**

Standard arc: **title → agenda → section dividers → content → takeaways → Q&A**

Max 5 bullets per slide. Split dense tables across slides.

**Step 3 — Generate HTML**

1. Read [design-tokens.md](references/design-tokens.md) — **required before writing any CSS**
2. Start from [template.html](references/template.html)
3. Paste **full** [leafygreen-theme.css](references/leafygreen-theme.css) into `<style>` (fonts from setup-leafygreen Step 4)
4. Include [mongodb-logomark.svg](references/mongodb-logomark.svg) in header (`color="green-base"` equivalent)
5. Add slides using [slide-patterns.md](references/slide-patterns.md)

Or run the builder when content is JSON:

```bash
python scripts/build-reveal.py slides.json output.html
```

**Step 4 — Speaker notes**

Every slide needs `<aside class="notes">`. Presenter presses **S** in browser.

**Step 5 — Verify**

Open the file locally. Test: ← →, **O** overview, **S** speaker view, **F** fullscreen.

## Design compliance (setup-leafygreen + leafygreen-authoring)

**Before delivering any deck**, confirm:

### HTML decks (this skill)

- [ ] Colors map to `palette.*` tokens in [design-tokens.md](references/design-tokens.md) — no random hex
- [ ] Fonts are CloudFront URLs from **setup-leafygreen Step 4** (Euclid Circular A + MongoDB Value Serif)
- [ ] Body background is `palette.green.dark3` (`#001E2B`)
- [ ] H2 / accents use `palette.green.base` (`#00ED64`)
- [ ] Muted text uses `palette.gray.base` (`#89979B`), body uses `palette.gray.light2`
- [ ] Borders use `palette.gray.dark2` (`#3D4F58`)
- [ ] Cards/slide surfaces use `palette.black` with `palette.gray.dark2` border
- [ ] Header includes MongoDB logomark (`green-base` green)
- [ ] HTML patterns map to LG components per design-tokens.md table

### React decks (setup-leafygreen path)

Follow [react-deck-setup.md](references/react-deck-setup.md) — all 7 setup steps, `LeafyGreenProvider darkMode={true}`, `@leafygreen-ui/palette` for colors, LeafyGreen components only (no plain `<button>`, `<table>`, etc.).

## LeafyGreen brand tokens

Full token reference: [design-tokens.md](references/design-tokens.md)

Stylesheet (paste verbatim): [leafygreen-theme.css](references/leafygreen-theme.css)

## reveal.js layout (header / footer chrome)

Fixed `.lg-header` and `.lg-footer` sit outside the reveal canvas. The theme:

- Insets `.reveal` with `--lg-chrome-top` / `--lg-chrome-bottom` so slides centre in the remaining viewport
- Uses flexbox on sections (`justify-content: center`) for vertical centring
- Compacts `.content-slide` and `.small` card grids so dense slides fit without clipping
- Sets `center: true` and `margin: 0.08` in `Reveal.initialize`

If a slide still overflows, add `class="small"` to the section or split content across slides.

## reveal.js config

Always initialize with notes, highlight, hash, and slide numbers:

```javascript
Reveal.initialize({
  hash: true,
  slideNumber: 'c/t',
  transition: 'slide',
  plugins: [ RevealNotes, RevealHighlight ]
});
```

CDN pins: `reveal.js@5` from jsDelivr. See [template.html](references/template.html).

## Content voice

For talks with PMs, execs, or mixed rooms:

- Lead with outcomes, not architecture
- Define jargon on first use (see phrasebook pattern)
- Use analogies before acronyms
- Include "questions to ask builders" slide
- GitHub stars ≠ production-ready

Full guide: [content-voice.md](references/content-voice.md)

## Quality checklist

Before delivering:

- [ ] Design compliance section above — all boxes checked
- [ ] Single `.html` opens in browser (CDN OK)
- [ ] Speaker notes on every slide
- [ ] ≤ 5 bullets per content slide
- [ ] Title and section slides visually distinct
- [ ] Tested ← →, **O**, **S**, **F**

## When to use React instead

Use `setup-leafygreen` + `leafygreen-authoring` when the deck needs:
- Live LeafyGreen components (Button, Card, Table, Badge)
- Interactive widgets or embedded demos
- A dev-server workflow with hot reload

Use **this skill** when the goal is **share one file** (Slack, email, static host).

## Examples

See [examples.md](examples.md). Sample JSON: [examples/sample-slides.json](examples/sample-slides.json).

## Additional resources

- [design-tokens.md](references/design-tokens.md) — palette.* → CSS (required)
- [react-deck-setup.md](references/react-deck-setup.md) — setup-leafygreen + leafygreen-authoring bridge
- [slide-patterns.md](references/slide-patterns.md) — HTML slide templates
- [leafygreen-theme.css](references/leafygreen-theme.css) — drop-in CSS
- [mongodb-logomark.svg](references/mongodb-logomark.svg) — header logo
- [content-voice.md](references/content-voice.md) — plain-language rules
- [template.html](references/template.html) — minimal starter
- [scripts/build-reveal.py](scripts/build-reveal.py) — JSON → HTML
