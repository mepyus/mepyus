# CODEX TASK v2

## 역할
너는 `vectorfl_next`의 **bounded builder**다.

너의 역할은 기존 `vectorfl`를 수정하는 것이 아니라,
기존 `vectorfl`를 **참조만** 하면서,
새 폴더에 `ADJACENT_SPACE_CONTRACT_v2.md`를 만족하는 최소 코어 골격을 구축하는 것이다.

너는 철학 해설자가 아니다.
너는 계약서 구현자다.

---

## 1. 최우선 목표
이번 작업의 최우선 목표는 다음 하나다.

**새 폴더에 `material -> trace -> point_seed -> space_cell -> local_space -> bridge_trace` 코어 골격을 만든다.**

이번 단계에서 완성 우주를 만들려고 하지 마라.
이번 단계에서 reader/control/physics를 코어에 넣으려고 하지 마라.
이번 단계의 목표는 오직 **새 기준의 formation core scaffold** 다.

---

## 2. 작업 루트 원칙
- 기존 `vectorfl/`는 참조만 한다.
- 작업 대상은 새 폴더(`vectorfl_next` 또는 지정된 새 루트)다.
- 기존 `vectorfl/` 수정 금지.
- 기존 stage 폴더 복제 금지.

---

## 3. 구현 우선순위
아래 순서대로만 진행하라.

### Step 1. repo skeleton
새 폴더에 최소 구조를 만든다.

권장 최소 구조 예시:
- `app/core/`
- `app/models/`
- `app/runtime/`
- `app/events/`
- `app/readers/` (빈 placeholder 가능)
- `docs/`

중요:
- 기존 stage0/stage1/stage2 이름 체계를 그대로 복제하지 마라.
- 새 코어 계층을 기준으로 구조를 잡아라.

### Step 2. core model definitions
다음 객체를 우선 구현한다.
- Material
- Trace
- PointSeed
- PressureProfile
- SpaceCell
- LocalSpace
- BridgeTrace

### Step 3. state transition scaffold
다음 상태 enum / state machine 뼈대를 만든다.
- SeedState
- CellState
- LocalSpaceState

### Step 4. append-only event log scaffold
상태 전이를 append-only event로 남기는 구조를 만든다.

### Step 5. minimal formation service boundary
다음 경계만 만든다.
- material ingest
- trace register
- point seed candidate creation
- space cell candidate creation
- local space formation check
- bridge trace registration

중요:
실제 알고리즘 완성보다 **경계와 불변조건**을 먼저 구현한다.

---

## 4. 구현 시 반드시 지켜야 할 불변조건

### 4-1. Material
- immutable
- raw payload 보존
- reader summary 덮어쓰기 금지

### 4-2. Trace
- evidence-bearing record
- 확정 edge 금지
- 단독 승격 트리거 금지

### 4-3. PointSeed
- 임시 응결핵
- ranking / promotion / eligibility 금지
- independent final object 금지

### 4-4. SpaceCell
- 최소 공간 단위
- cluster candidate 금지
- point의 약한 버전 금지

### 4-5. LocalSpace
- 큰 cell 금지
- 단순 aggregation 금지
- auto merge 금지

### 4-6. BridgeTrace
- merge trigger 금지
- transport lane 금지
- promotion trigger 금지

---

## 5. 시간/감정/환류에 대한 구현 태도
이 셋을 별도 해결 객체로 만들려고 하지 마라.

이번 단계에서 구현해야 하는 것은:
- 시간/감정/환류를 별도 본체로 정의하는 것 아님
- 그런 압력 변화가 **나중에 형성 경로를 바꿀 수 있는 구조적 자리**를 남기는 것

즉 다음이 가능해야 한다.
- pressure profile이 확장 가능하다
- reentry / lineage / source_run_ref를 담을 수 있다
- material이 재유입될 수 있다
- 같은 material family가 다른 cell/local space에 다시 놓일 수 있는 여지를 막지 않는다

---

## 6. 절대 금지

### 금지 1
기존 `vectorfl`의 코드 블록, stage 폴더, 실행 구조를 통복사하는 것

### 금지 2
기존 nomenclature만 바꿔서 재포장하는 것

### 금지 3
point/cluster/promotion 중심 설계를 다시 끌고 오는 것

### 금지 4
reader vocabulary(spine/basin/leak/return 등)를 core model field로 집어넣는 것

### 금지 5
시간/감정/환류를 속성 필드 몇 개 추가로 처리하는 것

### 금지 6
과도한 완성 욕심으로 복잡한 알고리즘까지 한 번에 넣는 것

### 금지 7
bounded step을 넘는 대규모 리팩터링

---

## 7. 이번 턴 최소 구현 범위
이번 턴에서 우선 만들어야 할 최소 범위는 다음이다.

1. 새 폴더 구조
2. core object definitions
3. state enum / transition scaffold
4. append-only event record schema
5. minimal service boundary skeleton
6. docs에 object/flow 설명 초안

이번 턴에서 하지 말아야 할 것:
- physics reader 구현
- probe logic 구현
- scoring optimization
- visualization
- CLI orchestration 완성
- 기존 reference space migration

---

## 8. 참고 아카이브 취급 방식
`GRAVITY-SCAFFOLD-VFL INTEGRATION` 류 문서는 **참조만** 한다.

그 문서에서 가져와도 되는 것:
- reader/control layer에서의 해석 vocabulary 아이디어
- reference center space local repair 시각

그 문서에서 코어로 가져오면 안 되는 것:
- spine/basin/leak를 core ontology로 박는 것
- 057/101 repair logic을 universal law로 승격하는 것

---

## 9. 보고 형식
매 턴 아래 형식으로만 보고하라.

### 1. current diagnosis
- 지금 구현 단계가 어디인지
- 남은 핵심 리스크가 무엇인지

### 2. exact changes
- 만든 파일
- 각 파일의 역할

### 3. contract check
- 이번 턴에 지킨 계약
- 위반 위험이 남은 지점

### 4. next bounded step
- 다음 한 단계만 제안

---

## 10. 완료 판정
다음이 충족되면 이번 1차 빌드는 성공이다.

- 새 폴더에 formation core scaffold 존재
- material/trace/point_seed/space_cell/local_space/bridge_trace 객체 정의 완료
- 상태 enum 및 event log scaffold 존재
- 기존 `vectorfl` 직접 수정 없음
- 기존 stage 폴더 복제 없음
- reader vocabulary가 core에 침범하지 않음

---

## 11. 한 줄 실행 기준
**새 엔진은 point를 빨리 증명하는 엔진이 아니라, space_cell을 최소 공간 단위로 삼아 형성 중인 공간을 보존하는 엔진이어야 한다.**
