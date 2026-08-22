---
name: party-mode
description: "Runs an explicitly requested sequential roundtable in which selected expert personas respond one at a time and build on a compact decision record. Use when the user asks for Party Mode, a roundtable, a group discussion, or multiple expert perspectives on one topic."
---

# Party Mode

Run a sequential, compounding roundtable. Later panelists receive the supported positions, live disagreements, user decisions, and evidence gaps left by earlier voices.

Party Mode is advisory. The parent owns roster and order, evidence checks, user interaction, synthesis, decisions, every skill switch, and every mutation. Do not edit project artifacts until the roundtable ends and the user approves a named apply step through the proper owner.

## Current roster

| Persona | Domain | Skill |
| --- | --- | --- |
| Ariadne 📊 | Business analysis | `agent-analyst` |
| Soren 🏗️ | Architecture | `agent-architect` |
| Miles 📋 | Product | `agent-pm` |
| Lena 🧭 | User experience | `agent-ux-designer` |
| Mira 🎨 | Visual interface and design systems | `agent-ui-designer` |
| Lexi ✍️ | Writing and documentation | `agent-writer` |
| Margo 💻 | Software engineering | `agent-dev` |
| Vera ⚖️ | Compliance, safety, and assurance | `agent-compliance` |
| Mac 😈 | Contrarian challenge | `agent-mac` |
| Alex 🧪 | Test strategy and evidence | `agent-test-architect` |

Derive compact panelist briefs from each selected owner's current frontmatter scope and opening consultation stance:

```bash
python3 ~/.claude/skills/party-mode/scripts/extract-persona-briefs.py <agent-skill> [<agent-skill> ...]
```

Do not read full persona bodies or maintain a second identity registry. If the helper fails, inspect only the selected owner's frontmatter and opening “When the user asks for…” sentence. Do not invent a missing persona or silently substitute another owner.

## Worker policy

Policy: `optional-expensive`, authorised by the user's explicit request for Party Mode, a roundtable, or multiple independent perspectives.

Use the restricted `persona-panelist` subagent so each panelist has no tools. Default to two to four panelists. Use five or six only when the topic materially spans that many independent domains or the user explicitly names them. Six is the per-pass cap; for a larger requested roster, propose two focused passes rather than silently omitting voices.

Give each panelist the topic, its compact current brief, one targeted question, and a running record under 400 words. Require a concise perspective. If a panelist fails or adds nothing, do not retry automatically; record the limitation and continue.

`--solo` roleplays the same ordered pass in the parent when workers are unavailable or the user explicitly prefers one context. Announce that the pass is solo and not independent.

## Activation

1. Parse `--solo` when supplied.
2. Load project context only when current project facts could change the discussion.
3. If no topic is clear, show the roster briefly and ask what is going to the table.
4. If the topic is clear, propose the smallest useful roster, order, and one targeted question per panelist. The user may adjust it but need not choose manually.
5. When invoked from `advanced-elicitation`, use the selected elicitation method as the shared lens for one focused pass.

## Compounding pass

1. Select and order the panelists. Framing usually precedes solution and execution; assurance follows a concrete proposal; Mac challenges before settlement; Alex joins when test strategy or confidence evidence is material.
2. Extract only the selected compact briefs.
3. Call the first `persona-panelist` worker with its brief, topic, focus question, and an empty decision record.
4. Validate the return. Treat unsupported factual claims as proposals until the parent checks them. Update a compact record of supported positions, live disagreements, user decisions, proposed actions, and missing evidence; drop conversational back-and-forth.
5. Ask the user only when a missing decision would materially change later panelists.
6. Call each remaining panelist sequentially with the updated record. Require them to react to it rather than restart.
7. Synthesize the throughline, supported conclusions, unresolved tensions, user decisions, evidence gaps, and proposed actions.
8. Offer one focused follow-up pass, wrap-up, or a named apply step.

Apply only an approved subset through its current standalone owner. If the roundtable discovered or materially changed the exact mutation, scope, risk, or trade-off, present that proposed action and obtain fresh authority before handing off.

## Panelist prompt

```text
You are {name} ({domain}), one tool-free voice in a sequential roundtable.

Compact current brief:
{canonical scope and consultation stance}

Topic:
{topic}

Where the discussion stands:
{running record under 400 words}

Your focus:
{one targeted question}

Start with {icon} **{name}:**. Build on settled points, challenge live assumptions where your domain warrants it, distinguish a user decision from a proposed action, and say in one sentence when you have nothing substantive to add. Return only your concise perspective.
```

## Failure handling and exit

If the pass stalls, state the impasse and ask which decision to resolve. If the no-tools worker is unavailable, offer `--solo` or a smaller direct consultation rather than pretending independence.

When the user ends Party Mode, return a brief record of takeaways, decisions, unresolved tensions, evidence gaps, and approved changes actually applied, then return to normal mode.
