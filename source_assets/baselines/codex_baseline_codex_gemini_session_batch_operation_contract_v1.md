[[DOCROLE:baseline]]
[[RUNMODE:ingest_only]]
[[PRIORITY:high]]

# OPERATION CONTRACT — CODEX ↔ GEMINI (SESSION-BATCH MODE → FUTURE INTEGRATION)

## 0. 목적
현재 구조에서 Codex와 Gemini CLI의 역할을 명확히 분리하고,
운영 방식을 **세션 단위 배치 처리 모드**로 고정한다.

또한 향후 운영화면 도입 시
동일 흐름을 **단일 과정 내 포함 구조로 확장 가능하도록 기준을 미리 잠근다.**

## 1. 현재 운영 모드 (LOCK)

### 핵심 구조

Codex = 실행 주체
Gemini = 후단 판독기

### 실행 흐름 (현재 고정)

1. Codex 실행
2. 결과 생성 (runtime 반영)
3. 여러 작업 누적
4. 세션 종료 시 Gemini CLI 호출
5. 요약 / 점검 / 브리핑 수행
6. 결과를 observer 로그로 저장
7. 사용자 판단

### 구조 표현

Codex (N회 실행)
-> runtime 상태 누적
-> [세션 종료]
-> Gemini 1회 실행
-> observer 기록
-> 사용자 판단

## 2. Gemini 실행 타이밍 (고정 규칙)

Gemini는 아래 시점에서만 실행한다.

- 세션 종료 시
- 의미 있는 작업 묶음 완료 시
- 운영 반영 직전
- 이상 징후 발생 시 (선택)

### 금지

- Codex 실행 직후 자동 호출
- 매 실행마다 반복 호출
- 중간 상태에서 호출

## 3. Gemini 역할 정의 (LOCK)

Gemini는 다음 역할만 수행한다.

### 허용

- 변경 요약
- 상태 요약
- diff 리뷰
- pointer / 구조 점검
- 의심 지점 제시

### 금지

- 코드 수정
- 파일 변경
- 상태 확정
- 기준선 결정
- 삭제/병합 판단
- 엔진 구조 변경 제안

### 출력 규칙 (강제)

Gemini는 반드시:

- 수정하지 말 것
- 확정 판단하지 말 것
- 후보 / 의심 형태로 제시할 것
- 근거 파일 경로 포함할 것
- 불확실성 명시할 것

## 4. Gemini 입력 단위 (배치 기준)

Gemini는 단일 실행 결과가 아니라
**작업 묶음(batch)**을 입력으로 받는다.

### 기본 입력 묶음

#### A. 상태 요약

- latest board
- provenance compacted latest
- 최근 receipt 일부

#### B. 구조 점검

- latest board
- per-run board 일부
- pointer 관련 파일

#### C. 변경 리뷰

- git diff
- 변경 파일 목록
- 관련 runtime 결과

## 5. 저장 위치 (LOCK)

Gemini 출력은 반드시 아래에 저장한다.

`runtime/observer/gemini/`

### 저장 단위

- 1 실행 = 1 로그 아님
- 1 세션 = 1 로그 기준

### 예시 구조

```text
runtime/
└── observer/
    └── gemini/
        └── YYYY-MM-DD/
            ├── session_review_001.md
            ├── session_pointer_check_001.md
            └── session_diff_review_001.md
```

## 6. 기록 규칙

- append-only 유지
- overwrite 금지
- latest는 별도 유지 가능
- context 반드시 포함

### context 필수 필드

```md
## context
- session_id:
- related_runs:
- input_scope:
- command:
- timestamp:
```

## 7. 역할 분리 (절대 기준)

### User

- 방향 설정
- 실행 승인
- 최종 판단

### Codex

- 코드 수정
- 실행
- 엔진 상태 생성

### Gemini

- 읽기
- 분석
- 요약
- 점검

## 8. 현재 운영 정의 (한 줄)

“Codex가 여러 번 실행되고,
Gemini는 세션 끝에 한 번 실행된다”

## 9. 향후 확장 (PRE-DEFINED PATH)

운영화면 도입 후 확장 방향:

### 목표 구조

입력 UI
-> Codex 실행
-> Gemini 실행
-> 결과 표시

### 통합 흐름

User Input
-> Codex
-> Gemini
-> UI Rendering

### 중요 조건

Gemini는 통합되더라도:

- read-only 유지
- 수정 권한 없음
- 판단 권한 없음

## 10. 확장 금지 조건 (현재 단계)

아래는 지금 하지 않는다.

- Gemini 자동 실행 파이프라인 구성
- Codex 내부에 Gemini 호출 삽입
- 엔진 흐름에 Gemini 강제 편입

## 11. 성공 기준

- Codex 실행 흐름 유지됨
- Gemini는 세션 단위로만 실행됨
- Gemini 출력이 observer 로그로 남음
- 엔진 데이터와 Gemini 결과가 분리됨

## 12. 최종 정의

Gemini는
엔진을 바꾸는 도구가 아니라
엔진을 읽는 도구다.

따라서 현재는:

“세션 끝에서만 호출되는 후단 판독기”

로 고정한다.
