# Watch / Hold / Residue / Process Asset Placement Clarifier v0

## 1. Status
**STATUS: WATCH_HOLD_RESIDUE_PROCESS_ASSET_PLACEMENT_CLARIFIER_COMPLETE**

## 2. Executive summary
증거의 신분(Provenance)을 분류한 후, 그 신호를 **어디에 배치(Placement)할지** 결정하는 것은 공간이 시스템 레지스트리로 변질되는 것을 막는 마지막 안전장치입니다. 이 배치 문법은 신호를 `Watch`, `Hold`, `Residue`, `Process Asset`, `Candidate`라는 5개의 인지적 바구니로 나누어, 시스템 구현 없이도 우리가 무엇을 중요하게 여기고 무엇을 보류할지 명확히 관리하게 합니다.

## 3. Final placement definitions

| Placement | Meaning | Use when | Must not mean | Main risk |
| :--- | :--- | :--- | :--- | :--- |
| **Watch** | 관찰 대상 | 신호/위험이 흥미로울 때 | 확정된 사실 | 관찰이 곧 조치로 오인 |
| **Hold** | 의도적 보류 | 증거 부족/권한 확인 필요 시 | 거부 | 결정 회피 수단화 |
| **Residue** | 파편 흔적 | 나중에 필요할지 모르는 조각 | 활성 상태 | 아카이브 쓰레기화 |
| **Process Asset** | 재사용 패턴 | 운영 학습이 반복될 때 | 시스템 규율(Law) | 레지스트리/원장화 |
| **Candidate** | 미래의 부품 후보 | 구조적 단위로 발전 가능 시 | 공식 상태 | 미완성본의 성급한 승격 |

## 4. Evidence label to placement mapping

| Evidence label | Safe default placement | Possible upgrade | Upgrade condition | Must not become |
| :--- | :--- | :--- | :--- | :--- |
| **EXTRACTED** | Candidate | Process Asset | 반복 입증 | 사실의 증명 |
| **INTERPRETED** | Local Note | Process Asset | 운영 학습화 | 진실(Truth) |
| **INFERRED** | Watch | Line Candidate | 연결 반복 | 확정 라인 |
| **AMBIGUOUS** | Hold | Watch | 신호 명확화 | 판단 보류 회피 |
| **USER_JUDGED** | Process Asset | Baseline(금지) | 사용자 명시적 승인 | 권한 오남용 |
| **PROCESS_TRACE** | Residue | Process Asset | 운영 레슨으로 반복 시 | 작업 로그의 Truth화 |

## 5. Relation-first Input Output Placement
- **Source Bundle:** `Candidate` (입력 관리)
- **Meaning Block:** `Local Note` -> `Candidate`
- **Relation Map:** `Watch` (초기 연결성 검증 단계)
- **Line/Axis Pressure:** `Watch` (축으로 가기 전의 긴장 상태)
- **Input Report Card:** `User_Judged` (최종 요약본)

## 6. Minimal rule set
1. 모든 신호는 배치(Placement) 단계에서 '승격(Promotion)'되지 않습니다.
2. `AMBIGUOUS`한 연결은 무조건 `Watch`나 `Hold`로 보내 섣부른 판단을 막습니다.
3. `Process Asset`은 오직 반복되는 운영 학습을 통해서만 형성됩니다.
4. 모든 배치는 `User Gate`를 통해 인간의 판단을 거쳐야 합니다.
5. 공간의 모든 위치는 '상태'가 아니라 '인지적 위치'일 뿐입니다.

## 7. Integration points
- **Input Processor:** 입력 수용 시 신분(Label)과 위치(Placement)를 함께 결정.
- **Linkage Gate:** 연결 검증 결과에 따라 `Watch`에서 `Connection Seed`로 이동.
- **Re-entry Support:** 마지막 세션의 `Watch/Hold` 신호를 다음 세션의 `Primary Anchor`로 보존.

## 8. Structural problem list

| Problem | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Registry Drift** | HIGH | 배치를 곧 인덱스로 오해함 | '후보' 상태로 엄격 분류 | 시스템 레지스트리 생성 |
| **Ceremony Drift** | MEDIUM | 배치를 위한 의사결정이 너무 무거움 | compact 모드 활용 | 모든 신호에 배치 카드 작성 |
| **Authority Drift** | HIGH | 워커의 배치를 최종 결정으로 오해함 | User Gate 강화 | Gemini 권한 승격 |

## 9. Recommended next state
**KEEP_AS_PLACEMENT_GRAMMAR_CANDIDATE**

*Reasoning:* 이번 보정으로 '신분'과 '배치' 문법이 정립되었습니다. 추가 구현은 없습니다. 외부 자극이 올 때까지 이 문법을 유지합니다.

## 10. Watch items
*   배치(Placement)가 곧 시스템 레지스트리/원장이 되는 것.
*   'Residue'가 나중에 버릴 수 없는 아카이브가 되어 쌓이는 것.
*   'Watch' 항목이 시스템의 자동 라우터(블로커)가 되는 것.
*   Gemini가 판단한 배치가 사용자의 결정 없이 고정되는 것.

## 11. Do not do yet
- NO implementation, automation, or runtime script.
- NO registry, index, ledger, router, controller.
- NO formal schema or official workflow.
- NO current-position update or baseline promotion.
- NO Graphify integration or LLM-Wiki implementation.
- NO tool/API/function attachment.
- NO ontology creation.
- NO forced pipeline creation.
- NO integrated engine implementation.
- NO Gemini verified-truth authority.

## 12. Final status
**STATUS: WATCH_HOLD_RESIDUE_PROCESS_ASSET_PLACEMENT_CLARIFIER_COMPLETE**
