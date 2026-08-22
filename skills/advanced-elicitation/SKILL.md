---
name: advanced-elicitation
description: "Runs iterative, method-led refinement of an existing draft, section, idea, or answer. Use when the user asks for advanced elicitation, wants to choose a structured elicitation method, or wants repeated user-approved passes that deepen, challenge, expand, or improve supplied or recently generated content."
---

# Advanced Elicitation

Improve a current piece of content through one or more user-selected elicitation methods.

## Operating rules

- Keep one accepted working version separate from each proposed pass.
- Follow the interaction loop in order and stop whenever it requires the user's response.
- Treat accepted changes as updates to the conversational working version. Do not edit an artifact merely because the user accepted an elicitation pass; return accepted content to the invoking owner or wait for a separate request to apply it.
- Use the normal assistant style unless the selected method calls for a named viewpoint or the user explicitly combines the session with Party Mode.

## Entry

Load [the method registry](methods.csv). If no current content is obvious, ask which draft, section, idea, or answer should be refined before presenting methods.

When invoked by another skill or process:

1. Receive the current content and the decision or outcome it needs to support.
2. Run the elicitation loop against that content.
3. Return the accepted working version when the user selects `x`.
4. Let the invoking owner decide whether and how to apply it under that owner's normal authority.

If Party Mode is already active or the user explicitly asks to combine it with elicitation, invoke `party-mode` for roster, worker, and synthesis rules. Use the selected elicitation method as the roundtable's common lens; do not maintain a persona roster here.

## Select methods

The registry contains:

- `category`: method grouping;
- `method_name`: display name;
- `description`: purpose and best-fit context; and
- `output_pattern`: a flexible execution shape.

Use the conversation and current content to assess content type, complexity, stakeholders, consequence, uncertainty, and creative potential. Select five strong methods with a useful mix of foundational and specialised approaches. Put the strongest matches first.

Present:

```text
Advanced Elicitation Options
If Party Mode is active, selected personas may join in.
Choose a number (1-5), [r] to Reshuffle, [a] to List All, or [x] to Proceed:

1. [Method Name]
2. [Method Name]
3. [Method Name]
4. [Method Name]
5. [Method Name]
r. Reshuffle
a. List all methods
x. Proceed / no further elicitation
```

## Interaction loop

### Numbered method

1. Apply the selected method to the accepted working version using its registry description and output pattern.
2. Adapt depth and form to the content, consequence, and available evidence.
3. Show the proposed enhanced version and a concise account of what changed or was revealed.
4. Ask whether to accept the proposed changes into the working version (`y`, `n`, or another instruction), then stop for the response.
5. On acceptance, replace the working version. On rejection, discard the proposal. Follow direct revision instructions as given.
6. Re-present the same `1-5, r, a, x` choices.

If the user selects several numbers, execute them in sequence as one combined pass on the accepted working version, then ask once whether to accept the combined proposal.

### Reshuffle

Offer five fresh methods, preserving category diversity and putting the strongest current matches first.

### List all

List every method and its description in a compact table. Let the user select any method by name or number, then use the numbered-method loop.

### Direct feedback

Apply the requested revision to the working version, make the resulting content clear, and re-present the choices.

### Proceed

Return the accepted working version. If it is unclear which proposals were accepted, ask what should carry forward before claiming completion.

## Execution rules

- Use the registry description to preserve the method's real purpose; use the output pattern as guidance rather than a rigid template.
- Tie every pass to the current content and its intended decision or outcome.
- Show concise rationale, assumptions, checks, or comparison criteria when useful. Do not expose private hidden reasoning.
- Distinguish evidence, user-supplied facts, inference, generated alternatives, and unresolved uncertainty.
- For named or multiple viewpoints, identify each lens clearly. Use Party Mode only when it is already active or the user explicitly requested independent perspectives; otherwise apply the viewpoints inline without claiming independence.
- Each accepted method builds on the latest accepted working version.
- Always return to the choice prompt after a method pass until the user selects `x`.
