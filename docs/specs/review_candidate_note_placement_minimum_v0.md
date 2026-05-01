# Review Candidate Note Placement Minimum v0

## Purpose

This spec defines the phase-1 placement rule for review candidate notes.

It is placement guidance only.

## Default Placement

In phase 1, a review candidate note should live inside the body of the related `digestion` package file.

Do not create a separate note file by default.

Do not create a new directory for review candidate notes by default.

## Body Section Marker

Mark the note with a Markdown section heading:

```markdown
## Review Candidate Note
```

The section should stay short and human-readable.

It is not front matter and not a new schema.

## When Body-First Is Appropriate

Body-first placement is appropriate when the note is short, directly about one digestion package, and only records review-readiness.

The note should remain secondary to the digestion package.

The digestion package remains the interpretation record.

## Why It Should Not Become A Package Yet

A review candidate note says the digestion work may be ready for review reading.

It does not record actual review judgment.

Only actual review work should become a `review` package.

Keeping the note inside the digestion package prevents readiness from being mistaken for routing, promotion, or review output.

## Why A Separate File Is Not Default

A separate file would add a note layer before phase 1 has shown pressure for it.

It would also require naming, placement, linking, and cleanup conventions that are not needed yet.

Body-first placement keeps the digestion record readable in one place.

## Future Split Conditions

A future split may be justified if review candidate notes become long, repeated across many packages, referenced independently, reviewed separately, or numerous enough that digestion package bodies become hard to scan.

A future split may also be justified if one digestion package needs multiple distinct review candidate notes.

Until that pressure appears, keep notes in the digestion package body.

## Tiny Example

For:

```text
space/packages/digestion/pkg_digestion_omx_path_policy_001.md
```

Suggested body section shape:

```markdown
## Review Candidate Note

readiness: ready for review reading
digestion_work_done: Interpreted the OMX path-check material as current-path evidence, not a runtime decision.
clarified_point_for_review: The current path can be recorded without deciding a normalized alias.
first_review_pointer: space/packages/digestion/pkg_digestion_omx_path_policy_001.md
acceptable_uncertainty: The later alias name and path normalization policy remain open.
review_should_check: Whether this separation keeps phase 1 bounded and avoids premature path policy.
```

This section is only a note inside the digestion package body.

It is not a new package type, not a new file format, and not review routing.

## Non-Goals

- No new directories by default.
- No review routing.
- No promotion engine.
- No lifecycle automation.
- No line or axis extraction.
- No runtime behavior.
- No UI behavior.

