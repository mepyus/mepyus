# washtank_structure_line_review_v1

## verdict

- `references/WashTank`는 React + Vite 프론트엔드 위에 `JMS` 서비스 레이어를 얹은 프로그램이다.
- 이 프로그램의 가장 굵은 선은 `main orchestration line`과 `jms service line`이다.
- 하지만 실제 코드에는 `direct rpc bypass line`과 `supabase client split line`이 같이 살아 있어서 connector family가 부분적으로 갈라져 있다.

## review focus

- `git_search`에서 잡은 line 기준을 적용했다.
- 특히 아래 선을 중심으로 읽었다.
  - main orchestration line
  - service connector line
  - state / observation read-model line
  - direct bypass line
  - client split line

## primary findings

### 1. main orchestration line is concentrated in `main.jsx`

- 진입점은 [main.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/main.jsx#L1) 이다.
- 이 파일은 단순 router가 아니라 아래를 모두 가진다.
  - global state hub
  - all-data sync hub
  - action gateway
  - page router
  - menu/dashboard shell

중요 지점:

- `syncAll()`이 전체 read path를 묶는다
- `triggerAction()`이 상태 전이 gateway 역할을 한다
- `renderView()`가 페이지 배분기다

판단:

- 이 앱의 body는 page들이 아니라 `main.jsx`다.
- page tree보다 `main.jsx -> jms.js -> supabase/rpc` 선이 더 중요하다.

### 2. jms service line is the real control spine

- [jms.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/jms.js#L1) 는 observation, mutation, rpc wrapper를 한 파일에서 거의 다 담당한다.
- 실제 규칙 선언도 이 파일에 적혀 있다.
  - 상태 전이 = trigger_event_v2
  - job 생성 = create_job_v2
  - 위치 이동 = rpc_move_tank_location
  - 출고 요청 = outbound_requests + outbound RPC

판단:

- 이 repo에서 실제 connector spine은 route file이 아니라 `services/jms.js`다.
- page들은 거의 모두 이 service line 위에 올라탄 thin operator surface로 읽는 것이 맞다.

### 3. declared service-only rule is broken by direct rpc bypasses

- `main.jsx` 상단 주석은 “모든 데이터 통신은 jms 서비스 레이어를 통해서만 수행”이라고 잠근다.
- 그런데 실제로는 아래가 service line을 우회한다.
  - [Ehandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/Ehandler.jsx#L1)
  - [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/Fhandler.jsx#L340)
- 이 둘은 `supabase.rpc("rpc_assign_tank_yard_location", ...)`, `supabase.rpc("rpc_assign_tank_location_id", ...)`를 직접 호출한다.

판단:

- 선언된 connector family는 `page -> jms -> supabase/rpc`인데
- 실제 구현은 일부 페이지에서 `page -> supabase/rpc` 우회선을 열고 있다.

이게 만드는 문제:

- action contract가 page별로 새어 나온다
- rpc naming / payload rule이 page 안에 퍼진다
- 나중에 logging, retry, guard, actor normalization을 일괄 적용하기 어렵다

### 4. supabase client split line is inconsistent

- [supabaseClient.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/supabaseClient.js#L1) 는 하드코딩된 URL/anon key를 쓴다.
- [services/supabase.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/supabase.js#L1) 는 `VITE_SUPABASE_*` env 기반이다.
- [jms.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/jms.js#L16) 는 `../supabaseClient`를 쓴다.
- [jms_core.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/jms_core.js#L1) 는 `./supabase`를 쓴다.

판단:

- 이건 단순 중복이 아니라 client authority split이다.
- 결국 `jms.js` line과 `jms_core.js` line이 같은 backend contract를 가리키더라도, credential/source-of-truth가 갈라져 있다.

이게 의미하는 것:

- 어떤 서비스 라인이 canonical인지 애매하다
- local/dev/prod 환경 전환 시 drift risk가 크다
- reference 구조를 재사용할 때도 그대로 가져오기 어렵다

### 5. `jms_core.js` is a secondary line, not the dominant one

- [jms_core.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/jms_core.js#L1) 는 더 정돈된 core wrapper처럼 보인다.
- `execute_job_lifecycle_v2`를 중심으로 helper를 얇게 얹는다.
- 하지만 실제 앱의 main line은 이것이 아니라 `jms.js` 쪽이다.

판단:

- 이 프로그램에는 “정리된 core line”과 “실사용 fat service line”이 동시에 있다.
- 현재 운영 truth는 `jms_core.js`보다 `jms.js`에 더 가깝다.

### 6. read-model normalization line exists inside main app instead of dedicated view service

- `normalizeInspectionQueueRow()` 같은 read-model 함수가 [main.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/main.jsx#L57) 안에 있다.
- `fetchInspectionQueue()`도 read-model fallback까지 main에서 처리한다.

판단:

- 이 앱은 page rendering line과 read-model composition line이 완전히 분리돼 있지 않다.
- 즉 `main.jsx`가 controller + adapter + router를 동시에 가진다.

## connector family reading

### line 1. main orchestration line

- file:
  - [main.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/main.jsx#L1)
- role:
  - page routing
  - sync hub
  - action gateway
  - menu shell

### line 2. service connector line

- file:
  - [jms.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/jms.js#L1)
- role:
  - observation queries
  - rpc wrapper
  - job/status/location action contract

### line 3. direct bypass line

- files:
  - [Ehandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/Ehandler.jsx#L1)
  - [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/Fhandler.jsx#L340)
- role:
  - direct location rpc invocation

### line 4. client split line

- files:
  - [supabaseClient.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/supabaseClient.js#L1)
  - [services/supabase.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/supabase.js#L1)
- role:
  - duplicate backend client roots

### line 5. secondary clean-core line

- file:
  - [jms_core.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/services/jms_core.js#L1)
- role:
  - more canonical job lifecycle wrapper
- current status:
  - structurally cleaner but not the dominant live spine

## what this program is structurally

- 이 프로그램은 “page bundle”이 아니다.
- 더 정확히는 아래 구조다.

`UI pages -> MainApp orchestration -> JMS fat service -> Supabase RPC/table layer`

다만 예외선이 두 개 있다.

- direct rpc bypass
- split supabase client authority

그래서 이 repo는 clean service-led app이 아니라
`service-led app with local bypass seams`
로 읽는 것이 맞다.

## review summary

- 강점:
  - `main.jsx`와 `jms.js`를 보면 실제 spine이 어디인지 비교적 빨리 잡힌다
  - 서비스 레이어에 도메인 동사가 모여 있어서 업무 흐름을 읽기 쉽다
  - inspection queue처럼 read-model 의도가 분명한 부분이 있다

- 약점:
  - service-only rule이 실제 코드에서 깨진다
  - supabase client authority가 갈라져 있다
  - `main.jsx`가 너무 많은 역할을 먹고 있다
  - cleaner core line인 `jms_core.js`가 실사용 line과 분리돼 있다

## translation hint for our line reading

- 이 reference에서 가져갈 만한 것은 “service connector를 중심에 두는 사고”다.
- 가져오면 안 되는 것은 “page에서 직접 rpc를 열어도 된다는 관성”이다.
- 특히 우리 쪽 line으로 번역하면:
  - `main orchestration line`
  - `service connector line`
  - `bypass seam detection`
  - `client authority split detection`

을 같이 보는 게 맞다.

## one-line lock

> WashTank는 `main.jsx -> jms.js -> supabase/rpc`가 가장 굵은 live connector line인 React 운영앱이지만, `Ehandler/Fhandler`의 direct rpc bypass와 `supabaseClient.js / services/supabase.js` 이중화 때문에 connector family가 부분적으로 갈라진 reference다.
