# Integrated Engine Lower Input Front Door Map v0

## 1. Verdict

PASS_WITH_NOTE

The lower input organ has multiple front doors. The strongest front door is structured document routing, but raw/direct observer ingest and source/reference material zones also exist.

No single canonical front door is declared here.

## 2. Front Door A - Structured Document Routing

Primary path:

```text
structured doc
-> scripts/process_structured_doc_with_routing.py
-> marker parse / label normalization
-> label packet / registries / provenance links
-> observer ingest unless reference_only
-> receipt / operation board / events / origin map
```

Observed evidence:

- `scripts/process_structured_doc_with_routing.py`
- `runtime/manifests/document_routing_alias_map_v1.json`
- `app/input_layer/labeler/labeler.py`
- `runtime/manifests/label_packets/`
- `runtime/manifests/structured_internal_docs_registry_v1.json`
- `runtime/manifests/ticket_registry_v1.json`
- `runtime/manifests/provenance_link_index_v1.json`
- `runtime/receipts/`
- `runtime/views/operation_board_latest.md`

What enters:

- Structured document with optional marker blocks such as `DOCROLE`, `RUNMODE`, `PRIORITY`.

What it does:

- Normalizes routing markers.
- Builds core intake labels.
- Writes label packet.
- Registers structured doc.
- Creates ticket for execution-coupled paths.
- Calls observer ingest unless `runmode=reference_only`.
- Writes origin map, receipt, operation board, events, commands.

Status:

- Active and strongest observed lower-organ front door.

## 3. Front Door B - Observer Ingest Direct Mode

Primary path:

```text
raw/source file
-> app/work/observer_ingest_min/run_observer_ingest_min.py --input
-> profile detection
-> split
-> source_manifest / split_units / processing_trace / readable board / operator summary
```

Observed evidence:

- `app/work/observer_ingest_min/run_observer_ingest_min.py`
- `app/work/observer_ingest_min/observer_ingest_min_spec.md`
- `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`

What enters:

- A single source file with optional label and profile.

What it does:

- Detects transcript/note/article/mixed profile.
- Chooses timestamp/heading/paragraph split.
- Writes generated observer ingest outputs.

Status:

- Active simple/raw front door.

## 4. Front Door C - Observer Ingest Registry Mode

Primary path:

```text
input registry json
-> run_observer_ingest_min.py --registry
-> per-row direct ingest
-> generated observer outputs
```

Observed evidence:

- `app/work/observer_ingest_min/contracts/input_registry_contract_v1.md`
- `app/work/observer_ingest_min/examples/sample_input_registry.json`
- `run_observer_ingest_min.py`

What enters:

- Registry rows with `input_id`, `source_path`, `label`, `input_kind`, `split_mode`, and note.

Status:

- Active batch/raw front door.

## 5. Front Door D - Source / Reference Material Zones

Observed zones:

- `source_assets/`
- `references/`
- `docs/reports/`
- `docs/specs/`
- `runtime/views/current_asset_map_v1.md`

What enters:

- Existing source documents, directives, external case inputs, baselines, reference engines, and generated/readable surfaces.

Current relation:

- These are material source zones. They become lower-organ input only when a routing or ingest path reads them.

Status:

- Active source zones, not automatic ingest front doors.

## 6. Re-entry From Runtime Surface Artifacts

Observed examples:

- `runtime/views/current_asset_map_v1.md` has operation receipt.
- `runtime/views/operation_board_latest.md` can be routed or inspected.
- `runtime/reports/*` and `runtime/views/multi_lens_document_reading/*` can become reference/source material for later reread.

Current reading:

- Runtime surface artifacts may re-enter as source/reference material, but they should not be mistaken for raw source.

Status:

- Possible re-entry front door, bounded and case-specific.

## 7. Where Direct Ingest Is Discouraged

The lower organ already carries several signals against direct flattening:

- `observer_ingest_min_spec.md` says it is easy ingest + visible split + readable trace, not canonical/mixed/corridor/axis analysis.
- `core_input_layer_labeler_stabilization_smoke_v1.md` shows `reference_only`, `ingest_only`, and `ingest_then_execute` are deliberately separated.
- Structured routing defaults missing markers to conservative `memo / ingest_only / normal`.

Meaning:

- Direct ingest is allowed for minimal visibility.
- But promotion, execution, line extraction, and canonical ingestion are not direct consequences of input entry.

## 8. Phase 2 Validation

- Repo-evidence check: passed. Front doors are grounded in routing script, observer ingest runner, contracts, source zones, and receipts/views.
- Multiple-entry preservation check: passed. Structured routing, direct observer ingest, registry observer ingest, and source/reference re-entry are separated.
- Fake canonical front door check: passed. Structured routing is strongest observed, not declared the only canonical door.

