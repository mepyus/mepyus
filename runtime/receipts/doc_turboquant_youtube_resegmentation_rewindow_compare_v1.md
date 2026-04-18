# doc_turboquant_youtube_resegmentation_rewindow_compare_v1.md

- operation_date: 2026-03-29
- operation_scope: segmentation/window sensitivity compare for `turboquant_youtube`
- prepared_by: Codex

## source

- `inputs/external_cases/TurboQuant_youtube.txt`

## compare runs

- baseline reference:
  - `app/work/dialogue_loop_test/generated/turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z.json`
- run B:
  - `app/work/dialogue_loop_test/generated/turboquant_youtube_reseg_b_v1_w3_s1_20260328T213755Z.json`
- run C:
  - `app/work/dialogue_loop_test/generated/turboquant_youtube_reseg_c_v1_w4_s2_20260328T213755Z.json`

## validation

- identical source reused across all runs
- no baseline overwrite
- compare based on probe output + canonical candidate mapping only
- all three runs checked for:
  - `block_count`
  - `window_count`
  - packet/state movement

## result

- run B and run C both remained `block_count=1`, `window_count=1`
- no packet texture movement observed
- no canonical candidate movement observed
- final read: `compression-dominant intrinsic` within current segmentation/window tuning range
