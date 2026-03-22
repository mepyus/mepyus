# engine body structure draft v0

## 0. one-line definition

**이 엔진의 본체는 그래프가 아니라, 입력에서 생성된 값과 연결 층위를 저장·보류·재판독하는 구조다. 그래프는 그 본체를 읽는 하나의 투영면이다.**

## 1. what the engine body is

### A. ledger body

ledger body는 기록하는 몸통이다.

여기에는 아래가 남는다.

- 입력 원본과 분해 단위
- anchor / processing / handle / local_ref
- canonical / possibility / review / blocker / proposal / pre-entry
- lifecycle
- revisit 필요성
- state signature
- review ledger

즉 ledger body는
**무슨 일이 있었고, 지금 어디 있으며, 왜 거기 있는지**를 붙잡아두는 몸통이다.

### B. layer board body

layer board body는 상태 층위를 잡는 몸통이다.

입력이나 후보는 하나의 평면 점이 아니라 각자 층위를 가진다고 본다.

예:

- none
- possibility
- review
- space pre-entry
- canonical
- archived / cold

즉 layer board는
**이 재료가 지금 어느 층에 머물고 있고, 왜 못 넘어가고 있는지**를 보는 구조다.

## 2. what the engine body is not

### graph is not the engine body

그래프는 여전히 필요하지만 본체는 아니다.

그래프는:

- 어떤 것들이 대략 연결되는지
- 어떤 군집이 보이는지
- 어떤 축이 넓게 퍼져 있는지

를 보여주는 projection이다.

즉 graph는 본체를 읽는 한 방식일 뿐이다.

## 3. what the field of judgment is

### local workbench

local workbench는 국소 작업대다.

예를 들어 `doc_006` 같은 후보에서 중요한 건 문서 전체가 아니라 `best_local_ref` 주변이다.

workbench에는 아래가 올라온다.

- 원문 local_ref
- translated handles
- processing residual
- family support
- canonicalization proposal
- blockers
- next review target

즉 local workbench는
**왜 이 후보가 여기까지 왔고, 왜 여기서 막혔는가**를 읽는 현장이다.

이건 디버그용 보조 화면이 아니라 엔진 판단이 실제로 일어나는 현장형 그릇이다.

## 4. full structure

### engine body

- ledger body
- layer board body

### field

- local workbench

### projections

- graph view
- space view
- timeline view
- review surface

즉 구조는 이렇게 읽는다.

**Ledger가 기억하고, Layer가 상태를 잡고, Workbench가 국소 판단을 하고, Graph/Space는 그것을 보여준다.**

## 5. why this structure fits

### 1. because the engine already went beyond graph

지금 엔진은 단순 점/선만 다루지 않는다.

현재 다루는 것:

- weak trace
- review lane
- promotion review
- lifecycle
- revisit
- hot / warm / cold
- fixture / control
- canonical과 space의 분리

이건 그래프 하나로 본체를 설명할 수 없다.

### 2. because it matches the engine philosophy

이 엔진은 연결을 하나의 정답선으로 보지 않는다.

- 같음
- 유사
- 연결 가능
- 강한 연결
- 보류 자산

가 중요하다.

그러므로 본체는
**층위를 보존하는 구조**여야 한다.

### 3. because it fits future model attachment

나중에 예측 모델, 시나리오 모델, 학습 모델이 붙으려면 그래프 그림보다 먼저 필요한 건:

- 값 생성 이력
- 상태 변화
- 후보 보류 이력
- local_ref 단위 근거
- lifecycle

이다.

즉 미래 확장도 ledger/layer 중심 구조가 본체여야 가능하다.

## 6. simple role summary

### ledger

무슨 일이 있었나?

### layer

지금 어디 있나?

### workbench

왜 여기 있나? 다음엔 뭘 봐야 하나?

### graph

대략 뭐랑 뭐가 닿아 있나?

### space view

이걸 공간적으로 읽으면 어떤 풍경인가?

## 7. mapping to current engine

### already in ledger body

- review_state_ledger
- state_signature
- evaluated_at
- trace_temperature
- lifecycle_stage
- lifecycle_reason
- proposal / blocker / review 기록

### already in layer board body

- none
- possibility
- review
- space pre-entry
- canonical
- blocked_waiting_revisit
- approved_active

### already in local workbench

- best_local_ref
- translation hit
- processing residual
- family support
- canonicalization proposal trace
- next_review_blocker

### already in projections

- graph view
- space entry reading
- review output surface

즉 이 구조는 새로 만드는 것이라기보다,
**이미 생긴 걸 바르게 이름 붙이는 작업**에 가깝다.

## 8. locked sentences

### engine definition

우리는 space를 만드는 게 아니라, 입력 위에서 연결 층위를 생성·저장·재판독하는 엔진을 만든다.

### body definition

그 엔진의 본체는 ledger와 layer다.

### field definition

실제 판단과 검토는 local workbench에서 일어난다.

### view definition

graph와 space는 본체가 아니라 읽기면이다.

## 9. final summary

**엔진 본체는 Ledger Body와 Layer Board Body이며, Local Workbench는 그 본체의 국소 판단 현장이다. Graph와 Space는 본체가 아니라 그 상태를 읽는 projection이다.**

## 10. final lock

**그래프는 지도이고, 작업대는 현장이며, 진짜 엔진의 그릇은 ledger와 layer다.**
