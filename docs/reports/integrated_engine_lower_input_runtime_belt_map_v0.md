# Integrated Engine Lower Input Runtime Belt Map v0

## 1. Verdict

PASS_WITH_NOTE

The lower input runtime belt is a chain of compatibility wrappers, core runtime helpers, routing script effects, observer ingest outputs, and manifest/event/report surfaces. It is not one clean module.

## 2. Runtime Belt Summary

```text
source / structured doc
-> label normalization / intake label packet
-> observer ingest split and trace
-> origin/provenance handles
-> registries / ledgers / receipts
-> operation board / multi-lens readout / reports
-> possible later reread, translation, extraction, line support
```

## 3. Runtime Participants

| participant | appears to receive | transforms | hands forward | confusion risk |
| --- | --- | --- | --- | --- |
| `app/runtime/inputter.py` | Runtime import calls | Re-exports `app.core.runtime.inputter` | Compatibility access to inputter functions | Wrapper can be mistaken for implementation body |
| `app/core/runtime/inputter.py` | Material dict or source fields with raw payload | Splits material into `DustInput` units with source ref, source span, sibling ids | Dust units for runtime formation / later material handling | Dust input is not observer ingest split unit and not line |
| `app/runtime/labeler.py` | Runtime import calls | Re-export wrapper | Compatibility access to labeler | Wrapper/body distinction can be missed |
| `app/input_layer/labeler/labeler.py` | Raw routing markers and alias map | External labels -> normalized labels -> core intake labels -> label packet | `runtime/manifests/label_packets/*`, routing script | Label packet can be overread as full semantic classification |
| `app/runtime/observer.py` | Runtime observation calls | Re-exports `app.core.runtime.observer` | Compatibility access to observer | Wrapper can hide deeper event/material dependency |
| `app/core/runtime/observer.py` | Runtime root events, space cells, materials, bridges, pressure profiles | Builds scoped reactive space observation, session timeline, counts, process summary | Runtime reports/views and observer readouts | Downstream observer is not the same as lower ingest runner |
| `app/runtime/connection_engine.py` | Runtime relation calls | Re-exports `app.core.runtime.connection_engine` | Compatibility access to relation engine | Connection work is downstream support, not input formation itself |
| `app/core/runtime/connection_engine.py` | Anchors, scene, flow, role, direction, time | Builds relation profile, edge type, edge reasons | Connection/edge decisions for later runtime relations | Relation output can be mistaken for line/axis promotion |
| `app/runtime/source_view/` | Source/fragment view payloads | Builds and renders source readable surface | `runtime/reports/source_fragment_view.*` and source views | View is display layer, not origin |
| `scripts/process_structured_doc_with_routing.py` | Structured docs and routing markers | Orchestrates labels, registries, provenance, observer ingest, origin map, events, receipt, operation board | Lower-organ ledgers and surfaces | It is an organ bridge, not just a script |

## 4. Belt Role By Stage

### Stage 1. Label and route shaping

Assets:

- `app/input_layer/labeler/labeler.py`
- `runtime/manifests/document_routing_alias_map_v1.json`
- `scripts/process_structured_doc_with_routing.py`

Role:

- Normalize external marker language into core intake labels and processing profile.

### Stage 2. Split / trace / readable formation

Assets:

- `app/work/observer_ingest_min/run_observer_ingest_min.py`
- `app/work/observer_ingest_min/generated/*`

Role:

- Turn source material into source manifest, split units, processing trace, readable input board, and operator summary.

### Stage 3. Provenance and origin handles

Assets:

- `app/input_layer/source_locator/origin_map_minimum_v1.py`
- `runtime/manifests/origin_maps/`
- `runtime/manifests/provenance_link_index_v1.json`

Role:

- Preserve return handles between derived outputs and source document.

### Stage 4. Ledger / receipt / board trail

Assets:

- `runtime/events/engine_event_ledger.jsonl`
- `runtime/events/folder_activity/`
- `runtime/receipts/`
- `runtime/views/operation_board_latest.md`
- `runtime/commands/structured_doc_routing_commands_v1.md`

Role:

- Make lower-organ processing inspectable after the fact.

### Stage 5. Downstream observer / relation / view surfaces

Assets:

- `app/core/runtime/observer.py`
- `app/core/runtime/connection_engine.py`
- `app/runtime/source_view/`
- `runtime/reports/`
- `runtime/views/multi_lens_document_reading/`

Role:

- Prepare downstream observations, source views, and multi-lens reading surfaces that may support later reread/translation/extraction.

## 5. Phase 3 Validation

- Belt check: passed. The document maps handoff roles rather than listing files only.
- Lower-organ relevance check: passed. Each participant is tied to input shaping, split/trace/provenance, or downstream input residue.
- Speculation check: passed. Empty or wrapper-like areas are labeled as such.

