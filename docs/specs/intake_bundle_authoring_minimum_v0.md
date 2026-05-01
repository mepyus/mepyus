# Intake Bundle Authoring Minimum v0

## Purpose

This spec defines the smallest human-writing convention for phase-1 intake bundles.

It is for manual capture of external results before automatic OMX intake mapping exists.

## Definition

An intake bundle is a bounded capture of an external result before it becomes an `intake` package.

It is not yet a package record.

It does not need a `package_id`, `package_kind`, package `status`, or package file placement.

## Minimum Sections

Use these sections when manually writing an intake bundle:

```text
source_tool:
task_intent:
source_refs:
outputs_artifacts:
short_tool_summary:
known_risks_or_blockers:
suggested_next_move:
language_bridge_notes:
```

## Required Capture

`source_tool` is required. Name the external tool, system, or human process that produced the result.

`task_intent` is required. State what the external result was trying to answer or produce.

`short_tool_summary` is required. Summarize the result in a few sentences or less.

`suggested_next_move` is required. State the likely next human move if this bundle becomes intake material.

## Optional Or Nullable Capture

`source_refs` may be `null` when no source references are known.

`outputs_artifacts` may be `null` when no artifact path, log path, file path, or output pointer exists.

`known_risks_or_blockers` may be `null` when no risk or blocker is known.

`language_bridge_notes` may be `null` when no translation into space wording is needed yet.

Optional sections may be omitted only in very short scratch captures. If the bundle is being preserved for later package creation, include every section and use `null` where needed.

## Detail Boundary

Capture enough detail for a later human to decide whether an `intake` package should be created.

Do not paste large raw logs, full transcripts, full command outputs, or large generated artifacts into the bundle.

Point to raw logs or artifacts when they are longer than a short excerpt or when their exact contents matter.

Use short excerpts only when they are needed to understand the result without opening the raw artifact.

## Difference From A Package Record

An intake bundle captures what came from outside.

A package record gives material a stable place inside our space.

The bundle can be messy, provisional, and source-facing.

The package record should use the locked package fields, vocabulary, file placement, and authoring convention.

## Becoming An Intake Package

An intake bundle may become an `intake` package when a human decides the captured result should enter the space layer.

At that point, the package record should point back to the bundle through `source_bundle_ref` when possible.

The package `short_summary` should summarize why the material matters to the space, not merely repeat the tool output.

The package `next_action` should name the next space-facing move.

## Successful Result Example

```text
source_tool: external_search
task_intent: Check whether the current OMX reference path exists locally.
source_refs: references/git_search/oh-my-codex-main/
outputs_artifacts: null
short_tool_summary: The local reference checkout exists at references/git_search/oh-my-codex-main/. No shorter alias is present.
known_risks_or_blockers: The path name may differ from older notes that say oh-my-codex.
suggested_next_move: Create an intake package if path normalization needs review.
language_bridge_notes: Treat this as source-path evidence, not a runtime decision.
```

## Failed Result Example

```text
source_tool: external_command
task_intent: Inspect a referenced local artifact before package creation.
source_refs: null
outputs_artifacts: runtime/logs/missing_example.log
short_tool_summary: The command could not find the referenced artifact.
known_risks_or_blockers: The missing artifact prevents confident package creation.
suggested_next_move: Check whether the reference path was copied incorrectly.
language_bridge_notes: Keep this as blocked intake evidence until the source path is resolved.
```

## What To Omit In Phase 1

Omit hook payloads, parser-ready schemas, execution metadata, retry details, worker state, UI state, lifecycle transitions, line assignments, axis assignments, graph links, and validation results.

## Non-Goals

- No hook format.
- No automatic extraction.
- No schema validation.
- No lifecycle automation.
- No UI design.
- No storage engine.
- No line or axis automation.

