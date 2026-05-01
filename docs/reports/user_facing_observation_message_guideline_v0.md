# User-facing Observation Message Guideline v0
# Topic: Lightweight Maturation Vocabulary & Ambient Status Displays

## 0. Declaration
- **Mode:** Guideline synthesis only.
- **Scope:** Read-only / No source-space modification.
- **Status:** Strategic reference material only; no implementation or internal design.
- **Authority:** All wording rules remain provisional strategic reference material.
- **Date:** 2026-04-26

## 1. Why This Guideline Exists
Round 009 and 010 established that "Status" is an observer signal, not an ontology. To prevent the "Dark Room" effect and reduce review fatigue, we need a standard, low-friction vocabulary that signals maturity and risk to the human observer *without* creating a heavy schema. This guideline serves as a "Voice and Tone" manual for all system-to-human interaction.

## 2. User-facing Status Vocabulary

| Internal Status | User-facing Label | Meaning |
| :--- | :--- | :--- |
| **OK** | 완료 | 실행 성공 (Truth/Lock/Baseline 아님) |
| **RUNNING** | 진행 중 | 현재 워커 작업 중 |
| **FAILED** | 실패 | 작업 수행 중 예외 발생 |
| **BLOCKED** | 막힘 | 실행을 진행할 수 없는 상태 |
| **VALIDATION_REQUIRED** | 검증 필요 | 논리적 무결성 확인 요망 |
| **HUMAN_REVIEW_REQUIRED**| 사용자 판단 필요 | 인간 승인(Lock) 권한 필요 |
| **HOLD** | 보류 | 안전을 위해 일시 정지 |

*Forbidden:* `승인됨`, `확정됨`, `기준 반영됨`, `자동 반영됨`, `정답`, `완전히 검증됨`, `lock 완료`, `canonical`, `promoted`, `흡수`

## 3. Basic Message Form
[상태] 요약
주의: ...
다음: ...
근거: ...

- **Low Risk:** Status + Summary + Next Action (1~2 lines).
- **High Risk/Review:** Status + Summary + Risk + Next Action + Provenance (3~4 lines).

## 4. Display Rules by Risk Level
- **Low Risk:** Keep messages brief; omit "주의" and "근거" unless requested.
- **Validation Required:** Highlight the logic check (e.g., `logic_changed=false`).
- **Human Review Required:** Emphasize sovereignty (e.g., "AI proposing baseline promotion").

## 5. Standard Messages by Case

### Case 1. Read-only report
[완료] 읽기 전용 리포트 생성
다음: 없음
근거: 리포트 보기

### Case 2. Small code/text change
[검증 필요] 버튼 문구 수정
주의: 로직 영향 확인 필요
다음: 검증
근거: 변경 내용 보기

### Case 3. Refactor
[검증 필요] 구조 정리 완료
주의: 동작 변경 없음을 확인 요망
다음: 검증
근거: 변경 내용 보기

### Case 4. Baseline proposal
[사용자 판단 필요] 공간 baseline 변경 제안
주의: 자동 반영 금지
다음: 보류
근거: 제안 보기

### Case 5. File deletion
[사용자 판단 필요] 파일 삭제 제안
주의: 삭제 대신 보관/접기 검토
다음: 보류
근거: 삭제 대상 목록 보기

### Case 6. External research
[검증 필요] 외부 자료 조사 결과
주의: 바로 쓰지 말고 공간 적합성 먼저 검토
다음: 공간에 넣어보기
근거: 리포트 보기

## 6. Forbidden Words & Safe Reframes
- **Forbidden:** `승인됨`, `확정됨`, `기준 반영됨`, `자동 반영됨`
- **Safe:** `완료`, `검증 필요`, `사용자 판단 필요`, `보류`, `후보`, `제안`, `근거 확인 필요`, `공간에 넣어보기`, `보관 검토`

## 7. Remaining Ambiguities
- **Report Packet Status:** Should we handle simple read-only reports with a separate `Report Packet` or consolidate into `Research`?
- **Evidence Access:** How do we make evidence links accessible in CLI without UI?
- **Fatigue:** Is the number of `VALIDATION_REQUIRED` cases per session sustainable?
- **Session Aggregation:** When do we compress 10+ packets into one?

## 8. What This Guideline Is Not
- Not UI design.
- Not an automation design.
- Not a JSON schema.
- Not an approval mechanism.

## 9. Closeout
This guideline is wording-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, UI, reingestion design, JSON schema, CLI trace contract, aggregation threshold, or agent architecture was created.
All wording rules remain provisional strategic reference material.
