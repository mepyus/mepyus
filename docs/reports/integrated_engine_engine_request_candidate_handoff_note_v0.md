# Integrated Engine Engine Request Candidate Handoff Note v0

## Verdict

PASS

## This Round Goal

Step 5 was to make VectorFL-shaped CLI turns visible on the Engine surface as request candidates.

This is not engine execution, not processing automation, and not a write-back/deposit action. The goal was only to let the Engine surface see which CLI returns are ready to be considered as processing input.

## Modified Files

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_engine_request_candidate_handoff_note_v0.md`
- `docs/reports/integrated_engine_next_operating_checklist_v0.md`

## What Changed

The Engine surface `CLI Return / Validation Feed` now includes an `engine request candidates` area.

That area only includes CLI turns where:

- `route_label = engine_request_candidate`
- or mark includes `engine_request_candidate`

Each candidate card shows:

- route label
- session id
- purpose
- short structured return preview
- `Send to VectorFL` reread action
- `candidate only` boundary label

## Why This Is Bounded

The Engine surface now sees request candidates, but it still does not execute them.

No manifest shape changed, no engine processing endpoint was added, no auto-run was opened, and no candidate becomes canonical. The candidate can be sent back to VectorFL for reread before any next package opens.

## Verification

Build verification:

```text
cd app/ui/integrated_engine
npm run build
```

Result: PASS.

State smoke:

```text
engine_request_candidate_count: 7
first_candidate: cli_20260416T123852Z_1ad257c6
route_label: engine_request_candidate
marks: engine_request_candidate
```

This confirms engine request candidates are visible from the current CLI host state.

## What Passed

- Engine surface now has a bounded request-candidate view.
- The view uses route labels from VectorFL instead of treating all CLI returns as engine input.
- Candidate cards can be sent back to VectorFL for reread.
- No auto-execution or auto-deposit was introduced.
- The 3-surface body remains intact.

## Watchpoints

1. Some older `validation_target` turns classify as engine request candidates by conservative rule; this is acceptable for now but may need route tightening later.
2. Engine request candidates do not yet produce a formal request packet.
3. Return-to-VectorFL validation remains the next required loop before deposition.

## Next Small Valid Step

Start Step 6: Engine Return To VectorFL Validation Loop.

The next step should make engine-facing return material visible for VectorFL validation before any user decision or deposit candidate step.
