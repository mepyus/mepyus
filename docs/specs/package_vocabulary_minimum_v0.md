# Package Vocabulary Minimum v0

## Purpose

This spec defines the smallest allowed vocabulary for phase-1 package records.

It only locks `package_kind` and `status`.

## Allowed `package_kind`

- `intake`
- `digestion`
- `review`
- `memory`

No other `package_kind` values are part of phase 1.

## Allowed `status`

- `open`
- `active`
- `blocked`
- `held`
- `closed`

## Status Meanings

### `open`

Means the package exists and is available for attention.

Use when the package has been recorded but no current work is underway.

Does not imply priority, assignment, readiness, or automatic scheduling.

### `active`

Means the package is currently being worked.

Use when someone or some later process is actively reading, digesting, reviewing, or maturing it.

Does not imply a worker process, lock, automation, or exclusive ownership.

### `blocked`

Means the package cannot move forward until a concrete blocker is resolved.

Use when missing input, unclear source material, external dependency, or unresolved decision prevents useful progress.

Does not imply retry logic, failure state, escalation routing, or automated recovery.

### `held`

Means the package is intentionally paused even though it is not blocked.

Use when the material is valid but deferred, waiting for timing, context, or later judgment.

Does not imply rejection, closure, archive, or low value.

### `closed`

Means the package has no current next move in phase 1.

Use when the package has been accepted, superseded, discarded, or completed enough for now.

Does not imply deletion, permanent memory promotion, final truth, or irreversible archive.

## `next_action` Remains Free-Text

`next_action` stays free-text in phase 1 because the package record is a meaning contract, not a workflow engine.

A controlled action vocabulary would prematurely define lifecycle automation, assignment, retries, and promotion behavior.

Free text is enough to record the next intended move while the package system is still structure-first.

## Tiny Examples

```text
package_id: pkg_intake_001
package_kind: intake
status: open
short_summary: OMX session output received for later digestion.
next_action: Read once and decide whether it becomes digestion material.
```

```text
package_id: pkg_digestion_001
package_kind: digestion
status: active
short_summary: Extracting the layer split from the sidecar baseline.
next_action: Turn stable points into review notes.
```

```text
package_id: pkg_review_001
package_kind: review
status: blocked
short_summary: Package boundary wording needs a source-path decision.
next_action: Confirm whether the OMX reference path should remain canonical.
```

```text
package_id: pkg_memory_001
package_kind: memory
status: held
short_summary: Candidate durable rule: package is a meaning contract, not runtime.
next_action: Revisit after two more package specs use the same wording.
```

## Non-Goals

- No lifecycle state machine.
- No automation rules.
- No validation engine design.
- No retry logic.
- No worker state.
- No UI state.
- No promotion system.
- No graph relationships.

