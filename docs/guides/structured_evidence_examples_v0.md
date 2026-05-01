# Structured Evidence Examples v0

## Runtime Contract Field

```json
{
  "source_ref": "runtime/contracts/merge_diff_report_v1.json",
  "asset_kind": "runtime_contract",
  "path_ref": "$.evidence_depth_summary",
  "node_kind": "object",
  "shape_summary": "object keys: pointer_only, weak_grounded, direct_grounded, cross_supported, total",
  "value_excerpt": "{\"pointer_only\": 0, \"weak_grounded\": 0, ...}",
  "salience_reason": "Shows that merge reports can carry evidence-depth distribution."
}
```

## Generated Run Field

```json
{
  "source_ref": "runtime/merge_diff_reports/phase1_7_run_03_merge_diff_report.json",
  "asset_kind": "runtime_artifact",
  "path_ref": "$.chosen_mode",
  "node_kind": "scalar",
  "value_excerpt": "\"diff\"",
  "salience_reason": "The run preserved diff mode for a comparison question."
}
```

## Shape Only Fallback

```json
{
  "source_ref": "runtime/contracts/example.json",
  "asset_kind": "runtime_contract",
  "path_ref": "$",
  "node_kind": "shape_summary",
  "shape_summary": "object keys: contract_id, contract_status",
  "value_excerpt": "",
  "salience_reason": "Only top-level shape was readable; semantic field salience remains weak."
}
```

## Validation

Structured evidence should explain why a path matters, not merely show that the file is JSON.
