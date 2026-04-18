# git_search program folder script connection reading v0

## purpose

이번 문서는 `references/git_search/`를
폴더 구조 그 자체가 아니라
각 프로그램이 폴더를 어떻게 작동 표면으로 쓰는지,
그리고 스크립트가 그 폴더들을 어떻게 내부 연결로 묶는지 보기 위한 읽기 기록이다.

핵심 질문은 두 가지다.

1. 각 프로그램은 폴더를 어떤 책임 단위로 쓰는가
2. 어떤 스크립트/엔트리포인트가 그 폴더들을 연결해 하나의 실행 흐름으로 만드는가

## 1. `everything-claude-code-main`

### folder usage

이 repo는 폴더를 product module보다
`portable operating surface` 단위로 쓴다.

핵심 폴더:

- harness-specific roots
  - `.claude`
  - `.codex`
  - `.cursor`
  - `.kiro`
  - `.opencode`
  - `.agents`
- shared surfaces
  - `commands`
  - `hooks`
  - `skills`
  - `rules`
  - `manifests`
- execution layer
  - `scripts`

즉 폴더는 "도메인 로직"보다
"어느 harness 표면에 어떻게 투영되는가"를 기준으로 나뉜다.

### script connection pattern

이 repo의 중심 연결기는 `scripts/ecc.js`다.

읽힌 구조:

- `ecc.js`
  - 명령 이름을 해석한다
  - 실제 script 파일로 라우팅한다
- `install-plan.js`
  - manifest를 읽어 install plan을 계산한다
- `session-inspect.js`
  - adapter registry를 통해 서로 다른 session source를 canonical snapshot으로 바꾼다
- `lib/orchestration-session.js`
  - coordination dir 안의 `status.md`, `task.md`, `handoff.md`를 읽고 하나의 session snapshot으로 재조립한다
- `lib/observer-sessions.js`
  - project root를 기준으로 observer lease 파일을 project-scoped로 관리한다

### how folders become connected

이 repo는
스크립트가 폴더를 직접 다 불러오는 방식이 아니라,
`command shell -> script -> lib -> state/adapter -> projected surface`
흐름으로 묶는다.

중요 연결선:

1. `commands/hooks/skills/rules`
   - 사용자가 보는 operating surface
2. `scripts/*.js`
   - 그 surface를 해석하는 command router
3. `scripts/lib/*`
   - session, install, observer, orchestration 로직
4. state/adapter snapshot
   - 여러 파일을 하나의 canonical readout으로 재구성

### structural reading

이 repo는 폴더를 보관함으로 쓰지 않는다.
폴더는 각 harness surface가 나뉜 projection이고,
스크립트는 그 projection 사이를 횡단하는 router다.

한 줄로 요약하면:

`folder = portable surface`, `script = surface router`.

## 2. `openclaw-main`

### folder usage

이 repo는 폴더를
명확한 내부 시스템 도메인으로 쓴다.

중심 폴더:

- `src/routing`
- `src/sessions`
- `src/agents`
- `src/acp`
- `src/config`
- `src/infra`
- `extensions/*`
- `docs/*`

여기서는 폴더가
interface projection이 아니라
control-plane domain 자체다.

### script and module connection pattern

이 repo는 `scripts/`보다 `src/` 내부 모듈 연결이 본체다.

읽힌 구조:

- `routing/resolve-route.ts`
  - channel/account/peer/guild/team/roles를 받아 agent route를 결정한다
- `routing/session-key.ts`
  - route가 붙을 session key shape를 만든다
- `agents/agent-command.ts`
  - CLI/config/session/runtime/auth/workspace/skills를 한 번에 조합해 agent command를 실행한다
- `library.ts`
  - config, session store, prompt, binaries, process exec, plugin runtime를 lazy-load/export 하는 facade 역할을 한다
- `package.json`
  - `gateway`, `doctor`, `onboard`, extension boundary lint, gateway tests 같은 스크립트 엔트리들을 선언한다

### how folders become connected

이 repo의 연결은
script wrapper보다 session key와 routing resolution이 중심이다.

중요 연결선:

1. inbound source
   - channel/account/peer
2. `src/routing`
   - route와 session key 생성
3. `src/sessions`
   - persistence/lifecycle 연결
4. `src/agents`
   - command execution, model/auth/skills/workspace 연결
5. `extensions/*`
   - provider/channel/tool/plugin 생태계 결합

즉 폴더는 도메인 경계이고,
연결은 `routing -> session key -> agent runtime -> extension` 순으로 발생한다.

### structural reading

이 repo에서 스크립트는 진입점이지만,
실제 연결을 만드는 것은 도메인 모듈이다.

한 줄로 요약하면:

`folder = internal control-plane domain`, `script = launch surface`, `session key = main connector`.

## 3. `claw-code-main`

### folder usage

이 repo는 폴더를
외부 포팅 표면과 내부 런타임 거울층으로 동시에 쓴다.

핵심 폴더:

- `src/`
  - Python 포팅 표면
- `rust/crates/*`
  - deeper substrate
- `tests/`
  - behavior verification
- `src/reference_data`
  - archived snapshot mirror

즉 폴더는 기능 구현보다
`mirror + shim + substrate` 관계를 드러낸다.

### script and module connection pattern

중심 엔트리포인트는 `src/main.py`다.

읽힌 구조:

- `main.py`
  - 여러 subcommand를 파싱한다
  - summary/manifest/bootstrap/turn-loop/remote mode를 각각 모듈로 보낸다
- `bootstrap_graph.py`
  - startup sequence를 graph 형태로 요약한다
- `runtime.py`
  - command/tool backlog와 query engine, setup, history를 한 session object로 조합한다
- `query_engine.py`
  - manifest, command backlog, tool backlog, transcript store, session persistence를 turn loop로 묶는다
- `execution_registry.py`
  - mirrored commands/tools를 실제 실행 shim으로 등록한다

### how folders become connected

이 repo는 폴더 사이를 실제 production runtime처럼 연결하지 않고,
`mirrored inventory -> runtime session mock -> transcript persistence`
흐름으로 묶는다.

중요 연결선:

1. `commands.py`, `tools.py`
   - mirrored inventory
2. `execution_registry.py`
   - execution shim registry
3. `query_engine.py`
   - prompt/turn/transcript/session logic
4. `runtime.py`
   - setup/context/history/routing을 session surface로 조합
5. `main.py`
   - CLI entry surface

### structural reading

이 repo에서 폴더는 실제 시스템의 live organ이라기보다
포팅된 관찰 표면이다.

한 줄로 요약하면:

`folder = mirrored port surface`, `script/main = inventory composer`.

## 4. `claude-code-main`

### folder usage

이 repo는 폴더를
작은 host extension bundle로 쓴다.

핵심 폴더:

- `.claude`
- `.claude-plugin`
- `plugins/*`
- `examples/*`
- `scripts/*`

이 구조에서는 폴더가 큰 앱 도메인이 아니라
host에 얹히는 capability pack이다.

### script connection pattern

읽힌 구조:

- `scripts/sweep.ts`
  - GitHub issue lifecycle을 자동 처리한다
- plugin readme들, 특히 `plugins/hookify/README.md`
  - markdown rule 파일을 `.claude` 아래에 만들어 host event와 연결한다

### how folders become connected

여기서 연결의 본체는
코드 내부 모듈 그래프보다
`host event -> plugin rule -> hook behavior`
다.

중요 연결선:

1. plugin README / config
   - 사용 규칙 정의
2. `.claude` local files
   - host가 읽는 rule surface
3. scripts
   - repo 운영 자동화 또는 glue logic

### structural reading

이 repo는 폴더를
내부 엔진 장기 구조보다
작게 붙였다 떼는 extension point로 쓴다.

한 줄로 요약하면:

`folder = capability pack`, `script = automation glue`, `connection = host interception`.

## 5. `ralph-main`

### folder usage

이 repo는 폴더를 거의 최소화한다.

핵심 파일/폴더:

- `ralph.sh`
- `prompt.md`
- `CLAUDE.md`
- `prd.json`
- `progress.txt`
- `skills/*`
- `flowchart/`

즉 폴더보다 상태 파일 몇 개가 더 중요하다.

### script connection pattern

중심은 `ralph.sh` 하나다.

읽힌 구조:

- branch name을 읽는다
- `prd.json`, `progress.txt`, `.last-branch`를 관리한다
- branch가 바뀌면 이전 run을 archive한다
- 선택한 tool에 따라 `prompt.md` 또는 `CLAUDE.md`를 주입한다
- 출력에서 completion signal을 찾는다
- 완료되지 않으면 fresh iteration을 다시 돈다

### how folders become connected

연결은 매우 단순하다.

1. `skills/*`
   - PRD 작성/변환에 쓰인다
2. `prd.json`
   - loop의 task memory
3. `progress.txt`
   - append-only learning memory
4. `ralph.sh`
   - 위 파일들을 연결하고 새 iteration을 발생시킨다

### structural reading

이 repo는 폴더 구조를 복잡하게 쓰지 않는다.
대신 shell loop가 파일 몇 개를 상태 spine으로 묶는다.

한 줄로 요약하면:

`folder = auxiliary`, `script = state loop spine`.

## 6. `autoresearch-master`

### folder usage

이 repo는 폴더보다 flat root를 전략적으로 쓴다.

핵심 파일:

- `program.md`
- `prepare.py`
- `train.py`
- `results.tsv` (운영 중 생성)

즉 구조 복잡도를 의도적으로 제거한다.

### script connection pattern

실질 연결은 문서와 파일 역할 제한에서 나온다.

읽힌 구조:

- `program.md`
  - 실험 loop 전체 절차를 규정한다
- `prepare.py`
  - data, tokenizer, dataloader, evaluation harness를 고정한다
- `train.py`
  - 유일한 mutation surface다

### how folders become connected

사실상 폴더 연결은 없다.
대신 역할 제한이 연결을 만든다.

1. `program.md`
   - 사람이 아닌 agent의 작업 프로토콜
2. `prepare.py`
   - 고정된 infra/eval layer
3. `train.py`
   - mutable experiment body
4. `run.log`, `results.tsv`
   - 실험 결과 memory

### structural reading

이 repo는 폴더를 거의 안 쓰는 대신
역할 분리와 file-level contract를 극단적으로 강하게 쓴다.

한 줄로 요약하면:

`folder = minimized`, `script/file contract = main connector`.

## 7. cross-repo comparison

이번 세션에서 보인 공통 차이는 아래다.

### A. folder as surface

- `everything-claude-code-main`
  - harness projection surface
- `claude-code-main`
  - capability pack surface

### B. folder as domain

- `openclaw-main`
  - internal control-plane domain

### C. folder as mirrored port

- `claw-code-main`
  - porting/mirroring surface

### D. folder minimized, file loop emphasized

- `ralph-main`
- `autoresearch-master`

## 8. what scripts actually do

스크립트/엔트리포인트는 공통적으로 아래 중 하나를 맡는다.

1. router
   - 예: `everything-claude-code-main/scripts/ecc.js`
2. assembler
   - 예: `openclaw`의 routing/session/agent 조합
3. composer
   - 예: `claw-code-main/src/runtime.py`
4. loop spine
   - 예: `ralph.sh`
5. protocol file
   - 예: `autoresearch/program.md`

즉 "스크립트"는 항상 shell 파일만 뜻하지 않는다.
어떤 repo에서는 CLI script고,
어떤 repo에서는 session-key 모듈이고,
어떤 repo에서는 protocol markdown이 사실상 loop engine이다.

## 9. translation hint for our space

우리 공간에 바로 중요한 힌트는 아래다.

1. 폴더는 저장 위치가 아니라 책임 단위로 읽어야 한다
2. 스크립트는 파일 실행기이기 전에 폴더 간 연결기다
3. 내부 연결의 중심이 shell일 수도 있고 session key일 수도 있고 manifest resolver일 수도 있다
4. 구조를 잘 읽으려면 "어디에 뭐가 있나"보다
   "무엇이 무엇을 불러와 하나의 실행 경로를 만드는가"를 봐야 한다

## 10. current judgment

이번 세션 기준으로 가장 중요한 관찰은 이거다.

- 좋은 구조는 폴더를 많이 나누는 데서 나오지 않는다
- 좋은 구조는 폴더의 책임과 연결기의 위치가 선명할 때 나온다

그리고 각 repo는 서로 다른 방식으로 그걸 한다.

- ECC는 script router로
- OpenClaw는 session/routing domain으로
- Claw rewrite는 mirror composer로
- Claude plugin repo는 host interception으로
- Ralph는 shell loop spine으로
- autoresearch는 file contract로

연결을 만들고 있었다.
