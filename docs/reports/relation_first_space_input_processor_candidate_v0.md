# Relation-first Space Input Processor Candidate v0

## 1. Status
**STATUS: RELATION_FIRST_SPACE_INPUT_PROCESSOR_CANDIDATE_COMPLETE**

## 2. Sources used
- `docs/reports/space_input_processor_readiness_scan_corrected.md`
- `docs/reports/integrated_engine_component_map_and_part_spec_reading_v0.md`
- `docs/reports/standardized_intake_packet_candidate_spec_v0.md`
- `docs/reports/line_axis_linkage_gate_candidate_spec_v0.md`
- `docs/reports/cross_session_reentry_support_candidate_spec_v0.md`
- `docs/reports/vibe_trading_corrected_structure_reference_packaging_v0.md`

## 3. Executive summary
기존의 '분절 우선(segmentation-first)' 입력 방식은 재료를 파편화하여 맥락적 압력(meaning pressure)을 희석시켰습니다. 새로운 **'관계 우선(relation-first)' 입력기는 재료의 원본 흐름을 먼저 보존**하고, 그 안의 큰 의미 단위(Meaning Block)와 관계(Relation)를 먼저 파악한 뒤, 기존 라인/축/프로세스 자산과 연결할 때만 선택적으로 분절합니다. 이는 자동화된 엔진이 아닌, 우리가 자료를 더 깊게 읽고 연결하기 위한 **운영 문법**입니다.

## 4. Old input problem diagnosis

| Old input behavior | Useful part | Damage / dilution | Why it matters now | Correction direction |
| :--- | :--- | :--- | :--- | :--- |
| **Over-fragmentation** | 빠른 검색 | 흐름 및 맥락 상실 | 큰 구조적 흐름 보존 필요 | 관계 우선 읽기 |
| **Summary before connection** | 빠른 정보 습득 | 기존 라인과의 연결 약화 | 기존 축과의 연결 우선 | 연결 우선 분절 |
| **Translation priority** | 가독성 | 원본의 의도 압력 상실 | 원본의 맥락 보존 | 소스 수준의 독해 |

## 5. Larger input units
- **Source Bundle:** 전체 원본의 흐름이 보존된 단위.
- **Source-level Reading:** 파편이 아닌 원본 전체를 관통하는 흐름 파악.
- **Meaning Block:** 분절 전의 거시적 의미 단위.
- **Relation Cluster:** 연결 씨앗이 뭉쳐있는 맥락적 덩어리.
- **Line / Axis Pressure:** 자료가 기존 공간에 가하는 인지적 압력/연결 요구.

## 6. Relation-first processing flow

| Stage | Role | Input | Output | Preserve | Must not become |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Source Capture** | 원본 보존 | External Material | Source Bundle | 원본 흐름 | 공식 진실 |
| **2. Meaning Detection** | 의미 덩어리 파악 | Source Bundle | Meaning Blocks | 거시적 의도 | Ontology |
| **3. Relation Extraction** | 관계 파악 | Meaning Blocks | Internal Relation Map | 연결 씨앗 | Registry |
| **4. Space Linkage** | 구조 연결 | Relation Map | Linkage Verdict | 기존 축 압력 | 자동화 파이프라인 |
| **5. Selective Segment** | 필요 분절 | Linkage Verdict | Essential Units | 필수 핵심 정보 | 무분별한 파편화 |

## 7. Karpathy / Graphify fit (Corrected)

| Signal | Source-supported structure | Project reading | Keep as |
| :--- | :--- | :--- | :--- |
| **Persistent intermediate wiki** | Karpathy Lens | 프로세스 기억 보조 | Reference |
| **Relation graph/report** | Graphify Lens | 증거 관계 맵 | Reference |
| **Query / Path / Explain** | Graphify Lens | 구조적 검증 도구 | Reference |

## 8. Line / Axis centered input check
- **연결 씨앗:** `Intake Packet`의 목적과 기존 `Line/Axis`를 비교하여 검출.
- **라인 압력:** 반복되는 연결 확인 시 `Line Candidate`로 승격.
- **축 압력:** 여러 라인이 동일 질문을 가리킬 때 `Axis Candidate`로 식별.
- **과잉 명명 방지:** 증거가 충분히 쌓일 때까지 연결 상태(`CONNECTION_SEED`)를 유지.

## 9. Candidate processor shape
- **Purpose:** 자료의 원본 압력을 보존하고 기존 공간의 렌즈로 연결하는 문법.
- **Input unit:** Source Bundle (원본 파일/링크 전체).
- **Processing stages:** Capture -> Block Detection -> Relation Map -> Linkage -> Select Segmentation -> Card.
- **Output artifacts:** Source Note, Relation Map, Input Report Card.
- **Boundary:** 구현/자동화/온톨로지화 절대 금지.

## 10. Minimal artifact set

| Artifact | Required? | Purpose | Compact version | Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Source Bundle** | required | 원본 보존 | 원본 파일/링크 | 파편화 |
| **Meaning Block Note** | required | 큰 흐름 보존 | 요약 한 줄 | 맥락 누락 |
| **Relation Map** | required | 공간 내 위치 확인 | Line/Axis 명시 | 온톨로지화 |
| **Input Report Card** | required | 판단/액션 요약 | 다음 행동만 | ceremony화 |

## 11. Structural problem list

| Problem | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Graph Drift** | HIGH | 그래프가 곧 시스템 구조라고 착각함 | 연결 확인 도구로만 활용 | Ontology 생성 |
| **Wiki Drift** | MEDIUM | 요약이 곧 진실이 됨 | Raw Source 링크 유지 | Source of truth 선언 |
| **Ceremony Drift** | MEDIUM | 처리 단계가 너무 많아짐 | Compact 모드 우선 | 필수 절차 강제 |

## 12. Recommended next state
**READY_TO_DRAFT_SPACE_INPUT_PROCESSOR_CANDIDATE_WITH_WATCH**

## 13. Watch items
*   소프트웨어적 도구(Graphify/Karpathy)가 곧바로 우리 공간의 아키텍처가 되는 압박.
*   연결 확인(Linkage)이 자동화된 라우터로 변질되는 것.
*   후보 신호들이 너무 빨리 시스템의 '법'으로 승격되는 것.
*   User 게이트가 실질적인 판단 없이 '통과 의식'으로 전락하는 것.

## 14. Do not do yet
- NO implementation.
- NO automation.
- NO runtime script.
- NO registry, index, ledger.
- NO formal schema.
- NO official workflow.
- NO current-position update.
- NO baseline promotion.
- NO Graphify integration.
- NO LLM-Wiki implementation.
- NO graph database.
- NO wiki system.
- NO tool/API/function attachment.
- NO ontology creation.
- NO source truth transfer to generated wiki.
- NO graph-as-authority.
- NO input processor runtime.
- NO integrated engine implementation.
- NO Gemini verified-truth authority.
- NO Codex final authority.

## 15. Final status
**STATUS: RELATION_FIRST_SPACE_INPUT_PROCESSOR_CANDIDATE_COMPLETE**
