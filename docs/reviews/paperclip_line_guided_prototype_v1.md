# Paperclip Line-Guided Prototype v1

## 핵심 아이디어

이 prototype은 Paperclip를 우리 공간으로 대체하지 않는다.

대신 아래 구조를 만든다.

- Paperclip가 업무를 할당한다
- 에이전트는 바로 일을 시작하지 않는다
- 먼저 할당된 업무를 우리 공간의 line으로 번역한다
- 그 line을 기준으로 업무를 처리한다
- 처리 과정과 결과를 다시 공간으로 밀어넣는다
- 재주입된 line이 다음 업무 할당의 바닥이 된다

즉 우리 공간은 `사후 기록 저장소`가 아니라
`assignment-aware operating layer`가 된다.

## 왜 이 구조가 강한가

이 방식은 line을 한 번만 쓰지 않는다.

- 할당 전 line
- 처리 중 line
- 처리 후 reinjection line
- 다음 업무를 위한 reuse line

즉 line이 태그가 아니라
업무의 앞뒤를 연결하는 operating spine이 된다.

## 계층 구조

### layer 1. Paperclip orchestration

Paperclip가 맡는 것:

- 회사 구조
- agent 역할
- issue/task assignment
- heartbeat execution
- approval / budget / routing

### layer 2. assignment-to-line translation

우리 공간이 첫 번째로 개입하는 지점이다.

할당된 issue를 아래 질문으로 번역한다.

- 이 일은 어떤 line에 닿는가
- 관련된 기존 residue가 있는가
- 비슷한 work history가 있는가
- 이미 승격된 pattern이 있는가
- 어떤 corridor 또는 boundary에 속하는가

이 단계의 출력은 `line-guided work packet` 이다.

### layer 3. line-guided execution

에이전트는 issue 원문만 보고 일하지 않는다.

아래를 함께 본다.

- translated line summary
- relevant residue
- prior successful pattern
- caution / promotion notes

즉 작업의 입력이 `issue only` 에서 `issue + line context` 로 바뀐다.

### layer 4. process reinjection

작업이 끝나면 결과만 남기는 것이 아니라
처리 과정도 다시 공간으로 넣는다.

reinjection 대상:

- 작업 중 판단 분기
- 실패 residue
- 유효했던 pattern
- changed artifacts
- follow-up need

### layer 5. next-assignment reuse

재주입된 내용은 archive로 잠드는 것이 아니라
다음 assignment translation 때 다시 참조된다.

즉 기억이 바로 다음 일의 입력 구조를 바꾼다.

## 최소 흐름

### 1. assignment intake

Paperclip issue가 agent에 할당된다.

입력:

- issue id
- title
- description
- assignee
- project / goal / parent issue

### 2. line translation pass

우리 공간이 issue를 읽고 line packet으로 바꾼다.

출력 예시:

- `primary_line`
- `support_lines`
- `relevant_residue_refs`
- `promotion_refs`
- `execution_hints`
- `risk_notes`

### 3. execution

agent는 translated packet을 바닥으로 일한다.

즉 실질 입력은 아래 둘의 결합이다.

- original Paperclip assignment
- vectorfl line packet

### 4. reinjection

작업 후 아래를 기록한다.

- what changed
- what worked
- what failed
- what should be reused
- what remains unresolved

### 5. reuse

다음 issue가 오면
이전 reinjection 기록이 translation 단계에서 다시 사용된다.

## line packet이 중요한 이유

이 prototype의 핵심 객체는 `issue`가 아니라
`line-guided work packet` 이다.

이 packet은 아래 사이를 잇는다.

- Paperclip assignment
- vectorfl memory
- current execution
- future reuse

즉 issue를 그대로 처리하지 않고,
공간의 line을 통과시켜 의미를 붙인 뒤 처리하게 만든다.

## 우리 공간에 실제로 남는 것

이 구조가 되면 우리 공간에는 아래가 남는다.

### 1. assignment interpretation memory

업무를 어떻게 읽고 어떤 line으로 번역했는지 남는다.

### 2. execution residue memory

업무 도중의 실패, 보류, 애매한 판단이 residue로 남는다.

### 3. reusable operating pattern

반복 성공한 처리 방식이 pattern으로 올라온다.

### 4. agent-role operating history

특정 역할이나 agent가 어떤 line에서 잘 작동하는지 보인다.

### 5. next-work shaping memory

다음 업무를 더 잘 자르고 더 잘 안내하는 기반이 남는다.

## Paperclip 쪽에 실제로 생기는 이점

Paperclip는 단순 orchestration tool에서
더 두꺼운 운영 구조로 바뀐다.

- issue가 더 정확히 해석된다
- 같은 유형의 업무를 매번 처음부터 하지 않는다
- assignment quality가 올라간다
- 에이전트 실행 품질이 line-aware하게 올라간다
- 조직 운영 결과가 휘발되지 않는다

즉 Paperclip의 본래 기능은 유지하면서
업무 처리 품질과 장기 기억이 함께 붙는다.

## 도입 순서

### phase 1. translation only

먼저 assignment를 line packet으로 번역만 한다.

목표:

- issue를 line-aware하게 읽을 수 있는지 검증

### phase 2. translation + reinjection

그 다음 처리 과정과 결과를 공간으로 다시 밀어넣는다.

목표:

- residue와 pattern이 실제로 축적되는지 확인

### phase 3. reuse loop

그 다음 재주입된 line이 다음 assignment를 바꾸게 한다.

목표:

- 기억이 다음 일의 입력을 실제로 변화시키는지 검증

### phase 4. selective governance feedback

마지막에만 assignment/routing/approval에 제한적으로 되먹임한다.

목표:

- 우리 공간의 해석이 orchestration 품질을 개선하는지 확인

## 리스크

### 1. translation이 과하게 무거워질 수 있음

모든 issue마다 과도한 해석 단계를 붙이면 느려진다.

### 2. line이 너무 많아질 수 있음

assignment마다 새 line을 만들면 오히려 구조가 흐려진다.

### 3. Paperclip의 원래 모델을 흐릴 수 있음

번역은 보강이어야지 대체가 되면 안 된다.

## 기억할 문장

이 prototype의 가장 중요한 문장은 아래다.

- assignment를 line으로 번역하고
- line을 기준으로 실행하고
- 실행을 다시 line으로 밀어넣고
- 그 line이 다음 assignment의 바닥이 된다

## 결론

이 방식은 단순 sidecar보다 훨씬 강하다.

왜냐하면 우리 공간이

- 일의 앞에서 해석하고
- 일의 중간에서 안내하고
- 일의 뒤에서 흡수하고
- 다음 일의 앞에 다시 놓이는

다층 line spine이 되기 때문이다.
