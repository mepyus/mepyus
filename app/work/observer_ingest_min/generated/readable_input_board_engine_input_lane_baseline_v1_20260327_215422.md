# readable input board / engine_input_lane_baseline_v1_20260327_215422

## 1. 입력 정보
- input_id: `engine_input_lane_baseline_v1`
- label: `engine_input_lane_baseline_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/policies/engine_input_lane_baseline_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `335`
- unit_count: `46`

## 3. unit 목록 요약
- unit_001 — heading_block / engine_input_lane_baseline_v1 ~ engine_input_lane_baseline_v1 — "# engine_input_lane_baseline_v1..."
- unit_002 — heading_block / 0. 목적 ~ 0. 목적 — "## 0. 목적 이 문서는 엔진으로 들어오는 입력의 종류가 늘어나더라도 입력 혼잡과 중심 오염을 막기 위해 사용하는 **단일 intake 기준문(SSOT)** 이다. 핵심 목적은 3개다. 1. 입력이 늘어나도 혼잡해..."
- unit_003 — heading_block / 1. 최상위 원칙 ~ 1. 최상위 원칙 — "## 1. 최상위 원칙..."
- unit_004 — heading_block / 1-1. 입력은 늘어나도 된다 ~ 1-1. 입력은 늘어나도 된다 — "### 1-1. 입력은 늘어나도 된다 외부자료, 표준문서, 일반메모, 대화, 산출물, 툴 출력 등 입력 종류가 늘어나는 것 자체는 문제로 보지 않는다...."
- unit_005 — heading_block / 1-2. 중심 규칙은 느리게만 늘어난다 ~ 1-2. 중심 규칙은 느리게만 늘어난다 — "### 1-2. 중심 규칙은 느리게만 늘어난다 입력 레인이 늘어나는 것과 core 규칙이 늘어나는 것은 같은 일이 아니다. 입력문은 여러 개여도 괜찮지만 중심 규칙 승격은 매우 보수적으로 다룬다...."
- unit_006 — heading_block / 1-3. 입력자는 완벽히 분류할 필요가 없다 ~ 1-3. 입력자는 완벽히 분류할 필요가 없다 — "### 1-3. 입력자는 완벽히 분류할 필요가 없다 사용자가 명확히 알면 lane 힌트를 붙여준다. 애매하면 미분류로 넣을 수 있어야 한다. 즉 기본 원칙은 이거다. - 알면 붙인다 - 애매하면 미분류로 넣는다 - ..."
- unit_007 — heading_block / 1-4. 원본이 먼저다 ~ 1-4. 원본이 먼저다 — "### 1-4. 원본이 먼저다 사용자 해석, 요약, 평가보다 원본 source가 먼저 보존되어야 한다. 특히 외부자료는 canonical source를 먼저 고정한다...."
- unit_008 — heading_block / 1-5. 입력 레인과 중심 승격을 분리한다 ~ 1-5. 입력 레인과 중심 승격을 분리한다 — "### 1-5. 입력 레인과 중심 승격을 분리한다 어떤 입력이 들어왔다는 사실만으로 그 입력이 core 후보가 되는 것은 아니다. 입력 수용과 구조 승격은 별개의 단계다...."
- unit_009 — heading_block / 2. 현재 intake lane 정의 ~ 2. 현재 intake lane 정의 — "## 2. 현재 intake lane 정의 현재 엔진은 입력 구조가 여러 개로 분열된 것이 아니라 **성격이 다른 재료를 받기 위한 입력 레인(lane)이 여러 개 있는 상태**로 본다. 기본 lane은 아래 6개로..."
- unit_010 — heading_block / 3. lane 목록 ~ 3. lane 목록 — "## 3. lane 목록..."
- unit_011 — heading_block / L1. 선언문 (declaration) ~ L1. 선언문 (declaration) — "### L1. 선언문 (declaration) 정의: - 방향 선언 - 존재 이유 선언 - 태도 선언 - “무엇을 위해 이 구조를 두는가”를 밝히는 문서 예시: - 선언문 - 철학 선언 - 운용 의도 선언 - 엔진 ..."
- unit_012 — heading_block / L2. 기준문 (baseline) ~ L2. 기준문 (baseline) — "### L2. 기준문 (baseline) 정의: - 반복 운용 시 흔들리지 않게 붙잡는 고정 기준 - 앞으로 판단의 축으로 삼을 문서 예시: - 잠금 기준 - 구조 기준 - 운영 기준 - 승격/보류/분리 원칙 - “..."
- unit_013 — heading_block / L3. 지시문 (directive) ~ L3. 지시문 (directive) — "### L3. 지시문 (directive) 정의: - 사람 또는 Codex/CLI/후속 프로세스가 실제로 따라야 하는 실행 지시 - 작업 단위, 목적, 범위, 금지사항, 산출물 형식 등을 담는 문서 예시: - Cod..."
- unit_014 — heading_block / L4. 외부입력자료 (external_input) ~ L4. 외부입력자료 (external_input) — "### L4. 외부입력자료 (external_input) 정의: - 외부에서 가져온 원문 사례, 전사본, 기사, 강연, 문서, 인터뷰, 보고서 등 - 엔진 밖에서 생성된 원본 재료 예시: - `saltlux.txt`..."
- unit_015 — heading_block / L5. 일반입력 (general_input) ~ L5. 일반입력 (general_input) — "### L5. 일반입력 (general_input) 정의: - 아직 문서 성격이 고정되지 않은 재료 - 생각 메모, 대화, 단상, 현장 메모, 중간 정리, 방향 스케치 등 예시: - 짧은 아이디어 - 작업 중 생각 ..."
- unit_016 — heading_block / L6. 미분류 (unclassified) ~ L6. 미분류 (unclassified) — "### L6. 미분류 (unclassified) 정의: - 사용자가 lane을 확정하지 못했거나 - 하나로 단정하기 애매하거나 - 복합 성격이 섞여 있는 입력 예시: - 지시문 같기도 하고 기준문 같기도 한 초안 -..."
- unit_017 — heading_block / 4. 사용자 입력 규칙 ~ 4. 사용자 입력 규칙 — "## 4. 사용자 입력 규칙 사용자는 매 입력마다 완벽한 분류를 할 필요가 없다...."
- unit_018 — heading_block / 4-1. 최선 ~ 4-1. 최선 — "### 4-1. 최선 사용자가 아래 중 하나의 prefix를 붙여준다. - [선언문] - [기준문] - [지시문] - [외부자료] - [일반입력] - [미분류]..."
- unit_019 — heading_block / 4-2. 차선 ~ 4-2. 차선 — "### 4-2. 차선 prefix 없이 넣되, 한 줄로 의도만 알려준다. 예: - “이건 외부 사례 원문” - “이건 실행 지시 초안” - “이건 아직 정리 안 된 생각” - “이건 기준으로 잠그고 싶은 문장”..."
- unit_020 — heading_block / 4-3. 허용 ~ 4-3. 허용 — "### 4-3. 허용 아무 표시 없이 raw로 넣어도 된다. 다만 이 경우 엔진은 기본적으로 general_input 또는 unclassified로 먼저 본다...."
- unit_021 — heading_block / 5. intake 처리 순서 ~ 5. intake 처리 순서 — "## 5. intake 처리 순서 모든 입력은 아래 순서로 본다. 1. source 존재 확인 2. lane 힌트 존재 확인 3. 원문/해석 분리 가능 여부 확인 4. 우선 intake class 부여 5. rece..."
- unit_022 — heading_block / 6. lane 간 우선 판단 규칙 ~ 6. lane 간 우선 판단 규칙 — "## 6. lane 간 우선 판단 규칙 애매할 때는 아래 기준으로 본다...."
- unit_023 — heading_block / 6-1. 실행 행위가 분명하면 directive 우선 후보 ~ 6-1. 실행 행위가 분명하면 directive 우선 후보 — "### 6-1. 실행 행위가 분명하면 directive 우선 후보 “무엇을 하라”가 명확하면 directive 후보로 본다...."
- unit_024 — heading_block / 6-2. 반복 판단 기준을 잠그면 baseline 우선 후보 ~ 6-2. 반복 판단 기준을 잠그면 baseline 우선 후보 — "### 6-2. 반복 판단 기준을 잠그면 baseline 우선 후보 앞으로의 판단축을 고정하는 문장이면 baseline 후보로 본다...."
- unit_025 — heading_block / 6-3. 존재 이유/방향 선언이면 declaration 우선 후보 ~ 6-3. 존재 이유/방향 선언이면 declaration 우선 후보 — "### 6-3. 존재 이유/방향 선언이면 declaration 우선 후보 실행보다 존재 이유와 방향성이 중심이면 declaration 후보로 본다...."
- unit_026 — heading_block / 6-4. 외부 원문이면 external_input 우선 ~ 6-4. 외부 원문이면 external_input 우선 — "### 6-4. 외부 원문이면 external_input 우선 외부에서 온 원문/전사/기사/강연은 external_input 우선이다...."
- unit_027 — heading_block / 6-5. 어느 쪽도 확실치 않으면 unclassified ~ 6-5. 어느 쪽도 확실치 않으면 unclassified — "### 6-5. 어느 쪽도 확실치 않으면 unclassified 억지로 고르지 않는다...."
- unit_028 — heading_block / 7. 외부자료 특별 규칙 ~ 7. 외부자료 특별 규칙 — "## 7. 외부자료 특별 규칙 외부자료는 별도 주의가 필요하다...."
- unit_029 — heading_block / 7-1. canonical source 우선 ~ 7-1. canonical source 우선 — "### 7-1. canonical source 우선 요약본보다 원본 파일을 먼저 고정한다...."
- unit_030 — heading_block / 7-2. 바로 core로 올리지 않는다 ~ 7-2. 바로 core로 올리지 않는다 — "### 7-2. 바로 core로 올리지 않는다 외부자료는 구조 힌트를 줄 수 있지만 처음부터 중심 규칙으로 채택하지 않는다...."
- unit_031 — heading_block / 7-3. first-pass 분리 판독을 원칙으로 한다 ~ 7-3. first-pass 분리 판독을 원칙으로 한다 — "### 7-3. first-pass 분리 판독을 원칙으로 한다 기본 판독 슬롯: - core_candidate - outer_candidate - defer - observer_only..."
- unit_032 — heading_block / 7-4. 반복성이 보이기 전에는 refinement만 열고 core promotion은 보류한다 ~ 7-4. 반복성이 보이기 전에는 refinement만 열고 core promotion은 보류한다 — "### 7-4. 반복성이 보이기 전에는 refinement만 열고 core promotion은 보류한다 외부자료는 특히 벤더 수사, 마케팅 문장, 포지셔닝 문장이 섞일 수 있으므로 반복 구조가 보일 때까지 보수적으로..."
- unit_033 — heading_block / 8. 혼잡 방지 규칙 ~ 8. 혼잡 방지 규칙 — "## 8. 혼잡 방지 규칙..."
- unit_034 — heading_block / 8-1. 입력문은 넓게, 중심문은 좁게 ~ 8-1. 입력문은 넓게, 중심문은 좁게 — "### 8-1. 입력문은 넓게, 중심문은 좁게 입력은 자유롭게 받되 core로 가는 문은 아주 좁게 유지한다...."
- unit_035 — heading_block / 8-2. intake expansion과 ontology expansion을 혼동하지 않는다 ~ 8-2. intake expansion과 ontology expansion을 혼동하지 않는다 — "### 8-2. intake expansion과 ontology expansion을 혼동하지 않는다 입력 lane이 하나 늘었다고 엔진 존재 구조 자체가 바뀐 것은 아니다...."
- unit_036 — heading_block / 8-3. 미분류를 허용한다 ~ 8-3. 미분류를 허용한다 — "### 8-3. 미분류를 허용한다 혼잡의 큰 원인은 미분류가 아니라 **억지 조기 분류**다...."
- unit_037 — heading_block / 8-4. 정련은 한 번에 한 축만 연다 ~ 8-4. 정련은 한 번에 한 축만 연다 — "### 8-4. 정련은 한 번에 한 축만 연다 여러 refinement 축을 동시에 열면 판독 혼탁이 커진다...."
- unit_038 — heading_block / 8-5. 원본과 해석을 가능하면 분리 저장한다 ~ 8-5. 원본과 해석을 가능하면 분리 저장한다 — "### 8-5. 원본과 해석을 가능하면 분리 저장한다 특히 external_input과 user_summary가 섞일 때 주의한다...."
- unit_039 — heading_block / 9. 새로운 lane 추가 규칙 ~ 9. 새로운 lane 추가 규칙 — "## 9. 새로운 lane 추가 규칙 입력이 늘어날 수는 있다. 하지만 새 lane 추가는 아래 조건을 만족할 때만 한다...."
- unit_040 — heading_block / 새 lane 추가 조건 ~ 새 lane 추가 조건 — "### 새 lane 추가 조건 1. 기존 6개 lane으로 반복적으로 수용이 어렵다 2. 단순 하위 예시가 아니라 실제 처리 규칙이 다르다 3. provenance / routing / 판독 방식 차이가 분명하다 4..."
- unit_041 — heading_block / 추가 원칙 ~ 추가 원칙 — "### 추가 원칙 - 새 lane을 만들기 전 먼저 기존 lane의 subtype으로 흡수 가능한지 본다 - 새 lane을 만들면 이 문서에만 추가한다 - 다른 문서에 제각각 추가 정의를 흩뿌리지 않는다 즉 새 입력..."
- unit_042 — heading_block / 10. 변경 기록 규칙 ~ 10. 변경 기록 규칙 — "## 10. 변경 기록 규칙 이 문서는 단일 SSOT로 유지한다. 새로운 입력 유형이나 판독 기준 변경이 생기면 아래 changelog에 누적 기록한다...."
- unit_043 — heading_block / 11. 추천 사용자 prefix 표준 ~ 11. 추천 사용자 prefix 표준 — "## 11. 추천 사용자 prefix 표준 실사용 prefix는 아래 6개를 권장한다. - [선언문] - [기준문] - [지시문] - [외부자료] - [일반입력] - [미분류] 권장 운영 문장: - lane을 알면 ..."
- unit_044 — heading_block / 12. 최종 잠금 ~ 12. 최종 잠금 — "## 12. 최종 잠금 이 엔진은 입력이 늘어나는 것을 문제로 보지 않는다. 문제는 입력이 기준 없이 바로 중심으로 섞이는 것이다. 따라서 intake 운영의 핵심은 아래 한 문장으로 잠근다. **입력은 자유롭게 확..."
- unit_045 — heading_block / 13. changelog ~ 13. changelog — "## 13. changelog..."
- unit_046 — heading_block / v1 ~ v1 — "### v1 - declaration / baseline / directive / external_input / general_input / unclassified 6-lane 고정 - 사용자 완전 사전분류 의무 없..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

