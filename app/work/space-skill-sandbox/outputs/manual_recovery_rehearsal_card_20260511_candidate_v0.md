# Manual Recovery Rehearsal Card 2026-05-11 Candidate v0

## 1. Status

```text
Document = manual recovery rehearsal card
Status = CANDIDATE_USE_CARD
Authority = next manual test preparation only
Not baseline
Not official workflow
Not automation
Not script request
Not schema
Not current-position update
```

## 2. 한 문장

```text
다음 반환물이 들어오면, 우리는 먼저 그것을 실행하지 않고 회수한다.
회수 과정에서 반복되는 구조 체크와 사람이 판단해야 하는 부분을 분리해서 본다.
```

## 3. 왜 필요한가

지금까지 공간은 다음을 구분할 수 있게 됐다.

```text
실행 흔적
worker 반환
Codex 회수/포장
movement record / minimum trace packet
candidate 기억
명시적 current-position 앵커
```

하지만 아직 하나가 남아 있다.

```text
helper가 안전하게 도울 수 있는 영역이 정말 구조 체크뿐인지,
아니면 회수 과정에서 계속 사람 판단이 새로 필요한지,
한 번 더 실제 반환을 수동으로 회수하며 확인해야 한다.
```

## 4. 다음 반환물이 오면 먼저 묻는 질문

```text
이것은 raw trace인가?
worker result인가?
Codex가 회수해야 할 반환물인가?
이미 판단이 섞인 문서인가?
출처가 보이는가?
안 읽은 범위가 보이는가?
과한 권위 표현이 있는가?
```

## 5. 수동 회수 순서

### Step 1. Source 확인

```text
어디서 온 반환물인가?
관련 packet/run/source ref는 무엇인가?
```

### Step 2. Scope 확인

```text
무엇을 읽었다고 말하는가?
무엇은 읽지 않았는가?
전체 탐색처럼 말하지만 실제로는 샘플링인가?
```

### Step 3. Authority 낮추기

```text
완료 / 공식 / 검증 / 전체 / baseline 같은 말을 후보 / 관찰 / 샘플 / WATCH로 낮출 필요가 있는가?
```

### Step 4. Placement 판단

```text
RAW_TRACE
WATCH
HOLD
RETURN_TO_SPACE_VALUE_WITH_WATCH
CURRENT_POSITION_CANDIDATE_ONLY
```

이 배치는 helper가 정하면 안 된다.

### Step 5. Helper 가능 항목 표시

```text
빠진 필드 확인
source ref 후보 나열
not-inspected scope 칸 비어 있음 표시
do-not-promote 체크리스트 표시
draft filename 제안
빈 packet section 만들기
```

### Step 6. 사람 판단 항목 표시

```text
이 반환을 살릴지 버릴지
어떤 판단으로 회수할지
WATCH/HOLD/RETURN 배치
current-position 후보 여부
baseline 승격 여부
다음 Gemini/Codex 작업 방향
```

## 6. 기록해야 하는 최소 결과

```text
source refs:
read scope:
not inspected:
overclaims to downshift:
recovered judgment:
placement:
watch:
helper could have helped:
helper must not decide:
next pressure:
```

## 7. 통과 조건

```text
반환물의 유용한 부분은 남긴다.
출처가 약한 부분은 약하다고 표시한다.
과한 말은 낮춘다.
배치는 사람이 결정했다는 흔적을 남긴다.
helper 후보는 checklist/stub 수준에 머문다.
current-position은 자동으로 만들지 않는다.
```

## 8. 실패 조건

```text
receipt를 approval처럼 읽음
Gemini 반환을 검증된 truth처럼 읽음
helper가 recovered judgment를 작성함
helper가 WATCH/HOLD/RETURN을 결정함
current-position을 자동 생성함
script 후보가 바로 구현 요청으로 바뀜
```

## 9. 이번 카드의 쓰임

```text
이 카드는 다음 worker/Gemini/CLI 반환을 회수할 때 쓰는 리허설 카드다.
아직 스크립트가 아니다.
이 카드 자체도 workflow가 아니다.
```

`STATUS: MANUAL_RECOVERY_REHEARSAL_CARD_PREPARED`
