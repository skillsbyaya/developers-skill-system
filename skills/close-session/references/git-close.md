# Git Close

Read this reference only when the project is a Git repository and session-owned changes may be committed or pushed.

## Establish policy and intent

Read the project's declared Git workflow and current branch. Inspect status and the complete session-owned diff. Identify unrelated, generated, secret, environment, migration, or destructive files before staging.

Stop before mutation when:

- project Git policy or the expected branch is missing or unclear;
- the current branch conflicts with the task or project workflow;
- session-owned and unrelated changes cannot be separated safely;
- required checks or user decisions are still outstanding; or
- the proposed commit would include secrets, local environment files, or unintended generated output.

Do not infer that `main` is protected or that direct work on it is allowed.

## Commit

Commit only when the user's close request and project workflow make a commit appropriate for the completed session-owned unit.

1. Run the checks required by the project and the changed surface.
2. Re-read Git status and the intended diff.
3. Stage explicit paths only.
4. Immediately before committing, recheck the branch and every staged path against project policy and session intent.
5. Use a concise project-conforming message that describes the completed unit.

If checks fail or the unit is incomplete, keep the work uncommitted and report the exact continuation boundary.

## Push

Push only when the user requested it or the declared project workflow explicitly permits unattended push for this branch and state. Immediately before pushing, recheck branch, upstream, local commits, and project policy.

When a natural close request and the declared project workflow already authorise a completed session-owned unit to proceed through checks, commit, and push to a non-live branch, carry out that sequence as one routine landing action. Do not ask separately at each step or treat the absence of separate `commit` and `push` requests as a reason to stop. This never extends authority to a live branch, live release, live deployment, or any state the workflow does not clearly authorise.

Ask before any push that is not clearly authorised. Never describe an unperformed commit or push as complete.

## Land

A push is not a landing when the declared workflow ends somewhere further on. Follow that workflow to its stated end state — opening the pull request, waiting for the required gates, and merging in the style the project declares — rather than stopping at the last step this reference happens to name.

Merge authority follows the same rule as push: carry it out when the declared workflow permits it for this branch and state, including where the project has explicitly waived deployment approval. Stop and report instead when the workflow reserves the merge, real users or real data depend on the target, gates are failing or incomplete, or the change carries an unresolved decision.

A mergeable pull request left open is unfinished work, not a handoff. When something genuinely blocks it, name the blocker; do not reassign the merge to the user as a substitute for finishing it.
