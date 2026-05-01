# Space Skill Sandbox v0.3 Closeout Card

## 1. 한 줄 결론
Space Skill Sandbox v0.3은 샌드박스 내 실패와 보정 신호를 다음 작업자용 가이드 후보로 회수하는 'Failure-to-Guide' 흐름을 확립하고, 이를 포함한 5개 스킬을 55줄의 압축된 가이드 후보로 안전하게 라우팅함.

## 2. 현재 샌드박스 상태
- **Package 1 (Core)**: 자료 반입, 사전 방어, 구조적 푸터 검증 완료.
- **Package 2 (Graph)**: Graph Layer 평가 및 Mini Graph Provenance 검증 완료.
- **Package 3 (Failure Recovery)**: 실패 사례의 가이드 후보 전환 및 번들 보관 검증 완료.
- **Compaction**: 5개 스킬 라우팅 및 7개 실패 가이드 후보를 통합한 v0.3 가이드 후보 확정.
- **Overall**: `package_validated: true`, `ready_for_more_sandbox_runs: true`.

## 3. v0.2에서 검증된 기반
- **external-material-intake**: 외부 자료를 내부 기준과 비교해 수준을 낮추는 스킬 후보.
- **preflight-guard**: 고위험 작업을 사용자 판단 필요로 올리는 차단 스킬 후보.
- **structured-footer**: 결과를 4줄(status/summary/risk/next)로 요약하는 스킬 후보.
- **graph-layer-evaluation**: Graph 도구 설치 없이 지도층 후보로 평가하는 스킬 후보.
- **worker_guide_v0_2_candidate**: 4개 스킬을 라우팅하는 55줄의 가이드 후보.

## 4. v0.3에서 추가된 것

### failure-to-guide.v0_1.skill
- **역할**: validation note, 실패 사례, PASS_WITH_NOTE를 분석하여 작업자용 가이드 후보 문장으로 변환.
- **핵심 원칙**: 실패는 버리는 데이터가 아니라 가이드 후보의 원료이며, 절대 자동으로 baseline이 되지 않음.

### failure_guide_candidates_bundle_v0
- **역할**: 추출된 7개의 가이드 후보를 근거(Source Anchor)와 함께 격리 보관하는 별도 저장소.
- **지표**: `guide_candidates_expected: 7`, `guide_candidates_recorded: 7`, `source_anchor_missing: 0`.
- **비고**: 이 번들은 워커 가이드나 정식 규칙(source-space rule)이 아님.

### worker_guide_v0_3_candidate
- **역할**: 5개 스킬 라우팅 구조에 7개 실패 가이드 후보를 가드레일과 중단점으로 압축 통합한 가이드 후보.
- **지표**: `guide_lines: 55`, `skills_routed: 5`, `routing_cases_passed: 8/8`.
- **판단**: 7개 후보를 모두 반영했으나 universal guardrail 수준으로 압축했기에 overinclude로 보지 않음.

## 5. 현재 라우팅 가능한 Skill 후보
1. **external-material-intake**: 외부 자료의 무분별한 도입 방지.
2. **preflight-guard**: 위험 작업의 독단적 수행 차단 및 사용자 에스컬레이션.
3. **structured-footer**: 명확한 작업 상태 보고 및 오해 방지.
4. **graph-layer-evaluation**: 설치 없이 그래프 기반 분석 가능성 평가.
5. **failure-to-guide**: 실패/위험 기록을 다음 가이드 후보로 자산화.

## 6. Worker Guide v0.3 Candidate의 역할
- **라우팅 지도**: 5개 스킬 후보 중 작업 목적에 맞는 도구를 선택하는 지침 제공.
- **가드레일 강화**: 번들에서 선별된 '완료 ≠ 승인', 'source-claimed ≠ truth' 등의 지침을 전파.
- **효율성 확보**: 낮은 위험의 read-only 확인(파일 존재 등)은 과하게 막지 않도록 허용 범위를 명시.
- **비고**: 본체 가이드가 아닌 샌드박스 내부용 후보 가이드임.

## 7. 지금까지 검증된 작동 흐름
**외부 자료/운영 패턴 → lens → skill → run → validation → closeout → worker guide compaction → failure material 회수 → guide candidate bundle → worker guide v0.3 candidate**

기존 공간을 유지하면서, 샌드박스 내에서 외부 재료와 실패 기록을 렌즈로 읽어 스킬 후보로 낮추고, 검증을 거쳐 작업자가 읽을 수 있는 짧은 가이드로 압축하는 순환 구조가 완성됨.

## 8. 사용자가 얻은 실용적 의미
- 작업자가 매번 긴 맥락을 설명하지 않아도 55줄 가이드를 통해 5개 스킬을 적절히 활용할 수 있음.
- 실패나 보정 지침이 휘발되지 않고 다음 작업자를 위한 가이드 후보로 축적되는 흐름이 생김.
- 위험 작업(설치, 자동화, 본체 수정)은 엄격히 차단하고, 안전한 확인 작업은 허용하는 유연한 경계가 설정됨.

## 9. 유지된 경계
- **완료 ≠ 승인/baseline/lock**: 샌드박스 작업 완료는 최종 승인이 아님.
- **candidate skill ≠ source-space rule**: 후보 스킬은 정식 규칙이 아님.
- **worker guide candidate ≠ source-space guide**: 가이드 후보는 본체 기준이 아님.
- **failure guide candidate ≠ baseline**: 실패에서 얻은 교훈은 후보일 뿐 고정된 기준이 아님.
- **source-claimed ≠ truth**: 원문 주장은 사실 확정이 아님.
- **inferred-pattern ≠ baseline**: 추론된 패턴은 시스템 기준이 아님.
- **[[SYNTH]] node ≠ 원문 용어**: 해석 용어와 원본 데이터를 엄격히 분리함.
- **Graph Layer ≠ Deep Space**: 그래프는 사실이 아닌 해석의 지도임.

## 10. 아직 하면 안 되는 것
- skill을 source-space guide로 승격하거나 본체 worker guide 업데이트.
- worker_guide_v0_3_candidate를 본체 가이드로 직접 반영.
- Graphify / gstack / tool 실제 설치, hook / MCP / watch mode 추가.
- 자동 skill routing, 자동 guide update, 자동 reingestion 구현.
- 전체 Deep Space graph화 또는 Mini Graph 포맷을 ontology/baseline으로 승격.
- failure guide candidate를 정식 운영 규칙이나 baseline으로 취급.

## 11. 사용자 판단이 필요한 지점
- 현재 검증된 v0.3 패키지(skill/guide)를 본체(source-space)로 승격할지 여부.
- 실제 외부 도구를 설치하거나 설정을 변경(config, hook 등)할지 여부.
- 자동화된 라우팅이나 가이드 업데이트 흐름을 설계할지 여부.
- 현재의 샌드박스 패키지를 닫고 보류할지, 다음 실험을 진행할지 여부.

## 12. 다음 sandbox run 후보
- **A. Run Record Review Skill sandbox run**: 여러 run 결과를 비교해 반복 패턴과 위험을 추출하는 skill 검증.
- **B. External Material Intake 실제 사례 추가 테스트 (추천)**: 새로운 외부 자료 1개를 투입하여 v0.3 가이드의 라우팅 정확도 재확인.
- **C. Sandbox v0.3 사용자 검토 후 보류**: 추가 실험 없이 현재 상태 관찰 및 정독.
- **D. Worker Guide v0.3 표현 축소/미세 조정**: 55줄 가이드를 더 줄이거나 표현을 낮추는 검토.

**추천 이유**: v0.3 guide가 5개 skill 라우팅을 통과했으므로, 실제 외부 자료 하나를 넣어 전체 흐름이 자연스럽게 작동하는지 보는 것이 가장 효과적임.

## 13. 4줄 footer
status: 완료
summary: Space Skill Sandbox v0.3가 5개 skill 후보와 worker_guide_v0_3_candidate까지 검증되어, 외부 자료 처리/위험 차단/결과 요약/Graph Layer 평가/실패 회수 흐름을 샌드박스 안에서 라우팅할 수 있는 상태로 정리됨
risk: 아직 source-space promotion, 자동화, 설치, 본체 worker guide 반영, ontology/schema/baseline 승격 단계는 아님
next: 사용자 검토 후 실제 외부 자료 1개로 v0.3 guide 라우팅 테스트를 진행할지, 현재 상태를 보류할지 판단

---
This is a sandbox v0.3 closeout card only.
No source-space promotion was performed.
No automation, hook, MCP, watch mode, tool installation, baseline, schema, controller, router, ontology, or production workflow was created.
worker_guide_v0_3_candidate remains a sandbox candidate guide, not a source-space guide or baseline.
All listed skills remain sandbox candidate skills.
failure_guide_candidates_bundle_v0 remains a sandbox candidate bundle, not a worker guide or source-space rule.
