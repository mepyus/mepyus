# Integrated Engine Structured Doc Routing To Observer Ingest Bridge v0

## 1. Verdict

PASS_WITH_NOTE

`scripts/process_structured_doc_with_routing.py` is the clearest concrete bridge between structured document routing and observer ingest.

It is not merely code glue. It acts like an organ bridge: marker normalization, label formation, registry update, observer ingest call, provenance link creation, origin map, receipt, operation board, commands, and events are tied together in one route.

## 2. What The Routing Script Appears To Do

Observed behavior:

1. Resolve the document path.
2. Parse marker blocks in the first lines: `DOCROLE`, `RUNMODE`, `PRIORITY`.
3. Load `runtime/manifests/document_routing_alias_map_v1.json`.
4. Normalize external labels.
5. Build core intake labels.
6. Build and write label packet.
7. Update structured doc registry.
8. Append provenance links.
9. Append engine/folder events.
10. Create ticket if `runmode` is `ingest_then_execute` or `execute_only`.
11. Call observer ingest unless `runmode` is `reference_only`.
12. Write GMD native read from observer outputs.
13. Write multi-lens readout and supervisor surface.
14. Write minimal origin map seed.
15. Write commands doc, receipt, operation board.
16. Sync folder status surfaces.

## 3. What It Creates Or Records

| object | likely path |
| --- | --- |
| label packet | `runtime/manifests/label_packets/<doc_id>_label_packet.json` |
| structured doc registry entry | `runtime/manifests/structured_internal_docs_registry_v1.json` |
| ticket entry | `runtime/manifests/ticket_registry_v1.json` |
| provenance links | `runtime/manifests/provenance_link_index_v1.json` |
| engine events | `runtime/events/engine_event_ledger.jsonl` |
| folder activity events | `runtime/events/folder_activity/*.jsonl` |
| observer ingest outputs | `app/work/observer_ingest_min/generated/*_<observer_run_id>.*` |
| GMD native read | `app/work/observer_ingest_min/generated/gmd_native_read_<observer_run_id>.json` |
| multi-lens readouts | `runtime/views/multi_lens_document_reading/*` |
| origin map | `runtime/manifests/origin_maps/<doc_id>_receipt_seed_origin_map.json` |
| command trace | `runtime/commands/structured_doc_routing_commands_*.md` |
| receipt | `runtime/receipts/<doc_id>_operation_receipt.md` |
| operation board | `runtime/views/operation_board_*.md`, `runtime/views/operation_board_latest.md` |

## 4. How It Connects To Origin Maps / Labels / Tickets / Manifests / Receipts

### Labels

`app/input_layer/labeler/labeler.py` normalizes external markers and builds core labels. The routing script writes those labels as label packets.

### Tickets

Only execution-coupled run modes create tickets. `ingest_only` and `reference_only` remain non-execution paths.

### Manifests

The script updates structured doc registry, ticket registry, provenance index, label packet store, origin map store, and sometimes multi-lens view surfaces.

### Receipts

The receipt records source, raw markers, normalized routing, registration, ticket status, events, generated files, commands, GMD native read, and final processing status.

### Origin Maps

The origin map is a minimal source-return handle, not a full provenance graph.

## 5. How Observer Ingest Outputs Appear In The Chain

If normalized `runmode` is not `reference_only`, routing calls:

```text
app/work/observer_ingest_min/run_observer_ingest_min.py --input <doc> --label <stem> --profile auto
```

That produces:

- source manifest
- split units
- processing trace
- readable input board
- operator summary

The routing script then:

- adds those paths to generated files
- records provenance links from source doc to outputs
- appends an output-generated event
- uses source manifest/split units/processing trace to build GMD native read
- uses split units for multi-lens readout and supervisor surface

## 6. What Remains Unclear

- Whether every structured document should pass through this script, or whether some are intentionally observer-ingest-only.
- Whether the multi-lens readout is always expected or only a current bridge artifact.
- How generated observer outputs are later selected into current VectorFL evidence bundles.
- Whether `runtime/manifests/provenance_link_index_v1.json` is sufficient as the long-term provenance join surface.
- How concurrency/race concerns from labeler smoke tests affect high-volume routing.

## 7. Phase 6 Validation

- Bridge clarity check: passed. The script's organ-bridge role is now visible.
- Observer relation grounding check: passed. The exact observer ingest call and generated output set are grounded in code.
- Unclear-parts honesty check: passed. Routing scope, multi-lens expectation, evidence-bundle selection, provenance sufficiency, and concurrency concerns remain open.

