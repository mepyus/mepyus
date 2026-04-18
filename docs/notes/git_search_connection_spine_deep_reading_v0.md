# git_search connection spine deep reading v0

## purpose

이번 문서는 앞선 구조 비교보다 한 단계 더 내려가서
각 프로그램의 연결 spine을 본다.

여기서 spine은 단순 엔트리포인트가 아니라

- 어떤 호출 사슬이 실제 실행 경로를 만들고
- 어떤 상태 저장층이 여러 폴더를 하나로 묶고
- 어디서 여러 파일이 다시 하나의 canonical readout으로 합쳐지는가

를 뜻한다.

이번 세션에서 특히 밀도 높게 본 대상은

- `everything-claude-code-main`
- `openclaw-main`

이다.

## 1. ECC deep spine

### 1.1 top connector

ECC의 1차 spine은 `scripts/ecc.js`다.

역할:

- 명령 문자열을 해석한다
- 어떤 스크립트가 실제 실행 대상인지 결정한다
- install/plan/catalog/status/sessions/session-inspect 같은 명령들을 라우팅한다

즉 여기서
폴더들은 아직 분리된 surface지만,
`ecc.js`가 그것들을 하나의 command shell로 묶는다.

### 1.2 install spine

install 계열 호출 사슬은 아래처럼 읽힌다.

1. `scripts/ecc.js`
2. `scripts/install-plan.js` 또는 `scripts/install-apply.js`
3. `scripts/lib/install-manifests.js`
4. `scripts/lib/install-targets/*`
5. 설치 대상 harness surface

핵심 포인트:

- 폴더는 `commands`, `skills`, `rules`, `hooks`처럼 흩어져 있지만
- install spine은 manifest를 통해 그들을 module/component 단위로 다시 묶는다
- 즉 실제 연결기는 폴더 tree 자체가 아니라 manifest resolver다

### 1.3 session inspection spine

session inspection spine은 더 중요하다.

호출 사슬:

1. `scripts/session-inspect.js`
2. `scripts/lib/session-adapters/registry.js`
3. adapter 선택
   - `claude-history`
   - `dmux-tmux`
4. adapter별 source reading
5. canonical snapshot 반환

핵심 포인트:

- session source가 하나가 아니다
- 그래서 repo는 "원본 session 파일"을 canonical source로 두지 않는다
- adapter registry가 여러 source를 동일 snapshot shape로 번역한다

즉 여기서 canonical unit은
raw file이 아니라 adapter output이다.

### 1.4 orchestration reconstruction spine

`scripts/lib/orchestration-session.js`는
ECC가 여러 markdown 파일을 실제 운영 단위로 다시 합치는 지점이다.

읽힌 호출 구조:

- coordination dir 탐색
- worker dir 나열
- `status.md`
- `task.md`
- `handoff.md`
  를 각각 읽음
- worker snapshot으로 합침
- tmux pane 상태를 추가로 붙임
- 최종 session snapshot 생성

핵심 포인트:

- 상태는 하나의 DB row에서 바로 나오지 않는다
- worker status/task/handoff markdown + tmux pane 같은 분산 표면을 읽고 재구성한다
- 즉 이 repo의 연결은 "저장"보다 "재조립"에 가깝다

### 1.5 observer project scoping spine

`scripts/lib/observer-sessions.js`는
observer 상태를 global로 두지 않고 project-scoped로 고정한다.

호출 구조:

- cwd에서 project root 해석
- git root 또는 env root 확인
- project id 계산
- project dir 생성
- `.observer-sessions/*.json` lease 관리

핵심 포인트:

- observer/session 상태가 repo root에 종속된다
- 즉 동일 도구라도 project boundary가 state boundary가 된다

### 1.6 state-store spine

`scripts/status.js`, `scripts/sessions-cli.js`는
다른 표면들을 SQLite state store 기반으로 다시 읽는다.

호출 사슬:

1. `status.js` / `sessions-cli.js`
2. `lib/state-store/index.js`
3. migrations + queries + schema
4. status/session detail payload 생성

핵심 포인트:

- ECC는 두 개의 spine을 동시에 가진다
  - adapter/reconstruction spine
  - state-store reporting spine
- 즉 한쪽은 분산 표면 재조립,
  다른 한쪽은 SQLite 요약/질의다

### 1.7 ECC current judgment

ECC의 폴더 연결 방식은 아래처럼 잠글 수 있다.

- `commands/hooks/skills/rules`는 projection surface다
- `scripts/*.js`는 router다
- `session-adapters`와 `orchestration-session`은 reconstruction engine이다
- `state-store`는 reporting/query spine이다

한 줄로 요약하면:

ECC는 **router + reconstruction + query**의 3중 spine으로 폴더들을 묶는다.

## 2. OpenClaw deep spine

### 2.1 top connector

OpenClaw의 1차 spine은 CLI script보다
`routing/session key` 계층이다.

가장 중요한 질문은
"이 입력이 어느 agent/session으로 들어가는가"다.

그래서 top connector는 아래 두 파일로 읽힌다.

- `src/routing/resolve-route.ts`
- `src/routing/session-key.ts`

### 2.2 route resolution spine

`resolve-route.ts`는 inbound context를 route로 바꾼다.

읽힌 입력:

- channel
- accountId
- peer
- parentPeer
- guild/team
- role ids

읽힌 출력:

- `agentId`
- `sessionKey`
- `mainSessionKey`
- `lastRoutePolicy`
- `matchedBy`

핵심 포인트:

- route는 단순 channel switch가 아니다
- account, peer, guild, team, role, binding order가 모두 route 결정에 들어간다
- 즉 폴더 구조의 중심은 message transport가 아니라 identity resolution이다

### 2.3 session-key spine

`routing/session-key.ts`는 route를 persistence/concurrency key로 바꾼다.

여기서 중요한 일:

- agent id 정규화
- main session key 생성
- DM scope에 따라 session bucket 결정
- peer/channel/account 조합으로 key 조립
- thread suffix 부착

핵심 포인트:

- session key는 단순 식별자가 아니다
- routing, persistence, concurrency, group/direct 정책이 한 군데서 만난다

즉 이 repo의 핵심 connector는 파일 path가 아니라 session key shape다.

### 2.4 config session spine

`src/config/sessions/*`는 session key가 실제 파일과 store로 내려가는 층이다.

중요 파일:

- `paths.ts`
- `session-key.ts`
- `store.ts`
- `store-summary.ts`

읽힌 구조:

- `paths.ts`
  - `agents/<agentId>/sessions` 경로를 canonical root로 잡는다
- `config/sessions/session-key.ts`
  - direct/global/group scope를 canonical key로 바꾼다
- `store.ts`
  - session store load/save/cache/lock/maintenance/pruning/rotation을 담당한다
- `store-summary.ts`
  - full store를 다 읽지 않고 shallow snapshot만 읽는 경량 요약 경로를 제공한다

핵심 포인트:

- OpenClaw는 session을 단일 json 파일로만 보지 않는다
- path, lock, cache, maintenance, summary read를 분리해서 운영한다

### 2.5 agent execution spine

`src/agents/agent-command.ts`는 route/session spine 위에 올라가는 execution spine이다.

읽힌 조합 요소:

- config load
- secret resolution
- session resolution
- runtime env
- auth profiles
- model selection
- workspace
- skills
- delivery
- session store update

핵심 포인트:

- agent command는 하나의 함수지만 사실상 orchestration assembly surface다
- route/session에서 정해진 identity 위에
  실행, auth, skills, workspace, delivery를 순차 조립한다

### 2.6 lifecycle event spine

`src/sessions/session-lifecycle-events.ts`는 작지만 중요하다.

역할:

- session lifecycle listener 등록
- lifecycle event 발행

핵심 포인트:

- event surface를 storage 내부에 숨기지 않고 별도 seam으로 뺀다
- 작은 파일이지만 구조적으로 강한 절개선이다

### 2.7 OpenClaw current judgment

OpenClaw의 폴더 연결 방식은 아래처럼 잠글 수 있다.

- `routing`이 identity와 destination을 정한다
- `session-key`가 route를 stable persistence key로 만든다
- `config/sessions`가 그 key를 file/store/cache/lock 경로로 내린다
- `agents/agent-command`가 그 위에 runtime assembly를 얹는다
- `extensions/*`는 그 다음 결합된다

한 줄로 요약하면:

OpenClaw는 **routing + session-key + store + runtime assembly** spine으로 폴더를 묶는다.

## 3. ECC vs OpenClaw

둘 다 큰 구조지만 연결 방식은 다르다.

### ECC

- 여러 surface를 script가 라우팅한다
- 여러 source를 adapter가 canonical snapshot으로 재조립한다
- 상태 요약은 state-store가 맡는다

즉:

`script router -> adapter reconstruction -> state query`

### OpenClaw

- inbound identity를 route가 먼저 결정한다
- route를 session key가 stable key로 변환한다
- 그 key를 store/path/lock 계층이 유지한다
- agent assembly가 실행을 붙인다

즉:

`route -> session key -> store -> agent runtime`

## 4. connector archetypes

이번 심화 읽기에서 드러난 연결기 archetype은 아래다.

1. router
   - ECC `ecc.js`
2. manifest resolver
   - ECC install spine
3. adapter registry
   - ECC session-inspect spine
4. reconstruction engine
   - ECC orchestration snapshot
5. identity resolver
   - OpenClaw route/session-key
6. persistence spine
   - OpenClaw config/sessions store
7. runtime assembler
   - OpenClaw agent-command

## 5. translation hint for our space

우리 공간에서 중요한 건
"폴더를 어떻게 나눌까"보다
"무엇을 연결 spine으로 둘까"다.

현재 우리 공간에 바로 유효한 질문은 아래다.

1. 우리는 ECC처럼 재구성 spine이 필요한가
2. 우리는 OpenClaw처럼 identity/session spine이 필요한가
3. 현재 `app`과 `runtime` 사이에 별도 connector layer가 더 필요한가
4. `runtime/observer/exploration`는 readout lane인데,
   그것을 묶는 canonical reconstruction entrypoint가 있는가

## 6. current judgment

이번 심화 세션의 가장 중요한 관찰은
좋은 구조에서 폴더보다 더 중요한 것은
`연결 spine의 위치와 종류`라는 점이다.

그리고 지금 본 두 repo는 전혀 다른 식으로 그걸 해결한다.

- ECC는 reconstruction-heavy
- OpenClaw는 identity-heavy

이 차이를 구분해서 읽어야
reference를 덜 피상적으로 가져올 수 있다.
