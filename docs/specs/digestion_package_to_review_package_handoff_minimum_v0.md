# Digestion Package To Review Package Handoff Minimum v0

## Purpose

This spec defines the minimal manual rule for creating a `review` package from a `digestion` package that has a review candidate note.

It is human-operated and spec-only.

## Boundary

A `digestion` package is the interpretation work record.

A `review` package is the first actual checking or judgment record for that interpretation.

The handoff does not route every digestion package to review and does not create lifecycle machinery.

## Minimum Readiness Condition

A `digestion` package with a review candidate note is eligible for a `review` package when a human can answer:

```text
What digestion package is being reviewed?
What clarified point should review inspect?
What source pointer or package should review read first?
What uncertainty is acceptable during review?
What should review check or judge?
```

The review candidate note should already show that the next useful move is checking, not more interpretation.

If the clarified point is not inspectable, the uncertainty is unnamed, or the next useful move is more digestion, the package should remain digestion-only.

## Thin Carry-Over Mapping

When manually creating a `review` package, carry over only the minimum useful meaning:

```text
digestion package path -> review source_bundle_ref
candidate first_review_pointer or digestion package path -> review bounded_content_pointer
digestion origin -> review origin when still accurate
candidate clarified_point_for_review plus review_should_check -> review short_summary
candidate review_should_check plus acceptable_uncertainty -> review next_action
```

The review package should newly set:

```text
package_id: a new review package id
package_kind: review
created_at: the manual creation time
updated_at: the manual creation time
status: open
```

Use `status: active` only if review judgment is already being written in the review package at creation time.

## What Is Not Copied Directly

Do not copy the full digestion package body into the review package.

Do not copy the full digestion note or review candidate note mechanically.

Do not copy raw logs, source artifacts, line or axis assumptions, review outcomes, memory wording, or routing instructions.

Summarize the review-readiness note into a review-facing purpose.

Keep source material as a pointer through `bounded_content_pointer`.

## How The Review Package Points Back

The review package should point back to the digestion package path through `source_bundle_ref`.

This keeps the digestion package as the interpretation record and the review package as the checking record.

## When Digestion Should Remain Digestion-Only

A digestion package should remain digestion-only even with a review candidate note when the clarified point is vague, the source cannot be inspected, the review question is not clear, the uncertainty is unnamed, or no human is ready to begin review.

The presence of a review candidate note is not a promotion trigger.

## Digestion Versus Review Package

The digestion package records interpretation work.

The review package records actual checking or judgment work.

The review package may begin with a thin purpose and next action, but it should not pretend that review judgment already exists unless it is actually written there.

## Tiny Mapping Example

Source digestion package:

```text
space/packages/digestion/pkg_digestion_omx_path_policy_001.md
```

Hypothetical review package path:

```text
space/packages/review/pkg_review_omx_path_policy_001.md
```

Thin manual carry-over:

```text
package_id: pkg_review_omx_path_policy_001
package_kind: review
origin: local_filesystem_check
created_at: 2026-04-19T00:00:00Z
updated_at: 2026-04-19T00:00:00Z
source_bundle_ref: space/packages/digestion/pkg_digestion_omx_path_policy_001.md
bounded_content_pointer: space/packages/digestion/pkg_digestion_omx_path_policy_001.md
status: open
short_summary: Review whether the OMX path-policy digestion keeps current evidence separate from future alias policy.
next_action: Check whether the separation stays bounded and avoids premature path policy.
```

This example shows a new package record shape only.

It is not automatic promotion, not final review judgment, and not line or axis output.

## Non-Goals

- No automatic promotion.
- No review routing engine.
- No acceptance or rejection automation.
- No line or axis inference.
- No memory branching.
- No runtime behavior.
- No UI behavior.
- No storage or index design.

