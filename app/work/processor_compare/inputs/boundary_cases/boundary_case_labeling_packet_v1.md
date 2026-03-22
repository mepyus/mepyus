# Boundary Case Labeling Packet v1

목적:
- `boundary_cases_v1_01_final.json`의 각 `case_text`를
  `Codex / ChatGPT / Gemini`가 같은 schema로 라벨링하게 한다.
- 지금은 `fragment boundary`보다 `scene / role / score` drift를 보는 것이 우선이다.

사용 대상 세트:
- 기본: [boundary_cases_v1_01_final.json](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/inputs/boundary_cases/final_sets/boundary_cases_v1_01_final.json)
- 보조: [boundary_cases_v1_final.json](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/inputs/boundary_cases/final_sets/boundary_cases_v1_final.json)

입력 규칙:
- 각 case는 독립 fragment처럼 처리한다.
- `case_text`를 그대로 `fragment_text`로 사용한다.
- `final_case_id`를 `fragment_id`로 그대로 사용한다.
- `target_axis`, `boundary_pair`, `expected_tension`은 참고용 메타이며 모델 출력 JSON에는 넣지 않는다.

고정 메타:
- `input_doc_id`: `boundary_cases_v1_01`
- `input_bundle_id`: `bundle_boundary_calibration_v1`
- `source_type`: `calibration_case`
- `fragment_version`: `v1`

권장 실행 방식:
1. 처리자에게 [processor_execution_prompt_v2.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/standards/processor_execution_prompt_v2.md) 를 준다.
2. 각 case를 아래 입력 포맷으로 하나씩 넣는다.
3. 응답 JSON을 처리자별 raw 폴더에 JSONL로 저장한다.

입력 포맷:
```text
[input metadata]
input_doc_id: boundary_cases_v1_01
input_bundle_id: bundle_boundary_calibration_v1
fragment_id: bcase_v101_001
fragment_text: 신경 가소성은 인간의 뇌가 경험에 반응하여 스스로 구조를 재설계하는 놀라운 능력을 의미합니다. 어제와 다른 오늘의 나를 만드는 이 생물학적 기제는, 결국 우리가 고정된 운명의 수혜자가 아니라 스스로를 조각해 나가는 예술가임을 증명하는 과학적 증거일지도 모릅니다.
source_type: calibration_case
fragment_version: v1
```

저장 위치:
- Codex raw: [raw/codex](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/processor_outputs/boundary_labels/raw/codex)
- ChatGPT raw: [raw/chatgpt](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/processor_outputs/boundary_labels/raw/chatgpt)
- Gemini raw: [raw/gemini](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/processor_outputs/boundary_labels/raw/gemini)

권장 파일명:
- `boundary_cases_v1_01.jsonl`

출력 규칙:
- JSONL 한 줄당 1 case
- 총 30줄
- `fragment_id`는 반드시 `final_case_id` 그대로 유지

