# run_020_compact_relay_request_003_check

## 1. Run Declaration
Sandbox Relay v0 규약의 Compact Template v0.1을 기반으로 `request_003`을 처리하고, 작업 의도와 경계 유지 여부를 검증하는 dry-run 기록임.

## 2. Inbox Request Used
- `app/work/space-skill-sandbox/relay/inbox/request_003_compact_external_material_test.md`

## 3. Task Packet / Relay Flow Used
- `app/work/space-skill-sandbox/relay/prompts/gemini_task_packet_template_v0.md` 참조.

## 4. Worker Guide Routing
`worker_guide_v0_3_candidate.md`를 읽고 아래와 같이 라우팅함.
- **Main**: `external-material-intake.skill.md`
- **Support**: `preflight-guard.v0_1.skill.md`, `structured-footer.v0_1.skill.md`, `graph-layer-evaluation.v0_1.skill.md`, `failure-to-guide.v0_1.skill.md`

## 5. Skills Consulted
- `external-material-intake.skill.md`
- `preflight-guard.v0_1.skill.md`
- `structured-footer.v0_1.skill.md`
- `graph-layer-evaluation.v0_1.skill.md`
- `failure-to-guide.v0_1.skill.md`

## 6. External Material Reading
- **문제**: 비정형 데이터의 신뢰성 있는 지식 가공.
- **핵심 구조**: Neuro-Symbolic, Graph RAG, MCP 기반 에이전트.
- **분석**: "의미층(Ontology)과 실행층(Agent)의 분리"라는 원칙은 우리 공간과 닿으나, "개념 선고정(Ontology 우선)"은 우리 철학인 '연결의 응결'과 충돌함.

## 7. Borrow / Hold / Reject
- **Borrow**: 역할 분리 원리 (Codex/Gemini 역할 강화).
- **Hold**: Grounding 루프 (내부 검증 절차 강화 시 참고).
- **Reject**: Ontology 선고정 방식 (유연성 유지 위해 기각).

## 8. Provenance Classification
| Claim | Classification | Source Anchor | Risk if Misread | Action |
|---|---|---|---|---|
| 구버는 뉴로-심볼릭 AI를 채택함 | source-claimed | tech_analysis Section 1 | 업체의 주장을 시스템 확정 사실로 오독 | 거리 유지 |
| MCP로 유연한 결합 가능 | source-claimed | tech_analysis Section 3 | 자동화 도입 오해 | 차단 |

## 9. Stop Point Check
- 기업형 자동 오케스트레이션 및 고정 온톨로지 도입 감지.
- **Action**: 차단 및 'Reject for Now' 처리.

## 10. Failure-to-Guide Signal Check
- **Signal**: 외부 철학의 성급한 이식 위험.
- **status**: candidate (번들 보관)

## 11. Compact Template Usability Check
- **compactness**: 기존 대비 섹션이 6개로 줄어 작성이 간결함.
- **usability**: 필수 경계와 라우팅 구조가 그대로 유지되어 작업 목적 달성에 충분함.
- **결론**: 기존 v0 템플릿보다 효율적임.

## 12. Manual Copy/Paste Reduction Check
- 사용자가 필요한 항목만 작성함으로써 의도 전달이 명확해지고, 릴레이 구조 내에서 맥락이 고정되어 추가 설명이 불필요함.
- **verdict**: 성공.

## 13. 4-line Footer
status: 완료
summary: compact relay request_003을 사용해 Sandbox Relay v0가 다른 외부 자료에도 반복 적용 가능한지 dry-run함
risk: compact template이 너무 짧아 stop point나 boundary가 누락될 수 있음
next: validation_round_21에서 compact 충분성, 라우팅 정확도, 경계 유지 여부를 검증
