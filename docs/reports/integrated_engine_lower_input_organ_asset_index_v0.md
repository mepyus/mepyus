# Integrated Engine Lower Input Organ Asset Index v0

## 1. Verdict

PASS_WITH_NOTE

The lower input organ is a distributed intake-digestion belt. It is not the upper User / VectorFL / Engine intake surface, and it is not line generation.

Current lower-organ center of gravity:

- `app/input_layer`
- `scripts/process_structured_doc_with_routing.py`
- `app/work/observer_ingest_min`
- `app/runtime/inputter.py`, `app/runtime/labeler.py`, `app/runtime/observer.py`
- `runtime/manifests`, `runtime/events`, `runtime/receipts`, `runtime/views`, `runtime/reports`

## 2. Raw / Structured / Reference Intake Assets

| path | current role | lower-organ position | state |
| --- | --- | --- | --- |
| `scripts/process_structured_doc_with_routing.py` | Structured document front door; parses routing markers, normalizes labels, writes label packet, registries, events, receipts, observer outputs, origin map, operation board | front-door / routing bridge / trace writer | active |
| `runtime/manifests/document_routing_alias_map_v1.json` | Alias map used to normalize `DOCROLE`, `RUNMODE`, `PRIORITY` markers | support / routing basis | active |
| `app/work/observer_ingest_min/run_observer_ingest_min.py` | Direct or registry input runner; loads files, detects profile, splits, writes manifest/split/trace/readable board/operator summary | front-door / transformation | active |
| `app/work/observer_ingest_min/contracts/input_registry_contract_v1.md` | Input registry contract for `input_id`, `source_path`, `label`, `input_kind`, `split_mode`, note | front-door contract | active |
| `app/work/observer_ingest_min/examples/sample_input_registry.json` | Example registry input | support | supporting |
| `source_assets/` | Source material zone with directives, baselines, external case inputs, declarations, handoffs | raw/reference source zone | active / broad |
| `references/` | External/reference material and imported reference engines | reference source zone | supporting / broad |

## 3. Segmentation / Label / Anchor / Source-Location Assets

| path | current role | lower-organ position | state |
| --- | --- | --- | --- |
| `app/input_layer/folder_status.md` | Defines `app/input_layer` as intake and fragmentization front layer | organ index | active |
| `app/input_layer/segmenter/` | Experimental split/fragmentization module slice | transformation | active / experimental |
| `app/input_layer/labeler/labeler.py` | Normalizes external labels, builds core intake labels and structured doc label packet | label/intake shaping | active |
| `app/input_layer/labeler/folder_status.md` | Notes that labeler is a core input-layer slot, not a universal labeling module | boundary support | active |
| `app/input_layer/anchorizer/` | Assigns anchor handles to input/fragments | anchor/provenance support | active |
| `app/input_layer/source_locator/locator.py` | Source path / line range / location linkage helper | provenance support | active |
| `app/input_layer/source_locator/origin_map_minimum_v1.py` | Builds minimal origin map with heading path, char span, source preview | origin/provenance formation | active |
| `docs/contracts/origin_map_minimum_fields_v1.md` | Origin map field contract | support contract | active support |

## 4. Routing Assets

| path | current role | lower-organ position | state |
| --- | --- | --- | --- |
| `runtime/manifests/structured_internal_docs_registry_v1.json` | Structured document registry updated by routing script | ledger / registry | active |
| `runtime/manifests/ticket_registry_v1.json` | Ticket registry for execution-coupled structured docs | ledger / routing action | active |
| `runtime/manifests/provenance_link_index_v1.json` | Links source docs to label packets, observer outputs, origin maps, readouts, receipts | provenance ledger | active |
| `runtime/manifests/label_packets/` | Structured doc intake label packets | label packet surface | active |
| `runtime/manifests/origin_maps/` | Minimal origin maps for source return | provenance surface | active |
| `runtime/events/engine_event_ledger.jsonl` | Append-only engine event ledger | trace / ledger | active |
| `runtime/events/folder_activity/` | Folder activity logs from routing and sync | trace / ledger | active |

## 5. Observer Ingest Assets

| path | current role | lower-organ position | state |
| --- | --- | --- | --- |
| `app/work/observer_ingest_min/observer_ingest_min_spec.md` | Defines easy ingest + visible split + readable trace | organ spec | active |
| `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md` | Defines source manifest, split units, processing trace, readable input board, operator summary | output contract | active |
| `app/work/observer_ingest_min/generated/source_manifest_*` | Source identity, profile, split mode, unit count, run id | generated source manifest | active surface |
| `app/work/observer_ingest_min/generated/split_units_*` | Unit ids, refs, excerpts, char counts | generated split residue | active / replayable |
| `app/work/observer_ingest_min/generated/processing_trace_*` | Minimal process trace | trace | active |
| `app/work/observer_ingest_min/generated/readable_input_board_*` | Human-readable split board | readable surface | active |
| `app/work/observer_ingest_min/generated/operator_summary_*` | Operator summary of input, split, flow, status, next extension | readable surface | active |
| `app/work/observer_ingest_min/generated/gmd_native_read_*` | Preserves segmentation basis, ordering basis, role hints, relation clues, uncertainty | bridge material for later reading/translation/line support | active / newer |

## 6. Runtime Intake / Observer / Report Bridge Assets

| path | current role | lower-organ position | state |
| --- | --- | --- | --- |
| `app/runtime/inputter.py` | Re-export of `app.core.runtime.inputter` for runtime input splitting into dust units | runtime intake bridge | active compatibility layer |
| `app/core/runtime/inputter.py` | Builds `DustInput` units from material/source text with source refs and sibling ids | transformation belt | active |
| `app/runtime/labeler.py` | Runtime labeler wrapper | runtime compatibility layer | active |
| `app/runtime/observer.py` | Re-export of `app.core.runtime.observer` | runtime observer bridge | active compatibility layer |
| `app/core/runtime/observer.py` | Reads runtime formation events, materials, cells, bridges, pressure profiles and builds observations | downstream observer belt | active |
| `app/runtime/connection_engine.py` | Re-export/compatibility for connection engine | downstream relation support | active |
| `app/core/runtime/connection_engine.py` | Builds relation profiles and edge reasons from anchors, scenes, flows, roles, direction, time | relation/connection support | active |
| `app/runtime/source_view/` | Builds/render source-side readable surfaces | downstream view bridge | active |
| `runtime/reports/` | Rendered source/measurement/space/terrain reports and smoke reports | report surface | active surface |

## 7. Manifest / Trace / Receipt / Report / View Artifacts

| path | current role | lower-organ position | state |
| --- | --- | --- | --- |
| `runtime/manifests/folder_status.md` | Inventory of manifest zones: label packets, origin maps, source views, registries, hints | artifact map | active |
| `runtime/events/folder_status.md` | Event ledger and folder activity zone summary | trace map | active |
| `runtime/receipts/folder_status.md` | Operation receipts summary; many structured doc receipts | receipt map | active |
| `runtime/views/folder_status.md` | Operation boards, multi-lens readouts, state views, shell views | view map | active / mixed |
| `runtime/views/operation_board_latest.md` | Latest structured routing operation board pointer | trace/view surface | active |
| `runtime/views/multi_lens_document_reading/` | Multi-lens readout and supervisor surfaces from structured routing | later reading support | active |
| `runtime/commands/structured_doc_routing_commands_v1.md` | Latest structured doc routing command pointer | command trace | active |

## 8. Phase 1 Validation

- Lower-organ focus check: passed. Upper 3-surface UI assets are not centered here.
- Upper intake exclusion check: passed. UI intake is mentioned only as contrast, not indexed as the main object.
- Active/residue/transitional check: passed. Generated outputs, split units, runtime wrappers, and empty/compatibility-like zones are labeled without over-cleaning.

