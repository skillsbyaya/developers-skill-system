# Review

Review is report-only when requested alone. A combined review-and-fix request authorises bounded test rewrites within the requested scope. Test deletion or consolidation always requires explicit confirmation.

1. Establish a file, directory, changed-test set, risk-relevant slice, or whole-suite scope.
2. Inspect mechanically and semantically for hard waits, hidden conditional flow, weak or missing assertions, shared data, brittle selectors, order dependence, cleanup failures, unnecessary abstraction, slow setup, and focused-test violations.
3. Cross-reference intended behaviour and current source to classify obsolete or orphaned tests, redundant tests, real regressions, and mismatches that need a decision.
4. Grade findings:
   - **Critical:** can pass while important behaviour is broken, or is materially non-deterministic.
   - **High:** serious reliability or isolation failure, or dead tests that materially pollute the signal.
   - **Medium:** maintainability, brittleness, slowness, or redundant coverage.
   - **Low:** minor clarity or efficiency issue.
5. Return `PASS` with no Critical or High findings, `CONCERNS` with any High or a meaningful cluster of Medium findings, and `FAIL` with any Critical finding.

When a durable review is requested, already exists for the scope, or is needed for continuation, resolve the `test-review` row through [the convention-resolution rules](../../../organise-docs/references/convention-resolution.md) and create or update one current review. Include evidence-linked findings, concrete corrections, deletion or consolidation candidates, strengths worth preserving, and limitations.

When bounded fixes are already authorised, select the matching Initialize, Write or Update, Repair, or Improve operation and continue without waiting for separate acceptance of the findings. Then rerun the affected review and tests; do not update the verdict by assertion. Otherwise present the findings and stop.
