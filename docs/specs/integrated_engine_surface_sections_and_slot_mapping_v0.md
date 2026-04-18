# Integrated Engine Surface Sections and Slot Mapping v0

## 1. Purpose

이 문서는 현재 잠근 surface object contracts v0를 바탕으로 통합엔진 3면의 화면 섹션 순서와 각 섹션이 받는 primary contract slot을 얇게 고정하기 위한 문서다.

이 문서는 UI 디자인 문서가 아니고, 최종 컴포넌트 트리 문서도 아니며, 실제 state schema 확정 문서도 아니다.

현재 단계의 성격은 아래와 같다.

- section / slot 의미 경계 문서
- surface contract를 실제 화면 의미에 매핑하기 위한 중간 문서
- mock를 예쁜 샘플이 아니라 상태 객체를 받을 자리로 읽기 위한 문서
- 3면의 역할 혼합을 막기 위한 구조 정렬 문서

## 2. One-Line Lock

현재 통합엔진의 3면은 다음처럼 읽는다.

- 사용자면 = 목적 선언 + 팀 운영 표면
- 벡터플면 = 중간 흐름 / 통로 표면
- 엔진면 = 입력 / 처리 / 환류 컨트롤 표면

따라서 각 면의 섹션은 그 면의 역할을 더 선명하게 만들도록 정렬되어야 하며, 다른 면의 역할을 끌어오지 않도록 slot을 고정해야 한다.

## 3. Section / Slot Mapping Principles

### Principle 1. Surface First

섹션은 먼저 화면의 역할을 살리고, 그다음 contract를 받는다.

contract가 화면을 강제로 규정하는 것이 아니라, 이미 잠근 surface 역할을 contract가 지지하는 구조로 간다.

### Principle 2. Primary Contract First

각 섹션에는 먼저 primary contract를 붙인다.

보강 contract는 뒤에 붙일 수 있지만, 초기에는 primary contract가 무엇인지가 더 중요하다.

### Principle 3. Summary Is Not Ownership

다른 surface의 contract가 summary로 보일 수는 있지만, 그 contract의 owning surface가 바뀌는 것은 아니다.

예:

- `UserGoalState` 일부가 엔진면 summary에 보일 수는 있어도, 그 contract의 owning surface는 여전히 user surface다.

### Principle 4. Do Not Overfill

지금 단계에서는 모든 섹션을 꽉 채우려 하지 않는다.

섹션 이름과 slot 의미를 먼저 잠그고, 나중에 보강층을 얹는다.

## 4. User Surface Section Mapping v0

### 4.1 Surface Role

사용자면은 목적을 선언하고, 팀을 구성하고, 담당을 배치하고, 작업 흐름을 운영하는 표면이다.

핵심 단어:

- 목적
- 선언
- 팀
- 담당
- 운영

### 4.2 Section Order

#### Section A. Goal Declaration

Role:

- 현재 목적 선언의 중심축

Primary Contract:

- `UserGoalState`

What it should show:

- 현재 목표 제목
- 왜 이 목표를 하는지
- 이번 턴 범위
- 현재 상태

Why it comes first:

- 사용자면은 task board가 아니라 운영 선언면이므로, 목적이 항상 팀보다 먼저 와야 한다.

Not for now:

- 실행 버튼
- 자동 배정
- CLI 실행 트리거

#### Section B. Material Context

Role:

- 현재 목적이 어떤 공간 재료와 연결되어 있는지 보여주는 요약 영역

Primary Contract:

- `UserGoalState` summary
- 특히 `linked_ingest_ids` 계열

What it should show:

- 이번 목적에 연결된 입력 재료 수
- 엔진을 통해 들어온 관련 재료 요약
- 지금 목적이 맨땅이 아니라 어떤 재료 위에 있는지

Why it matters:

- 사용자면은 추상 선언만 하는 곳이 아니라, 현재 목적이 어떤 재료를 기반으로 하는지 알아야 한다.

Not for now:

- 엔진 입력 상세 관리
- ingest 재실행
- 파이프라인 제어

#### Section C. Team Relay Board

Role:

- 팀 구성과 relay 흐름의 중심판

Primary Contract:

- `TeamFlowState`

What it should show:

- 팀 목록
- 팀 역할
- 현재 상태
- 팀별 instruction
- 현재 중심 팀

Why it matters:

- 사용자면의 핵심은 카드 나열이 아니라 목적을 팀 흐름으로 조직하는 것이다.

Not for now:

- 팀 자동 생성
- 팀 자동 라우팅
- worker spawn 직접 실행

#### Section D. Handoff / Waiting / Report

Role:

- 현재 어느 팀이 무엇을 기다리고 있고, 어떤 handoff가 생겼는지 보여주는 운영 관찰 영역

Primary Contract:

- `TeamFlowState` summary

Secondary Candidate Later:

- `WorkMemoryRecord` summary only

What it should show:

- 현재 대기 상태
- handoff 상태
- done / hold / waiting 이유
- 팀 사이의 현재 relay 위치

Why it matters:

- 사용자면은 단순히 지시만 하는 면이 아니라, 흐름이 어디에 걸려 있는지도 봐야 한다.

Not for now:

- 장기 기억 상세 브라우저
- full log center
- repo/task execution history explorer

### 4.3 User Surface One-Line Lock

사용자면은 `Goal Declaration -> Material Context -> Team Relay Board -> Handoff / Waiting / Report` 순으로 읽히는 운영 선언면으로 잠근다.

## 5. VectorFL Surface Section Mapping v0

### 5.1 Surface Role

벡터플면은 사용자 작업과 엔진 처리 사이에서 현재 line / relation / gap / genealogy / ingress / reflux 상태를 드러내는 중간 통로다.

핵심 단어:

- line
- relation
- gap
- genealogy
- ingress
- reflux
- 중간 흐름

### 5.2 Section Order

#### Section A. Flow Summary

Role:

- 현재 목적과 연결된 중간 흐름의 요약

Primary Contract:

- `VectorFlowState`

What it should show:

- 현재 흐름에 대한 짧은 요약
- 현재 목적과 가장 직접 연결된 line 흐름
- 현재 중간 상태의 핵심 판단

Why it comes first:

- 벡터플면은 단순 atlas가 아니라 현재 목적의 중간 변화가 무엇인지 먼저 보여줘야 한다.

Not for now:

- 구현 지시
- 팀 운영 제어
- 엔진 명령 실행

#### Section B. Active Line Atlas

Role:

- 현재 표면에 떠오른 주요 line들을 보는 영역

Primary Contract:

- `VectorFlowState.active_lines`

What it should show:

- line title
- health
- current_stage
- 주요 연결 요약

Why it matters:

- 벡터플면은 line을 보여주되, 그 line이 현재 흐름 안에서 어떤 단계에 있는지 같이 보여줘야 한다.

Not for now:

- line 직접 수정
- line 직접 강화 명령
- 외부 검색 실행 명령

#### Section C. Relation / Gap Field

Role:

- 현재 흐름에서 부족한 지점과 연결 관계를 읽는 영역

Primary Contract:

- `VectorFlowState.gaps`
- relation summary candidate

What it should show:

- gap title
- 왜 비어 있는지
- 어떤 line과 연결되는지
- relation의 현재 밀도/부족 상태

Why it matters:

- 벡터플면은 예쁜 relation web이 아니라, 현재 흐름에서 어디가 얇고 어디를 보강해야 하는지를 보여주는 면이다.

Not for now:

- gap 자동 해결
- relation 재계산 실행
- 직접 정비 액션

#### Section D. Ingress / Reflux / Pending Trace

Role:

- 현재 line들이 ingress / processing / export / reflux / pending validation 중 어디에 있는지를 보여주는 흐름 strip

Primary Contract:

- `VectorFlowState.lineage_events`
- `VectorFlowState.active_lines.current_stage`

What it should show:

- 현재 유입 중인 것
- 현재 처리 중인 것
- export 대기
- reflux 중 상태
- 검증 대기 상태

Why it matters:

- 벡터플면이 중간 통로가 되려면, 현재 흐름 단계가 드러나야 한다.

Not for now:

- engine pipeline 상세 제어
- validation packet 조작
- ingest trigger

### 5.3 VectorFL Surface One-Line Lock

벡터플면은 `Flow Summary -> Active Line Atlas -> Relation / Gap Field -> Ingress / Reflux / Pending Trace` 순으로 읽히는 중간 통로면으로 잠근다.

## 6. Engine Surface Section Mapping v0

### 6.1 Surface Role

엔진면은 외부 자료를 공간 재료로 넣고, 현재 처리 흐름을 보고, 검증 환류를 다시 공간에 넣는 입력 / 처리 / 환류 컨트롤면이다.

핵심 단어:

- 입력
- 처리
- 파이프라인
- 환류
- 감시
- 정비
- 컨트롤

### 6.2 Section Order

#### Section A. Ingest Entry

Role:

- 외부 자료 입력 입구

Primary Contract:

- `EngineIngestState`

What it should show:

- 어떤 자료가 들어왔는지
- 어떤 경로에서 왔는지
- 현재 queued / processing / done / failed / hold 상태
- 어느 목적과 연결되었는지 요약 가능 여부

Why it comes first:

- 시나리오상 엔진면의 첫 장면은 외부 자료 입력이다. 따라서 엔진면의 첫 섹션도 입력 입구여야 한다.

Not for now:

- 파일 직접 수정
- repo write
- direct execute command
- autonomous retry

#### Section B. Pipeline Status

Role:

- 현재 엔진 처리 흐름 표시

Primary Contract:

- `EnginePipelineState`

What it should show:

- current step
- 전체 파이프라인 status
- 단계별 상태와 짧은 note
- 어디서 멈췄는지 / 어디까지 왔는지

Why it comes second:

- 입력이 들어온 뒤, 엔진면의 본질은 그 입력이 현재 어떤 처리 단계를 지나고 있는지 보여주는 데 있다.

Not for now:

- run now
- retry now
- auto recovery
- script body execution

#### Section C. Validation Return

Role:

- 검증 결과와 과정 잔여물이 다시 공간 재료가 되는 환류 입구

Primary Contract:

- `ValidationReturnPacket`

What it should show:

- 검증 환류 요약
- accepted refs
- hold refs
- reasoning note summary
- next reingest 요청 여부

Why it comes third:

- 엔진면은 입력과 처리만이 아니라 환류를 다시 공간으로 넣는 면이기 때문에, 환류 섹션은 1차 핵심 섹션이다.

Not for now:

- auto reingest
- autonomous fix request
- repo patch execution

#### Section D. Asset Inventory

Role:

- 엔진 자산 상태 요약

Primary Contract Later:

- `EngineAssetRegistry`

Why it is later:

- inventory는 중요하지만, 엔진면의 본질은 입력 / 처리 / 환류다. 따라서 inventory는 1차 핵심 섹션 뒤에 온다.

#### Section E. Watchpoint Registry

Role:

- 현재 감시 포인트 정리

Primary Contract Later:

- `WatchpointRegistry`

Why it is later:

- watchpoint는 엔진 감시를 두껍게 하지만, 입력/처리/환류보다 먼저 오면 엔진면이 admin dashboard처럼 보일 위험이 있다.

#### Section F. Event Trace

Role:

- 처리 과정 이벤트 추적

Primary Contract Later:

- `EventTraceState`

Why it is later:

- trace는 중요하지만, 지금 단계에서는 보강층으로 두는 것이 맞다.

#### Section G. Work Memory / Reasoning Notes

Role:

- 판단, 보류, close-out, handoff 기록의 얇은 표시

Primary Contract Later:

- `WorkMemoryRecord`

Why it is later:

- 기록은 중요하지만, 현재 엔진면 1차 구조는 입력/처리/환류를 먼저 살아나게 해야 한다.

### 6.3 Engine Surface One-Line Lock

엔진면은 `Ingest Entry -> Pipeline Status -> Validation Return -> Asset / Watch / Trace / Memory` 순으로 읽히는 공간 컨트롤면으로 잠근다.

## 7. Cross-Surface Notes

### 7.1 Shared Rule

secondary surface에서 보이는 contract는 summary consumption만 허용한다. owning surface가 바뀌는 것은 아니다.

예:

- `UserGoalState` 일부가 엔진 summary에 보일 수 있다.
- `ValidationReturnPacket` 일부가 사용자면 report summary에 보일 수 있다.

하지만 이 경우에도 contract ownership은 이동하지 않는다.

### 7.2 Do Not Mix

- 사용자면에 엔진 inventory를 주인공으로 놓지 않는다.
- 벡터플면에 팀 운영을 주인공으로 놓지 않는다.
- 엔진면에 목적 선언을 주인공으로 놓지 않는다.

## 8. Immediate Use

이 문서는 지금 당장 다음 용도로 쓴다.

1. 각 surface의 섹션 이름을 다시 정렬할 때
2. mock 화면에서 어떤 영역이 primary contract slot인지 표시할 때
3. Codex / Gemini에게 이 패널은 왜 여기에 있는가를 설명할 때
4. 보강층 4개를 어디에 붙일지 결정할 때

## 9. One-Line Final Lock

현재 통합엔진의 각 surface는 자기 역할을 살리는 섹션 순서와 contract slot을 먼저 잠그고, 그 위에 보강 상태를 얹는 방식으로 성숙시킨다.
