# Code-Area Reference

Create or refresh one concise reusable reference without turning the repository into an inventory.

1. Read `project-context.md` when present and relevant to the area's purpose or constraints.
2. Resolve the `codebase-reference` row through [the convention-resolution rules](../../organise-docs/references/convention-resolution.md).
3. Identify the target, intended reader, and decision or recurring work the reference must support. Check for an existing reference covering the same area and update it in place.
4. Read relevant source files and their direct configuration, tests, interfaces, and dependency boundaries. For a small target, inspect every source file. For a large target, inventory it first, state a coherent boundary, and ask before expanding materially.
5. Prefer the smallest map that lets a future reader change or assess the area safely. Avoid line-by-line inventories, full export lists, generated trees, and generic technology summaries unless the task requires one.

Use only decision-relevant sections:

```markdown
# {Area} codebase reference

## Purpose and boundary

## How it works

## Key paths and responsibilities

## Interfaces and data flow

## Constraints, risks, and change hazards

## Verification and relevant tests

## Related context
```

Link to canonical documents instead of copying them. Include paths, commands, interface shapes, and test names only when verified. Update an existing containing-folder index only when it already owns navigation; otherwise report the new path for a later approved documentation sweep.

Finish by confirming that the reference has no placeholders; paths and links resolve; and boundary, behaviour, risks, and verification are clear. Report the output path, material files inspected, uncertainties, and any follow-up requiring wider scope.
