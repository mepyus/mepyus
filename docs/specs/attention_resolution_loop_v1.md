# Attention Resolution Loop v1

## Purpose
- Add lifecycle rules to derived attention items.
- Keep queue status stable without modifying canonical state.

## Queue Status
- `new`
- `seen`
- `deferred`
- `resolved`
- `suppressed`
- `reopened`

## Current Automatic Loop Scope
- v1 automatically derives:
  - `new`
  - `suppressed`
  - `resolved`
  - `reopened`
- `seen` and `deferred` remain reserved for explicit operator interaction.

## Transition Rules
- `new -> suppressed`
  - repeated provenance-only background update
  - flooding prevention
- `new/seen/deferred -> resolved`
  - attention no longer supported by latest routing result
  - superseded by newer attention signature
  - absorbed into background provenance summary
- `resolved/suppressed -> reopened`
  - same asset gets a new active canonical shift
  - same or replacement signature reactivates attention

## Strict vs Normal Resolution
- strict attention reasons:
  - `traceability_shift`
  - `grounding_shift`
  - `blocker_added`
  - `packet_texture_shift`
  - `manual_correction_requires_attention`
- normal attention reasons:
  - provenance-only and lighter shifts

## Attention Signature
- derived from:
  - `asset_id`
  - `priority_level`
  - `diff_class`
  - `changed_fields` signature
  - `attention_reason`
  - trigger family

## Duplicate / Merge
- repeated provenance-only runtime updates merge into background summary
- identical active signature is not re-added as a separate active attention item

## Guards
- resolution never edits canonical state
- raw history remains immutable
- `experimental_namespace` does not drive lifecycle transitions
