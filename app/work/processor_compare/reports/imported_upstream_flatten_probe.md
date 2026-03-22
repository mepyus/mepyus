# Imported Upstream Flatten Probe 2026-03-21

## 1. current diagnosis
- imported upstream 상태: split_preserved_but_post_materialization_local_signal_sparse
- flatten suspected: true
- live-imported none 의 가장 강한 upstream blocker: imported material은 문장 단위 split은 유지하지만 post-materialization metadata에서 `anchor_bundle / processing_values / transformable_handles`가 거의 사라진다

## 2. exact changes
- added helper: [imported_material_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/imported_material_probe.py)
- added probe/log only: pre_materialization_profile, post_materialization_profile, flatten_indicators
- intentionally unchanged: bridge evaluator threshold, viewer, translation layer

## 3. verification
### canonical cases
- unchanged by this turn

### live-imported none
- engine_phase1_observer_probe_20260321 <-> doc_004: `none` / none_reason=`anchor_vocabulary_translation_gap`
  left pre units=1 avg_span=121.0 | right pre units=15 avg_span=69.07
  right post material_count=15 anchor_bundle_ratio=0.0 processing_ratio=0.0 handle_ratio=0.0
  right flatten indicators: material_count_high_but_anchor_bundle_absent, material_count_high_but_processing_values_absent, material_count_high_but_transformable_handles_absent, single_source_ref_spread_over_many_materials, localizable_anchor_density_absent
- engine_phase1_observer_probe_20260321 <-> doc_005: `none` / none_reason=`anchor_vocabulary_translation_gap`
  left pre units=1 avg_span=121.0 | right pre units=73 avg_span=69.58
  right post material_count=73 anchor_bundle_ratio=0.0 processing_ratio=0.0 handle_ratio=0.0
  right flatten indicators: material_count_high_but_anchor_bundle_absent, material_count_high_but_processing_values_absent, material_count_high_but_transformable_handles_absent, single_source_ref_spread_over_many_materials, localizable_anchor_density_absent
- engine_phase1_observer_probe_20260321 <-> doc_006: `none` / none_reason=`anchor_vocabulary_translation_gap`
  left pre units=1 avg_span=121.0 | right pre units=73 avg_span=72.68
  right post material_count=73 anchor_bundle_ratio=0.0 processing_ratio=0.0 handle_ratio=0.0
  right flatten indicators: material_count_high_but_anchor_bundle_absent, material_count_high_but_processing_values_absent, material_count_high_but_transformable_handles_absent, single_source_ref_spread_over_many_materials, localizable_anchor_density_absent

### live-legacy possibility
- engine_phase1_imported_doc_probe_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`
  left pre units=1 avg_span=117.0 | right pre units=1 avg_span=87.0
  left post material_count=1 anchor_bundle_ratio=1.0 processing_ratio=1.0 handle_ratio=1.0
  right post material_count=2 anchor_bundle_ratio=0.0 processing_ratio=0.0 handle_ratio=0.0
- engine_phase1_imported_doc_probe2_20260321 <-> test_live_space_sync_20260321: `possibility_candidate`
  left pre units=1 avg_span=100.0 | right pre units=1 avg_span=87.0
  left post material_count=1 anchor_bundle_ratio=1.0 processing_ratio=1.0 handle_ratio=1.0
  right post material_count=2 anchor_bundle_ratio=0.0 processing_ratio=0.0 handle_ratio=0.0

## 4. upstream reading
- imported docs are not failing at the first split stage
- imported docs do fragment into sentence-like dust units (`doc_004=15`, `doc_005=73`, `doc_006=73`)
- but imported post-materialization contract is sparse:
  - `anchor_bundle_presence_ratio = 0.0`
  - `processing_values_presence_ratio = 0.0`
  - `transformable_handles_presence_ratio = 0.0`
- live probe materials keep all three at `1.0`
- therefore: flatten + vocabulary gap both present, flatten dominates

## 5. next recommendation
- first: fragment narrowing/localizable projection 보다 정확히는 imported post-materialization contract 복원이 우선
- second: bounded handle translation layer 는 그 다음
- translation layer 를 지금 먼저 넣으면 upstream flatten 위에 덧칠할 위험이 큼
