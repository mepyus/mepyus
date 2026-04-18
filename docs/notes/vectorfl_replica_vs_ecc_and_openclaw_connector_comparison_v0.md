# vectorfl_replica vs ecc and openclaw connector comparison v0

## purpose

이번 문서는
우리 저장소 `vectorfl_replica`를

- ECC식 reconstruction spine
- OpenClaw식 identity/session spine

과 직접 비교해서,
현재 무엇이 이미 있고 무엇이 아직 없으며
무엇이 실제로 필요한지를 판단하기 위한 메모다.

## 1. our current connector candidates

우리 저장소는 connector가 전혀 없는 상태가 아니다.
다만 그것들이 분산돼 있고,
아직 하나의 canonical connector layer로 읽히지는 않는다.

현재 눈에 띄는 connector 후보는 아래다.

### A. structured doc routing spine

중심:

- `scripts/process_structured_doc_with_routing.py`

현재 흐름:

- 문서 입력
- routing
- registry/provenance/event
- observer ingest
- receipt
- latest board / commands / surfaced views

즉 이것은 이미
`input -> routing -> manifest/receipt/view`
를 묶는 실제 spine이다.

### B. engine state bridge spine

중심:

- `app/runtime/engine_state_runtime_update_bridge.py`
- `app/runtime/engine_state_update_patch_builder.py`
- `app/core/state_store/engine_state_store.py`
- `app/core/state_store/engine_state_update_policy.py`

현재 흐름:

- runtime evidence 발생
- patch/proposal normalize
- policy 적용
- history append
- latest regenerate
- event surface write

즉 이것은 이미
`runtime evidence -> canonical state`
를 연결하는 bridge spine이다.

### C. observer exploration sidecar lane

중심:

- `runtime/observer/exploration/json/`
- `runtime/observer/exploration/md/`
- `docs/specs/exploration_observation_sidecar_contract_v1.md`

현재 역할:

- 얇은 observation packet 보존
- candidate/defer/future use readout

즉 아직 reconstruction entrypoint는 약하지만
readout lane은 이미 존재한다.

### D. engine state store / latest surface split

중심:

- `runtime/state/engine_state_history/*`
- `runtime/views/engine_state_latest/*`
- `docs/specs/engine_state_store_v1.md`

현재 역할:

- append-only history
- derived latest

즉 저장과 surfaced readout을 분리하는 관점은 이미 꽤 강하다.

## 2. ECC-style reconstruction spine comparison

### what ECC has

ECC는
여러 흩어진 표면을 다시 하나의 canonical readout으로 합치는 데 강하다.

대표:

- session adapter registry
- orchestration markdown + tmux snapshot 재조립
- state-store query surface

핵심은
원본이 여러 군데 흩어져 있어도
adapter/reconstruction layer가 그것을 다시 묶는다는 점이다.

### what we already have

우리 저장소에도 유사한 성격이 있다.

1. structured doc routing
   - 문서 입력 이후 여러 산출을 하나의 경로로 묶는다
2. engine state bridge
   - runtime evidence를 canonical state로 재조립한다
3. latest/history split
   - latest를 authoritative source로 보지 않고 파생 surface로 본다

즉 ECC와 완전히 같지는 않지만,
우리 저장소는 이미 reconstruction-friendly 방향에 서 있다.

### what we are missing

빠진 것은 lane 자체보다
reconstruction entrypoint의 선명함이다.

현재 부족한 점:

- `runtime/observer/exploration`를 다시 읽는 canonical entrypoint가 약하다
- 여러 receipt/view/observer artifact를 묶는 supervisor-facing reconstruction surface가 제한적이다
- structured doc routing spine가 특정 lane에 강하게 묶여 있어 repo-wide connector처럼 읽히진 않는다

### judgment

ECC식 reconstruction spine은
우리 저장소에 **상당히 필요하다**.

다만 형태는 ECC를 그대로 따라가면 안 된다.

왜냐하면:

- 우리는 multi-harness portability가 목적이 아니다
- 우리는 state store reporting보다 evidence reread와 surfaced interpretation이 중심이다

따라서 필요한 것은

- adapter-heavy ECC 복제

가 아니라

- `observer / receipt / manifest / view`를 다시 묶는
  **bounded reconstruction entrypoint**

다.

## 3. OpenClaw-style identity/session spine comparison

### what OpenClaw has

OpenClaw는
입력이 어느 agent/session으로 들어가는지를 가장 먼저 해결한다.

핵심:

- route resolution
- session-key normalization
- per-agent session path/store/cache/lock
- runtime assembly on top

즉 identity/session이 전체 구조의 1차 spine이다.

### what we already have

우리 저장소에도 session/run 흔적은 있다.

예:

- `run_id`
- `source_session`
- Gemini observer session 기록
- work session logs
- receipts와 commands surface

하지만 이것들은 운영 흔적과 provenance의 일부일 뿐,
전체 엔진의 1차 connector는 아니다.

### what we do not have

현재 우리 저장소에는 아래가 없다.

- agent/session destination을 먼저 정하는 router spine
- stable session key를 기준으로 전체 runtime을 묶는 계층
- per-agent workspace/session store/cache/lock 구조
- identity resolution을 중심에 둔 execution assembly

즉 OpenClaw식 identity/session 중심 구조는
현재 엔진의 본체와는 결이 다르다.

### judgment

OpenClaw식 identity/session spine은
현재 우리 저장소에 **핵심 우선순위는 아니다**.

이유:

1. 우리 엔진은 multi-channel agent routing product가 아니다
2. 현재 핵심 문제는 "누가 어느 session으로 가는가"보다
   "무슨 evidence가 어떤 readout과 state surface로 재구성되는가"다
3. session identity를 두껍게 만들면
   현재의 space-first, reread-first 방향보다 execution control-plane 쪽이 과도하게 커질 수 있다

단,
전혀 무가치는 아니다.

부분적으로 유효한 힌트:

- `run_id`, `source_session`, `observer session` naming 정규화
- session/run path를 더 일관되게 읽히게 만드는 규칙
- work session log와 runtime receipt 사이의 연결 명시

즉 full identity spine이 아니라
**lightweight run/session normalization**
정도는 유효하다.

## 4. side-by-side conclusion

### ECC-style reconstruction

- 현재 적합도: 높음
- 이유: 우리 저장소는 이미 evidence -> receipt/view/latest 재구성 흐름이 강하다
- 필요한 형태: repo-wide bounded reconstruction entrypoint

### OpenClaw-style identity/session

- 현재 적합도: 낮음에서 중간
- 이유: 우리 저장소의 본체는 routing product가 아니라 reread/evidence engine이다
- 필요한 형태: full session spine이 아니라 lightweight run/session normalization

## 5. what this means for our next design step

현재 가장 맞는 다음 질문은 아래다.

1. `runtime/observer/exploration`와 `runtime/receipts`, `runtime/views`를 함께 다시 읽는 reconstruction entrypoint를 만들 것인가
2. structured doc routing, engine state bridge, observer sidecar를 하나의 connector family로 명시할 것인가
3. session identity를 키우기보다 `run_id/source_session/observer_run_id/routing_run_id` 규칙을 더 선명하게 잠글 것인가

## 6. current judgment

한 줄로 잠그면 아래다.

- 우리 저장소에는 ECC식 reconstruction spine이 더 필요하다
- 우리 저장소에는 OpenClaw식 identity/session spine 전체가 아니라, 얇은 run/session normalization만 필요하다

즉 다음 구조설계의 중심은
`routing productization`이 아니라
`evidence reconstruction clarity`
여야 한다.
