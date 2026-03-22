# Imported Local Alignment Readiness 2026-03-21

## 1. current diagnosis
- imported many-material spread 상태: wide_spread_with_partial_local_discrimination
- doc_004: local_ref 분화=`15/15` / readiness=`high` / blockers=none
- doc_005: local_ref 분화=`73/73` / readiness=`partial` / blockers=processing_profile_too_flat
- doc_006: local_ref 분화=`73/73` / readiness=`partial` / blockers=processing_profile_too_flat
- live-imported none 의 가장 강한 locality blocker: source_local_ref는 material마다 있지만 imported materials가 여전히 넓은 표면처럼 반응함

## 2. exact changes
- touched file: [imported_material_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/imported_material_probe.py)
- added metrics: `unique_source_local_ref_count`, `anchor_signature_unique_ratio`, `processing_signature_unique_ratio`, `handle_signature_unique_ratio`, `local_alignment_readiness`
- intentionally unchanged: viewer, bridge thresholds, translation layer

## 3. verification
### imported docs local spread
- doc_004: materials=15 unique_local_refs=15 materials_per_local_ref_max=1
  anchor_sig_ratio=1.0 processing_sig_ratio=0.3333 handle_sig_ratio=1.0
  scene_unique=3 flow_unique=2 role_unique=3
- doc_005: materials=73 unique_local_refs=73 materials_per_local_ref_max=1
  anchor_sig_ratio=0.9452 processing_sig_ratio=0.1644 handle_sig_ratio=1.0
  scene_unique=4 flow_unique=3 role_unique=4
- doc_006: materials=73 unique_local_refs=73 materials_per_local_ref_max=1
  anchor_sig_ratio=0.8904 processing_sig_ratio=0.1644 handle_sig_ratio=1.0
  scene_unique=4 flow_unique=2 role_unique=4

### live-imported none
- engine_phase1_observer_probe_20260321 <-> doc_004: `none` / none_reason=`anchor_vocabulary_translation_gap`
  locality blockers: readiness=high / none
  translation_gap_details: anchor_vocabulary_translation_gap, one_sided_anchor_presence, processing_projection_mismatch, scene_flow_alignment_insufficient, weak_trace_not_compounding, imported_doc_signal_not_reconciled, document_span_too_broad_for_local_alignment, granularity_mismatch
- engine_phase1_observer_probe_20260321 <-> doc_005: `none` / none_reason=`anchor_vocabulary_translation_gap`
  locality blockers: readiness=partial / processing_profile_too_flat
  translation_gap_details: anchor_vocabulary_translation_gap, one_sided_anchor_presence, processing_projection_mismatch, scene_flow_alignment_insufficient, weak_trace_not_compounding, imported_doc_signal_not_reconciled, document_span_too_broad_for_local_alignment, granularity_mismatch
- engine_phase1_observer_probe_20260321 <-> doc_006: `none` / none_reason=`anchor_vocabulary_translation_gap`
  locality blockers: readiness=partial / processing_profile_too_flat
  translation_gap_details: anchor_vocabulary_translation_gap, one_sided_anchor_presence, processing_projection_mismatch, scene_flow_alignment_insufficient, weak_trace_not_compounding, imported_doc_signal_not_reconciled, document_span_too_broad_for_local_alignment, granularity_mismatch

### live-legacy possibility kept
- engine_phase1_imported_doc_probe_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`
- engine_phase1_imported_doc_probe2_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`

## 4. current reading
- contract recovered but local discrimination still weak-to-partial
- source_local_ref is present and per-material unique
- but anchor/processing signatures are not diverse enough to make imported docs fully local-alignable yet
- translation layer should be local_ref-scoped, not document-scoped

## 5. next recommendation
- local ref 분화를 한 턴 더 밀 수도 있지만, 지금도 translation unit은 이미 local_ref 단위로 제한해야 한다는 근거는 충분함
- 따라서 다음 bounded handle translation layer는 문서 전체가 아니라 local_ref 단위로 시험하는 것이 맞다
