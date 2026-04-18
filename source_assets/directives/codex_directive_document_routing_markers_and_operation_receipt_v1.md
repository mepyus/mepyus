[[A]] [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]

# codex_directive_document_routing_markers_and_operation_receipt_v1

## 0. 문서 목적
이번 작업의 목적은 아래 4개를 동시에 해결하는 것이다.

1. 구조화 문서를 붙여 넣었을 때 기존처럼 바로 실행부터 튀지 않도록,
   **가벼운 문서 라우팅 표식 체계**를 고정한다.
2. 사용자가 문서 맨 위에 최소 표식만 붙여도
   **입력 -> 등록 -> 티켓화 -> 실행** 흐름이 안정적으로 갈 수 있게 만든다.
3. 문서 처리 후 결과가 여러 파일에 흩어져 사용자가 일일이 들어가 확인해야 하는 번거로움을 줄이기 위해,
   **단일 operation receipt / board view** 를 만든다.
4. 이 작업 자체도
   **입력 후 실행(ingest_then_execute)** 흐름으로 처리하고,
   md 파일 생성 / event 기록 / 결과 요약이 실제로 남는지 검산한다.

즉 이번 턴은
**문서 라우팅 표식 + 단일 처리 요약면 + 최소 운영 뷰 시드**
를 설치하는 턴이다.

## 1. 현재 문제 진단

### 1.1 실행이 먼저 튄다
구조화 문서를 붙여 넣으면, 현재는 종종
- 문서를 먼저 엔진 재료로 등록/판독하기보다
- 기존 습관대로 바로 실행부터 들어가는 경향이 있다.

이건 현재 운영 기준과 어긋난다.

현재 맞는 순서는 아래다.

- 문서 수신
- 문서 역할 판독/등록
- 필요한 경우에만 티켓화
- 실행
- 사건 기록
- 단일 요약면 생성

### 1.2 표식이 없으면 역할 분리가 흐려진다
지금까지는 대화 맥락으로도 추론이 가능했지만,
- declaration
- baseline
- directive
- summary
- memo

같은 문서 역할과,

- ingest_only
- ingest_then_execute
- reference_only

같은 처리 모드를 매번 문맥 추론에만 맡기면 헷갈릴 수 있다.

### 1.3 결과 확인이 너무 분산돼 있다
현재는
- registry
- ticket
- provenance
- event ledger
- ingest 결과 파일
- status 문서

를 각각 따로 들어가 봐야 해서 확인 비용이 높다.

즉 지금 필요한 것은
**가벼운 입력 표식** 과
**단일 요약/조회면** 이다.

## 2. 이번 턴의 목표 상태

이번 턴이 끝나면 아래가 가능해야 한다.

1. 사용자가 문서 맨 위에 작은 표식 2~3개만 붙여도 된다.
2. Codex는 그 표식을 보고 먼저 ingest/등록을 수행한다.
3. `RUNMODE` 가 실행을 허용할 때만 티켓화 및 실행으로 간다.
4. 처리 결과는 append-only 이벤트로 남는다.
5. 사용자는 개별 파일을 일일이 뒤지지 않고,
   **operation receipt** 또는 **operation board** 에서 한 번에 본다.
6. 실행에 사용한 명령어도 별도 md 에 저장되어 later reuse 가능하다.

## 3. 이번 턴의 핵심 원칙

### 3.1 표식은 작고 가벼워야 한다
무거운 문법을 만들지 않는다.
최소 표식 3개만 도입한다.

- `[[DOCROLE:...]]`
- `[[RUNMODE:...]]`
- `[[PRIORITY:...]]`

### 3.2 무표식 기본값은 실행 금지 쪽으로 둔다
가장 중요한 기본값은 아래다.

**`RUNMODE` 가 없으면 `ingest_only` 로 간주한다.**

즉 무표식 문서는 바로 실행하지 않는다.

### 3.3 사람은 편하게 쓰고, 엔진은 정규화해서 저장한다
사용자는 영어 canonical value를 억지로 외우지 않아도 된다.
한글 표현도 허용하되, Codex는 내부에서 canonical value로 정규화해 기록한다.

예:
- `[[DOCROLE:지시서]]` -> `directive`
- `[[RUNMODE:입력후실행]]` -> `ingest_then_execute`
- `[[PRIORITY:높음]]` -> `high`

### 3.4 operation receipt 는 단일 조회면이어야 한다
이번 문서 처리 결과를 확인할 때
여러 registry, ledger, generated 파일을 따로 열지 않도록
**한 문서당 1개의 operation receipt** 를 만든다.

### 3.5 운영 뷰는 처음부터 거대 UI로 가지 않는다
이번 턴은 live UI 전체가 아니라
**운영화면 뷰 시드(seed)** 를 만든다.

즉:
- latest operation board
- recent docs
- recent tickets
- recent outputs
- recent events
- latest commands

정도의 단일 md/board면이면 충분하다.

## 4. 반드시 만들 산출물

### 4.1 정책 문서
- `docs/policies/document_routing_markers_policy_v1.md`

### 4.2 사용자용 템플릿 문서
- `docs/templates/structured_doc_routing_header_template_v1.md`

### 4.3 alias / normalization 기준
- `runtime/manifests/document_routing_alias_map_v1.json`

### 4.4 처리 스크립트 또는 wrapper
- `scripts/process_structured_doc_with_routing.py`

### 4.5 operation receipt
- `runtime/receipts/<doc_id>_operation_receipt.md`

### 4.6 operation board 시드
- `runtime/views/operation_board_latest.md`

### 4.7 실행 명령어 저장 문서
- `runtime/commands/structured_doc_routing_commands_v1.md`

## 5. 라우팅 표식 규칙

### 5.1 최소 표식
문서 맨 위에 아래 세 줄을 허용한다.

```text
[[DOCROLE:directive]]
[[RUNMODE:ingest_then_execute]]
[[PRIORITY:high]]
```

또는 사용자 편의상 아래도 허용한다.

```text
[[DOCROLE:지시서]]
[[RUNMODE:입력후실행]]
[[PRIORITY:높음]]
```

Codex는 이를 내부 canonical value로 정규화한다.

### 5.2 기본값 규칙
- `DOCROLE` 없고 애매하면 `memo`
- `RUNMODE` 없으면 `ingest_only`
- `PRIORITY` 없으면 `normal`

### 5.3 사용 권장 규칙
- declaration / baseline / summary / memo -> 보통 `ingest_only`
- directive -> 보통 `ingest_then_execute`
- 외부 참고자료 -> `reference_only`
- `execute_only` 는 예외적으로만 허용

## 6. 처리 흐름
`문서 -> parse -> normalize -> register -> (optional ticket) -> (optional execute) -> record -> receipt -> board`

## 7. 반드시 점검할 기록 항목
- `doc_registered`
- `routing_normalized`
- `ticket_created` (해당 시)
- `execution_started` (해당 시)
- `file_created` / `file_updated` (해당 시)
- `output_generated`
- `receipt_written`
- `board_updated`

## 8. operation receipt 확인 항목
1. 어떤 문서를 처리했는가
2. 어떤 표식을 읽었는가
3. 어떤 canonical 값으로 정규화되었는가
4. 티켓이 생겼는가
5. 실제 실행되었는가
6. 어떤 이벤트가 남았는가
7. 어떤 산출물이 생겼는가
8. 어디를 보면 다음 추적이 가능한가
9. 어떤 명령으로 재현 가능한가

## 9. operation board 최소 섹션
- latest structured docs
- latest tickets
- latest outputs
- latest events
- latest receipts
- latest commands
- current note / caution

## 10. 이번 턴 비범위
- full web UI 구축
- 거대한 dashboard 프레임워크 설치
- 모든 문서 타입 완전 지원
- complex ontology 편집기 추가
- 자동 reclassification 고도화
- 모든 existing docs 일괄 마이그레이션

## 11. 완료 조건
1. 라우팅 표식 정책 md가 생긴다.
2. 사용자용 최소 템플릿이 생긴다.
3. alias 정규화 기준 파일이 생긴다.
4. 라우팅 처리 wrapper 또는 동등한 진입점이 생긴다.
5. 문서 1개 이상을 `ingest_then_execute` 로 실제 처리한다.
6. operation receipt 가 생성된다.
7. latest operation board 가 생성/갱신된다.
8. 실행 명령어 문서가 생긴다.
9. event ledger 에 처리 단계가 append 된다.

## 12. 보고 형식
- 생성/수정 파일 목록
- 테스트 문서 처리 결과
- 기록 검산
- 다음 턴 연결점

## 13. 마지막 지시
Codex는 이번 턴에서
**구조화 문서를 “붙여 넣자마자 바로 실행되는 텍스트”가 아니라,
작은 라우팅 표식을 통해 먼저 등록/판독되고, 필요할 때만 실행되며,
그 전체 처리 결과가 단일 receipt와 board로 모이는 운영 객체**로 만들어라.

특히 아래를 지켜라.
- `RUNMODE` 가 없으면 기본값은 `ingest_only`
- 사용자는 한글 alias를 써도 된다
- Codex는 내부 canonical value로 정규화한다
- 처리 결과는 여러 파일에 흩어지지 않고 receipt/board 에 요약된다
- 실행 명령어도 따로 저장한다
- 이번 작업 자체가 이벤트로 남는지 검산한다
