# engine_operator_automation_split_v1.md

## 1. purpose

이 문서는 현재 freeze된 state-first process console 엔진에서
무엇을 자동 파이프라인으로 돌리고,
무엇을 메인 테크니션 판단층으로 남길지를 고정한다.

핵심 목적은 두 가지다.

- 반복 처리에는 토큰을 덜 쓰고
- 판단/검토/교정/반영에는 토큰을 더 쓴다

---

## 2. top principle

### 2-1. automation-first for repetition

아래 성격의 작업은 기본적으로 자동화 우선이다.

- 반복 실행
- 반복 변환
- 반복 surface refresh
- 반복 validation
- 반복 receipt/log/report skeleton 작성

### 2-2. operator-first for judgment

아래 성격의 작업은 메인 테크니션 직접 판단 우선이다.

- canonical 경계 판정
- 보수적 enum 선택
- compare 결과 해석
- blocker/attention 의미 분리
- freeze 유지/해제 여부 판단
- derived 과잉 해석 억제

### 2-3. no silent promotion

자동화 층은 high-level object, naming-heavy 해석, 구조 승격을
자동으로 canonicalize하지 않는다.

---

## 3. official split

## 3-1. fully automatable lane

아래는 스크립트/파이프라인으로 기본 처리한다.

### source/run lane

- source path resolve
- probe run execution
- compare run batch execution
- generated output path registration

### canonical state lane

- validated record append
- latest regeneration
- history write
- update provenance stamping

### derived refresh lane

- diff regeneration
- interpretation badge regeneration
- attention queue refresh
- attention resolution pass
- attention memory refresh
- compacted history refresh

### surface preparation lane

- process console payload build
- header/state panel/queue/memory payload refresh
- latest index rebuild

### maintenance lane

- receipt generation
- delta log append
- report skeleton generation
- fixture rerun
- consistency checks

---

## 3-2. operator judgment lane

아래는 메인 테크니션이 계속 직접 맡는다.

### canonical judgment

- `packet_texture` 보수 판정
- `grounding_status` 상향/하향 판정
- `emergence_status` 과대승격 방지
- `carryover_risk` 보수 판정
- `maturation_state` tie-break read
- `comparison_memory_reason` / `gate_blocker_summary` 선택

### compare judgment

- segmentation-sensitive인지
- intrinsic compression dominant인지
- mixed/partial recovery인지
- baseline overwrite를 허용할지 말지

### layer judgment

- core 변경 필요 여부
- derived 결과를 어디까지 surface에 올릴지
- experimental을 어떤 수준에서만 노출할지
- freeze 경계 유지 여부

### correction judgment

- automation 결과가 과장됐는지
- provenance_only를 active issue처럼 읽고 있는지
- naming-heavy signal이 canonical로 새고 있는지

---

## 3-3. hybrid lane

아래는 자동 산출 + 인간 판정의 결합으로 간다.

### candidate state build

- 자동:
  - probe/read artifact 요약
  - candidate enum suggestion
  - evidence_refs 정리
- operator:
  - 최종 canonical state 선택

### compare report

- 자동:
  - parameter table
  - result comparison table
  - changed field listing
- operator:
  - final judgment
  - recommendation

### queue/attention reading

- 자동:
  - priority routing
  - queue lifecycle
  - memory summary generation
- operator:
  - 중요도 재해석
  - false positive 억제

---

## 4. current automation targets

현재 바로 스크립트화/강화해야 할 대상:

1. single-asset live run orchestration
2. compare run orchestration
3. canonical state candidate assembler
4. derived surface full refresh command
5. process console payload verification command
6. report/receipt/log bundle writer

---

## 5. current operator responsibilities

현재 내가 계속 직접 책임지는 것:

1. canonical state finalization
2. compare verdict wording
3. blocker/attention 의미 교정
4. freeze boundary policing
5. experimental leakage detection
6. false recovery / false improvement 차단

---

## 6. execution rule

앞으로 기본 실행 순서는 아래를 따른다.

1. automation lane이 raw run, append, refresh, verification을 수행한다
2. operator lane이 결과를 읽고 보수 판정을 내린다
3. 필요한 correction만 다시 반영한다
4. 최종 report/receipt는 operator judgment가 잠긴 뒤 닫는다

---

## 7. prohibition

자동화 층에서 금지:

- canonical field 추가/수정
- update policy 우회
- baseline latest 무단 overwrite
- high-level object 자동 승격
- experimental namespace의 canonical 침투
- graph-first surface 재정의

---

## 8. one-line lock

반복 가능한 것은 파이프라인이 처리하고, 의미 경계와 보수 판정은 메인 테크니션이 맡는다. 이 엔진의 자동화 목적은 인간 판단을 대체하는 것이 아니라, 인간 판단이 더 고품질로 집중되게 만드는 것이다.
