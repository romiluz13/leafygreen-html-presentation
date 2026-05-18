# Slide HTML Patterns

Copy into `<div class="slides">`. Colors must match [design-tokens.md](design-tokens.md).

## Title slide

```html
<!-- palette.green.dark3 -->
<section class="title-slide" data-background-color="#001E2B">
  <span class="lg-badge">May 2026</span>
  <h1>Presentation Title</h1>
  <h3>Subtitle in plain language</h3>
  <aside class="notes">Welcome. Set expectations for the room.</aside>
</section>
```

## Section divider

```html
<!-- palette.green.dark2 -->
<section class="section-slide" data-background-color="#023430">
  <p class="section-label">Part 1</p>
  <h2>Section title</h2>
  <aside class="notes">Transition line for the speaker.</aside>
</section>
```

## Content with animated bullets

```html
<section>
  <h2>What you'll walk away with</h2>
  <ul>
    <li class="fragment fade-up">First outcome</li>
    <li class="fragment fade-up">Second outcome</li>
    <li class="fragment fade-up">Third outcome</li>
  </ul>
  <aside class="notes">Keep this under 60 seconds.</aside>
</section>
```

## Table

Use `class="small"` on `<section>` when more than 4 rows.

```html
<section class="small">
  <h2>At a glance</h2>
  <table class="lg-table">
    <thead>
      <tr><th>Column A</th><th>Column B</th></tr>
    </thead>
    <tbody>
      <tr><td>Row 1</td><td>Detail</td></tr>
    </tbody>
  </table>
  <aside class="notes">Walk row by row — don't read the table verbatim.</aside>
</section>
```

## Phrasebook / glossary card

```html
<section class="small">
  <h2>Terms you'll hear</h2>
  <div class="lg-card-grid">
    <div class="lg-card fragment">
      <strong class="lg-accent">MCP</strong>
      <p>Standard way to plug tools into agents — like USB-C for AI.</p>
      <p class="lg-muted">Ask builders: "Do you support MCP?"</p>
    </div>
  </div>
  <aside class="notes">Cover 3–4 terms live; rest is reference.</aside>
</section>
```

## Blockquote

```html
<section>
  <h2>Key insight</h2>
  <blockquote>When someone says "revolutionary," ask what changed outside the loop.</blockquote>
  <aside class="notes">Pause after the quote.</aside>
</section>
```

## Code block

```html
<section>
  <h2>The agent loop</h2>
  <pre><code data-trim data-line-numbers>
User goal → AI decides → Tool runs → Check result → Repeat
  </code></pre>
  <aside class="notes">Technical audience only — skip for mixed rooms.</aside>
</section>
```

## Vertical (nested) slides

Use for sub-topics under one heading:

```html
<section>
  <section><h2>Topic</h2></section>
  <section><h3>Sub-topic A</h3><p>Detail</p></section>
  <section><h3>Sub-topic B</h3><p>Detail</p></section>
</section>
```

## Closing slide

```html
<!-- palette.green.dark3 -->
<section class="title-slide center-slide" data-background-color="#001E2B">
  <h1>Questions?</h1>
  <h3>You are now part of the conversation</h3>
  <aside class="notes">Thank the room. Stay for hallway questions.</aside>
</section>
```

## Fragment styles

`fade-in`, `fade-up`, `fade-down`, `fade-left`, `fade-right`, `highlight-green`, `highlight-blue`

## Presenter shortcuts

| Key | Action |
|-----|--------|
| ← → | Previous / next |
| O | Overview grid |
| S | Speaker notes window |
| F | Fullscreen |
| Esc | Exit overview / notes |
