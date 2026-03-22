# doc_005 Analysis

## 적합성 판단

- 비교 실험용으로 매우 적절하다.
- 블로그형 설명문이지만 정의, 예시, 문제 제기, 구조 설명, 운영 확장까지 모두 들어 있다.
- 처리자별 절단 기준, 추상화 수준, anchor granularity 차이를 넓게 볼 수 있다.

## Codex 기준선 절단 판단

### fragment 1
- 범위: 팔란티어 소개와 온톨로지 핵심 요약
- 중심 움직임: `palantir ontology summary`

### fragment 2
- 범위: Ontology를 디지털 트윈으로 설명하는 정의 구간
- 중심 움직임: `ontology as digital twin`

### fragment 3
- 범위: 블로그 작성 예시로 현실을 객체/관계/행동으로 쪼개는 설명
- 중심 움직임: `objectification example`

### fragment 4
- 범위: 현실의 데이터 사일로 문제와 온톨로지 필요성
- 중심 움직임: `silo problem and ontology value`

### fragment 5
- 범위: Object / Property / Link / Action 개요
- 중심 움직임: `ontology component overview`

### fragment 6
- 범위: Object Type 설명과 비즈니스 컨테이너 성격
- 중심 움직임: `object type container`

### fragment 7
- 범위: Property 설명과 계산 지표 포함 의미
- 중심 움직임: `property extended attribute`

### fragment 8
- 범위: Link Type 설명, 세 관계 방식, 관계의 의미적 활용
- 중심 움직임: `link type relational reasoning`

### fragment 9
- 범위: Action Type과 운영계 접점 설명
- 중심 움직임: `action type operational bridge`

### fragment 10
- 범위: Object / Property / Link / Action 통합과 디지털 트윈 결론
- 중심 움직임: `digital twin operating system`

## 관찰 포인트

- 처리자마다 `Object / Property / Link / Action`을 각각 독립 fragment로 분리하는지, 일부를 합치는지 차이가 날 수 있다.
- 예시 구간을 `example`, `support`, `instruction` 중 무엇으로 읽는지 흔들릴 수 있다.
- `reasoning`, `automation`, `digital_twin`, `operating_system` 같은 추상 태그는 Gemini/ChatGPT에서 과확장될 가능성이 있다.

## 비교 메모

- Codex는 10 fragment로 절단했고, `요약 -> 정의 -> 예시 -> 문제 -> 구성 개요 -> Object -> Property -> Link -> Action -> 결론` 흐름을 가장 구조적으로 유지했다.
- ChatGPT는 12 fragment로 가장 잘게 자르며, 특히 `문제`와 `해법`, `Link 메커니즘`과 `Link 가치`, `결론`을 더 세분화한다.
- Gemini는 9 fragment로 가장 크게 묶으며, `도입+정의`, `문제+필요성`, `Link 메커니즘`과 `Link 가치`를 압축하거나 추상화한다.
- ChatGPT는 여전히 `scene=definition`, `scene=example` 같은 enum 오용이 반복되어 schema 준수 면에서 가장 취약하다.
- Gemini는 schema는 지키지만 `reflection`, `meta`, `expansion`을 더 쉽게 부여하며 원문보다 한 단계 추상화된 설명으로 이동하는 경향이 있다.
- 축값 평균은 Codex보다 ChatGPT와 Gemini가 더 높고 ambiguity는 더 낮다. 이 패턴은 `doc_001~004`와 동일하게 반복된다.
