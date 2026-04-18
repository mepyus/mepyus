# paperclip vectorfl first overlay test v0

## 1. purpose

이 문서는
Paperclip의 업무 할당/실행 결과를 VectorFL이 실제로 받아
`line 생성 / candidate 추출 / 기록`
재료로 처리할 수 있는지 보는
가장 작은 1차 overlay test를 정의한다.

목표는 full integration이 아니다.

이번 테스트의 목표는 아래 하나다.

- `issue -> heartbeat run -> result/comment`
  이 최소 흐름이 VectorFL 쪽에서
  `trace + residue + line candidate seed`
  로 남을 수 있는지 확인한다.

## 2. test philosophy

- Paperclip는 그대로 둔다
- Codex local agent도 그대로 둔다
- VectorFL은 sidecar/overlay로만 붙는다
- host ontology와 VectorFL ontology를 섞지 않는다
- 첫 테스트에서는 advisory return까지 욕심내지 않는다

즉 이번 실험은
`can ingest and retain`
를 보는 테스트다.

## 3. minimum test scope

### 3-1. host side

- company 1개
- codex_local agent 1개
- issue 1개
- heartbeat run 1회
- result/comment 1개 이상

### 3-2. vectorfl side

아래 3종만 남기면 성공으로 본다.

- execution trace 1개
- residue note 1개
- line candidate seed 1개

## 4. intake targets

이번 테스트에서 VectorFL이 받는 대상은 아래 3개만 제한한다.

### A. issue surface

- title
- description
- assignee
- project/goal/company context

### B. heartbeat run surface

- run id
- invocation source
- status
- started/finished
- context snapshot
- error or result summary

### C. output artifact surface

- issue comment
- run summary
- produced artifact ref if any

## 5. vectorfl-side interpretation rule

이번 첫 테스트에서는 과도한 ontology를 쓰지 않는다.

### 5-1. line generation

아래 정도만 보면 충분하다.

- work-root line candidate
- transition blockage / continuation line candidate
- explanation/readout line candidate

즉 issue와 run 결과에서
“어떤 distinction와 next action bias가 생겼는가”
만 잡으면 된다.

### 5-2. line extraction

첫 테스트에서는 formal extraction보다
`future extraction material produced`
 수준이면 충분하다.

즉:

- ordered run trace
- residue-to-next-work note
- repeated handoff를 나중에 볼 수 있는 trace

를 남기면 된다.

### 5-3. line recording

이번 테스트의 핵심 성공 조건이다.

최소 아래가 append-only로 남아야 한다.

- issue-root trace
- run trace
- result/residue note
- source artifact refs

## 6. minimal success conditions

아래 네 가지가 되면 1차 성공으로 본다.

1. Paperclip issue와 heartbeat run 정보를 밖으로 꺼낼 수 있다
2. VectorFL이 이를 source record로 저장할 수 있다
3. run 결과를 residue 또는 line candidate seed로 적을 수 있다
4. 다음 run에서 다시 참조할 수 있는 trace를 남길 수 있다

## 7. minimal failure conditions

아래 중 하나면 1차 실패로 본다.

- Paperclip run 결과를 안정적으로 추출하지 못함
- issue/run/result granularity가 너무 거칠어 VectorFL이 source material로 쓰기 어려움
- 결과가 단순 log dump만 되고 line candidate/residue로 전환되지 않음
- 기록은 남지만 다음 run에 재참조 가능한 형태가 아님

## 8. recommended first scenario

가장 작은 첫 시나리오는 아래다.

### scenario

- issue:
  간단한 문서 정리 또는 상태 요약 업무 1개
- agent:
  codex_local 1개
- run:
  heartbeat 1회
- output:
  comment 또는 result summary 1개

### why this scenario

- artifact가 단순하다
- 입력/결과 경계가 비교적 명확하다
- VectorFL이 trace/residue를 남기기 쉽다
- 실패해도 원인 분석이 쉽다

## 9. suggested vectorfl outputs for this first test

이번 첫 테스트에서는 아래 출력만 있으면 충분하다.

### 9-1. issue-root trace

- source: paperclip issue
- issue id
- title
- context
- selected initial line candidate label

### 9-2. run trace

- heartbeat run id
- status
- result summary
- related issue id
- transition note

### 9-3. residue note

- what remains unresolved
- what should bias the next run
- whether explanation-first / reread / retry / clarify is needed

## 10. what not to do in the first test

- full multi-agent org test
- budget/approval integration까지 동시에 보기
- UI embedding까지 같이 보기
- formal flow line promotion 보기
- complex family registry부터 먼저 만들기

첫 테스트는 어디까지나
`can Paperclip work results become VectorFL-readable retained material`
를 보는 것이다.

## 11. next step after success

이 첫 테스트가 성공하면 다음은 아래 둘 중 하나다.

- repeated runs 2~3회로 residue-backed next hint가 생기는지 보기
- issue/run/result 외에 approval/pause/governance event를 intake에 추가해보기

즉 첫 테스트 이후에야
generation/extraction/governance를 더 두껍게 붙이면 된다.

## 12. final judgment

가장 현실적인 첫 overlay test는
`Paperclip issue 1개 -> codex_local heartbeat 1회 -> result/comment 1개 -> VectorFL trace/residue 1회 기록`
이다.

이 수준이면
Paperclip 결과가 VectorFL에서

- line candidate seed가 되는지
- future extraction material이 되는지
- append-only memory가 되는지

를 과장 없이 확인할 수 있다.
