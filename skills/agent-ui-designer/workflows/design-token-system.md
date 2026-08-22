# Design-Token System

Create, ingest, audit, migrate, publish, or govern one canonical visual token and shared-pattern system. Keep experience behaviour with `agent-ux-designer`, visual direction in this owner's UI specification, implementation layout in application code, and reusable visual decisions in this workflow.

## Select the operation

| Need | Operation |
| --- | --- |
| No coherent token source exists, a theme or brand input needs a complete system, or required roles are missing | Generate |
| Brand guidance, design-tool exports, screenshots, or visual explorations need reconciliation with the current system | Ingest |
| Tokens, styles, guides, references, patterns, or generated outputs may have drifted | Audit |
| Legacy values, classes, components, or token names need safe movement to the canonical system | Migrate |
| Canonical tokens must feed Tailwind, Style Dictionary, CSS, design tools, native platforms, documentation, or CI | Publish |
| A visual decision's owner, extension rule, deprecation, exception, or release impact must be decided | Govern |

An explicit operation or clear request selects it directly without UX consultation or another workflow as preflight. Combine operations only when the requested finished result genuinely requires them; otherwise finish or checkpoint one before selecting the next.

Audit and advisory governance are report-only. A broad "audit and fix" request authorises assessment, not changes whose exact target, scope, compatibility impact, rollback, or visual trade-off becomes knowable only through the audit. Present the findings and proposed mutation, then obtain confirmation before applying that newly determined change.

Generate, ingest, migrate, publish, or requested governance edits may change the canonical token source, shared patterns, requested guides or visual references, generated outputs, and expressly implicated consumers. Confirm before a broad call-site migration, replacement of an established canonical format, meaning-changing rename, alias or deprecation removal, manual edit to generated output, or write to an external design system. If the exact bounded change and consequences were already established and authorised, proceed without another ceremony.

## Resolve the current system

Inspect the supplied project and relevant configuration before choosing a format or adding files:

- canonical token or theme sources and their aliases;
- generated outputs, build configuration, package versions, and consumers;
- shared classes or components that own reusable visual chrome;
- established or missing placement, alignment, and ordering conventions for repeated action types (modal action rows, page-level primary actions, table-row actions, toolbar actions) and where transient patterns (banners, toasts, notifications) sit relative to nearby controls;
- UX specifications, pattern guides, visual references, brand guidance, and design-tool exports;
- representative style call sites, including inline styles and framework utilities; and
- supported browsers, platforms, themes, accessibility targets, and release constraints.

Treat the configured build and actual consumers as evidence of authority. Do not create a second token system because another format is fashionable. External brand, Figma, Tokens Studio, screenshot, or reference-site material is input to reconcile, not an authority that silently overwrites the current source.

Keep these responsibilities distinct:

| Artifact | Owns | Must not become |
| --- | --- | --- |
| Canonical token source | Actual reusable visual values, aliases, themes, and machine-readable metadata | A prose design rationale or a generated duplicate |
| Shared pattern layer | Reusable component or class chrome assembled from tokens | Per-screen layout or another token source |
| Pattern or design-system guide | Intent, names, usage, status, exceptions, deprecations, and migration guidance | A copy of literal token values |
| Visual reference | A rendered view of canonical or clearly provisional variables | An independent source of visual decisions |
| UI specification | Visual intent, component appearance, composition, and token-role requirements | The canonical value store |
| UX specification | Experience intent, interaction behaviour, copy, and state requirements | A source of literal visual values |

## Maintain a coherent token model

- Define every reusable visual decision once and consume it through a token or shared pattern. Keep genuine one-off layout local; do not turn every coordinate into a token.
- Prefer role or purpose names for public tokens. Keep internal ramps or primitives behind semantic roles where that improves generation or theming.
- Cover the categories the product actually uses: canvas and surface, text and border, brand and action, semantic state, categorical differentiation, typography, spacing, control sizing, radius, elevation and focus, breakpoints, and motion when present.
- Keep brand, action, semantic-state, and categorical colours distinct even when their current values coincide.
- Add component tokens only for a real component, variant, platform output, or compatibility need. Otherwise use semantic tokens plus one shared component or class implementation.
- Preserve existing supported scales and naming unless they cause a concrete conflict. A generated default is not evidence that a mature system should be renamed.
- Keep accessibility in the system definition. Test final resolved text-bearing pairs, focus treatments, non-colour cues, and every supported theme; formula choice alone does not prove accessibility.

Read [the implementation reference](../references/design-token-implementation.md) only when generating values, creating or changing a token format or export pipeline, or technically validating colour and build behaviour.

## Operate safely

### Generate or ingest

Map supplied brand, UX requirements, and UI direction to explicit roles before creating values. If several visual directions remain plausible, use a token-rendered comparison with provisional variables and obtain the user's choice before promoting one direction into the canonical source.

If the user asked only to extract, compare, or critique an external reference, return candidate primitives, roles, and transferable principles, then stop before creating starter files or touching the current system. Preserve design-tool aliases that express real intent, collapse accidental duplicates only after showing the mapping, and do not treat a design-tool mode as a runtime theme without a deliberate consumer mapping.

Adopt the current format and scales when they are sound. With no established format, choose the smallest source that serves the actual consumers; do not add a multi-platform pipeline to a single simple web application without a demonstrated need.

Generate the necessary foundations as one coherent system, including light and dark or other themes only when the product supports them. Record unresolved brand, contrast, font licensing, platform, or consumer decisions rather than inventing certainty.

### Audit

Check for:

- raw colour, spacing, type, radius, shadow, focus, control-size, or breakpoint values outside approved sources and exceptions;
- duplicate component chrome or variants that should use one shared pattern;
- the same action type (e.g. a modal's primary/cancel actions, a page's primary action, a table row's actions) placed, ordered, or aligned differently across screens with no canonical convention recorded;
- a transient pattern (banner, toast, notification) mounted so its appearance or removal can reposition a nearby control, rather than in a position that keeps surrounding chrome stable;
- token guides that restate values and visual references that define their own values;
- brand, state, and categorical roles used interchangeably;
- stale, manually edited, missing, or conflicting generated outputs;
- unresolved or circular aliases, deep-merge collisions, and mixed token-format conventions;
- design-tool or reference inputs promoted without role mapping, contrast checks, or confirmation; and
- deprecated tokens introduced in new work or removed before consumers migrated.

Do not flag canonical definitions, generated outputs that match their source, static brand assets, quoted accessibility thresholds, or isolated third-party overrides that cannot consume the system. Report exact locations, consequence, corrective direction, and uncertainty. When drift exists but no canonical convention has been chosen yet (placement, ordering, or otherwise), report the drift and the candidate conventions already in use; do not select or apply one without confirmation.

### Migrate

Separate reusable chrome from local layout. Build an explicit mapping from legacy values, names, utilities, or classes to canonical roles and patterns. Preserve compatibility aliases while consumers move, mark replacements and removal conditions, and migrate in bounded verifiable slices unless a broad sweep was explicitly authorised.

When introducing shared classes or patterns, check naming, specificity, cascade, and global-style collisions rather than assuming a new name is isolated. After each slice, verify visual behaviour, supported themes, accessibility, build output, and remaining usage. For a placement, ordering, or notification-reflow fix specifically, verify against an actual render (start the app, trigger the relevant state, inspect or screenshot the result) rather than static review alone — positional correctness depends on runtime layout, not just source. Update migration status in the existing guide when one exists; do not create a guide solely to narrate the work.

### Publish

Choose one canonical input and generate every other platform representation from it. Inspect the current Tailwind, Style Dictionary, DTCG, design-tool, native-platform, or custom build contract before emitting syntax.

Add only checks that can make a release decision more reliable: source build succeeds, generated outputs match, aliases resolve without cycles or collisions, required consumers exist, contrast checks pass, raw visual values stay within approved locations, and deprecated tokens are not introduced in new work.

Treat token names and shared patterns as a project API. Classify equivalent corrections as patch-like, additive roles as minor-like, and removals or meaning changes as breaking; use deprecation and replacement paths before removal.

### Govern

Classify a disputed decision as canonical token value, shared pattern, UX intent, implementation layout, generated output, or deliberate exception. Put each part in its owner and state the split when a decision crosses boundaries.

Keep exception and migration status honest: on-system, provisional, deprecated with replacement, deliberate exception with reason, or known gap. An exception must name why the shared system cannot serve the case and when it should be revisited.

## Documents and finished result

For a new standalone pattern guide or rendered visual reference, resolve the `design-system-guide` or `visual-reference` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md). A companion to an existing UX or design-system artifact uses sidecar naming beside that parent. App-embedded style guides remain application code.

Finish by reporting the operation, canonical source, consumers and outputs inspected, exact changes or findings, compatibility aliases and deprecations, migration state, checks run, unresolved decisions, and next owner when UI specification, UX, product-interface implementation, accessibility testing, or release assurance remains. Token and shared-pattern migration may update bounded consumers; unrelated product behaviour stays with `agent-dev`. A no-op result states why the current system already satisfies the request.
