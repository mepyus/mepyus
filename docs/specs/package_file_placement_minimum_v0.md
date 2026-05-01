# Package File Placement Minimum v0

## Purpose

This spec defines the phase-1 file placement convention for package records.

It is a filesystem convention only.

## Directory Convention

One package kind maps to one package folder:

```text
space/packages/intake/
space/packages/digestion/
space/packages/review/
space/packages/memory/
```

Each phase-1 package record lives directly inside the folder matching its `package_kind`.

No nested package directories are part of phase 1.

## Filename Convention

Package record filenames should use:

```text
{package_id}.md
```

The filename stem should match the `package_id` in the package record.

Example:

```text
space/packages/intake/pkg_intake_001.md
```

## Initial File Format

Phase-1 package records use Markdown with minimal YAML front matter.

The front matter carries the locked minimum package record fields:

```markdown
---
package_id:
package_kind:
origin:
created_at:
updated_at:
source_bundle_ref:
bounded_content_pointer:
status:
short_summary:
next_action:
---

# Package Notes

Human-readable notes may go here.
```

The Markdown body is optional in phase 1.

If present, it is for human notes, clarifications, and bounded context. It is not a second schema.

## Example Paths

```text
space/packages/intake/pkg_intake_001.md
space/packages/digestion/pkg_digestion_001.md
space/packages/review/pkg_review_001.md
space/packages/memory/pkg_memory_001.md
```

## Why This Placement Fits Phase 1

The convention is flat, visible, and easy to inspect.

The folder name and `package_kind` reinforce each other without introducing routing, indexes, loaders, or storage design.

One file per package record keeps package identity simple and avoids premature bundling.

## Why Markdown With Front Matter

Markdown keeps the record human-readable first.

YAML front matter keeps the minimum record fields easy to scan and later export without making a machine format primary.

Plain Markdown alone would make the locked fields less consistent.

JSON would be more machine-oriented than phase 1 needs.

YAML alone would weaken human notes and reading context.

## Deferred Options

JSON, YAML-only records, generated indexes, database-backed storage, package directories, and machine exports are deferred.

They may be reconsidered after real package records show pressure that a flat Markdown convention cannot handle.

## Non-Goals

- No loader implementation.
- No schema validation.
- No indexing engine.
- No migration logic.
- No filesystem watcher.
- No package surfaces expansion.
- No code generation.

