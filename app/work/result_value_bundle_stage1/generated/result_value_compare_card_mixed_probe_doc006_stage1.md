# result-value compare card: mixed_probe_doc006_stage1

## 1. card header
- candidate_id: `mixed_probe_doc006_stage1`
- case_type: `mixed`
- workbench_reading_category: `mixed`
- workbench_reading_status: `confirmed_hold`
- verdict: closure gap이 남아 confirmed_hold로 유지되는 후보

## 2. source
- source_ref: `left=engine_phase1_observer_probe_20260321` / `right=processor_compare/doc_006.txt`
- source_local_ref: `left=missing` / `right=persisted`
- lineage_refs: `left=sparse` / `right=present`

## 3. translation
- translated_handles: `left=missing` / `right=persisted`
- anchor_bundle: `left=rep=4, support=3, promoted=7` / `right=rep=4, support=4, promoted=8`
- processing_values: `left=D=0.5, I=0.5, S=0.5, flow=compare, scene=review` / `right=D=0.6, I=0.68, S=0.52, flow=compare, scene=review`
- translation_join: `right_present_left_missing`

## 4. join
- best_local_ref: `processor_compare/doc_006.txt::dst_src_2fd2c39f0fd7_016`
- bridge_trace_ref: `missing`
- local_space_ref: `persisted`
- join_closure: `mixed_pair_explicit_bridge_missing`

## 5. block
- next_review_blocker: `live_side_family_present_but_not_canonicalized`
- missing_join_points: `["left.source_local_ref missing", "left.translated_handles missing", "exact current_pair bridge_trace missing"]`
- block_summary: `source-side live material lacks source_local/translated layer and the current pair has no exact persisted bridge closure`
- mixed_record_ref: `mixed_minimum_record::mixed_probe_doc006_stage1`
- closure_gap_summary: `["left.source_local_ref missing", "left.translated_handles missing", "exact current_pair bridge_trace missing"]`
- derived_support_summary: `best_local_ref + review_focus + next_review_blocker`
- next_review_question: `increase_cross_path_family_corroboration`

## 6. reuse hints
- point_seed: `yes`
- workbench_seed: `yes`
- compare_seed: `yes`
- ribbon_seed: `later`
