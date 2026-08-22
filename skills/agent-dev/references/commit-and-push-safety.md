# Commit and Push Safety

Read this reference immediately before any commit or push performed through Agent Dev. It does not apply to read-only version-control inspection.

1. Read the project's declared Git workflow and identify the expected branch or content-to-branch mapping for this change. Do not infer that `main` is protected or that direct-to-`main` work is allowed. If policy or expected intent is missing or unclear, stop before mutation and explain what must be decided.
2. Recheck the current branch against the expected branch. Inspect recent reflog entries when the working directory may be shared or the checkout could have changed unexpectedly.
3. Inspect every staged file and the complete staged diff, including content staged before this turn. Confirm that all staged content is change-owned and belongs on the expected branch and in this commit.
4. If branch, policy, reflog, target, or staged intent is unexpected, mismatched, or entangled, do not commit or push. Report expected versus actual state and wait for direction.
5. Commit only the intended change-owned files. Never force-push, bypass checks, or push to production or an unknown target. Obtain the required confirmation before any push or deployment to a live target used by real users or real data.

After any fix or restaging, repeat the affected checks above; an earlier safe result is stale.
