# Test System and Suite

Use this workflow for hands-on project testing and for read-only assessment or teaching. Infer one operation and read only its reference.

| Operation | Read |
| --- | --- |
| Understand the setup, gaps, coverage shape, or overall health | [Assess](../references/test-system/assess.md) |
| Establish a missing test layer or complete partial framework scaffolding | [Initialize](../references/test-system/initialize.md) |
| Add or adapt tests for behaviour that already exists | [Write or update](../references/test-system/write-update.md) |
| Audit whether tests are trustworthy, relevant, and maintainable | [Review](../references/test-system/review.md) |
| Diagnose and fix failing, flaky, slow, or misconfigured tests | [Repair](../references/test-system/repair.md) |
| Strengthen a suite with several interacting weaknesses | [Improve](../references/test-system/improve.md) |
| Learn testing concepts or practices through a real or supplied example | [Teach](../references/test-system/teach.md) |

An explicit operation selects it immediately. For a vague “sort out the tests” request, select Assess and use its light route. If the request spans several operations, state the smallest useful sequence and load them one at a time. Do not read sibling operations or switch to consultation merely because the work requires testing judgement.

## Establish the current testing state

Inspect evidence in proportion to the selected operation:

- stack, package manager, runtime and workspace boundaries;
- installed frameworks, configuration, scripts, and test locations;
- representative tests, fixtures, helpers, data factories, and conventions;
- canonical commands and current outcomes;
- relevant implementation, requirements, recent changes, CI references, reviews, or summaries; and
- whether the setup is absent, partial, coherent, inconsistent, failing, flaky, slow, stale, or thin against risk.

A local repair or lesson may need one command and a few files. Framework setup, a whole-suite review, or a broad improvement programme may require wider manifests, lockfiles, test directories, and current project sources. Do not claim whole-suite coverage from file counts or a partial scan.

Resolve only the strategy needed for the operation. A combined assessment-and-fix request carries through ordinary in-scope testing decisions without an interim stop. Before dependent mutation, ask again only when evidence exposes materially different work, deletion, a production behaviour change, or a consequential level, scope, dependency, acceptable omission, or “how much is enough” trade-off that the user has not already authorised. Reuse a current strategy or coverage map when it answers the question. If new evidence contradicts it, name the conflict instead of silently following either source.

## Finish

If the current state already satisfies the requested outcome, make no change and report the evidence. Otherwise report the operation, state found, files changed if any, commands and results, repeated-run evidence where relevant, remaining failures or limitations, durable artifact updated if any, and the next highest-value testing action. Do not claim an unrun check passed, infer release permission, mutate delivery lifecycle, or commit or push.
