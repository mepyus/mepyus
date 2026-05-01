# run_018_relay_request_002_repeatability_check

## 1. Run Declaration
Sandbox Relay v0 규약에 따라 생성된 `request_002`를 기반으로 `worker_guide_v0_3_candidate`와 스킬 후보를 참조하여 외부 자료(Saltlux Goover 기술 분석) 분석의 반복 가능성을 검증함.

## 2. Inbox Request Used
- `app/work/space-skill-sandbox/relay/inbox/request_002_external_material_test.md`

## 3. Task Packet / Relay Flow Used
- `app/work/space-skill-sandbox/relay/prompts/gemini_task_packet_template_v0.md`의 지침을 다시 따름. (Read First → Routing → Execute)

## 4. Worker Guide Routing
`worker_guide_v0_3_candidate.md`를 읽고 아래와 같이 라우팅 판단함.
- **Main**: `skills/external-material-intake.skill.md` (외부 자료 구조 판독 및 내부 비교)
- **Support**:
  - `skills/preflight-guard.v0_1.skill.md` (Stop point 감지 - MCP/자동화 차단)
  - `skills/structured-footer.v0_1.skill.md` (결과 요약)
  - `skills/graph-layer-evaluation.v0_1.skill.md` (Ontology/Graph RAG 관련 provenance 분류)
  - `skills/failure-to-guide.v0_1.skill.md` (반복 위험 신호 포착)

## 5. Skills Consulted
- `external-material-intake.skill.md`
- `preflight-guard.v0_1.skill.md`
- `structured-footer.v0_1.skill.md`
- `graph-layer-evaluation.v0_1.skill.md`
- `failure-to-guide.v0_1.skill.md`

## 6. External Material Reading
- **해결하려는 문제**: 비정형 데이터의 신뢰성 있는 지식 가공 및 자동화된 에이전트 워크플로우 구축.
- **만든 사람의 문제의식**: LLM의 할루시네이션 극복 및 기업용 미션 크리티컬 시스템의 신뢰성 확보.
- **핵심 구조**: Neuro-Symbolic (Ontology + LLM), Graph RAG, Agentic Workflow (MCP 기반).
- **작동 흐름**: 외부 트리거(Signal) → 요약(Briefing) → 생성(Drafting)의 순환 구조.
- **숨은 전제**: Ontology(T-Box)가 사전에 정교하게 정의되어야 A-Box(데이터)를 정확히 Grounding할 수 있음.

## 7. Same / Similar but Dangerous / Different
### Same
- **관심사 분리**: 지식의 뼈대(Ontology/Core)와 실행 엔진(Agent/Skill)을 분리하는 구조적 접근.
- **역할 기반 에이전트**: 업무별로 역할을 세분화하여 책임을 부여하는 방식.

### Similar but Dangerous
- **MCP (Model Context Protocol)**: 에이전트 간 컨텍스트 공유를 위해 매우 유용해 보이지만, 현재 우리 샌드박스에 도입하기에는 아직 이른 '도구 기반 자동화' 표준임. 성급한 도입 시 시스템 형상 변동 위험.
- **Verification Loop**: 할루시네이션 억제를 위해 필수적이지만, '정답지(Ontology)'를 선고정하려는 압력은 우리 공간의 유연성을 해칠 수 있음.

### Different
- **뉴로-심볼릭 AI**: 우리는 LLM과 심볼릭의 결합보다는 '기록(Log)과 증거(Evidence)'를 통한 사후 검증(Provenance)에 더 집중함.
- **멀티모달 시각물 변환**: 기술적 목적이 지식 가공보다는 '자동 보고서 생성'에 치우쳐 있음.

## 8. Borrow / Hold / Reject
### Borrow Later
- **역할 기반 에이전트 이름**: `Signal Agent` 등의 명명 체계는 향후 우리 worker guide의 세부 스킬 명명 시 참고 가능.

### Hold
- **Graph RAG / Grounding 루프**: 샌드박스의 provenance 검증 절차를 강화하는 논리적 참조 모델로 보관.

### Reject for Now
- **MCP 표준 도입**: 현재는 설치 및 설정 변경이 수반되므로 기각.
- **Ontology 선고정 스키마**: 우리 공간의 '응결 우선' 원칙과 충돌하므로 기각.

## 9. Provenance Classification
| Claim | Classification | Source Anchor | Risk if Misread | Action |
|---|---|---|---|---|
| 구버는 뉴로-심볼릭 AI 접근법을 채택함 | source-claimed | tech_analysis Section 1 | 기술적 사실이 아닌 업체의 주장일 수 있음 | 차용 지침에서 거리 유지 |
| MCP 도입으로 유연한 결합이 가능함 | source-claimed | tech_analysis Section 3 | 자동화 표준이 우리에게 즉시 유익하다고 오해 | preflight-guard로 차단 |
| 지식 그래프를 통해 할루시네이션을 억제함 | source-claimed | tech_analysis Section 2.1 | 그래프만 있으면 진실이 보장된다고 오독 | 샌드박스 provenance 기준 우선 |
| Luxia 모델은 PPT 시각물 변환에 최적화됨 | source-claimed | tech_analysis Section 2.2 | 우리 엔진도 시각화가 우선이라고 오해 | 보류(Hold) 처리 |
| 검증 루프는 산업용 시스템 설계의 필수 모델임 | inferred-pattern | tech_analysis Section 3 | 이를 근거로 우리 검증 절차를 강제화하려는 경향 | 내부 판단으로 유보 |

## 10. Stop Point Check
- **MCP 표준 도입 및 에이전트 자동화**: 자료 내 MCP 언급과 자동화된 에이전트 워크플로우 제안을 감지함.
- **Action**: `preflight-guard`에 의해 '사용자 판단 필요'로 격상하고, 샌드박스 내 어떠한 설치나 자동화 시도도 수행하지 않음.

## 11. Failure-to-Guide Signal Check
- **failure_material**: 외부의 'MCP'와 같은 도구 표준을 공간의 유연한 규약보다 먼저 도입하려는 위험.
- **risk_if_repeated**: 시스템이 특정 도구에 종속(Lock-in)되거나 설치 오버헤드가 발생함.
- **guide_candidate**: 외부 도구 표준(MCP 등)은 비교 재료일 뿐, 샌드박스 내에서 사용자 명시적 승인 없이 도입하지 않는다.
- **status**: candidate
- **action**: `external_run_failure_signal_bundle_v0`에 추가 기록 가능하도록 보류.

## 12. Relay Repeatability Check
- **request_002만으로 작업 목적이 전달되었는가?**: 예. `request_001`과 유사한 구조의 요청만으로 분석 목표와 제약 사항이 명확히 전달됨.
- **request_001과 같은 relay 흐름을 재사용했는가?**: 예. `inbox` -> `task packet` -> `worker guide` -> `skills` -> `run` -> `outbox` 흐름을 완벽히 재사용함.
- **task packet template이 다시 실행 지시 역할을 했는가?**: 예. 템플릿의 지침에 따라 가이드를 먼저 읽고 라우팅하는 동작이 반복됨.
- **worker guide가 다시 라우팅 판단 기준으로 쓰였는가?**: 예. 55줄 가이드가 이번에도 정확히 5개 스킬을 복합 라우팅하는 지도가 됨.
- **outbox result 형식이 반복 가능했는가?**: 예. `result_template_v0`를 통해 일관된 요약 표면을 생성함.
- **남아 있는 수동 단계는 request 작성과 turn trigger뿐인가?**: 예. 파일 생성과 명령 시작 외의 모든 중간 중계 과정이 파일 시스템을 통해 처리됨.

## 13. Manual Copy/Paste Reduction Check
- 사용자가 분석 결과 전체를 채팅창에 복붙할 필요 없이, `result_002` 파일의 경로와 요약만 공유하면 됨.
- 대규모 텍스트 전송에 따른 토큰 소모와 병목이 줄어듦.

## 14. 4-line Footer
status: 검증 필요
summary: relay request_002를 사용해 Sandbox Relay v0가 다른 외부 자료에도 반복 적용 가능한지 dry-run함
risk: relay가 자동화나 production workflow처럼 오해될 수 있음
next: validation_round_19에서 relay 반복성, 라우팅 정확도, 수동 복붙 감소 여부를 검증
