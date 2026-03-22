# space is a view, not the engine

## 1. purpose
- 이 문서는 `space`를 엔진 본체로 보지 않고, 엔진 출력을 읽는 하나의 표현 방식으로 고정하기 위한 정책 메모다
- 핵심은 `공간`보다 `출력 안정성`, `연결 층위`, `과정 추적`, `보류 자산 보존`을 엔진의 본체로 두는 것이다

## 2. core statement
- 우리가 만드는 것은 `space app` 자체가 아니다
- 우리가 만드는 것은
  - 입력기
  - 라벨기
  - 앵커기
  - 연결 층위 판독
  - review / blocker / proposal / promotion trace
  를 일관되게 생성하고 저장하고 다시 읽을 수 있는 엔진이다
- `space`는 그 엔진을 읽는 하나의 surface 이다

## 3. engine first reading
- 엔진의 본체는 아래에 있다
  - input output stability
  - label / anchor consistency
  - connection tier generation
  - blocker preservation
  - deferred asset preservation
  - review and promotion trace

## 4. what space means under this policy
- space는 연결 구조를 읽는 한 가지 방식이다
- 즉 같은 엔진 출력은 아래처럼 여러 방식으로 읽힐 수 있다
  - space view
  - graph view
  - table / ledger
  - review queue
  - promotion trace
  - database query result

## 5. practical consequence
- 입력기 + 라벨기 + 앵커기가
  - 충분히 일관되고
  - 확률적으로 비슷한 결과를 반복해서 내고
  - weak / strong / blocked / review 상태를 같은 문법으로 남길 수 있다면
- 우리는 이미 엔진을 가진 것이다
- 그 출력을 반드시 `space`로만 봐야 하는 것은 아니다

## 6. current repo implication
- viewer는 frozen Phase 1 surface다
- 현재 메인 자산은 viewer가 아니라 runtime engine 쪽에 있다
- 중요한 것은
  - canonical / possibility / review / blocker / proposal / pre-entry
  구조를 계속 엔진 안에 남기는 것이다
- space는 그것을 operator가 읽는 하나의 작업대다

## 7. final sentence
- space는 엔진의 본체가 아니다
- space는 엔진이 만든 연결 구조를 읽는 하나의 view 이다
- 엔진의 본체는
  - 일관된 입력 출력
  - 연결 층위 생성
  - 보류 자산 보존
  - 과정 추적
  에 있다
