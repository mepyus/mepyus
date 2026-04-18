[[A]] [[OBJ:domain_specific_vs_reusable_split_note_v1]] [[SEM:separating_named_objects_from_reusable_second_order_attitudes]]

# domain-specific vs reusable split note v1

## 1. purpose

- 이번 노트의 목적은 2차 보정에서 나온 이름과 태도를 분리해 기록하는 것이다.

## 2. currently domain-specific leaning signals

- `business_power_shift`
- `orchestration`
- `domain_to_component_reframing`
- `agent interface moat shift`
- `future_of_work_supervisor`

이 이름들은 지금 AI/에이전트/제품 전환 맥락에 강하게 묶여 있다.

## 3. reusable attitudes beneath them

- 질문 opening이 객체 다중 생존과 함께 뜨는지 본다
- relation movement가 설명층을 실행/전략/검증 쪽으로 내리는지 본다
- 같은 단락이 context frame에 따라 역할 이동을 보이는지 본다
- residue는 삭제보다 summary-stage 우선순위 재배치로 다룬다
- 2차 값은 곧바로 잠그지 않고 candidate/hold 상태로 둔다

## 4. comparison-domain update from `claude_code_index`

- `claude_code_index`를 넣어 보니, 객체 naming은 많이 흔들렸지만 판독 태도 일부는 유지됐다.
- 유지된 태도:
  - question opening을 block/window 조건과 함께 본다
  - relation movement를 transition/execution/specification 질문으로 읽는다
  - residue를 hard suppression이 아니라 opening priority 문제로 본다
- 흔들린 부분:
  - `AI의 미래`, `일의 미래`, `에이전트 애플리케이션` 같은 이름이 코드/도구 자산에도 과하게 전면화됐다
  - context unit 이름은 유지됐지만 실제 ref가 비어 있는 경우가 나왔다
  - paragraph role reading은 heading 구조가 달라지자 바로 무너졌다

즉 이번 비교는 아래를 더 선명하게 만든다.

- 객체 이름은 도메인에 따라 쉽게 leakage가 생긴다
- 하지만 판독 태도와 보류 태도는 도메인 바깥에서도 어느 정도 유지될 수 있다
- 따라서 일반화는 계속 `이름`이 아니라 `태도와 조건`부터 봐야 한다

## 5. split principle

- 객체 이름은 도메인 특화일 수 있다
- 판독 태도는 재사용 가능할 수 있다
- scaffold에 기대는 기관은 도메인 바깥에서 쉽게 무너질 수 있다
- 따라서 일반화는 객체명이 아니라 태도와 조건부터 보고, 기관은 scaffold dependency를 따로 기록해야 한다

## 6. attitude vs institution split

- reusable attitude examples:
  - question opening을 object co-survival과 함께 본다
  - relation movement를 transition/execution/specification으로 읽는다
  - residue를 summary priority 문제로 본다
- scaffold-bound institution examples:
  - heading-driven paragraph role interpretation
  - ref가 비어도 이름만 남는 context unit reconstruction
  - AI dialogue naming scaffold를 끌고 가는 object opening layer

즉 지금부터는 `무엇을 보는 태도`와 `그 태도를 실행하는 현재 기관`을 분리해서 기록해야 한다.

## 7. priority implication

- segmentation 축은 태도와 기관을 동시에 살릴 가능성이 가장 크다
- pointer 축은 태도는 남는데 grounding이 비는 문제를 줄이는 데 우선적이다
- heading 축은 기관 복구 가치가 있으나 현재는 reusable attitude 전체를 살리는 1순위는 아니다
- heading-independent probe 결과도 이 점을 지지한다:
  - heading이 약해도 role-like attitude는 약하게 남을 수 있다
  - 하지만 paragraph-role institution 자체는 여전히 scaffold-bound 하다

## 8. one-line summary

> 지금 일반화해야 하는 것은 `business_power_shift` 같은 이름이 아니라, 그런 이름이 떠오르게 만드는 2차 판독 태도와 조건이다.

## 9. three-axis integrated split read

- three-axis experiments made the split clearer:
  - segmentation / pointer / heading can each soften failure
  - but softening failure is not the same as recovering a reusable institution
- therefore:
  - reusable attitude may survive
  - institution may still remain scaffold-bound
- current common gate blockers belong mostly to the institution side:
  - question-inducing candidate absence
  - fallback grounding dominance
  - weak role-like only
  - pivot/compression non-recurrence
  - scaffold carryover risk
