# readable input board / codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935

## 1. 입력 정보
- input_id: `codex_directive_program_level_upgrade_delta_based_program_operation_v1`
- label: `codex_directive_program_level_upgrade_delta_based_program_operation_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_directive_program_level_upgrade_delta_based_program_operation_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `315`
- unit_count: `34`

## 3. unit 목록 요약
- unit_001 — heading_block / preamble ~ preamble — "[[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] [[A]] [[OBJ:program_operation_upgrade_baseline]]..."
- unit_002 — heading_block / PROGRAM-LEVEL UPGRADE BASELINE + CODEX DIRECTIVE V1 ~ PROGRAM-LEVEL UPGRADE BASELINE + CODEX DIRECTIVE V1 — "# PROGRAM-LEVEL UPGRADE BASELINE + CODEX DIRECTIVE V1..."
- unit_003 — heading_block / 주제: 전체 재스캔 중심 운용에서 변화분 중심 프로그램 운용으로 전환 ~ 주제: 전체 재스캔 중심 운용에서 변화분 중심 프로그램 운용으로 전환 — "# 주제: 전체 재스캔 중심 운용에서 변화분 중심 프로그램 운용으로 전환..."
- unit_004 — heading_block / 0. 선언 ~ 0. 선언 — "## 0. 선언 이제부터 현재 repo/workspace를 “문서와 스크립트의 묶음”이 아니라 **지속적으로 입력되고, 기록되고, 갱신되고, 확인되는 프로그램 단 운영체계**로 취급한다. 이 선언의 의미는 단순히 파..."
- unit_005 — heading_block / 1. 현재 판단 ~ 1. 현재 판단 — "## 1. 현재 판단 현재까지 잠긴 구조는 다음과 같다. - structured doc routing 안정화 - receipt / board / commands / per-run surface 정리 - provena..."
- unit_006 — heading_block / 현재 약점 ~ 현재 약점 — "### 현재 약점 - 새로운 폴더/문서/규칙이 생길 때 전체를 다시 읽는 부담이 크다 - folder_status.md류가 원장처럼 오해될 수 있다 - 변화가 append-only로 남는 구조가 폴더 단위로는 아직 ..."
- unit_007 — heading_block / 2. 최상위 기준 ~ 2. 최상위 기준 — "## 2. 최상위 기준 앞으로 폴더/규칙/문서/상태 갱신은 아래 기준을 따른다...."
- unit_008 — heading_block / 기준 1 — 전체 재스캔을 기본으로 하지 않는다 ~ 기준 1 — 전체 재스캔을 기본으로 하지 않는다 — "### 기준 1 — 전체 재스캔을 기본으로 하지 않는다 - 전체 폴더를 매번 다시 읽는 방식은 예외 상황에서만 허용한다 - 기본은 변화분 append + 국소 갱신이다..."
- unit_009 — heading_block / 기준 2 — 원장과 사람이 보는 문서를 분리한다 ~ 기준 2 — 원장과 사람이 보는 문서를 분리한다 — "### 기준 2 — 원장과 사람이 보는 문서를 분리한다 - 원장 = json/jsonl manifest/change log - 사람이 보는 문서 = md status/guide/summary - 사람이 보는 문서는 ..."
- unit_010 — heading_block / 기준 3 — 새 사실은 append-only change log에 먼저 남긴다 ~ 기준 3 — 새 사실은 append-only change log에 먼저 남긴다 — "### 기준 3 — 새 사실은 append-only change log에 먼저 남긴다 새로 생긴 폴더/문서/규칙/자산은 먼저 사건으로 기록된다. 예: - folder_created - doc_created - rul..."
- unit_011 — heading_block / 기준 4 — 현재 상태는 inventory manifest로 유지한다 ~ 기준 4 — 현재 상태는 inventory manifest로 유지한다 — "### 기준 4 — 현재 상태는 inventory manifest로 유지한다 각 폴더/영역의 현재 상태는 inventory manifest가 든다. 이 manifest는 구조적 현재 상태 스냅샷이다...."
- unit_012 — heading_block / 기준 5 — status 문서는 manifest에서 렌더한다 ~ 기준 5 — status 문서는 manifest에서 렌더한다 — "### 기준 5 — status 문서는 manifest에서 렌더한다 folder_status.md 같은 문서는 직접 원장이 아니다. inventory와 change log를 보고 다시 그리는 얇은 문서다...."
- unit_013 — heading_block / 기준 6 — 갱신 범위는 바뀐 폴더와 부모 몇 단계만 ~ 기준 6 — 갱신 범위는 바뀐 폴더와 부모 몇 단계만 — "### 기준 6 — 갱신 범위는 바뀐 폴더와 부모 몇 단계만 - 변경이 생기면 해당 폴더 inventory 갱신 - 필요시 부모 1~2단계 inventory 갱신 - 전체 repo 재빌드는 기본 금지..."
- unit_014 — heading_block / 기준 7 — 프로그램화 우선 ~ 기준 7 — 프로그램화 우선 — "### 기준 7 — 프로그램화 우선 앞으로 새 구조를 추가할 때는 “설명문 하나 더”보다 “어떤 변화가 생겼고 어디를 갱신해야 하는가”를 먼저 구조화한다. ---..."
- unit_015 — heading_block / 3. 프로그램 단 운용 구조 ~ 3. 프로그램 단 운용 구조 — "## 3. 프로그램 단 운용 구조 이제부터 아래 3층을 명확히 나눈다...."
- unit_016 — heading_block / A. 변화 이력층 (change layer) ~ A. 변화 이력층 (change layer) — "### A. 변화 이력층 (change layer) 무슨 일이 생겼는지 append-only로 기록한다. 예상 위치: - `runtime/manifests/folder_changes/folder_change_log...."
- unit_017 — heading_block / B. 현재 상태층 (inventory layer) ~ B. 현재 상태층 (inventory layer) — "### B. 현재 상태층 (inventory layer) 각 폴더/영역의 현재 상태를 구조적으로 유지한다. 예상 위치: - `runtime/manifests/folder_inventory/` 예상 파일 예: - `d..."
- unit_018 — heading_block / C. 사람용 읽기층 (status/render layer) ~ C. 사람용 읽기층 (status/render layer) — "### C. 사람용 읽기층 (status/render layer) 사람이 읽기 쉽게 보여주는 상태 문서다. 예: - `folder_status.md` - 요약 문서 - 가이드 문서 일부 상태 섹션 이 층의 역할: -..."
- unit_019 — heading_block / 4. Codex 작업 원칙 ~ 4. Codex 작업 원칙 — "## 4. Codex 작업 원칙 앞으로 Codex는 새 폴더/문서/규칙이 생길 때 아래 원칙을 따른다...."
- unit_020 — heading_block / 4.1 새 사실 발생 시 먼저 사건으로 남긴다 ~ 4.1 새 사실 발생 시 먼저 사건으로 남긴다 — "### 4.1 새 사실 발생 시 먼저 사건으로 남긴다 예: - 문서 생성 - 폴더 생성 - 규칙 추가 - 계약 문서 추가 - 운영 가이드 추가 이런 변화가 있으면 먼저 change log 관점으로 읽는다...."
- unit_021 — heading_block / 4.2 해당 영역 inventory를 갱신한다 ~ 4.2 해당 영역 inventory를 갱신한다 — "### 4.2 해당 영역 inventory를 갱신한다 예: - `docs/guides/quick_start.md` 생성 시 - `docs.guides.json` 갱신 - 필요시 `docs.json` 갱신..."
- unit_022 — heading_block / 4.3 사람용 status/render 문서를 갱신한다 ~ 4.3 사람용 status/render 문서를 갱신한다 — "### 4.3 사람용 status/render 문서를 갱신한다 필요한 범위의 folder_status.md 또는 상태 문서를 렌더한다...."
- unit_023 — heading_block / 4.4 전체 재스캔은 하지 않는다 ~ 4.4 전체 재스캔은 하지 않는다 — "### 4.4 전체 재스캔은 하지 않는다 정상 흐름에서는 바뀐 폴더와 부모만 갱신한다. ---..."
- unit_024 — heading_block / 5. Codex에게 내리는 이번 지시 ~ 5. Codex에게 내리는 이번 지시 — "## 5. Codex에게 내리는 이번 지시 이번 턴의 목적은 “변화분 중심 프로그램 운용”을 실제 작업공간 기준으로 시작하는 것이다...."
- unit_025 — heading_block / 반드시 할 일 ~ 반드시 할 일 — "### 반드시 할 일 아래를 우선 설계/생성/고정한다. #### 5.1 folder change log 레이어 추가 생성 대상 예: - `runtime/manifests/folder_changes/` - `runti..."
- unit_026 — heading_block / 6. 이번 턴에서 하지 말 것 ~ 6. 이번 턴에서 하지 말 것 — "## 6. 이번 턴에서 하지 말 것 아래는 지금 하지 않는다. - repo 전체 재구성 - 기존 모든 폴더 status 완전 재작성 - 대규모 schema generalization - 분산 시스템 수준 동기화 설계..."
- unit_027 — heading_block / 7. 최소 성공 기준 ~ 7. 최소 성공 기준 — "## 7. 최소 성공 기준 이번 턴이 성공으로 판정되려면 최소 아래를 만족해야 한다...."
- unit_028 — heading_block / required minimum ~ required minimum — "### required minimum - change log 파일/폴더가 생긴다 - folder inventory manifest 구조가 생긴다 - 특정 폴더에 대한 inventory 파일이 최소 2개 이상 생성된다..."
- unit_029 — heading_block / strong success ~ strong success — "### strong success - 새 문서 1개 추가 시 change log append 확인 - 해당 폴더 inventory만 갱신됨 - 부모 폴더 inventory가 제한 범위로 갱신됨 - 사람용 status..."
- unit_030 — heading_block / 8. 추천 테스트 시나리오 ~ 8. 추천 테스트 시나리오 — "## 8. 추천 테스트 시나리오 Codex는 아래 같은 최소 시나리오를 돌려 확인한다...."
- unit_031 — heading_block / 시나리오 A — guides 문서 추가 ~ 시나리오 A — guides 문서 추가 — "### 시나리오 A — guides 문서 추가 - `docs/guides/` 아래 새 문서 생성 - change log에 `doc_created` append - `docs.guides.json` 갱신 - 필요시 `..."
- unit_032 — heading_block / 시나리오 B — gemini observer 문서 추가 ~ 시나리오 B — gemini observer 문서 추가 — "### 시나리오 B — gemini observer 문서 추가 - `runtime/observer/gemini/` 아래 새 session 로그 생성 - change log append - `runtime.observ..."
- unit_033 — heading_block / 9. 운영 철학 잠금 ~ 9. 운영 철학 잠금 — "## 9. 운영 철학 잠금 이 기준은 단순히 파일 정리 편의를 위한 것이 아니다. 앞으로 우리는 다음 관점으로 간다. - 작업공간은 누적되는 프로그램이다 - 변화는 사건으로 기록된다 - 현재 상태는 구조적 inven..."
- unit_034 — heading_block / 10. 최종 잠금 문장 ~ 10. 최종 잠금 문장 — "## 10. 최종 잠금 문장 가장 중요한 문장은 아래다. **전체를 매번 다시 읽지 말고, 변화는 append하고, 현재 상태는 inventory로 유지하며, 사람이 보는 상태 문서는 그 결과를 얇게 렌더하라.** ..."

## 4. 당장 읽히는 흐름
- 입력은 중간 단위 block으로 나뉘었고, 앞/중간/뒤 흐름을 빠르게 재확인하기 좋은 분해다.

