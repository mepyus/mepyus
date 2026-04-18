# VectorFL Paper Structural Flow Inheritance Lock v0

이 문서는 `Paperclip`를 `VectorFL Page`로 포크할 때  
단순 shell composition만이 아니라, `운용 흐름 구조`까지 어디까지 계승할지를 잠근다.

목적은 Paperclip의 ontology를 들이는 것이 아니라,  
`기관에 일이 부여되고, 흐름이 다음 기관으로 이어지며, 그 이동과 상태가 표면에 보이는 구조`를 VectorFL 쪽으로 다시 소유하는 것이다.

## 1. Core Sentence

VectorFL Paper는 Paperclip의 login/account layer는 버리더라도,  
`case가 들어오고 -> 현재 담당 기관/lane에 놓이고 -> 다음 기관으로 흐를 수 있으며 -> 그 상태와 제한이 표면에 드러나는 운영 흐름 구조`는 적극적으로 계승한다.

즉 가져오는 것은 `issue ontology`가 아니라  
`work progression structure`다.

## 2. What Must Be Inherited

현재 단계에서 VectorFL Paper가 Paperclip에서 구조적으로 계승해야 하는 것은 아래다.

### 2-1. assigned work visibility

- 지금 무엇이 현재 처리 단위인가
- 어느 기관 / lane이 그것을 받고 있는가
- 어떤 제한이 걸려 있는가

즉 `누가 지금 받고 있는가`가 보여야 한다.

### 2-2. progression visibility

- 현재 단계가 무엇인가
- 다음 기관 / 다음 lane 후보가 무엇인가
- 지금 멈춰 있는가, 진행 중인가, 재검토 중인가

즉 흐름은 단순 상세 페이지 안에 숨어 있지 않고,
`진행 구조`로 보여야 한다.

### 2-3. responsibility surface

- 입력기 쪽에서 잡고 있는가
- line/state 쪽에서 붙잡고 있는가
- translation / flow interpretation 쪽에서 좁혀 읽고 있는가
- governance가 hold 중인가

즉 `어느 기관이 현재 책임을 가지고 있는가`가 표면에 드러나야 한다.

### 2-4. next-hop legibility

- 다음 기관 / 다음 lane / 다음 reread 방향이 무엇인가
- 아직 확정이 아니라 candidate인지
- governance 때문에 보류인지

즉 `다음 흐름의 가시성`이 있어야 한다.

### 2-5. history-coupled operation

- 현재 상태와 history/trace가 분리되지 않아야 한다
- 지금 current-reading이 어떤 trace / residue / reentry와 이어지는지 보여야 한다

즉 progression은 history와 분리된 generic kanban이 되어서는 안 된다.

## 3. What Is Not Inherited

아래는 구조적으로도 그대로 들이지 않는다.

- company hierarchy
- project / goal naming
- issue naming
- heartbeat naming
- approval / budget naming
- account / login / org workspace model

즉 `운용 흐름 구조`는 계승하지만,  
그 흐름을 설명하는 Paperclip 고유 ontology는 계승하지 않는다.

## 4. VectorFL Re-Semanticization Rule

Paperclip의 구조 흐름은 아래처럼 VectorFL 의미로 다시 쓴다.

- issue progression
  -> `case / lane progression`
- assignee visibility
  -> `current organ / current lane responsibility`
- detail status
  -> `current-reading + governance state`
- activity timeline
  -> `trace / residue / reentry history`
- blocked / needs approval
  -> `hold / restriction / observer-only / promotion forbidden`

즉 구조는 남기되, 의미는 VectorFL이 다시 소유한다.

## 5. Required Structural Surfaces

현재 단계에서 VectorFL Paper에 반드시 보여야 하는 구조면은 아래다.

### 5-1. current responsibility strip

- 지금 어느 기관 / lane이 case를 받고 있는지

### 5-2. progression strip

- 직전 / 현재 / 다음 후보 흐름

### 5-3. governance visibility

- hold, restriction, release condition, next check trigger

### 5-4. trace-coupled explanation

- 왜 이 단계에 머무는지
- 어떤 residue가 다음 reread를 여는지

### 5-5. linked-program visibility

- 외부 프로그램과 어떤 경계로 이어져 있는지

## 6. First Build Consequence

이 기준이 들어오면 첫 build line의 해석도 더 선명해진다.

- `Current Reading`
  - 단순 상세 body가 아니라 현재 흐름 중심면
- `Cases / Queue`
  - 단순 목록이 아니라 progression entry surface
- `Inputs / Intake`
  - 앞단 재료면
- `History / Trace`
  - 현재 흐름의 근거면
- `Programs / Connections`
  - 외부 접속 경계면

즉 queue와 detail은 따로 노는 면이 아니라,
`current responsibility + progression + governance + trace`를 함께 보여주는 구조로 읽어야 한다.

## 7. What This Changes From Earlier Reading

이 문서는 이전의 `shell composition only` 읽기를 부정하지 않는다.  
다만 그 위에 한 가지를 더 추가한다.

- 이전:
  - frame, panel, queue, detail, history composition을 가져온다
- 지금:
  - 그 composition 위에 `운용 흐름 구조`도 같이 계승한다

즉 VectorFL Paper는 더 이상 `예쁜 껍데기 포크`가 아니라,  
`운용 구조를 다시 소유한 포크`로 읽어야 한다.

## 8. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Paper는 Paperclip의 ontology를 가져오지 않지만, 현재 처리 단위의 책임 위치, 기관 간 진행 구조, governance에 의한 정지와 보류, trace와 결합된 흐름 설명, 다음 기관으로의 이동 가시성이라는 운영 흐름 구조는 적극적으로 계승하여 VectorFL의 case/lane/current-reading/governance/trace 의미로 다시 소유한다.`
