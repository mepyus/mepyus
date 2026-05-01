# Space Skill Sandbox v0.2 Closeout Card

## 1. 한 줄 결론
Space Skill Sandbox v0.2는 외부 자료 분석, 위험 작업 차단, 결과 요약, 그래프 평가 등 4가지 핵심 스킬 후보를 수립하고, 이를 55줄의 압축된 가이드 후보로 라우팅하는 안전한 실험 환경을 구축함.

## 2. 현재 샌드박스 상태
- **Package 1 (Core)**: 자료 반입(Intake), 사전 방어(Preflight), 구조적 푸터(Footer) 검증 완료.
- **Package 2 (Graph)**: Graph Layer 평가 및 Mini Graph Provenance 포맷 검증 완료.
- **Compaction**: 작업 효율화를 위한 가이드 후보 압축 및 반복성 테스트 완료.
- **Overall**: `package_validated: true`, `ready_for_more_sandbox_runs: true`.

## 3. 검증된 Skill 후보

### external-material-intake
외부 URL/자료를 바로 도입하지 않고, 내부 기준과 비교해 comparison / borrow-later / caution으로 낮추는 skill 후보.

### preflight-guard
삭제, baseline 승격, 설치/config 변경, 권한 변경 등 고위험 작업을 사용자 판단 필요로 올리고, 낮은 위험의 read-only 확인은 과하게 막지 않는 skill 후보.

### structured-footer
작업 결과를 status / summary / risk / next 4줄로 낮추되, 완료를 승인/lock/baseline으로 오해하지 않게 하는 skill 후보.

### graph-layer-evaluation
Graphify / Graph Layer / Mini Graph Map / provenance 관련 요청을 도구 설치 없이 지도층 후보로 평가하는 skill 후보.

## 4. Worker Guide v0.2 Candidate의 역할
- **압축성**: 55줄로 압축되어 작업자가 한눈에 파악 가능.
- **라우팅 지도**: 4가지 검증된 스킬 후보로 작업을 수동 라우팅하는 지침 제공.
- **안전성**: 6개 라우팅 테스트를 전수 통과(100%)했으며, 가드레일 누락 없음.
- **비고**: 본체(source-space) 가이드가 아닌 샌드박스 전용 후보 가이드임.

## 5. 지금까지 검증된 작동 흐름
**외부 자료/운영 패턴 → Lens → Skill → Run → Validation → Closeout → Worker Guide Compaction**
기존 공간을 곧바로 바꾸지 않고, 샌드박스 내에서 외부 재료를 렌즈로 읽고 스킬 후보로 낮춘 뒤, 실제 런과 검증을 거쳐 작업자가 읽을 수 있는 짧은 가이드로 압축하는 순환 구조가 정착됨.

## 6. 사용자가 얻은 실용적 의미
- 사용자가 매번 외부 자료를 복붙하고 긴 맥락을 반복 설명하는 부담을 줄이기 위한 첫 구조가 생겼음.
- CLI/Gemini/Codex가 샌드박스 내에서 어떤 skill 후보를 참조해야 하는지 알 수 있는 짧은 guide 후보가 생겼음.
- 외부 도구나 아이디어를 바로 도입하지 않고 Borrow / Hold / Reject 및 provenance 구분으로 낮추는 흐름이 생겼음.
- 위험 작업은 사용자 판단 필요로 올리고, 낮은 위험 read-only 작업은 과하게 막지 않는 경계가 검증되었음.

## 7. 유지된 경계
- **완료 ≠ 승인/baseline/lock**: 샌드박스의 작업 완료는 최종 승인이 아님.
- **candidate skill ≠ source-space rule**: 후보 스킬은 아직 정식 규칙이 아님.
- **worker guide candidate ≠ source-space guide**: 가이드 후보는 본체 기준이 아님.
- **source-claimed ≠ truth**: 원문 주장은 사실 확정이 아님.
- **inferred-pattern ≠ baseline**: 추론된 패턴은 시스템 기준이 아님.
- **ambiguous-link ≠ 무시 가능**: 모호한 연결은 기록하고 관리함.
- **[[SYNTH]] node ≠ 원문 용어**: 해석 용어와 원문 용어를 엄격히 분리함.
- **Graph Layer ≠ Deep Space**: 그래프는 지물(사실)이 아닌 지도임.

## 8. 아직 하면 안 되는 것
- skill을 source-space guide로 승격.
- 본체 worker guide 업데이트.
- Graphify / gstack / tool 실제 설치 및 실행.
- hook / MCP / watch mode 추가.
- 자동 skill routing 및 자동 reingestion 구현.
- 전체 Deep Space graph화.
- Mini Graph format을 ontology / schema / baseline으로 승격.
- candidate나 Graph 결과를 절대적 truth로 취급.

## 9. 사용자 판단이 필요한 지점
- 현재 검증된 skill/guide 후보를 본체(source-space)로 승격할지 여부.
- 실제 외부 도구(Graphify 등)를 환경에 설치하거나 설정을 변경할지 여부.
- hook / MCP 같은 실행 경로를 생성할지 여부.
- 현재의 샌드박스 패키지를 닫고 보류할지, 아니면 추가 실험을 진행할지 여부.

## 10. 다음 sandbox run 후보
- **A. Failure-to-Guide Skill sandbox run (추천)**: 실패/반복 오류/validation note를 다음 worker guide 후보 문장으로 바꾸는 스킬 검증.
- **B. Run Record Review Skill sandbox run**: 여러 run 결과를 비교해 반복 패턴과 위험을 추출하는 스킬 검증.
- **C. Worker Guide v0.2 사용자 검토 후 보류**: 추가 실험 없이 현재 상태 관찰 및 정독.
- **D. External Material Intake 실제 사례 추가 테스트**: 새로운 외부 자료 1개를 투입하여 v0.2 가이드의 라우팅 정확도 재확인.

## 11. 4줄 footer
status: 완료
summary: Space Skill Sandbox v0.2가 4개 skill 후보와 worker_guide_v0_2_candidate까지 검증되어, 샌드박스 안에서 외부 자료/위험 작업/결과 요약/Graph Layer 평가를 라우팅할 수 있는 상태로 정리됨
risk: 아직 source-space promotion, 자동화, 설치, 본체 worker guide 반영, ontology/schema/baseline 승격 단계는 아님
next: 사용자 검토 후 Failure-to-Guide Skill run으로 이동할지, 현재 상태를 보류할지 판단

---
This is a sandbox v0.2 closeout card only.
No source-space promotion was performed.
No automation, hook, MCP, watch mode, tool installation, baseline, schema, controller, router, ontology, or production workflow was created.
worker_guide_v0_2_candidate remains a sandbox candidate guide, not a source-space guide or baseline.
All listed skills remain sandbox candidate skills.
