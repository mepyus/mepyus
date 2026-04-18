# VectorFL Line Facet v0

## 핵심 원칙

라인은 하나의 살아 있는 해석 단위로 유지한다.
다만 그 안에 들어 있는 의미를 facet로 분리해서 보이게 한다.

즉 아래 셋을 분리한다.

- `line`
- `facet`
- `pipeline`

여기서

- `line` 은 중심 객체
- `facet` 는 그 line을 구성하는 의미 면
- `pipeline` 은 그 line을 처리하는 절차

이다.

## 1. line의 최소 공통 facet

모든 line에는 최소 네 개 facet가 공통으로 들어간다.

### 1. material_facet

이 line이 무엇을 재료로 삼았는가

예:

- 원문 조각
- 이벤트
- 상태 변화
- 로그
- 과거 residue
- reference

이게 없으면 line이 공중에 뜬다.

### 2. distinction_facet

이 line이 무엇을 무엇과 다르게 보았는가

예:

- 단순 지연 vs 구조적 병목
- 상태 변화 vs 판단 변화
- 절차 누락 vs capacity 문제
- 예외적 사고 vs 반복 패턴

같은 재료도 구별이 다르면 전혀 다른 line이 된다.

### 3. linkage_facet

이 line이 무엇과 무엇을 연결하는가

예:

- 현재 hold ↔ 과거 bay conflict residue
- operator note ↔ phase transition
- 공정 흐름 ↔ 실제 상태 이벤트

이 facet가 있어야 line이 점이 아니라 결이 된다.

### 4. direction_facet

이 line이 어디로 읽게 하는가

예:

- 원인 추적 쪽으로 읽게 함
- 다음 전환 조건을 보게 함
- 예외 관리 쪽으로 읽게 함
- 재검토/승인 흐름으로 읽게 함

이게 없으면 line은 연결 메모에 머문다.

## 2. line의 확장 facet

모든 line에 반드시 필요하진 않지만,
VectorFL을 실제로 굴릴 때 중요하게 붙는 면이다.

### 5. operation_facet

이 line이 실제로 무엇을 하게 만드는가

예:

- why-blocked 설명
- 다음 위치 추천
- hold 해제 검토 요청
- 재세척 후보 제안

즉 line의 실행성이다.

### 6. residue_facet

이 line이 이후에 무엇을 남기는가

예:

- future candidate
- drift 징후
- 재호출 anchor
- 설명 패턴
- 예외 기억

즉 line의 재생산성이다.

## 3. 최소 구조

```text
line
├─ material_facet
├─ distinction_facet
├─ linkage_facet
├─ direction_facet
├─ operation_facet   (optional but recommended)
└─ residue_facet     (optional but recommended)
```

이 방식은 line을 쪼개 없애는 것이 아니라,
한 line 안에 있는 풍부함을 면으로 드러내는 것이다.

## 4. line type은 facet와 별도로 둔다

facet와 type을 섞지 않는다.

- `facet` 는 한 line 내부 구조
- `type` 은 그 line의 역할 분류

v0에서는 type을 네 개만 둔다.

- `reading_line`
- `structural_line`
- `decision_line`
- `residue_line`

예:

- `type = decision_line`
- `facet = material / distinction / linkage / direction / operation / residue`

## 5. 예시: 탱크 프로그램 line

예:

- `inspect hold explanation` line

type:

- `decision_line`

facets:

### material_facet

- wash 완료 이벤트
- inspect bay 상태
- hold 등록 로그
- operator review requirement

### distinction_facet

- 단순 지연이 아니라 capacity-based hold로 읽음
- 상태 미변경이 아니라 전환 차단으로 읽음

### linkage_facet

- wash completed ↔ inspect transition
- inspect transition ↔ bay capacity
- bay capacity ↔ hold registration
- hold registration ↔ operator review requirement

### direction_facet

- 현재 상태 설명으로만 보지 않고
- 왜 inspect로 못 갔는가의 원인 line으로 읽게 함

### operation_facet

- why-blocked 설명
- 관련 이벤트 표시
- review 요청 action 후보 생성

### residue_facet

- 이후 유사 hold 설명 시 capacity + review를 함께 보여줘야 한다는 residue 남김

## 6. 왜 이 방식이 좋은가

장점은 세 가지다.

### 1. line의 풍부함을 유지한다

line을 단계로 쪼개 죽이지 않는다.

### 2. Codex가 무엇을 했는지 보이게 된다

예:

- 번역을 했는지
- 구별을 바꿨는지
- 연결을 새로 만들었는지

가 보인다.

### 3. LLM 입력 구조로 바로 쓰기 좋다

로컬 LLM은 raw 문서보다
이런 구조화된 facet를 더 잘 다룬다.

## 7. pipeline과의 관계

이건 매우 중요하다.

facet는
line이 무엇으로 이루어지는가
를 보여준다.

pipeline은
line을 어떻게 다루는가
를 보여준다.

즉 둘은 다르다.

예:

pipeline:

- detect
- translate
- compare
- select
- observe
- reinject

facet:

- material
- distinction
- linkage
- direction
- operation
- residue

앞은 절차이고,
뒤는 구조다.

## 8. Codex용 최소 지시 문장

앞으로는 아래 문장을 기준 지시로 쓴다.

> 이번 line을 하나의 객체로 유지하되, 최소한 material_facet, distinction_facet, linkage_facet, direction_facet를 분리해 적고, 가능하면 operation_facet과 residue_facet까지 채워라.

이렇게 하면
단순히 line을 만들었다가 아니라
어떤 면에서 그 line을 구성했는지가 보인다.

## 9. 현재 v0 판단

지금 단계에서는 아래 구분이 가장 적절하다.

- `line` = 하나의 살아 있는 해석 단위
- `facet` = 그 line을 구성하는 의미 면
- `type` = 그 line의 역할
- `pipeline` = 그 line을 다루는 절차

이 네 개를 분리하면,
라인의 풍부함을 살리면서도 훨씬 명시적으로 다룰 수 있다.

## 10. 한 줄 요약

라인을 나눈다는 건 line을 쪼개 없애는 게 아니라,
한 line 안에 들어 있는 의미의 여러 면을 facet로 분리해서 드러내는 것이다.
