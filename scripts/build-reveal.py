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


def section_class_attr(*names: str) -> str:
    cleaned = [n for n in names if n]
    return f' class="{" ".join(cleaned)}"' if cleaned else ""


def slide_sections(slide: dict) -> list[str]:
    stype = slide.get("type", "content")
    title = slide.get("title", "")
    notes = slide.get("notes", "")

    if stype == "title":
        return [slide_html(slide)]

    if stype == "glossary" and slide.get("glossary"):
        items = slide["glossary"]
        chunk_size = 4
        chunks = [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]
        sections: list[str] = []
        for index, chunk in enumerate(chunks):
            chunk_slide = {
                **slide,
                "title": title if len(chunks) == 1 else f"{title} ({index + 1}/{len(chunks)})",
                "glossary": chunk,
            }
            sections.append(glossary_html(chunk_slide))
        return sections

    if stype == "content" and slide.get("bullets") and len(slide["bullets"]) > 5:
        chunks = [slide["bullets"][i : i + 5] for i in range(0, len(slide["bullets"]), 5)]
        sections = []
        for index, chunk in enumerate(chunks):
            chunk_slide = {
                **slide,
                "title": title if len(chunks) == 1 else f"{title} ({index + 1}/{len(chunks)})",
                "bullets": chunk,
                "quote": slide.get("quote") if index == 0 else None,
            }
            sections.append(content_html(chunk_slide))
        return sections

    return [slide_html(slide)]


def glossary_html(slide: dict) -> str:
    title = esc(slide.get("title", ""))
    notes = esc(slide.get("notes", ""))
    notes_block = f'<aside class="notes">{notes}</aside>' if notes else ""
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


def content_density_classes(slide: dict) -> str:
    classes: list[str] = []
    bullet_list = slide.get("bullets", [])
    if slide.get("contentSlide"):
        classes.append("content-slide")
    if len(bullet_list) >= 5 or slide.get("quote") or max((len(b) for b in bullet_list), default=0) > 90:
        classes.append("small")
    if len(bullet_list) > 5:
        classes.append("dense")
    return " ".join(classes)


def content_html(slide: dict) -> str:
    title = esc(slide.get("title", ""))
    notes = esc(slide.get("notes", ""))
    notes_block = f'<aside class="notes">{notes}</aside>' if notes else ""
    body_parts = []
    if slide.get("bullets"):
        body_parts.append(bullets(slide["bullets"]))
    if slide.get("quote"):
        body_parts.append(f"<blockquote>{esc(slide['quote'])}</blockquote>")
    class_attr = section_class_attr(*content_density_classes(slide).split())
    return f"""      <section{class_attr}>
        <h2>{title}</h2>
        {"".join(body_parts)}
        {notes_block}
      </section>"""


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
        row_count = len(t.get("rows", []))
        classes = []
        if row_count > 3:
            classes.append("small")
        if row_count > 6:
            classes.append("dense")
        class_attr = section_class_attr(*classes)
        return f"""      <section{class_attr}>
        <h2>{title}</h2>
        {table(t["headers"], t["rows"])}
        {notes_block}
      </section>"""

    if stype == "glossary" and slide.get("glossary"):
        return glossary_html(slide)

    if stype == "showcase" and slide.get("cards"):
        subtitle = esc(slide.get("subtitle", ""))
        subtitle_html = (
            f'<p class="lg-muted" style="margin-bottom: 0.6em;">{subtitle}</p>' if subtitle else ""
        )
        cards = []
        for card in slide["cards"]:
            lines = "".join(f"<p>{esc(line)}</p>" for line in card.get("lines", []))
            cards.append(
                f"""        <div class="lg-card fragment fade-up">
          <strong class="lg-accent">{esc(card["title"])}</strong>
          {lines}
        </div>"""
            )
        grid = "\n".join(cards)
        return f"""      <section class="content-slide">
        <h2>{title}</h2>
        {subtitle_html}
        <div class="lg-card-grid">
{grid}
        </div>
        {notes_block}
      </section>"""

    if stype == "code" and slide.get("code"):
        caption = esc(slide.get("caption", ""))
        caption_html = f'<p class="lg-muted fragment">{caption}</p>' if caption else ""
        code = esc(slide["code"])
        return f"""      <section>
        <h2>{title}</h2>
        <pre><code data-trim data-line-numbers>
{code}
        </code></pre>
        {caption_html}
        {notes_block}
      </section>"""

    return content_html(slide)


def build(deck: dict) -> str:
    title = esc(deck.get("title", "Presentation"))
    footer = esc(deck.get("footer", "MongoDB · Internal"))
    slides = deck.get("slides", [])
    all_sections: list[str] = []
    for slide in slides:
        all_sections.extend(slide_sections(slide))
    sections = "\n\n".join(all_sections)
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
  <div class="lg-footer">{footer}</div>
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
      center: true,
      margin: 0.08,
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
    section_count = sum(len(slide_sections(s)) for s in deck.get("slides", []))
    print(f"Wrote {section_count} slides → {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
