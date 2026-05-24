# Recovery Helper Observation Sheet 2026-05-11 Candidate v0

## 1. Status

```text
Document = observation sheet
Status = CANDIDATE_OBSERVATION_AID
Authority = evidence collection support only
Not implementation
Not automation
Not workflow
Not baseline
Not current-position update
```

## 2. 목적

```text
다음 수동 회수에서 helper가 도울 수 있는 반복 구조와,
helper가 절대 판단하면 안 되는 영역을 분리해 기록한다.
```

## 3. 관찰 대상

```text
one new worker return
one Gemini report
one CLI/runtime result
one user-pasted external tool return
```

## 4. Helper가 도울 수 있었는지 볼 항목

| Field | Helper-safe? | Why |
|---|---:|---|
| missing source refs | yes | 빈 칸이나 경로 누락은 구조 체크 |
| missing packet/run refs | yes | 연결 후보를 보여주는 수준 |
| missing not-inspected scope | yes | 안 읽은 범위를 쓰라는 알림 |
| authority words present | yes | "official", "baseline", "completed" 같은 단어 감지 |
| missing watch section | yes | 섹션 존재 여부 확인 |
| draft filenames | yes | 사람이 승인할 후보 이름 제안 |
| recovered judgment wording | no | 의미 판단 |
| WATCH/HOLD/RETURN placement | no | 회수 판단 |
| source material selection | no | 렌즈 선택 |
| current-position update | no | 명시적 앵커 판단 |
| baseline promotion | no | 사용자/공간 권위 판단 |

## 5. 회수 후 적을 칸

```text
return source:
related packet/run:
what was readable:
what was missing:
what was overclaimed:
manual recovered judgment:
manual placement:
helper-safe checks observed:
human-only judgments observed:
new failure mode:
script maturity implication:
```

## 6. Script Maturity 판정 칸

```text
Does this confirm the same repeated manual shape?
Yes / No / Partial

Did helper-safe work remain only checklist/stub work?
Yes / No / Partial

Did any new human-only judgment appear?
Yes / No / Partial

Does this support Level 3 dry-run later?
No by default.
Only candidate if repeated shape is confirmed and user explicitly wants it.
```

## 7. 금지

```text
이 시트를 채웠다고 helper 구현으로 넘어가지 않는다.
이 시트는 helper의 요구사항 문서가 아니다.
이 시트는 사람 판단을 줄이기 위한 것이 아니라,
사람 판단이 어디에 남아야 하는지 보이게 하는 것이다.
```

`STATUS: RECOVERY_HELPER_OBSERVATION_SHEET_PREPARED`
