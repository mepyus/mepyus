# VectorFL First Organ MD Bundle Fileset v0

이 문서는 앞서 잠근 `기관 instruction skeleton`을  
실제 파일셋 관점에서 어떻게 나눠 둘지 초안 수준으로 고정한다.

목적은 지금 당장 md 파일을 전부 만드는 것이 아니라,
기관 수가 늘어날 때도 `지시 / handoff / caution / return contract`가 섞이지 않게  
최소 파일 구조 감각을 먼저 잠그는 것이다.

## 1. Core Sentence

첫 기관 md bundle은
`기관마다 한 덩어리 거대 문서`보다,
`core instruction + handoff contract + caution rules + return contract`
가 느슨하게 분리된 작은 파일셋으로 가는 것이 맞다.

즉 기관별 지시는 persona 문서가 아니라  
`운용 계약 파일 묶음`으로 읽어야 한다.

## 2. First Target Organs

현재 단계에서 first fileset 대상으로 보기 좋은 기관은 아래 넷이다.

- `input organ`
- `translation organ`
- `flow interpretation organ`
- `governance organ`

이 네 기관은 이미 아래 문서에서 skeleton이 잡혀 있다.

- [vectorfl_first_organ_instruction_skeletons_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_first_organ_instruction_skeletons_v0.md)
- [vectorfl_organ_instruction_bundle_and_handoff_packet_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_organ_instruction_bundle_and_handoff_packet_lock_v0.md)
- [vectorfl_first_organ_chain_example_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_first_organ_chain_example_v0.md)

## 3. Recommended Fileset Shape

현재 단계에서 기관별 md bundle은 아래 4파일 감각이 가장 적절하다.

### 3-1. `ROLE.md`

역할:

- role sentence
- reading priorities
- what this organ must not overclaim

즉 기관의 `읽기 정체성`을 잠그는 파일이다.

### 3-2. `HANDOFF.md`

역할:

- accepted inputs
- required handoff packet fields
- common triggers
- continuity / carry expectations

즉 기관이 `무엇을 어떻게 이어받는가`를 잠그는 파일이다.

### 3-3. `CAUTION.md`

역할:

- weak input handling
- unresolved edge preservation
- governance-sensitive stops
- what must remain candidate-only

즉 기관이 `어디서 보수적으로 멈추는가`를 잠그는 파일이다.

### 3-4. `RETURN.md`

역할:

- summary return shape
- trace return shape
- governance return shape if any
- next handoff readiness wording

즉 기관이 `무엇을 남기고 넘기는가`를 잠그는 파일이다.

## 4. Why This Split Is Better Than One Big File

이 분리가 좋은 이유는 아래다.

### 4-1. role과 caution이 섞이지 않는다

기관의 정체성과 보수 규칙이 분리된다.

### 4-2. handoff와 return이 대칭으로 보인다

무엇을 받는지와 무엇을 넘기는지가 한 쌍으로 읽힌다.

### 4-3. 기관 증가에 더 잘 버틴다

나중에 기관 수가 많아져도 같은 파일 리듬으로 확장할 수 있다.

### 4-4. Paperclip 참조와도 잘 맞는다

Paperclip에서 본

- static instruction
- dynamic context
- summary return

구조를 VectorFL 쪽에서 더 명시적으로 분리해 소유할 수 있다.

## 5. Suggested Naming Rule

현재 단계에서는 아래처럼 읽는 것이 가장 무난하다.

- `organs/input/ROLE.md`
- `organs/input/HANDOFF.md`
- `organs/input/CAUTION.md`
- `organs/input/RETURN.md`

- `organs/translation/...`
- `organs/flow_interpretation/...`
- `organs/governance/...`

중요한 점:

- 지금은 실제 파일 생성을 잠그는 단계가 아님
- naming 감각만 먼저 고정한다

## 6. What Must Stay Shared

기관별 파일로 쪼개도 아래는 공통 기준으로 남아야 한다.

- current-reading first
- governance carry must not drop
- trace/residue/reentry carry must not drop
- ontology import 금지
- candidate와 closure의 구분 유지

즉 기관별 md가 생겨도  
상위 VectorFL 원칙은 계속 공유 기준으로 살아 있어야 한다.

## 7. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- exact repository directory
- whether files are repo-local or runtime-generated
- AGENTS.md style auto-injection mechanics
- per-organ templating system
- editing UI

즉 지금은 `파일셋 감각`만 잠근다.

## 8. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL의 첫 기관 md bundle은 input, translation, flow interpretation, governance 네 기관에 대해 ROLE/HANDOFF/CAUTION/RETURN 네 묶음으로 나뉜 운용 계약 파일셋 감각으로 준비하는 것이 가장 적절하고, 이 분리는 나중에 기관 수가 늘어나도 지시, 전달, 보수 규칙, 반환 형식이 섞이지 않게 하는 최소 구조가 된다.`
