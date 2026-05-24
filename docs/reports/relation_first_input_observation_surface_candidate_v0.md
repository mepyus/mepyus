# Relation-first Input Observation Surface Check v0

## 1. Status
**STATUS: RELATION_FIRST_INPUT_OBSERVATION_SURFACE_COMPLETE**

## 2. Sources used
- `docs/reports/relation_first_space_input_processor_candidate_closeout_v0.md`
- `docs/reports/relation_first_space_input_processor_candidate_v0.md`
- `docs/reports/evidence_provenance_classification_candidate_v0.md`
- `docs/reports/minimum_agent_function_unit_candidate_closeout_v0.md`
- `docs/reports/line_axis_linkage_gate_candidate_spec_v0.md`
- `docs/reports/standardized_intake_packet_candidate_spec_v0.md`
- `docs/reports/cross_session_reentry_support_candidate_spec_v0.md`

## 3. Executive summary
관계 우선(relation-first) 입력기를 도입함에 따라, 사용자는 복잡한 보고서를 일일이 읽지 않고도 **현재 입력된 재료가 어떤 신분(Provenance)이며, 공간의 어디에 배치(Placement)되었는지**를 직관적으로 확인할 수 있어야 합니다. 본 점검에서는 이를 위해 **'입력 보고 카드(Input Report Card)'**라는 최소 단위의 가시화 면을 설계했습니다. 이는 대시보드나 UI 구현이 아니라, 워커가 산출물에 반드시 포함해야 할 **'운영 확인용 표지'**입니다.

## 4. Pass 1 — Minimum Visibility Check

| Field | Always visible? | Compact version | Expand only? | Why |
| :--- | :--- | :--- | :--- | :--- |
| **Source Identity** | Yes | Name only | - | 입력을 구별하기 위함 |
| **User Intent** | Yes | Short Intent | - | 행동의 목적 확인 |
| **Evidence Label** | Yes | Label name | - | 근거 신뢰성 확인 |
| **Placement** | Yes | Label name | - | 현재 상태(Watch/Hold 등) |
| **Linkage Status** | Conditional | - | Yes | 기존 라인/축 연결 여부 |
| **Next Safe Action** | Yes | Action name | - | 안전한 다음 발걸음 |

## 5. Pass 2 — Input Report Card Shape

### Input Report Card (Standard/Heavy)
```markdown
# Input Report Card
- source: 
- user intent: 
- source-level reading: 
- meaning blocks: 
- key relations: 
- evidence labels: 
- placement: 
- line/axis pressure: 
- watch/hold: 
- next safe action: 
- re-entry signal: 
- User Gate: 
```

### Mini Input Card (Compact)
```markdown
# Mini Input Card
- item: 
- relation: 
- label: 
- placement: 
- next safe action: 
```

## 6. Pass 3 — Relation Map Visibility Check

| Relation item | Display as | Label needed? | Placement needed? | Must not become |
| :--- | :--- | :--- | :--- | :--- |
| **Source -> Claim** | Relation list | EXTRACTED | - | Confirmed Fact |
| **Claim -> Evidence** | Trace | PROCESS_TRACE | - | Truth Source |
| **Relation -> Line** | Line Pressure | INFERRED | Yes | Confirmed Line |
| **Line -> Axis** | Axis Pressure | INFERRED | Yes | Official Axis |

## 7. Pass 4 — User Gate Visibility Check

| Situation | User decide? | Decision options | Do not ask |
| :--- | :--- | :--- | :--- |
| **New Candidate** | Yes | Accept/Watch/Hold/Discard | 자동 도입 |
| **Contamination** | Yes | Correct/Discard/Hold | 자동 수정 |
| **Line/Axis Pressure** | Yes | Confirm Line/Hold | 자동 승격 |

## 8. Pass 5 — Observation Surface Risk Check

| Risk | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- |
| **Dashboard Pressure** | HIGH | 가시화면이 UI처럼 관리됨 | Input Report Card로 제한 | UI Dashboard 구축 |
| **Ceremony Drift** | MEDIUM | 카드 작성이 본질이 됨 | Compact 모드 우선 | 필수 양식화 |
| **Context Over-read** | HIGH | 가시화면 때문에 전체를 다 읽음 | 요약 위주 전시 | 원본 전체 스캔 |

## 9. Structural problem list

| Problem | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Visualization Drift** | HIGH | 카드 표지판이 곧 대시보드임 | 텍스트 기반 카드 유지 | UI 컴포넌트 개발 |
| **Ceremony Drift** | MEDIUM | 모든 작업에 카드를 붙임 | 트리거 발생 시에만 사용 | 매 작업마다 강제 |
| **Authority Drift** | HIGH | 라벨이 진실처럼 보임 | 'Worker Evidence' 명시 | 팩트 확인 도구화 |

## 10. Recommended next state
**KEEP_AS_OBSERVATION_SURFACE_CANDIDATE**

이 가시화 면은 지금 당장 UI로 구현하는 것이 아니라, 다음에 새로운 외부 자료가 들어올 때 워커가 결과물 맨 위에 붙이는 **'표지판 문법'**으로 보존합니다.

## 11. Watch items
*   가시화 면이 대시보드나 UI 컴포넌트로 관리되기 시작하는 것.
*   입력 보고 카드가 모든 작업의 필수 관문(의식)이 되는 것.
*   관계 지도가 온톨로지(Ontology)로 오독되는 것.

## 12. Do not do yet
- NO implementation, UI, or dashboarding.
- NO automation or runtime script.
- NO registry, index, ledger, router, controller.
- NO formal schema.
- NO official workflow.
- NO current-position update.
- NO Graphify integration.
- NO LLM-Wiki implementation.
- NO tool/API/function attachment.
- NO ontology creation.
- NO integrated engine implementation.
- NO Gemini verified-truth authority.

## 13. Final Status
**STATUS: RELATION_FIRST_INPUT_OBSERVATION_SURFACE_COMPLETE**
