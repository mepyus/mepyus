# User-Language Trace-to-Memory Operating Card 2026-05-11 v0

## 1. Status

```text
Document = user-language operating card
Status = CANDIDATE_USAGE_AID
Authority = explanation / orientation support only
Not baseline
Not official workflow
Not automation
Not schema
Not current-position update
```

## 2. 한 문장

```text
공간은 실행 흔적을 바로 기억으로 삼지 않는다.
흔적은 회수되고, 판단이 붙고, 경계가 표시된 뒤에야 기억 후보가 된다.
```

## 3. 가장 중요한 흐름

```text
runtime 흔적
-> worker 결과
-> Codex 회수 / 포장
-> movement record 또는 minimum trace packet
-> candidate 기억
-> 필요할 때만 명시적 current-position 앵커
```

## 4. 쉽게 말하면

### Runtime

```text
무언가 실행됐다는 흔적.
```

예:

```text
명령 실행 기록
Gemini raw result
manifest
receipt
folder status
```

뜻하는 것:

```text
일이 있었다.
무언가 관찰됐다.
파일이나 결과가 생겼다.
```

뜻하지 않는 것:

```text
그게 맞다.
승인됐다.
우리 기준이 됐다.
다음부터 자동으로 써도 된다.
```

### Recovery / Packaging

```text
흔적을 다시 읽어서 쓸 수 있는 판단으로 낮춰 담는 과정.
```

여기서 하는 일:

```text
무엇을 읽었는지 확인한다.
무엇을 안 읽었는지 표시한다.
과한 표현을 낮춘다.
WATCH / HOLD / RETURN 같은 배치를 붙인다.
승격하면 안 되는 것을 적는다.
```

### Candidate Memory

```text
앞으로 참고할 수 있는 기억 후보.
```

뜻하는 것:

```text
다음 판단에 도움 된다.
다시 꺼내 읽을 수 있다.
비슷한 작업의 참고점이 된다.
```

뜻하지 않는 것:

```text
확정된 원칙이다.
공식 workflow다.
baseline이다.
자동 실행 조건이다.
```

### Current-Position

```text
다음에 다시 들어올 때 어디서 시작해야 하는지 알려주는 명시적 앵커.
```

중요한 점:

```text
current-position은 자동으로 생기지 않는다.
유용한 결과가 나왔다고 바로 current-position이 되지 않는다.
명시적으로 앵커로 세울 때만 current-position이 된다.
```

## 5. 세 가지 짧은 규칙

```text
Receipt is not approval.
영수증은 승인이 아니다.
```

```text
Packaging before memory.
기억이 되기 전에 회수/포장이 먼저다.
```

```text
Anchor is explicit.
앵커는 자동이 아니라 명시적으로 세운다.
```

## 6. 지금 공간에서 생긴 힘

이제 우리는 Gemini나 runtime 결과를 보면 바로 이렇게 물을 수 있다:

```text
이건 그냥 흔적인가?
쓸 수 있는 후보 기억인가?
WATCH로 둬야 하나?
HOLD해야 하나?
current-position까지 갈 필요가 있나?
아니면 그냥 raw trace로 남겨야 하나?
```

이 질문들이 생겼다는 것이 중요하다.

단순히 정리된 것이 아니라, 공간이 결과를 삼키기 전에 판단을 회수할 수 있게 됐다.

## 7. Helper / Script에 대한 쉬운 말

helper가 나중에 생긴다면 도와도 되는 것:

```text
빠진 항목 찾기
source ref 후보 보여주기
not-inspected scope 적으라고 알림
do-not-promote 체크리스트 보여주기
빈 양식 초안 만들기
```

helper가 하면 안 되는 것:

```text
이 결과가 맞는지 판단
WATCH / HOLD / RETURN 배치 결정
recovered judgment 작성
current-position 업데이트
baseline 승격
```

## 8. 현재 위치

```text
Gemini whole-space map = 후보 지도 / WATCH
runtime-to-current-position map = 후보 연결 지도 / WATCH
recovery helper = Level 2 후보 카드 / 구현 아님
```

## 9. 다음 빌드업 방향

지금 당장 필요한 것은 새 스크립트가 아니다.

다음은 한 번 더 실제 반환을 수동 회수하면서 확인하는 것이다:

```text
반복되는 항목이 정말 같은가?
helper가 도와도 되는 부분이 정말 구조 체크뿐인가?
사람 판단이 필요한 부분이 어디서 나타나는가?
WATCH / HOLD / RETURN 배치가 여전히 사람이 해야 하는가?
```

## 10. Watch

```text
기술 문서가 사용자 언어를 밀어내는 것
helper가 판단자가 되는 것
current-position이 자동 workflow처럼 취급되는 것
Gemini 지도 반환이 검증된 진실처럼 취급되는 것
runtime 흔적이 승인처럼 취급되는 것
```

`STATUS: USER_LANGUAGE_TRACE_TO_MEMORY_OPERATING_CARD_PREPARED`
