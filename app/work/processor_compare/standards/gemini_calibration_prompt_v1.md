# Gemini Calibration Prompt v1

목적:
- 장문 문서 처리 시 Gemini에서 반복적으로 관찰된 drift를 억제한다.
- 특히 대묶음, 추상화 확대, meta/reflection 과사용, `scene=process` 같은 비표준 scene 생성을 줄이는 데 목적이 있다.

이 프롬프트는 `processor_execution_prompt_v2.md`를 대체하지 않는다.
공통 프롬프트를 준 뒤, Gemini에게 추가 보정 지시로 붙인다.

## Gemini 추가 보정 지시

너는 장문 문서를 처리할 때 다음 경향을 보이지 않도록 주의해야 한다.

1. 과대묶음 금지
- 요약/정의, 문제/해법, 메커니즘/가치, 과제/결론을 자동으로 하나의 큰 블록으로 흡수하지 말 것
- 의미축이 바뀌면 분리 후보로 먼저 검토할 것

2. 상위 추상화 과잉 금지
- 원문에 있는 중간 손잡이를 지우고 지나치게 큰 상위 개념 하나로 덮지 말 것
- `ontology_centric_system`, `digital_twin_reflection` 같은 과도한 상위 추상화는 억제할 것

3. meta/reflection 과사용 금지
- 결론이라고 자동으로 `scene=reflection`, `role=meta`로 올리지 말 것
- 실제 메타 총평이 아닌 경우 기본은 `scene=explanation`
- 결론 문단은 우선 `role=thesis` 또는 `role=expansion` 후보로 본다

4. 비표준 scene 생성 금지
- `process`는 scene이 아니다
- 절차/단계 설명도 기본은 `scene=explanation`
- `definition`, `example`, `process`, `thesis`, `support`를 scene으로 사용하지 말 것

5. anchor 과대추상화 금지
- anchor 수를 줄이기 위해 중요한 중간 구조를 생략하지 말 것
- 상위 개념 1개로 덮기보다, 재사용 가능한 중간 anchor를 유지할 것

## 장문 문서 우선 체크

장문 문서를 처리할 때 아래 세 경계를 먼저 확인한다.

1. 요약/도입 vs 정의
2. 문제 제기 vs 해법 진술
3. 기술 메커니즘 vs 가치/활용

위 세 구간은 큰 블록으로 자동 흡수하지 말고,
의미축이 바뀌는지 먼저 점검한 뒤 fragment를 나눌 것.

## 강제 규칙

- `scene=definition` 금지
- `scene=example` 금지
- `scene=process` 금지
- `scene=thesis` 금지
- `scene=support` 금지

## 권장 기본값

- 정의 문단: `scene=explanation`, `role=definition`
- 사례 문단: `scene=explanation`, `role=example`
- 메커니즘 설명: `scene=explanation`, `role=support`
- 결론 문단: 우선 `scene=explanation`, `role=thesis` 또는 `role=expansion`

## 자기 점검

출력 전에 아래를 스스로 확인한다.

1. 내가 요약과 정의를 하나로 과도하게 합쳤는가?
2. 내가 문제와 해법을 한 덩어리로 뭉갰는가?
3. 내가 메커니즘과 가치/AI 활용을 같은 fragment로 과도하게 흡수했는가?
4. 내가 결론을 실제보다 더 meta/reflection으로 올렸는가?
5. 내가 scene에 비표준 값을 넣었는가?
