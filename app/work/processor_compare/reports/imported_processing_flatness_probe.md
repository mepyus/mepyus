# imported processing flatness probe

## 1. current diagnosis
- imported processing flatness 상태: doc_005/doc_006 remain flat at processing signature level while doc_004 is smaller and more discriminative
- 가장 강한 upstream flatness 지점: imported docs are normalized to source_type=text and then labeled through label_dust_inputs; many units default to scene=review, flow=compare, D/I/S=0.5 before materialization
- doc_004: high readiness; 15 units only; pre/post processing_signature_unique_ratio stays 0.3333 and scene_flow_role_uniqueness_ratio is 0.4667
- doc_005: partial readiness; 73 units; pre/post processing_signature_unique_ratio stays 0.1644 with processing_profile_flatness_score 0.7623
- doc_006: partial readiness; 73 units; pre/post processing_signature_unique_ratio stays 0.1644 with processing_profile_flatness_score 0.8103

## 2. exact changes
- 변경 파일: `app/core/runtime/imported_material_probe.py`
- 추가 probe: `pre_processing_signature_unique_ratio`
- 추가 probe: `pre_processing_signature_entropy`
- 추가 probe: `pre_scene_flow_uniqueness_ratio`
- 추가 probe: `processing_value_variance`
- 추가 probe: `processing_signature_entropy`
- 추가 probe: `local_ref_processing_uniqueness`
- 추가 probe: `processing_profile_flatness_score`
- 추가 probe: `scene_flow_role_uniqueness_ratio`
- 경로 추적 확인 파일: `scripts/import_processor_compare_docs.py`
- 경로 추적 확인 파일: `app/core/runtime/inputter.py`
- 경로 추적 확인 파일: `app/core/runtime/live_input.py`
- 경로 추적 확인 파일: `app/core/runtime/labeler.py`
- 유지: viewer routes
- 유지: translation scope
- 유지: canonical/possibility evaluator thresholds

## 3. verification
- canonical 사례 유지:
  - doc_004 <-> doc_005: `canonical` / `imported-imported`
  - doc_005 <-> doc_006: `canonical` / `imported-imported`
  - test_live_space_sync_20260321 <-> test_canonical_ingest_20260321: `canonical` / `legacy-legacy`
- doc별 processing profile 비교:
  - `doc_004.txt`: pre_sig_ratio=0.3333, post_sig_ratio=0.3333, pre_entropy=0.8313, post_entropy=0.8313, flatness_score=0.7263
  - `doc_005.txt`: pre_sig_ratio=0.1644, post_sig_ratio=0.1644, pre_entropy=0.6056, post_entropy=0.6056, flatness_score=0.7623
  - `doc_006.txt`: pre_sig_ratio=0.1644, post_sig_ratio=0.1644, pre_entropy=0.5569, post_entropy=0.5569, flatness_score=0.8103
- mixed pair 결과 재설명:
  - `doc_004`: mode=`none`, none_reason=`anchor_vocabulary_translation_gap`, translation_available=False, matched_handles=[]
  - `doc_005`: mode=`none`, none_reason=`anchor_vocabulary_translation_gap`, translation_available=False, matched_handles=[]
  - `doc_006`: mode=`possibility_candidate`, none_reason=``, translation_available=True, matched_handles=['rag']

## 4. current reading
- processing flatness is confirmed as the next dominant blocker, but doc_006 reaches possibility because local_ref translation hits rag; doc_005 remains none because flatness combines with no translation-assisted handle convergence

## 5. next recommendation
- 다음 병목: target processing projection refinement before widening translation
- refinement 방향: prefer local_ref-level processing derivation/projection refinement over document-wide adjustment
- 병행 축: keep vocabulary gap as secondary track, not primary next move
