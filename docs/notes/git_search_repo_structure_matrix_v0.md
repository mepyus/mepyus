# git_search repo structure matrix v0

## purpose

`references/git_search/`를
기능 목록이 아니라 구조 비교 메모리로 다시 읽기 위한 표면이다.

이번 문서는 각 repo를 공통된 6칸으로 정리한다.

1. folder map
2. dominant file forms
3. structural center
4. connection lines
5. adoptable line
6. not adopted / caution

## 1. `everything-claude-code-main`

### folder map

- multi-harness hidden roots
  - `.claude`
  - `.codex`
  - `.cursor`
  - `.kiro`
  - `.opencode`
  - `.agents`
- portable operating surfaces
  - `agents`
  - `commands`
  - `contexts`
  - `hooks`
  - `manifests`
  - `plugins`
  - `rules`
  - `skills`
- execution / state side
  - `scripts`
  - `schemas`
  - `ecc2`

### dominant file forms

- markdown command and skill surfaces
- hook declarations
- JS scripts and library modules
- state-store oriented modules
- harness-specific mirror folders

### structural center

한 파일 중심이 아니라
portable operating surface와
script/state-store composition의 관계가 중심이다.

### connection lines

- harness-specific roots -> shared commands/rules/skills
- command surface -> scripts -> state/adapters
- session inspection -> adapter registry -> canonical snapshot
- hooks/manifests -> cross-harness behavior portability

### adoptable line

- 하나의 core만 세우지 않고 operating surface를 병렬 유지하는 방식
- canonical state를 direct source 하나가 아니라 adapter 결과로 잡는 방식
- project-scoped operating memory를 재구성 표면으로 만드는 방식

### not adopted / caution

- cross-harness parity를 너무 빨리 일반화하면 현재 공간이 과도하게 productized될 수 있다
- surface 수가 많아질수록 현재 우리 저장소의 late-condensation 철학이 흐려질 수 있다

## 2. `openclaw-main`

### folder map

- product / device side
  - `apps`
  - `ui`
- internal control-plane docs
  - `docs`
- large extension ecology
  - `extensions/*`
- source packages
  - `src`
  - `packages`

### dominant file forms

- TypeScript product/runtime modules
- extension package manifests
- docs by operating domain
- UI package files

### structural center

중심은 단일 assistant 파일이 아니라
gateway, routing, sessions, security 같은
control-plane decomposition이다.

### connection lines

- gateway -> routing -> session identity/lifecycle
- gateway -> security/audit checks
- core control plane -> extensions for channels/providers/tools
- docs mirror the same domain split

### adoptable line

- 내부 도메인 경계를 폴더 이름만으로도 읽히게 만드는 방식
- route/session/security를 별도 공간으로 유지하는 방식
- 거대한 extension 생태계를 control-plane 위에 얹는 방식

### not adopted / caution

- 이 repo는 이미 product/control-plane body가 큰 상태다
- 현재 우리 공간은 아직 operator/product plane보다 reread and evidence discipline이 중심이라 그대로 가져오면 규모 과잉이 된다

## 3. `claw-code-main`

### folder map

- outer surface
  - `src`
  - `tests`
- inner substrate
  - `rust/crates/api`
  - `rust/crates/runtime`
  - `rust/crates/tools`
  - `rust/crates/commands`
  - `rust/crates/plugins`
  - `rust/crates/server`
  - `rust/crates/lsp`
  - `rust/crates/claw-cli`

### dominant file forms

- thin Python wrappers
- Rust crate decomposition
- tests attached to behavior slices
- porting/compatibility oriented files

### structural center

outer Python surface보다
Rust runtime/session substrate가 중심이다.

### connection lines

- python entry -> runtime wrapper -> rust crates
- session/hook/permission/compact concerns -> separate runtime modules
- commands/plugins/tools -> substrate above core runtime

### adoptable line

- thin outer operating layer + deeper inner substrate 분리
- session, hook, permission, continuation concern을 내부 모듈로 명시하는 방식
- wrapper와 substrate를 섞지 않는 방식

### not adopted / caution

- 현재 우리 저장소는 언어 이중화가 목표가 아니다
- substrate 분해 사고는 유용하지만, 지금 당장 Rust-like internal rebuild로 번역할 단계는 아니다

## 4. `claude-code-main`

### folder map

- host-specific roots
  - `.claude`
  - `.claude-plugin`
- examples and scripts
  - `examples`
  - `scripts`
- plugin surfaces
  - `plugins/*`

### dominant file forms

- plugin readmes
- hook/event-oriented setup files
- small validator/helper scripts
- host-specific rule surfaces

### structural center

중심은 internal runtime ownership이 아니라
host event interception과 plugin extension이다.

### connection lines

- host command/hook surface -> plugin/hook logic
- examples/settings -> extension usage pattern
- small scripts -> validation or glue behavior

### adoptable line

- core를 바꾸지 않고 외부 interception layer를 붙이는 방식
- 작은 plugin bundle을 통해 operating behavior를 추가하는 방식

### not adopted / caution

- 현재 우리 공간의 본체는 외부 host 얹기보다 내부 reread body와 evidence discipline이다
- plugin-oriented thinking이 과해지면 core/body 판단이 얇아질 수 있다

## 5. `ralph-main`

### folder map

- loop core
  - root scripts/files
- skill side
  - `skills/prd`
  - `skills/ralph`
- explanation/demo side
  - `flowchart`

### dominant file forms

- shell loop script
- prompt/skill markdown
- small JSON task memory
- visualization demo files

### structural center

구조 중심은 복잡한 runtime이 아니라
fresh-context 반복 루프와
append-only task memory다.

### connection lines

- PRD -> `prd.json` -> shell loop
- loop iteration -> git commit/progress append -> next fresh instance
- skills -> PRD generation/conversion -> loop input

### adoptable line

- fresh-context를 강제하면서도 잔적 기억으로 반복하는 방식
- `progress.txt`와 `prd.json` 같은 작은 persistent memory

### not adopted / caution

- 현재 우리 공간은 task completion loop보다 line reread와 bounded evidence가 더 중심이다
- 너무 빨리 PRD loop 중심으로 읽으면 현재 철학이 execution-first로 기울 수 있다

## 6. `autoresearch-master`

### folder map

- almost-flat root
  - `prepare.py`
  - `train.py`
  - `program.md`
  - `pyproject.toml`

### dominant file forms

- single mutable training file
- one human-authored program file
- one setup/runtime utility file

### structural center

중심은 architecture richness가 아니라
무엇을 고정하고 무엇만 변형 대상으로 둘지의 극단적 선명함이다.

### connection lines

- human program -> agent behavior
- agent edits -> single mutable file
- fixed time budget eval -> keep/discard loop

### adoptable line

- mutation surface를 극단적으로 좁혀 reviewability를 확보하는 방식
- fixed evaluation window로 실험 루프를 안정화하는 방식

### not adopted / caution

- 현재 우리 저장소는 단일 수정 표면보다 다층 공간 판독이 중요하다
- 너무 좁은 mutation model은 현재의 space-first reading에는 맞지 않는다

## 7. cross-repo extracted lines

이번 재독에서 두꺼웠던 공통 line은 아래다.

- operating surface는 하나가 아닐 수 있다
- canonical state는 단일 파일보다 재구성 표면일 수 있다
- inner runtime substrate와 outer operating surface를 분리할수록 구조가 선명해진다
- extension ecology는 core ownership과 분리될 때 더 안정적이다
- 반복 루프는 큰 runtime 없이도 작은 잔적 기억으로 유지될 수 있다
- mutation surface를 좁히면 실험 판단이 빨라진다

## 8. translation guard for our space

우리 공간으로 번역할 때는 아래 순서를 지키는 것이 맞다.

1. repo를 곧바로 도입하지 않는다
2. 먼저 구조 패턴만 분류한다
3. 그다음 `adoptable line`만 적는다
4. 마지막에만 우리 공간의 어느 층에 붙을지 결정한다

한 줄로 잠그면:

`git_search`는 코드 수입 창고가 아니라
운영 표면, 내부 substrate, 반복 루프, 외부 interception 구조를 분류하는 비교 메모리다.
