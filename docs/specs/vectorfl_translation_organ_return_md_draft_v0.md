# Translation Organ RETURN.md Draft v0

## return purpose

Translation organ의 반환은 raw output이 아니라,  
다음 기관과 current-reading이 바로 읽을 수 있는 `grammar-aware return`이어야 한다.

즉 반환의 목적은:

- 지금 어떤 문법으로 읽는 것이 맞는지 짧게 밝히고
- 다음 기관이 이어받을 lane/flow 판단 재료를 남기고
- 아직 강하지 않은 부분은 caution으로 표시하는 것이다

## minimum return blocks

### 1. translation summary

- 지금 이 case/material/surface를 어떤 grammar로 읽는 것이 맞는지
- 예:
  - transition-thickening
  - explanation-first
  - reread-before-presentation

### 2. lane hint update

- 다음 기관이 볼 lane candidate
- current lane 유지 또는 shift suggestion

### 3. supporting evidence refs

- source ref
- intake packet ref
- surface ref
- trace carry ref

### 4. caution note

- weak translation
- mixed material still unresolved
- direct readout not safe

## preferred wording

- "read as ..."
- "treat this as ..."
- "carry forward ..."
- "do not close yet ..."
- "next lane candidate ..."

## avoid wording

- "resolved"
- "final"
- "approved"
- "ready for presentation" without governance support
- "this definitively means ..." when unresolved edge remains

## return example shape

- translation_summary:
  - "Read this as transition-thickening rather than presentation-ready."
- lane_hint_update:
  - `lane_transition_preflight_reread`
  - `lane_operator_readout_review`
- supporting_evidence_refs:
  - intake packet
  - current surface
  - residue trace
- caution_note:
  - "Mixed runtime and operator-note material still carries unresolved edge."

## handoff note

이 반환은 흐름해석기관이나 governance/current-reading 반환면으로 넘어갈 준비를 해야 한다.

그래서 최소한 아래는 빠지면 안 된다.

- next lane candidate
- unresolved edge 여부
- evidence refs
- caution carry

## final sentence

Translation organ의 반환은 문장을 멋있게 만드는 요약이 아니라,  
현재 case를 어떤 문법으로 읽어야 하는지와 그에 따라 다음 기관이 무엇을 이어받아야 하는지를 짧고 보수적으로 넘기는 grammar-aware return이어야 한다.
