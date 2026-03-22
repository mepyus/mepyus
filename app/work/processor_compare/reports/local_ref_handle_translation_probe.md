# local_ref-scoped bounded handle translation probe

## 1. current diagnosis
- translation 전 상태: imported contract recovered, but live-imported remained none with anchor_vocabulary_translation_gap dominance
- translation 후 상태: local_ref-scoped translated handles are attached additively and mixed evaluator reads them only for live-imported possibility assist
- 가장 강한 잔여 blocker: processing_projection_mismatch / broad imported alignment still dominate on doc_004 and doc_005, while doc_006 can narrow to local_ref-scoped rag matches

## 2. exact changes
- 변경 파일: `app/core/runtime/local_ref_handle_translation.py`
- 변경 파일: `app/core/runtime/imported_material_contract.py`
- 변경 파일: `app/core/runtime/imported_material_probe.py`
- 변경 파일: `app/core/runtime/live_input_space.py`
- 적용: added local_ref-scoped translation helper backed by alias dictionary and strict source_local_ref provenance
- 적용: attached translated_handles additively to imported material metadata without overwriting original transformable_handles
- 적용: extended imported probe with translation gain and broadcast leak metrics
- 적용: let mixed evaluator read translated handles only on live-imported pairs as possibility assist; canonical logic unchanged
- 유지: viewer routes and rendering
- 유지: region semantics
- 유지: canonical thresholds
- 유지: document-scoped alias broadcast

## 3. verification
- canonical 사례 유지:
  - doc_004 <-> doc_005: `canonical` / `imported-imported`
  - doc_005 <-> doc_006: `canonical` / `imported-imported`
  - test_live_space_sync_20260321 <-> test_canonical_ingest_20260321: `canonical` / `legacy-legacy`
- imported docs local translation profile:
  - `processor_compare/doc_004.txt`: translation_applied_local_ref_count=6, translation_handle_gain_ratio=0.4, translation_broadcast_leak=False, readiness=high
  - `processor_compare/doc_005.txt`: translation_applied_local_ref_count=27, translation_handle_gain_ratio=0.3699, translation_broadcast_leak=False, readiness=partial
  - `processor_compare/doc_006.txt`: translation_applied_local_ref_count=26, translation_handle_gain_ratio=0.3562, translation_broadcast_leak=False, readiness=partial
- live-imported none 군 재테스트:
  - engine_phase1_observer_probe_20260321 <-> doc_004: `none` / none_reason=`anchor_vocabulary_translation_gap` / translation_available=False / matched_local_ref_count=0
  - engine_phase1_observer_probe_20260321 <-> doc_005: `none` / none_reason=`anchor_vocabulary_translation_gap` / translation_available=False / matched_local_ref_count=0
  - engine_phase1_observer_probe_20260321 <-> doc_006: `possibility_candidate` / none_reason=`` / translation_available=True / matched_local_ref_count=26
- live-legacy possibility 유지:
  - engine_phase1_imported_doc_probe_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`
  - engine_phase1_imported_doc_probe2_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`
- translation_assisted_alignment_count: 1
- translation_assisted_possibility_count: 1
- broadcast leak: False

## 4. current reading
- translation helps doc_006 at local_ref scope, but broad imported alignment and processing flatness still block doc_004/doc_005; canonical lane remains preserved

## 5. next recommendation
- 다음 병목: treat processing flatness as next blocker before widening translation coverage
- translation 범위: if translation continues, keep it local_ref-scoped only
- possibility review: review doc_006 translation-assisted possibility basis before considering any broader promotion rule
