---
name: choose-model
description: "Recommends paired Claude and Codex models and their reasoning effort for a task, session, or worker. Use when the user asks which model or effort to use or before work starts when a verified actionable switch would materially affect quality or cost."
---

# Choose Model

Choose the lightest available model and effort that preserves the task's required result. Recommend for the task regardless of which tool hosts this conversation. Delegation policy remains with the workflow choosing whether and how to delegate.

## Select the operation

- **Recommend:** choose a model and effort for a named task, session, or worker.
- **Configure:** explain or, when requested and supported, apply the choice to a new session or bounded worker.
- **Refresh:** update [the model guide](references/model-guide.md) from current local and official evidence.

An explicit request may happen at any time. Propose a choice without being asked only before substantive work begins, when the switch is actionable on the chosen surface and no other unsolicited setup proposal has already consumed the task's setup interruption. Never interrupt active work to suggest a parent-session change that cannot be applied.

A recommendation is advisory. Apply it in the same run only when the exact target is already specified or the user explicitly authorised the selected choice within stated quality, cost, and availability bounds. Otherwise return the choice and trade-off before configuration.

## Make the choice

1. Establish the hardest material requirement: difficult judgement, broad or noisy context, implementation and tool use, multimodal work, adversarial checking, or routine bounded transformation. Include stakes, reversibility, latency, and cost.
2. Read [the model guide](references/model-guide.md). Inspect local help, a visible picker, configuration, or a successful low-risk invocation only when it can change the answer.
3. Give both a Codex option and a Claude option unless the user explicitly limits the answer to one provider. The current host is not that limit. Match task suitability, not supposed model equivalence; label unverified availability without withholding the other option.
4. Use each model's own effort scale and the lowest level that preserves the result. Do not compensate for a weak brief by raising effort; clarify the outcome or packet first.

## Refresh current guidance

Refresh when the user asks for current advice, reports staleness, the requested option is absent, or local controls conflict with the guide.

Check:

1. installed help, configuration, and visible availability for the relevant surfaces;
2. current official documentation for both providers during a full refresh; and
3. a low-risk availability check only when still needed and authorised.

Update the checked date, observed versions, supported controls, current model roles, availability caveats, and source links. Keep volatile names and product facts in the guide, not this core.

## Finish

Return:

- **Choice:** `Codex: <model>, <effort> / Claude: <model>, <effort>` and one short task-specific reason.
- **Apply:** only when requested, give or use the verified control for the named target. Report a switch only after observing success.
