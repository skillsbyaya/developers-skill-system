---
name: choose-model
description: "Selects a model and reasoning-effort level for Claude Code, Codex, or a worker. Use when the user asks which model or effort to use, wants to avoid an unsuitable model, asks to refresh current guidance, or before work starts when a verified actionable switch would materially affect quality or cost."
---

# Choose Model

Choose the lightest available model and effort that preserves the task's required result. A model choice is useful only when the selected surface exposes a real control and changing it would materially improve quality, speed, context handling, or cost.

## Select the operation

- **Recommend:** choose a model and effort for a named task, session, or worker.
- **Configure:** explain or, when requested and supported, apply the choice to a new session or bounded worker.
- **Refresh:** update [the model guide](references/model-guide.md) from current local and official evidence.

An explicit request may happen at any time. Propose a choice without being asked only before substantive work begins, when the switch is actionable on the chosen surface and no other unsolicited setup proposal has already consumed the task's setup interruption. Never interrupt active work to suggest a parent-session change that cannot be applied.

A recommendation is advisory. Apply it in the same run only when the exact target is already specified or the user explicitly authorised the selected choice within stated quality, cost, and availability bounds. Otherwise return the choice and trade-off before configuration.

## Make the choice

1. Identify the exact surface: the active or a new Claude Code session, a Claude worker, Codex, or another named environment. Do not transfer model names, effort labels, availability, or controls between surfaces without verification.
2. Establish the hardest material requirement: difficult judgement, broad or noisy context, implementation and tool use, multimodal work, adversarial checking, or routine bounded transformation. Include stakes, reversibility, latency, and cost.
3. Read [the model guide](references/model-guide.md). Inspect local help, a visible picker, configuration, or a successful low-risk invocation only when it can change the answer. Help output proves accepted syntax, not account entitlement; state what is documented, locally observed, or inferred.
4. Keep the current setup when a switch has no supported material benefit. Otherwise give one choice and one fallback with the task-specific trade-off.
5. Use the surface's own effort scale and the lowest level that preserves the result. Do not compensate for a weak brief by raising effort; clarify the outcome or packet first.

Prefer a moving alias or recommended default when the user wants sensible upgrades over time. Use a fixed identifier only when reproducibility, evaluation, or compatibility requires it.

## Apply only verified controls

Do not claim to switch the active parent conversation without an observable supported control. For a new session or worker, construct only controls shown by the installed surface or current official documentation. Confirm success from the resulting session, picker, configuration, or invocation rather than from the command shape alone.

Delegation policy remains with the workflow choosing whether and how to delegate. This skill selects only the model and effort after a real execution surface and capability need exist.

## Refresh current guidance

Refresh when the user asks for current advice, reports staleness, the requested option is absent, or local controls conflict with the guide.

Check:

1. installed help, configuration, and visible availability for the target surface;
2. current official documentation for that provider and surface; and
3. a low-risk availability check only when still needed and authorised.

Update the checked date, observed versions, supported controls, current model roles, availability caveats, and source links. Keep volatile names and product facts in the guide, not this core.

## Finish

Return:

- **Choice:** model or alias and effort;
- **Why:** the hardest requirement and expected benefit;
- **Apply:** the verified switch or configuration path, or recommendation-only boundary;
- **Fallback:** one alternative and its trade-off; and
- **Evidence:** what was locally observed, documented, or left uncertain.
