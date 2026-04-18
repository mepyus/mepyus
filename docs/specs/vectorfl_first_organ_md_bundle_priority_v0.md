# VectorFL First Organ MD Bundle Priority v0

이 문서는 첫 기관 md bundle을 실제로 만들 때  
무엇부터 쓰고 무엇은 나중으로 미뤄도 되는지 우선순위를 짧게 잠근다.

목적은 기관별 파일셋을 한 번에 과하게 만들지 않고,
가장 필요한 기준부터 차례로 고정하는 것이다.

## 1. Priority Verdict

첫 md bundle 작성 우선순위는 아래가 맞다.

1. `translation organ`
2. `flow interpretation organ`
3. `governance organ`
4. `input organ`

## 2. Why This Order

### 2-1. translation organ first

- 지금 가장 많이 흔들릴 수 있는 곳이 grammar shift다
- intake 재료를 current-reading 쪽으로 밀기 전 가장 먼저 기준이 필요하다

### 2-2. flow interpretation second

- next hop, unresolved edge, reread direction이 실제 운영 흐름의 중심이다
- Paperclip 구조에서 가져오려는 `progression legibility`도 여기와 가장 강하게 만난다

### 2-3. governance third

- hold, observer-only, promotion forbidden, closure-before-presentation을
  어디서 어떻게 멈출지 기준이 있어야 한다

### 2-4. input fourth

- input도 중요하지만 이미 qmd-ref 기준과 intake 구조 문서가 많이 잠겨 있다
- 따라서 지금은 후속 기관의 의미 계약이 더 우선이다

## 3. Minimum Good Enough Bundle

첫 작성은 모든 파일을 다 채울 필요가 없다.

기관 하나당 아래만 먼저 있으면 충분하다.

- `ROLE.md`
- `RETURN.md`

그 다음에

- `HANDOFF.md`
- `CAUTION.md`

를 붙여도 된다.

## 4. What To Avoid

- 첫 단계부터 너무 긴 철학 문서 만들기
- 모든 기관을 한 번에 다 작성하기
- persona/톤 문서처럼 쓰기
- return contract 없이 role만 적기

즉 첫 번들은 `짧고 계약적`이어야 한다.

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`첫 기관 md bundle 작성은 translation -> flow interpretation -> governance -> input 순서가 가장 적절하며, 각 기관도 처음에는 ROLE/RETURN을 먼저 잡고 HANDOFF/CAUTION을 뒤에 붙이는 짧은 계약 문법으로 시작하는 것이 맞다.`
