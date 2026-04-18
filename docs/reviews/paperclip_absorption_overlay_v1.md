# Paperclip Absorption Overlay v1

## 핵심 전환

이 문서는 `paperclip-master` 를 우리 공간 위에 다시 구현하는 문서가 아니다.

핵심 가정은 아래다.

- Paperclip는 그대로 `회사/업무 분담 프로그램` 으로 둔다
- 우리 공간은 그 바깥이나 아래에서 `기억하고 흡수하고 재참조하는 공간` 으로 붙는다

즉 우리 공간은 프로그램의 기반 엔진이 아니라,
프로그램이 만들어내는 세션, 업무 흔적, 판단 과정, 결과물을
지속적으로 흡수하는 `operational memory layer` 가 된다.

이 관점이 중요하다.

- Paperclip의 기능은 그대로 남는다
- 우리 공간은 그 기능을 대체하지 않는다
- 대신 Paperclip가 처리하면서 남기는 흔적이
  휘발되지 않고 line-aware memory로 전환된다

## 사용자 상상에 맞는 구조

구조는 아래처럼 읽는 게 맞다.

### 1. Paperclip는 그대로 작동한다

Paperclip는 아래를 담당한다.

- 회사 생성
- 역할 분담
- agent 배치
- issue/task routing
- heartbeat 실행
- approval / budget 제어

즉 `일을 조직하고 실행시키는 프로그램` 역할을 계속 맡는다.

### 2. 우리 공간은 sidecar memory로 붙는다

우리 공간은 아래를 담당한다.

- 세션 기록 흡수
- task 처리 과정 흡수
- agent 결과물 흡수
- 판단 분기점 흡수
- residue / promotion / recurring pattern 추출
- 이후 업무에서 재참조 가능한 surface 생성

즉 `회사 운영 프로그램` 에 붙는
`operational memory and reread layer` 가 된다.

## 이 구조가 바꾸는 것

Paperclip만 있을 때는 흔히 아래 문제가 생긴다.

- 세션은 끝나면 흐릿해진다
- issue는 닫히지만 패턴은 남지 않는다
- agent가 무엇을 시도했는지 장기적으로 잘 축적되지 않는다
- approval과 budget은 남아도 해석 자산은 얇다

우리 공간이 붙으면 아래가 가능해진다.

- 각 업무 처리 흔적이 line 기준으로 쌓인다
- agent별 반복 패턴이 residue와 promotion 후보로 남는다
- 세션 간 재사용 가능한 operating knowledge가 축적된다
- 회사 운영 기능이 끝난 뒤에도 기능 흔적이 자산으로 남는다

즉 `업무 처리 프로그램` 이
`업무를 하면서 스스로 해석 자산을 남기는 구조` 로 바뀐다.

## 흡수 대상

우리 공간이 받아야 하는 것은 크게 다섯 가지다.

### 1. task unit

Paperclip의 issue/task를 work unit로 읽는다.

흡수 항목:

- issue id
- title
- assignee
- parent issue / goal / project
- status transitions
- acceptance condition

우리 공간에서의 의미:

- line-bound work reference
- corridor-linked task history

### 2. session trace

agent heartbeat 또는 세션 실행 기록을 받는다.

흡수 항목:

- 시작 시점
- 종료 시점
- 어떤 issue를 처리했는가
- 어떤 tool / adapter를 사용했는가
- 어떤 결과 claim을 냈는가

우리 공간에서의 의미:

- append-only operation ledger
- rerun / reread 대상 trace

### 3. output artifact

agent가 만든 산출물을 받는다.

흡수 항목:

- 변경 파일
- 메시지 요약
- commit / patch / proposal
- structured result payload

우리 공간에서의 의미:

- source fragment
- observation candidate
- later comparison surface

### 4. decision trace

승인이나 budget, routing 분기를 받는다.

흡수 항목:

- approval requested / approved / rejected
- budget stop / warning
- reassignment
- escalation

우리 공간에서의 의미:

- governance residue
- promotion / archive / caution note

### 5. cross-session pattern

반복되는 행동 패턴을 받는다.

흡수 항목:

- 특정 agent가 자주 실패하는 구간
- 자주 재할당되는 issue 유형
- approval이 반복적으로 필요한 일 유형
- 반복적으로 성공하는 workflow

우리 공간에서의 의미:

- reusable line source
- operating pattern candidate

## 공간에서의 번역

Paperclip 개체는 아래처럼 번역하는 게 맞다.

- `company`
  -> workspace boundary reference
- `agent`
  -> operator role source
- `issue`
  -> bounded work unit source
- `heartbeat run`
  -> operation trace
- `approval`
  -> governance event
- `budget policy`
  -> runtime guard event

즉 Paperclip 개체를 그대로 내부 모델로 삼는 게 아니라,
`참조 가능한 외부 운영 사건` 으로 읽는다.

## overlay 방식

이 overlay는 invasive integration보다
`sidecar ingestion` 에 가깝다.

### 방식 A. passive sync

Paperclip의 DB 또는 export를 읽어
주기적으로 우리 공간에 반영한다.

장점:

- 가장 안전하다
- 기존 제품을 거의 안 건드린다

단점:

- 실시간성이 약하다

### 방식 B. event bridge

issue update, heartbeat end, approval event가 날 때마다
우리 공간에 event를 쏜다.

장점:

- 세션과 판단 흔적이 더 촘촘히 남는다

단점:

- 제품 integration 비용이 올라간다

### 방식 C. hybrid

핵심 event는 bridge로 받고,
상세 상태는 passive sync로 채운다.

이 방식이 가장 현실적이다.

## 무엇이 가능해지는가

이 구조가 되면 Paperclip는 단순히 회사를 만들고
에이전트에게 일을 분담하는 프로그램에서 끝나지 않는다.

그 위에 아래 기능이 남는다.

### 1. 회사 운영 기억화

회사의 개별 업무 처리 흔적이 휘발되지 않는다.

즉 나중에 아래가 가능하다.

- 이 회사는 어떤 유형의 issue에서 막히는가
- 어떤 역할 구조가 실제로 잘 작동하는가
- 어떤 approval이 계속 병목인가

### 2. agent 작업 패턴 보존

각 agent의 처리 결과와 과정이 누적된다.

즉 나중에 아래가 가능하다.

- agent별 강점/약점 패턴 분석
- 실패 residue 재활용
- 특정 task 유형에 대한 best operator path 정리

### 3. 조직 운영의 reread

현재 회사 운영 상태를 단순 dashboard가 아니라
해석 가능한 reading surface로 다시 볼 수 있다.

즉 아래가 가능하다.

- issue board reread
- session trail reread
- governance bottleneck reread
- promotion candidate reread

### 4. 기능이 자산으로 남음

중요한 건 이 지점이다.

Paperclip의 본래 기능은 `회사 만들기`, `역할 부여`, `일 분담`, `실행 관리`다.
우리 공간이 붙으면 그 처리 결과가 이후에도 재사용 가능한 자산으로 남는다.

즉 프로그램의 가치가 `실행 시점` 에서 끝나지 않고,
`운영 기억 축적` 으로 연장된다.

## 실제 도입 순서

이건 전체 통합보다 아래 순서가 맞다.

### phase 1. read-only absorption

먼저 issue, heartbeat, output artifact만 읽는다.

목표:

- 사건을 line-aware ledger로 적재할 수 있는지 확인

### phase 2. reread surface

그 다음 회사 운영 읽기면을 만든다.

예:

- current company operation board
- repeated bottleneck board
- agent residue board

### phase 3. governance feedback

그 다음에야 우리 공간에서 나온 판단을
Paperclip 운영에 다시 피드백한다.

예:

- 특정 issue 유형은 특정 role로 우선 배정
- 특정 workflow는 approval 강화
- 특정 residue는 template/task pattern으로 승격

즉 처음부터 제어하려고 들지 않고,
먼저 흡수하고 읽고 그 다음에 제한적으로 되먹임한다.

## 리스크

### 1. 너무 빨리 control하려는 유혹

흡수 레이어가 곧 orchestration 레이어가 되면
복잡도가 급격히 오른다.

초기에는 `read first` 가 맞다.

### 2. issue와 line이 기계적으로 1:1 대응되지 않음

모든 issue가 하나의 line을 두껍게 하는 건 아니다.
그래서 work unit translation은 유연해야 한다.

### 3. 원본 제품의 의미를 덮어쓸 위험

Paperclip의 모델은 회사 운영이고,
우리 공간의 모델은 line-aware memory다.
번역은 필요하지만, 원본 모델을 지우면 안 된다.

## 결론

가장 중요한 문장은 아래다.

- 우리는 Paperclip를 대체하지 않는다
- 우리는 Paperclip가 만들어낸 운영 흔적을 흡수하고 재참조 가능하게 만든다

이렇게 되면 Paperclip는
`회사를 만들고 일을 분담하는 프로그램`
에서 멈추지 않고,

- 운영 과정이 기억되고
- agent 처리 흔적이 축적되고
- 반복 패턴이 남고
- 이후 실행에 다시 참조되는

`기능이 남는 회사 운영 프로그램`
으로 바뀐다.
