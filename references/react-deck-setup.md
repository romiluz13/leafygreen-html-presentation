# React Presentation Deck Setup

When a deck needs **live LeafyGreen components** (Button, Card, Badge, Table, IconButton), follow `setup-leafygreen` and `leafygreen-authoring` exactly — do not improvise.

## Decision

| Need | Path |
|------|------|
| Share one HTML file | This skill — reveal.js + [leafygreen-theme.css](leafygreen-theme.css) |
| Interactive React deck | `setup-leafygreen` steps 1–7 + `leafygreen-authoring` |

## setup-leafygreen checklist (required)

Run all steps in order from `setup-leafygreen`:

1. Vite + React + TypeScript scaffold
2. Install packages (`leafygreen-provider`, `button`, `typography`, `tokens`, `icon`, `icon-button`, `logo`) + `vite-plugin-node-polyfills`
3. `vite.config.ts` — `dedupe` + `alias` for React (prevents invalid hook call)
4. `main.tsx` — `LeafyGreenProvider` as **default import**, `darkMode={true}`
5. `index.css` — **replace entire file** with setup-leafygreen Step 4 fonts + body reset only
6. Clear `App.css` — template styles break LeafyGreen colors
7. `npm run dev` + `npm run build` verify

## leafygreen-authoring rules for slide components

- **Typography:** `H1`, `H2`, `H3`, `Body`, `Subtitle` — never raw `<h1>` / `<p>`
- **Controls:** `Button`, `IconButton` — never raw `<button>`
- **Data:** `Table`, `HeaderRow`, `Row`, `HeaderCell`, `Cell` — never raw `<table>`
- **Labels:** `Badge` — never raw `<span>` chips
- **Surfaces:** `Card` — never raw `<div>` cards
- **Logo:** `<MongoDBLogoMark height={24} color="green-base" />` — never `darkMode` prop
- **Colors:** `import { palette } from '@leafygreen-ui/palette'` — never hard-coded hex in TSX
- **Imports:** named imports for LG components; `Icon` and `LeafyGreenProvider` are default exports

## React 19 type errors

Add `{/* @ts-ignore - React 19 polymorphic type mismatch */}` before `Button`, `IconButton`, `Card`, and typography components if `tsc` fails. Components render correctly — see setup-leafygreen `references/gotchas.md`.

## File structure

```
src/
├── main.tsx          # LeafyGreenProvider here only
├── App.tsx           # Presentation shell
├── slides.ts         # Slide content + speaker notes
└── components/
    └── SlideContent.tsx
```

One component per file, PascalCase names, explicit TypeScript interfaces — per leafygreen-authoring.

## Sync HTML ↔ React content

Keep `slides.json` or `slides.ts` as single content source. Export to HTML:

```bash
npx tsx -e "import { slides } from './src/slides.ts'; ..."
python ~/.cursor/skills/mongodb-presentations/scripts/build-reveal.py slides.json shareable.html
```
