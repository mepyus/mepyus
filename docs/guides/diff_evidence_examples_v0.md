# Diff Evidence Examples v0

## Mode Shift

```json
{
  "path_ref": "$.chosen_mode",
  "change_type": "mode_shift",
  "before_excerpt": "\"merge\"",
  "after_excerpt": "\"diff\"",
  "delta_summary": "$.chosen_mode changed from merge to diff",
  "salience_reason": "Mode changes affect final response behavior."
}
```

## Evidence Depth Change

```json
{
  "path_ref": "$.evidence_depth_summary.cross_supported",
  "change_type": "evidence_depth_change",
  "before_excerpt": "5",
  "after_excerpt": "8",
  "delta_summary": "cross-supported evidence count increased",
  "salience_reason": "Evidence depth is a direct grounding-quality signal."
}
```

## Trivial Diff

```json
{
  "path_ref": "$.created_at",
  "change_type": "modified",
  "salience_reason": "Usually low salience unless the question asks about timing."
}
```

## Validation

Diff evidence should show what changed and why the change matters.
