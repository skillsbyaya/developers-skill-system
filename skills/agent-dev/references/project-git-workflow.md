# Project Git Workflow

Read this reference only when the user asks to set, change, explain, or audit a project's branching, review, and release convention.

## Determine the real stage and project shape

Inspect the project's explicit instructions and current branches before proposing a change. Establish whether real users or real data depend on the project, whether different modules or targets require different branches, and which target is live. Ask when stage or mapping is consequential and unclear. An explicit project requirement overrides the personal stage default.

Use this default only where the project has no stronger requirement:

| Stage | Branching and delivery convention |
| --- | --- |
| No real users or real data depend on the project | Work directly on `main`; no routine pull request, release tag, or changelog ceremony. Apply proportionate verification and the commit safety check. |
| Real users or real data depend on the project | Use a working `dev` or sandbox branch for changes and integrate to `main` only for a live release. Review the integrated change proportionately before release; tag the released `main` revision with the project's version convention. No changelog prose is required by default. |

Cross at the point real users or real data first depend on the project. Do not infer a single protected branch when repository policy maps different modules, environments, or change types to different branches.

## Set or change the workflow

Present the proposed branch and target mapping, live-release path, confirmation points, review expectation, and tag convention. Agree a tag convention when a live project has none rather than inventing one silently. Treat creation or renaming of branches, changing defaults or protections, and altering a live release path as consequential; obtain the user's decision when it was not already explicit.

When authorised, record the chosen workflow in the project's explicit instruction source. State concrete current behaviour: project stage, branch or content-to-branch mapping, which target is live, when confirmation is required, how changes reach live, and any review or tagging rule. Keep historical rationale elsewhere and do not create a second policy file or machine-readable schema merely for completeness.

Apply only the requested repository changes. Verify the written policy against actual branch and target configuration and name any host-side protection that cannot be checked.

## Audit only

Compare current project instructions, branches, targets, and release behaviour. Report matches, gaps, contradictions, and the smallest correction. Do not mutate instructions, branches, protections, or release configuration unless the user asks for the change. Missing or unclear policy is a failed audit result and a stop condition for later commit or push, not permission to infer a default.
