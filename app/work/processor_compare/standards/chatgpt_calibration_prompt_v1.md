# ChatGPT Calibration Prompt v1

목적:
- 장문 문서 처리 시 ChatGPT에서 반복적으로 관찰된 drift를 억제한다.
- 특히 과세분화, 높은 confidence, 낮은 ambiguity, scene enum 오용을 줄이는 데 목적이 있다.

이 프롬프트는 `processor_execution_prompt_v2.md`를 대체하지 않는다.
공통 프롬프트를 준 뒤, ChatGPT에게 추가 보정 지시로 붙인다.

## ChatGPT 추가 보정 지시

너는 장문 문서를 처리할 때 다음 경향을 보이지 않도록 주의해야 한다.

1. 과세분화 금지
- 문단이 조금 바뀐다고 바로 새 fragment로 자르지 말 것
- 같은 중심 의미 움직임이면 하나로 유지할 것
- 특히 문제 직후 짧은 해법 문장은 자동 분리하지 말 것

2. scene enum 오용 금지
- `definition`, `example`, `thesis`, `support`, `problem`, `bridge`는 role 값이다
- scene에 넣지 말 것
- 정의 문단도 기본적으로 `scene=explanation`, `role=definition`
- 사례 문단도 기본적으로 `scene=explanation`, `role=example`

3. 높은 confidence 자동 부여 금지
- 정의/설명 문단이라고 confidence를 자동으로 높이지 말 것
- fragment를 과감하게 잘랐다면 confidence를 보수적으로 낮출 것
- ambiguity를 너무 빨리 0.05 이하로 닫지 말 것

4. 해법/결론의 독립 thesis화 억제
- 해법 문장이 짧게 붙어 있으면 문제-해법 흐름으로 유지 가능한지 먼저 검토할 것
- 결론 문단이 실제 핵심 주장인지, 단순 요약/정리인지 구분할 것

5. anchor 과세분화 금지
- 비슷한 상위 개념을 서로 다른 micro-anchor로 과하게 쪼개지 말 것
- 재사용 가능한 중간 수준 anchor를 우선할 것

## 장문 문서 우선 체크

장문 문서를 처리할 때 아래 세 경계를 먼저 확인한다.

1. 요약/도입 vs 정의
2. 문제 제기 vs 해법 진술
3. 기술 메커니즘 vs 가치/활용

위 세 구간은 자동 분리하지 말고,
정말 의미축이 갈라지는지 먼저 확인한 뒤 fragment를 나눌 것.

## 강제 규칙

- `scene=definition` 금지
- `scene=example` 금지
- `scene=process` 금지
- `scene=thesis` 금지
- `scene=support` 금지

## 권장 기본값

- 정의 문단: `scene=explanation`, `role=definition`
- 사례 문단: `scene=explanation`, `role=example`
- 문제 문단: `scene=explanation`, `role=problem`
- 결론 문단: `scene=explanation`, `role=thesis`

## 자기 점검

출력 전에 아래를 스스로 확인한다.

1. 내가 문단을 너무 잘게 쪼갰는가?
2. role 값을 scene에 넣었는가?
3. confidence를 너무 높게 주고 ambiguity를 너무 낮게 주었는가?
4. 결론을 너무 빨리 thesis로 올렸는가?
