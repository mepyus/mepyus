# space detailed structure handoff for future agents v0

## 0. purpose

이 문서는 앞으로 다른 에이전트나 LLM이 붙더라도
현재 `vectorfl_replica` 공간을 빠르게 이해할 수 있게,
공간의 상세 구조와 읽기 순서를 handoff 형태로 정리한 문서다.

핵심 목적은:

- 공간을 단순 코드 저장소나 문서 창고로 오해하지 않게 하기
- 어디를 먼저 읽어야 하는지 알려주기
- 무엇이 construction이고 무엇이 line reread인지 분명히 하기
- premature lock / premature hub naming을 줄이기

---

## 1. current one-line identity

현재 공간은
정의된 개념을 먼저 집어넣는 엔진이 아니라,
재료를 넣고, 흔적을 남기고, 반복 reread를 거쳐
line이 두꺼워지고 응결이 늦게 떠오르도록 만드는
`space-first maturation engine`에 가깝다.

즉:

- fragment / source 보존
- hold / calibration / parked
- repeated reread
- late condensation
- human-language meaning reread

이 중심축이다.

---

## 2. top-level structure

### 2.1 `inputs/`

역할:
- raw input lane
- 외부 txt / 인터뷰 / transcript / 비교 재료의 초기 보관소

질문:
- 원문이 어디 있는가
- 아직 가공되지 않은 외부 재료는 무엇인가

### 2.2 `source_assets/`

역할:
- 현재 공간 철학과 운영 기준의 핵심 source layer

하위 중심:
- `declarations/`
- `baselines/`
- `directives/`
- `external_case_inputs/`
- `handoffs/`
- `session_notes/`

질문:
- 사용자의 사고 방식이 어디에 직접 녹아 있는가
- 어떤 철학과 operating rule이 반복 선언되었는가

### 2.3 `references/`

역할:
- archive가 아니라 `calibration memory`
- 외부 repo / 외부 방법론 / 비교 자산 / later surface seed

핵심 원칙:
- reference 전체를 도입하지 않는다
- 필요한 line만 선택적으로 가져온다
- 지금 안 쓰는 것도 이유와 reopen 조건을 기록한 채 남긴다

### 2.4 `docs/`

역할:
- 해석 자산과 운영 자산이 함께 있는 문서층

중심 하위:
- `specs/` : 잠긴 기준
- `notes/` : 과정 메모 / close-out / intake 평가
- `reports/` : 실제 reread / observation / meaning 정리
- `policies/` : 운영 정책

질문:
- 무엇이 잠겼는가
- 무엇이 실제 관찰 결과인가
- 무엇이 아직 provisional인가

### 2.5 `app/`

역할:
- engine body / runtime body / work memory

중심 하위:
- `core/runtime/`
- `runtime/`
- `work/`

질문:
- 실제 engine rail은 어디에 있는가
- 어디가 mature body이고 어디가 experimental work tree인가

### 2.6 `runtime/`

역할:
- append-only trace / manifest / receipt / view surface

중심 하위:
- `manifests/`
- `receipts/`
- `views/`
- `events/`

질문:
- 실제로 무엇이 돌았는가
- 어떤 line/receipt/view가 남았는가
- 어떤 reference intake memory가 기록되었는가

---

## 3. read order for a new agent

새 에이전트는 아래 순서로 읽는 것이 맞다.

1. root philosophy
   - `CURRENT.md`
   - `vectorfl_status.md`
   - `vectorfl_philosophical_interpretation_v1.md`

2. source philosophy
   - `source_assets/declarations/*`
   - `source_assets/baselines/*`

3. current reread posture
   - [current_space_reread_operating_summary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/notes/current_space_reread_operating_summary_v0.md)
   - [space_three_axis_operating_loop_and_material_intake_spec_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_three_axis_operating_loop_and_material_intake_spec_v0.md)
   - [space_construction_line_reading_line_inspection_three_axis_spec_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_construction_line_reading_line_inspection_three_axis_spec_v0.md)

4. repo-wide structure
   - [vectorfl_replica_repo_wide_structure_and_trace_survey_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_replica_repo_wide_structure_and_trace_survey_v1.md)

5. current runtime memory
   - `runtime/manifests/latent_line_registry_v1.json`
   - `runtime/manifests/line_registry.json`
   - `runtime/manifests/reference_intake_memory_v0.json`

6. then actual observation
   - 외부 자료 1건 또는 내부 문제축 1건을 입구로 잡고 reread 시작

즉:
`철학 -> 운영 루프 -> 구조 지도 -> 실제 trace -> reread`
순서가 맞다.

---

## 4. current three-axis operating model

### 4.1 space construction

하는 일:
- 입력 수집
- 분절
- 저장
- provenance / receipt / trace 생성
- 기능 구현
- 변경 이유 재료화

### 4.2 line reading

하는 일:
- 같은 재료에서 line 후보 보기
- 같은 line을 다른 목적어/폴더/코드/runtime/view에 대입
- line thickening과 응결 조짐 보기
- human-language meaning reread까지 내려가기

### 4.3 line inspection

하는 일:
- 반복성 확인
- cross-line interference 확인
- philosophy fit / mismatch 확인
- premature naming 방지
- depth-entry check

---

## 5. current strongest repeated lines

현재 반복적으로 가장 두껍게 보이는 선은 아래다.

- preserve before promotion
- calibration before ingest
- hold / parked / defer discipline
- reread before concept freeze
- space first, llm later
- line-first observation before hub naming
- construction / reading / inspection separation

즉 이 공간은 지금
빠른 실행기보다
`느린 숙성 + 반복 reread + 늦은 응결`
쪽이 더 본체에 가깝다.

---

## 6. important operating caution

새 에이전트가 특히 조심해야 할 편향은 아래다.

### 6.1 explanation-first convergence

- `docs/specs`, `docs/notes`, `docs/reports`만 읽고
  line을 빨리 이름 붙이기 쉬움

### 6.2 one-pass naming temptation

- 한 번 읽고 line/hub라고 부르기 쉬움

### 6.3 under-reading runtime/reference evidence

- 실제 반복성과 evidence는
  `references/`, `runtime/`, `app/work/`에도 많은데
  문서층만 과대평가하기 쉬움

### 6.4 lock pull

- reread가 충분하기 전에 note/spec/close-out로 수렴하기 쉬움

즉 새 에이전트는
설명 밀도 높은 층만 읽고 결론 내리면 안 된다.

---

## 7. minimum reread rule

현재 기준에서 한 번 읽고 line을 확정하면 안 된다.

최소:

- 같은 line을 4~5회 reread
- 목적어 변경
- 폴더 변경
- 코드/runtime/view 교차
- 가능하면 무관한 line도 교차 참조

그 뒤에도 살아남는 응결만
잠정 line / 잠정 hub로 다룬다.

---

## 8. references lane rule

reference는 다음 셋으로 나눠 기억한다.

- `adopt_now`
- `keep_as_calibration_reference`
- `defer_with_reason_memory`

중요:

- 지금 필요없음 = 불필요함 아님
- `not now`를 `not needed`처럼 쓰면 안 됨
- future reopen condition을 처음부터 같이 남겨야 함

예:
- `references/ralph/ralph-main`
- `references/ralph/claude-code-main`

둘 다 지금 본체가 아니라 calibration memory지만,
later execution harness / pluginized surface의 seed로 다시 열릴 수 있다.

---

## 9. what a new agent should not do

- hub를 먼저 정하지 말 것
- strong/weak를 본질값처럼 다루지 말 것
- reference 전체를 도입 대상으로 보지 말 것
- explanation layer만 읽고 line이라 부르지 말 것
- construction 없이 reading만 하지 말 것
- meaning reread 없이 structure summary만 하지 말 것

---

## 10. what a new agent should do first

새 에이전트의 첫 작업은 보통 아래가 맞다.

1. 자료 1건 또는 reference 1건을 입구로 잡는다
2. line 3~5개를 잠정적으로 뽑는다
3. 그 line으로 `source_assets / docs / references / app / runtime`를 다시 읽는다
4. human-language meaning reread까지 내려간다
5. inspection으로 premature naming을 걷어낸다
6. 결과를 report 또는 note로 남긴다

---

## 11. one-line summary

이 공간은 정답을 빨리 잠그는 엔진이 아니라,
재료를 넣고 line을 반복 reread하며,
그 line이 두꺼워지고 응결이 뒤늦게 드러나도록 만드는
space-first maturation engine으로 읽어야 한다.
