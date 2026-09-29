# Git Close

Read this reference when a project is a Git repository and session-owned work must be preserved or landed. Enter at the step that matches the state: uncommitted, committed but unpushed, checkpointed remotely, or pushed and ready to land.

## Establish policy and intent

Read the project's declared Git workflow and current branch. Inspect status and the complete session-owned diff. Identify unrelated, generated, secret, environment, migration, or destructive files before staging.

Stop before mutation when:

- project Git policy or the expected branch is missing or unclear;
- the current branch conflicts with the task or project workflow;
- session-owned and unrelated changes cannot be separated safely;
- the proposed commit would include secrets, local environment files, or unintended generated output.

Do not infer that `main` is protected or that direct work on it is allowed.

## Commit

Every session has standing authority to commit its separable state to the declared non-live working branch so it can resume locally or in the cloud. This checkpoint authority does not extend to a live or protected branch, merge, release, deployment, destructive operation, unrelated work, or a target that project policy forbids.

1. Run the checks required for the unit's current boundary. For incomplete or failing work, record the exact result and use a clearly labelled checkpoint commit rather than presenting it as complete.
2. Re-read Git status and the intended diff.
3. Stage explicit paths only.
4. Immediately before committing, recheck the branch and every staged path against project policy and session intent.
5. Use a concise project-conforming message that describes the completed unit, or begins with `checkpoint:` when the unit is incomplete or required checks fail.

Never land or merge a checkpoint whose required evidence is failing. If a safe checkpoint cannot be made because ownership, branch policy, staged intent, secrets, or entanglement is unresolved, keep the work local and report that exact blocker.

## Push

Push every session checkpoint when the declared target is a non-live working branch and project policy permits it. Immediately before pushing, recheck branch, upstream, local commits, and project policy. Set the upstream for a new working branch when needed and permitted.

When the user's delivery instruction and declared project workflow authorise a completed unit to proceed beyond checkpointing through pull request, gates, and merge, carry out that sequence as one routine landing action. Do not ask separately at each step. This never extends authority to a live branch, live release, live deployment, or any state the workflow does not clearly authorise.

Never describe an unperformed commit or push as complete.

## Land

A pushed checkpoint is sufficient preservation for incomplete work but is not a landing. For a completed unit, follow the declared workflow to its stated end state — opening the pull request, waiting for the required gates, and merging in the style the project declares — rather than stopping at the last step this reference happens to name.

Merge authority follows the same rule as push: carry it out when the declared workflow permits it for this branch and state, including where the project has explicitly waived deployment approval. Stop and report instead when the workflow reserves the merge, real users or real data depend on the target, gates are failing or incomplete, or the change carries an unresolved decision.

A mergeable pull request left open is unfinished work, not a handoff. When something genuinely blocks it, name the blocker; do not reassign the merge to the user as a substitute for finishing it.
