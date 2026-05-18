#!/usr/bin/env python3
"""Build a MongoDB LeafyGreen reveal.js HTML deck from slides JSON."""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
THEME_CSS = (SKILL_DIR / "references" / "leafygreen-theme.css").read_text(encoding="utf-8")
LOGO_SVG = (SKILL_DIR / "references" / "mongodb-logomark.svg").read_text(encoding="utf-8").strip()


def esc(text: str) -> str:
    return html.escape(text)


def bullets(items: list[str], fragment: bool = True) -> str:
    cls = ' class="fragment fade-up"' if fragment else ""
    lis = "".join(f"<li{cls}>{esc(b)}</li>" for b in items)
    return f"<ul>{lis}</ul>"


def table(headers: list[str], rows: list[list[str]]) -> str:
    thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body = ""
    for row in rows:
        tds = "".join(f"<td>{esc(c)}</td>" for c in row)
        body += f"<tr>{tds}</tr>"
    return f'<table class="lg-table"><thead><tr>{thead}</tr></thead><tbody>{body}</tbody></table>'


def slide_html(slide: dict) -> str:
    stype = slide.get("type", "content")
    title = esc(slide.get("title", ""))
    notes = esc(slide.get("notes", ""))
    notes_block = f'<aside class="notes">{notes}</aside>' if notes else ""

    if stype == "title":
        subtitle = esc(slide.get("subtitle", ""))
        badge = esc(slide.get("badge", ""))
        badge_html = f'<span class="lg-badge">{badge}</span>' if badge else ""
        extra = ""
        if slide.get("bullets"):
            extra = f'<p class="lg-muted">{esc(slide["bullets"][0])}</p>'
        return f"""      <section class="title-slide" data-background-color="#001E2B">
        {badge_html}
        <h1>{title}</h1>
        <h3>{subtitle}</h3>
        {extra}
        {notes_block}
      </section>"""

    if stype == "section":
        subtitle = esc(slide.get("subtitle", ""))
        return f"""      <section class="section-slide" data-background-color="#023430">
        <p class="section-label">{title}</p>
        <h2>{subtitle}</h2>
        {notes_block}
      </section>"""

    if stype == "closing":
        subtitle = esc(slide.get("subtitle", ""))
        body = bullets(slide.get("bullets", []), fragment=False) if slide.get("bullets") else ""
        return f"""      <section class="title-slide center-slide" data-background-color="#001E2B">
        <h1>{title}</h1>
        <h3>{subtitle}</h3>
        {body}
        {notes_block}
      </section>"""

    if stype == "table" and slide.get("table"):
        t = slide["table"]
        small = ' class="small"' if len(t.get("rows", [])) > 4 else ""
        return f"""      <section{small}>
        <h2>{title}</h2>
        {table(t["headers"], t["rows"])}
        {notes_block}
      </section>"""

    if stype == "glossary" and slide.get("glossary"):
        cards = []
        for item in slide["glossary"]:
            cards.append(
                f"""        <div class="lg-card fragment">
          <strong class="lg-accent">{esc(item["term"])}</strong>
          <p>{esc(item["plain"])}</p>
          <p class="lg-muted">Ask builders: “{esc(item["askBuilders"])}”</p>
        </div>"""
            )
        grid = "\n".join(cards)
        return f"""      <section class="small">
        <h2>{title}</h2>
        <div class="lg-card-grid">
{grid}
        </div>
        {notes_block}
      </section>"""

    body_parts = []
    if slide.get("bullets"):
        body_parts.append(bullets(slide["bullets"]))
    if slide.get("quote"):
        body_parts.append(f"<blockquote>{esc(slide['quote'])}</blockquote>")

    return f"""      <section>
        <h2>{title}</h2>
        {"".join(body_parts)}
        {notes_block}
      </section>"""


def build(deck: dict) -> str:
    title = esc(deck.get("title", "Presentation"))
    slides = deck.get("slides", [])
    sections = "\n\n".join(slide_html(s) for s in slides)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/black.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css">
  <style>
{THEME_CSS}
  </style>
</head>
<body>
  <header class="lg-header" aria-label="MongoDB">
    {LOGO_SVG}
    <span class="lg-header-title">{title}</span>
  </header>
  <div class="lg-footer">MongoDB · Internal</div>
  <div class="reveal">
    <div class="slides">

{sections}

    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
  <script>
    Reveal.initialize({{
      hash: true,
      slideNumber: 'c/t',
      transition: 'slide',
      plugins: [ RevealNotes, RevealHighlight ]
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: build-reveal.py slides.json output.html", file=sys.stderr)
        return 1
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    deck = json.loads(src.read_text(encoding="utf-8"))
    dst.write_text(build(deck), encoding="utf-8")
    print(f"Wrote {len(deck.get('slides', []))} slides → {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
