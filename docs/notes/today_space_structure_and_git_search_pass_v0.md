# today space structure and git_search pass v0

## purpose

오늘 작업의 시작점으로
현재 저장소를 공간 단위로 다시 읽고,
구조설계가 필요한 지점을 먼저 고른 뒤,
`references/git_search/` 재독 순서와 라인 추출 기준을 잠깐 잠그기 위한 메모다.

이 메모는 구현 제안서가 아니라
`space first -> structure reading -> line extraction`
순서를 유지하기 위한 작업 표면이다.

## 1. current top-level reading

현재 저장소의 상위 구조는 대략 아래 6개 공간으로 읽힌다.

1. `inputs/`
   - raw input dropzone
   - 원문 보존 lane

2. `source_assets/`
   - 선언, baseline, directive, handoff가 모이는 source philosophy layer

3. `docs/`
   - spec / note / report / review가 섞인 interpretation layer

4. `app/`
   - engine code body + runtime-facing code body + experimental work tree

5. `runtime/`
   - append-only manifest / receipt / view / event layer

6. `references/`
   - 외부 구조와 방법론을 calibration memory로 붙잡아 두는 비교층

## 2. structure-design checkpoints

오늘 기준으로 구조설계 점검이 필요한 부분은 아래다.

### A. `app/` vs `runtime/` boundary

현재 `app/`과 `runtime/`은 분리는 되어 있지만
어휘가 다시 겹친다.

겹치는 축:

- `ingest`
- `runtime`
- `space`
- `bridge`
- `view`
- `measurement`

위험:

- code organ과 emitted artifact organ이 다시 섞여 보일 수 있다.
- 새 agent가 `app/runtime/`과 `runtime/views/`를 같은 층으로 오해할 수 있다.
- space engine 개념이 코드 구조와 산출물 구조 모두에 중복 투사된다.

오늘 점검 질문:

- `app/`은 "실행 가능한 organ"인가
- `runtime/`은 "실행 결과와 상태 잔적"인가
- 둘 사이의 stop-line이 문서상 충분히 명시돼 있는가

### B. `docs/architecture/` emptiness

`docs/architecture/`는 사실상 비어 있고,
현재는 auto-sync 표면만 있다.

의미:

- architecture narrative가 `docs/notes/`와 `docs/reports/`로 분산돼 있다.
- 구조설계 판단을 다시 하려면 note를 넓게 뒤져야 한다.

오늘 점검 질문:

- architecture layer에 최소한의 canonical map이 필요한가
- 아니라면 계속 `notes/reports` 중심으로 두되, 읽기 순서만 잠글 것인가

### C. `app/work/` scale and maturity marking

`app/work/`는 실험축이 풍부하지만,
mature rail과 probe rail의 구분을 빠르게 읽기 어렵다.

의미:

- work tree가 현재 strongest exploration memory이기도 하다.
- 동시에 new agent에게는 noise처럼 보일 수 있다.

오늘 점검 질문:

- `app/work/` 하위에 maturity marker가 더 필요한가
- 아니면 대표 work lane만 별도 index로 잡으면 충분한가

### D. exploration observation sidecar gap

기존 보고서에서 이미 잡힌 약점은
탐색 결과의 표준 반환층이 약하다는 점이다.

현재 reading:

- trace 회수는 강함
- relation/reason/future use를 표준 슬롯으로 묶는 층은 약함

오늘 점검 질문:

- `runtime/observer/exploration/`에 sidecar note/json 레인을 붙일 것인가
- `docs/templates/`와 함께 최소 관찰 계약을 만들 것인가

## 3. git_search spatial classification

`references/git_search/`는 하나의 묶음이 아니라
서로 다른 구조 성격을 가진 reference cluster다.

### 1. `everything-claude-code-main`

분류:
- multi-surface operating bundle

먼저 볼 이유:
- command / skill / hook / agent / manifest가 병렬 surface로 공존한다.
- "운영 표면 묶음"을 내부 core 하나 없이 조직하는 방식을 보여 준다.

주요 line:
- command shell
- session adapter
- orchestration snapshot
- state-store based inspection

### 2. `openclaw-main`

분류:
- product/control-plane/runtime organ reference

먼저 볼 이유:
- `src/gateway`, `src/routing`, `src/sessions`, `src/security`처럼
  내부 도메인 경계를 폴더 수준에서 강하게 드러낸다.

주요 line:
- gateway assembly
- route resolution
- session identity/lifecycle
- audit/security aggregation

### 3. `claw-code-main`

분류:
- thin outer surface + deeper runtime substrate

먼저 볼 이유:
- 얇은 Python 표면과 Rust runtime 분해가 공존한다.
- session / hooks / permissions / compact를 내부 substrate concern으로 분리한다.

주요 line:
- python entry
- rust runtime/session loop
- permissions
- continuation/compact

### 4. `claude-code-main`

분류:
- external orchestration / plugin interception reference

먼저 볼 이유:
- 내부 runtime ownership보다 host event interception 구조가 중심이다.
- plugin과 hook 기반 외부 제어를 작게 붙이는 방식을 읽기 좋다.

주요 line:
- host event
- hook script
- block/warn/repeat control

### 5. `ralph-main`

분류:
- repeat loop minimal pattern

먼저 볼 이유:
- fresh-context 반복 루프를 가장 작은 파일군으로 보여 준다.
- `prd.json`, `progress.txt`, `ralph.sh` 같은 잔적 기반 지속 기억을 본다.

주요 line:
- PRD task list
- append-only progress
- shell loop

### 6. `autoresearch-master`

분류:
- single-file mutation experiment loop

먼저 볼 이유:
- 구조 밀도는 낮지만, "무엇을 고정하고 무엇만 바꾸는가"가 아주 선명하다.
- 최소 수정 표면 설계의 극단 사례로 읽을 수 있다.

주요 line:
- `program.md`
- `train.py`
- fixed timebox evaluation

## 4. suggested reread order for today

오늘 `git_search`를 다시 볼 때는 아래 순서가 효율적이다.

1. `everything-claude-code-main`
   - 운영 표면 다층성 확인

2. `openclaw-main`
   - 내부 도메인 경계와 control-plane decomposition 확인

3. `claw-code-main`
   - thin shell vs deep substrate 확인

4. `claude-code-main`
   - 외부 hook/plugin 개입 방식 확인

5. `ralph-main`
   - 최소 반복 루프 패턴 확인

6. `autoresearch-master`
   - 단일 수정 표면과 실험 루프 확인

## 5. line extraction rule

이번 재독에서는 구현 기능보다
아래 line만 뽑는 것이 맞다.

### extract

- canonical unit이 무엇인가
- structural center가 어디에 있는가
- 폴더 간 연결 line이 무엇인가
- state가 단일 파일에 있는가, 재구성되는가
- session / routing / hook / audit / task / memory가 별도 공간인가
- outer operating surface와 inner runtime substrate가 분리되는가

### do not extract first

- 함수별 세부 로직
- provider별 옵션 나열
- setup 문구와 마케팅 문구
- feature inventory 전수

## 6. immediate next actions

오늘 실제 실행 순서는 아래가 적절하다.

1. `app/`와 `runtime/` 경계 문서를 먼저 한 번 더 찾는다.
2. `git_search`는 repo별로
   - folder map
   - dominant file forms
   - structural center
   - connection lines
   네 칸으로 기록한다.
3. 각 repo에서 우리 공간으로 바로 번역하지 말고
   먼저 "reference classification"만 적는다.
4. 마지막에만
   - adoptable line
   - not adopted reason
   - future borrowable structure
   를 붙인다.

## 7. current judgment

오늘 기준 최우선 구조설계 과제는
새 기능 추가가 아니라 아래 두 가지다.

1. `app` 대 `runtime`의 stop-line을 더 선명하게 읽히게 만들기
2. `exploration observation sidecar`를 붙일 수 있는 최소 계약을 정리하기

그리고 `git_search`는
코드 카피 소스가 아니라
운영 표면 / 내부 substrate / 반복 루프 / 외부 interception 패턴을 분류하는
비교 구조 메모리로 읽는 것이 맞다.
