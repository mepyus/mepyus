# VectorFL Organ Instruction Bundle And Handoff Packet Lock v0

이 문서는 기관별 md/instruction을 어떻게 읽고,  
기관 간 전달 패킷에 최소 무엇이 들어가야 하는지를 현재 단계 기준으로 잠근다.

목적은 아직 파일 경로나 구현체를 정하는 것이 아니라,
`기관 지시층`과 `기관 전달층`의 최소 문법을 잃지 않는 것이다.

## 1. Core Sentence

VectorFL 기관 구조에서는
`instruction bundle`이 기관의 읽기 책임과 반환 형식을 고정하고,
`handoff packet`이 현재 case/lane/governance/trace 상황을 다음 기관에 안전하게 넘기는 최소 계약이 되어야 한다.

즉 정적 지시와 동적 전달을 분리해 읽는 것이 맞다.

## 2. Instruction Bundle

기관별 instruction bundle은 아래 두 질문에 답해야 한다.

- 이 기관은 무엇을 읽는가
- 이 기관은 무엇을 반환해야 하는가

현재 단계에서 최소 묶음은 아래다.

### 2-1. role sentence

- 이 기관이 현재 맡는 책임 한 줄

### 2-2. accepted inputs

- 어떤 packet/context/ref를 받을 수 있는가

### 2-3. reading priorities

- 무엇을 먼저 보고 무엇은 보조로 볼 것인가

### 2-4. output contract

- summary / trace / governance / next-hop 중 무엇을 내야 하는가

### 2-5. caution rules

- weak input
- unresolved edge
- direct closure 금지
같은 조건에서 어떤 보수 규칙을 따르는가

즉 instruction bundle은 persona 문서보다  
`기관 책임 계약서`에 가깝다.

## 3. Handoff Packet

기관 간 handoff packet은 자유 대화가 아니라 shared environment packet으로 읽는다.

현재 단계에서 최소 필드는 아래다.

- `case_ref`
- `from_organ_ref`
- `to_organ_ref`
- `current_lane_ref`
- `case_summary`
- `current_surface_excerpt`
- `governance_state`
- `relevant_input_refs`
- `trace_carry_refs`
- `question_or_trigger`
- `expected_return_type`

## 4. Why These Fields Matter

### case_ref

- 같은 case continuity를 잃지 않게 한다

### from_organ_ref / to_organ_ref

- 책임 이동과 현재 handoff 방향을 보이게 한다

### current_lane_ref

- handoff가 lane-free generic transfer가 되지 않게 한다

### case_summary / current_surface_excerpt

- 전체 current-reading을 다 보내지 않고도 최소 읽기 상태를 붙인다

### governance_state

- hold / restriction을 handoff 과정에서 잃지 않게 한다

### relevant_input_refs

- source/intake 근거를 다시 돌아갈 수 있게 한다

### trace_carry_refs

- residue/reentry continuity를 보존한다

### question_or_trigger

- 다음 기관이 왜 지금 호출됐는지 분명히 한다

### expected_return_type

- 다음 기관이 무엇을 반환해야 하는지 좁힌다

## 5. First Approved Return Types

현재 단계에서 먼저 허용하는 반환 형식은 아래다.

- `translation_summary`
- `lane_hint_update`
- `flow_reading_summary`
- `governance_caution`
- `trace_return`
- `current_reading_ready_fragment`

즉 모든 기관이 같은 형식으로 말하지 않고,
`어떤 종류의 반환을 기대하는가`가 같이 붙어야 한다.

## 6. Governance Carry Rule

handoff packet에서는 governance가 절대 빠지면 안 된다.

최소 carry 항목:

- `hold_state`
- `restriction_flags`
- `release_condition` 또는 `not_ready_reason`

이유:

- direct presentation 금지
- observer-only
- promotion forbidden
같은 조건이 handoff 중 사라지면, 다음 기관이 잘못된 closure를 만들 수 있다.

## 7. Trace Carry Rule

handoff packet에서는 trace도 최소 carry가 필요하다.

최소 carry 항목:

- latest residue note
- latest reentry hint
- unresolved edge note

이유:

- 다음 기관은 빈 현재만 읽는 것이 아니라
- 무엇을 보존해야 하는지 같이 이어받아야 한다

## 8. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- exact md file naming
- exact directory layout
- packet serialization format
- transport method
- concurrent multi-organ handoff policy

즉 지금은 `지시층`과 `전달층`의 최소 내용만 잠근다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL 기관 구조에서는 기관별 instruction bundle이 읽기 책임과 반환 형식을 고정하고, handoff packet은 case, lane, governance, source/input refs, trace carry, question/trigger, expected return type를 잃지 않고 다음 기관에 넘기는 최소 shared-environment 계약으로 작동해야 한다.`
