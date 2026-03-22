# observer output contract v1

## source_manifest
- `input_id`
- `source_path`
- `label`
- `input_kind`
- `detected_profile`
- `split_mode_used`
- `raw_line_count`
- `unit_count`
- `run_id`

## split_units
- `unit_id`
- `start_ref`
- `end_ref`
- `unit_type`
- `text_excerpt`
- `char_count`
- `source_segment_ids`

## processing_trace
- `run_id`
- `input_id`
- `detected_profile`
- `split_mode_used`
- `source_unit_count`
- `merged_unit_count`
- `engine_stage`
  - `ingest_only`
  - `split_complete`
  - `summary_written`
- `notes`

## readable_input_board
반드시 포함:
1. 입력 정보
2. split mode
3. 총 unit 수
4. unit 목록 요약
5. 각 unit 짧은 발췌
6. 당장 읽히는 흐름 한 줄 메모

## operator_summary
반드시 포함:
1. 입력 인식 결과
2. 분해 결과
3. 흐름 요약
4. 처리 상태
5. 다음 확장 가능 포인트
