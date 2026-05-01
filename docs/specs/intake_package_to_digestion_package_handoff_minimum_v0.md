# Intake Package To Digestion Package Handoff Minimum v0

## Purpose

This spec defines the minimal manual rule for creating a `digestion` package from an `intake` package that has a digestion candidate note.

It is human-operated and spec-only.

## Boundary

An `intake` package is the first accepted space record for material.

A `digestion` package is the first actual interpretation record for that material.

The handoff does not promote every intake package and does not create lifecycle machinery.

## Minimum Readiness Condition

An `intake` package with a digestion candidate note is eligible for a `digestion` package when a human can answer:

```text
What intake package is being interpreted?
What bounded source should digestion read first?
What specific meaning question should digestion clarify?
What uncertainty is allowed to remain unresolved?
```

The candidate note should already show that the next useful move is interpretation, not more source capture.

If the source cannot be read, the meaning question is unclear, or the note only parks the material, the package should remain intake-only.

## Thin Carry-Over Mapping

When manually creating a `digestion` package, carry over only the minimum useful meaning:

```text
intake package path -> digestion source_bundle_ref
intake bounded_content_pointer or candidate first_source_pointer -> digestion bounded_content_pointer
intake origin -> digestion origin when still accurate
candidate space_question plus digestion_should_clarify -> digestion short_summary
candidate digestion_should_clarify plus allowed_uncertainty -> digestion next_action
```

The digestion package should newly set:

```text
package_id: a new digestion package id
package_kind: digestion
created_at: the manual creation time
updated_at: the manual creation time
status: open
```

Use `status: active` only if interpretation work is already being written in the digestion package at creation time.

## What Is Not Copied Directly

Do not copy the full intake package body into the digestion package.

Do not copy the digestion candidate note mechanically.

Do not copy full raw logs, transcripts, execution metadata, bundle text, or source artifacts.

Summarize the readiness note into a digestion-facing purpose.

Keep raw material as a pointer through `bounded_content_pointer`.

## How The Digestion Package Points Back

The digestion package should point back to the intake package path through `source_bundle_ref`.

This keeps the intake package as the accepted source record and the digestion package as the interpretation record.

## When Intake Should Remain Intake-Only

An intake package should remain intake-only even with a candidate note when the source pointer is missing, the candidate note is vague, the question is not interpretable, the next useful move is more capture, or no human is ready to begin interpretation.

The presence of a candidate note is not a promotion trigger.

## Intake Versus Digestion Package

The intake package records accepted material and source context.

The digestion package records actual interpretation intent and work.

The digestion package may begin with a thin purpose and next action, but it should not pretend that interpretation output already exists.

## Tiny Mapping Example

Source intake package:

```text
space/packages/intake/pkg_intake_omx_path_check_001.md
```

Hypothetical digestion package path:

```text
space/packages/digestion/pkg_digestion_omx_path_policy_001.md
```

Thin manual carry-over:

```text
package_id: pkg_digestion_omx_path_policy_001
package_kind: digestion
origin: local_filesystem_check
created_at: 2026-04-19T00:00:00Z
updated_at: 2026-04-19T00:00:00Z
source_bundle_ref: space/packages/intake/pkg_intake_omx_path_check_001.md
bounded_content_pointer: references/git_search/oh-my-codex-main/
status: open
short_summary: Interpret the OMX path-check intake material into a phase-1 path policy question.
next_action: Clarify current-path evidence versus future alias policy without deciding runtime behavior.
```

This example shows a new package record shape only.

It is not automatic promotion and not line or axis interpretation output.

## Non-Goals

- No automatic promotion.
- No line or axis inference.
- No lifecycle engine.
- No UI behavior.
- No runtime behavior.
- No storage or index design.
- No review or memory branching rules.

