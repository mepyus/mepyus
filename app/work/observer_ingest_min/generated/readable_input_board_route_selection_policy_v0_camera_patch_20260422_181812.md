# readable input board / route_selection_policy_v0_camera_patch_20260422_181812

## 1. 입력 정보
- input_id: `route_selection_policy_v0_camera_patch`
- label: `route_selection_policy_v0_camera_patch`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reviews/route_selection_policy_v0.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `201`
- unit_count: `33`

## 3. unit 목록 요약
- unit_001 — heading_block / Route Selection Policy v0 ~ Route Selection Policy v0 — "# Route Selection Policy v0..."
- unit_002 — heading_block / 목적 ~ 목적 — "## 목적 이 문서는 [route_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/route_registry_v0.jso..."
- unit_003 — heading_block / selection 기본 원칙 ~ selection 기본 원칙 — "## selection 기본 원칙..."
- unit_004 — heading_block / 1. family first ~ 1. family first — "### 1. family first 먼저 family를 고른다. route는 그 다음이다. 즉 순서는 아래다. 1. 현재 issue/root signal이 어느 family에 속하는가 2. 그 family 안에서 어..."
- unit_005 — heading_block / 2. narrower route wins ~ 2. narrower route wins — "### 2. narrower route wins 같은 family 안에서 둘 다 열릴 수 있으면, 더 좁고 더 특수한 route를 먼저 쓴다. 이유: - broad route를 먼저 열면 residue가 평평해진다 ..."
- unit_006 — heading_block / 3. preservation before collapse ~ 3. preservation before collapse — "### 3. preservation before collapse input과 transition 계열에서는 먼저 보존성이 높은 route를 고른다. 예: - 무작정 closure보다 reread - 무작정 direc..."
- unit_007 — heading_block / 4. operator clarity before cleverness ~ 4. operator clarity before cleverness — "### 4. operator clarity before cleverness readout 계열에서는 먼저 operator가 가장 빨리 이해할 수 있는 route를 연다. 예: - broad state overview..."
- unit_008 — heading_block / family별 v0 정책 ~ family별 v0 정책 — "## family별 v0 정책..."
- unit_009 — heading_block / 1. fam_input_to_reading ~ 1. fam_input_to_reading — "## 1. fam_input_to_reading..."
- unit_010 — heading_block / candidate routes ~ candidate routes — "### candidate routes - `route_input_direct_ingest` - `route_preprocess_compare_first`..."
- unit_011 — heading_block / selection rule ~ selection rule — "### selection rule 기본 우선순위는 아래다. 1. preprocess necessity ambiguity가 보이면 `route_preprocess_compare_first` 2. ambiguity가 없..."
- unit_012 — heading_block / practical reading ~ practical reading — "### practical reading - raw transcript가 거칠거나 - uncertain-needs-probe 류 판정이 있으면 direct ingest보다 compare-first를 우선한다 - 반대로..."
- unit_013 — heading_block / fallback ~ fallback — "### fallback - `route_input_direct_ingest` 실패/잔여 확대 -> `route_preprocess_compare_first` - `route_preprocess_compare_firs..."
- unit_014 — heading_block / 2. fam_transition_thickening ~ 2. fam_transition_thickening — "## 2. fam_transition_thickening..."
- unit_015 — heading_block / candidate routes ~ candidate routes — "### candidate routes - `route_preflight_reread` - `route_stage_corridor_probe`..."
- unit_016 — heading_block / selection rule ~ selection rule — "### selection rule 기본 우선순위는 아래다. 1. active latent line과 phase signal이 있으면 `route_preflight_reread` 2. stage lineage가 분명하..."
- unit_017 — heading_block / practical reading ~ practical reading — "### practical reading - 현재 문제를 “지금 active line이 어떤 상태인가”로 읽는 경우 `route_preflight_reread`가 기본이다 - corridor lineage를 따라 bo..."
- unit_018 — heading_block / fallback ~ fallback — "### fallback - `route_preflight_reread` 후 boundary ambiguity가 유지 -> `route_stage_corridor_probe` - `route_stage_corridor..."
- unit_019 — heading_block / 3. fam_operator_readout ~ 3. fam_operator_readout — "## 3. fam_operator_readout..."
- unit_020 — heading_block / candidate routes ~ candidate routes — "### candidate routes - `route_readonly_board` - `route_internal_search`..."
- unit_021 — heading_block / selection rule ~ selection rule — "### selection rule 기본 우선순위는 아래다. 1. broad overview 요청이거나 현재 상태를 먼저 보여줘야 하면 `route_readonly_board` 2. explicit query가 있고 ..."
- unit_022 — heading_block / practical reading ~ practical reading — "### practical reading - operator가 “지금 상태가 뭐지?”에 가깝다면 `route_readonly_board` - operator가 “이 문제와 관련된 내부 route나 근거가 뭐지?”에 가..."
- unit_023 — heading_block / fallback ~ fallback — "### fallback - `route_readonly_board`에서 더 좁은 탐색 필요 -> `route_internal_search` - `route_internal_search` 결과가 빈약하거나 과한 경우 ..."
- unit_024 — heading_block / cross-family handoff 정책 ~ cross-family handoff 정책 — "## cross-family handoff 정책..."
- unit_025 — heading_block / 1. input -> transition ~ 1. input -> transition — "### 1. input -> transition 입력 family에서 direct ingest 또는 preprocess shaping이 끝난 뒤, 실제 전환/막힘/두꺼워짐 판단이 필요하면 `fam_transition..."
- unit_026 — heading_block / 2. transition -> readout ~ 2. transition -> readout — "### 2. transition -> readout transition family에서 나온 판단이 operator-facing explanation이나 현재 상태 해석으로 가야 하면 `fam_operator_rea..."
- unit_027 — heading_block / 3. readout does not replace transition ~ 3. readout does not replace transition — "### 3. readout does not replace transition readout family는 설명과 표면화가 목적이지, transition 판단 자체를 대체하지 않는다...."
- unit_028 — heading_block / selection order 요약 ~ selection order 요약 — "## selection order 요약 v0에서 route 선택 순서는 아래로 고정한다. 1. family 판정 2. activation condition 확인 3. exclusion condition 확인 4. s..."
- unit_029 — heading_block / 아직 약한 부분 ~ 아직 약한 부분 — "## 아직 약한 부분..."
- unit_030 — heading_block / 1. signal 값이 정량화돼 있지 않다 ~ 1. signal 값이 정량화돼 있지 않다 — "### 1. signal 값이 정량화돼 있지 않다 지금은 `high residue`, `ambiguity`, `overview request` 같은 문장형 규칙이 많다...."
- unit_031 — heading_block / 2. policy는 projection registry와 아직 분리돼 있다 ~ 2. policy는 projection registry와 아직 분리돼 있다 — "### 2. policy는 projection registry와 아직 분리돼 있다 나중에는 projection layer와 함께 읽어야 더 정확해진다...."
- unit_032 — heading_block / 3. family selection도 아직 문서적이다 ~ 3. family selection도 아직 문서적이다 — "### 3. family selection도 아직 문서적이다 issue-root classifier 수준의 규칙은 다음 단계에서 별도 필요하다...."
- unit_033 — heading_block / 현재 결론 ~ 현재 결론 — "## 현재 결론 v0에서 중요한 것은 완벽한 자동 선택이 아니다. 중요한 것은 아래를 잠그는 것이다. - 같은 family 안에서 무엇을 먼저 여는가 - 언제 fallback 하는가 - 언제 다음 family로 넘기..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

