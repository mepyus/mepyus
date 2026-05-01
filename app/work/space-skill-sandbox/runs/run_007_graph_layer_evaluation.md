# run_007_graph_layer_evaluation

## 1. Run Declaration
Graphify의 Graph Layer 개념을 우리 공간의 '지도층 후보'로 평가하기 위한 sandbox dry-run. 실제 설치/도입 없음.

## 2. Input Material
Graphify GitHub 개념 및 폴더 구조 분석 요약.

## 3. Skill Used
graph-layer-evaluation.v0_1.skill

## 4. Internal References
- app/work/space-skill-sandbox/review/sandbox_package_closeout_card_v0.md
- app/work/space-skill-sandbox/worker_guides/worker_guide_v0_1.md
- app/work/space-skill-sandbox/skills/structured-footer.v0_1.skill.md

## 5. Graph Layer Reading
- GRAPH_REPORT.md를 공간 지도 후보로 읽음.
- 필요한 맥락(subgraph)만 꺼내는 context injection 통로로 활용 가능.
- EXTRACTED / INFERRED / AMBIGUOUS 구분을 통해 Provenance-First 원칙 유지 가능.

## 6. Borrow / Hold / Reject
Borrow:
- GRAPH_REPORT.md를 공간 지도처럼 읽는 개념
- 필요한 subgraph만 꺼내는 원칙
- EXTRACTED / INFERRED / AMBIGUOUS 구분

Hold:
- Graphify 설치 및 항상 실행(always-on)
- MCP 연결
- 전체 공간의 영구 Graph화

Reject for now:
- Graph 결과를 Truth로 취급하는 행위
- INFERRED 엣지를 기준으로 기준(Baseline)을 자동 변경하는 행위

## 7. Risk Check
- 실제 도구 설치 시 발생할 수 있는 공간 오염 및 외부 도구 의존성 강화.
- 추론(INFERRED) 결과를 기준(Truth)으로 오해하여 공간 구조가 왜곡될 위험.

## 8. User Judgment Boundary
- 본체 Worker Guide에 Graphify 개념을 기본 검색기로 승격하는 것은 사용자 판단이 필요함.
- 외부 도구의 설치/도입 여부는 사용자 판단 필요.

## 9. 4-line Footer
status: 검증 필요
summary: Graphify의 Graph Layer 개념을 Deep Space 위의 탐색 가능한 지도층 후보로 평가함
risk: 실제 설치, hook, MCP, 전체 공간 graph화, graph 결과의 truth화는 사용자 판단 필요
next: validation_round_7에서 skill이 설치/자동화 없이 Graph Layer를 평가했는지 검증
