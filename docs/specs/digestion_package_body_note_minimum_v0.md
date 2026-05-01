# Digestion Package Body Note Minimum v0

## Purpose

This spec defines the minimal body-note convention for writing interpretation work inside a `digestion` package.

It is a human-readable writing convention only.

## Default Placement

Write digestion body notes inside the body of the related `digestion` package file.

Do not add new front matter fields.

Do not create a separate note file by default.

## Section Marker

Use this Markdown heading:

```markdown
## Digestion Note
```

The section records actual interpretation work, not readiness.

## Minimum Content

A minimal digestion note should help a human record:

- what source was read;
- what meaning question was examined;
- what was clarified;
- what remains unresolved;
- what the next interpretation move may be.

The wording may be plain prose or short labeled lines.

Do not turn the section into a validation schema.

## Difference From Digestion Candidate Note

A digestion candidate note belongs to an `intake` package and says the material may be ready for digestion reading.

A digestion note belongs to a `digestion` package and records interpretation work that has begun.

The candidate note asks whether to interpret.

The digestion note records what the interpretation is finding.

## Difference From Review Or Memory Notes

A digestion note should clarify meaning, uncertainty, and next interpretation movement.

It should not judge acceptance, correctness, or final quality as a review note would.

It should not promote durable recall, reusable wording, or long-term memory as a memory note would.

Review and memory may become later package work, but they are not part of this body-note convention.

## Interpretation Focus

Keep the digestion package body focused on what the source seems to mean for the space.

Do not add line extraction, axis extraction, routing decisions, review instructions, memory promotion, UI behavior, or runtime behavior.

## Length Guidance

Keep the note short when the interpretation is straightforward or only one clarification has been made.

Use a slightly more explanatory note when the source, question, or unresolved uncertainty needs one or two sentences of context.

If the note grows into multiple independent interpretations, create later package guidance before adding structure.

## Tiny Example Section Shape

```markdown
## Digestion Note

source_read: references/git_search/oh-my-codex-main/
meaning_question: Should the current OMX reference path be treated as direct evidence or as a later alias-policy question?
clarified: The current path can be recorded as source evidence without deciding a normalized alias yet.
unresolved: The later alias name and path policy remain open.
next_interpretation_move: Separate current-path wording from any future normalization rule.
```

This is a body note only.

It is not a new schema, package kind, extraction system, review route, or memory route.

## Non-Goals

- No line extraction.
- No axis extraction.
- No promotion logic.
- No routing to review.
- No routing to memory.
- No automation.
- No runtime behavior.
- No UI behavior.

