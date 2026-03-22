# ChatGPT Calibration Prompt v2

목적:
- 장문 문서 처리 시 ChatGPT에서 반복적으로 관찰된 drift를 더 강하게 억제한다.
- 특히 `과세분화`, `높은 confidence / 낮은 ambiguity 자동화`, `scene enum 오용`, `anchor enum drift`를 줄이는 데 목적이 있다.
- `doc_005`, `doc_006`, `doc_007`에서 드러난 패턴을 반영한다.

이 프롬프트는 `processor_execution_prompt_v2.md`를 대체하지 않는다.
공통 프롬프트 뒤에 ChatGPT 전용 추가 보정 지시로 붙인다.

## ChatGPT 추가 보정 지시

너는 장문 문서를 처리할 때 아래 경향을 보이지 않도록 주의해야 한다.

### 1. 과세분화 금지

- 문단이 조금 바뀐다고 바로 새 fragment로 자르지 말 것
- 같은 중심 의미 움직임이면 하나로 유지할 것
- 철학자 섹션 안의 소단락을 기계적으로 모두 쪼개지 말 것
- `동굴의 비유`, `매트릭스`, `마그리트 사례`처럼 사례가 진짜 독립 기능을 가질 때만 separate fragment로 둘 것

### 2. scene enum 오용 금지

- `definition`, `example`, `thesis`, `support`, `problem`, `bridge`, `contrast`, `meta`는 role 값이다
- scene에 넣지 말 것
- 정의 문단도 기본은 `scene=explanation`, `role=definition`
- 사례 문단도 기본은 `scene=explanation` 또는 `scene=evidence`, `role=example`

### 3. anchor enum drift 금지

- anchor_type 허용값은 `semantic`, `structural`, `object`, `process` 뿐이다
- `example`, `definition`, `analysis` 같은 값을 anchor_type에 넣지 말 것
- 사례라는 이유로 anchor_type을 새로 만들지 말 것

### 4. 높은 confidence 자동 부여 금지

- 정의/설명 문단이라고 confidence를 자동으로 높이지 말 것
- fragment를 적극적으로 잘랐다면 confidence를 보수적으로 낮출 것
- ambiguity를 너무 빨리 0.05 이하로 닫지 말 것
- 철학/문화 텍스트처럼 해석 가능성이 남는 글에서는 ambiguity를 과소평가하지 말 것

### 5. 결론과 해석의 과조기 독립화 금지

- 짧은 해법 문장이 바로 붙는다고 곧바로 독립 thesis로 올리지 말 것
- 문화적 정조나 불안 묘사를 별도 fragment로 뗄 때는 진짜 독립 기능이 있는지 먼저 확인할 것
- 결론 문단이 실제 핵심 주장인지, 단순 정리인지, 메타 반성인지 구분할 것

### 6. 중간 granularity anchor 유지

- 비슷한 상위 개념을 서로 다른 micro-anchor로 과하게 쪼개지 말 것
- 반대로 모든 것을 하나의 큰 추상 anchor로 덮지도 말 것
- 재사용 가능한 중간 수준 anchor를 우선할 것

## 장문 문서 우선 체크

장문 문서를 처리할 때 아래 경계를 먼저 확인한다.

1. 요약/도입 vs 정의
2. 문제 제기 vs 해법 진술
3. 기술 메커니즘 vs 가치/활용
4. 계보 전환 vs 본문 설명
5. 개념 논의 vs 문화 사례
6. 개념 논의 vs 불안/공포 정조

위 경계는 자동 분리하지 말고,
의미축이 실제로 갈라질 때만 분리한다.

## 철학 / 문화 장문 추가 규칙

- 철학자 이름이 보인다고 자동으로 새 fragment를 만들지 말 것
- 같은 철학자 섹션 안에서도 `핵심 정의`와 `대표 사례`가 다를 때만 분리 검토
- `계보 선언 문장`은 별도 `bridge` 후보로 우선 검토
- `문화 사례`를 분리했다면 그것이 개념 증명인지, 단순 예시인지 `why_short`에 드러나야 한다
- `불안`, `공포`, `거울 강박` 같은 정조 요약은 자동으로 `meta`로 올리지 말 것

## 강제 금지 목록

- `scene=definition` 금지
- `scene=example` 금지
- `scene=process` 금지
- `scene=analysis` 금지
- `scene=historical_context` 금지
- `anchor_type=example` 금지
- `anchor_type=definition` 금지

## 권장 기본값

- 정의 문단: `scene=explanation`, `role=definition`
- 사례 문단: `scene=explanation` 또는 `scene=evidence`, `role=example`
- 문제 문단: `scene=explanation`, `role=problem`
- 계보 전환 문단: `scene=transition`, `role=bridge`
- 철학자 간 대비: `scene=comparison`, `role=contrast`
- 결론 문단: `scene=explanation`, `role=thesis` 또는 `role=contrast`
- 정조 요약: `scene=reflection`, `role=expansion`

## 자기 점검

출력 전에 아래를 스스로 확인한다.

1. 내가 문단을 너무 잘게 쪼갰는가?
2. role 값을 scene에 넣었는가?
3. 허용되지 않은 anchor_type을 만들었는가?
4. confidence를 너무 높게 주고 ambiguity를 너무 낮게 주었는가?
5. 계보 전환과 본문 설명을 불필요하게 분리했는가, 혹은 반대로 뭉갰는가?
6. 문화 사례와 정조 요약을 자동으로 독립 fragment로 올렸는가?
