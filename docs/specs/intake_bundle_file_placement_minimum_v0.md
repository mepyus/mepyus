# Intake Bundle File Placement Minimum v0

## Purpose

This spec defines the minimum placement convention for preserved manual intake bundles in phase 1.

It is a file placement convention only.

## Placement

Preserved manual intake bundles should live under:

```text
space/intake_bundles/
```

This folder is part of the space layer, but it is not package storage.

Do not place manual intake bundles under `space/packages/`.

## Why Not `space/packages/`

`space/packages/` is reserved for package records that already use the locked package record, package vocabulary, package authoring rules, and package file placement.

An intake bundle is earlier than that.

It captures an external result before a human decides whether it should become an `intake` package.

Keeping bundles outside `space/packages/` prevents provisional source-facing notes from being mistaken for package records.

## Filename Convention

Use one file per preserved bundle.

Filename pattern:

```text
bundle_{YYYYMMDDTHHMMSSZ}_{short_slug}.md
```

Use UTC time in the filename.

Use lowercase ASCII letters, numbers, and underscores in `short_slug`.

The slug should describe the captured result, not the future package.

## Initial File Format

Use plain Markdown with named sections.

Do not use YAML front matter for phase-1 intake bundles.

Recommended section shape:

```markdown
# Intake Bundle

source_tool:
task_intent:
source_refs:
outputs_artifacts:
short_tool_summary:
known_risks_or_blockers:
suggested_next_move:
language_bridge_notes:
```

Plain Markdown is enough because the bundle is a human capture note, not a package record.

If a value is unknown, write `null`.

## Difference From Package Placement

Package records live under:

```text
space/packages/{package_kind}/{package_id}.md
```

Manual intake bundles live under:

```text
space/intake_bundles/{bundle_filename}.md
```

Package files use Markdown with minimal YAML front matter because they carry the locked package record.

Intake bundle files use plain Markdown because they are pre-package capture notes.

## Link To Later Intake Package

When a bundle becomes an `intake` package, the package record may point back to the bundle path through `source_bundle_ref`.

The bundle file does not need to point forward to the package.

No automatic conversion is implied.

## Example Paths

Successful bundle example:

```text
space/intake_bundles/bundle_20260419T000000Z_omx_path_check_success.md
```

Failed bundle example:

```text
space/intake_bundles/bundle_20260419T001000Z_missing_artifact_failed.md
```

## Why This Fits Phase 1

The convention is flat, inspectable, and human-readable.

It keeps source-facing capture separate from package records.

It gives preserved bundles a stable place without introducing ingestion, indexing, promotion, or storage design.

## Non-Goals

- No automatic conversion.
- No watchers.
- No indexing engine.
- No validation.
- No hook integration.
- No runtime ingestion.
- No package promotion logic.

