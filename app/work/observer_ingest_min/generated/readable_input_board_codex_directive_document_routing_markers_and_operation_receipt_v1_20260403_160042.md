# readable input board / codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_160042

## 1. 입력 정보
- input_id: `codex_directive_document_routing_markers_and_operation_receipt_v1`
- label: `codex_directive_document_routing_markers_and_operation_receipt_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `253`
- unit_count: `34`

## 3. unit 목록 요약
- unit_001 — heading_block / preamble ~ preamble — "[[A]] [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]..."
- unit_002 — heading_block / codex_directive_document_routing_markers_and_operation_receipt_v1 ~ codex_directive_document_routing_markers_and_operation_receipt_v1 — "# codex_directive_document_routing_markers_and_operation_receipt_v1..."
- unit_003 — heading_block / 0. 문서 목적 ~ 0. 문서 목적 — "## 0. 문서 목적 이번 작업의 목적은 아래 4개를 동시에 해결하는 것이다. 1. 구조화 문서를 붙여 넣었을 때 기존처럼 바로 실행부터 튀지 않도록, **가벼운 문서 라우팅 표식 체계**를 고정한다. 2. 사용자가..."
- unit_004 — heading_block / 1. 현재 문제 진단 ~ 1. 현재 문제 진단 — "## 1. 현재 문제 진단..."
- unit_005 — heading_block / 1.1 실행이 먼저 튄다 ~ 1.1 실행이 먼저 튄다 — "### 1.1 실행이 먼저 튄다 구조화 문서를 붙여 넣으면, 현재는 종종 - 문서를 먼저 엔진 재료로 등록/판독하기보다 - 기존 습관대로 바로 실행부터 들어가는 경향이 있다. 이건 현재 운영 기준과 어긋난다. 현재 ..."
- unit_006 — heading_block / 1.2 표식이 없으면 역할 분리가 흐려진다 ~ 1.2 표식이 없으면 역할 분리가 흐려진다 — "### 1.2 표식이 없으면 역할 분리가 흐려진다 지금까지는 대화 맥락으로도 추론이 가능했지만, - declaration - baseline - directive - summary - memo 같은 문서 역할과, -..."
- unit_007 — heading_block / 1.3 결과 확인이 너무 분산돼 있다 ~ 1.3 결과 확인이 너무 분산돼 있다 — "### 1.3 결과 확인이 너무 분산돼 있다 현재는 - registry - ticket - provenance - event ledger - ingest 결과 파일 - status 문서 를 각각 따로 들어가 봐야 해..."
- unit_008 — heading_block / 2. 이번 턴의 목표 상태 ~ 2. 이번 턴의 목표 상태 — "## 2. 이번 턴의 목표 상태 이번 턴이 끝나면 아래가 가능해야 한다. 1. 사용자가 문서 맨 위에 작은 표식 2~3개만 붙여도 된다. 2. Codex는 그 표식을 보고 먼저 ingest/등록을 수행한다. 3. `..."
- unit_009 — heading_block / 3. 이번 턴의 핵심 원칙 ~ 3. 이번 턴의 핵심 원칙 — "## 3. 이번 턴의 핵심 원칙..."
- unit_010 — heading_block / 3.1 표식은 작고 가벼워야 한다 ~ 3.1 표식은 작고 가벼워야 한다 — "### 3.1 표식은 작고 가벼워야 한다 무거운 문법을 만들지 않는다. 최소 표식 3개만 도입한다. - `[[DOCROLE:...]]` - `[[RUNMODE:...]]` - `[[PRIORITY:...]]`..."
- unit_011 — heading_block / 3.2 무표식 기본값은 실행 금지 쪽으로 둔다 ~ 3.2 무표식 기본값은 실행 금지 쪽으로 둔다 — "### 3.2 무표식 기본값은 실행 금지 쪽으로 둔다 가장 중요한 기본값은 아래다. **`RUNMODE` 가 없으면 `ingest_only` 로 간주한다.** 즉 무표식 문서는 바로 실행하지 않는다...."
- unit_012 — heading_block / 3.3 사람은 편하게 쓰고, 엔진은 정규화해서 저장한다 ~ 3.3 사람은 편하게 쓰고, 엔진은 정규화해서 저장한다 — "### 3.3 사람은 편하게 쓰고, 엔진은 정규화해서 저장한다 사용자는 영어 canonical value를 억지로 외우지 않아도 된다. 한글 표현도 허용하되, Codex는 내부에서 canonical value로 정규..."
- unit_013 — heading_block / 3.4 operation receipt 는 단일 조회면이어야 한다 ~ 3.4 operation receipt 는 단일 조회면이어야 한다 — "### 3.4 operation receipt 는 단일 조회면이어야 한다 이번 문서 처리 결과를 확인할 때 여러 registry, ledger, generated 파일을 따로 열지 않도록 **한 문서당 1개의 ope..."
- unit_014 — heading_block / 3.5 운영 뷰는 처음부터 거대 UI로 가지 않는다 ~ 3.5 운영 뷰는 처음부터 거대 UI로 가지 않는다 — "### 3.5 운영 뷰는 처음부터 거대 UI로 가지 않는다 이번 턴은 live UI 전체가 아니라 **운영화면 뷰 시드(seed)** 를 만든다. 즉: - latest operation board - recent d..."
- unit_015 — heading_block / 4. 반드시 만들 산출물 ~ 4. 반드시 만들 산출물 — "## 4. 반드시 만들 산출물..."
- unit_016 — heading_block / 4.1 정책 문서 ~ 4.1 정책 문서 — "### 4.1 정책 문서 - `docs/policies/document_routing_markers_policy_v1.md`..."
- unit_017 — heading_block / 4.2 사용자용 템플릿 문서 ~ 4.2 사용자용 템플릿 문서 — "### 4.2 사용자용 템플릿 문서 - `docs/templates/structured_doc_routing_header_template_v1.md`..."
- unit_018 — heading_block / 4.3 alias / normalization 기준 ~ 4.3 alias / normalization 기준 — "### 4.3 alias / normalization 기준 - `runtime/manifests/document_routing_alias_map_v1.json`..."
- unit_019 — heading_block / 4.4 처리 스크립트 또는 wrapper ~ 4.4 처리 스크립트 또는 wrapper — "### 4.4 처리 스크립트 또는 wrapper - `scripts/process_structured_doc_with_routing.py`..."
- unit_020 — heading_block / 4.5 operation receipt ~ 4.5 operation receipt — "### 4.5 operation receipt - `runtime/receipts/<doc_id>_operation_receipt.md`..."
- unit_021 — heading_block / 4.6 operation board 시드 ~ 4.6 operation board 시드 — "### 4.6 operation board 시드 - `runtime/views/operation_board_latest.md`..."
- unit_022 — heading_block / 4.7 실행 명령어 저장 문서 ~ 4.7 실행 명령어 저장 문서 — "### 4.7 실행 명령어 저장 문서 - `runtime/commands/structured_doc_routing_commands_v1.md`..."
- unit_023 — heading_block / 5. 라우팅 표식 규칙 ~ 5. 라우팅 표식 규칙 — "## 5. 라우팅 표식 규칙..."
- unit_024 — heading_block / 5.1 최소 표식 ~ 5.1 최소 표식 — "### 5.1 최소 표식 문서 맨 위에 아래 세 줄을 허용한다. ```text [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] ``` ..."
- unit_025 — heading_block / 5.2 기본값 규칙 ~ 5.2 기본값 규칙 — "### 5.2 기본값 규칙 - `DOCROLE` 없고 애매하면 `memo` - `RUNMODE` 없으면 `ingest_only` - `PRIORITY` 없으면 `normal`..."
- unit_026 — heading_block / 5.3 사용 권장 규칙 ~ 5.3 사용 권장 규칙 — "### 5.3 사용 권장 규칙 - declaration / baseline / summary / memo -> 보통 `ingest_only` - directive -> 보통 `ingest_then_execute` -..."
- unit_027 — heading_block / 6. 처리 흐름 ~ 6. 처리 흐름 — "## 6. 처리 흐름 `문서 -> parse -> normalize -> register -> (optional ticket) -> (optional execute) -> record -> receipt -> boa..."
- unit_028 — heading_block / 7. 반드시 점검할 기록 항목 ~ 7. 반드시 점검할 기록 항목 — "## 7. 반드시 점검할 기록 항목 - `doc_registered` - `routing_normalized` - `ticket_created` (해당 시) - `execution_started` (해당 시) - `..."
- unit_029 — heading_block / 8. operation receipt 확인 항목 ~ 8. operation receipt 확인 항목 — "## 8. operation receipt 확인 항목 1. 어떤 문서를 처리했는가 2. 어떤 표식을 읽었는가 3. 어떤 canonical 값으로 정규화되었는가 4. 티켓이 생겼는가 5. 실제 실행되었는가 6. 어떤 ..."
- unit_030 — heading_block / 9. operation board 최소 섹션 ~ 9. operation board 최소 섹션 — "## 9. operation board 최소 섹션 - latest structured docs - latest tickets - latest outputs - latest events - latest receipts..."
- unit_031 — heading_block / 10. 이번 턴 비범위 ~ 10. 이번 턴 비범위 — "## 10. 이번 턴 비범위 - full web UI 구축 - 거대한 dashboard 프레임워크 설치 - 모든 문서 타입 완전 지원 - complex ontology 편집기 추가 - 자동 reclassificati..."
- unit_032 — heading_block / 11. 완료 조건 ~ 11. 완료 조건 — "## 11. 완료 조건 1. 라우팅 표식 정책 md가 생긴다. 2. 사용자용 최소 템플릿이 생긴다. 3. alias 정규화 기준 파일이 생긴다. 4. 라우팅 처리 wrapper 또는 동등한 진입점이 생긴다. 5. 문..."
- unit_033 — heading_block / 12. 보고 형식 ~ 12. 보고 형식 — "## 12. 보고 형식 - 생성/수정 파일 목록 - 테스트 문서 처리 결과 - 기록 검산 - 다음 턴 연결점..."
- unit_034 — heading_block / 13. 마지막 지시 ~ 13. 마지막 지시 — "## 13. 마지막 지시 Codex는 이번 턴에서 **구조화 문서를 “붙여 넣자마자 바로 실행되는 텍스트”가 아니라, 작은 라우팅 표식을 통해 먼저 등록/판독되고, 필요할 때만 실행되며, 그 전체 처리 결과가 단일 ..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

