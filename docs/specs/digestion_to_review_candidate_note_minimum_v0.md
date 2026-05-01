# Digestion To Review Candidate Note Minimum v0

## Purpose

This spec defines a minimal human note for deciding whether digestion work is ready for review reading.

It is a review-readiness note only.

## Definition

A review candidate note is a short human-written note attached to, or written inside, a `digestion` package.

It says why the digestion work may be ready for review.

It is not a `review` package.

It is not a routing rule or promotion trigger.

## Eligibility

A `digestion` package is eligible for a review candidate note when:

- at least one digestion note has clarified something;
- the clarified point can be inspected by another human;
- the remaining uncertainty is named;
- the next useful move is review reading, not more interpretation.

## Minimum Readiness Questions

Before saying digestion is ready for review reading, a human should answer:

```text
What digestion work was done?
What clarified point should review inspect?
What source pointer or package should review read first?
What uncertainty remains acceptable for review?
What should review judge or check?
```

The answers may be short.

## What May Remain Unresolved

The note does not need final acceptance, durable memory wording, line placement, axis placement, or review outcome.

It does not need to resolve every uncertainty from digestion.

Uncertainty is acceptable when it is named clearly enough for review to inspect.

## Difference From A Digestion Note

A digestion note records interpretation work inside a `digestion` package.

A review candidate note records that some part of that interpretation is ready to be inspected.

The digestion note clarifies meaning.

The review candidate note frames what should be checked.

## Difference From A Review Package

A review candidate note is not a `review` package.

It does not contain review judgment, acceptance, rejection, correction, or quality decision.

It may later help author a `review` package, but it does not require one and does not create one.

## When Digestion Should Stay Digestion-Only

Keep digestion work digestion-only when the interpretation is still unclear, the source has not been read enough, the clarified point cannot be stated, the remaining uncertainty is unnamed, or the next useful move is more interpretation.

Staying digestion-only is not failure.

It means review is not yet the next useful move.

## Ready For Review Reading

It is reasonable to say ready for review reading when a human can identify a clarified point and name what review should inspect or check.

This does not imply routing, promotion, lifecycle movement, or review package creation.

## Tiny Example

Digestion package:

```text
space/packages/digestion/pkg_digestion_omx_path_policy_001.md
```

Minimal review candidate note:

```text
digestion_package_ref: space/packages/digestion/pkg_digestion_omx_path_policy_001.md
readiness: ready for review reading
digestion_work_done: Interpreted the OMX path-check material as current-path evidence, not a runtime decision.
clarified_point_for_review: The current path can be recorded without deciding a normalized alias.
first_review_pointer: space/packages/digestion/pkg_digestion_omx_path_policy_001.md
acceptable_uncertainty: The later alias name and path normalization policy remain open.
review_should_check: Whether this separation keeps phase 1 bounded and avoids premature path policy.
```

This is only a readiness note.

It is not a review package and not a promotion rule.

## Non-Goals

- No automation.
- No review routing.
- No promotion engine.
- No line or axis extraction.
- No memory routing.
- No runtime behavior.
- No UI behavior.
- No storage or index design.

