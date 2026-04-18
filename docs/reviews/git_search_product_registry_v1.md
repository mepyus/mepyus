# Git Search Product Registry v1

## 목적

이 문서는 `references/git_search/*` 를 폴더 구조가 아니라 제품 기능 기준으로 읽는다.

판단 질문은 아래 순서다.

1. 이 레포는 무슨 제품 또는 운영 커널인가
2. 핵심 실행 루프는 무엇인가
3. 기억/상태/거버넌스는 어디에 놓이는가
4. 우리 공간을 바닥에 깔고 그 위에 overlay prototype으로 얹을 수 있는가

여기서 말하는 우리 공간의 바닥은 아래를 뜻한다.

- line memory
- observer / reread / promotion governance
- append-only operation memory
- runtime surface / generated surface separation

즉 외부 제품을 통째로 복제하는 것이 아니라,
외부 제품의 control plane 또는 operating kernel을
우리 line-aware space 위에 얹을 수 있는지 본다.

## 판정 요약

### 1차 prototype 적합

- `paperclip-master`
- `openclaw-main`
- `ralph-main`

### 2차 prototype 적합

- `autoresearch-master`

### 참고용 harness cohort

- `claude-code-main`
- `everything-claude-code-main`
- `claw-code-main`

## product cards

### 1. paperclip-master

제품 정의:

- multi-agent company orchestration control plane

핵심 기능:

- 회사 생성
- org tree 기반 agent 배치
- 단일 assignee issue/task 운용
- heartbeat 기반 실행
- budget / approval / audit 제어

핵심 루프:

- company -> agents -> issues -> heartbeat_runs -> approvals/budgets

기억/상태:

- DB 중심
- company-scoped entities
- run log / cost / activity / approvals 기록

우리 공간 위 overlay 가능성:

- 높음

overlay 방식:

- `company` -> `workspace boundary`
- `agent` -> `line role`
- `issue` -> `line-bound work unit`
- `heartbeat` -> `bounded operating loop`
- `approval` -> `promotion gate`
- `budget` -> `runtime guard`

판단:

- 제품 전체를 가져오면 회사 앱이 되어 과하다.
- 하지만 `역할`, `일감`, `실행 루프`, `제동 장치` 추상화는 우리 공간 운영 커널과 매우 잘 맞는다.

prototype 형태:

- `vectorfl workspace board`
- line owner / support operator tree
- work unit registry
- promotion / archive / runtime guard panel

### 2. openclaw-main

제품 정의:

- personal AI assistant gateway with multi-channel control plane

핵심 기능:

- 다채널 메시징 입력
- gateway daemon
- node/client 분리
- plugin capability model
- agent loop, session, memory, approval/tool guard

핵심 루프:

- inbound channel -> gateway -> context assembly -> model inference -> tool execution -> streamed reply -> persistence

기억/상태:

- session
- context engine
- memory plugin slot
- plugin registry

우리 공간 위 overlay 가능성:

- 높음

overlay 방식:

- 우리 공간이 `semantic reading/memory engine`
- OpenClaw가 `user-facing gateway + plugin control plane`

붙는 지점:

- `observer_ingest_min` / `surface readout` -> context/memory surface
- `promotion governance` -> approvals / exec guard
- `runtime` -> gateway-readable canonical memory backing store

판단:

- OpenClaw의 강점은 input surface와 control plane이다.
- 우리 공간은 line memory와 reread 판단이 강하다.
- 둘을 겹치면 “assistant shell 위에 line-aware memory kernel” prototype이 가능하다.

prototype 형태:

- multi-surface ingress shell
- vectorfl-backed memory/context provider
- line-aware reply framing / reread path hints

### 3. ralph-main

제품 정의:

- clean-context autonomous execution loop

핵심 기능:

- PRD를 JSON task로 변환
- fresh context 반복 실행
- progress/githistory/prd로 기억 유지
- bounded iteration loop

핵심 루프:

- PRD -> task list -> fresh run -> progress update -> repeat until complete

기억/상태:

- `prd.json`
- `progress.txt`
- git history

우리 공간 위 overlay 가능성:

- 매우 높음

overlay 방식:

- Ralph는 얇은 loop runner로 두고
- 우리 공간은 persistent memory / observation / residue evaluation layer로 둔다

붙는 지점:

- `progress.txt` 대신 line-aware operation ledger
- `prd.json` 대신 line-bound work unit registry
- fresh-run 결과를 observer / promotion gate로 재독

판단:

- 가장 작고 실험하기 쉬운 prototype 대상이다.
- 회사 모델이나 다채널 gateway 없이도
  “loop 위에 우리 memory kernel을 얹는” 감각을 빨리 검증할 수 있다.

prototype 형태:

- `ralph + vectorfl memory spine`
- fresh context run
- post-run reread
- keep/discard/promote decision

연결 문서:

- [Ralph Overlay Prototype v1](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/ralph_overlay_prototype_v1.md)

### 4. autoresearch-master

제품 정의:

- autonomous experiment loop for model/training improvement

핵심 기능:

- 한 파일 수정
- 짧은 실험 반복
- 결과 비교 후 keep/discard
- branch advancing

핵심 루프:

- propose change -> run experiment -> read metric -> keep or reset

기억/상태:

- `program.md`
- `results.tsv`
- git branch
- run log

우리 공간 위 overlay 가능성:

- 중간 이상

overlay 방식:

- 우리 공간이 experiment memory / residue reading / comparison surface가 된다

붙는 지점:

- `results.tsv` -> structured observation ledger
- keep/discard -> promotion/archive decision
- branch progression -> line thickening / candidate evolution

판단:

- coding assistant shell보다 연구/실험 shell에 가깝다.
- 우리 공간과 붙이면 “experiment governance kernel” prototype이 된다.
- 다만 일반 제품 shell보다는 domain이 좁아 2차 대상이 적절하다.

prototype 형태:

- experiment proposal
- bounded run capture
- observer comparison card
- keep/discard/promote board

### 5. claude-code-main

제품 정의:

- agentic coding tool 본체

핵심 기능:

- terminal-native coding agent
- repo understanding
- task execution
- plugin support

우리 공간 위 overlay 가능성:

- 낮음

판단:

- 이건 overlay 대상 제품이라기보다 underlying harness/tool에 가깝다.
- 우리 공간이 그 위에 올라가는 편이지, 반대로 별도 제품 prototype 대상으로 읽기는 약하다.

### 6. everything-claude-code-main

제품 정의:

- harness performance system

핵심 기능:

- rules / hooks / skills
- memory persistence
- orchestration tuning
- security scanning
- cross-harness install/runtime support

우리 공간 위 overlay 가능성:

- 중간

판단:

- 제품이라기보다 meta-harness layer다.
- 우리 공간에 바로 얹는 대상보다는
  prototype을 운영할 때 필요한 optimization/control patterns 참고처에 가깝다.

쓸모:

- hook design
- context budget discipline
- session persistence
- orchestration status patterns

### 7. claw-code-main

제품 정의:

- coding harness clean-room rewrite / runtime reimplementation

핵심 기능:

- CLI/runtime/tool/plugin/session architecture 재구성
- Python/Rust port

우리 공간 위 overlay 가능성:

- 중간 이하

판단:

- 제품보다 harness runtime 연구 자산에 가깝다.
- 우리 공간 위에 바로 얹는 것보다
  `tool/runtime/session/plugin` 층을 참고하는 쪽이 맞다.

## prototype ranking

### P1. Ralph overlay

목표:

- 가장 작은 프로토타입으로
  `fresh run + persistent vectorfl memory + reread gate`
  가 먹히는지 검증

필요 요소:

- work unit registry
- progress ledger
- post-run observer summary
- keep/discard/promote decision

### P2. OpenClaw overlay

목표:

- multi-surface assistant shell 위에
  우리 line-aware memory kernel을 붙이는지 검증

필요 요소:

- ingress surface
- context/memory adapter
- approval/guard bridge
- reply shaping using line/readout surfaces

### P3. Paperclip overlay

목표:

- line role / work unit / gate 기반 operating kernel을 만들고
  workspace를 company-like boundary로 운용하는지 검증

필요 요소:

- role tree
- work unit registry
- bounded heartbeat-like run
- promotion/archive/runtime guards

### P4. Autoresearch overlay

목표:

- 실험 루프에 observer/promotion governance를 붙여
  experiment memory kernel을 만드는지 검증

## 권고

첫 prototype은 `Ralph overlay` 가 가장 맞다.

이유:

- 가장 작다
- clean-context loop가 분명하다
- 우리 공간의 강점인 memory / reread / decision gate를 바로 붙일 수 있다
- 실패해도 비용이 작다

그 다음은 `OpenClaw overlay` 가 좋다.

- user-facing surface와 control plane이 필요할 때
- 우리 공간을 context/memory kernel로 붙이는 연습이 된다

`Paperclip overlay` 는 세 번째가 적절하다.

- 가장 강력하지만 가장 구조가 무겁다
- 추상화만 잘 떼와야 한다

## one-line conclusion

`references/git_search/*` 는 같은 종류의 폴더 묶음이 아니다.
기능 기준으로 보면,
우리가 바로 prototype으로 붙여볼 대상은
`Ralph(loop)`, `OpenClaw(control plane)`, `Paperclip(governance kernel)` 이고,
우리 공간은 그 아래에서 `line-aware memory / reread / promotion kernel` 로 놓는 것이 가장 자연스럽다.
