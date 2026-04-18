# multi lens document reading transition over surface partial match spec v0

## verdict

- `transition_over_surface` partial-match rule is locked as a spec asset
- this turn does not change implementation code
- current `transition_over_surface` under-reading is fixed as an isolated bottleneck first

## what the recent patch actually showed

- recent patch는 `input_to_reading_organ`의 over-trigger 완화에는 기여했다
- 그러나 `transition_over_surface`는 현재 fixture 기준에서 여전히 mostly `absent/weak` 수준에 머물렀다
- strong 전체가 `0`으로 내려간 상태에서도
  `transition_over_surface` 쪽 recovery는 거의 보이지 않았다
- 따라서 지금 별도 병목은 `transition_over_surface`의 partial-match rule과 seed combination boundary 부재에 가깝다

## technical summary

### why transition_over_surface is now the isolated bottleneck

- 이번 턴에서는 `input_to_reading_organ`을 다시 흔들지 않는다
- stable/thick 두 lens 중 현재 더 둔감한 축은 `transition_over_surface`다
- 이 lens는 단순 token 반응을 피하려다 보니
  실제 조합형 단서도 충분히 살리지 못하고 있다

### current under-reading pattern

- `transition_over_surface`는 현재 fixture 기준으로 mostly `absent/weak`다
- 단독 `표면`이나 단독 `transition`은 strong이 아니어야 한다는 경계는 유지돼야 한다
- 문제는 `transition/surface`, `전환/표면`의 조합형 단서가 있어도
  그것을 언제 `weak`로 읽고 언제 `strong` 후보로 올릴지 경계가 문서로 잠기지 않았다는 점이다

### partial match proposal

`transition_over_surface`는 아래 조건에서 `weak` partial match 후보가 될 수 있다.

- `transition` 계열 표현은 있으나 `surface` 계열이 약하게만 보일 때
- `surface` 계열 표현은 있으나 `transition` 맥락이 약하게만 동반될 때
- `transition/surface` 또는 `전환/표면`의 조합이 있으나
  `linkage_confidence=low`라서 strong으로 올리기 어려울 때
- 단일 token이 아니라 조합형 단서가 보이지만,
  설명 문장에서 무엇이 부족한지 함께 말할 수 있을 때

여전히 `absent`로 두는 경우:

- 단독 `표면`
- 단독 `transition`
- 단독 `전환`
- 설명 불가능한 약한 단일 token 반응
- 조합이 있다고 해도 basis 문장으로 설명할 수 없는 경우

### seed combination boundary proposal

`strong` 후보가 될 수 있는 조합:

- `transition + surface`
- `전환 + 표면`
- `transition over surface`
- `surface transition`
- `표면 전환`
- `표면 위 전환`
- `표면 넘어 전환`

`weak`에만 머물러야 하는 조합:

- `transition` 계열은 있으나 `surface` 계열이 직접 결합하지 않은 경우
- `surface` 계열은 있으나 전환 맥락이 약한 경우
- 조합은 있으나 `linkage_confidence=low`인 경우
- 영어/한국어 혼합 조합이 있으나
  문장 안에서 transition-over-surface라는 구조를 명확히 설명하지 못하는 경우

여전히 `strong` 금지인 단독 표현:

- 단독 `표면`
- 단독 `surface`
- 단독 `transition`
- 단독 `전환`

### reading_basis rule

- `strong`
  - 어떤 조합 seed가 걸렸는지 직접 적어야 한다
  - 예: `matched seed: 표면 전환; primary stable/thick lens basis`

- `weak`
  - partial match라는 점과 무엇이 부족한지 직접 적어야 한다
  - 예: `partial transition-only phrase; missing surface combination`
  - 예: `surface phrase present but transition context weak`

- `absent`
  - no relevant transition-over-surface seed / no basis를 직접 적어야 한다

### non-goals

- no input_to_reading_organ re-tuning
- no keyword map full redesign
- no scoring formula introduction
- no document-level aggregation
- no candidate/thin expansion

### next patch gate

다음 patch는 아래 범위로만 연다.

- `transition_over_surface` 한정
- partial match refinement
- seed combination refinement
- reading_basis 문장 refinement

다음 patch에서도 금지:

- `input_to_reading_organ` 재조정
- scoring formula 도입
- candidate/thin 확대
- aggregation 연결

## user-language summary

### current under-reading pattern

- 지금 `transition_over_surface`는 너무 많이 `absent/weak`로 남는다
- 단독 `표면`을 strong으로 올리지 않는 건 맞지만,
  조합형 단서를 읽는 기준이 아직 너무 약하다

### partial match proposal

- `transition`와 `surface`가 느슨하게라도 같이 보이면
  그건 `weak` partial match 후보로 볼 수 있다
- 하지만 단어 하나만 걸린 경우는 계속 `absent`로 남겨야 한다

### seed combination boundary proposal

- `표면 전환`, `surface transition`, `transition over surface` 같은 조합은 strong 후보가 될 수 있다
- 반면 단독 `표면`, 단독 `transition`은 여전히 strong 금지다

### user-language restatement

- 이번 턴에서 잠근 핵심은 단순하다
- `transition_over_surface`는 단일 token lens가 아니라 조합형 단서 lens로 다뤄야 한다
- 다음 patch는 그 조합형 경계만 좁게 다루면 된다
