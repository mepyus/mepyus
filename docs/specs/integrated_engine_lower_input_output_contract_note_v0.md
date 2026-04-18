# Integrated Engine Lower Input Output Contract Note v0

## 1. Verdict

PASS_WITH_NOTE

This note describes what the lower input organ currently produces. It is not a final API schema and not a line-generation contract.

## 2. Output Objects

### 2.1 Provenance / Origin Map

- What it is: A source return handle with heading path, character span, source preview, derived time, and derived-from kind.
- Likely formed in: `app/input_layer/source_locator/origin_map_minimum_v1.py`, called by `scripts/process_structured_doc_with_routing.py`.
- Handed to next: `runtime/manifests/origin_maps/`, provenance index, later source return/reread.
- What it is not: It is not a full provenance graph and not a line.
- Confusion risk: A source span can look like semantic proof; it is only an origin handle.

### 2.2 Label Packet

- What it is: A structured doc intake label packet containing doc id/ref, external labels, core labels, generated time, and packet kind.
- Likely formed in: `app/input_layer/labeler/labeler.py`, written by structured doc routing.
- Handed to next: `runtime/manifests/label_packets/`, structured doc registry, receipt.
- What it is not: It is not full interpretation or final classification of meaning.
- Confusion risk: `execution_linkable=true` can be overread as actual execution completed.

### 2.3 Source Manifest

- What it is: Source identity, source path, label, input kind, detected profile, split mode, line count, unit count, run id.
- Likely formed in: `app/work/observer_ingest_min/run_observer_ingest_min.py`.
- Handed to next: observer generated zone, provenance links, receipts, future evidence bundles.
- What it is not: It is not processed meaning and not line extraction.
- Confusion risk: Manifest structure can be mistaken for content understanding.

### 2.4 Split Unit

- What it is: Unit id, start/end refs, unit type, excerpt, char count, source segment ids.
- Likely formed in: observer ingest runner after timestamp/heading/paragraph splitting.
- Handed to next: readable board, GMD native read, multi-lens readout, later reread/probe support.
- What it is not: It is not a line, not an axis, not a final segment grammar.
- Confusion risk: Because it is unit-shaped, it can be mistaken for a semantic line candidate.

### 2.5 Processing Trace

- What it is: Run id, input id, detected profile, split mode, unit counts, engine stage, notes.
- Likely formed in: observer ingest runner.
- Handed to next: receipts, generated zone, debugging and audit.
- What it is not: It is not a complete reasoning trace.
- Confusion risk: `engine_stage=summary_written` may sound like deeper engine processing than it is.

### 2.6 Routing Basis

- What it is: Normalized `docrole`, `runmode`, `priority`, core labels, processing profile, execution linkability, ticket relation.
- Likely formed in: structured doc routing script and input-layer labeler.
- Handed to next: doc registry, ticket registry, receipt, event ledger.
- What it is not: It is not user approval, not action completion, not promotion.
- Confusion risk: Routing basis can be mistaken for governance decision.

### 2.7 Readable Board / Operator Summary

- What it is: Human-readable summary of input recognition, split result, unit excerpts, flow note, processing status, and next extension point.
- Likely formed in: observer ingest runner.
- Handed to next: operator inspection, future evidence bundles, supervisor review.
- What it is not: It is not a final report, not canonical memory, and not a line/axis artifact.
- Confusion risk: Readability can make it feel more mature than the underlying split supports.

### 2.8 Operation Receipt

- What it is: Per-document record of source, raw markers, normalized routing, registration, ticket, events, generated files, commands, GMD native read, final status.
- Likely formed in: `scripts/process_structured_doc_with_routing.py`.
- Handed to next: `runtime/receipts`, supervisor audit, provenance inspection.
- What it is not: It is not proof of semantic correctness.
- Confusion risk: A receipt proves the lower organ ran, not that later interpretation is valid.

### 2.9 GMD Native Read

- What it is: Derived readout preserving segmentation basis, ordering basis, role hints, relation clues, uncertainty, and provisional line blocks.
- Likely formed in: structured doc routing after observer ingest.
- Handed to next: observer generated zone, later line translation/internal recall support.
- What it is not: It is not axis promotion or final line set.
- Confusion risk: The phrase "provisional line block" can invite premature line artifact reading.

### 2.10 Multi-Lens Readout / Supervisor Surface

- What it is: Multi-lens observation payload and supervisor-facing surface derived from split units and registry context.
- Likely formed in: structured doc routing using `build_multi_lens_observation_payload` and `build_multi_lens_supervisor_surface`.
- Handed to next: `runtime/views/multi_lens_document_reading/`.
- What it is not: It is not final extraction or canonical synthesis.
- Confusion risk: Supervisor surface can be overread as approval surface.

## 3. Contract Summary

The lower input organ emits:

```text
label / manifest / split / trace / origin / provenance / receipt / readable surface
```

It prepares material for later work. It does not itself complete line generation, translation, extraction, or promotion.

## 4. Phase 4 Validation

- Object distinction check: passed. Label packet, source manifest, split unit, trace, routing basis, origin map, receipt, readable board, and GMD/multi-lens surfaces are separated.
- Artifact grounding check: passed. Objects are tied to actual scripts, contracts, manifests, and generated zones.
- Line inflation check: passed. Lower input outputs are explicitly blocked from being read as line artifacts by default.

