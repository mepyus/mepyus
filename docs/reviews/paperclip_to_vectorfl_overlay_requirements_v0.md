# paperclip to vectorfl overlay requirements v0

## 1. purpose

이 문서는
`Paperclip에서 업무 할당과 실행이 일어날 때, 그 결과를 VectorFL이 받아 line 생성 / 추출 / 기록으로 처리할 수 있는가`
라는 질문에 대해,
구조적으로 필요한 최소 overlay requirement만 정리한다.

핵심은 Paperclip를 대체하는 것이 아니라,
Paperclip의 생성물을 VectorFL이 흡수할 수 있는지 보는 것이다.

## 2. current verdict

현재 코드 구조 기준으로는 가능하다.

이유는 Paperclip 안에 이미 VectorFL이 intake할 수 있는 surface가 분리되어 있기 때문이다.

- issue
- heartbeat run
- issue comment / run result
- approval / budget / pause
- org / assignee / parent-child relation

즉 VectorFL이 line 재료로 삼을 수 있는 `work`, `run`, `decision`, `artifact`, `relation`이 이미 있다.

## 3. minimum intake surfaces

VectorFL이 우선 받아야 할 1차 intake surface는 아래 3개다.

### 3-1. issue surface

- 무엇을 줌:
  - 업무 제목/설명
  - assignee
  - parent-child
  - project/goal/company 맥락
- 왜 중요한가:
  - 업무 단위를 line candidate의 root material로 바꿀 수 있다

### 3-2. heartbeat run surface

- 무엇을 줌:
  - 실행 시작/종료
  - status
  - context snapshot
  - session continuity
  - error / usage
- 왜 중요한가:
  - line 생성보다 먼저 `실행 경로`와 `reentry 흔적`을 얻을 수 있다

### 3-3. output artifact surface

- 무엇을 줌:
  - comment
  - result summary
  - produced file / URL / log
- 왜 중요한가:
  - 실제 결과를 line material, residue, surface seed로 바꿀 수 있다

## 4. vectorfl side requirements

Paperclip 결과를 VectorFL이 처리하려면 최소 아래 4층이 필요하다.

### 4-1. artifact intake layer

- issue / run / result / comment / governance event를 받는다
- source type을 구분한다
- Paperclip ontology를 그대로 유지한 채 source record를 만든다

### 4-2. line translation layer

- issue/work 설명 -> source line candidate
- run status / path -> transition/reentry hint
- result/comment -> observed line or residue line
- approval/pause -> governance note / hold trace

### 4-3. accumulation layer

- line registry
- residue memory
- execution trace
- later candidate grouping

여기서 핵심은:
- 새 line 생성 가능성
- repeated pattern 추출 가능성
- append-only 기록 가능성

### 4-4. advisory return layer

- Paperclip로 다시 돌려줄 최소 결과
- 예:
  - explanation-first caution
  - repeated blockage note
  - residue-backed next-work hint
  - issue reread note

## 5. what vectorfl can realistically do

현재 VectorFL이 이 overlay에서 현실적으로 할 수 있는 일은 아래 3가지다.

### 5-1. line generation

가능하다.

다만 처음부터 rich line ontology를 강제하기보다,
아래 정도가 현실적이다.

- work-root line candidate
- transition blockage line candidate
- readout/explanation line candidate
- residue line

즉 issue와 run 결과를 받아 line family seed를 만들 수 있다.

### 5-2. line extraction

가능하다.

다만 지금 단계에서는 formal flow line보다
`candidate extraction` 쪽이 더 현실적이다.

- repeated issue -> run -> result ordering
- repeated residue -> next issue tendency
- repeated explanation-first override
- repeated same-family recurrence

즉 Paperclip trace를 기반으로 later candidate grouping은 충분히 가능하다.

### 5-3. line recording

가장 현실적이고 바로 가능하다.

- append-only run trace
- issue-linked line note
- residue memory
- family/projection/route bias history

즉 기록은 가장 먼저 붙일 수 있는 층이다.

## 6. what is still unclear

아직 불명확하거나 별도 설계가 필요한 것은 아래다.

- Paperclip artifact를 어느 granularity로 intake할지
  - run 단위
  - comment 단위
  - issue state transition 단위
- Paperclip ontology와 VectorFL ontology를 어디까지 분리 보존할지
- advisory return을 Paperclip UI/issue/comment 어디에 붙일지
- governance event를 단순 기록할지, next run bias에 실제 반영할지

즉 가능성은 충분하지만,
connector granularity는 아직 정해야 한다.

## 7. most realistic first test

첫 실험은 가장 작게 가는 게 맞다.

1. Paperclip issue 1개 생성
2. codex_local agent heartbeat 1회 실행
3. issue / heartbeat run / result comment를 추출
4. VectorFL이 이를
   - line candidate
   - execution trace
   - residue note
   로 남김
5. 그다음 run에서 residue-backed next hint가 가능한지 확인

즉 처음부터 full integration보다
`issue -> run -> result -> vectorfl trace` 한 바퀴가 1차 검증 포인트다.

## 8. final judgment

질문에 대한 가장 정확한 답은 이렇다.

`Paperclip의 업무 할당과 실행 결과를 VectorFL이 받아 line 생성·추출·기록으로 처리하는 것은 구조적으로 가능하다.`

현재 기준으로는
- line 생성: 가능
- line 추출: candidate 수준으로 가능
- line 기록: 가장 먼저, 가장 안정적으로 가능

따라서 핵심 과제는
Paperclip를 로컬로 돌릴 수 있느냐 자체보다,
`issue / run / result / governance event를 VectorFL intake grammar로 넘기는 얇은 overlay를 어떻게 두느냐`
에 있다.
