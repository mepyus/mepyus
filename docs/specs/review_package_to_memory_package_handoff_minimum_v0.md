# Review Package To Memory Package Handoff Minimum v0

## Purpose

This spec defines the minimal manual rule for creating a `memory` package from a `review` package that has a memory candidate note.

It is human-operated and spec-only.

## Boundary

A `review` package is the checking or judgment work record.

A `memory` package is the first durable preservation record for reviewed material.

The handoff does not route every review package to memory and does not create lifecycle machinery.

## Minimum Readiness Condition

A `review` package with a memory candidate note is eligible for a `memory` package when a human can answer:

```text
What review package is the source?
What reviewed result or wording may be worth preserving?
Why is it useful beyond this one package?
What limit or uncertainty remains?
What should still be checked after memory package creation?
```

The memory candidate note should already show that the next useful move is durable preservation consideration, not more review.

If the reviewed result is vague, the reuse value is unclear, or the remaining limit is unnamed, the package should remain review-only.

## Thin Carry-Over Mapping

When manually creating a `memory` package, carry over only the minimum useful meaning:

```text
review package path -> memory source_bundle_ref
review bounded_content_pointer or review package path -> memory bounded_content_pointer
review origin -> memory origin when still accurate
candidate result_worth_preserving plus why_memory_consideration -> memory short_summary
candidate check_before_memory plus remaining_limit -> memory next_action
```

The memory package should newly set:

```text
package_id: a new memory package id
package_kind: memory
created_at: the manual creation time
updated_at: the manual creation time
status: open
```

Use `status: active` only if durable memory wording is already being written in the memory package at creation time.

## What Is Not Copied Directly

Do not copy the full review package body into the memory package.

Do not copy the full review note or memory candidate note mechanically.

Do not copy review routing assumptions, line or axis assumptions, lifecycle state, acceptance automation, or source artifacts.

Summarize the memory candidate note into a memory-facing preservation purpose.

Keep source material as a pointer through `bounded_content_pointer`.

## How The Memory Package Points Back

The memory package should point back to the review package path through `source_bundle_ref`.

This keeps the review package as the checking record and the memory package as the durable preservation record.

## When Review Should Remain Review-Only

A review package should remain review-only even with a memory candidate note when the result is not stable enough, reuse value is unclear, the remaining limit is unnamed, or no human is ready to begin memory writing.

The presence of a memory candidate note is not a promotion trigger.

## Review Versus Memory Package

The review package records checking or judgment work.

The memory package records durable preservation intent and later durable wording.

The memory package may begin with a thin preservation purpose and next action, but it should not pretend that final durable memory wording already exists unless it is actually written there.

## Tiny Mapping Example

Source review package:

```text
space/packages/review/pkg_review_omx_path_policy_001.md
```

Target memory package path:

```text
space/packages/memory/pkg_memory_omx_path_policy_001.md
```

Thin manual carry-over:

```text
package_id: pkg_memory_omx_path_policy_001
package_kind: memory
origin: local_filesystem_check
created_at: 2026-04-19T00:00:00Z
updated_at: 2026-04-19T00:00:00Z
source_bundle_ref: space/packages/review/pkg_review_omx_path_policy_001.md
bounded_content_pointer: space/packages/review/pkg_review_omx_path_policy_001.md
status: open
short_summary: Preserve the reviewed wording that current-path evidence can be recorded without deciding a normalized alias.
next_action: Recheck the wording after another path-related package while keeping alias policy unresolved.
```

This example shows a new package record shape only.

It is not automatic promotion, not memory routing, and not line or axis output.

## Non-Goals

- No automatic promotion.
- No memory routing engine.
- No lifecycle machinery.
- No line or axis inference.
- No runtime behavior.
- No UI behavior.
- No storage or index design.

