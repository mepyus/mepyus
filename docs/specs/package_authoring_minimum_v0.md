# Package Authoring Minimum v0

## Purpose

This spec defines minimal human authoring rules for phase-1 package records.

It is a writing convention only.

## Field Presence

Every locked package record field should appear in front matter every time:

```text
package_id
package_kind
origin
created_at
updated_at
source_bundle_ref
bounded_content_pointer
status
short_summary
next_action
```

Do not add new front matter fields in phase 1.

## Unknown And Empty Values

Use `null` when the value is unknown or not available yet.

Use an empty string `""` only when the value is intentionally blank and the blank itself is meaningful.

Do not use an empty list `[]` in phase-1 package records. The locked minimum record has no list fields.

Prefer `null` over guessing.

Prefer a short concrete value over a placeholder phrase such as `TBD`.

## Timestamps

Write timestamps in UTC ISO 8601 form:

```text
YYYY-MM-DDTHH:MM:SSZ
```

Use the same value for `created_at` and `updated_at` when first authoring a package record.

Only change `updated_at` when the package record is manually updated.

## `package_id`

Use lowercase ASCII letters, numbers, and underscores.

Start with `pkg_`.

Keep the filename stem identical to `package_id`.

Example:

```text
package_id: pkg_example_intake_001
file: space/packages/intake/pkg_example_intake_001.md
```

## `short_summary`

Write one sentence or sentence fragment.

State what the package is about, not what the whole system does.

Keep it specific enough that a human can scan a folder and understand why the package exists.

## `next_action`

Write free text.

Name the next intended human move in plain language.

Do not encode workflow commands, automation states, retry instructions, or assignment rules.

## `bounded_content_pointer`

Point to the smallest useful bounded content location.

If the package body itself is the only bounded content, `bounded_content_pointer` may temporarily point to the package file itself.

Use `null` only when no bounded content location is known yet.

## Markdown Body

The body is optional.

Keep the body very short when front matter is enough and the package only needs a scan note.

Use a slightly explanatory body when a human needs one or two sentences to understand context, uncertainty, or why the next action is written that way.

Do not use the body to add new structured fields.

## Good Authoring Example

```markdown
---
package_id: pkg_example_review_002
package_kind: review
origin: space_package_example
created_at: 2026-04-19T00:00:00Z
updated_at: 2026-04-19T00:00:00Z
source_bundle_ref: pkg_example_digestion_001
bounded_content_pointer: docs/specs/package_record_minimum_v0.md
status: open
short_summary: Review whether the package record remains meaning-first.
next_action: Check for fields that imply lifecycle automation.
---

# Package Notes

This record needs a quick boundary inspection before reuse.
```

## Avoid This

```markdown
---
package_id: review package 2
package_kind: inspection
origin: TBD
created_at: today
updated_at:
source_bundle_ref: []
bounded_content_pointer: ""
status: needs_retry
short_summary: This is about everything.
next_action: assign_to_worker_and_retry_until_done
priority: high
---
```

This example adds fields, invents vocabulary, uses vague placeholders, uses an empty list, weakens timestamp consistency, and turns `next_action` into workflow logic.

## Non-Goals

- No validation engine.
- No schema enforcement.
- No authoring CLI.
- No auto-generated timestamps.
- No linting rules.
- No loader behavior.
- No migration logic.

