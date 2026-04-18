# Integrated Engine CLI Turn Route Classification Note v0

## Verdict

PASS

## This Round Goal

Step 3 was to make each VectorFL CLI conversation turn readable as a route candidate.

This is not auto-routing, not assignment execution, not engine execution, and not deposit ingestion. It is a visible classification layer so the supervisor can see whether a turn should be reread in VectorFL, considered for User-surface assignment, considered as an Engine request, held, or prepared as a deposit candidate.

## Modified Files

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_cli_turn_route_classification_note_v0.md`
- `docs/reports/integrated_engine_next_operating_checklist_v0.md`

## What Changed

The CLI mark set now includes:

- `user_assignment_candidate`
- `engine_request_candidate`
- `hold`

The existing marks remain:

- `reread_target`
- `implementation_return`
- `validation_target`
- `deposit_candidate`

The API now classifies a turn into one of the Step 3 route labels:

- `vectorfl_reread`
- `user_assignment_candidate`
- `engine_request_candidate`
- `deposit_candidate`
- `hold`

The VectorFL CLI panel now shows a route badge on the latest turn and recent turn cards. It also exposes route mark buttons for user assignment candidate, engine request candidate, and hold.

## Classification Rule

The route label is derived from marks first, then from `suggested_next_use`.

Current priority:

1. `hold` or failed status -> `hold`
2. `user_assignment_candidate` mark -> `user_assignment_candidate`
3. `deposit_candidate` mark -> `deposit_candidate`
4. `engine_request_candidate`, `implementation_return`, or `validation_target` mark -> `engine_request_candidate`
5. `suggested_next_use = implementation_return | validation_target` -> `engine_request_candidate`
6. `suggested_next_use = deposit_candidate` -> `deposit_candidate`
7. otherwise -> `vectorfl_reread`

This priority is intentionally conservative. A label is a next-reading candidate, not completion.

## Verification

Build verification:

```text
cd app/ui/integrated_engine
npm run build
```

Result: PASS.

User-assignment route smoke:

```text
session_id: cli_20260416T123507Z_64047d89
mark: user_assignment_candidate
computed route_label: user_assignment_candidate
```

Engine-request route smoke:

```text
session_id: cli_20260416T123852Z_1ad257c6
mark: engine_request_candidate
computed route_label: engine_request_candidate
```

API state verification through `build_cli_host_control_state(Path("runtime"))` showed:

```text
latest route_label = engine_request_candidate
recent route_label includes user_assignment_candidate
available_marks includes user_assignment_candidate / engine_request_candidate / hold
```

## What Passed

- Route labels are visible without opening raw session artifacts.
- User assignment and engine request candidate marks are accepted by the API.
- Route labels do not execute assignment, engine processing, or deposit.
- The CLI remains an on-top tool layer.
- The 3-surface body remains intact.

## Watchpoints

1. Route labels can overlap with older marks; current priority keeps user-assignment explicit when selected.
2. Step 4 still needs a real User-surface assignment handoff, not just a route badge.
3. Step 5 still needs Engine request candidate visibility, not execution.

## Next Small Valid Step

Start Step 4: User Assignment Handoff.

The next step should allow a routed CLI turn to become a candidate assignment to a selected User-surface team/role while keeping detailed reread in VectorFL.
