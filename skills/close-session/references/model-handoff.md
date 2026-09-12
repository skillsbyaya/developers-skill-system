# Model recommendation in a handoff

Resolve the next action before choosing its model. Use the existing owner record and any project model-routing policy; do not inspect unrelated work or start a model audit during close. Capability class and reasoning effort are separate choices.

- Use the project's class vocabulary. Without one, use **High capability** for consequential or unresolved cross-system judgement and **Standard capability** for bounded work with settled contracts and strong verification.
- Name one model appropriate to the next session's actual surface, within the user's budget and availability constraints. Prefer an existing verified recommendation or current local model guidance when available. If the exact model is unverified, still state the capability class and mark the named choice conditional on availability; do not invent an identifier. Do not invoke a model-selection workflow during routine close, transfer aliases or effort scales between providers, infer account entitlement, change a session model, or silently downgrade a required High capability gate.
- For owner completion, use the recorded assurance need: running prescribed checks or settled Git actions may be mechanical, but coverage judgement, consequential review, and failure diagnosis are not.
- Choose effort independently, using only supported levels: normally medium for settled implementation and high for consequential implementation or independent review; low only for mechanical work with a clear oracle. Do not equate Standard capability with low effort. If availability or supported effort is unverified, label the recommendation conditional rather than claiming it is usable.
- The handoff names the next action only. A required review is its own session, not metadata on the session before it: while implementation is next, the review's model, scope and dependency boundary stay in the owning record, and the handoff carries no review-model line or second action; once implementation is ready for that review, the review becomes the next action and its model goes on the Model line. A story commit is not a prerequisite for review.

After the one pasteable handoff sentence, place **Model** and **Effort** on separate lines in the same handoff block. For example, where the project has verified these choices:

> **Model:** Standard capability — Sonnet.
>
> **Effort:** medium.

These are recommendations for the next action, not a report of the current session's model or effort. A human/external-only handoff uses `Model: not applicable — human/external action` and `Effort: not applicable`, each on its own line. Do not invent an AI continuation to handle a human decision.
