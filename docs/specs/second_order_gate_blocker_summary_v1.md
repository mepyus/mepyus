[[A]] [[OBJ:second_order_gate_blocker_summary_v1]] [[SEM:minimal_summary_spec_for_current_second_order_gate_blockers]]

# second-order gate blocker summary v1

## 1. purpose

- 이 문서의 목적은 운영자가 현재 `next loop entry gate`를 막고 있는 blocker를 최소 요약 형태로 한눈에 볼 수 있게 하는 것이다.
- 여기서 blocker는 실패 낙인이 아니라 premature closure point를 가리킨다.

## 2. blockers

### blocker_name
- `question_inducing_candidate_absence`
  - blocker_type: emergence blocker
  - repeated_assets:
    - `openai_02_11`
    - `graphrag_neosh`
    - `enterprise`
    - `claude_code_index`
  - affected_readings:
    - question-inducing block
    - question seed promotion
  - evidence_level: high
  - why_it_blocks_gate:
    - gate가 요구하는 non-zero question-inducing recurrence가 아직 없다
  - what_would_count_as_relief:
    - cross-asset에서 non-zero candidate가 반복 등장
  - current_status: active

### blocker_name
- `fallback_grounding_dominance`
  - blocker_type: grounding blocker
  - repeated_assets:
    - `openai_02_11`
    - `graphrag_neosh`
    - `enterprise`
    - `claude_code_index`
  - affected_readings:
    - context unit
    - role-like reading
    - candidate support
  - evidence_level: high
  - why_it_blocks_gate:
    - 대부분의 회복이 direct가 아니라 fallback 수준에 머물러 institution recovery로 보기 어렵다
  - what_would_count_as_relief:
    - repeated partial direct grounding
  - current_status: active

### blocker_name
- `weak_role_like_only`
  - blocker_type: role institution blocker
  - repeated_assets:
    - `graphrag_neosh`
    - `enterprise`
    - `claude_code_index`
    - `openai_02_11`는 role-like reading 부재
  - affected_readings:
    - paragraph role
    - role shift
    - local/page/comparison role interpretation
  - evidence_level: medium_high
  - why_it_blocks_gate:
    - role 계열이 probe 수준을 넘지 못한다
  - what_would_count_as_relief:
    - evidence-linked repeated role-like reading beyond weak
  - current_status: active

### blocker_name
- `pivot_compression_non_recurrence`
  - blocker_type: higher-order condensation blocker
  - repeated_assets:
    - `openai_02_11`
    - `graphrag_neosh`
    - `enterprise`
    - `claude_code_index`
  - affected_readings:
    - pivot
    - compression
    - higher-order condensation
  - evidence_level: medium
  - why_it_blocks_gate:
    - upper second-order condensations가 반복 회복되지 않는다
  - what_would_count_as_relief:
    - partial repeated pivot/compression recovery
  - current_status: active

### blocker_name
- `scaffold_carryover_risk`
  - blocker_type: contamination blocker
  - repeated_assets:
    - `graphrag_neosh`
    - `enterprise`
    - `claude_code_index`
  - affected_readings:
    - object naming
    - context unit naming
    - role scaffold
  - evidence_level: medium_high
  - why_it_blocks_gate:
    - recovery처럼 보이는 값이 실제론 기존 scaffold carryover일 가능성이 높다
  - what_would_count_as_relief:
    - asset-specific support 없이도 evidence-linked new naming / reduced carryover
  - current_status: active

## 3. current read

- 지금 gate는 단일 blocker 하나 때문에 막힌 것이 아니라, 위 blocker 묶음이 동시에 남아 있기 때문에 닫혀 있다.

## 4. operator use

- 다음 판단은 “무엇을 더 실험할까”보다
  - 어떤 blocker가 약해졌는가
  - 어떤 blocker가 그대로인가
  - 어떤 blocker가 새로 생겼는가
  를 먼저 보는 방식으로 한다.
- 여기서 blocker는 금지 목록이 아니라 memory label이다.
- blocker 약화는 승격 준비보다 reinterpretation tolerance 증가로 먼저 읽는다.

## 5. one-line summary

> 현재 second-order gate는 emergence, grounding, role, condensation, carryover blocker가 동시에 남아 있기 때문에 닫혀 있으며, 다음 판단은 이 blocker 묶음의 완화 여부를 기준으로 이뤄져야 한다. 이 값들은 폐기물이 아니라 future comparison memory다.
