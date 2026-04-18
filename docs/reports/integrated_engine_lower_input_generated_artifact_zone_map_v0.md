# Integrated Engine Lower Input Generated Artifact Zone Map v0

## 1. Verdict

PASS_WITH_NOTE

The lower input organ leaves artifacts across several generated, trace, receipt, manifest, and view zones. This distributed residue is a major reason the lower input organ has felt hidden or messy.

This map does not recommend cleanup.

## 2. Generated / Residue / Trace Zones

| zone | lower-organ residue | kind | current handling | confusion risk |
| --- | --- | --- | --- | --- |
| `app/work/observer_ingest_min/generated/` | source manifests, split units, processing traces, readable input boards, operator summaries, GMD native reads | generated output / trace / readable surface | mixed active surface and replayable residue | Volume can make it look like canonical memory |
| `runtime/manifests/label_packets/` | structured doc intake label packets | generated manifest / label surface | active | Label packet can be overread as semantic interpretation |
| `runtime/manifests/origin_maps/` | minimal origin maps | provenance handle | active | Origin map can be overread as full provenance graph |
| `runtime/manifests/provenance_link_index_v1.json` | source-to-derived links | provenance ledger | active / append-like | Link existence can be mistaken for validation |
| `runtime/manifests/structured_internal_docs_registry_v1.json` | registered structured docs | registry ledger | active | Registration can be mistaken for ingestion completion |
| `runtime/manifests/ticket_registry_v1.json` | execution-coupled tickets | routing/action ledger | active | Ticket creation can be mistaken for execution result |
| `runtime/events/engine_event_ledger.jsonl` | file_created, doc_registered, routing_normalized, output_generated, receipt_written, board_updated events | append-only trace | active ledger | Event recorded does not mean semantic pass |
| `runtime/events/folder_activity/` | folder-level activity logs | append-only trace | active ledger | Folder activity can look like content status |
| `runtime/receipts/` | operation receipts per routed doc | receipt / audit surface | active | Receipt proves process trail, not correctness |
| `runtime/views/operation_board_latest.md` and run boards | latest/per-run operation board pointers | view / pointer surface | active | Board is pointer surface, not live dashboard |
| `runtime/views/multi_lens_document_reading/` | multi-lens readouts and supervisor surfaces | downstream readout / support surface | active | Supervisor surface can be overread as approval |
| `runtime/views/vectorfl_page_shell/inputs-intake.*` | rendered shell view of input/intake surface | display surface | active / mixed | UI shell can be mistaken for lower-organ source |
| `runtime/reports/` | source fragment, measurement, terrain, graph, smoke reports | report/view surface | active surface | Reports are downstream readable surfaces, not raw inputs |
| `runtime/commands/` | structured routing command traces | command trace | active support | Command pointer is not processing result |

## 3. Why It Feels Messy

The messiness is structural, not just visual:

- one routed document can produce label packet, observer outputs, GMD read, origin map, multi-lens readout, receipt, board, events, and commands
- some artifacts are ledgers, some are readable surfaces, some are replayable residue
- generated file names encode run ids and dates, making the organ visible only through artifact families
- upper integrated-engine surfaces can reference these artifacts later, but do not own their formation

## 4. Reuse / Read-Only / Append-Only / Mixed Status

| zone | recommended reading mode |
| --- | --- |
| `runtime/events/*` | append-only trace |
| `runtime/manifests/*registry*.json` | ledger / registry |
| `runtime/manifests/label_packets/*` | generated active support |
| `runtime/manifests/origin_maps/*` | provenance handle support |
| `app/work/observer_ingest_min/generated/source_manifest_*` | active source surface |
| `app/work/observer_ingest_min/generated/processing_trace_*` | trace surface |
| `app/work/observer_ingest_min/generated/readable_input_board_*` | readable input surface |
| `app/work/observer_ingest_min/generated/operator_summary_*` | operator-facing surface |
| `app/work/observer_ingest_min/generated/split_units_*` | reusable but replayable residue |
| `runtime/receipts/*` | receipt/audit surface |
| `runtime/views/*operation_board*` | pointer/readout surface |

## 5. Phase 7 Validation

- Messiness explanation check: passed. The map explains artifact spread by organ function, not by folder disorder only.
- Mixed-zone preservation check: passed. Generated, trace, ledger, view, and residue roles remain distinct.
- Cleanup-smuggling check: passed. No cleanup recommendation is made as fact.

