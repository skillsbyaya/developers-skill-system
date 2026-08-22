# Index Documents

Create or refresh a useful `index.md` for a bounded folder without changing the documents it lists.

## Set the boundary

1. Resolve the target folder from the request or one obvious supplied path; ask one short question only when several plausible folders remain.
2. Resolve the `directory-index` row through [the convention-resolution rules](../references/convention-resolution.md). Place `index.md` inside the folder it describes.
3. Inspect immediate eligible files and subdirectories. Recurse only when requested or when a small nested documentation tree clearly benefits from one index; state the boundary before traversing a large tree.
4. Exclude the index itself, hidden files, build or generated outputs, archives, and non-document assets unless requested. Do not follow a symlink outside the target boundary.

If no eligible documents remain, do not create an empty index; report the boundary and stop.

## Preserve curated information

When `index.md` already exists, identify its curated introduction, usage notes, section order or grouping, per-entry annotations, and any generated listing. Match existing entries by resolved relative path rather than display title.

- Preserve curated prose and grouping unless the user asks to change it.
- Carry a useful existing entry annotation forward when its target still exists and the annotation remains true. Generate or refresh only missing, generic, or demonstrably stale descriptions.
- Remove an entry only when its target is outside the stated boundary or no longer exists; do not treat omission from a fresh scan as permission to discard unmatched curated content until its path is resolved.
- If generated and curated regions cannot be distinguished confidently, show the proposed replacement and preservation mapping before writing.

For a new index, or an existing index with a clearly separable generated listing, wrap only the replaceable listing in:

```markdown
<!-- organise-docs:index:start -->
...generated entries...
<!-- organise-docs:index:end -->
```

Keep curated introductions and usage notes outside that region. Existing curated grouping or annotations may remain inside when preserving them is clearer; the markers never imply permission to overwrite content whose ownership is uncertain.

## Build the listing

- Read enough of each eligible document to identify its purpose and distinguish it from similarly named documents. Do not eagerly read every large file in full.
- For unsupported, binary, encrypted, or inaccessible items, use verifiable metadata and label the limitation instead of guessing.
- Use concise descriptions grounded in the source. Prefer the document's real title; otherwise derive a readable label from its filename.
- Group by an existing curated scheme when sound, otherwise by purpose when that improves choice, then by immediate subdirectory. Sort entries alphabetically within each group unless a curated or source-defined order is meaningful.
- Use correctly encoded links relative to the index location. Avoid decorative metadata that does not help a reader choose a document.

A simple listing entry is:

```markdown
- [Document title](relative/path.md) — Concise, source-grounded purpose.
```

## Verify and finish

Check that every listed path resolves, every eligible document within the stated boundary is represented or deliberately skipped, the index does not list itself, descriptions match their sources, and all preserved introductions, grouping, usage notes, and per-entry annotations remain intact.

If the current index already passes those checks, leave it unchanged and report a no-op.

Return the index path, traversal boundary, additions, refreshed or removed entries, preserved curated material, and skipped or unreadable items.
