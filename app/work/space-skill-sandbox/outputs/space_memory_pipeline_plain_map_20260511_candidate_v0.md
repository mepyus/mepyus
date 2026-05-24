# Space Memory Pipeline Plain Map 2026-05-11 Candidate v0

## 1. Status

```text
Document = plain map
Status = CANDIDATE_REFERENCE_ONLY
Authority = user-facing explanation support
Not baseline
Not official workflow
Not automation
Not schema
Not current-position update
```

## 2. 지도

```text
[흔적]
  runtime / receipt / manifest / Gemini raw result

    |
    v

[반환]
  worker result / Gemini report / CLI output

    |
    v

[회수]
  Codex가 읽고 낮춘다.
  무엇을 읽었는지, 안 읽었는지, 과한 말은 무엇인지 본다.

    |
    v

[배치]
  RAW_TRACE / WATCH / HOLD / RETURN_TO_SPACE_VALUE_WITH_WATCH

    |
    v

[기억 후보]
  다음 판단에 도움 되는 candidate material

    |
    v

[명시적 앵커]
  필요하고 선택됐을 때만 current-position
```

## 3. 각 칸의 질문

### 흔적

```text
무슨 일이 있었다는 증거인가?
아니면 승인처럼 읽힐 위험이 있는가?
```

### 반환

```text
worker가 무엇을 봤다고 말하는가?
근거와 안 본 범위가 드러나는가?
```

### 회수

```text
무엇을 낮춰야 하는가?
무엇을 WATCH로 둬야 하는가?
무엇을 HOLD해야 하는가?
```

### 배치

```text
이건 raw trace인가?
후보 기억인가?
watch인가?
hold인가?
current-position까지 갈 이유가 있는가?
```

### 기억 후보

```text
다음에 무엇이 쉬워지는가?
쉬워지는 게 없다면 기억으로 올리지 않는다.
```

### 명시적 앵커

```text
다음 세션이 여기서 다시 시작해야 하는가?
사용자/현재 방향상 정말 앵커가 필요한가?
```

## 4. 지금까지 증명된 것

```text
Gemini whole-space map은 후보 구조 지도로 회수 가능했다.
runtime-to-current-position map은 후보 연결 지도로 회수 가능했다.
빈/약한 반환은 HOLD 경계로 회수 가능했다.
partial 반환은 WATCH로 살려둘 수 있었다.
```

## 5. 아직 증명되지 않은 것

```text
helper가 실제 회수에서 어디까지 안전하게 도울 수 있는지
여러 worker가 서로 다른 판단을 반환했을 때 어떻게 회수할지
current-position 업데이트가 필요한 실제 순간을 어떻게 판단할지
script가 반복 구조만 돕고 판단을 침범하지 않을 수 있는지
```

## 6. 다음 테스트 조건

```text
새로운 Gemini/CLI/worker 반환 하나를 더 수동 회수한다.
그 과정에서 helper가 도울 수 있는 항목과 절대 도우면 안 되는 판단을 표시한다.
그 뒤에야 dry-run helper 후보를 생각한다.
```

`STATUS: SPACE_MEMORY_PIPELINE_PLAIN_MAP_PREPARED`
