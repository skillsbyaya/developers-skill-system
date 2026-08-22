# UI Specification

Create, update, validate, or critique the visual interface definition for a settled experience. Make the product clear, coherent, distinctive, accessible, and implementable without changing the underlying journey or interaction contract.

## Resolve the current state

Identify the product area, accepted experience requirements, current `EXPERIENCE.md` and `DESIGN.md` when present, brand inputs, existing interface and component system, token sources, visual references, supported contexts, implementation constraints, and unresolved visual choices.

Choose the operation:

- **Create:** no current visual interface definition exists for the scope.
- **Update:** accepted product, UX, brand, evidence, or implementation constraints require bounded changes.
- **Validate or critique:** judge visual clarity, coherence, distinctiveness, accessibility, system fit, and implementability without rewriting unless requested.

Start from supplied current artifacts and interfaces rather than imposing an ideal sequence. Preserve settled UX behaviour and existing supported design-system decisions unless evidence creates a material conflict.

## Define the visual interface

Cover only the decisions the scope earns:

1. **Visual thesis:** the product-specific character, trust or emotional intent, and the principles that resolve likely visual trade-offs.
2. **Hierarchy and composition:** grouping, emphasis, scan order, density, whitespace, alignment, content priority, and responsive rearrangement.
3. **Typography and language:** type roles, emphasis, measure, rhythm, numerals or data presentation, and how text hierarchy supports the accepted copy.
4. **Colour and imagery:** brand, action, semantic-state, categorical, surface, and content roles; imagery, illustration, iconography, and data-visualisation treatment where relevant.
5. **Components and patterns:** visual anatomy, appearance variants, hierarchy, density, responsive treatment, focus, feedback, and token or shared-pattern dependencies for the behavioural states defined by UX.
6. **Motion and transition:** purposeful feedback, continuity, hierarchy, and reduced-motion alternatives when motion materially helps.
7. **Responsive visual behaviour:** how composition, density, type, imagery, controls, and navigation presentation adapt across supported contexts without changing UX-owned priority or behaviour.

When alternatives are useful, produce meaningfully different visual directions rather than palette swaps. Each needs a concise thesis, signature element, product fit, risks, token implications, and the evidence or preference that would decide between them.

## Boundary with UX and tokens

`agent-ux-designer` defines what users need to understand and do, the information and journey structure, interaction behaviour, copy, states, and accessibility requirements. This workflow defines how those requirements are visually expressed.

Own visual role names, component appearance, composition, and rationale here. Do not duplicate literal token values in the specification. Use current token names when they exist; otherwise state provisional role requirements and hand them to this owner's design-token-system workflow.

If visual exploration reveals a material problem in hierarchy of information, journey, behaviour, copy, or state meaning, report it to `agent-ux-designer` rather than silently redesigning the experience. If a brand or product-position choice is unresolved, return it to `agent-pm` or the user.

## Visual references

Create a rendered comparison or reference only when seeing the interface materially improves a decision or the user asks for one. Render canonical token variables where available; clearly label provisional variables and never let a sidecar become an independent source of truth.

For a durable reference, use the `visual-reference` convention or sidecar naming beside the scoped UX artifact. App-embedded style-guide or preview pages remain application code and require the relevant implementation authority.

## Write and finish

For durable output, resolve the `ux` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md). Use the existing scoped UX folder and update `DESIGN.md` with visual thesis, hierarchy, composition, responsive presentation, component appearance, visual roles, token and pattern dependencies, reference links, implementation guidance, and unresolved visual decisions.

Do not rewrite `EXPERIENCE.md`. Report any conflict or required UX update to `agent-ux-designer`. Preserve stable supported visual decisions, reconcile contradictions, and remove stale content rather than appending history.

Validate that:

- the visual design expresses rather than alters the accepted experience;
- hierarchy, affordance, feedback, state distinctions, and responsive presentation are clear, recurring controls (navigation, primary and output actions) keep consistent placement across analogous screens, and layout stays stable when state- or async-driven text appears (loading, errors, confirmations, changing button labels);
- accessibility does not depend on colour, motion, or subtle styling alone;
- brand, action, semantic-state, and categorical roles remain distinct;
- components and patterns reuse the current system or state justified additions;
- visual references render canonical or clearly provisional roles;
- placement and layout-stability judgements are confirmed against the rendered interface (run or sandbox) when static inspection cannot settle them — token and value drift show in code, spatial and layout-shift drift do not; and
- implementation constraints, evidence limits, open decisions, and downstream owners are explicit.

Return the operation, scope, `DESIGN.md` and visual-reference paths changed or reviewed, visual decisions or findings, token and shared-pattern requirements, unresolved UX or product choices, evidence limits, and next owner. Validation and critique are report-only; obtain fresh authority before applying materially determined design changes.
