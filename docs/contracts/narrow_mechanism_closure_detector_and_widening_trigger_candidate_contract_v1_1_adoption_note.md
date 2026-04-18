# narrow mechanism closure detector + widening trigger v1.1 감독 기준 후보 채택 기록

## 1. 채택 판정

- 판정:
  - `narrow mechanism closure detector + widening trigger candidate contract v1.1`은
    현재 단계에서 **감독 기준 후보로 채택 가능**하다.
- 근거:
  1. 기존 validation pass에서 detector / widening trigger 구조가 사례들 앞에서 대체로 일관되게 맞았다.
  2. v1.1 wording refinement를 통해 감독자가 바로 적용할 수 있는 operational wording으로 좁혀졌다.
  3. small validation sample(`carryover_risk / vlm`)에서도
     `binding_closed = no` gate를 지키며 과발동하지 않았다.

## 2. 채택된 적용 범위

이번 채택은 아래 범위에 한정된다.

- `narrow mechanism closure detector`
- `widening trigger`
- 아래 판정 축의 분리 유지:
  - `binding closed`
  - `semantic fidelity`
  - `output-worthiness`
  - `meaning-context sufficiency`
- output/read unit 관점 포함:
  - 현재 unit이 읽기/표시 단위로 최소 성립하는가
  - 현재 unit이 row 의미를 충분히 운반하는가

즉 이 채택은 “값이 닫혔는가”만 보는 기준이 아니라,
“닫힌 값이 실제로 읽기 가능한 최소 의미 단위 위에 서 있는가”까지 함께 보는 감독 기준 후보 채택이다.

## 3. 채택되지 않은 범위

이번 채택은 아래를 포함하지 않는다.

- broad default widening rule
- full contract 선언
- 모든 row family에 대한 즉시 일반 적용
- `binding_closed = no`인 pre-closure 상태에 widening trigger를 직접 적용하는 것
- semantic fidelity guard 없이 closure success만으로 충분하다고 보는 해석

즉 이 문서는 broad 운영 규칙 채택 문서가 아니라,
**감독자가 사례를 읽을 때 사용할 candidate-level reading standard 채택 문서**다.

## 4. watchpoint

감독 기준 후보로 사용할 때 아래를 반드시 같이 본다.

1. `mechanism-only closure`를 `row-meaning-faithful closure`로 오해하지 말 것
2. 값이 닫혀도 문장이 출력 가능한 최소 의미 단위인지 별도 판정할 것
3. `closure success`와 `semantic fidelity okay`를 혼동하지 말 것
4. `output-worthiness`와 `meaning-context sufficiency`를 계속 분리해 볼 것
5. next sentence가 보강처럼 보여도, 그것만으로 widening을 자동 승인하지 말 것

## 5. optional note: pre-closure context-bearing watchpoint

### 5-1. 취지

다음 문장이 실제로 의미 보강을 주는 것처럼 보여도,
`binding_closed = no` 단계에서는 그것을 곧바로 widening rule로 넘기지 않기 위한 보조 메모다.

### 5-2. note 수준으로만 두는 이유

- 이 영역은 아직 detector/widening candidate contract 본체에 들어갈 만큼 검증되지 않았다.
- pre-closure는 closure 이후 local widening과 다르게,
  retrieval / unit quality / canonical mapping 부족이 먼저 병목일 수 있다.
- 따라서 지금은 규칙이 아니라 **watchpoint**로만 남긴다.

### 5-3. 현재 메모

- 다음 문장이 의미 보강적으로 보여도,
  `binding_closed = no` 상태에서는 widening trigger를 직접 적용하지 않는다.
- 대신 아래 가능성을 watchpoint로만 본다.
  - retrieval quality 문제인지
  - unit quality 문제인지
  - canonical mapping 부재 문제인지
  - pre-closure context-bearing reread 후보가 있는지

## 6. 왜 지금 채택 가능한가

- detector와 widening trigger를 분리하는 구조는 이미 validation pass를 통과했다.
- wording v1.1은 false positive를 줄이도록 operational하게 좁혀졌다.
- small validation sample은 “보강처럼 보이는 next sentence”가 있어도
  gate가 없으면 widening이 켜지지 않아야 한다는 점을 실제로 보여줬다.

따라서 현재 수준에서는 broad default rule이나 full contract는 아니지만,
**감독 기준 후보**로는 충분히 채택 가능하다.

## 7. 왜 full contract는 아닌가

- row family coverage가 아직 좁다.
- cross-family 근거는 과발동 방지엔 충분하지만,
  일반 운영 규칙으로 잠그기엔 아직 sample이 더 필요하다.
- pre-closure 영역은 여전히 note 수준이다.

즉 지금 채택되는 것은 full operational rule이 아니라,
감독자가 사례를 읽고 판정할 때 쓰는 **candidate-level supervisory standard**다.

## 8. 이후 감독 기준으로 무엇이 바뀌는가

다음부터 감독은 아래 순서로 읽는다.

1. `binding closed` 여부를 먼저 본다
2. 닫혔다면 `semantic fidelity`를 별도로 본다
3. 현재 unit의 `output-worthiness`를 본다
4. 현재 unit의 `meaning-context sufficiency`를 본다
5. 이 네 가지를 만족하면서 `narrow mechanism closure`일 때만 detector를 켠다
6. detector가 켜진 뒤에도 next sentence가 row 의미를 실제로 직접 보강할 때만 widening trigger를 검토한다

## 9. 한 줄 판정

- `narrow mechanism closure detector + widening trigger candidate contract v1.1`은
  **감독 기준 후보로 채택 가능**하며,
  broad default rule이나 full contract가 아니라
  detector / widening / output-read unit 판정을 함께 보는 조건부 감독 기준으로 사용한다.
