# Observation Surface Dry-run 001 Correction Note v0

## 0. Declaration
- **Mode:** Gemini-only / Read-only correction.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** Correction note for internal Dry-run evaluation.
- **Authority:** All corrections remain provisional operating guidance.
- **Date:** 2026-04-26

## 1. Why This Correction Exists
Dry-run 001 confirmed the logic of the Observation Surface but revealed "Status" and "Packet" labeling inconsistencies that threaten the project's strict sovereignty principles (e.g., auto-promotion risks, schema bloat). This note establishes the corrected triage rules before Gemini runs Dry-run 002.

## 2. Overall Verdict
PASS_WITH_NOTE

## 3. What Worked
- **Validation vs. Review Separation:** `validation_required` (for logic) and `human_review_required` (for baseline/sovereignty) correctly segregated the triage flow.
- **Minimal Surface:** The field set effectively triages without requiring complex UI/dashboards.

## 4. Corrections by Case

### Case 1 (Read-only report)
- **original:** OK
- **issue:** "즉시 공간에 반영 가능"은 반영(Baseline 승격)으로 오해할 소지가 있음.
- **corrected:** Status: OK (Execution Successful); Note: Execution success does not imply baseline/lock promotion.
- **reason:** Protecting Sovereign Authority.

### Case 2-A (Small text/code change)
- **original:** Refactor Packet
- **issue:** 코드 로직 변경/수정은 Refactor가 아님.
- **corrected:** Packet Type: Implementation Packet / Status: VALIDATION_REQUIRED
- **reason:** 문구/코드 로직 변경은 구현층 활동임.

### Case 2-B (Refactor)
- **original:** -
- **issue:** 리팩터링과 구현이 섞임.
- **corrected:** Packet Type: Refactor Packet / Status: VALIDATION_REQUIRED / Logic: logic_changed=false 확인 필수.
- **reason:** 리팩터링은 동작 불변성을 전제로 해야 함.

### Case 3 (Baseline proposal)
- **original:** Space Intake Packet
- **issue:** 근간을 건드리는 제안은 검증이 최우선.
- **corrected:** Packet Type: Validation Packet / Status: HUMAN_REVIEW_REQUIRED / Next: hold
- **reason:** 아키텍처 변경은 승인 전까지 HOLD 필수.

### Case 4 (File deletion)
- **original:** Refactor Packet
- **issue:** 삭제는 리팩터링이 아님. 손상 위험.
- **corrected:** Packet Type: Validation Packet / Status: HUMAN_REVIEW_REQUIRED / Next: quarantine
- **reason:** 삭제는 증거 유실 위험이 있으므로 즉시 Refactor 처리 불가.

### Case 5 (Research)
- **original:** PENDING
- **issue:** vocabulary에 PENDING 없음.
- **corrected:** Status: VALIDATION_REQUIRED
- **reason:** 정해진 어휘(OK/RUNNING/FAILED/BLOCKED/VALIDATION_REQUIRED/HUMAN_REVIEW_REQUIRED/HOLD)만 사용.

## 5. Corrected Dry-run Table

| Case | Corrected Status | Corrected Packet | Validation Required | Human Review Required | Next Packet | Key Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Case 1** | OK | Report Packet | No | No | none | Success != Lock |
| **Case 2-A** | VALIDATION_REQ | Implementation | Yes | No | validation | Logic check |
| **Case 2-B** | VALIDATION_REQ | Refactor | Yes | No | validation | Logic_changed=false |
| **Case 3** | HUMAN_REVIEW | Validation | Yes | Yes | hold | Lock needed |
| **Case 4** | HUMAN_REVIEW | Validation | Yes | Yes | quarantine | Risk of provenance loss |
| **Case 5** | VALIDATION_REQ | Research | Yes | No | space_intake | Asset triage needed |

## 6. Updated Guardrails
1. **OK != Lock:** 실행 성공이 곧 공간의 baseline 승격이나 truth가 아님.
2. **Vocabulary Strictness:** 임의의 상태어(PENDING 등) 사용 금지.
3. **Delete != Refactor:** 삭제는 잠재적 데이터 손실이므로 Validation/Human Review 단계로 강제함.
4. **Research Path:** 연구(Research Packet)에서 구현(Implementation Packet)으로 직접 전이 금지.

## 7. Remaining Open Questions
- 필드 정렬: 패킷 내 `layer_alignment`를 수동으로 채우는 것 외에 자동 판독 기준은 무엇인가?
- 상태어: `HOLD`와 `HUMAN_REVIEW_REQUIRED`의 경계가 모호할 때가 있음.

## 8. Closeout
This correction note is read-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, verification UI, bridge logic, drill-down design, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, JSON schema, CLI trace contract, aggregation threshold, or agent architecture was created.
All corrections remain provisional operating guidance.
