# Design-Token Implementation Reference

Read this reference only from the UI owner's design-token-system workflow when generating token values, creating or changing a canonical token format or export pipeline, or technically validating colour and build behaviour. Verify current syntax and support from the project's installed versions and official sources before relying on examples.

## Choose one source contract

Adopt the project's existing canonical format when it is coherent. With no established source:

- Plain CSS custom properties or a framework-native theme may be enough for one web consumer.
- Use a platform-neutral token format when several tools or platforms need the same decisions. The current Design Tokens Community Group format uses typed values, aliases, groups, and `$`-prefixed token properties; verify the latest published format before creating it.
- Inspect Style Dictionary's configured source and include paths, transforms, parsers, formats, and deep-merge behaviour. Use one input convention consistently; do not mix legacy `value` or `type` keys with DTCG `$value` or `$type` in one source merely because examples show both.
- In Tailwind, decide whether `@theme` is the canonical source or a generated or mapped consumer. Theme variables create utility or variant APIs, so use only supported namespaces and current syntax. When mapping external CSS variables, follow the installed version's documented indirection rules and avoid self-referential aliases.

Never maintain two hand-edited canonical sources. Generated outputs identify their source and are regenerated rather than manually repaired.

## Generate colour deliberately

- Map brand inputs to roles before deriving ramps. Keep action, semantic state, and categorical differentiation independent of the brand hue.
- Prefer a perceptual colour space such as OKLCH for generated ramps when the browser or build pipeline supports the required syntax. For unsupported targets, resolve values at build time or provide a verified fallback.
- Generate the smallest scale that serves actual semantic and component roles. Do not preserve an arbitrary number of steps merely because a template supplies them.
- Compute and test contrast from the final resolved colours in every supported theme. If no available on-colour meets the required target, adjust the background or introduce a dedicated text-bearing role; do not label the failing pair accessible.
- Treat automated contrast as one check, not complete accessibility evidence. Preserve non-colour cues, focus visibility, readable type, reduced-motion behaviour, and later human or assistive-technology testing where relevant.
- For dynamic themes, calculate dependent colours at build or runtime with a tested function or use a browser feature only after the project's support floor confirms it. Do not assume CSS can branch on contrast in every supported environment.

## Generate non-colour values deliberately

Adopt existing spacing, type, control, radius, elevation, breakpoint, and motion scales when they work. With no existing scale, derive a compact coherent set from the product's density, content, supported devices, and component needs. Check real screens and components before expanding it.

Breakpoints are part of the system even when a platform cannot interpolate them through ordinary variables. Typography includes family, size, line-height, weight, and measure responsibilities. Elevation includes visible focus treatment rather than shadows alone. Motion tokens exist only when the product uses motion beyond platform defaults.

## Validate aliases and outputs

Before publishing or accepting a migration:

- resolve aliases and reject cycles, missing targets, and collisions after merges;
- regenerate every required output from the canonical source;
- compare generated files with the checked-in or deployed result;
- inspect representative consumers in each platform or theme;
- search for new raw values and deprecated-token usage outside approved locations;
- run the project's build, type, lint, token, visual, and accessibility checks that can actually detect the changed contract; and
- state which remote enforcement, design-tool state, browser support, or rendered behaviour could not be verified locally.

## Current official source anchors

Use the latest applicable version, not a remembered example:

- [Design Tokens Community Group format](https://www.designtokens.org/TR/2025.10/format/)
- [Style Dictionary token model](https://styledictionary.com/info/tokens/)
- [Style Dictionary DTCG guidance](https://styledictionary.com/info/dtcg/)
- [Tailwind theme variables](https://tailwindcss.com/docs/theme)
- [MDN OKLCH reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
