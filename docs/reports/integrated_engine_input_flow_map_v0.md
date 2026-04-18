# Integrated Engine Input Flow Map v0

## 1. Verdict

PASS_WITH_NOTE

There are at least two overlapping input flows in the current repo:

1. The integrated-engine surface flow: user purpose enters the 3-surface body, VectorFL forms evidence-aware work packets, Engine receives processing/validation/deposit candidates, and returns come back as records or readable surface material.
2. The older/deeper observer ingest flow: raw or registry input is loaded, profiled, split, traced, and rendered into manifest/split/readable-board/operator-summary artifacts.

Both flows matter. They should not be collapsed into one fake sequence.

## 2. Staged Flow A: Integrated-Engine Surface Flow

### Stage A1. User-side request entry

Observed assets:

- `app/ui/integrated_engine/folder_status.md`
- `app/ui/integrated_engine/CommandHeaderPanel.tsx`
- `app/ui/integrated_engine/useUserSurfaceState.ts`
- `docs/specs/integrated_engine_surface_object_contracts_v0.md`

Current reading:

- User Surface starts with goal, scope, material context, team/role assignment, and decision relevance.
- It should not expose the full internal evidence atlas by default.
- It hands purpose and constraint forward, not final engine-ingest material by itself.

### Stage A2. VectorFL-side interpretation / translation / intermediate formation

Observed assets:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_internal_search_evidence_bundle_gate_patch_note_v0.md`
- `docs/reports/integrated_engine_body_packet_memory_lock_v0.md`
- `docs/specs/integrated_engine_execution_packet_schema_v0.md`
- `runtime/contracts/integrated_engine_live_execution_packet_instance_v0.json`

Current reading:

- VectorFL reads user purpose through lens/scope/guard/evidence.
- It forms a current work packet and can prepare a worker/CLI-consumable execution packet.
- The evidence bundle gate currently makes refs visible as evidence-aware bundle items, but it is not a full automatic repository search engine.

### Stage A3. Engine-side ingest / process / validate / trace-memory / return relation

Observed assets:

- `app/runtime/vectorfl_integrated_engine_api.py`
- `docs/specs/integrated_engine_return_record_schema_v0.md`
- `runtime/contracts/integrated_engine_live_return_record_instance_v0.json`
- `docs/specs/integrated_engine_surface_object_contracts_v0.md`

Current reading:

- Engine receives candidate material as request, validation target, deposit candidate, return record, or pipeline/case-related state.
- The current concrete packet/return pilot proves that an execution packet can produce a return record strong enough for redeposit evaluation.
- This is not automatic ingestion or canonical memory.

### Stage A4. Reflux and record/sedimentation

Observed assets:

- `runtime/contracts/integrated_engine_live_return_record_instance_v0.json`
- `docs/specs/integrated_engine_return_record_schema_v0.md`
- `docs/reports/integrated_engine_live_packetization_pilot_closeout_note_v0.md`

Current reading:

- Return records preserve attempted actions, evidence, gates, risks, decisions, non-actions, redeposit payload, and next valid use.
- Sedimentation is currently candidate/record material, not automatic canonical ingestion.

## 3. Staged Flow B: Observer Ingest / Preprocessed Input Flow

### Stage B1. Raw or registry input enters

Observed assets:

- `app/work/observer_ingest_min/contracts/input_registry_contract_v1.md`
- `app/work/observer_ingest_min/examples/sample_input_registry.json`
- `app/work/observer_ingest_min/run_observer_ingest_min.py`

Current reading:

- Direct mode accepts `--input`, optional `--label`, and profile.
- Registry mode accepts rows with `input_id`, `source_path`, `label`, `input_kind`, `split_mode`, and note.

### Stage B2. Profile detection and split selection

Observed assets:

- `app/work/observer_ingest_min/run_observer_ingest_min.py`
- `app/input_layer/segmenter/`

Current reading:

- The minimal observer ingest runner detects transcript/note/article/mixed shape and selects timestamp, heading, or paragraph split.
- The dedicated `app/input_layer/segmenter` exists as the broader split/fragmentization module slice, but its files are experimental.

### Stage B3. Output artifacts are written

Observed assets:

- `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`
- `app/work/observer_ingest_min/generated/`

Current output contract:

- `source_manifest_<run_id>.json`
- `split_units_<run_id>.json`
- `processing_trace_<run_id>.json`
- `readable_input_board_<run_id>.md`
- `operator_summary_<run_id>.md`

### Stage B4. Output becomes readable surface / support material

Observed assets:

- `docs/reviews/generated_retention_map_v1.md`
- `runtime/reports/`
- `app/runtime/source_view/`

Current reading:

- `source_manifest_*`, `processing_trace_*`, `readable_input_board_*`, and `operator_summary_*` are active surfaces for reading input again.
- `split_units_*` are useful but more replayable residue than permanent decision ledger.
- `runtime/reports` is a rendered reading surface, not the origin.

## 4. Reference -> Preprocessed -> Ingest Queue Relation

The current repo shows a partial relation, not one locked queue:

```text
a source/reference file or registry row
-> observer_ingest_min direct/registry run
-> source_manifest / split_units / processing_trace
-> readable_input_board / operator_summary
-> possible later evidence bundle, packet, or report reference
```

Separate but related:

```text
user purpose / current task
-> VectorFL evidence bundle gate
-> execution packet
-> worker-style processing or CLI run
-> return record / redeposit candidate
```

The first path prepares source material. The second path prepares operating work. A future engine packetization path can join them, but this package does not claim that join is fully implemented.

## 5. Observer / Report / View Outputs Relative To Input Chain

- `app/runtime/source_view/` builds source-readable surfaces after input exists.
- `runtime/reports/source_fragment_view.*` and related HTML/JSON views are downstream reading surfaces.
- `runtime/manifests/label_packets/` and related manifest zones are active current surfaces when runtime/viewer code depends on them.
- `docs/reviews/generated_retention_map_v1.md` warns that ledgers, active surfaces, and replayable residue must be treated differently.

## 6. Overlap / Ambiguity / Transition Note

The input side feels messy because the repo holds multiple historical layers at once:

- Current 3-surface UI operating layer.
- Process-camera packet/return layer.
- Older observer ingest minimum runner and generated assets.
- Input-layer code slices for segmenting, labeling, anchoring, locating.
- Runtime view/report layers that display derived source and measurement surfaces.

This is not automatically failure. It is a transitional overlap. The risk is pretending either that the old ingest flow is obsolete or that the new 3-surface flow already replaced all ingest mechanics.

## 7. Phase 3 Validation

- Observed-flow check: passed. The map follows actual files: UI shell, packet schema/instances, runtime API, observer ingest runner/contracts, generated outputs, runtime view surfaces.
- Transitional ambiguity check: passed. The integrated-engine surface flow and observer ingest flow are deliberately kept separate.
- Inspectability check: passed. The stages now show where a request, source material, work packet, return record, and readable input board sit relative to each other.

