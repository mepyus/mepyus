# vectorfl surface-only paperclip adoption lock v0

이 문서는 Paperclip를 `공간 본체`가 아니라 `운용화면 grammar`로만 참조하는 기준을 잠근다.

목적은 VectorFL 공간의 canonical 질서를 건드리지 않은 채,  
Paperclip native page class를 표면에만 도입해 더 operable한 운영화면을 만드는 것이다.

## 1. core sentence

VectorFL는 공간 자체를 Paperclip로 바꾸지 않는다.  
`VectorFL core space는 그대로 유지하고, Paperclip는 surface page grammar로만 채택한다.`

즉:

- 공간은 그대로 둔다
- 표면만 바꾼다
- Paperclip ontology는 들이지 않는다
- Paperclip native page class만 참조한다

## 2. what stays untouched

아래는 이번 기준에서도 그대로 유지된다.

- current-reading 중심성
- governance first-class
- trace / memory retention
- intake / core / shell ownership
- case / lane / organ / surface / trace canonical object
- ontology non-import rule

즉 Paperclip adoption은 `surface-only`다.

## 3. what is adopted from paperclip

도입 대상은 디자인 톤만이 아니라 `page grammar`다.

현재 단계에서 가져오는 것은 아래다.

- work list page grammar
- work detail page grammar
- right-side inspector grammar
- operable agent/organ detail grammar
- audit page grammar
- spatial page grammar

즉 가져오는 것은 `어떤 종류의 페이지가 있어야 실제 운용이 가능한가`에 대한 구조다.

## 4. what is not adopted

아래는 surface-only adoption에서도 들이지 않는다.

- company ontology
- issue ontology
- project / goal ontology
- heartbeat ontology
- approval / budget naming
- account/login model
- Paperclip backend/runtime semantics

즉 Paperclip를 shell app으로 통째로 들이는 것이 아니다.

## 5. why this is the right adoption mode

이 방식이 맞는 이유는 아래와 같다.

### 5-1. our space principles stay canonical

VectorFL가 지금까지 잠근

- current-reading
- governance
- trace
- organ handoff
- intake packet

질서를 그대로 유지할 수 있다.

### 5-2. the real gap was in operable surfaces

지금까지의 간극은 공간 철학 부족이 아니라

- work list
- detail
- inspector
- organ management
- audit

같은 operable page class 부족이었다.

즉 surface-only adoption이 정확히 그 gap을 메운다.

### 5-3. non-mixing rule remains intact

이 방식이면 Paperclip를 깊게 참조하더라도  
우리 쪽 canonical object와 ontology는 유지된다.

## 6. surface re-ownership rule

Paperclip page grammar는 가져오되, surface 의미는 VectorFL가 다시 소유한다.

예:

- issue list grammar
  -> `cases work list`
- issue detail grammar
  -> `case detail / current-reading work detail`
- issue properties grammar
  -> `case inspector`
- agent detail grammar
  -> `organ detail`
- activity grammar
  -> `trace audit`
- org chart grammar
  -> `spatial flow / relation page`

즉 `same page grammar, different semantic ownership`이 기준이다.

## 7. operator-facing consequence

이 기준이 들어오면 VectorFL 표면은 아래 요구를 만족해야 한다.

- 현재 case가 어디에 놓였는지 보인다
- 현재 organ/lane 책임이 보인다
- next-hop candidate가 보인다
- governance restriction이 inspector에 보인다
- organ 자체를 수정할 수 있다
- trace/audit를 별도 page class에서 읽을 수 있다

즉 단순 graph-like center view는 더 이상 중심 기준이 아니다.

## 8. first adoption consequence

surface-only adoption 이후 우선 page class는 아래가 된다.

1. `Cases` as work list page
2. `Case Detail` as current-reading work detail page
3. `Case Inspector` as right-side inspector
4. `Organs` as organ management list
5. `Organ Detail` as operable organ page
6. `Trace Audit` as audit page

## 9. final lock sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL는 공간과 canonical object를 그대로 유지한 채, Paperclip를 work list/detail/inspector/organ detail/audit/spatial page grammar를 제공하는 surface-only reference로 채택하고, 각 page의 의미는 VectorFL의 current-reading, governance, trace, organ 질서로 다시 소유한다.`
