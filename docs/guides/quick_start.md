# quick_start

## 목적
이 문서는 가장 빨리 다시 시작할 수 있게 만든 짧은 운영 문서다.

헷갈릴 때는 이 문서부터 본다.

## 기본 7단계
1. Codex로 작업한다
2. `gdiff`로 변경점과 위험 후보를 본다
3. 필요하면 Codex가 수정한다
4. 실행 또는 structured doc routing을 수행한다
5. `gsum`으로 현재 상태를 본다
6. `gcheck`로 pointer 구조를 점검한다
7. latest board / receipt / per-run artifact를 확인하고 사용자가 판단한다

## 최소 확인 경로
- latest board:
  - [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- latest commands:
  - [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)
- latest provenance compacted:
  - [runtime/views/provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)
- receipts:
  - [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)

## 가장 짧은 명령 흐름
- 작업
- `gdiff`
- 수정
- 실행 / routing
- `gsum`
- `gcheck`

## 문제가 생기면 어디부터 보나

### 1. 현재 상태가 궁금할 때
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)

### 2. 상세 근거가 필요할 때
- 최신 per-run board
- 최신 per-run commands
- 최신 receipt

### 3. provenance가 지저분해 보일 때
- [runtime/views/provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)

### 4. Gemini를 어떻게 써야 할지 헷갈릴 때
- [gemini_usage.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/gemini_usage.md)
- [gemini/gemini.md](/Users/sungsookim/universe/vectorfl_replica/gemini/gemini.md)

## 폴더 역할도 같이 기억
- `contracts/` = 법 / 절대 기준
- `policies/` = 운영 규정
- `reports/` = 분석 / 결과
- `guides/` = 사용 설명서 / 운영 메뉴얼

## 한 줄 결론
막히면 latest를 보고, 더 필요하면 per-run으로 내려가고, 판단은 마지막에 사용자가 한다.
