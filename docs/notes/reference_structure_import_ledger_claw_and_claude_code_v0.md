# reference_structure_import_ledger_claw_and_claude_code_v0

## purpose

이 문서는 `references/git_search/claw-code-main` 과
`references/git_search/claude-code-main` 에서
우리 구조로 가져올 만한 기능적/구조적 요소를
즉시 구현 제안이 아니라 `import ledger` 형태로 기록해 두는 문서다.

핵심 원칙:

- reference의 코드 조각을 그대로 가져오지 않는다
- reference가 구현하고 있는 `공간 분리`, `상태 관리`, `guard 방식`, `loop 방식`을 읽는다
- 그것을 우리 구조의 다른 층위로 번역해 둔다
- 나중에 patch를 열 때 다시 꺼내 쓸 수 있게 한다

## source posture

### claw-code-main

이 repo는 주로 `engine-owning runtime substrate` 로 읽는다.

- 내부 세션 구조
- permission policy
- hook runner
- runtime config
- compaction / continuation
- sandbox state separation

즉 내부 엔진의 층 분리를 읽기 위한 자료다.

### claude-code-main

이 repo는 주로 `engine-extending plugin / hook / orchestration surface` 로 읽는다.

- stop-hook loop
- lightweight state file
- declarative hook wiring
- rule-driven guard
- settings hierarchy

즉 바깥에서 엔진을 감싸는 운영 구조를 읽기 위한 자료다.

## import candidates

### 1. structured reading trace

- reference source
  - `claw-code-main/rust/crates/runtime/src/session.rs`
- what to import
  - 판독 이력을 구조화된 세션/메시지 단위로 남기는 감각
  - 단순 문자열 로그가 아니라 역할별 block을 가진 trace 구조
- our translation
  - `structured reading trace`
  - `entry_point`
  - `connected_segments`
  - `reconstructed_flow`
  - `missing_links`
  - `judgment`
- target space
  - primary: `app/core`
  - secondary surface: `runtime/views`
- why it matters
  - `reading_basis`를 앞으로 단순 문장 하나가 아니라
    재구성 가능한 판독 이력 구조로 확장할 수 있다

### 2. downgrade reason separation

- reference source
  - `claw-code-main/rust/crates/runtime/src/permissions.rs`
  - `claw-code-main/rust/crates/runtime/src/sandbox.rs`
- what to import
  - requested / allowed / denied / fallback_reason 분리
  - 하향 판정 이유를 구조적으로 남기는 방식
- our translation
  - `reading downgrade reason`
  - 예:
    - `missing_organ_link`
    - `missing_after_state`
    - `partial_flow_only`
    - `low_linkage_confidence`
    - `flow_explanation_not_closed`
- target space
  - primary: `app/core`
  - documentation lock: `docs/specs`
- why it matters
  - `weak/caution`이 하나의 뭉툭한 상태로 남지 않고
    왜 strong으로 못 갔는지 나중에 좁게 refinement 할 수 있다

### 3. guard layer separate from reader core

- reference source
  - `claw-code-main/rust/crates/runtime/src/hooks.rs`
  - `claude-code-main/plugins/hookify/core/rule_engine.py`
  - `claude-code-main/plugins/hookify/core/config_loader.py`
- what to import
  - core logic와 guard logic를 분리하는 방식
  - rule-driven warning / deny 계층을 별도 운영하는 감각
- our translation
  - `reader core`
  - `over-read guard`
  - `promotion guard`
  - `flow-basis required guard`
- target space
  - primary: `app/core`
  - experimental guard probes: `app/work`
- why it matters
  - line reading 본체와 과잉 판독 방지 규칙을 같은 함수에 섞지 않게 해 준다

### 4. lightweight reread loop state

- reference source
  - `claude-code-main/plugins/ralph-wiggum/scripts/setup-ralph-loop.sh`
  - `claude-code-main/plugins/ralph-wiggum/hooks/stop-hook.sh`
- what to import
  - 작은 state file로 active / iteration / completion condition을 관리하는 방식
  - 무거운 런타임 개조 없이 bounded loop를 실험하는 감각
- our translation
  - `sentence-connection reread experiment loop`
  - `bounded reread state`
  - `re-entry iteration ledger`
- target space
  - primary: `app/work`
  - not core runtime by default
- why it matters
  - core reader를 바로 흔들지 않고도
    sentence-connection reread의 반복 실험을 작은 단위로 운용할 수 있다

### 5. flow summary compaction

- reference source
  - `claw-code-main/rust/crates/runtime/src/compact.rs`
- what to import
  - raw history를 그대로 누적하지 않고
    continuation 가능한 summary로 접는 방식
- our translation
  - `flow reconstruction summary`
  - `compressed reading_basis packet`
  - `recent raw + prior flow summary` 구조
- target space
  - primary: `app/core`
  - surfaced form: `runtime/views`
- why it matters
  - line reading loop가 길어져도
    raw segment 나열 대신 복원된 흐름 중심으로 기억을 유지할 수 있다

### 6. declarative hook wiring

- reference source
  - `claude-code-main/plugins/ralph-wiggum/hooks/hooks.json`
  - `claude-code-main/plugins/security-guidance/hooks/hooks.json`
- what to import
  - event / matcher / command 연결을 선언형으로 두는 방식
- our translation
  - `observation hook registry`
  - `validation trigger map`
  - `surface-only verifier wiring`
- target space
  - primary: `runtime/contracts`
  - experimental use: `app/work`
- why it matters
  - future verifier나 observer를 if-else 덩어리로 넣지 않고
    어떤 이벤트에서 어떤 검증이 붙는지 얇게 선언할 수 있다

### 7. settings hierarchy / feature split

- reference source
  - `claw-code-main/rust/crates/runtime/src/config.rs`
  - `claude-code-main/examples/settings/README.md`
- what to import
  - settings source hierarchy
  - feature flags를 hooks/plugins/permissions/sandbox처럼 분리하는 구조
- our translation
  - `reading feature split`
  - `observer-only feature`
  - `core reader feature`
  - `guard feature`
  - `surface formatting feature`
- target space
  - primary: `runtime/config`
  - doctrine alignment: `docs/contracts`
- why it matters
  - sentence-connection reading 도입이 broad refactor가 아니라
    좁은 feature split로 관리될 수 있게 해 준다

### 8. validator-size hook examples

- reference source
  - `claude-code-main/examples/hooks/bash_command_validator_example.py`
- what to import
  - 아주 작은 validator를 별도 파일로 두고
    rule 위반 시 block/warn 하는 패턴
- our translation
  - `reading basis validator`
  - `strong without flow explanation blocker`
  - `token-only strong blocker`
- target space
  - primary: `app/work`
  - later optional move: `app/core`
- why it matters
  - 거대한 heuristic refactor 없이도
    최소 검증 규칙부터 따로 붙일 수 있다

## our-space translation map

### docs/specs

- import role
  - 구조 이름을 잠그는 곳
  - 예:
    - `structured reading trace`
    - `reading downgrade reason`
    - `flow reconstruction summary`

### app/work

- import role
  - lightweight loop
  - validator 실험
  - guard probe
  - observer-first 검증

### app/core

- import role
  - actual reader core
  - structured trace
  - downgrade reason
  - guard/core 분리
  - summary compaction

### runtime/views

- import role
  - 표면화만 담당
  - import 대상은 logic이 아니라
    `표면에 무엇을 어떻게 보일지`에 한정

## current priority

우선순위는 아래로 본다.

1. `structured reading trace`
2. `downgrade reason separation`
3. `guard layer separate from reader core`
4. `flow summary compaction`
5. `lightweight reread loop state`
6. `declarative hook wiring`
7. `settings hierarchy / feature split`
8. `validator-size hook examples`

## caution

- reference의 loop를 그대로 우리 문제의 해답으로 오인하지 말 것
- reference의 hook을 그대로 우리 core reader 대체물로 오인하지 말 것
- 우리 문제의 본체는 여전히 `sentence-connection-based line reading` 이다
- 따라서 import는 항상 `구조 번역` 형태여야 하며,
  `기능 literal copy` 가 되어서는 안 된다

## next use

이 ledger는 아래 상황에서 다시 꺼내 쓴다.

- future patch scope를 자를 때
- `app/work` 실험 loop를 설계할 때
- `app/core` reader/guard 분리 구조를 설계할 때
- `reading_basis`와 `downgrade reason`을 구조화할 때
- `runtime/views`에 무엇을 노출하고 무엇을 숨길지 결정할 때
