# CODEx 지시서 — Processor Compare Pipeline v1

## 0. 목적
이번 작업의 목적은 UI/뷰어를 만드는 것이 아니다.
Replica 코어를 수정하는 것도 아니다.

목표는 오직 하나다.

**동일 fragment 입력에 대해 Codex / ChatGPT / Gemini의 표준 출력(JSON)을 저장하고,
그 차이를 비교하여 입력기/라벨기/앵커기 조정 데이터로 축적하는 비교 파이프라인을 만든다.**

이번 턴에서 필요한 것은:
- raw 출력 보존
- schema 검증
- 정규화
- 비교
- summary report 생성

뷰어/공간 표현은 추후 문제다.

---

## 1. 작업 원칙
- Replica 코어 로직 수정 금지
- read-only / sidecar / work 영역에서만 작업
- raw 출력은 절대 덮어쓰지 말 것
- normalized와 comparison 결과는 별도 폴더에 저장
- 동일 schema를 강제
- 비교 목적은 정답 판정이 아니라 차이 축적임

---

## 2. 디렉토리 목표 구조

작업 폴더 예시:

app/work/processor_compare/
  ├── standards/
  │   └── processor_standard_v1.md
  ├── inputs/
  │   └── sample_fragments.jsonl
  ├── processor_outputs/
  │   ├── raw/
  │   │   ├── codex/
  │   │   ├── chatgpt/
  │   │   └── gemini/
  │   └── normalized/
  │       ├── codex/
  │       ├── chatgpt/
  │       └── gemini/
  ├── reports/
  │   ├── comparison_summary.json
  │   ├── comparison_summary.md
  │   ├── stable.jsonl
  │   ├── split.jsonl
  │   ├── hidden_candidate.jsonl
  │   └── broken_link.jsonl
  └── scripts/
      ├── validate_processor_output.py
      ├── normalize_processor_output.py
      ├── compare_processor_outputs.py
      └── run_compare_pipeline.sh

---

## 3. 표준 입력/출력 기준
`standards/processor_standard_v1.md` 파일을 만들고,
아래 schema를 기준으로 raw JSON 검증이 가능하게 하라.

필수 필드:
- input_doc_id
- input_bundle_id
- fragment_id
- fragment_text
- source_type
- fragment_version
- anchors
- direction
- intensity
- stability
- scene
- role
- semantic_tags
- structural_tags
- confidence
- ambiguity
- evidence_text
- why_short
- processor_notes

anchors 배열 각 원소 필드:
- anchor_id
- anchor_label
- anchor_type
- anchor_scope

제약:
- direction/intensity/stability/confidence/ambiguity 는 0~1 float
- scene/role는 지정된 enum
- semantic_tags/structural_tags/evidence_text/processor_notes는 배열
- processor_notes는 최대 2개
- 자유 장문 설명 금지

---

## 4. validate script 요구사항
`validate_processor_output.py`

역할:
- raw JSON 또는 JSONL 파일 읽기
- schema 누락/타입 오류/enum 오류/범위 오류 검증
- processor별 오류 리포트 출력
- 실패 건수와 상세 메시지 출력
- exit code를 적절히 반환

---

## 5. normalize script 요구사항
`normalize_processor_output.py`

역할:
- raw 출력 읽기
- processor_id를 외부 인자로 받거나 폴더명으로 추론
- 문자열 trim
- 태그 lower/snake_case 정리
- anchor_label 정규화
- 배열 정렬(의미 훼손 없는 범위)
- normalized JSONL 출력

주의:
- raw 절대 수정 금지
- 의미를 새로 만들지 말 것
- 정규화는 비교 가능성 확보 목적만 수행

---

## 6. compare script 요구사항
`compare_processor_outputs.py`

입력:
- normalized/codex
- normalized/chatgpt
- normalized/gemini

비교 단위:
- 같은 fragment_id
- 가능하면 같은 normalized anchor_label 기준

비교 항목:
- numeric deltas: direction/intensity/stability/confidence/ambiguity
- scene/role agreement
- semantic_tags overlap
- structural_tags overlap
- anchor overlap
- evidence_text overlap(간단 수준)
- why_short는 비교 설명용 참고만

출력 분류:
1. stable
   - 세 처리자가 거의 유사
2. split
   - 반복적으로 명확히 갈라짐
3. hidden_candidate
   - 한 처리자만 반복적으로 잡는 값/anchor/tag
4. broken_link
   - 어떤 처리자는 연결/anchor를 만들고 어떤 처리자는 못 만듦

리포트:
- comparison_summary.json
- comparison_summary.md
- stable.jsonl
- split.jsonl
- hidden_candidate.jsonl
- broken_link.jsonl

---

## 7. markdown summary 요구사항
`comparison_summary.md`에는 최소한 아래를 넣어라.

- 총 fragment 수
- processor별 유효 출력 수
- stable / split / hidden_candidate / broken_link 개수
- divergence가 큰 anchor top N
- scene disagreement top N
- role disagreement top N
- tag mismatch examples
- 입력기 조정 후보 포인트
- 라벨기 조정 후보 포인트

이 문서는 사람이 읽기 쉽게 짧고 명확하게 작성.

---

## 8. shell runner 요구사항
`run_compare_pipeline.sh`

순서:
1. validate raw/codex
2. validate raw/chatgpt
3. validate raw/gemini
4. normalize
5. compare
6. reports 생성

실패 시 어디서 멈췄는지 명확히 출력.

---

## 9. 범위 제한
이번 턴에서는 절대 하지 말 것:
- viewer/UI
- Replica core schema 변경
- DB 마이그레이션
- visualization
- vectorfl_next 삽입
- replica 본 파이프라인 개조

---

## 10. 최종 산출물
최종적으로 아래가 있어야 한다.

- standards/processor_standard_v1.md
- sample input 1개 이상
- validate/normalize/compare/run scripts
- sample report 1세트
- README 또는 짧은 사용법

목표는 “비교값이 잘 보이는지 확인하는 것”이다.