# Gemini Calibration Prompt v2

목적:
- 장문 문서 처리 시 Gemini에서 반복적으로 관찰된 drift를 더 강하게 억제한다.
- 특히 `대묶음`, `추상화 확대`, `meta/reflection 과상승`, `비표준 scene 생성`, `입력 메타 임의 수정`을 줄이는 데 목적이 있다.
- `doc_005`, `doc_006`, `doc_007`에서 드러난 패턴을 반영한다.

이 프롬프트는 `processor_execution_prompt_v2.md`를 대체하지 않는다.
공통 프롬프트 뒤에 Gemini 전용 추가 보정 지시로 붙인다.

## Gemini 추가 보정 지시

너는 장문 문서를 처리할 때 아래 경향을 보이지 않도록 주의해야 한다.

### 1. 과대묶음 금지

- 요약/정의, 문제/해법, 메커니즘/가치, 과제/결론을 자동으로 하나의 큰 블록으로 흡수하지 말 것
- 계보 전환, 화폐/매트릭스 같은 보조 사례, 불안/공포 정조를 쉽게 흡수하지 말 것
- 의미축이 바뀌면 separate fragment 후보로 먼저 검토할 것

### 2. 상위 추상화 과잉 금지

- 원문에 있는 중간 손잡이를 지우고 지나치게 큰 상위 개념 하나로 덮지 말 것
- `ontology_centric_system`, `digital_twin_reflection`, `philosophical_essay_summary` 같은 과도한 상위 추상화는 억제할 것
- anchor 수를 줄이기 위해 중요한 중간 구조를 생략하지 말 것

### 3. meta / reflection 과사용 금지

- 결론이라고 자동으로 `scene=reflection`, `role=meta`로 올리지 말 것
- 철학 글이라고 자동으로 `reflection`을 부여하지 말 것
- 실제 메타 총평이 아닌 경우 기본은 `scene=explanation`
- 들뢰즈 같은 결론부도 먼저 `comparison + contrast` 또는 `explanation + thesis/expansion` 후보로 본다

### 4. 비표준 scene 생성 금지

- scene 허용값 밖의 새 범주를 만들지 말 것
- `definition`, `example`, `process`, `analysis`, `historical_context`, `technical_reflection`, `thesis`, `support`를 scene으로 사용하지 말 것
- 절차 설명도 기본은 `scene=explanation`
- 역사적 배경 설명도 기본은 `scene=explanation` 또는 `scene=transition`

### 5. 입력 메타 임의 수정 금지

- `input_doc_id`, `input_bundle_id`, `source_type`, `fragment_version`는 입력값을 그대로 유지할 것
- `bundle_simulacra_v1`, `philosophical_essay` 같은 새 메타 값을 만들지 말 것
- 원문을 `...`로 줄여 쓰지 말고 해당 fragment에 포함된 실제 원문을 보존할 것

### 6. 중간 anchor granularity 유지

- 모든 것을 하나의 상위 anchor로 덮지 말 것
- 그렇다고 anchor를 과도하게 늘리지도 말 것
- 재사용 가능한 중간 수준 anchor를 유지할 것

## 장문 문서 우선 체크

장문 문서를 처리할 때 아래 경계를 먼저 확인한다.

1. 요약/도입 vs 정의
2. 문제 제기 vs 해법 진술
3. 기술 메커니즘 vs 가치/활용
4. 계보 전환 vs 본문 설명
5. 개념 논의 vs 문화 사례
6. 개념 논의 vs 불안/공포 정조

이 경계들을 큰 블록으로 자동 흡수하지 말고,
의미축이 바뀌는지 먼저 점검한 뒤 fragment를 나눌 것.

## 철학 / 문화 장문 추가 규칙

- 철학자 섹션을 자동으로 큰 요약 블록 하나로 압축하지 말 것
- `화폐 예시`, `매트릭스`, `거울 강박`처럼 개념 작동 방식을 보여주는 사례를 쉽게 생략하지 말 것
- `플라톤부터 들뢰즈까지` 같은 계보 전환문은 별도 `bridge` 후보로 검토
- `불안/공포` 묘사는 단순 사례인지, 문화적 정조 요약인지 구분해서 판정할 것
- `정조 요약`을 메타로 올릴 때는 실제로 한 단계 위 해석인지 먼저 점검할 것

## 강제 금지 목록

- `scene=definition` 금지
- `scene=example` 금지
- `scene=process` 금지
- `scene=analysis` 금지
- `scene=historical_context` 금지
- `scene=technical_reflection` 금지
- 입력 메타 임의 수정 금지

## 권장 기본값

- 정의 문단: `scene=explanation`, `role=definition`
- 사례 문단: `scene=explanation` 또는 `scene=evidence`, `role=example`
- 메커니즘 설명: `scene=explanation`, `role=support`
- 계보 전환 문단: `scene=transition`, `role=bridge`
- 철학자 간 대비: `scene=comparison`, `role=contrast`
- 결론 문단: 우선 `scene=explanation`, `role=thesis` 또는 `role=contrast`
- 정조 요약: `scene=reflection`, `role=expansion`

## 자기 점검

출력 전에 아래를 스스로 확인한다.

1. 내가 요약과 정의를 하나로 과도하게 합쳤는가?
2. 내가 문제와 해법을 한 덩어리로 뭉갰는가?
3. 내가 메커니즘과 가치/활용을 같은 fragment로 과도하게 흡수했는가?
4. 내가 계보 전환이나 사례 fragment를 누락시켰는가?
5. 내가 scene에 비표준 값을 넣었는가?
6. 내가 입력 메타를 임의로 바꿨는가?
7. 내가 결론을 실제보다 더 meta/reflection으로 올렸는가?
