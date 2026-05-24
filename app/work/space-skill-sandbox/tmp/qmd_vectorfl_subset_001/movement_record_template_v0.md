# Movement Record Template v0

## Status

```yaml
status: template_candidate
baseline_lock: false
automation: false
writer_created: false
purpose: closeout_as_return_to_space
```

Movement Record is a lightweight markdown record. It is not a database schema and not an automatic writer target.

Use it when an external-tool run, planning package, or bounded exploration has created reusable judgment.

```markdown
# MOVEMENT_RECORD

## Status

status:
date:
baseline_lock: false
automation: false

## Input Purpose

[What the user or package asked for.]

## Activated Space Memory

- Line:
- Axis:
- Camera:
- Lens:
- Stable anchor:
- Session anchor:

## Space Assets Consulted

- `[path]`: [use]
- `[path]`: [use]

## External Tool Role

[Codex / Gemini / Hermes / OmX / other role and boundary.]

## Tool Output Summary

[Short summary of what happened.]

## Read Trace / Evidence

- `[path or output]`: [claim supported]

## Issue / Watch Item

- [watch, gap, drift, or boundary note]

## User Decision Point

[Only if a user decision was required.]

## Return-to-Space Value

- Recoverable material:
- Reusable judgment:
- Issue / watch:
- Future reuse note:

## Next Re-Entry Trigger

- [When this record should reappear.]

## Do Not

- [What should not be promoted or automated from this record.]
```

## Relation To Existing Return Record Minimum

This template extends the spirit of `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md` for external-tool movement.

Keep it lighter than a package sidecar. If it becomes heavy, preserve pointers and compress the judgment.

