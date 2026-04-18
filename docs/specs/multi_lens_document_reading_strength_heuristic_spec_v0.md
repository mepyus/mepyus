# multi lens document reading strength heuristic spec v0

## verdict

- strength heuristic is locked as a spec asset
- this turn does not change implementation code
- current bias is fixed as a heuristic-reading problem first, not as a line-maturity judgment problem

## what Turn 2 actually showed

- 실제 적용 대상은 stable/thick lens 두 개뿐이었다
- 전체 분포는 `strong=4`, `weak=8`, `absent=14`였다
- `line_input_to_reading_organ`은 일부 한국어/영어 keyword에 비교적 민감하게 반응해 `strong` 쪽으로 기울었다
- `line_transition_over_surface`는 현재 starter keyword map에서 거의 반응하지 않아 `absent` 쪽으로 기울었다
- `low linkage_confidence` singleton은 주로 `weak`로 내려갔다
- candidate/thin lens는 실제 strength 분포 판단 대상이 아니라 secondary metadata 수준으로만 남았다

## technical summary

### current heuristic behavior

- `strong`
  - keyword match가 있고 `linkage_confidence`가 `low`가 아닐 때
- `weak`
  - keyword match는 없지만 `linkage_confidence=low`일 때
- `absent`
  - relevant keyword가 없고 low-confidence 보정도 아닐 때
- `caution`
  - 현재 stable/thick skeleton에서는 최소 사용 원칙을 유지한다

이 규칙은 line maturity 판정이 아니라 starter heuristic output 규칙이다.

### stable/thick lens reading

- 이번 spec에서 refinement 대상으로 보는 것은 stable/thick 두 lens뿐이다
- `line_input_to_reading_organ`
  - 현재 starter keyword map 기준으로 over-trigger 가능성이 있다
  - 특히 `입력`, `읽기` 같은 일반성이 큰 표현에 비교적 민감하다
- `line_transition_over_surface`
  - 현재 starter keyword map 기준으로 under-reading 상태다
  - `transition`, `surface`, `전환`, `표면` 같은 좁은 trigger에 거의만 의존한다

### reading_basis explanation rule

`reading_basis`는 최소한 사람이 왜 그 결과가 나왔는지 추적할 수 있어야 한다.

필수 설명 원칙:

- `strong`
  - matched keyword 또는 matched seed를 직접 적는다
  - stable/thick lens 기준 결과임을 밝힌다
  - keyword match만 적고 끝내지 말고, 왜 `strong`으로 유지됐는지 짧게 드러나야 한다

- `weak`
  - `low linkage_confidence` 또는 partial basis 성격을 직접 적는다
  - `strong`이 아닌 이유가 basis 문장 안에 보여야 한다

- `absent`
  - `no relevant keyword` 또는 `no basis`를 직접 적는다
  - absent가 의미 부재 증명이 아니라 current heuristic miss임을 혼동하지 않게 써야 한다

- `caution`
  - 최소 사용 원칙을 유지한다
  - ambiguous case가 아니면 `strong / weak / absent` 중심으로 둔다

### observed bias patterns

- `line_input_to_reading_organ` strong bias
  - 현재 seed가 일반 표현과 너무 가깝기 때문에 과민 반응 가능성이 있다

- `line_transition_over_surface` absent bias
  - 현재 seed가 좁고 표면 표현 위주라 under-reading 가능성이 높다

- low-confidence singleton weak pattern
  - 현재 weak는 low-confidence 보정 역할이 강하고,
    semantic partial match를 따로 설명하지 않는다

- candidate/thin exclusion
  - candidate/thin lens는 지금 strength 관찰의 실제 대상이 아니므로
    분포 해석에 섞으면 안 된다

### non-goals

- no scoring formula introduction
- no document-level aggregation
- no variation map implementation
- no candidate/thin expansion
- no line registry change

### next patch gate

다음 patch는 아래 범위로만 연다.

- stable/thick 두 lens에 한해서만
- keyword seed refinement
- reading_basis 설명 문장 refinement

다음 patch에서도 아래는 금지한다.

- candidate/thin lens 실제 적용 확대
- scoring formula 도입
- aggregation 연결
- variation map 연결

## user-language summary

### current heuristic behavior

- 지금 `strong / weak / absent`는 line의 진짜 성숙도를 말하는 게 아니다
- 그냥 현재 starter heuristic이 어떻게 반응했는지 보여 주는 출력이다

### observed bias patterns

- `input_to_reading_organ`은 지금 조금 과민하다
- `transition_over_surface`는 지금 조금 둔감하다
- low-confidence singleton은 의미 판독이라기보다 약한 보정으로 `weak`가 붙는다
- candidate/thin은 아직 읽기 분포 판단 대상이 아니다

### reading_basis explanation rule

- `strong`이면 어떤 keyword가 걸렸는지 보여야 한다
- `weak`이면 왜 약하게 본 건지 보여야 한다
- `absent`이면 지금 heuristic에서 근거를 못 찾았다는 점이 보여야 한다

### user-language restatement

- 지금 잠근 핵심은 단순하다
- multi-lens strength output은 아직 heuristic output이다
- 다음 patch는 stable/thick 두 lens의 keyword와 basis 설명만 좁게 다뤄야 한다
