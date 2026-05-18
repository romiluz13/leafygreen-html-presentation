# Plain-Language Content Voice for MongoDB Presentations

Use when the audience includes non-technical people, PMs, executives, or mixed rooms who should leave able to **talk with builders**.

## The goal

By the end, someone who never wrote code should be able to:
- Explain the topic in their own words
- Ask a smart follow-up question
- Tell when someone is hand-waving vs. being concrete

## Rules

### 1. Lead with outcomes, not architecture
- ❌ "OpenClaw embeds Pi via createAgentSession()"
- ✅ "OpenClaw is an assistant you install once — it talks to you on WhatsApp and can use your tools"

### 2. Define before you abbreviate
First mention must include plain English:
| Jargon | First say |
|--------|-----------|
| ReAct | "think → act → check → repeat" |
| RAG | "search your documents before answering" |
| MCP | "a standard plug for connecting tools — like USB-C for AI" |
| Gateway | "the inbox that receives your WhatsApp/Slack messages" |
| Harness | "the software that runs the think-act loop" |

### 3. Use analogies
- Chatbot = consultant who only talks
- Agent = assistant who can also use your tools
- Framework = building blocks — you design the house
- Runtime = furnished apartment — move in and customize
- Visual platform = IKEA — assemble on a screen

### 4. Include a phrasebook slide
For each term:
1. **Term** (what builders say)
2. **Plain** (one sentence)
3. **Ask builders** (a question that shows you understand)

### 5. Include "questions that make builders take you seriously"
Examples:
- What happens when the model picks the wrong action?
- Where does memory live — can we export or delete it?
- What does this cost at our expected usage?
- Does it survive a restart mid-task?

### 6. Separate categories before comparing products
Wrong: "OpenClaw vs LangChain"
Right: "Personal assistant vs framework — different jobs"

### 7. Reality checks on hype
- GitHub stars ≠ production-ready
- Demos ≠ deployments that ran last week unattended
- Open source ≠ safe by default

## Slide density

- Max **5 bullets** per content slide
- Tables: max **5 rows** visible — split if needed
- One idea per slide
- Section dividers every 4–6 slides

## Speaker notes

Every slide needs `<aside class="notes">` with:
- What to emphasize
- Analogy to use if the room looks lost
- What to skip if short on time

## Tone

Confident, curious, honest. Not salesy. Not insider-baseball.
