---
name: optimise-tokens
description: "Diagnoses recurring Claude Code context and token cost across sessions, skills, or documents. Use for token audits, unexpectedly large context, expensive sessions, repeated context growth, or evidence-backed reduction of eager loading, duplication, stale content, and uneconomic delegation."
---

# Optimise Tokens

Find the mechanisms creating avoidable context or token cost, then propose the smallest changes that improve the whole task. Preserve the required outcome, accuracy, coverage, risk controls, user preferences, and finished-result evidence; existing ceremony has no protection when it adds no material value.

## Select the scope

| Request | Inspect |
| --- | --- |
| System-wide usage, recent expensive sessions, or unexplained context growth | Read [Session data](reference/session-data.md), then analyse a bounded recent window. |
| One named skill | Read its core and only the resources needed to explain loading and behaviour. |
| One named document or context source | Read that file and the consumers that determine whether its size is avoidable. |

Do not read session transcripts for a named-file audit. Do not turn a request to shorten writing for a reader into a token-system audit; that belongs to `agent-writer` distillation or revision.

## Establish the baseline

Record the evidence available for the chosen scope: file size, selected-resource size, session peaks, cache behaviour, turn count, duration, worker timing, repeated reads, or loaded metadata. Treat token and monetary savings as estimates unless the platform supplies exact costs.

A high number is an effect, not a cause. Trace the growth path before proposing a fix. A skill appearing in an expensive session, a worker appearing near a context peak, or a large file existing on disk does not prove causation.

## Diagnose the mechanism

Check only mechanisms supported by the evidence:

- always-loaded instructions or metadata that rarely affect a decision;
- eager loading of conditional references, templates, examples, or broad file sets;
- duplicated facts or rules across owners and consumers;
- repeated broad reads or searches whose useful return is small;
- long-lived sessions that mix unrelated tasks or retain obsolete context;
- dynamic content placed where it repeatedly invalidates useful caching;
- growing living documents that preserve journal history or stale sections;
- worker cold starts, duplicated reads, integration, or correction cycles that cost more than inline work; and
- a genuinely separable noisy phase whose compact return can protect the main context.

For worker or subagent changes, read `~/.claude/skills/upskill/references/worker-use.md`. Require a supported whole-task benefit after briefing, cold start, returned output, integration, duplicated work, and likely corrections. Parallelism and a smaller parent transcript do not by themselves prove a saving.

Classify the cause as:

- **local:** one file, route, or loading decision;
- **owner-wide:** a repeated pattern in one skill or document owner; or
- **systemic:** a demonstrated class that affects several owners.

## Propose before mutation

Rank findings by supported whole-task impact. For each finding report:

```text
FINDING:      what is costly and where
EVIDENCE:     measurement or observed loading path
ROOT CAUSE:   local, owner-wide, or systemic mechanism
FIX NOW:      smallest change to remove current waste
PREVENTION:   owner change that stops recurrence, or "one-off"
SAVING:       bounded estimate and assumptions
UTILITY RISK: none, low, medium, or high — what could be lost
```

If evidence is insufficient, recommend a bounded measurement instead of a fix. If a proposed reduction could weaken quality, safety, coverage, a fixed preference, or verification, present it as a trade-off requiring approval rather than pure optimisation.

Route durable changes to their owner:

- skill structure, triggers, or loading → `upskill`;
- a particular oversized source needing compact downstream context → `agent-writer` distillation;
- living document structure or recurring stale content → `organise-docs`;
- end-of-session context handling → `close-session`;
- a material model or effort choice → `choose-model`; and
- ordinary implementation → the relevant delivery owner.

Do not create a second token-policy store or copy the same prevention rule into every consumer.

## Apply approved changes

Assessment is report-only unless the user also approves exact fixes. Apply only the accepted scope through the owning skill. A broad “audit and optimise” request does not authorise a consequential change whose target, mechanism, quality trade-off, or blast radius became clear only during diagnosis.

After mutation, remeasure the touched path, verify that the original outcome and assurance still hold, and report no-op findings honestly. If implementation reveals a different cause, stop and return it as a new finding rather than expanding the approved change silently.
