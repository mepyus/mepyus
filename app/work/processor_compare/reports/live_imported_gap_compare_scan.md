# Live Imported Gap Compare Scan 2026-03-21

## 1. current diagnosis
- current bridge state: bridge-common runtime with imported-gap semantics partially resolved
- live-legacy possibility 상태: active
- live-imported none 상태: dominant
- strongest sub blockers: anchor_vocabulary_translation_gap (3), document_span_too_broad_for_local_alignment (3), granularity_mismatch (3), imported_doc_signal_not_reconciled (3), imported_semantics_flattened (3), one_sided_anchor_presence (3), processing_projection_mismatch (3), scene_flow_alignment_insufficient (3)

## 2. exact changes
- touched file: [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
- added: pair-level mixed evaluator, `translation_gap_details`, `none_reason_kind`, `weak_support_summary`, `blocked_alignment_evidence`
- intentionally unchanged: canonical threshold, viewer, region semantics

## 3. verification
### canonical cases kept canonical
- doc_004 <-> doc_005: `canonical`
- doc_005 <-> doc_006: `canonical`
- test_live_space_sync_20260321 <-> test_canonical_ingest_20260321: `canonical`

### live-legacy possibility cases
- engine_phase1_imported_doc_probe_20260321 <-> test_live_space_sync_20260321: `possibility_candidate` / blockers: missing_canonical_anchor_alignment, processing_overlap_below_canonical, cross_path_translation_gap, processing_overlap_below_possibility
  basis: anchor=1, processing=2, echo=2
- engine_phase1_imported_doc_probe2_20260321 <-> test_live_space_sync_20260321: `possibility_candidate` / blockers: missing_canonical_anchor_alignment, processing_overlap_below_canonical, cross_path_translation_gap, processing_overlap_below_possibility
  basis: anchor=1, processing=2, echo=2

### live-imported none cases
- engine_phase1_observer_probe_20260321 <-> doc_004: `none` / none_reason=`anchor_vocabulary_translation_gap`
  translation_gap_details: anchor_vocabulary_translation_gap, one_sided_anchor_presence, processing_projection_mismatch, scene_flow_alignment_insufficient, weak_trace_not_compounding, imported_doc_signal_not_reconciled, document_span_too_broad_for_local_alignment, granularity_mismatch
  weak_support: anchor=0, processing=0, echo=0, observer=True
- engine_phase1_observer_probe_20260321 <-> doc_005: `none` / none_reason=`anchor_vocabulary_translation_gap`
  translation_gap_details: anchor_vocabulary_translation_gap, one_sided_anchor_presence, processing_projection_mismatch, scene_flow_alignment_insufficient, weak_trace_not_compounding, imported_doc_signal_not_reconciled, document_span_too_broad_for_local_alignment, granularity_mismatch
  weak_support: anchor=0, processing=0, echo=0, observer=True
- engine_phase1_observer_probe_20260321 <-> doc_006: `none` / none_reason=`anchor_vocabulary_translation_gap`
  translation_gap_details: anchor_vocabulary_translation_gap, one_sided_anchor_presence, processing_projection_mismatch, scene_flow_alignment_insufficient, weak_trace_not_compounding, imported_doc_signal_not_reconciled, document_span_too_broad_for_local_alignment, granularity_mismatch
  weak_support: anchor=0, processing=0, echo=0, observer=True

### none_reason / translation_gap_details distribution
- none_reason_distribution: {"anchor_vocabulary_translation_gap": 3}
- translation_gap_distribution: {"anchor_vocabulary_translation_gap": 3, "one_sided_anchor_presence": 3, "processing_projection_mismatch": 3, "scene_flow_alignment_insufficient": 3, "weak_trace_not_compounding": 3, "imported_doc_signal_not_reconciled": 3, "document_span_too_broad_for_local_alignment": 3, "granularity_mismatch": 3, "imported_semantics_flattened": 3}

## 4. current reading
- mixed-path possibility lane active, live-imported none no longer opaque
- live-imported none decomposed into translation blocker classes

## 5. next recommendation
- first: imported material flatten 이 실제 upstream 원인인지 확인
- second: live-imported에서 `anchor_vocabulary_translation_gap` 을 줄일 handle translation layer가 필요한지 검토
- not yet ready for viewer/region escalation
