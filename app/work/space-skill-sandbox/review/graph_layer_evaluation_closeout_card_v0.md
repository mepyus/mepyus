# Graph Layer Evaluation Closeout Card v0

## 1. 한 줄 결론
Graph Layer는 Deep Space를 대체하는 층이 아니라 그 위에 놓이는 '탐색 가능한 지도층 후보'이며, 이를 안전하게 다루기 위한 **Mini Graph Provenance Format**의 유효성이 샌드박스 내에서 검증됨.

## 2. 이번 Graph Layer 실험에서 검증한 것
- 외부 도구(Graphify 등) 설치 없이 'Graph Layer' 개념을 샌드박스 내에서 평가함.
- 그래프 결과의 Truth-Overreach(과잉 사실화)를 막기 위한 3단계 분류 체계(source-claimed, inferred-pattern, ambiguous-link)를 검증함.
- 수동 Mini Graph Map 작성을 통해 복잡한 외부 자료 간의 구조적 반복 패턴(Recurrence)을 추출할 수 있음을 확인함.

## 3. 생성된 주요 후보 자산

### graph-layer-evaluation-lens
Graph Layer가 우리 공간에 적합한지, 그리고 공간 오염 위험이 없는지 판단하기 위한 평가 기준 렌즈.

### graph-layer-evaluation.v0_1.skill
사용자가 외부 그래프 도구 도입을 요청할 때, 이를 즉시 수용하지 않고 Borrow / Hold / Reject 프레임으로 낮추어 평가하는 스킬 후보.

### run_007 / validation_round_7
Graphify의 개념을 우리 공간의 '지도층 후보'로 정의하고, 설치 없이 개념적 유용성을 최초로 확인한 run.

### run_008 / validation_round_8
그래프 결과물에 대한 Provenance(근거) 분류 작업의 기초를 다지고, truth/baseline 오해 위험을 최초로 식별한 run.

### Mini Graph Provenance Format Candidate v0
노드 타입(Original, [[SYNTH]], Working)과 엣지 분류를 정의하여, 그래프 데이터를 안전하게 기록하기 위한 후보 포맷.

### run_009 / validation_round_10
Mini Graph Provenance 포맷을 Browser Harness, mini-swe-agent 등 서로 다른 자료 묶음에 적용하여 분류 체계의 반복 가능성과 안전성을 최종 검증한 run.

## 4. 핵심 provenance 구분

### source-claimed
원문이 직접 주장한 인과관계나 소속 관계. 이는 '사실'이 아니라 '원문이 주장한 내용'으로 보존됨.

### inferred-pattern
여러 자료의 반복되는 구조를 통해 우리가 추론한 관계. 시스템의 Baseline이 아닌 분석적 통찰로 취급함.

### ambiguous-link
연결 가능성은 있으나 근거가 약한 관계. 무시하기보다 기록하되, 'Reject for now' 또는 추가 검증 대상으로 관리함.

## 5. 사용자가 얻은 실용적 의미
- Graph Layer를 지도가 아닌 진실로 오해하여 발생하는 시스템 Drift 위험을 관리할 수 있게 됨.
- [[SYNTH]] 노드 태그를 통해 우리가 만든 해석과 원문의 용어를 명확히 구분함.
- Mini Graph Map을 보조 지도로 활용하여, 원문에서 더 깊이 확인해야 할 '다음 질문 후보'를 효과적으로 도출함.

## 6. 아직 하면 안 되는 것
- Graphify 설치 및 실행
- Graphify hook 설치 및 MCP 연결
- watch mode 추가
- 전체 Deep Space의 영구 Graph화
- source-space promotion (본체 반영)
- 본체 worker guide 업데이트
- Mini Graph format을 ontology / schema / baseline으로 승격
- INFERRED / inferred-pattern 결과를 공식 기준으로 반영
- AMBIGUOUS / ambiguous-link를 무단 무시
- Graph 결과를 절대적 truth로 취급
- 자동 reingestion과 결합

## 7. 사용자 판단이 필요한 지점
- 어떤 수준의 Graph Layer를 실제 검색 보조 도구로 채택할지 여부.
- 실제 Graphify 도구의 설치 및 실행 여부.
- 샌드박스에서 검증된 Provenance Format을 상위 레이어(Bridge 등)로 승격할지 여부.

## 8. 다음 선택지
- **A. Graph Layer 실험은 closeout 후 보류** (현재까지의 성과를 보존하고 멈춤)
- **B. 다른 skill 후보로 이동** (예: Failure-to-Guide Skill)
- **C. Failure-to-Guide Skill sandbox run** (가이드 실패 사례 분석)
- **D. Worker Guide v0_1 축소/정리 run** (후보 가이드들의 복잡도 관리)
- **E. 실제 Graphify 설치/실행 여부는 사용자 판단 후 별도 단계 진행**

## 9. 4-line footer
status: 완료
summary: Graph Layer Evaluation 실험이 lens / skill / run_007-009 / validation_round_7-10 / Mini Graph Provenance Format Candidate v0까지 샌드박스 안에서 검증되고 closeout card로 정리됨
risk: Graphify 설치, hook/MCP, 전체 공간 graph화, ontology/schema/baseline 승격은 아직 사용자 판단 필요
next: 사용자 검토 후 Graph Layer 실험을 닫을지, Failure-to-Guide 또는 Worker Guide 정리 run으로 이동할지 판단

---
This is a sandbox Graph Layer closeout card only.
No Graphify installation or execution was performed.
No automation, hook, MCP, watch mode, source-space promotion, baseline, schema, controller, router, ontology, or production workflow was created.
Mini Graph Provenance Format Candidate v0 remains a sandbox candidate format, not a source-space ontology or baseline.
