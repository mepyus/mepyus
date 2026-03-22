# Boundary Case Labeling Checklist v1

저장 전에 이 다섯 가지만 확인:

1. 파일은 `JSONL`인가
2. 총 줄 수는 `30`줄인가
3. `fragment_id`가 `bcase_v101_001` 같은 `final_case_id`와 정확히 일치하는가
4. `input_doc_id`, `input_bundle_id`, `source_type`, `fragment_version`를 임의 수정하지 않았는가
5. `scene`이 허용값 밖으로 나가지 않았는가

허용 `scene`:
- `discovery`
- `explanation`
- `comparison`
- `evidence`
- `question`
- `reflection`
- `instruction`
- `transition`
- `unknown`

허용 `role`:
- `thesis`
- `support`
- `bridge`
- `example`
- `contrast`
- `definition`
- `expansion`
- `problem`
- `meta`
- `unknown`

