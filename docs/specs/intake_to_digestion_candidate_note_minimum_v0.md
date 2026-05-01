# Intake To Digestion Candidate Note Minimum v0

## Purpose

This spec defines a minimal human note for deciding whether an `intake` package is ready for digestion reading.

It is an interpretation-readiness note only.

## Definition

A digestion candidate note is a short human-written note attached to, or written near, an `intake` package.

It says why the intake material may be worth interpreting into space meaning.

It is not a `digestion` package.

It is not a promotion rule.

## Eligibility

An `intake` package is eligible for a digestion candidate note when:

- the package has enough bounded content to read;
- the package has a space-facing reason to interpret it;
- the next useful move is interpretation, not more source capture;
- no missing source material blocks basic reading.

## Minimum Readiness Questions

Before saying an intake package is ready for digestion reading, a human should answer:

```text
What is the intake material?
What space-facing question or meaning does it raise?
What should digestion try to clarify?
What source pointer should digestion read first?
What uncertainty can remain unresolved for now?
```

The answers may be short.

## What May Remain Unresolved

The note does not need final claims, line placement, axis placement, durable memory wording, or review judgment.

It also does not need to resolve naming, future storage, UI behavior, or automation.

Uncertainty is acceptable if the material is readable and the interpretation question is clear.

## Difference From Intake Bundle To Intake Package Handoff

Bundle-to-package handoff decides whether external capture should enter the space layer.

The digestion candidate note decides whether an existing `intake` package is ready to be interpreted inside the space layer.

The first boundary is acceptance into space.

The second boundary is readiness for meaning work.

## Difference From A Digestion Package

A digestion candidate note identifies readiness.

A `digestion` package records actual interpretation work.

The note may later help author a `digestion` package, but it does not create one and does not require one.

## When Intake Should Stay Intake-Only

Keep an intake package intake-only when the source pointer is missing, the material cannot be read, the space-facing reason is unclear, the next action is more source capture, or the package only needs to be parked.

Staying intake-only is not failure.

It means interpretation is not yet the next useful move.

## Ready For Digestion Reading

It is reasonable to say ready for digestion reading when a human can point to readable bounded content and name the specific meaning question digestion should clarify.

This does not imply promotion, automation, or lifecycle movement.

## Tiny Example

Intake package:

```text
space/packages/intake/pkg_intake_omx_path_check_001.md
```

Minimal digestion candidate note:

```text
intake_package_ref: space/packages/intake/pkg_intake_omx_path_check_001.md
readiness: ready for digestion reading
material: Source evidence confirms the current local OMX reference checkout path.
space_question: Should phase 1 use references/git_search/oh-my-codex-main/ directly or define a normalized alias policy later?
digestion_should_clarify: Separate current-path evidence from future path policy without making a runtime decision.
first_source_pointer: references/git_search/oh-my-codex-main/
allowed_uncertainty: The later alias name can remain undecided.
```

This is only a readiness note.

It is not a digestion package and not a promotion rule.

## Non-Goals

- No automation.
- No promotion engine.
- No line or axis extraction system.
- No supervisor workflow expansion.
- No UI behavior.
- No runtime ingestion.
- No storage or index design.

