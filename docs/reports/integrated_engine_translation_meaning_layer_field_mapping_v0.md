# Integrated Engine Translation Meaning Layer Field Mapping v0

## 1. Verdict

PASS_WITH_NOTE

The current one-handler package and return record can support a compact meaning layer, but several fields are derived rather than directly present.

## 2. Source Materials

Primary sources:

- `runtime/contracts/integrated_engine_single_handler_package_instance_v0.json`
- `runtime/contracts/integrated_engine_single_handler_return_record_instance_v0.json`
- current one-handler UI constants in `VectorFLIntegrationShell.tsx`

Supporting context:

- current slot architecture docs
- current material collection gap note
- bridge maturity findings that bridge remains dependency-heavy

## 3. Engine Meaning Mapping

| meaning field | current source field(s) | support level | note |
| --- | --- | --- | --- |
| `engine_meaning_summary` | package `output_summary`, return `output_summary` | supported / derived | Summarizes that one package can move across surfaces with different density. |
| `engine_completion_status` | return `validation_state`, return `return_redeposit_summary` | supported / derived | Must remain candidate-only, not complete/canonical. |
| `engine_uncertainty_notes` | return `surface_results.*.remaining_risk` | partial / derived | Risks are surface-specific, not a single engine uncertainty field. |
| `engine_not_done_summary` | return `what_was_not_done`, package `authority_boundary` | directly supported | Strong boundary source. |

## 4. VectorFL Meaning Mapping

| meaning field | current source field(s) | support level | note |
| --- | --- | --- | --- |
| `vectorfl_state` | package `current_status` | direct | Current state is `usable_with_hold`. |
| `vectorfl_state_reason` | package `evidence_summary`, return `validation_state`, return `output_summary` | supported / derived | The package is usable because flow is visible; hold remains because bridge/automation/final translation are not authorized. |
| `vectorfl_blocker_summary` | package `support_detail.blocker`, return `surface_results.vectorfl.remaining_risk` | direct | Main blocker is dependency-heavy bridge and dense CliHost packet controls. |
| `vectorfl_open_edge_summary` | return risks, material collection gap note | partial / derived | Open edge is translation clarity and support detail density. |
| `vectorfl_next_route_reason` | package `next_valid_action`, return `next_valid_use` | supported / derived | Stabilize one-handler mode before expansion. |

## 5. User Meaning Mapping

| meaning field | current source field(s) | support level | note |
| --- | --- | --- | --- |
| `user_now_meaning` | package `purpose`, `current_status`, return `output_summary` | supported / derived | User can treat this as a usable one-handler operating surface, not final automation. |
| `user_next_action_reason` | package `next_valid_action`, return `next_valid_use`, return risks | supported / derived | Next action is conservative because remaining risks are support-density and bridge dependency. |
| `user_warning_summary` | package `scope.excluded`, return `what_was_not_done`, authority boundaries | direct | Strong warning source: no automation, no second handler, no canonical bridge. |

## 6. Missing / Newly Derived Fields

Newly derived in this package:

- `engine_meaning_summary`
- `engine_completion_status`
- `engine_uncertainty_notes`
- `vectorfl_state_reason`
- `vectorfl_open_edge_summary`
- `vectorfl_next_route_reason`
- `user_now_meaning`
- `user_next_action_reason`

Directly grounded:

- `vectorfl_state`
- `vectorfl_blocker_summary`
- `engine_not_done_summary`
- `user_warning_summary`

## 7. Validation

- Current-field support is separated from derived meaning: passed.
- Partial support is marked: passed.
- No fake certainty introduced: passed.

