# prompts_usage

## 목적
이 문서는 `gemini/prompts/` 아래 프롬프트를 언제 어떻게 쓰는지 빠르게 알려주는 문서다.

프롬프트 위치:
- [review_diff.md](/Users/sungsookim/universe/vectorfl_replica/gemini/prompts/review_diff.md)
- [summarize_board.md](/Users/sungsookim/universe/vectorfl_replica/gemini/prompts/summarize_board.md)
- [check_pointer.md](/Users/sungsookim/universe/vectorfl_replica/gemini/prompts/check_pointer.md)

## `review_diff.md`

### 언제 쓰나
- Codex가 수정한 직후
- diff에서 위험 후보를 빠르게 보고 싶을 때

### 무엇을 검사하나
- 핵심 변화 요약
- 코어 경로 touched 여부
- 위험 변경 후보
- 확인 필요 포인트

### 예시 명령
- 입력:
  - `git diff`
  - changed files

### 기대 출력
- 핵심 변화 5줄
- 코어 touched 경고
- 위험 후보
- 확인 필요 포인트

## `summarize_board.md`

### 언제 쓰나
- 실행 / routing 후 현재 상태를 빨리 보고 싶을 때
- latest board와 provenance compacted를 함께 읽고 싶을 때

### 어떤 입력을 보나
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [runtime/views/provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)

### 예시 명령
- 입력:
  - latest board
  - provenance compacted latest

### 기대 출력
- 현재 상태 요약 5줄
- 주의 포인트 3개
- 다음 확인 포인트 3개

## `check_pointer.md`

### 언제 쓰나
- latest / per-run 구조가 제대로 분리됐는지 보고 싶을 때
- pointer surface thinning 이후 규칙이 유지되는지 검사할 때

### 어떤 입력을 보나
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)
- per-run board
- per-run commands

### 예시 명령
- 입력:
  - latest board
  - latest commands
  - 최근 per-run board
  - 최근 per-run commands

### 기대 출력
- latest에 과한 내용이 남았는지
- pointer 누락이 있는지
- 역할 분리가 깨졌는지

## 사용 순서 추천
1. 수정 직후:
   `review_diff.md`
2. 실행 직후:
   `summarize_board.md`
3. 구조 점검:
   `check_pointer.md`

## 한 줄 결론
프롬프트는 각각 역할이 다르다. diff는 검토용, summarize는 브리핑용, check_pointer는 구조 점검용이다.
