# Edit a Skill

Use this route when the requested change and its intended effect are already known and bounded.

## Preserve the boundary

Keep the skill's existing job, owner, and neighbours unless the requested change necessarily alters them. Inspect only the affected instruction, metadata, route, resource, helper, consumer, or registration plus enough surrounding context to edit it safely.

Apply the smallest complete change. Update dependent wording, links, generated declarations, or consumers only where the bounded change makes them stale. Preserve fixed user preferences and unrelated content; do not attach opportunistic cleanup, mechanism review, or architecture redesign.

Read [platform compatibility](platform-compatibility.md) when metadata, invocation, execution context, or supported structure changes. Read [registration and consumers](registration-and-consumers.md) when the description, name, modes, location, documents, routes, or consumers change. Read [worker use](worker-use.md) only when worker behaviour changes.

## Verify and stop

Validate the changed behavior with the smallest realistic case set that can expose regression. Parse affected metadata, resolve changed paths, and test changed deterministic helpers. Check adjacent triggers when trigger text changed and direct use when workflow instructions changed.

Stop when the requested effect and affected consumers are coherent. If evidence shows the owner or purpose itself is wrong, do not silently broaden the edit; state the conflict and move to restructure only when that broader outcome is authorised.
