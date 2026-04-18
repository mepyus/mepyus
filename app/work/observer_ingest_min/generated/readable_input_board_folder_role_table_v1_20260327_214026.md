# readable input board / folder_role_table_v1_20260327_214026

## 1. 입력 정보
- input_id: `folder_role_table_v1`
- label: `folder_role_table_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `179`
- unit_count: `30`

## 3. unit 목록 요약
- unit_001 — heading_block / folder_role_table_v1 ~ folder_role_table_v1 — "# folder_role_table_v1..."
- unit_002 — heading_block / 0. 목적 ~ 0. 목적 — "## 0. 목적 이 문서는 프로그램급 작업공간으로 승격하는 과정에서 각 폴더가 무엇을 담당하는지, 무엇을 두면 안 되는지, 새 파일이 생겼을 때 어디로 배치해야 하는지를 빠르게 판단하기 위한 **폴더 역할표 v1**..."
- unit_003 — heading_block / 1. 최상위 폴더 읽기 ~ 1. 최상위 폴더 읽기 — "## 1. 최상위 폴더 읽기 | 폴더 | 역할 | 여기에 들어오는 것 | 들어오면 안 되는 것 | 한 줄 판단 | |---|---|---|---|---| | `app/` | 엔진 본체 | core logic, run..."
- unit_004 — heading_block / 2. app/ 하위 역할 ~ 2. app/ 하위 역할 — "## 2. app/ 하위 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 비고 | |---|---|---|---|---| | `app/core/` | 핵심 구조/핵심 계약 | schema, regi..."
- unit_005 — heading_block / 3. scripts/ 하위 역할 ~ 3. scripts/ 하위 역할 — "## 3. scripts/ 하위 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 | |---|---|---|---|---| | `scripts/intake/` | 입력 수용 실행 | p..."
- unit_006 — heading_block / 4. docs/ 하위 역할 ~ 4. docs/ 하위 역할 — "## 4. docs/ 하위 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 비고 | |---|---|---|---|---| | `docs/policies/` | 상위 운영 기준 | baseline,..."
- unit_007 — heading_block / 5. runtime/ 하위 역할 ~ 5. runtime/ 하위 역할 — "## 5. runtime/ 하위 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 | |---|---|---|---|---| | `runtime/views/` | 사람이 읽는 최신 요약면..."
- unit_008 — heading_block / 6. input/sources 계열 역할 ~ 6. input/sources 계열 역할 — "## 6. input/sources 계열 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 | |---|---|---|---|---| | `input/external/` | 외부 원문 자..."
- unit_009 — heading_block / 7. references/ 하위 역할 ~ 7. references/ 하위 역할 — "## 7. references/ 하위 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 한 줄 판단 | |---|---|---|---|---| | `references/calibration/` | 보..."
- unit_010 — heading_block / 8. work/ 또는 app/work/ 하위 역할 ~ 8. work/ 또는 app/work/ 하위 역할 — "## 8. work/ 또는 app/work/ 하위 역할 | 경로 | 역할 | 둬야 하는 것 | 두면 안 되는 것 | 원칙 | |---|---|---|---|---| | `work/experiments/` | 실험 묶..."
- unit_011 — heading_block / 9. 파일 배치 빠른 판단표 ~ 9. 파일 배치 빠른 판단표 — "## 9. 파일 배치 빠른 판단표..."
- unit_012 — heading_block / 9-1. 이 파일이 원문인가 ~ 9-1. 이 파일이 원문인가 — "### 9-1. 이 파일이 원문인가 그렇다면 `input/` 또는 `sources/` 계열로 간다...."
- unit_013 — heading_block / 9-2. 이 파일이 엔진이 실제로 사용하는 코드인가 ~ 9-2. 이 파일이 엔진이 실제로 사용하는 코드인가 — "### 9-2. 이 파일이 엔진이 실제로 사용하는 코드인가 그렇다면 `app/` 또는 `scripts/` 로 간다...."
- unit_014 — heading_block / 9-3. 이 파일이 상위 규칙/지침/기준인가 ~ 9-3. 이 파일이 상위 규칙/지침/기준인가 — "### 9-3. 이 파일이 상위 규칙/지침/기준인가 그렇다면 `docs/policies`, `docs/directives`, `docs/declarations`, `docs/specs` 중 하나로 간다...."
- unit_015 — heading_block / 9-4. 이 파일이 사람이 빠르게 읽는 최신 상태면인가 ~ 9-4. 이 파일이 사람이 빠르게 읽는 최신 상태면인가 — "### 9-4. 이 파일이 사람이 빠르게 읽는 최신 상태면인가 그렇다면 `runtime/views` 또는 `runtime/rendered` 로 간다...."
- unit_016 — heading_block / 9-5. 이 파일이 추적 기록인가 ~ 9-5. 이 파일이 추적 기록인가 — "### 9-5. 이 파일이 추적 기록인가 그렇다면 `runtime/receipts`, `logs/`, 또는 registry/provenance/event 계열로 간다...."
- unit_017 — heading_block / 9-6. 이 파일이 아직 실험 중인가 ~ 9-6. 이 파일이 아직 실험 중인가 — "### 9-6. 이 파일이 아직 실험 중인가 그렇다면 `work/` 또는 `app/work/` 로 간다...."
- unit_018 — heading_block / 10. 새 폴더 생성 전 체크 ~ 10. 새 폴더 생성 전 체크 — "## 10. 새 폴더 생성 전 체크 새 폴더를 만들기 전에 아래를 순서대로 본다. 1. 기존 폴더 역할 안에 들어갈 수 없는가 2. 반복적으로 같은 유형이 발생하는가 3. 단순 편의가 아니라 책임이 분리되는가 4. ..."
- unit_019 — heading_block / 11. 폴더 운영 금지선 ~ 11. 폴더 운영 금지선 — "## 11. 폴더 운영 금지선..."
- unit_020 — heading_block / 금지 1 ~ 금지 1 — "### 금지 1 원본, latest, 실험본을 한 폴더에 섞지 않는다...."
- unit_021 — heading_block / 금지 2 ~ 금지 2 — "### 금지 2 비슷한 정책 문서를 여러 폴더에 중복 생성하지 않는다...."
- unit_022 — heading_block / 금지 3 ~ 금지 3 — "### 금지 3 일회성 스크립트를 장기 운영 스크립트 폴더에 오래 방치하지 않는다...."
- unit_023 — heading_block / 금지 4 ~ 금지 4 — "### 금지 4 runtime latest를 원본 보관 위치처럼 쓰지 않는다...."
- unit_024 — heading_block / 금지 5 ~ 금지 5 — "### 금지 5 work 산출물을 lock된 기준 자산처럼 취급하지 않는다...."
- unit_025 — heading_block / 12. 현재 추천 SSOT 문서 배치 ~ 12. 현재 추천 SSOT 문서 배치 — "## 12. 현재 추천 SSOT 문서 배치..."
- unit_026 — heading_block / 정책 ~ 정책 — "### 정책 - `docs/policies/engine_input_lane_baseline_v1.md` - `docs/policies/codex_baseline_program_grade_workspace_upgrad..."
- unit_027 — heading_block / 지시 ~ 지시 — "### 지시 - `docs/directives/...`..."
- unit_028 — heading_block / 선언 ~ 선언 — "### 선언 - `docs/declarations/...`..."
- unit_029 — heading_block / 명세 ~ 명세 — "### 명세 - `docs/specs/folder_role_table_v1.md` 즉 이 문서 자체는 `docs/specs/folder_role_table_v1.md` 에 둔다. 현재 맥락상 이 문서는 **역할 명세..."
- unit_030 — heading_block / 13. 최종 잠금 ~ 13. 최종 잠금 — "## 13. 최종 잠금 폴더는 단순 저장통이 아니다. 폴더는 역할과 책임 경계를 고정하는 구조 단위다. 따라서 앞으로 새 입력, 새 문서, 새 스크립트, 새 산출물이 생길 때마다 먼저 “무엇을 만들까”보다 **“이 ..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

