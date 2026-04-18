# Integrated Engine Translation Meaning Layer Contract v0

## 1. Verdict

PASS_WITH_NOTE

This contract defines a bounded meaning layer for the current one-handler package. It does not redesign the layout, add handlers, automate bridges, or change the current slot architecture.

## 2. Purpose

The meaning layer makes the current translation chain explicit:

```text
Engine result meaning
-> VectorFL state / reason
-> User next-action reason
```

It translates current package and return-record fields into compact operating meaning. It is not raw trace, full return detail, or a new package schema.

## 3. Engine-Side Meaning Fields

| field | role | supported by current fields | status |
| --- | --- | --- | --- |
| `engine_meaning_summary` | What the engine result means relative to the current purpose | return record `output_summary`, package `output_summary` | derived / supported |
| `engine_completion_status` | Whether the run is complete, partial, or candidate-only | return record `validation_state`, `return_redeposit_summary`, authority boundary | derived / supported |
| `engine_uncertainty_notes` | What remains uncertain or unsafe to infer | return record `surface_results.*.remaining_risk`, `what_was_not_done` | derived / partial |
| `engine_not_done_summary` | What the engine explicitly did not authorize or finish | return record `what_was_not_done`, package `authority_boundary` | directly supported |

## 4. VectorFL-Side Meaning Fields

| field | role | supported by current fields | status |
| --- | --- | --- | --- |
| `vectorfl_state` | Current interpreted state | package `current_status` | directly supported |
| `vectorfl_state_reason` | Why that state is assigned | package `evidence_summary`, return `validation_state`, bridge dependency-heavy finding | derived / supported |
| `vectorfl_blocker_summary` | Main blocker or open edge | package `support_detail.blocker`, return `surface_results.vectorfl.remaining_risk` | directly supported |
| `vectorfl_open_edge_summary` | What remains unresolved | bridge maturity notes, return record risks | derived / partial |
| `vectorfl_next_route_reason` | Why the current next route is preferred | package `next_valid_action`, return `next_valid_use`, authority boundary | derived / supported |

## 5. User-Side Meaning Fields

| field | role | supported by current fields | status |
| --- | --- | --- | --- |
| `user_now_meaning` | What this means for the user now | package `purpose`, `current_status`, return `output_summary` | derived / supported |
| `user_next_action_reason` | Why the suggested action is current | package `next_valid_action`, return `next_valid_use`, risks | derived / supported |
| `user_warning_summary` | What the user should not overread | package `scope.excluded`, return `what_was_not_done`, authority boundary | directly supported |

## 6. Placement Contract

User front-safe:

- `user_now_meaning`
- `user_next_action_reason`
- `user_warning_summary`

VectorFL front-safe:

- `vectorfl_state`
- `vectorfl_state_reason`
- `vectorfl_blocker_summary`
- `vectorfl_open_edge_summary`
- `vectorfl_next_route_reason`

Engine front-safe:

- `engine_meaning_summary`
- `engine_completion_status`
- `engine_uncertainty_notes`
- `engine_not_done_summary`

Inspector-only:

- full return record
- full evidence bundle
- packet formation detail
- full bridge rules
- lower-input trace

## 7. Boundaries

This layer does not authorize:

- second handler expansion
- team system expansion
- bridge automation
- upper/lower unification
- canonical redeposit
- final glossary or UI copy lock

## 8. Validation

- Contract is bounded: passed.
- Meaning fields are distinct from raw trace fields: passed.
- Current-field support vs derived inference is separated: passed.

