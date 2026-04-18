# readable input board / codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719

## 1. 입력 정보
- input_id: `codex_baseline_session_id_and_gemini_log_link_contract_v1`
- label: `codex_baseline_session_id_and_gemini_log_link_contract_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_baseline_session_id_and_gemini_log_link_contract_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `378`
- unit_count: `43`

## 3. unit 목록 요약
- unit_001 — heading_block / preamble ~ preamble — "[[DOCROLE:baseline]] [[RUNMODE:ingest_only]] [[PRIORITY:high]] [[A]] [[OBJ:baseline_document]] [[SEM:session_id_and_gemi..."
- unit_002 — heading_block / CODEX BASELINE — SESSION ID RULE + GEMINI OBSERVER LOG LINK CONTRACT V1 ~ CODEX BASELINE — SESSION ID RULE + GEMINI OBSERVER LOG LINK CONTRACT V1 — "# CODEX BASELINE — SESSION ID RULE + GEMINI OBSERVER LOG LINK CONTRACT V1..."
- unit_003 — heading_block / 0. 목적 ~ 0. 목적 — "## 0. 목적 이 기준문의 목적은 현재 잠겨 있는 Codex ↔ Gemini 세션 배치 운영 계약 위에 아래 두 가지를 추가로 고정하는 것이다. 1. session_id 규칙 2. Gemini observer 로그..."
- unit_004 — heading_block / 1. 현재 전제 ~ 1. 현재 전제 — "## 1. 현재 전제 이미 잠겨 있는 기준은 다음과 같다. - Codex = 앞단 실행 주체 - Gemini = 세션 종료 시 한 번 호출되는 후단 판독기 - Gemini 출력 저장 위치 = `runtime/obse..."
- unit_005 — heading_block / 2. session_id의 필요성 ~ 2. session_id의 필요성 — "## 2. session_id의 필요성 session_id는 단순 이름표가 아니다. session_id는 아래를 가능하게 한다. - 여러 Codex 실행을 하나의 작업 세션으로 묶기 - 세션 종료 후 Gemini 판..."
- unit_006 — heading_block / 3. 식별자 역할 분리 ~ 3. 식별자 역할 분리 — "## 3. 식별자 역할 분리 아래 역할 분리를 절대 기준으로 고정한다...."
- unit_007 — heading_block / run_id ~ run_id — "### run_id - 개별 실행 단위 식별자 - routing 실행 / Codex 실행 / receipt / per-run artifact와 연결됨 - 이미 존재하는 실행 추적 단위..."
- unit_008 — heading_block / session_id ~ session_id — "### session_id - 여러 run_id를 묶는 상위 작업 세션 식별자 - Gemini batch review 단위 - 사용자가 “이번 작업 흐름”으로 인식하는 단위 즉: - run_id = 점 - sessi..."
- unit_009 — heading_block / 4. session_id 규칙 (LOCK) ~ 4. session_id 규칙 (LOCK) — "## 4. session_id 규칙 (LOCK)..."
- unit_010 — heading_block / 4.1 기본 형식 ~ 4.1 기본 형식 — "### 4.1 기본 형식 session_id는 아래 형식으로 생성한다. `session_YYYYMMDD_NN` 예시: - `session_20260325_01` - `session_20260325_02` - `ses..."
- unit_011 — heading_block / 4.2 생성 원칙 ~ 4.2 생성 원칙 — "### 4.2 생성 원칙 - 날짜 기준으로 관리한다 - 같은 날 여러 세션이 있으면 2자리 순번을 붙인다 - 사람이 읽고 바로 이해 가능해야 한다 - 지나치게 긴 uuid형 session_id는 기본값으로 쓰지 않는..."
- unit_012 — heading_block / 4.3 의미 ~ 4.3 의미 — "### 4.3 의미 - session_id 하나는 “작업 묶음 하나”를 의미한다 - 너무 넓게 잡지 않는다 - 하루 전체를 무조건 한 세션으로 보지 않는다 - 의미 있는 작업 묶음 단위로 자른다 권장 예: - 기능 ..."
- unit_013 — heading_block / 5. session_id 적용 범위 ~ 5. session_id 적용 범위 — "## 5. session_id 적용 범위 session_id는 아래에 연결될 수 있어야 한다...."
- unit_014 — heading_block / 직접 포함 대상 ~ 직접 포함 대상 — "### 직접 포함 대상 - Gemini observer 로그 - session summary 문서 - session review 문서 - 필요시 Codex handoff 문서..."
- unit_015 — heading_block / 참조 포함 대상 ~ 참조 포함 대상 — "### 참조 포함 대상 - 관련 run_id 목록 - latest board / per-run board 참조 - receipt 참조 - provenance compacted latest 참조 중요: **sessio..."
- unit_016 — heading_block / 6. Gemini 로그 저장 구조 (LOCK) ~ 6. Gemini 로그 저장 구조 (LOCK) — "## 6. Gemini 로그 저장 구조 (LOCK)..."
- unit_017 — heading_block / 6.1 기본 저장 위치 ~ 6.1 기본 저장 위치 — "### 6.1 기본 저장 위치 Gemini 출력은 반드시 아래에 저장한다. `runtime/observer/gemini/`..."
- unit_018 — heading_block / 6.2 권장 폴더 구조 ~ 6.2 권장 폴더 구조 — "### 6.2 권장 폴더 구조 권장 구조는 아래와 같다. `runtime/observer/gemini/YYYY-MM-DD/` 예시: - `runtime/observer/gemini/2026-03-25/` - `run..."
- unit_019 — heading_block / 6.3 권장 파일 ~ 6.3 권장 파일 — "### 6.3 권장 파일 세션 단위 저장 기본 파일 예시는 아래와 같다. - `session_review_001.md` - `session_pointer_check_001.md` - `session_diff_revi..."
- unit_020 — heading_block / 7. Gemini 로그 필수 context 구조 (LOCK) ~ 7. Gemini 로그 필수 context 구조 (LOCK) — "## 7. Gemini 로그 필수 context 구조 (LOCK) 모든 Gemini observer 로그는 아래 context를 반드시 포함한다. ```md..."
- unit_021 — heading_block / context ~ context — "## context - session_id: - related_runs: - related_receipts: - related_boards: - input_scope: - command: - timestamp: ``..."
- unit_022 — heading_block / 필드 의미 ~ 필드 의미 — "### 필드 의미 - `session_id`: 이 로그가 속한 작업 세션 - `related_runs`: 이 세션에서 참고한 run_id 목록 - `related_receipts`: 참조한 receipt 경로 또는 ..."
- unit_023 — heading_block / 8. Codex ↔ Gemini 연결 방식 (LOCK) ~ 8. Codex ↔ Gemini 연결 방식 (LOCK) — "## 8. Codex ↔ Gemini 연결 방식 (LOCK)..."
- unit_024 — heading_block / 8.1 현재 연결 원칙 ~ 8.1 현재 연결 원칙 — "### 8.1 현재 연결 원칙 현재 구조에서 Codex와 Gemini는 자동 연결되지 않는다. 현재 연결 방식은 아래로 고정한다. 1. Codex가 여러 run을 실행한다 2. 결과가 runtime에 누적된다 3. ..."
- unit_025 — heading_block / 8.2 연결의 핵심 ~ 8.2 연결의 핵심 — "### 8.2 연결의 핵심 - Codex는 현실을 만든다 - Gemini는 그 현실을 나중에 읽는다 - session_id는 그 둘을 사람 기준의 흐름으로 묶는다 ---..."
- unit_026 — heading_block / 9. session 단위 입력 묶음 규칙 ~ 9. session 단위 입력 묶음 규칙 — "## 9. session 단위 입력 묶음 규칙 Gemini는 session_id를 기준으로 아래 유형의 입력 묶음을 받을 수 있다...."
- unit_027 — heading_block / A. 상태 요약 세션 ~ A. 상태 요약 세션 — "### A. 상태 요약 세션 입력 예: - latest board - provenance compacted latest - 최근 receipt 일부 - 관련 per-run board 일부 출력: - session r..."
- unit_028 — heading_block / B. 구조 점검 세션 ~ B. 구조 점검 세션 — "### B. 구조 점검 세션 입력 예: - latest board - latest commands - 관련 per-run board / commands - pointer 관련 파일 출력: - session point..."
- unit_029 — heading_block / C. 변경 리뷰 세션 ~ C. 변경 리뷰 세션 — "### C. 변경 리뷰 세션 입력 예: - git diff - changed files - 관련 receipt / board - 필요시 관련 정책/계약 문서 출력: - session diff review 즉 sess..."
- unit_030 — heading_block / 10. latest와 session의 관계 ~ 10. latest와 session의 관계 — "## 10. latest와 session의 관계 latest는 현재 대표 상태를 가리킨다. session은 작업 흐름 묶음을 가리킨다. 둘의 관계는 아래와 같다. - latest = 가장 최근 상태 포인터 - per..."
- unit_031 — heading_block / 11. append-only 규칙 ~ 11. append-only 규칙 — "## 11. append-only 규칙 Gemini observer 로그에도 append-only 감각을 유지한다...."
- unit_032 — heading_block / 규칙 ~ 규칙 — "### 규칙 - 기존 session 로그 overwrite 금지 - 수정이 필요하면 새 로그를 추가하거나 revision을 남긴다 - latest 성격의 파일이 필요하면 별도 유지 가능하나 원본 로그는 남긴다 예: ..."
- unit_033 — heading_block / 12. 하지 말아야 할 것 ~ 12. 하지 말아야 할 것 — "## 12. 하지 말아야 할 것 아래는 금지한다...."
- unit_034 — heading_block / 금지 1 ~ 금지 1 — "### 금지 1 session_id를 engine core state처럼 사용하지 말 것..."
- unit_035 — heading_block / 금지 2 ~ 금지 2 — "### 금지 2 Gemini observer 로그를 provenance / registry / event로 혼입하지 말 것..."
- unit_036 — heading_block / 금지 3 ~ 금지 3 — "### 금지 3 run_id를 없애고 session_id만 남기는 식으로 단순화하지 말 것..."
- unit_037 — heading_block / 금지 4 ~ 금지 4 — "### 금지 4 1실행마다 무조건 새 session_id를 발급하지 말 것..."
- unit_038 — heading_block / 금지 5 ~ 금지 5 — "### 금지 5 며칠치 전혀 다른 작업을 하나의 session_id로 뭉개지 말 것 ---..."
- unit_039 — heading_block / 13. 향후 확장 경로 (PRE-DEFINED) ~ 13. 향후 확장 경로 (PRE-DEFINED) — "## 13. 향후 확장 경로 (PRE-DEFINED) 운영화면이 생기면 아래 확장이 가능하다...."
- unit_040 — heading_block / 현재 ~ 현재 — "### 현재 - 사용자가 Codex 실행 - 세션 종료 시 Gemini 호출 - observer 로그 저장..."
- unit_041 — heading_block / 추후 ~ 추후 — "### 추후 - 입력 페이지에서 session 시작 - Codex 실행 결과가 session에 자동 연결 - Gemini batch review가 같은 session에 연결 - 운영화면에서 session 단위로 확인..."
- unit_042 — heading_block / 14. 성공 기준 ~ 14. 성공 기준 — "## 14. 성공 기준 이 기준문이 올바르게 학습되면 아래가 가능해야 한다. - Codex와 Gemini 모두 run_id와 session_id를 구분해서 이해한다 - Gemini 로그는 반드시 `runtime/ob..."
- unit_043 — heading_block / 15. 최종 잠금 ~ 15. 최종 잠금 — "## 15. 최종 잠금 현재 구조에서 가장 중요한 문장은 아래다. **Codex는 run을 만든다. Gemini는 session을 읽는다.** 그리고 저장 규칙은 아래다. **Gemini observer 로그는 `r..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

