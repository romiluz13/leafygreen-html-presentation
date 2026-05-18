# Examples

## Example 1: Mixed-audience tech talk

**Prompt:**
> Create a MongoDB-branded HTML presentation about [topic] for a mixed room. Plain language. Include a phrasebook slide and speaker notes.

**Agent workflow:**
1. Read [references/content-voice.md](references/content-voice.md)
2. Structure ~20–30 slides: title → agenda → sections → phrasebook → takeaways → Q&A
3. Build from [references/template.html](references/template.html) + [references/leafygreen-theme.css](references/leafygreen-theme.css)
4. Output single `.html` file

---

## Example 2: JSON-driven build

**Prompt:**
> Build the deck from slides.json

**Commands:**
```bash
python scripts/build-reveal.py examples/sample-slides.json my-talk.html
open my-talk.html
```

---

## Example 3: Product update (5 slides)

**Prompt:**
> Quick 5-slide MongoDB-branded update: title, problem, solution, metrics, Q&A

**Slide outline:**
1. Title — product name + date badge
2. Problem — 3 fragment bullets
3. Solution — before/after table
4. Metrics — 2–3 numbers with green accent
5. Q&A closing slide

---

## Example 4: When NOT to use this skill

**Prompt:**
> Build a presentation with live LeafyGreen Button and Card components

**Route to:** `setup-leafygreen` + `leafygreen-authoring` (Vite + React)

---

## slides.json schema

```json
{
  "title": "Presentation Title",
  "slides": [
    {
      "type": "title",
      "title": "Main Title",
      "subtitle": "Subtitle",
      "badge": "May 2026",
      "notes": "Speaker notes here"
    },
    {
      "type": "content",
      "title": "Slide heading",
      "bullets": ["Point 1", "Point 2"],
      "quote": "Optional blockquote",
      "notes": "Speaker notes"
    },
    {
      "type": "section",
      "title": "Part 1",
      "subtitle": "Section subtitle",
      "notes": "Transition"
    },
    {
      "type": "table",
      "title": "Comparison",
      "table": {
        "headers": ["A", "B"],
        "rows": [["1", "2"]]
      },
      "notes": "Notes"
    },
    {
      "type": "glossary",
      "title": "Phrasebook",
      "glossary": [
        {
          "term": "MCP",
          "plain": "Standard plug for AI tools",
          "askBuilders": "Do you support MCP?"
        }
      ],
      "notes": "Notes"
    },
    {
      "type": "closing",
      "title": "Questions?",
      "subtitle": "Thank you",
      "notes": "Notes"
    }
  ]
}
```

Slide types: `title`, `section`, `content`, `table`, `glossary`, `closing`
