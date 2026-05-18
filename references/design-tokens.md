# LeafyGreen Design Tokens for HTML Presentations

CSS cannot import `@leafygreen-ui/palette` at runtime. Map **`palette.*` token names** to CSS custom properties — same values as `setup-leafygreen` and `leafygreen-authoring`.

Source of truth: `@leafygreen-ui/palette` (React apps import from here, not `@leafygreen-ui/tokens`).

## Required CSS variables

Paste into `:root` in [leafygreen-theme.css](leafygreen-theme.css):

```css
:root {
  /* palette.green */
  --palette-green-dark3: #001E2B;   /* palette.green.dark3 — page background */
  --palette-green-dark2: #023430;   /* palette.green.dark2 — section slides */
  --palette-green-dark1: #00684A;   /* palette.green.dark1 */
  --palette-green-base:  #00ED64;   /* palette.green.base — H2, accents */
  --palette-green-light1: #71F6BA;
  --palette-green-light2: #BCFFDB;

  /* palette.gray */
  --palette-gray-dark4: #112E39;    /* palette.gray.dark4 — card alt surface */
  --palette-gray-dark3: #1C2D33;
  --palette-gray-dark2: #3D4F58;    /* palette.gray.dark2 — borders */
  --palette-gray-dark1: #5C6C75;
  --palette-gray-base:  #89979B;    /* palette.gray.base — muted text */
  --palette-gray-light2: #E8EDF4;  /* palette.gray.light2 — body text */

  /* palette.blue */
  --palette-blue-base: #016BF8;     /* palette.blue.base — links, progress */

  /* palette.black / white */
  --palette-black: #000000;         /* palette.black — slide surface */
  --palette-white: #FFFFFF;
}
```

## Token → usage map (dark mode decks)

| Token | Use in slides |
|-------|----------------|
| `palette.green.dark3` | Viewport background, title slides (`data-background-color`) |
| `palette.green.dark2` | Section divider slides |
| `palette.green.base` | H2, section labels, accents, controls, table headers |
| `palette.gray.light2` | Body text, H1 on content slides |
| `palette.gray.base` | Muted text, footer, slide numbers |
| `palette.gray.dark2` | Borders — tables, cards, slide frame |
| `palette.black` | Slide card surface (matches React `Card` on dark bg) |
| `palette.blue.base` | Links, progress bar start |

## Typography (verbatim from setup-leafygreen Step 4)

| Role | Font | Weight |
|------|------|--------|
| H1, H2, H3 | MongoDB Value Serif | 400 |
| Body, bullets, tables | Euclid Circular A | 400 |

Font URLs — copy exactly from `setup-leafygreen` Step 4 CloudFront URLs. Do not substitute Google Fonts or system-only stacks.

## HTML → React component mapping

When upgrading a deck to React (`setup-leafygreen`), map HTML patterns to LeafyGreen components per `leafygreen-authoring`:

| HTML pattern | LeafyGreen component |
|--------------|------------------------|
| `.lg-badge` | `<Badge variant="lightgray">` |
| `.lg-card` | `<Card>` |
| `.lg-table` | `<Table>`, `<HeaderRow>`, `<Row>`, `<HeaderCell>`, `<Cell>` |
| `h1` / `h2` | `<H1>`, `<H2>`, `<H3>` from `@leafygreen-ui/typography` |
| body text | `<Body>`, `<Subtitle>` |
| `.lg-logo` | `<MongoDBLogoMark height={24} color="green-base" />` |
| nav buttons | `<IconButton>`, `<Button size="small">` |

React decks: wrap in `<LeafyGreenProvider darkMode={true}>` in `main.tsx` only. Follow all 7 steps in `setup-leafygreen`.

## Rules (from leafygreen-authoring)

1. **Never use random hex** — every color must map to a `palette.*` token above
2. **Never substitute plain HTML** for UI in React decks when a LeafyGreen component exists
3. **darkMode={true}** on provider for presentation decks (matches setup-leafygreen default)
4. **MongoDBLogoMark** — use `color="green-base"` on dark backgrounds (not `darkMode` prop)

## reveal.js `data-background-color`

reveal.js requires literal hex on sections. Use only these values:

- Title / closing: `#001E2B` (`palette.green.dark3`)
- Section dividers: `#023430` (`palette.green.dark2`)

Add an HTML comment with the token name when using inline hex.
