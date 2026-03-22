# Imported Contract Recovery 2026-03-21

## 1. current diagnosis
- imported post-materialization 상태: partially_restored_minimal_handoff_contract
- 어떤 contract field 가 왜 비었는지: 기존 imported materials는 dust split 이후 metadata에 `observer trace`만 남고 `anchor_bundle / processing_values / transformable_handles`가 빠져 있었다
- 가장 강한 upstream 손실 지점: dust 이후 material metadata assembly / persistence gap

## 2. exact changes
- added helper: [imported_material_contract.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/imported_material_contract.py)
- added script: [recover_imported_material_contract.py](/Users/sungsookim/universe/vectorfl_replica/scripts/recover_imported_material_contract.py)
- updated probe: [imported_material_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/imported_material_probe.py)
- recovered fields: `anchor_bundle`, `processing_values`, `transformable_handles`, `dropped_weak_anchors`
- intentionally unchanged: bridge evaluator threshold, viewer, translation layer

## 3. verification
### recovery after metrics
- engine_phase1_observer_probe_20260321 <-> doc_004: `none` / none_reason=`anchor_vocabulary_translation_gap`
  imported post material_count=15 anchor_bundle_ratio=1.0 processing_ratio=1.0 handle_ratio=1.0 local_ref_ratio=1.0
  flatten indicators: single_source_ref_spread_over_many_materials
- engine_phase1_observer_probe_20260321 <-> doc_005: `none` / none_reason=`anchor_vocabulary_translation_gap`
  imported post material_count=73 anchor_bundle_ratio=1.0 processing_ratio=1.0 handle_ratio=1.0 local_ref_ratio=1.0
  flatten indicators: single_source_ref_spread_over_many_materials
- engine_phase1_observer_probe_20260321 <-> doc_006: `none` / none_reason=`anchor_vocabulary_translation_gap`
  imported post material_count=73 anchor_bundle_ratio=1.0 processing_ratio=1.0 handle_ratio=1.0 local_ref_ratio=1.0
  flatten indicators: single_source_ref_spread_over_many_materials

### live-legacy possibility kept
- engine_phase1_imported_doc_probe_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`
- engine_phase1_imported_doc_probe2_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`

### canonical cases kept
- doc_004 <-> doc_005
- doc_005 <-> doc_006
- test_live_space_sync_20260321 <-> test_canonical_ingest_20260321

## 4. current reading
- imported materials now carry minimal handoff contract
- contract recovery confirmed, but imported many-material spread is still broad
- live-imported none is no longer pure contract absence; now it is closer to `broad imported alignment + vocabulary gap`

## 5. next recommendation
- first: one more turn on local reference / imported many-material spread
- second: then bounded handle translation layer can be considered
- translation layer is no longer pure 덧칠 risk, but still premature if imported localizable projection stays broad
