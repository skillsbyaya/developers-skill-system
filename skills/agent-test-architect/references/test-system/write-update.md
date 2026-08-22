# Write or Update

Use this operation only for implemented behaviour. Not-yet-implemented acceptance criteria belong to ATDD.

1. Resolve scope from the request, changed code, story or specification, named feature, or existing gap.
2. Map important behaviours and realistic failure modes. Prioritise by risk and choose the lowest level that proves each claim.
3. Search existing tests so the change extends or corrects coverage rather than duplicating it.
4. Follow current fixtures, factories, naming, selectors, assertions, and cleanup. Cover happy, error, boundary, permission, and destructive paths in proportion to risk.
5. When source and test disagree, use authoritative intent when clear. Otherwise expose the mismatch instead of choosing the current code or test by convenience.
6. Run the narrow changed tests first, then the relevant broader suite when shared contracts or risk justify it.

If a current test summary exists and the work changes durable coverage knowledge worth preserving, resolve the `test-summary` row through [the convention-resolution rules](../../../organise-docs/references/convention-resolution.md) and update that summary with the behaviour covered, commands and results, and remaining gaps. Do not create or churn a standing summary for routine edits.
