# Evidence / Provenance Classification Candidate v0

## 1. Status
**STATUS: EVIDENCE_PROVENANCE_CLASSIFICATION_CANDIDATE_COMPLETE**

## 2. Sources used
- `docs/reports/relation_first_space_input_processor_candidate_closeout_v0.md`
- `docs/reports/relation_first_space_input_processor_candidate_v0.md`
- `docs/reports/space_input_processor_readiness_scan_v0.md`
- `docs/reports/external_ai_material_internalization_pipeline_readiness_check_v0.md`
- `docs/reports/minimum_agent_function_unit_candidate_closeout_v0.md`
- `docs/reports/line_axis_linkage_gate_candidate_spec_v0.md`

## 3. Executive summary
우리가 도입한 '관계 우선(relation-first)' 입력기는 기존보다 훨씬 더 풍부한 해석적 신호를 생성합니다. 이 신호들이 시스템의 '진실(Truth)'로 오독되지 않게 하려면, **각 신호가 어떤 근거(Provenance)를 가지고 있는지 표시하는 가벼운 문법**이 필수적입니다. 이 분류 체계는 자동화된 진실 판별기가 아니라, 워커와 사용자가 작업의 맥락을 읽을 때 켜는 **'신분 확인 안경'**입니다.

## 4. Pass 1 — Label Definition Check

| Label | Meaning | Use when | Must not mean | Main risk |
| :--- | :--- | :--- | :--- | :--- |
| **EXTRACTED** | 원문 그대로의 증거 | 자료 직접 인용 시 | 해석된 결론 | 증거의 과신 |
| **INTERPRETED** | 워커의 독해 | 원문 의미 요약 시 | 확정적 사실 | 워커 해석의 진실화 |
| **INFERRED** | 유추된 연결/압력 | 원문에서 맥락적 추론 시 | 검증된 관계 | 추론의 사실화 |
| **AMBIGUOUS** | 불명확/상충 | 증거 부족/해석 충돌 시 | 오류/실패 | 판단 보류 |
| **USER_JUDGED** | 사용자 승인/수정 | 사용자가 판단을 확정 시 | 원본 개찬 | 사용자 판단의 고착화 |
| **PROCESS_TRACE** | 과정의 흔적 | 작업 이력 기록 시 | 원본에 대한 사실 | 작업 내용의 오염 |

## 5. Pass 2 — Relation-first Input Output Test
- **Source Bundle:** `EXTRACTED` 기반의 원본 보존.
- **Meaning Block:** `INTERPRETED` (의미 덩어리)와 `EXTRACTED` (근거) 결합.
- **Relation Map:** `INFERRED`가 강하게 작동함 (맥락적 연결).
- **Line / Axis Pressure:** `INFERRED` + `WATCH` 상태.
- **Input Report Card:** `USER_JUDGED` 혹은 `INTERPRETED` 상태.

## 6. Pass 3 — Worker Output / Gemini Result Test
- **Gemini Summary:** `INTERPRETED` (원본에 기반함).
- **Unsupported Inference:** `AMBIGUOUS` 혹은 `INFERRED` 후 `WATCH` 태그.
- **Correction:** `USER_JUDGED`로 보정하여 기록.

## 7. Pass 4 — Line / Axis Pressure Test
- **CONNECTION_SEED:** `INFERRED` 레벨이 충분할 때 생성.
- **LINE_CANDIDATE:** `INFERRED` 연결이 반복 입증(3회 이상)될 때.
- **AXIS_CANDIDATE:** 여러 라인 압력이 동일한 질문을 향할 때.
- **Premature naming:** `AXIS_CANDIDATE` 단계에서는 절대 축 확정 금지.

## 8. Pass 5 — Watch / Hold / Residue / Process Asset Test
- **Watch:** `AMBIGUOUS`하거나 확인이 더 필요한 모든 상태.
- **Hold:** 재료는 있으나 연결 경로가 없는 상태.
- **Residue:** 추후 유용할 수 있으나 현재 우선순위 낮은 조각.
- **Process Asset:** `EXTRACTED` + `INTERPRETED` + `USER_JUDGED`가 성숙한 패턴으로 굳어진 것.

## 9. Pass 6 — Minimal Card / Template Check

### Minimal Evidence Label (Compact)
```markdown
- item:
- label: (EXTRACTED/INTERPRETED/INFERRED)
- reason:
- next safe action:
```

### Evidence Card (Standard/Heavy)
```markdown
# Evidence Label Card
- item:
- label: 
- source reference:
- reason:
- confidence:
- relation to line/axis:
- watch / hold item:
- next safe action:
```

## 10. Final label set

| Final label | Definition | Use for | Do not use for |
| :--- | :--- | :--- | :--- |
| **EXTRACTED** | 원문 직접 근거 | 팩트/데이터 확인 | 해석 주입 |
| **INTERPRETED** | 워커가 읽은 의미 | 맥락 보존/요약 | 원본의 진실화 |
| **INFERRED** | 원문 맥락적 유추 | 라인/축 후보 형성 | 확인된 팩트 |
| **AMBIGUOUS** | 모호/상충/추가 확인 필요 | 재검토 대상 | 확정 판정 |
| **USER_JUDGED** | 사용자 승인/보정 | 최종 의사결정 상태 | 원본 자체 수정 |
| **PROCESS_TRACE** | 작업 과정의 로그 | 워커 작업 추적 | 사실의 증명 |

## 11. Minimal rule set
1. 모든 추론(Inferred)은 반드시 라벨링하고, 이를 팩트와 혼용하지 마십시오.
2. 해석(Interpreted)은 반드시 `Source reference`를 포함해야 합니다.
3. 모호(Ambiguous)한 관계는 `Watch` 항목으로 돌려 재검토를 유도하십시오.
4. 사용자 판단(User-Judged)은 상태를 바꿀 뿐, 원본을 덮어쓰지 마십시오.
5. 과정 흔적(Process-Trace)은 '도구의 기록'일 뿐, '소스의 진실'이 아닙니다.

## 12. Integration points
- `Intake Packet`: 패킷 단계에서 초기 증거 등급(`EXTRACTED/INTERPRETED`) 부여.
- `Linkage Gate`: `INFERRED` 관계가 기존 `Line/Axis`와 충돌하는지 검토.
- `Re-entry Support`: `USER_JUDGED` 결과물만 재진입 앵커로 보존.

## 13. Structural problem list

| Problem | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Provenance Drift** | HIGH | 해석과 원문이 뒤섞임 | 항상 라벨링 준수 | 출처 없는 요약 |
| **Ceremony Drift** | MEDIUM | 모든 필드 작성이 무거움 | compact/standard 필드 선택 | 모든 라벨 필수화 |
| **Authority Drift** | HIGH | 워커의 라벨을 절대화함 | User 게이트 재확인 | Gemini 라벨을 truth로 승격 |

## 14. Recommended next state
**KEEP_AS_EVIDENCE_PROVENANCE_LABEL_CANDIDATE**

## 15. Watch items
*   라벨링이 곧 시스템의 '사실(Truth)'이 되는 것.
*   증거 라벨이 시스템의 레지스트리로 굳어지는 것.
*   사용자 판단을 라벨로 찍어 시스템의 법으로 바꾸는 것.
*   워커가 모든 데이터에 과도한 라벨링을 하려는 의식화 경향.

## 16. Do not do yet
- NO implementation of any tool.
- NO automation or runtime script.
- NO registry, index, ledger.
- NO formal schema.
- NO official workflow declaration.
- NO current-position update.
- NO baseline promotion.
- NO MCP attachment.
- NO ontology creation.
- NO forced pipeline creation.
- NO integrated engine implementation.
- NO Gemini verified-truth authority.
- NO Codex final authority.

## 17. Final status
**STATUS: EVIDENCE_PROVENANCE_CLASSIFICATION_CANDIDATE_COMPLETE**
