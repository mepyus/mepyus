# doc_lecture_transcript_cohort_batch_test_v1.md

- operation_date: 2026-03-29
- operation_scope: lecture transcript cohort batch test
- prepared_by: Codex

## cohort

- `choi_ai_classroom_cnn`
- `choi_ai_classroom_neural_networks`
- `choi_ai_classroom_transformer1`
- `choi_ai_classroom_vlm`

## validation

- same source class used across all 4 assets
- same probe params applied:
  - `window_size=6`
  - `stride=3`
  - `segment_assist=index_support`
- each asset passed through:
  - source
  - probe packet
  - canonical state append
  - latest/history
  - diff/attention/memory
  - process console read

## result

- all 4 assets formed multi-window packets (`window_count` 163~169)
- all 4 assets were conservatively canonicalized as:
  - `structured_open_low_emergence`
  - `partially_grounded`
  - `low_emergence`
  - `medium`
  - `weak`
  - `traceable`
- final cohort judgment: `lecture-structured recoverable cohort`
- compare surface written:
  - `runtime/views/lecture_transcript_cohort_compare_v1.json`
