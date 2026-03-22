# imported processing refinement

## 1. current diagnosis
- 가장 강한 잔여 병목: translation-assisted handle convergence is still the decisive difference between doc_005 and doc_006, even after processing flatness is reduced
- doc_004: processing differentiation improved strongly because small imported set now reacts to local definition/process cues instead of collapsing to review/run or review/compare
- doc_005: processing uniqueness improved substantially, but mixed pair remains none because translation-assisted convergence is still absent
- doc_006: processing uniqueness improved and possibility is preserved, but the actual mixed-path lift still comes from local_ref rag translation rather than processing overlap itself

## 2. exact changes
- 변경 파일: `app/core/runtime/labeler.py`
- 변경 파일: `scripts/refine_imported_processing_profiles.py`
- 변경 파일: `app/core/runtime/imported_material_probe.py`
- refinement: added processor_compare-doc-only local cue refinement for scene/flow/D/I/S inference
- refinement: shifted heading, definition, process, problem, solution, and contrast cues into local dust labeling
- refinement: added selective re-label script so imported docs can be updated without full rebuild or reingest
- 유지: viewer routes
- 유지: translation scope
- 유지: canonical/possibility evaluator thresholds
- 유지: bridge opening rules

## 3. verification
- canonical 사례 유지:
  - doc_004 <-> doc_005: `canonical`
  - doc_005 <-> doc_006: `canonical`
  - test_live_space_sync_20260321 <-> test_canonical_ingest_20260321: `canonical`
- processing 지표 전/후 비교:
  - `doc_004.txt`: sig_ratio 0.3333 -> 0.6, flatness 0.7263 -> 0.403, local_ref_uniqueness 0.3333 -> 0.6
  - `doc_005.txt`: sig_ratio 0.1644 -> 0.274, flatness 0.7623 -> 0.5573, local_ref_uniqueness 0.1644 -> 0.274
  - `doc_006.txt`: sig_ratio 0.1644 -> 0.2055, flatness 0.8103 -> 0.563, local_ref_uniqueness 0.1644 -> 0.2055
- mixed pair 결과 재확인:
  - `doc_004`: mode=`none`, none_reason=`anchor_vocabulary_translation_gap`, translation_available=False, matched_handles=[]
  - `doc_005`: mode=`none`, none_reason=`anchor_vocabulary_translation_gap`, translation_available=False, matched_handles=[]
  - `doc_006`: mode=`possibility_candidate`, none_reason=``, translation_available=True, matched_handles=['rag']

## 4. current reading
- processing flatness was reduced meaningfully on doc_005/doc_006, but doc_006 possibility is still mainly translation-assisted while doc_005 remains none due to no local handle convergence

## 5. next recommendation
- 다음 축: revisit translation+processing interplay rather than widening translation blindly
- 보조 refinement: if another processing pass is needed, focus on local_ref-level refinement for unknown/heading-like spans only
- review 시작점: possibility promotion review should start from doc_006, not doc_005
