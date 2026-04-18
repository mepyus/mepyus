[[DOCROLE:baseline]]
[[RUNMODE:ingest_only]]
[[PRIORITY:high]]

[[A]] [[OBJ:baseline_document]] [[SEM:session_id_and_gemini_log_link_contract]] [[ROLE:baseline]]

# CODEX BASELINE — SESSION ID RULE + GEMINI OBSERVER LOG LINK CONTRACT V1

## 0. 목적
이 기준문의 목적은 현재 잠겨 있는 Codex ↔ Gemini 세션 배치 운영 계약 위에
아래 두 가지를 추가로 고정하는 것이다.

1. session_id 규칙
2. Gemini observer 로그와 Codex 실행 결과를 연결하는 방식

이 기준문은 실행 지시가 아니라
**운영 흐름을 안정적으로 추적하기 위한 기준선 자산**이다.

---

## 1. 현재 전제
이미 잠겨 있는 기준은 다음과 같다.

- Codex = 앞단 실행 주체
- Gemini = 세션 종료 시 한 번 호출되는 후단 판독기
- Gemini 출력 저장 위치 = `runtime/observer/gemini/`
- Gemini 출력은 엔진 데이터가 아니라 observer 로그다
- Gemini는 매 실행마다 호출하지 않고 세션 단위 batch로 호출한다

이 문서는 위 구조를 유지한 채,
**세션이라는 묶음 단위를 명확히 식별하고 연결하는 기준**을 추가한다.

---

## 2. session_id의 필요성
session_id는 단순 이름표가 아니다.

session_id는 아래를 가능하게 한다.

- 여러 Codex 실행을 하나의 작업 세션으로 묶기
- 세션 종료 후 Gemini 판독 결과를 같은 묶음에 연결하기
- 나중에 운영화면에서 “이 세션에서 무슨 일이 있었는지” 보기
- latest / per-run / observer 로그를 사람 기준 흐름으로 재구성하기

한 줄 요약:
**run_id는 개별 실행의 식별자이고, session_id는 작업 흐름 묶음의 식별자다.**

---

## 3. 식별자 역할 분리
아래 역할 분리를 절대 기준으로 고정한다.

### run_id
- 개별 실행 단위 식별자
- routing 실행 / Codex 실행 / receipt / per-run artifact와 연결됨
- 이미 존재하는 실행 추적 단위

### session_id
- 여러 run_id를 묶는 상위 작업 세션 식별자
- Gemini batch review 단위
- 사용자가 “이번 작업 흐름”으로 인식하는 단위

즉:

- run_id = 점
- session_id = 점들을 묶는 선/묶음

---

## 4. session_id 규칙 (LOCK)

### 4.1 기본 형식
session_id는 아래 형식으로 생성한다.

`session_YYYYMMDD_NN`

예시:
- `session_20260325_01`
- `session_20260325_02`
- `session_20260326_01`

### 4.2 생성 원칙
- 날짜 기준으로 관리한다
- 같은 날 여러 세션이 있으면 2자리 순번을 붙인다
- 사람이 읽고 바로 이해 가능해야 한다
- 지나치게 긴 uuid형 session_id는 기본값으로 쓰지 않는다

### 4.3 의미
- session_id 하나는 “작업 묶음 하나”를 의미한다
- 너무 넓게 잡지 않는다
- 하루 전체를 무조건 한 세션으로 보지 않는다
- 의미 있는 작업 묶음 단위로 자른다

권장 예:
- 기능 하나 끝날 때
- 안정화 작업 하나 끝날 때
- 운영 화면 작업 한 덩어리 끝날 때

비권장 예:
- 며칠치 작업을 하나의 session_id로 묶기
- 너무 자잘하게 1실행마다 새 session_id 만들기

---

## 5. session_id 적용 범위
session_id는 아래에 연결될 수 있어야 한다.

### 직접 포함 대상
- Gemini observer 로그
- session summary 문서
- session review 문서
- 필요시 Codex handoff 문서

### 참조 포함 대상
- 관련 run_id 목록
- latest board / per-run board 참조
- receipt 참조
- provenance compacted latest 참조

중요:
**session_id는 개별 엔진 이벤트를 대체하지 않는다.**
기존 run_id / receipt / board 구조 위에 얹히는 상위 묶음이다.

---

## 6. Gemini 로그 저장 구조 (LOCK)

### 6.1 기본 저장 위치
Gemini 출력은 반드시 아래에 저장한다.

`runtime/observer/gemini/`

### 6.2 권장 폴더 구조
권장 구조는 아래와 같다.

`runtime/observer/gemini/YYYY-MM-DD/`

예시:
- `runtime/observer/gemini/2026-03-25/`
- `runtime/observer/gemini/2026-03-26/`

### 6.3 권장 파일
세션 단위 저장 기본 파일 예시는 아래와 같다.

- `session_review_001.md`
- `session_pointer_check_001.md`
- `session_diff_review_001.md`
- `session_summary_001.md`

또는 session_id 중심 네이밍도 허용한다.

예시:
- `session_20260325_01_review.md`
- `session_20260325_01_pointer_check.md`
- `session_20260325_01_summary.md`

권장 방향:
**session_id 중심 네이밍을 우선 추천한다.**

---

## 7. Gemini 로그 필수 context 구조 (LOCK)
모든 Gemini observer 로그는 아래 context를 반드시 포함한다.

```md
## context
- session_id:
- related_runs:
- related_receipts:
- related_boards:
- input_scope:
- command:
- timestamp:
```

### 필드 의미

- `session_id`: 이 로그가 속한 작업 세션
- `related_runs`: 이 세션에서 참고한 run_id 목록
- `related_receipts`: 참조한 receipt 경로 또는 목록
- `related_boards`: 참조한 latest/per-run board 경로
- `input_scope`: 무엇을 읽고 판독했는지 요약
- `command`: Gemini에 준 실제 지시 또는 명령 형태
- `timestamp`: observer 로그 생성 시각

중요:
**Gemini 로그는 반드시 “무엇을 보고 이런 말을 했는지”가 남아야 한다.**

---

## 8. Codex ↔ Gemini 연결 방식 (LOCK)

### 8.1 현재 연결 원칙

현재 구조에서 Codex와 Gemini는 자동 연결되지 않는다.

현재 연결 방식은 아래로 고정한다.

1. Codex가 여러 run을 실행한다
2. 결과가 runtime에 누적된다
3. 사용자가 session_id를 기준으로 작업 묶음을 정한다
4. 세션 종료 시 Gemini를 호출한다
5. Gemini는 해당 session_id 기준으로 batch review를 수행한다
6. 결과는 `runtime/observer/gemini/`에 observer 로그로 남긴다

### 8.2 연결의 핵심

- Codex는 현실을 만든다
- Gemini는 그 현실을 나중에 읽는다
- session_id는 그 둘을 사람 기준의 흐름으로 묶는다

---

## 9. session 단위 입력 묶음 규칙

Gemini는 session_id를 기준으로 아래 유형의 입력 묶음을 받을 수 있다.

### A. 상태 요약 세션

입력 예:

- latest board
- provenance compacted latest
- 최근 receipt 일부
- 관련 per-run board 일부

출력:

- session review
- session summary

### B. 구조 점검 세션

입력 예:

- latest board
- latest commands
- 관련 per-run board / commands
- pointer 관련 파일

출력:

- session pointer check

### C. 변경 리뷰 세션

입력 예:

- git diff
- changed files
- 관련 receipt / board
- 필요시 관련 정책/계약 문서

출력:

- session diff review

즉 session_id는 하나지만,
그 안의 Gemini 로그는 목적별로 나눌 수 있다.

---

## 10. latest와 session의 관계

latest는 현재 대표 상태를 가리킨다.
session은 작업 흐름 묶음을 가리킨다.

둘의 관계는 아래와 같다.

- latest = 가장 최근 상태 포인터
- per-run = 실제 실행 근거
- session = 여러 run과 관찰 로그를 묶는 사람 기준 작업 단위

중요:
**session은 latest를 대체하지 않고, latest를 사람 흐름으로 해석하는 보조 묶음이다.**

---

## 11. append-only 규칙

Gemini observer 로그에도 append-only 감각을 유지한다.

### 규칙

- 기존 session 로그 overwrite 금지
- 수정이 필요하면 새 로그를 추가하거나 revision을 남긴다
- latest 성격의 파일이 필요하면 별도 유지 가능하나 원본 로그는 남긴다

예:

- `session_20260325_01_review.md`
- `session_20260325_01_review_v2.md`

권장:

- 최초 로그는 유지
- 추가 판독은 v2, v3 식으로 남긴다

---

## 12. 하지 말아야 할 것

아래는 금지한다.

### 금지 1

session_id를 engine core state처럼 사용하지 말 것

### 금지 2

Gemini observer 로그를 provenance / registry / event로 혼입하지 말 것

### 금지 3

run_id를 없애고 session_id만 남기는 식으로 단순화하지 말 것

### 금지 4

1실행마다 무조건 새 session_id를 발급하지 말 것

### 금지 5

며칠치 전혀 다른 작업을 하나의 session_id로 뭉개지 말 것

---

## 13. 향후 확장 경로 (PRE-DEFINED)

운영화면이 생기면 아래 확장이 가능하다.

### 현재

- 사용자가 Codex 실행
- 세션 종료 시 Gemini 호출
- observer 로그 저장

### 추후

- 입력 페이지에서 session 시작
- Codex 실행 결과가 session에 자동 연결
- Gemini batch review가 같은 session에 연결
- 운영화면에서 session 단위로 확인

즉 향후에는 아래 구조로 확장 가능하다.

`UI Session -> Codex Runs -> Gemini Review -> Session View`

하지만 현재는 아직 자동 편입이 아니라
**수동 session batch 운영 모드**를 유지한다.

---

## 14. 성공 기준

이 기준문이 올바르게 학습되면 아래가 가능해야 한다.

- Codex와 Gemini 모두 run_id와 session_id를 구분해서 이해한다
- Gemini 로그는 반드시 `runtime/observer/gemini/`로 간다
- Gemini는 session 종료 시 batch review만 수행한다
- observer 로그에는 session_id와 related_runs가 남는다
- 나중에 운영화면으로 확장해도 구조가 안 깨진다

---

## 15. 최종 잠금

현재 구조에서 가장 중요한 문장은 아래다.

**Codex는 run을 만든다.
Gemini는 session을 읽는다.**

그리고 저장 규칙은 아래다.

**Gemini observer 로그는 `runtime/observer/gemini/`에 남고,
각 로그는 반드시 session_id와 related_runs를 포함한다.**

최종 한 줄:
**현재 운영 기준은 run 중심 실행 + session 중심 판독이며, 그 연결 축은 session_id다.**
