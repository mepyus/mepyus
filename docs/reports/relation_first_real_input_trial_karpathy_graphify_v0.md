# Relation-first Real Input Trial — Karpathy llm-wiki + Graphify v0

## 1. Status
**STATUS: RELATION_FIRST_REAL_INPUT_TRIAL_KARPATHY_GRAPHIFY_COMPLETE**

## 2. Verdict
**REAL_INPUT_TRIAL_WORKED_WITH_WATCH**

## 3. Executive summary
Karpathy의 `llm-wiki`와 `Graphify`를 실제 소스 번들로 태워본 결과, '관계 우선(Relation-first)' 입력기 체인은 자료를 조각내지 않고도 의미의 압력(Meaning Pressure)을 보존함을 확인했습니다. 다만, 분석 대상이 풍부할수록 필드 작성 과정에서 의식(Ceremony)이 발생할 위험이 있으므로, 향후 운영 시에는 'Standard' 이상의 모드를 사용할 때 신중한 필드 선별이 요구됩니다.

## 4. Pass 1 — Source Bundle Capture
- **source_bundle_name:** AI-Source-Bundle-V001 (Karpathy/Graphify)
- **sources:** Karpathy llm-wiki gist, Graphify GitHub
- **user_intent:** Agent workspace 구조 참조를 위한 관계 흐름 보존
- **why_now:** 공간의 입력을 파편화하지 않고 구조적으로 보존하는 문법 검증 필요
- **input_type:** external repo / reference material
- **selected_mode:** `STANDARD`
- **do_not_infer:** 자동화/실행계획/온톨로지화 금지
- **watch_items:** 외부 도구의 구조가 시스템 설계로 직결되는 압박
- **next_safe_action:** 관찰 및 렌즈 보존

## 5. Pass 2 — Source-level Reading
- **source:** Karpathy llm-wiki
- **source-level reading:** LLM을 이용한 지속적인 지식 관리(Persistent intermediate wiki)와 추론/로그의 분리.
- **core mechanism:** Raw vs Generated layer separation, Index vs Log.
- **source:** Graphify
- **source-level reading:** 증거 기반의 관계 추출과 쿼리 가능한 경로(Query path) 관리.
- **core mechanism:** Evidence relation map, extraction/inference/ambiguous label.

**Synthesis:** 두 자료는 모두 '상태(State)'가 아니라 '흐름(Flow)'과 '증거(Evidence)'를 관리하는 데 집중합니다.

## 6. Pass 3 — Meaning Block Detection

| Meaning Block | Source | Preserves | Why it matters | Label |
| :--- | :--- | :--- | :--- | :--- |
| **Layered Context** | Karpathy | Raw vs Generated | 소스 근거 유지 | EXTRACTED |
| **Evidence Relation** | Graphify | Evidence Map | 맥락적 연결 보존 | INFERRED |
| **Schema-guided** | Karpathy | 규칙 기반 동작 | 구조적 제약 보존 | WATCH |
| **Trace Memory** | Graphify | 이력 추적 | 작업의 재생 가능성 | PROCESS_TRACE |

## 7. Pass 4 — Relation Map

| Relation | Label | Placement | Why it matters | Watch |
| :--- | :--- | :--- | :--- | :--- |
| **Source -> Claim** | EXTRACTED | Candidate | 검증을 위한 원문 고립 방지 | 과도한 인용 |
| **Claim -> Evidence** | PROCESS_TRACE | Process Asset | 추론 과정 보존 | Ledger화 위험 |
| **Claim -> Line Pressure** | INFERRED | Watch | 구조적 성장 확인 | prematurity |
| **Line Pressure -> Axis** | INFERRED | Watch | 공간의 방향성 확인 | ontology화 |

## 8. Pass 5 — Line / Axis Pressure Check
- **Connection Seed:** 존재함 (Trace와 Evidence의 관계 추출).
- **Line Pressure:** 다수의 에이전트 도구들이 'Bounded Execution'을 지향함.
- **Axis Pressure:** 'Role-bundle'과 'Affordance'의 분리가 차기 축 후보로 유망함.
- **Premature Naming:** 현재 단계에서 축 명명은 명백히 이릅니다(AXIS_NAMING_PREMATURE: YES).

## 9. Pass 6 — Selective Segmentation
- **Segment Candidates:** 5-layer compression rule, MCP tool surface map.
- **Reason:** 이들은 우리 공간에서 'Reusable Setting'으로 전환 가능한 정보임.
- **Selective Segment:** 전체 자료를 다 쪼개지 않고, 위 단위만 추출.

## 10. Pass 7 — Input Report Card + Re-entry Signal

### Standard Input Report Card
- **source:** Karpathy/Graphify bundle
- **user intent:** 구조 참조 및 문법 검증
- **source-level reading:** 관계 우선(Relation-first) 흐름 유지
- **meaning blocks:** 층위별 지식 관리 및 관계 추출
- **key relations:** Source-Evidence-Trace-Flow
- **evidence labels:** EXTRACTED, INFERRED, PROCESS_TRACE
- **placement:** Process Asset Candidate
- **line/axis pressure:** Line Candidate (Bounded Execution)
- **watch/hold:** 온톨로지화 주의
- **next safe action:** 상태 보존 및 관찰
- **re-entry signal:** 향후 에이전트 기능 설계 시 참조
- **User Gate:** 통과

## 11. Functional advantages found
*   **Karpathy:** 'Raw/Generated' 분리를 통해 해석이 원본을 덮어쓰는 사고 방지.
*   **Graphify:** 'EXTRACTED/INFERRED/AMBIGUOUS' 라벨링을 통해 추론의 신분 보존.
*   **통합 효과:** 우리 공간의 입력을 파편화하지 않고, '맥락 보존' 중심의 파이프라인으로 전환 가능.

## 12. Structural problem list

| Problem | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ceremony Drift** | MEDIUM | 패킷 작성이 무거워짐 | 템플릿 필드 간소화 | 강제적 양식 적용 |
| **Authority Drift** | HIGH | 워커의 해석이 사실로 오독됨 | 라벨링 준수 | truth 선언 |
| **Context Over-read** | MEDIUM | 전체를 다 읽으려 함 | boundary 지정 | 모든 자료 심층 독해 |

## 13. Recommended next state
**KEEP_AS_EXTERNAL_AI_MATERIAL_PIPELINE_CANDIDATE_WITH_WATCH**

## 14. Watch items
*   pipeline candidate becoming automation.
*   mode selection becoming ceremony.
*   Intake packet becoming mandatory form.
*   Linkage gate becoming ontology.
*   Re-entry support becoming current-position update.
*   Process asset becoming ledger.
*   User gate becoming checkbox.
*   Gemini evidence becoming truth.
*   mini-swe-agent becoming adoption pressure.

## 15. Do not do yet
- NO implementation, automation, or runtime script creation.
- NO registry, index, ledger, router, controller, formal schema.
- NO official workflow declaration.
- NO current-position update or baseline promotion.
- NO tool/API/function attachment.
- NO MCP attachment.
- NO integrated engine implementation from this test alone.
- NO Gemini verified-truth authority.
- NO Codex final authority.

## 16. Final status
**STATUS: RELATION_FIRST_REAL_INPUT_TRIAL_KARPATHY_GRAPHIFY_COMPLETE**
