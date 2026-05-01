# Digestion Candidate Note Placement Minimum v0

## Purpose

This spec defines the phase-1 placement rule for digestion candidate notes.

It is placement guidance only.

## Default Placement

In phase 1, a digestion candidate note should live inside the body of the related `intake` package file.

Do not create a separate note file by default.

Do not create a new directory for digestion candidate notes by default.

## Body Section Marker

Mark the note with a Markdown section heading:

```markdown
## Digestion Candidate Note
```

The section should stay short and human-readable.

It is not front matter and not a new schema.

## When Body-First Is Appropriate

Body-first placement is appropriate when the note is short, directly about one intake package, and only records interpretation-readiness.

The note should remain secondary to the intake package.

The intake package remains the accepted space record.

## Why It Should Not Become A Package Yet

A digestion candidate note says the intake package may be ready for digestion reading.

It does not record actual interpretation work.

Only actual interpretation work should become a `digestion` package.

Keeping the note inside the intake package prevents readiness from being mistaken for promotion.

## Why A Separate File Is Not Default

A separate file would add a new note layer before phase 1 has shown pressure for it.

It would also require naming, placement, linking, and cleanup conventions that are not needed yet.

Body-first placement keeps the package readable in one place.

## Future Split Conditions

A future split may be justified if digestion candidate notes become long, repeated across many packages, referenced independently, reviewed separately, or numerous enough that package bodies become hard to scan.

A future split may also be justified if one intake package needs multiple distinct candidate notes.

Until that pressure appears, keep notes in the intake package body.

## Tiny Example

For:

```text
space/packages/intake/pkg_intake_omx_path_check_001.md
```

Suggested body section shape:

```markdown
## Digestion Candidate Note

readiness: ready for digestion reading
space_question: Should phase 1 use references/git_search/oh-my-codex-main/ directly or define a normalized alias policy later?
digestion_should_clarify: Separate current-path evidence from future path policy without making a runtime decision.
first_source_pointer: references/git_search/oh-my-codex-main/
allowed_uncertainty: The later alias name can remain undecided.
```

This section is only a note inside the intake package body.

It is not a new package type, not a new file format, and not promotion logic.

## Non-Goals

- No new directories by default.
- No indexing.
- No promotion engine.
- No lifecycle automation.
- No line or axis extraction.
- No runtime behavior.
- No UI behavior.

