# Review To Memory Candidate Note Minimum v0

## Purpose

This spec defines the minimal readiness note for when review work may be worth memory consideration.

It is a human-readable readiness convention only.

## Default Placement

Write the memory candidate note inside the body of the related `review` package file.

Do not add new front matter fields.

Do not create a `memory` package from this note alone.

## Section Marker

Use this Markdown heading:

```markdown
## Memory Candidate Note
```

The section records possible memory value, not memory promotion.

## Minimum Content

A minimal memory candidate note should help a human record:

- what review work was done;
- what result or wording may be worth preserving;
- why it may deserve memory consideration;
- what uncertainty or limit still remains;
- what should be checked before creating any actual memory package.

The wording may be plain prose or short labeled lines.

Do not turn the section into a validation schema.

## Difference From Review Note

A review note records checking or judgment work inside a `review` package.

A memory candidate note records that some reviewed result may be worth considering for durable reuse later.

The review note says what was checked.

The memory candidate note says what might be worth preserving after checking.

## Difference From A Memory Package

A memory candidate note is not a `memory` package.

It does not promote durable recall, create reusable wording, define permanence, or route material into memory.

It may later help author a `memory` package, but it does not require one and does not create one.

## Review-Primary Boundary

The review package body should remain review-primary.

The memory candidate note should stay short and secondary to the review work that produced it.

If the note starts carrying durable wording, reuse rules, or long-term recall claims, it is outgrowing this convention.

## Length Guidance

Keep the note short when it points to one reviewed result or one possible reusable wording.

Use a slightly more explanatory note when the memory value or remaining limit needs one or two sentences of context.

If multiple memory candidates appear, create later package guidance before adding structure.

## Tiny Example Section Shape

```markdown
## Memory Candidate Note

review_work_done: Checked that current OMX path evidence stays separate from future alias policy.
result_worth_preserving: Current-path evidence can be recorded without deciding a normalized alias.
why_memory_consideration: This wording may help future specs avoid collapsing source evidence into runtime policy.
remaining_limit: The later alias name and path normalization policy remain unresolved.
check_before_memory: Confirm the wording remains useful after at least one more path-related package.
```

This is a body note only.

It is not a new schema, package kind, memory package, routing rule, or promotion engine.

## Non-Goals

- No memory routing.
- No promotion engine.
- No line extraction.
- No axis extraction.
- No runtime behavior.
- No UI behavior.
- No automation.

