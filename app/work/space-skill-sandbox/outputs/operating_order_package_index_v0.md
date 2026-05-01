# Operating Order Package Index v0

## 0. Status
- status: sandbox candidate
- package_scope: Run 029 ~ Run 041
- baseline: false
- source_space_rule: false
- automation: false

## 1. Purpose
이 인덱스는 Run 029~041에서 생성된 Operating Order Principles 패키지 산출물을 역할별로 분류하고, 각 문서의 참조 시점과 주의사항을 기록한다. 모든 문서는 'sandbox candidate' 상태이며, 어떠한 소스 공간 수정이나 자동화 승인을 포함하지 않는다.

## 2. Document Categories

### A. 본류 기준 문서 (Core Principles & Rules)
샌드박스 운영의 가장 높은 판단 기준을 제공하는 문서들이다.

| File Path | 역할 | 언제 참조하는지 | 주의점 |
|---|---|---|---|
| `outputs/operating_order_principles_v0.md` | 15개 운영 원칙 후보 | 모든 샌드박스 작업의 근간을 잡을 때 | 베이스라인 아님 |
| `outputs/operating_order_source_map_v0.md` | 외부/내부 참조 매핑 | 원칙의 근거와 경계를 확인할 때 | 단순 인용용 아님 |
| `outputs/sandbox_promotion_pipeline_v0.md` | 승격 단계 및 게이트 후보 | 자산의 성숙도와 다음 단계를 판단할 때 | 실제 승격 수행 불가 |
| `outputs/session_role_map_v0.md` | 세션 역할 및 권한 경계 | Gemini/Codex에 특정 역할을 부여할 때 | 에이전트 구현 아님 |
| `outputs/agent_handoff_boundary_rule_v0.md` | 에이전트 간 전달 경계 | 작업 패킷의 생성자와 실행자를 구분할 때 | 자동화 경계 준수 |

### B. 보조 판단 문서 (Judgment Lenses & Maps)
특정 작업을 분석하거나 경로를 결정할 때 사용하는 보조 도구들이다.

| File Path | 역할 | 언제 참조하는지 | 관련 Route/Role |
|---|---|---|---|
| `outputs/intent_level_route_map_v0.md` | 수동 판단 지도 후보 | 사용자 의도를 어떤 운영 경로로 낮출지 결정할 때 | Routing Session |
| `outputs/tool_affordance_caller_shift_lens_v0_1.md` | 근거 기반 분석 렌즈 후보 | 기존 프로그램을 '재료'로 분석하고 손잡이를 찾을 때 | Intake Session |
| `outputs/packet_provenance_discipline_v0.md` | 패키지 출처 기록 규약 | 작업 패킷의 메타데이터를 작성할 때 | Relay Session |
| `outputs/sandbox_standard_output_contract_v0.md` | 표준 출력 형식 후보 | 작업 결과 보고서의 형식을 맞출 때 | All Sessions |

### C. 실행 보조 문서 (Execution & Harness Support)
실제 명령 실행이나 환경 확인을 돕는 문서와 스크립트들이다.

| File Path | 역할 | 언제 참조하는지 | 상태 |
|---|---|---|---|
| `outputs/manual_gemini_runner_script_candidate_v0.md` | 러너 허용 범위 및 금지선 | 러너의 동작 원리와 제약을 확인할 때 | support document |
| `outputs/gemini_runner_preflight_checklist_v0.md` | 러너 실행 전 체크리스트 | 실제 러너 호출 전 환경 가용성을 점검할 때 | runner support |
| `scripts/sandbox/run_gemini_packet.sh` | 수동 Gemini 러너 스크립트 | 수동으로 패킷을 실행할 때 | executable support |

### D. 실험 결과 및 리뷰 문서 (Experiments & Reviews)
원칙과 렌즈를 실제 데이터에 적용해본 기록들이다.

| File Path | 역할 | 내용 | 상태 |
|---|---|---|---|
| `outputs/existing_program_affordance_trial_v0.md` | 1차 렌즈 실험 결과 | Runner 스크립트 분석 사례 | experiment record |
| `outputs/existing_program_affordance_trial_2_v0_1.md` | 2차 렌즈 실험 결과 | Indexer 스크립트 분석 사례 | experiment record |
| `review/run_035_risk_audit_note.md` | 위험 오판 교정 리뷰 | Shell Injection 오판 및 재분류 기록 | review note |
| `review/run_038_loop_closeout_note.md` | 렌즈 루프 결산 리뷰 | 렌즈 v0 -> v0.1 발전 과정 요약 | review note |
| `review/run_040_route_dry_classification.md` | 경로 분류 실험 결과 | 4가지 시나리오별 경로 매핑 사례 | review note |
| `review/operating_order_package_closeout_note_v0.md` | 전체 패키지 결산 노트 | Run 029~040 통합 학습 결과 | closeout record |

## 3. Usage Notice
이 인덱스에 나열된 모든 자산은 `app/work/space-skill-sandbox` 내에서만 유효한 후보(candidate)들이다. `operating_order_reuse_guide_v0.md`와 함께 참조하여 경계를 넘지 않도록 주의해야 한다.

---
**4-line Footer**
status: 완료
summary: Run 029~041의 모든 산출물을 역할별(본류, 보조, 실행, 리뷰)로 분류하여 인덱스 작성을 완료함
risk: 인덱스된 문서들이 베이스라인이나 확정 규칙이 아님을 명확히 인지해야 함
next: operating_order_reuse_guide_v0.md를 통해 구체적인 재사용 지침 정리
