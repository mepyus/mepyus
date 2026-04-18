# Input Organ RETURN.md Draft v0

## return purpose

Input organ의 반환은  
후속 기관이 바로 읽을 수 있는 context-bearing intake packet과  
약함/불완전성을 숨기지 않는 caution summary를 넘기는 것이다.

즉 반환의 목적은:

- 입력 재료를 등록 가능한 source로 정리하고
- context를 붙이고
- split/block 단위를 만들고
- weak/fallback 상태를 함께 carry하는 것이다

## minimum return blocks

### 1. intake packet

- source ref
- context layers
- classification
- split units or intake blocks

### 2. intake status

- healthy
- usable
- weak
- blocked
- residue_only

### 3. weakness note

- parser weakness
- mixed material
- missing structure
- ambiguous classification

### 4. fallback flag

- structure-aware parsing 대신 fallback이 사용됐는지

### 5. next lane hint

- translation_first
- line_state_generation_candidate
- governance_review_first
- reread_needed

## preferred wording

- "registered as ..."
- "attach context ..."
- "carry as weak intake ..."
- "fallback used ..."
- "route next toward ..."

## avoid wording

- "fully understood"
- "resolved input"
- "final line"
- "safe to close"

## return example shape

- intake_packet:
  - source ref
  - matched context layers
  - classification
  - split units
- intake_status:
  - `usable_with_caution`
- weakness_note:
  - "Initial intake used fallback split across mixed runtime and operator note material."
- fallback_flag:
  - `true`
- next_lane_hint:
  - `translation_first`

## handoff note

이 반환은 주로 translation organ이나 line/state organ으로 넘어간다.

그래서 최소한 아래는 빠지면 안 된다.

- source/context carry
- provenance/origin
- weakness/fallback
- next lane hint

## final sentence

Input organ의 반환은 작은 값 목록이 아니라,  
source/context/provenance와 약함을 잃지 않은 intake packet과 caution summary를 다음 기관에 넘기는 preparation-aware return이어야 한다.
