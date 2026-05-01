# Structured Evidence Contract v0

## Status

- phase: `phase1_8_structured_asset_reading_hardening`
- authority: `working_spec`
- compatibility: additive to Phase 1.6/1.7 evidence units

## Execution

Structured evidence unit fields:

- `source_ref`
- `asset_kind`
- `pointer`
- `path_ref`
- `node_kind`
- `shape_summary`
- `value_excerpt`
- `why_it_matters`
- `relation_type`
- `grounding_status`
- `local_confidence`
- `salience_reason`
- `comparison_hint`

Allowed `asset_kind` values:

- `runtime_contract`
- `runtime_artifact`
- `generated_json`
- `config_json`
- `structured_note`

Allowed `node_kind` values:

- `scalar`
- `object`
- `array`
- `object_member`
- `array_item`
- `shape_summary`
- `diff_node`

`path_ref` should use a JSONPath-like dotted path such as:

- `$.contract_id`
- `$.evidence_units[0].grounding_status`
- `$.validation.learning_fields_present`

If a path cannot be identified, fallback to the file pointer and mark the structured status as `shape_only` or `pointer_only`.

## Interpretation

Prose excerpts and structured evidence should not be treated as identical. A prose excerpt is read as local language. A structured artifact is read as shape plus field/path implications. `value_excerpt` alone is not enough because `true`, `merge`, or `v1` only matters when tied to a path and reason.

`path_ref` and `shape_summary` work together. `path_ref` gives the precise node. `shape_summary` tells whether the node is a scalar, object, array, or contract-shaped container. `salience_reason` is crucial because structured data can expose many fields; only some matter for the current question.

## Validation

- Structured fields are additive and do not remove prose evidence fields.
- Pointer fallback remains valid.
- Human readers can see why a node was selected.
- Artifact size remains bounded.
