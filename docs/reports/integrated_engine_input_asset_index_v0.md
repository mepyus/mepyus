# Integrated Engine Input Asset Index v0

## 1. Verdict

PASS_WITH_NOTE

The current input side is not a single UI panel or a single folder. It is a layered, transitional input system made from:

- user/request intake material on the 3-surface UI side
- VectorFL interpretation and evidence-bundle formation
- engine-facing ingress and packet/return records
- older/deeper observer ingest assets that turn source material into manifest, split, trace, readable board, and summary surfaces

This index is role-led. It does not propose moving folders or declaring a new canonical layout.

## 2. Request Intake Assets

| asset | current role | surface/subsystem | why it matters | status |
| --- | --- | --- | --- | --- |
| `app/ui/integrated_engine/folder_status.md` | Current main integrated-engine UI area summary | User / VectorFL / Engine shell | Locks that User Surface is goal/scope/team/decision, VectorFL is CLI/reread/mediation/validation, Engine is processing return/validation/deposit candidate | active |
| `app/ui/integrated_engine/CommandHeaderPanel.tsx` | User-side goal/scope/material context header | User surface | Provides the start area where purpose and scope become visible before mediation | active |
| `app/ui/integrated_engine/useUserSurfaceState.ts` | User surface state holder | User surface | Carries current goal/team/assignment-style state used by the user surface | active |
| `docs/specs/integrated_engine_surface_object_contracts_v0.md` | Surface object contract candidate | 3-surface contract layer | Defines `UserGoalState`, `TeamFlowState`, `EngineIngestState`, `EnginePipelineState`, `VectorFlowState`, and `ValidationReturnPacket` as surface state kinds | supporting |
| `docs/reports/integrated_engine_body_packet_memory_lock_v0.md` | Body / packet / memory lock | Operating rule layer | Locks the process from instruction intake through internal search, evidence bundle, mediation, engine processing, reflux, and record/sedimentation | active |

## 3. Interpretation / Translation Assets

| asset | current role | surface/subsystem | why it matters | status |
| --- | --- | --- | --- | --- |
| `app/ui/integrated_engine/CliHostControlPanel.tsx` | VectorFL-side CLI host/control and packet formation panel | VectorFL surface | Hosts current work packet formation, evidence bundle gate, CLI turn, latest return, route marks | active |
| `docs/reports/integrated_engine_internal_search_evidence_bundle_gate_patch_note_v0.md` | Evidence bundle gate patch note | VectorFL mediation layer | Shows that current packet formation should be evidence-aware before Send Codex Turn | active |
| `docs/reports/integrated_engine_surface_information_exposure_reread_note_v0.md` | Surface exposure reread note | 3-surface interpretation layer | Locks that surfaces share identity but not full information density | active |
| `docs/reports/integrated_engine_user_instruction_interpretation_protocol_v0.md` | User instruction interpretation protocol | VectorFL interpretation protocol | Provides the sequence for 3면 lock, object scope, lens, camera, guard, expected return, projection, and record/redeposit | active |
| `docs/specs/integrated_engine_execution_packet_schema_v0.md` | Worker/CLI-consumable packet schema | Process camera / VectorFL-to-worker bridge | Defines compact packet fields so a worker does not need the full conversation | active |
| `runtime/contracts/integrated_engine_live_execution_packet_instance_v0.json` | Live execution packet instance | Process camera pilot artifact | Demonstrates a concrete request packet with purpose, scope, lenses, evidence, allowed/forbidden actions, and authority boundary | active example |

## 4. Engine Ingress Assets

| asset | current role | surface/subsystem | why it matters | status |
| --- | --- | --- | --- | --- |
| `app/runtime/vectorfl_integrated_engine_api.py` | Integrated engine runtime API and manifest bridge | Engine / runtime bridge | Reads and writes latest work packet, assignment, internal read, synthesis, supervisor, worker, CLI, and return manifests | active |
| `runtime/manifests/` | Runtime manifest root | Runtime ledger / active surface | Holds latest operating and generated state surfaces used by viewer/UI/runtime flows | active / mixed |
| `runtime/contracts/` | Runtime contract and instance area | Process camera / packet-return contract layer | Holds execution packet and return record templates/instances | active |
| `docs/specs/integrated_engine_return_record_schema_v0.md` | Return record schema | Engine return/redeposit bridge | Defines what comes back after a packet is handled and what can become redeposit material | active |
| `runtime/contracts/integrated_engine_live_return_record_instance_v0.json` | Live return record instance | Process camera pilot artifact | Shows structured attempted actions, evidence, gates, risks, decision, redeposit payload, and boundary confirmation | active example |

## 5. Reference / Preprocessed / Ingest-Queue-Related Assets

| asset | current role | surface/subsystem | why it matters | status |
| --- | --- | --- | --- | --- |
| `app/input_layer/folder_status.md` | Input layer root index | Deeper input front | Identifies input_layer as the intake and fragmentization front layer | active |
| `app/input_layer/segmenter/` | Split / fragmentization module slice | Input layer | Turns input into fragment candidates; currently experimental, not full production truth | active / experimental |
| `app/input_layer/labeler/` | Core input-layer labeler slot | Input normalization | Normalizes external routing labels and constructs structured doc intake label packets | active / contract-first |
| `app/input_layer/anchorizer/` | Anchor handle assignment module | Input anchoring | Assigns anchors so fragments have stable handles and location-like meaning | active |
| `app/input_layer/source_locator/` | Source locator / origin-map / source-return handle module | Provenance ingress | Preserves source path, line/location linkage, and lightweight origin map handles | active |
| `app/work/observer_ingest_min/observer_ingest_min_spec.md` | Minimal observer ingest spec | Older/deeper ingest flow | Defines easy ingest, visible split, readable trace, and md summary outputs | active support |
| `app/work/observer_ingest_min/run_observer_ingest_min.py` | Minimal observer ingest runner | Ingest execution | Loads direct or registry input, detects profile, splits, writes source manifest, split units, processing trace, readable board, operator summary | active support |
| `app/work/observer_ingest_min/contracts/input_registry_contract_v1.md` | Input registry contract | Raw/registry input | Defines `input_id`, `source_path`, `label`, `input_kind`, `split_mode`, and note fields | active support |
| `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md` | Observer output contract | Ingest output | Defines source manifest, split units, processing trace, readable input board, and operator summary output shapes | active support |
| `app/work/observer_ingest_min/generated/` | Generated observer ingest artifacts | Active input reading surface / replayable residue | Contains `source_manifest_*`, `split_units_*`, `processing_trace_*`, `readable_input_board_*`, `operator_summary_*` | active / large / transitional |

## 6. Observer / Report / View Assets Downstream-Adjacent To Input

| asset | current role | surface/subsystem | why it matters | status |
| --- | --- | --- | --- | --- |
| `app/runtime/folder_status.md` | Runtime execution and projection layer index | Runtime / engine layer | Frames `app/runtime` as active execution and projection for input, reporting, views, measurement, and operator-facing state | active |
| `app/runtime/inputter.py` | Runtime intake bridge candidate | Runtime bridge | Listed as an input-layer-to-runtime handling contact point in `app/runtime/folder_status.md` | active / mixed |
| `app/runtime/source_view/` | Source-side view builder/render layer | Runtime source surface | Builds readable source-side surfaces connected to `runtime/reports` and source view outputs | active |
| `app/runtime/ingest/` | Runtime ingest slice placeholder | Runtime ingest slot | Empty but structurally marks a later ingest slice between input_layer and runtime execution | transitional / placeholder |
| `runtime/reports/` | Rendered reports and view outputs | Runtime report surface | Contains source fragment, measurement, region, terrain, graph, and smoke reports; `folder_status.md` says it is a reading surface, not a ledger | active surface |
| `docs/reviews/generated_retention_map_v1.md` | Generated/manifest/log retention map | Asset retention policy | Classifies runtime manifests, logs, and observer ingest outputs as ledger, active surface, or replayable residue | active support |

## 7. Phase 1 Validation

- Role-led index check: passed. Assets are grouped by request intake, interpretation, engine ingress, preprocessed/reference ingress, and downstream-adjacent views rather than raw tree order.
- Transitional labeling check: passed. `app/runtime/ingest` is marked placeholder, `observer_ingest_min/generated` is active but large/transitional, and `input_layer/segmenter` remains experimental.
- Restructuring claim check: passed. This index does not recommend folder moves or canonical placement changes.

