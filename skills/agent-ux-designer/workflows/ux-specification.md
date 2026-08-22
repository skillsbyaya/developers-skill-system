# UX Specification

Create, update, or validate formal experience requirements that guide product, UI design, implementation, and later assurance without deciding visual styling or duplicating product requirements.

## Resolve the current state

Identify the product area, affected users and journeys, desired outcome, current product decisions, existing UX folder or artifact, implementation constraints, evidence, and unresolved UX choices.

Start from supplied briefs, requirements, motivation maps, research, prototypes, architecture constraints, existing interfaces, UI designs, and validation evidence when they are relevant. They are inputs, not mandatory predecessors. Reuse current accepted decisions and update the existing specification rather than restarting.

Choose the operation:

- **Create:** no current specification exists for the scope.
- **Update:** accepted evidence or decisions require bounded changes.
- **Validate:** judge completeness, coherence, implementability, accessibility, and conflicts without rewriting unless requested.

Batch material user-owned choices. Do not require confirmation after every section or force a fixed sequence when the direction is already settled.

## Define the experience

Cover only decisions needed for this scope:

1. **Users and context:** relevant users, task, mental model, active motivations, constraints, and evidence limits.
2. **Experience intent:** core action, desired progress, emotional or trust goal, success signals, and principles that resolve likely trade-offs.
3. **Information architecture:** content hierarchy, navigation, entry points, orientation, progressive disclosure, and cross-journey consistency.
4. **Journeys and flows:** initiation, decisions, feedback, completion, interruption, abandonment, failure, recovery, permissions, and return.
5. **Interaction and copy:** controls, system feedback, focus and keyboard behaviour, motion intent, labels, instructions, confirmations, empty states, and errors.
6. **States and boundaries:** loading, empty, partial, stale, offline or degraded, error, success, disabled, permission, destructive, and recovery states that are reachable for this product.
7. **Responsive and inclusive behaviour:** how priority, layout, navigation, input, density, and feedback adapt across supported contexts; assistive technology, reduced motion, colour use, readable hierarchy, focus, and target requirements.

Use Mermaid or another diagram only when it makes a journey, hierarchy, state transition, or relationship materially easier to understand.

## Find the elegant move

Before specifying a new control, name the progress the user is trying to make and the work the current experience makes them do: decisions, recall, data entry, translation, navigation, waiting, coordination, or recovery. Do not accept the existing screen, step, or division of labour as fixed unless it is a product or technical constraint.

Look for the simplest coherent shift that improves the surrounding journey:

1. **Remove:** eliminate a decision, mode, repeated input, explanation, or state that does not contribute to the user's outcome.
2. **Reassign:** let the system retain, derive, validate, prefill, group, or automate work when it can do so reliably. Show material assumptions and make them easy to inspect and correct.
3. **Resequence:** put information and action at the moment and place they become relevant; preserve context rather than sending users elsewhere to complete a small dependency.
4. **Match the mental model:** use the user's objects, vocabulary, and natural order so intent maps directly to action and visible outcome without translation into system structure.
5. **Reveal progressively:** keep the common path calm while making advanced capability discoverable and exceptional complexity available when it becomes relevant.
6. **Close the loop:** respond at the locus of action, preserve place and entered work, and make the resulting state and next possible move apparent.

When the first answer merely repackages the current pattern, generate alternatives that change different layers of the experience rather than cosmetic variants. Compare them by conceptual load, causal clarity, continuity, agency, accessibility, consistency, implementation constraints, and how naturally they handle exceptions and recovery. Prefer the option that removes the most user work with the fewest new concepts or special cases. A longer but legible path can be more elegant than an opaque shortcut; invisible automation, surprise, and novelty are not elegance by themselves.

## Resolve consequential interactions

When an action could lose work, affect other people, create a commitment, change access, spend money, expose information, or be difficult to reverse, do not begin by choosing a confirmation component. Define the plausible error, its likelihood and consequence, what remains recoverable, when the consequence takes effect, and what the user knows at that moment.

Resolve the risk at the lowest-cost layer that is sufficient:

1. Remove invalid or accidental paths through constraints, safer defaults, appropriate separation, or better timing.
2. Preserve state or provide a reliable recovery path; make its scope and limits clear.
3. Put the concrete action and consequence where the choice is made, using outcome-labelled choices rather than generic assent.
4. Add a deliberate commitment step only for material risk that the earlier layers do not control. Its effort must address the actual failure mode and remain operable by keyboard and assistive technology without depending on speed, precision, sustained movement, colour, or motion alone.
5. After the action, show what happened, its scope, when it takes effect, and the available recovery or next step.

Do not make routine warnings so frequent that users learn to dismiss them. A blocking confirmation is warranted only when the action is plausibly accidental, materially consequential, and not adequately recoverable or preventable. Explain any non-obvious or downstream effect before commitment without obscuring the choice with boilerplate.

## Define interface requirements and the UI handoff

- Specify reusable interaction patterns and components by purpose, content, actions, behaviour, states, variants, keyboard and assistive-technology expectations, and recovery.
- State what visual hierarchy must communicate, which distinctions must remain perceivable, and which responsive priorities or density constraints the UI design must honour.
- Name required semantic roles or shared patterns without choosing literal colours, typography values, spacing, radii, shadows, control heights, or token architecture.
- Keep behavioural state distinct from visual treatment: UX defines what loading, error, success, disabled, destructive, or permission states mean and do; `agent-ui-designer` defines their visual expression.
- Record unresolved visual direction, brand expression, component appearance, visual-reference, or design-system work as a handoff to `agent-ui-designer`.

## Write the artifact

For durable output, resolve the `ux` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md). Use its scoped UX folder and update `EXPERIENCE.md` for users, context, evidence, experience principles, journeys, flows, interaction, copy, states, responsive priorities, accessibility, UI requirements, and validation needs.

Update an existing folder in place. Preserve stable supported decisions, reconcile contradictions, and remove stale content rather than appending a workflow history. Do not rewrite `DESIGN.md`; report any conflict or required UI update to `agent-ui-designer`.

## Validate and finish

Check that:

- every material user claim is evidenced or labelled as inference or assumption;
- journeys cover relevant failure, interruption, permission, and recovery paths;
- the chosen interaction reduces user work and conceptual load without hiding capability, assumptions, or state;
- consequential interactions use the least burdensome sufficient safeguard and communicate the actual outcome before commitment;
- interaction, copy, states, accessibility, and responsiveness are implementable;
- product, UX, UI, and architecture sources do not make competing claims;
- component behaviour and state requirements are complete enough for UI design and implementation; and
- open decisions, evidence gaps, validation needs, and downstream owners are explicit.

Return the operation, scope, `EXPERIENCE.md` path, decisions made, material changes or findings, unresolved choices, evidence limits, UI handoff, and next owner. Do not automatically begin visual design, implementation, or assurance.
