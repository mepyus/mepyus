# readable input board / general_line_vs_flow_candidate_v0_flow_guard_20260422_185702

## 1. 입력 정보
- input_id: `general_line_vs_flow_candidate_v0_flow_guard`
- label: `general_line_vs_flow_candidate_v0_flow_guard`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reviews/general_line_vs_flow_candidate_v0.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `91`
- unit_count: `8`

## 3. unit 목록 요약
- unit_001 — heading_block / General Line vs Flow Candidate v0 ~ General Line vs Flow Candidate v0 — "# General Line vs Flow Candidate v0..."
- unit_002 — heading_block / 목적 ~ 목적 — "## 목적 이 문서는 현재 VectorFL에서 `general line` 과 `flow candidate` 를 왜 분리해야 하는지 실행 spine 기준으로 실무적으로 정리한다...."
- unit_003 — heading_block / 1. general line ~ 1. general line — "## 1. general line 현재 VectorFL의 기본 단위는 family / projection / route 중심의 general line이다. 즉 지금 실제로 작동하는 것은: - current hint ..."
- unit_004 — heading_block / 2. flow candidate ~ 2. flow candidate — "## 2. flow candidate flow candidate는 한 번의 run 안의 경로가 아니라, 여러 run 사이에서 반복되는 multi-step transition pattern이다. 예: - input f..."
- unit_005 — heading_block / 3. 왜 지금 flow line으로 승격하면 안 되는가 ~ 3. 왜 지금 flow line으로 승격하면 안 되는가 — "## 3. 왜 지금 flow line으로 승격하면 안 되는가 현재는 run 수가 아직 적고, 반복 패턴도 host/context에 따라 쉽게 흔들릴 수 있다. 그래서 지금 단계에서 `flow_line` 을 first..."
- unit_006 — heading_block / 4. 현재 적절한 순서 ~ 4. 현재 적절한 순서 — "## 4. 현재 적절한 순서 현재 순서는 아래가 맞다. 1. general line으로 run을 해석한다 2. execution trace를 append-only로 남긴다 3. 여러 trace를 비교해 repeate..."
- unit_007 — heading_block / 5. future promotion에 필요한 최소 증거 ~ 5. future promotion에 필요한 최소 증거 — "## 5. future promotion에 필요한 최소 증거 나중에 flow line 승격을 검토하려면 적어도 아래가 필요하다. - 동일하거나 매우 유사한 multi-step sequence의 반복 - family ..."
- unit_008 — heading_block / 한 줄 요약 ~ 한 줄 요약 — "## 한 줄 요약 지금은 general line을 유지한 채 반복 run에서 보이는 transition pattern만 flow candidate로 관찰해야 하며, formal flow line promotion은 ..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

