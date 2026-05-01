# Review Package Body Note Minimum v0

## Purpose

This spec defines the minimal body-note convention for writing actual review work inside a `review` package.

It is a human-readable writing convention only.

## Default Placement

Write review body notes inside the body of the related `review` package file.

Do not add new front matter fields.

Do not create a separate note file by default.

## Section Marker

Use this Markdown heading:

```markdown
## Review Note
```

The section records actual checking or judgment work.

## Minimum Content

A minimal review note should help a human record:

- what source or package was checked;
- what point was examined;
- what was confirmed or challenged;
- what remains unresolved;
- what the next review move may be.

The wording may be plain prose or short labeled lines.

Do not turn the section into a validation schema.

## Difference From Review Candidate Note

A review candidate note belongs to a `digestion` package and says the digestion work may be ready for review.

A review note belongs to a `review` package and records checking or judgment work that has begun.

The candidate note frames what should be checked.

The review note records what checking is finding.

## Difference From Memory Note

A review note checks, challenges, confirms, or leaves open a point.

It does not promote durable recall, reusable wording, or long-term memory.

Memory work may become later package work, but it is not part of this body-note convention.

## Checking Focus

Keep the review package body focused on what was inspected and what judgment is emerging.

Do not add acceptance automation, memory routing, line extraction, axis extraction, UI behavior, runtime behavior, or lifecycle state expansion.

## Length Guidance

Keep the note short when the review checks one clear point.

Use a slightly more explanatory note when the checked point, challenge, or unresolved uncertainty needs one or two sentences of context.

If the note grows into multiple independent judgments, create later package guidance before adding structure.

## Tiny Example Section Shape

```markdown
## Review Note

source_checked: space/packages/digestion/pkg_digestion_omx_path_policy_001.md
point_examined: Whether current OMX path evidence is kept separate from future alias policy.
confirmed_or_challenged: Confirmed that the separation is bounded and does not decide runtime behavior.
unresolved: The later alias name and path normalization policy remain open.
next_review_move: Check whether this wording is stable enough for memory consideration later.
```

This is a body note only.

It is not a new schema, package kind, acceptance engine, memory route, line extraction, or axis extraction.

## Non-Goals

- No acceptance automation.
- No routing to memory.
- No line extraction.
- No axis extraction.
- No promotion logic.
- No runtime behavior.
- No UI behavior.

