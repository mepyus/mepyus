# Intake Bundle To Intake Package Handoff Minimum v0

## Purpose

This spec defines the minimal manual rule for turning an intake bundle into an `intake` package.

It is human-operated and spec-only.

## Boundary

An intake bundle is a pre-package external capture.

An intake package is the first accepted space record for that material.

The handoff does not convert every bundle into a package.

## Minimum Readiness Condition

A bundle is eligible to become an `intake` package when a human can answer all three questions:

```text
What external result was captured?
Why should this enter the space layer?
What is the next space-facing move?
```

If any answer is missing, unclear, or blocked by unavailable source material, the bundle should remain only a bundle.

## Thin Carry-Over Mapping

When creating an `intake` package from a bundle, carry over only the minimum useful meaning:

```text
bundle source_tool -> package origin
bundle file path -> package source_bundle_ref
bundle source_refs or outputs_artifacts -> package bounded_content_pointer when it is the smallest useful pointer
bundle short_tool_summary plus human judgment -> package short_summary
bundle suggested_next_move plus language_bridge_notes -> package next_action
```

The package should set:

```text
package_kind: intake
status: open
```

Use `status: blocked` only when the material is accepted into the space but cannot move forward because a concrete blocker remains.

## What Is Not Carried Directly

Do not copy full raw logs, full transcripts, complete command output, large generated artifacts, retry details, hook payloads, worker state, UI state, or execution metadata into the package record.

Do not carry bundle wording mechanically when it is only source-facing.

The package should restate the material in space-facing language.

## What Remains A Pointer

The original bundle remains a pointer through `source_bundle_ref`.

Raw logs, artifacts, source files, or command outputs remain pointers through `bounded_content_pointer` when they are the smallest useful bounded content.

If the bundle itself is the best bounded content, `bounded_content_pointer` may point to the bundle file.

## Why Bundle And Package Stay Distinct

The bundle preserves what came from outside.

The package records what the space accepts for digestion, review, connection, or memory maturation.

Keeping them distinct prevents provisional external captures from being mistaken for accepted space records.

It also keeps raw tool output separate from the package meaning contract.

## When A Bundle Should Stay Bundle-Only

Keep a bundle only as a bundle when source material is missing, the result cannot be inspected, the relevance to the space is unclear, the next space-facing move is unknown, or the capture is only a scratch note.

Bundle-only status does not mean failure of the package system.

It means the material has not crossed the manual acceptance boundary.

## Tiny Mapping Example

Successful bundle becomes intake package:

```text
bundle: space/intake_bundles/bundle_20260419T000000Z_omx_path_check_success.md

package_id: pkg_omx_path_check_001
package_kind: intake
origin: local_filesystem_check
source_bundle_ref: space/intake_bundles/bundle_20260419T000000Z_omx_path_check_success.md
bounded_content_pointer: references/git_search/oh-my-codex-main/
status: open
short_summary: Source evidence confirms the current local OMX reference checkout path.
next_action: Review whether path normalization should be recorded as a digestion package.
```

Failed bundle stays bundle-only:

```text
bundle: space/intake_bundles/bundle_20260419T001000Z_missing_artifact_failed.md

reason: The source artifact is missing, so the captured result cannot be inspected enough to enter the space layer.
next human move: Verify the artifact path before creating any intake package.
```

## Non-Goals

- No automatic conversion.
- No parser design.
- No validation engine.
- No watcher or ingestion loop.
- No package promotion beyond intake.
- No line or axis automation.
- No UI behavior.

