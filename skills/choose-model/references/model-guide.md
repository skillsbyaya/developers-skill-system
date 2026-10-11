# Model Guide

Checked: 2026-10-11

## Paired recommendations

Choose by task, regardless of the tool hosting the conversation. These are practical alternatives, not benchmark equivalences or proof of account access.

| Task | Codex | Claude Code |
| --- | --- | --- |
| Consequential judgement, difficult diagnosis or architecture, adversarial review, sustained ambiguous work | Astra (`gpt-6-astra`) | Opus (`opus`) |
| Everyday implementation, writing, synthesis, and multi-step tool use | Sol (`gpt-6.1-sol`) | Sonnet (`sonnet`) |
| Narrow extraction, classification, formatting, and mechanical work with a clear check | Luna (`gpt-6-luna`) | Haiku (`haiku`) |

The recommendation set is limited to these families. Fable is excluded from recommendations and fallbacks by the user's budget constraint; preserve that exclusion during refreshes unless the user changes it. If an option is unavailable, choose a suitable accessible model within this set and state the trade-off.

## Effort and controls

Start from model-specific defaults, then increase for unresolved complexity or demanding verification. Similar effort names do not imply equal reasoning, cost, or quality across models. A weak brief needs clarification, not higher effort.

### Codex

Official guidance starts Astra at Light (`low`), Sol at the client's default, and Luna at High. Increase for harder planning or checking. Max spends more time on one task; Ultra uses parallel subagents and requires an appropriate task and permission to delegate.

The current desktop tool schema exposes Astra and Sol at `low`, `medium`, `high`, `xhigh`, `max`, and `ultra`; Luna stops at `max`. These controls are observed locally, not a guarantee for other accounts or workers. Older Sol and Terra entries may remain visible; prefer the current families above for new recommendations.

Local CLI: Codex 0.144.1 accepts `--model` and `-c` configuration overrides. For example: `codex --model gpt-6-astra -c 'model_reasoning_effort="low"'`. In the CLI, `/model` selects model and effort; in the desktop app, use its model/effort picker. Verify a worker's supported controls separately.

### Claude Code

Current documentation lists Opus 5.5, Sonnet 5.5, and Haiku 5.5 with `low`, `medium`, `high`, `xhigh`, and `max`, defaulting to `medium`. Use higher effort when the task needs deeper checking; reserve `max` for a demonstrated need. Aliases can resolve differently by account or configuration.

Local CLI: Claude Code 2.1.250 accepts `--model` and `--effort`. For example: `claude --model opus --effort medium`. Existing sessions expose `/model` and `/effort`. Help proves accepted syntax, not entitlement; confirm the resolved model and supported effort before applying a choice.

## Sources

All checked on the date above. The task pairings are this guide's judgement based on provider roles, not a provider claim of equivalence.

- Local Claude Code and Codex version/help output; current Codex desktop tool model/effort schema.
- [Codex models and effort](https://learn.chatgpt.com/docs/models).
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-basic).
- [Claude Code models and effort](https://code.claude.com/docs/en/model-config).
