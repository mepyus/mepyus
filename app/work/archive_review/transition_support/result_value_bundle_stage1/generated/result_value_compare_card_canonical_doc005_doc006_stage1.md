# result-value compare card: canonical_doc005_doc006_stage1

## 1. card header
- candidate_id: `canonical_doc005_doc006_stage1`
- case_type: `canonical`
- workbench_reading_category: `canonical`
- workbench_reading_status: `stable_reading`
- verdict: source -> translation -> bridge가 비교적 닫힌 stable_reading 후보

## 2. source
- source_ref: `left=processor_compare/doc_005.txt` / `right=processor_compare/doc_004.txt`
- source_local_ref: `left=persisted` / `right=persisted`
- lineage_refs: `left=present` / `right=present`

## 3. translation
- translated_handles: `left=persisted` / `right=persisted`
- anchor_bundle: `left=rep=4, support=1, promoted=5` / `right=rep=4, support=4, promoted=8`
- processing_values: `left=D=0.78, I=0.58, S=0.5, flow=run, scene=spec` / `right=D=0.5, I=0.5, S=0.5, flow=unknown, scene=unknown`
- translation_join: `symmetric_or_unknown`

## 4. join
- best_local_ref: ``
- bridge_trace_ref: `persisted`
- local_space_ref: `persisted`
- join_closure: `pair_bridge_present`

## 5. block
- next_review_blocker: ``
- missing_join_points: `[]`
- block_summary: `canonical pair already closes through persisted bridge/local-space exposure`

## 6. reuse hints
- point_seed: `yes`
- workbench_seed: `yes`
- compare_seed: `yes`
- ribbon_seed: `weak`
