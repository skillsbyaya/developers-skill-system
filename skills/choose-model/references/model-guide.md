# Model Guide

Checked: 2026-07-16

This is a refreshable decision aid, not proof of account entitlement. Verify the target surface before applying a choice.

## Claude Code

Local evidence: Claude Code 2.1.170 accepts `--model <model>` and `--effort <low|medium|high|xhigh|max>` when starting a session. Its help lists moving aliases including `fable`, `opus`, and `sonnet`, plus full model identifiers. The current official CLI reference also documents aliases and notes that available effort levels depend on the model. Local help proves accepted controls, not which models the current account can use.

| Role | Best fit | Avoid when |
| --- | --- | --- |
| Strongest available reasoning model, commonly reached through the current `opus` alias | Consequential judgement, difficult architecture or diagnosis, adversarial review, and synthesis where subtle errors are expensive | Routine bounded transformations with strong verification |
| Balanced capable model, commonly reached through the current `sonnet` alias | Normal coding, drafting, research synthesis, and multi-step tool use | The task demonstrably needs the strongest reasoning available or a lighter option is clearly sufficient |
| Fast or light model exposed by the current surface | Narrow extraction, classification, formatting, and mechanical checks with a clear oracle | Ambiguous decisions, cross-system reasoning, or omission-sensitive work |

Use low effort for narrow mechanical work, medium for ordinary bounded work, and high for difficult or consequential reasoning. Use `xhigh` or `max` only when the installed model supports it and the expected gain justifies the extra time and tokens.

## Codex

Local evidence: Codex CLI 0.144.1 accepts `--model` for interactive and non-interactive runs. Reasoning effort can be supplied through current configuration when supported; inspect the effective configuration or current docs rather than inventing a dedicated flag.

Current official guidance starts with the recommended default or Power setting, then moves toward a faster option for clear repeatable work or a deeper option for complex open-ended work. As of this check, the documented GPT-5.6 family uses:

| Role | Current documented fit |
| --- | --- |
| Sol / recommended Power default | Complex, open-ended, high-value work needing judgement and polish |
| Terra | Everyday coding, tool use, exploration, and pragmatic multi-step work |
| Luna | Clear, repeatable, high-volume extraction, classification, transformation, and structured summaries |

Use the lowest reasoning effort that produces the required result. Low suits well-scoped work, medium balances speed and depth, and high or extra high suits difficult multi-step work. Max is for unusually hard single-agent reasoning; Ultra changes the execution shape by using subagents and should be selected only when meaningful parallel decomposition is justified.

Prefer the configured default when no material model choice exists. Verify current availability in the picker, `/model`, installed help, or a successful invocation before naming a model as usable.

## Other surfaces

Inspect that surface's own current controls and documentation. Do not reuse Claude or Codex model names, roles, or effort labels by analogy.

## Sources

- Local `claude --version` and `claude --help`, checked 2026-07-16.
- [Claude Code CLI reference](https://code.claude.com/docs/en/cli-usage), checked 2026-07-16.
- Local `codex --version`, `codex --help`, and `codex exec --help`, checked 2026-07-16.
- [Codex model selection](https://developers.openai.com/codex/models), checked 2026-07-16.
- [Codex configuration](https://developers.openai.com/codex/config-basic), checked 2026-07-16.

