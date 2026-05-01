# run_014_external_material_v0_3_routing_test

## 1. Run Declaration
실제 외부 기술 사례인 Saltlux Goover 요약 자료를 `worker_guide_v0_3_candidate`에 따라 라우팅하고, 분석 및 provenance 분류를 수행하는 dry-run 테스트임.

## 2. Input Material
- **Name**: Saltlux Goover / Ontology-based Multi-Agent System 사례 요약
- **Source**: `external_case_example_saltlux_goover_relation_reading_v0.md`
- **Type**: 외부 기술 사례, 구조 비교 재료

## 3. Worker Guide Routing
`worker_guide_v0_3_candidate`에 근거하여 아래와 같이 라우팅함.
- **Main**: `external-material-intake.skill.md` (외부 자료 구조 분석 및 내부 비교)
- **Support 1**: `graph-layer-evaluation.v0_1.skill.md` (Ontology/Graph 기반 구조 및 Provenance 분류)
- **Support 2**: `preflight-guard.v0_1.skill.md` (자동화/도구 설치 유도 차단)
- **Support 3**: `failure-to-guide.v0_1.skill.md` (우리 철학과 다른 'ontology 선고정' 위험 포착)
- **Footer**: `structured-footer.v0_1.skill.md` (최종 요약 반입)

## 4. Skills Used
- `external-material-intake.skill.md`
- `preflight-guard.v0_1.skill.md`
- `structured-footer.v0_1.skill.md`
- `graph-layer-evaluation.v0_1.skill.md`
- `failure-to-guide.v0_1.skill.md`

## 5. External Material Reading
- **해결하려는 문제**: 기업용 지식 관리 및 멀티 에이전트 오케스트레이션.
- **핵심 구조**: Ontology 기반의 Graph RAG와 역할 기반 에이전트(Signal, Briefing, Drafting)의 협업.
- **작동 흐름**: 생성 결과를 Ontology와 대조하여 검증(Grounding/Verification Loop).
- **숨은 전제**: 개념(Ontology)이 먼저 정의되어야 데이터가 유의미하게 결합될 수 있음.

## 6. Internal Reference Check
- `worker_guide_v0_3_candidate.md`: 라우팅 및 가드레일 기준.
- `external-material-intake.skill.md`: 비교 및 차용(Borrow) 기준.

## 7. Same / Similar but Dangerous / Different

### Same
- **의미층/실행층 분리**: 구조와 실행을 섞지 않는다는 원칙은 우리 공간의 '기준문/운영문서/관찰면' 분리와 일치함.
- **역할 기반 에이전트**: 에이전트별 역할을 명확히 하는 것은 우리 프로젝트의 Codex/Gemini/User 분리와 유사함.

### Similar but Dangerous
- **Verification Loop**: 결과를 그냥 믿지 않고 검증한다는 점은 같으나, 저쪽은 ontology(고정 기준)를 쓰고 우리는 provenance(흐름 추적)를 씀. ontology 방식 그대로 도입 시 유연성 훼손 위험.

### Different
- **Ontology 선고정**: 저쪽은 개념을 먼저 잠그고 데이터를 얹는 방식이나, 우리는 데이터가 먼저 쌓이고 나중에 개념이 응결되는 방식임. 전제 조건이 다름.

## 8. Borrow / Hold / Reject

### Borrow Later
- **역할 분리 원리**: 에이전트 수를 늘리는 것이 아니라, 각 스킬별 '역할(Role)'을 더 선명하게 정의하는 방식은 참고 가능.

### Hold
- **Grounding/Verification Loop**: 샌드박스 검증 노트를 더 강화된 루프로 구성할지에 대해서는 추가 검토 필요.

### Reject for Now
- **Ontology 선고정 방식**: 우리 엔진의 '희미한 연결 보존' 철학에 반하므로 코어 도입 기각.

## 9. Provenance Classification

| Claim | Classification | Source Anchor | Risk if Misread | Action |
|---|---|---|---|---|
| Saltlux Goover는 ontology와 agent workflow를 분리함 | source-claimed | 입력 자료 Section 3-1 | 실제 구현 세부가 다를 수 있음 | 구조 분리 원리만 차용 검토 |
| 우리 공간도 이미 구조와 실행을 분리하려는 방향을 가짐 | inferred-pattern | 입력 자료 Section 3-1 관계 판독 | 이 패턴을 공식 Baseline으로 오해할 위험 | 관찰된 패턴으로 유지 |
| ontology 선고정은 우리 철학과 충돌함 | inferred-pattern | 입력 자료 Section 3-4 관계 판독 | 모든 외부 ontology를 적대적으로 볼 위험 | 분리 유지 사유로 기록 |
| 미래에 이 사례를 탐색 기능 정의 예시로 쓸 수 있음 | inferred-pattern | 입력 자료 Section 5 | 확정된 로드맵으로 오해할 위험 | 힌트(Hint)로 보관 |
| 이 문서는 엔진 점검기로 작동함 | source-claimed | 입력 자료 Section 4-4 | 단순 기술 문서로만 읽힐 위험 | 다중 역할(재료/점검기)로 분류 |

## 10. Preflight / Stop Point Check
- **위험 요소**: 자료 내 'enterprise-grade orchestration'이나 'ontology 선고정'을 우리 공간에 그대로 구현하려는 시도.
- **판단**: 현재 샌드박스 범위를 넘는 작업이므로 **사용자 판단 필요**로 격상함. (실제 도구 설치나 스키마 변경 시도 없음)

## 11. Failure-to-Guide Signal Check
- **failure_material**: 외부 자료의 'Ontology 선고정'을 우리 공간의 Baseline으로 오해하여 성급하게 스키마를 잠그려는 위험.
- **risk_if_repeated**: 시스템의 유연성이 사라지고 숙성 전의 데이터가 고착화됨.
- **guide_candidate**: 외부의 ontology 방식은 비교축일 뿐, 우리 공간의 baseline으로 즉시 승격하지 않는다.
- **status**: candidate
- **action**: worker guide v0.3 번들 후보로 보류 기록.

## 12. 4-line Footer
status: 검증 필요
summary: 실제 외부 자료인 Saltlux 사례를 worker_guide_v0_3_candidate에 따라 라우팅하고, 철학적 비교 및 provenance 분류를 통해 샌드박스 내 분석을 수행함
risk: 외부의 'ontology 선고정' 방식을 우리 시스템의 정답으로 과잉 해석할 위험이 있으나, 'Reject for Now'로 분류하여 방어함
next: validation_round_15에서 라우팅 정확도 및 provenance 구분, stop point 감지 여부를 검증
