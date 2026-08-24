# CI Quality Pipeline

Use this workflow to design, create, repair, or validate repository CI quality gates. Turn the project's real risk-relevant local checks into maintainable hosted signals; do not substitute a generic job list for repository evidence.

This workflow owns quality-pipeline configuration, including triggers, job topology, permissions, reproducible setup, isolated services, caches, timeouts, failure artifacts, cleanup, and local configuration validation. It does not create missing test frameworks or tests, change production behaviour, configure deployment, administer repository rules or secrets, or decide release readiness.

## Establish the pipeline contract

Inspect only the evidence needed to establish:

- the CI platform and current configuration, including reusable workflows, composite actions, or shared includes;
- package managers, lockfiles, runtime files, workspaces, and working directories;
- existing build, format or lint, type-check, test, schema or migration, contract, security, accessibility, and other verification commands;
- the service, environment, secret, artifact, cleanup, and external-state requirements of each command;
- target events and branches, any merge queue, and documented required-check names; and
- current hosted failures or enforcement settings when remote access is already available and the user has authorised inspection.

Run candidate commands locally when safe and proportionate. Record pre-existing failures instead of assuming the pipeline change caused them. A failing test or build baseline may require the separately selected test-system repair workflow or `agent-dev`; do not hide it by weakening or bypassing the gate. If a proposed gate has no working project command or required framework, stop that gate and name the missing prerequisite; do not fabricate a command, placeholder test, or competing framework.

Before editing, make a compact gate map:

| Gate | Exact local command | Risk it blocks | Dependencies | Independent? | Intended signal |
| --- | --- | --- | --- | --- | --- |

Every gate needs repository evidence or an explicit user requirement. Coverage thresholds, sharding, burn-in loops, browser installation, and runtime matrices are choices to justify, not defaults.

Validation or assessment alone is report-only. A combined “review and fix,” “design and implement,” or similar request authorises discovery followed by in-scope quality-pipeline edits; do not pause after the gate map merely because discovery determined the exact configuration. Ask again only when discovery exposes materially different work, deletion, a production or deployment change, or a consequential trigger, topology, dependency, permission, status-name, or external-state trade-off that the user has not already authorised.

## Choose the smallest reliable topology

- Give materially different failure domains separate jobs when distinct diagnosis, permissions, services, runtimes, or hosted status matter. Keep tightly coupled commands together when splitting would only repeat setup.
- Run independent gates in parallel. Add dependencies only for real data, setup, or ordering requirements.
- Preserve stable required-check names unless a rename and its hosted-enforcement consequence are explicitly coordinated.
- Use checked-in project commands, pinned runtimes, the repository's package manager, and reproducible lockfile installation. Do not install an unrelated latest tool when the project already owns the command.
- Shard only when the runner supports it and measured runtime justifies the operational cost. Choose fail-fast behaviour deliberately.
- Add repeated flaky-test execution only where it answers a real reliability risk, normally as a scheduled or targeted job rather than multiplying every pull-request run.
- Upload only bounded failure evidence that materially shortens diagnosis, such as test reports, traces, logs, or screenshots, with bounded retention. Never upload secrets, environment dumps, databases, or broad workspace output.
- Ensure an intended required signal reports for every protected event and path. Path filters, skipped dependencies, or missing merge-queue triggers must not leave a required check permanently waiting.
- Add concurrency cancellation only when a superseded run is safe to cancel. Set timeouts for work that can hang.
- Cache dependency downloads or tool assets, not mutable workspace state. Include the relevant lockfile and tool version in the key, and keep correctness independent of a cache hit.

For an existing pipeline, preserve working triggers, permissions, gates, deployment boundaries, and meaningful comments unless the requested outcome requires a change. Explain any trigger, status-name, permission, or enforcement-impacting change before applying it.

## Keep execution safe

- Grant the minimum job and token permissions needed. Prefer read-only repository access for ordinary quality gates where the platform supports it.
- Never run checks against production services or customer data. Use isolated services, containers, emulators, or disposable databases, with cleanup that still runs after failure.
- Keep untrusted pull-request or fork code away from privileged secrets and write tokens. Do not use a privileged event or trusted follow-up workflow to execute untrusted code merely to make secrets available.
- Treat persistent or self-hosted runners as a trust boundary. Do not run untrusted fork code on them unless isolation from internal resources and reliable reset between runs are established.
- Treat event data, branch names, titles, bodies, labels, inputs, downloaded artifacts, and similar external values as untrusted. Do not interpolate them directly into executable shell or evaluate a command supplied through an input. Use the platform's safe data-passing mechanism and quote values as data.
- Follow the repository's dependency-pinning policy. Where the platform supports immutable third-party action or plugin references, treat pinning and update automation as an explicit supply-chain choice. On GitHub Actions, a full-length commit SHA is the immutable reference form; surface tag-only third-party actions as a deliberate risk rather than silently normalising them.
- Write safe references for required secrets or variables, but do not create, request, echo, infer, or persist secret values.
- Validate schemas and migrations without changing state by default. Apply a migration or another state-changing check without separate confirmation only when the target is isolated and disposable, no real, shared, or production users or data depend on it, the command cannot remove, rewrite, expose, or corrupt existing data or cause external side effects, and cleanup still runs after failure. Otherwise obtain explicit confirmation.

When volatile platform behaviour affects triggers, permissions, expression handling, fork safety, action pinning, merge queues, or required checks, verify it against current official documentation before relying on it. If that evidence is unavailable and the uncertainty affects safety or correctness, preserve the current behaviour or stop with the limitation instead of guessing.

## Implement and validate

Edit the platform-native configuration at the repository's established path. Keep each job readable enough that a hosted failure maps to an exact local command.

If the current configuration already satisfies the requested outcome, make no change and report the evidence.

For each applicable job:

1. check out the intended revision safely;
2. set up the project-pinned runtime and dependency cache;
3. install reproducibly from the lockfile;
4. start only the isolated services that gate needs;
5. run fixed project commands;
6. collect bounded diagnostic artifacts on failure; and
7. clean up stateful services even when an earlier step fails.

Avoid command-shaped workflow inputs, optional critical gates, blanket retries, duplicated setup with drifting versions, or comments that claim hosted enforcement the configuration cannot provide.

Validate with the strongest evidence available:

- parse or lint the platform configuration with a platform-aware validator when available, otherwise use a safe structural parser and state the limitation;
- inspect triggers, permissions, dependencies, conditions, matrices, timeouts, environment wiring, cache keys, artifact paths, and cleanup conditions;
- search executable blocks for untrusted expression interpolation and command-shaped inputs;
- confirm every gate maps to an existing command and every runtime or tool version comes from project evidence;
- run changed or representative local commands when proportionate, separating pre-existing failures from introduced failures; and
- compare final job names and event coverage with documented hosted requirements, including merge-queue events when applicable.

A valid local configuration is not proof that a hosted run passed or that the signal blocks merging. If remote access and authority are already available, inspect or trigger the smallest safe hosted verification. Otherwise return the exact follow-ups: secrets or variables to configure, first-run observation, required-check or ruleset administration, and any deliberate-failure test.

## Finish

Report:

- configuration files changed and triggers covered;
- each gate, its exact project command, and the risk it signals;
- local commands and configuration checks run, with results;
- pre-existing failures, skipped gates, assumptions, and unavailable evidence;
- secrets, variables, hosted runs, required checks, rulesets, or merge-queue settings still requiring external action; and
- whether hosted execution and merge enforcement were actually verified.

Do not create a recurring pipeline report. If the work establishes a durable, almost-always-needed project fact such as the CI platform or canonical verification command, make only that bounded update to the existing project context; do not duplicate details already authoritative in manifests or pipeline configuration. This workflow does not commit or push repository changes.
