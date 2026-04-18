# Integrated Engine Input Surface To Engine Ingest Mapping v0

## 1. Verdict

PASS_WITH_NOTE

The bridge from the 3 surfaces to engine ingest is clearer when read as role-filtered movement:

```text
User Surface purpose/material context
-> VectorFL interpretation/evidence/work packet
-> Engine request/process/validation/deposit candidate
-> VectorFL reflux/record
-> User decision or hold
```

This mapping does not claim that every step is fully automated or locked in code.

## 2. What Enters On The User Surface

User Surface receives or displays:

- raw request / goal
- scope and constraints
- material context
- team or role assignment relevance
- user decision or approval need

Observed assets:

- `app/ui/integrated_engine/folder_status.md`
- `app/ui/integrated_engine/CommandHeaderPanel.tsx`
- `app/ui/integrated_engine/useUserSurfaceState.ts`
- `docs/specs/integrated_engine_surface_object_contracts_v0.md`

Not yet engine-ingest material:

- raw goal text alone
- assignment relevance alone
- user-facing summary without evidence/guard

## 3. What Changes On The VectorFL Surface

VectorFL transforms the request by adding or making visible:

- object scope
- lens/task type
- governing locks or none/unspecified state
- evidence bundle and evidence readiness
- do / do-not guard
- expected return shape
- next route candidate
- manual/inferred/missing status

Observed assets:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_internal_search_evidence_bundle_gate_patch_note_v0.md`
- `docs/specs/integrated_engine_execution_packet_schema_v0.md`
- `runtime/contracts/integrated_engine_live_execution_packet_instance_v0.json`

Current caution:

- The evidence gate can make refs evidence-aware, but it does not yet perform full internal search.
- User-provided refs remain user-provided; the UI should not hide that behind "internal search complete."

## 4. What Becomes Engine-Ingest Material

Material becomes engine-ingest-ready when it has enough of the following:

- purpose
- scope boundary
- source/evidence bundle
- selected lens
- allowed and forbidden actions
- validation criteria or route status
- authority boundary
- expected return shape

Concrete current forms:

- execution packet: `runtime/contracts/integrated_engine_live_execution_packet_instance_v0.json`
- return record: `runtime/contracts/integrated_engine_live_return_record_instance_v0.json`
- process/validation/deposit candidates in runtime manifests via `app/runtime/vectorfl_integrated_engine_api.py`

Not engine-ingest-ready by itself:

- raw prompt
- loose file list
- readable board without current task guard
- UI card without route/authority state

## 5. What Remains Interpretive / Review / Display Material

These can support ingest but should not be confused with ingest-ready state:

- docs/reports audits and closeouts
- docs/reviews policies or retention maps
- `runtime/reports/*.html` rendered view outputs
- `app/work/observer_ingest_min/generated/readable_input_board_*`
- `operator_summary_*`
- UI panel state that has not been packetized

They matter because they can become evidence or support object, but they remain display/review material until bundled into a packet, request candidate, or return record.

## 6. What Is Currently Unclear Or Not Yet Locked

- Whether `app/runtime/ingest/` will become the actual runtime ingest implementation zone; it is currently empty.
- How `observer_ingest_min/generated` artifacts should be selected automatically for future evidence bundles.
- Whether `EngineIngestState` from `integrated_engine_surface_object_contracts_v0.md` will map directly to current manifests or needs a separate adapter.
- How source/preprocessed feed should move into current process-camera execution packets without manual reference selection.
- How trace/return records become memory without over-promoting deposit candidates.

## 7. Bridge Rule

Current bounded rule:

```text
User Surface starts purpose.
VectorFL turns purpose into evidence-aware packet material.
Engine consumes only bounded request/process/validation/deposit candidates or packet/return records.
Trace and return can become redeposit candidates, not canonical memory by default.
```

## 8. Phase 5 Validation

- Surface-to-ingest clarity check: passed. The document separates user entry, VectorFL transformation, engine-ingest-ready material, display/review material, and unclear zones.
- Unclear-zone preservation check: passed. Empty runtime ingest slice, generated artifact selection, and trace-to-memory pathway remain open.
- Implementation-overclaim check: passed. The note does not claim that the current repo has automatic input packetization or canonical ingestion.

