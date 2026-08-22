# Assurance Selection and Completion

Read this reference for a generic assurance request, a disputed completion condition, or a question about moving work from `review` to `done`. It selects a decision; it does not perform the selected method.

## Select from three inputs

1. **Consequence:** what happens if the work is wrong, how widely it can affect people or systems, and how reversible it is.
2. **Current evidence:** which scope-matched checks or reviews actually passed on the current revision, and what evidence is weak, stale, unavailable, or missing.
3. **Residual uncertainty:** the unanswered question that could still change acceptance.

Use the class as a floor, not as a workflow name:

| Class | Entry test | Minimum completion condition |
| --- | --- | --- |
| Routine | Bounded, readily reversible, isolated, no critical domain, reliable affected checks, and no material acceptance uncertainty | Current implementation evidence may suffice without independent review or ceremonial approval. |
| Material | Shared behaviour or contract, meaningful experience, moderate breadth or rollback cost, incomplete evidence, or another uncertainty that could change acceptance | Routine evidence plus one current human, focused independent, or other assurance result selected by the uncertainty. |
| Critical | Authentication or authorisation, tenant isolation, sensitive data or privacy, money, destructive behaviour, migration or data loss, concurrency or consistency, production rollout or rollback, consequential public contract, safety, legal or compliance exposure, or similar severe or irreversible impact | Fresh required specialist or independent evidence, current critical-path checks, explicit residual-risk decision, and fresh affected recheck after every fix. |

When classification is uncertain, use the higher class. Upgrade for wider impact, weak evidence or rollback, production or critical exposure, or a material unverified assumption.

## Choose the unanswered decision

| Residual question | Owner or `check-work` mode | Does not decide |
| --- | --- | --- |
| Can implementation responsibly start from the planning set? | implementation readiness | Story completion or shipping |
| Which differences in the live or dev experience still require human observation, and what exposure remains if those checks are skipped? | human preview, followed by explicit user result or acceptance where needed | Technical correctness or permission to ship |
| Does a bounded claim, plan, assumption, or specification survive hostile challenge? | adversarial review | Systematic path coverage or ongoing dialogue |
| Are reachable paths, states, transitions, or boundaries unhandled? | edge-case review | General quality or product desirability |
| Is a code change correct enough for its residual technical risk? | code review | Human experience, specialist compliance, or shipping |
| Is writing fit for its intended reader and purpose? | `agent-writer` editorial review | Technical correctness against repository evidence |
| Is test evidence adequate, or does the suite need work? | `agent-test-architect` consultation for unresolved strategy, or its test-system workflow for suite work | A ship verdict by itself |
| Does broad compliance or safety exposure apply, or is a SaaS programme ready for customer or external assurance? | `agent-compliance` consultation or SaaS assurance readiness | Generic acceptance, detailed legal advice, or control mutation |
| Does a named security, privacy, database, or legal exposure meet its specialist standard? | The relevant independent specialist | Generic acceptance |
| Can this bounded candidate ship now? | release readiness | Whether planning or implementation was well designed |

## `review` to `done`

`review` means implementation evidence exists but the selected completion condition is not yet satisfied. `done` means that condition is satisfied for the current revision. It does not mean deployed, released, or safe to ship.

| Selected condition | Evidence required before `done` |
| --- | --- |
| Routine implementation evidence | Acceptance conditions are supported; affected checks are current and green; the complete diff or finished artifact was inspected; no critical trigger, material unresolved decision or finding, or missing consequential evidence remains. |
| Human acceptance | The user performed the material checks or explicitly accepted the named exposure from skipped non-critical checks; requested changes are incorporated and affected checks rerun. |
| Focused independent assurance | The selected reviewer or method completed on the current revision; no required finding remains unresolved; fixes received a fresh affected recheck. |
| Critical assurance | Required specialist or independent evidence is current; critical-path evidence is present; no mandatory control or material finding remains unresolved; residual risks are explicitly accepted. |

Assessment does not change lifecycle state. The lifecycle owner may mark a strict routine case `done` directly and may reconcile other cases only from explicit current evidence.

Never infer `done` from a clean worktree, completed tasks, an old review, silence, or the absence of objections. A fix invalidates affected assurance. Implementation readiness never completes work; release readiness controls shipping, not whether work is done. For non-code work, use the artifact's acceptance evidence in place of code tests under the same consequence and uncertainty rules.
