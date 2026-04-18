# git_search_reference_landscape_v0

## purpose

이 문서는 `references/git_search` 전체를 다시 훑은 뒤,
각 자료가 어떤 공간/층위의 reference인지와
우리 구조로 가져올 만한 구조적 힌트가 무엇인지
landscape note 형태로 잠가 두는 문서다.

이 문서의 목적은:

- 개별 repo를 따로따로 보는 대신 전체 지형을 먼저 기억하기
- 어떤 repo가 어떤 층위의 reference인지 빠르게 재호출하기
- 이후 import ledger나 patch 설계에서 적절한 자료를 다시 집어오게 하기

## top-level inventory

현재 `references/git_search` 아래 주요 repo는 아래와 같다.

- `autoresearch-master`
- `claude-code-main`
- `claw-code-main`
- `everything-claude-code-main`
- `openclaw-main`
- `ralph-main`

대략적 파일 규모:

- `autoresearch-master`: small experimental repo
- `ralph-main`: small autonomous loop repo
- `claude-code-main`: medium plugin/hook repo
- `claw-code-main`: medium runtime substrate repo
- `everything-claude-code-main`: large multi-surface operating bundle
- `openclaw-main`: very large product/runtime/control-plane repo

## role map

### 1. autoresearch-master

primary reading:

- autonomous experiment loop
- fixed evaluation harness
- one-file mutation discipline
- human-written `program.md` as org-level instruction surface

what it teaches:

- editable surface를 아주 좁게 고정하는 방식
- fixed benchmark / fixed evaluation harness 아래에서 agent를 반복시키는 방식
- 실험 repo에서 `human edits instructions, agent edits one execution file` 구조

our translation hints:

- narrow experimental lane
- fixed evaluation corridor
- observer-safe bounded mutation surface

### 2. ralph-main

primary reading:

- autonomous fresh-context loop
- PRD -> structured task list -> repeated execution
- git history / progress file / task json 기반 memory persistence

what it teaches:

- same task를 fresh context 반복으로 밀어붙이는 구조
- `progress.txt` 와 `prd.json` 같은 lightweight external memory
- task decomposition quality가 loop quality를 좌우한다는 점

our translation hints:

- bounded reread loop
- external loop memory
- task/flow decomposition before repetition

### 3. claude-code-main

primary reading:

- Claude Code plugin / hook / command / skill extension surface
- host runtime 위에 얹히는 orchestration layer

what it teaches:

- stop hook / pretooluse / posttooluse 같은 event interception
- rule-driven guard layer
- lightweight plugin packaging
- loop를 host stop phase에 걸어 재진입시키는 방식

our translation hints:

- guard layer separate from reader core
- observation hooks
- lightweight reread state
- declarative hook wiring

### 4. claw-code-main

primary reading:

- engine-owning runtime substrate
- internal session / permission / hook / prompt / compaction / sandbox separation

what it teaches:

- session을 structured state로 저장하는 방식
- permission / fallback reason 분리
- hook runner를 runtime 내부에 배치하는 방식
- compaction / continuation을 runtime concern으로 다루는 방식

our translation hints:

- structured reading trace
- downgrade reason separation
- internal guard/core split
- flow summary compaction

### 5. everything-claude-code-main

primary reading:

- skill-first operating architecture
- multi-harness bundle
- commands + agents + skills + rules + hooks + manifests + install/control-plane

what it teaches:

- canonical surface를 skill로 이동시키고 command를 shim으로 남기는 방식
- managed loop with safety defaults
- verification을 독립 workflow로 두는 방식
- strategic compaction at logical boundaries
- workspace surface audit
- continuous learning with scoped memory

our translation hints:

- skill-first surface migration
- verification lane as a first-class workflow
- strategic flow summary boundaries
- workspace surface audit discipline
- scoped reading pattern evolution

### 6. openclaw-main

primary reading:

- full product/control-plane/runtime/system repo
- channels + gateway + agent runtime + skills + apps + control UI + ops + safety

what it teaches:

- large-scale assistant product에서 control plane를 명시적으로 두는 방식
- runtime, channels, tools, apps, UI, safety, onboarding을 하나의 operating system처럼 묶는 방식
- product surface와 gateway/control surface를 구분하는 방식

our translation hints:

- control-plane thinking
- operator surface vs core runtime separation
- onboarding / doctor / audit surfaces
- runtime + safety + UI가 하나의 operating system을 이루는 구도

## cross-repo clusters

전체를 다시 보면 이 자료들은 아래 cluster로 묶인다.

### cluster A. loop / repetition / re-entry

- `ralph-main`
- `claude-code-main` (`ralph-wiggum`)
- `everything-claude-code-main` (`loop-start`, `continuous-agent-loop`)
- `autoresearch-master`

이 cluster가 주는 공통 힌트:

- 반복은 단순 while loop가 아니다
- stop condition / quality gate / task decomposition / external memory가 같이 있어야 한다

### cluster B. hook / guard / event interception

- `claude-code-main`
- `everything-claude-code-main`
- `claw-code-main` runtime hooks

이 cluster가 주는 공통 힌트:

- core logic 바깥에 event-driven guard layer를 둘 수 있다
- warning / block / observe / summarize를 서로 다른 phase로 분리할 수 있다

### cluster C. runtime substrate / session / compaction

- `claw-code-main`
- `everything-claude-code-main` 일부
- `openclaw-main`

이 cluster가 주는 공통 힌트:

- 상태 저장
- session memory
- prompt assembly
- continuation / compaction
- control plane

### cluster D. skill-first operating surface

- `everything-claude-code-main`
- `claude-code-main`
- `ralph-main` skills

이 cluster가 주는 공통 힌트:

- user-facing canonical surface를 skill/workflow에 두고
  command는 compatibility shim으로 남길 수 있다

### cluster E. control plane / product surface

- `openclaw-main`
- `everything-claude-code-main`

이 cluster가 주는 공통 힌트:

- system은 core engine alone이 아니다
- operator surface, onboarding, audit, doctor, routing, safety, UI가 함께 있어야 한다

## likely import directions for our repo

전체 지형을 기준으로 보면
우리 repo에 가장 실제적으로 도움이 되는 방향은 아래다.

### docs/specs

- `everything-claude-code-main` 식 skill-first posture
- `claw-code-main` 식 structured runtime separation
- `claude-code-main` 식 hook/guard vocabulary

### app/work

- `ralph-main` / `autoresearch-master` 식 bounded experiment loop
- `claude-code-main` 식 lightweight hook-driven observation
- `everything-claude-code-main` 식 verification / audit workflows

### app/core

- `claw-code-main` 식 structured session / downgrade reason / compaction
- 이후 line reading core와 guard를 분리하는 설계

### runtime/views

- `everything-claude-code-main` / `openclaw-main` 식 operator surface 감각
- 하지만 logic은 넣지 않고 surfaced operating layer로만 유지

## current caution

- 이 자료들을 `코드 조각 창고`로 보면 안 된다
- 이 자료들은 먼저 `구조 유형의 도서관`으로 읽어야 한다
- 특히 `openclaw-main`처럼 규모가 큰 repo는
  line reading 직접 reference가 아니라
  control-plane / operator-surface / safety-system reference에 가깝다
- `autoresearch-master`는 full harness reference가 아니라
  fixed-eval experimental loop reference에 가깝다

## current best-use order

나중에 다시 사용할 때는 아래 순서로 참조한다.

1. 문제의 층위를 먼저 판정한다
   - loop 문제인가
   - guard 문제인가
   - runtime substrate 문제인가
   - operator surface 문제인가
2. 그 층위에 맞는 repo cluster를 고른다
3. 그 안에서 세부 import candidate를 고른다
4. 우리 공간으로 번역한다
5. 그 다음에만 patch or spec proposal로 내린다

## one-line summary

`references/git_search` 는 하나의 같은 종류 자료 모음이 아니라,
실험 loop, plugin orchestration, runtime substrate, skill-first operating architecture,
control-plane product surface까지 걸친 다층 reference library이며,
우리 repo는 이 자료들에서 코드 literal보다 공간 분리 원리와 운영 구조를 번역해 가져오는 방식으로 써야 한다.
