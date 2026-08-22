# ATDD

Use this workflow to turn clear acceptance criteria for not-yet-implemented behaviour into CI-safe red-phase test scaffolds and one implementation checklist. Write tests and the checklist only; do not write production code or change delivery lifecycle.

## Establish the red-phase target

1. Resolve the feature or story scope, authoritative acceptance criteria, affected components and integrations, current implementation state, existing test framework, canonical command, test layout, fixtures, and conventions.
2. The criteria must state observable outcomes. Clarify test wording when the intended behaviour is already clear; if several product interpretations remain, stop for the user or product owner rather than turning a guess into executable specification.
3. A configured framework and discoverable test pattern must exist. If the required layer is absent, return the smallest prerequisite setup and select the test-system workflow's initialize operation only after the user authorises any dependency or configuration change. Resume ATDD after that setup is verified.
4. Separate missing behaviour from behaviour that already exists. Use ATDD only for the missing part; existing behaviour belongs to the test-system workflow's write-or-update operation. Do not claim a red phase for a test that already passes.
5. Reuse current scaffolds or a current ATDD checklist for the same scope rather than creating a parallel set.

## Map criteria to scenarios

- Create a happy-path scenario for each material criterion and add negative, boundary, permission, destructive, concurrency, or failure scenarios only where the risk earns them.
- Choose the lowest level that proves each scenario. Avoid duplicating one claim across unit, integration, API, and end-to-end levels.
- Assign P0-P3 priorities when ordering matters. Every critical-risk path identified under the owner's shared rules is P0.
- Show a compact scenario-to-level-to-priority-to-criterion map. Proceed without another confirmation when the criteria, framework, level, and files are already settled. Ask only when a consequential interpretation, level, scope, external dependency, or interface choice remains.

## Write CI-safe scaffolds

Follow the project's existing layout, syntax, fixtures, data factories, helpers, and naming.

- Emit every scaffold skipped with the framework's supported mechanism and a brief red-phase reason. The committed suite must remain green.
- Write real expected assertions from the acceptance criteria. Never use placeholder assertions or weaken the expectation to match current behaviour.
- Use deterministic unique data with explicit cleanup. Add only the factories and fixtures the scenarios need.
- Include the priority in each test name.
- For UI tests, prefer semantic locators. When a stable hook will be required, name the `data-testid` in the checklist as an implementation requirement rather than silently inventing unrelated markup.
- Do not call external services. Record required mocks, endpoints, and success or failure responses in the checklist.
- Keep tests syntactically valid and discoverable when production interfaces do not yet exist. Use a supported deferred import or setup pattern when possible. Otherwise record the unresolved interface and do not present collection or import failure as successful red evidence.

An activated scaffold must fail because expected behaviour is missing. It must not fail first because the test is malformed, cannot collect, lacks environment, or uses a broken fixture.

## Verify the red phase

1. Run the canonical relevant suite with all new scaffolds skipped. Confirm they register as skipped and that previously passing tests remain green.
2. Activate one P0 scaffold, or the highest-priority scaffold when no P0 exists.
3. Run the narrow test. Confirm that it reaches an assertion or observable behaviour boundary and fails for the expected missing implementation.
4. If it fails for syntax, collection, import, environment, or fixture reasons, fix the scaffold or record the unresolved prerequisite. Do not claim red verification.
5. Re-skip the scaffold, rerun the relevant command, and record the observed failure and final skipped state.

When no scenario can be activated responsibly because an interface or environment decision remains unresolved, keep the scaffolds CI-safe, mark red verification incomplete, and state the exact prerequisite.

## Write the implementation checklist

Resolve the `atdd-checklist` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md) for the current folder and naming pattern. Then read [the checklist template](../templates/atdd-checklist.md) and fill it from current evidence.

When the scope uses a durable story or requirement ID, preserve its canonical base and area suffix from the authoritative source. Resolve [the identifier convention](../../organise-docs/references/convention-resolution.md) only if the ID must be parsed, corrected, or used for area routing; this workflow does not allocate or re-key IDs.

The checklist must map every acceptance criterion to its scaffolds, list fixtures, mocks, and required hooks, and order implementation one test at a time: activate, confirm the expected red failure, implement the minimum production change, reach green, then continue. Do not instruct delivery to delete or weaken a scaffold merely to make it pass.

Do not edit a story or delivery-status record. If one owns the work, return its path with the checklist and scaffold paths so `agent-dev` can attach the handoff while preserving its state authority.

If ATDD reveals a material interface, dependency, acceptance interpretation, or implementation trade-off that the user had not already authorised, present it for confirmation before implementation begins. Otherwise carry the user's existing authority for the already-bounded implementation outcome in the handoff.

## Finish

Report the scoped criteria, scenario map, test and fixture files created or updated, checklist path, commands and results, the spot-activation failure observed, unresolved prerequisites or assumptions, and the handoff to `agent-dev` for implementation. After implementation, use the test-system workflow for coverage beyond the acceptance criteria and `check-work release-readiness` for a ship verdict when one is needed.
