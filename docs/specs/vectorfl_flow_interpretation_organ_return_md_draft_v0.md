# Flow Interpretation Organ RETURN.md Draft v0

## return purpose

Flow interpretation organ의 반환은  
현재 흐름이 어떤 next hop으로 읽히는지와  
무엇이 아직 unresolved로 남아 있는지를 다음 기관과 current-reading이 읽을 수 있게 넘기는 것이다.

즉 반환의 목적은:

- next hop을 좁히고
- unresolved edge를 보존하고
- reread / reentry / caution을 current-reading과 governance가 이어받게 하는 것이다

## minimum return blocks

### 1. flow reading summary

- 현재 흐름을 어떻게 읽는지 한두 문장으로 정리
- 예:
  - "Read this as transition reread first, not direct operator presentation."

### 2. next hop candidates

- 다음 기관 / 다음 lane 후보
- 하나일 수도 있고 둘 이상일 수도 있음

### 3. unresolved edge note

- 아직 closure-ready가 아닌 이유
- preserve해야 하는 edge가 무엇인지

### 4. reentry hint

- 어떤 질문/트리거에서 다시 이 흐름을 열어야 하는지

### 5. caution note

- direct readout hold
- explanation-first bias
- governance-sensitive stop

## preferred wording

- "route next through ..."
- "keep this in ..."
- "do not collapse into ..."
- "preserve unresolved edge ..."
- "reopen when ..."

## avoid wording

- "final next step"
- "resolved path"
- "safe to close"
- "presentation ready" without governance support

## return example shape

- flow_reading_summary:
  - "Keep this in transition reread until closure evidence improves."
- next_hop_candidates:
  - `lane_transition_preflight_reread`
  - `lane_operator_readout_review`
- unresolved_edge_note:
  - "Closure-before-presentation remains unresolved."
- reentry_hint:
  - "If operator asks for summary first, reopen transition interpretation."
- caution_note:
  - "Direct presentation should remain held."

## handoff note

이 반환은 주로 governance organ과 current-reading return면으로 넘어간다.

그래서 최소한 아래는 빠지면 안 된다.

- next hop candidates
- unresolved edge note
- reentry hint
- caution carry

## final sentence

Flow interpretation organ의 반환은 다음 단계를 확정하는 명령이 아니라,  
현재 흐름이 어디로 이어져야 하는지와 무엇을 아직 preserve해야 하는지를 보수적으로 넘기는 progression-aware return이어야 한다.
