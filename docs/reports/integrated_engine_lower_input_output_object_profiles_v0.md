# Integrated Engine Lower Input Output Object Profiles v0

## 1. Verdict

PASS_WITH_NOTE

This note profiles the major lower-input output objects as operational objects. It preserves readiness boundaries from the lower input output contract and readiness matrix.

## 2. Provenance / Origin Map

- What it is: A source-return handle with source document id, heading path, character span, preview, and derivation metadata.
- How it is formed: Built by `app/input_layer/source_locator/origin_map_minimum_v1.py`, often called by structured document routing.
- Where it usually appears: `runtime/manifests/origin_maps/`.
- Downstream use: Source grounding, source return, reread anchor, bundle provenance support.
- Cannot safely be used for: Semantic proof, full provenance graph, line extraction, packet body alone.
- Minimum supporting context: Source manifest or document id, reason for citation, downstream purpose.
- Common misread: Treating a span as proof that the cited meaning has already been validated.

## 3. Label Packet

- What it is: Structured intake label packet carrying doc id/ref, external labels, normalized core labels, generated timestamp, and packet kind.
- How it is formed: `app/input_layer/labeler/labeler.py` via structured document routing.
- Where it usually appears: `runtime/manifests/label_packets/`.
- Downstream use: Routing evidence, run mode clarification, source registry support.
- Cannot safely be used for: Meaning classification, execution completion, user approval, final governance.
- Minimum supporting context: Source doc, routing basis, receipt or registry entry.
- Common misread: Reading `execution_linkable` as execution already performed.

## 4. Source Manifest

- What it is: Source identity and ingest metadata: input id, source path, label, input kind, profile, split mode, line count, unit count, run id.
- How it is formed: `app/work/observer_ingest_min/run_observer_ingest_min.py`.
- Where it usually appears: `app/work/observer_ingest_min/generated/source_manifest_*`.
- Downstream use: Source identity, split run reference, evidence bundle root.
- Cannot safely be used for: Content interpretation or line extraction.
- Minimum supporting context: Split units, processing trace, purpose of downstream read.
- Common misread: Treating unit count or detected profile as understanding strength.

## 5. Split Unit

- What it is: A segmented unit with id, start/end refs, unit type, excerpt, char count, and source segment ids.
- How it is formed: Observer ingest splitting by timestamp, heading, paragraph, or detected profile.
- Where it usually appears: `app/work/observer_ingest_min/generated/split_units_*`.
- Downstream use: Reread source chunk, quote/evidence locator, later translation/line candidate source.
- Cannot safely be used for: Line artifact, axis, final segment grammar, standalone packet.
- Minimum supporting context: Source manifest, trace, origin/provenance, reread purpose.
- Common misread: Calling every split unit a line because it already has boundaries.

## 6. Processing Trace

- What it is: Minimal run process trace with run id, input id, profile, split mode, unit count, engine stage, and notes.
- How it is formed: Observer ingest runner.
- Where it usually appears: `app/work/observer_ingest_min/generated/processing_trace_*`.
- Downstream use: Audit support, debugging, readiness support for bundle trace completeness.
- Cannot safely be used for: Content evidence alone or complete reasoning trace.
- Minimum supporting context: Source manifest, split units, receipt or run id.
- Common misread: Treating `summary_written` or similar stage labels as deeper semantic validation.

## 7. Routing Basis

- What it is: Normalized `docrole`, `runmode`, `priority`, processing profile, execution linkability, and ticket relation.
- How it is formed: Structured document routing plus input-layer labeler.
- Where it usually appears: Label packet, receipt, structured doc registry, ticket registry.
- Downstream use: Authority/routing guard, task route evidence, execution-coupled vs reference-only distinction.
- Cannot safely be used for: User decision, action completion, canonical promotion.
- Minimum supporting context: Raw markers, normalized labels, receipt, source doc.
- Common misread: Treating routing status as operational completion.

## 8. Readable Input Board

- What it is: Human-readable input recognition and split board with unit excerpts and status.
- How it is formed: Observer ingest runner from source manifest and split units.
- Where it usually appears: `app/work/observer_ingest_min/generated/readable_input_board_*`.
- Downstream use: First-pass human inspection, evidence browsing, supervisor readability.
- Cannot safely be used for: Final report, canonical memory, validated extraction.
- Minimum supporting context: Source manifest, split units, trace.
- Common misread: Treating polished readability as mature interpretation.

## 9. Operation Receipt

- What it is: Per-document record of source, markers, routing, registry updates, ticket status, events, generated files, commands, GMD read, and final status.
- How it is formed: `scripts/process_structured_doc_with_routing.py`.
- Where it usually appears: `runtime/receipts/`.
- Downstream use: Run audit, provenance inspection, bridge check, trace bundle support.
- Cannot safely be used for: Semantic correctness or approval.
- Minimum supporting context: Linked generated files and source doc.
- Common misread: Treating "ran successfully" as "meaning is validated."

## 10. Operator Summary

- What it is: Short readable summary of input, split flow, status, and next extension point.
- How it is formed: Observer ingest runner.
- Where it usually appears: `app/work/observer_ingest_min/generated/operator_summary_*`.
- Downstream use: Supervisor quick read, bundle summary support.
- Cannot safely be used for: Full evidence, final interpretation, packet by itself.
- Minimum supporting context: Source manifest, split units, processing trace.
- Common misread: Letting summary replace source evidence.

## 11. GMD Native Read

- What it is: Derived readout preserving segmentation basis, ordering basis, role hints, relation clues, uncertainty, and provisional line-block-like material.
- How it is formed: Structured doc routing after observer ingest.
- Where it usually appears: `app/work/observer_ingest_min/generated/gmd_native_read_*`.
- Downstream use: Bridge material for later reread, translation, line-support, and internal recall.
- Cannot safely be used for: Axis promotion, final line set, canonical extraction.
- Minimum supporting context: Source manifest, split units, uncertainty notes, downstream purpose.
- Common misread: Treating "provisional line block" as validated line.

## 12. Multi-Lens Readout / Supervisor Surface

- What it is: Multi-lens observation payload and supervisor-readable surface derived from split units and registry context.
- How it is formed: Structured document routing through multi-lens payload/surface builders.
- Where it usually appears: `runtime/views/multi_lens_document_reading/`.
- Downstream use: Reread support, supervisor inspection, possible evidence bundle component.
- Cannot safely be used for: Approval, promotion, canonical synthesis.
- Minimum supporting context: Source manifest, split units, purpose, authority boundary.
- Common misread: Treating supervisor-facing layout as supervisor decision.

## 13. Phase 2 Validation

- Repo grounding check: passed. Profiles are tied to already mapped scripts, generated zones, contracts, and manifests.
- Downstream use vs misuse check: passed. Each object includes safe use and unsafe use.
- Packet inflation check: passed. No profile silently upgrades an object into packet-candidate status without bundling criteria.

