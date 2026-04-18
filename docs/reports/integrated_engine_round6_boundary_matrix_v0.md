# Integrated Engine Round 6 Boundary Matrix v0

Date: 2026-04-15

## 0. scope

This matrix records only the boundary that can be decided from current scaffold panels, Round 5 inventory, and the v1 candidate interface contract.

It does not add scaffold code, manifest fields, read-map entries, selected-object behavior, side-inspection detail, or trace UI.

## 1. matrix

| panel_id | empty_state_status | empty_state_kind | trace_allowed_now | trace_kind_now | future_only_note | promotion_gate_needed |
|---|---|---|---|---|---|---|
| `request_organization_panel` | required | shaped request material absent; neutral placeholder only | no | mapped read reason only | distribution/ownership hints remain future-only | no for placeholder; yes for ownership extension |
| `operating_flow_panel` | required | current-loop material absent; keep operating role visible | yes | core-support route-state labels and visual route rhythm | selected route detail remains future-only | yes for selected route behavior |
| `anchor_support_panel` | optional | active anchor material absent; criteria placeholder only | no | mapped read reason only | deeper anchor comparison detail remains future-only | no for placeholder; yes for comparison UI |
| `return_decision_panel` | required | return material absent; no completion/failure inference | yes | core-support return/recheck/reflux route wording | deeper return decision inspection remains future-only | yes for selected return detail |
| `anchor_context_panel` | optional | anchor criteria absent; mediation boundary remains visible | no | mapped read reason only | richer anchor comparison remains future-only | no for placeholder; yes for comparison UI |
| `maturation_canvas_panel` | required | maturation body absent; keep body-reading role visible | yes | core-support reflux and return contribution as context | selected maturation object values remain future-only | yes for selected-object value rendering |
| `validation_mediation_panel` | required | request/return comparison material absent; no decision inference | yes | core-support request/return review relation | research-assist or validation-team detail remains future-only | yes for assistance structure |
| `routing_reflux_panel` | required | reflux route material absent; no completion inference | yes | core-support reflux target / preserve-trace wording | denser route preservation rows remain future-only | yes for trace density |
| `evidence_history_panel` | optional | primary connection record absent; compact trace support may be quiet | yes | core-support primary connection record trace | broader connection-record rows remain future-only | yes for broader trace density |
| `work_input_panel` | required | shaped input absent; no raw-user bypass or engine idle inference | no | mapped read reason only | worker intake detail remains future-only | yes for worker/process detail |
| `execution_state_panel` | required | current-loop execution state absent; no runtime status inference | yes | core-support current slot / visual slot rhythm | worker/process state remains future-only | yes for worker/process detail |
| `result_return_panel` | required | return material absent; no product completion/failure inference | yes | core-support validation/follow-up route wording | return-material inspection remains future-only | yes for return inspection |
| `execution_history_panel` | optional | engine return route record absent; history support may be quiet | yes | core-support mapped engine-return validation record | denser process or route history remains future-only | yes for denser trace |

## 2. status key

### empty_state_status

- required: later value rendering needs a neutral placeholder to protect panel meaning
- optional: scaffold remains readable without a specific empty message
- held: not used for current panel rows; held applies to selected-object and side-inspection details outside current core panels

### trace_allowed_now

- yes: compact trace or route-support wording is already part of the panel question or mapped read reason
- no: only manifest read evidence is visible; no route or connection trace should be added

### trace_kind_now

- core-support only
- no live timeline
- no selected-object drilldown
- no runtime status
- no governance or authority signal

## 3. boundary sentence

The matrix locks only absence and trace boundaries. It does not turn empty states or trace into implemented UI behavior.
