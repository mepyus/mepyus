# ADJACENT SPACE CONTRACT v2

## 0. 문서 목적
이 문서는 `vectorfl_next` 재구축의 공통 계약서다.

목적은 기존 `vectorfl`를 고치거나 복제하는 것이 아니라,
기존 `vectorfl`를 **동결된 참조본(frozen reference)** 으로 두고,
새 폴더에 **공간 형성 우선 / 조기 수렴 금지 / 다중 local space 허용** 기준을 가진 새 엔진 골격을 세우는 것이다.

이 계약서는 Codex CLI와 Gemini CLI 모두가 공유하는 최상위 기준선이다.

---

## 1. 최상위 목표
이번 작업의 목표는 완성 우주를 만드는 것이 아니다.

이번 작업의 목표는 다음 한 줄로 고정한다.

**입력을 빠르게 점/군집으로 닫지 않고, 살아 있는 압력 아래 material이 trace, point seed, space cell, local space로 자라날 수 있는 코어 골격을 새 폴더에 세운다.**

---

## 2. 기존 `vectorfl`의 지위
기존 `vectorfl`의 지위는 다음과 같다.

- 수정 대상이 아니다.
- 직접 확장 대상이 아니다.
- stage 폴더 복제 출처가 아니다.
- 참조 표본이다.
- 실패 패턴과 살아남아야 할 자산을 읽는 기준 사례다.

### 허용
- 설계 판단 참고
- 실패 재발 방지 참고
- observer / artifact / naming / invariants 참고

### 금지
- `stage0/stage1/stage2` 통복사
- 기존 폴더 내부 코드 직접 수정
- 기존 semantics를 이름만 바꿔 이식
- 기존 reference center 판독 language를 전역 법칙으로 일반화

---

## 3. 새 엔진의 정체
새 엔진은 다음과 같이 정의한다.

**새 엔진은 입력을 빨리 판정하는 엔진이 아니라, material이 살아 있는 압력 아래 서로 다른 위치와 관계를 가지며 local space로 자라나는 공간 형성 엔진이다.**

새 엔진은 다음을 지향한다.

- 판정보다 형성 우선
- 결과보다 보존 우선
- 단일 절대공간보다 다중 local space 우선
- merge보다 bridge trace 우선
- reader/control vocabulary와 core vocabulary 분리

---

## 4. 코어 계층 고정
새 엔진의 코어 계층은 아래 순서로만 자란다.

`material -> trace -> point_seed -> space_cell -> local_space -> bridge_trace`

### 절대 금지
- `material -> point` 직행
- `trace -> edge` 확정 직행
- `seed -> promoted point` 직행
- `space_cell -> cluster candidate` 재해석
- `cell 없이 local_space` 직행
- `bridge 생성 즉시 merge`

---

## 5. 최소 원칙

### 5-1. Material 우선
- 코어의 최소 원시 단위는 `material`이다.
- material은 immutable이다.
- 원문 수정 금지.
- reader 요약 덮어쓰기 금지.

### 5-2. Space Cell 우선
- 코어의 최소 공간 단위는 `space_cell`이다.
- `space_cell`은 점의 약한 버전이 아니다.
- `space_cell`은 형성 중인 공간을 보존하는 최소 공간 단위다.

### 5-3. Pressure 수용성
새 엔진은 시간/감정/환류를 별도 객체로 먼저 정의해 담는 것이 아니라,
살아 있는 압력과 상태 변화가 들어왔을 때 공간 형성 경로가 달라질 수 있어야 한다.

즉 중요한 것은 필드 수가 아니라,
다음이 가능하냐이다.

- 같은 material이 다시 들어왔을 때 다른 seed / cell / local space로 다시 놓일 수 있는가
- 기존 cell을 흔들 수 있는가
- 다른 bridge를 만들 수 있는가
- 새로운 local space를 열 수 있는가

### 5-4. Reader / Probe 분리
다음 단어들은 코어 vocabulary가 아니다.

- spine
- basin
- leak
- return
- mass
- attraction
- repulsion
- vortex
- wave

이 단어들은 **reader / probe / control** 계층 전용이다.

---

## 6. 핵심 객체 계약

### 6-1. Material
최소 원시 입력 단위.
필수 역할:
- 원문 보존
- 유입 시점 기록
- actor / session / project / source 기록
- 공간 재유입 가능성 보존

### 6-2. Trace
확정 edge가 아니라 **evidence-bearing trace**.
필수 역할:
- 약한 연결 근거 보존
- temporal reentry / context overlap / shared handle / contrast / co-occurrence 등 근거 기록

### 6-3. Point Seed
확정 point가 아니라 **임시 응결핵**.
필수 역할:
- cell 형성을 위한 중간핵
- 반복 응결 가능성 보존

### 6-4. Pressure Profile
cell 형성에 영향을 주는 살아 있는 압력 프로필.
최소 축 예시:
- temporal_pressure
- session_pressure
- project_pressure
- scene_pressure
- tone_pressure
- recurrence_pressure

중요: pressure는 hard truth가 아니라 **support_refs + strength_hint** 구조여야 한다.

### 6-5. Space Cell
다음 고정 문장을 정의로 사용한다.

**space_cell은 pressure profile 아래 함께 유지되는 material / trace / seed를 보존하는 최소 공간 단위다.**

보강 정의:
- 최소한의 안/밖 구분을 가진다.
- 내부 결속 징후를 가진다.
- point나 cluster의 미완성 버전이 아니다.
- 형성 중인 공간 보존 단위다.

### 6-6. Local Space
여러 cell이 반복적으로 유지되며 하나의 독립된 국소 장으로 읽히는 단위.

### 6-7. Bridge Trace
space 간 관계 가능성을 기록하는 흔적.
- merge 금지
- transport lane 금지
- auto promote 금지

---

## 7. 상태 전이 원칙
상태는 단칼 판정보다 과정 상태를 보존하는 방향으로 둔다.

### Seed 상태 예시
- isolated
- forming
- reentering
- cell_candidate
- cell_bound

### Cell 상태 예시
- candidate
- held
- unstable
- reentering
- dissolved

### Local Space 상태 예시
- forming
- stable_local
- sparse
- boundary_heavy
- bridge_exposed

### 고정 원칙
- 상태 전이는 append-only event log로 남긴다.
- 현재 상태와 전이 이력을 분리 저장한다.
- 직접 덮어쓰기 금지.

---

## 8. 시간/감정/환류에 대한 구조 원칙
이 세 가지를 먼저 객체로 정의하지 않는다.
먼저 아래를 구조적으로 허용해야 한다.

### 시간성
- 재등장
- 재진입
- 상태 전이
- 시간에 따른 위치 이동 가능성

### 감정성
- 단순 tag가 아니라 압력장 변화에 영향을 줄 여지
- 같은 material이 다른 결로 다시 놓일 수 있는 여지

### 환류성
- LLM / agent / code / report / run 결과가 다시 material로 재유입될 수 있어야 함
- lineage가 이어져야 함
- 이전 결과가 다음 공간 형성에 흔적으로 남아야 함

고정 문장:

**새 엔진은 시간/감정/환류를 별도 칸에 저장하는 엔진이 아니라, 그런 감각적 압력 변화가 들어왔을 때 공간 형성 경로가 달라질 수 있는 엔진이어야 한다.**

---

## 9. 공통 절대 금지 목록

### 금지 1
기존 `vectorfl`의 stage 폴더 통복사

### 금지 2
기존 `vectorfl` 코드 직접 수정

### 금지 3
material을 바로 point처럼 다루는 구현

### 금지 4
trace를 확정 edge처럼 다루는 구현

### 금지 5
point_seed를 ranking / promotion / eligibility 중심으로 설계

### 금지 6
space_cell을 cluster candidate처럼 다루는 설계

### 금지 7
reader vocabulary를 core schema 필드로 박는 설계

### 금지 8
bridge 생성 즉시 merge

### 금지 9
기존 center/reference space용 local repair language(057/101 등)를 전역 intake law로 일반화

### 금지 10
시간/감정/환류를 별도 필드 추가만으로 해결했다고 간주하는 설계

---

## 10. 최소 성공 조건
아래가 성립해야 이번 작업을 통과로 본다.

1. 새 폴더에 별도 코어 골격이 생성된다.
2. 기존 `vectorfl`는 읽기 전용 참조 상태로 유지된다.
3. material이 immutable하게 저장된다.
4. trace가 evidence-bearing record로 저장된다.
5. point_seed가 임시 응결핵으로만 동작한다.
6. space_cell이 최소 공간 단위로 구현된다.
7. local_space가 cell 반복 패턴으로 형성된다.
8. bridge_trace가 merge 없이 기록된다.
9. reader vocabulary 없이도 core formation이 동작한다.
10. 시간/감정/환류를 위한 구조적 자리(압력 변화에 따른 형성 경로 변화 가능성)가 남아 있다.

---

## 11. 산출물 원칙
최소 산출물은 다음 범주를 포함해야 한다.

- core object schema 또는 model definitions
- state transition design
- append-only event log design
- storage / runtime path layout
- read-only reader / probe separation note
- existing vectorfl reference mapping note

---

## 12. 공통 보고 형식
각 CLI는 매 실행 턴마다 아래 형식으로 보고해야 한다.

### 12-1. what changed
- 추가/수정 파일
- 변경 목적

### 12-2. contract check
- 지킨 항목
- 위반 가능성 있는 항목

### 12-3. risk
- 조기 수렴 위험
- 기존 semantics 재유입 위험
- 구조 과잉/필드 과잉 위험

### 12-4. next bounded step
- 다음 한 단계만 제안

---

## 13. 한 줄 잠금 문장
**space_cell은 점의 미완성 버전이 아니라, 살아 있는 압력 아래 함께 유지되는 material/trace/seed를 보존하는 최소 공간 단위다.**
