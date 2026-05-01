# run_009_mini_graph_provenance_repeatability_check

## 1. Run Declaration
Mini Graph Provenance Format Candidate v0를 새로운 자료 묶음에 적용하여 분류 체계의 반복 가능성과 안전성을 수동으로 검증함.

## 2. Input Materials
- **source material missing**: Using prior conversation summary as input material for Browser Harness and mini-swe-agent.
- **Graphify Analysis Note**: Based on `run_008` context.

## 3. Format Candidate Used
Mini Graph Provenance Format Candidate v0

## 4. Node Candidates

- **node**: bash-only execution
  - **node_type**: Original
  - **source_anchor**: mini-swe-agent core philosophy
  - **note**: 원문에 명시된 실행 철학.

- **node**: helpers.py
  - **node_type**: Original
  - **source_anchor**: Browser Harness structure
  - **note**: 브라우저 조작을 돕는 유틸리티 파일.

- **node**: Thin Harness
  - **node_type**: [[SYNTH]]
  - **source_anchor**: Browser Harness + mini-swe-agent 반복 패턴
  - **note**: 여러 자료에서 관측되는 최소한의 실행 하네스 구조를 우리가 명명함.

- **node**: GRAPH_REPORT.md
  - **node_type**: Original
  - **source_anchor**: Graphify output spec
  - **note**: 도구 기술 문서에 명시된 출력 파일명.

## 5. Edge Candidates

- **edge**: mini-swe-agent --[claims-to-be]--> bash-only execution
  - **classification**: source-claimed
  - **source_anchor**: mini-swe-agent README (paraphrased)
  - **risk_if_misread**: 원문 주장을 절대적 진실로 오해할 수 있음.
  - **action**: 참조 가능

- **edge**: Browser Harness --[includes]--> helpers.py
  - **classification**: source-claimed
  - **source_anchor**: Browser Harness file list
  - **risk_if_misread**: 단순 포함 관계이므로 위험 낮음.
  - **action**: 참조 가능

- **edge**: Thin Harness --[describes]--> Browser Harness & mini-swe-agent
  - **classification**: inferred-pattern
  - **source_anchor**: Commonality in execution layer design
  - **risk_if_misread**: 원문 용어로 오해할 위험.
  - **action**: 검증 필요

- **edge**: Graph Layer --[potential-replacement]--> Worker Guide
  - **classification**: ambiguous-link
  - **source_anchor**: None (Speculative jump from tool capability)
  - **risk_if_misread**: 자동화에 대한 과도한 신뢰 유발.
  - **action**: Reject for now

- **edge**: Mini Graph Map --[leads-to]--> Next Query Candidate
  - **classification**: inferred-pattern
  - **source_anchor**: Operational use case for navigation
  - **risk_if_misread**: 지도가 곧 진실이라고 믿을 위험.
  - **action**: Borrow later

## 6. Provenance Classification Summary
- source-claimed: 2건
- inferred-pattern: 2건
- ambiguous-link: 1건

## 7. Query Candidates
- "mini-swe-agent의 bash-only 철학이 Browser Harness의 helpers.py 구조와 결합될 때 발생하는 보안 경계는?"
- "Thin Harness 구조를 유지하면서 Graphify의 GRAPH_REPORT를 통합할 때, [[SYNTH]] 노드의 오염을 막는 방법은?"

## 8. Risk Check
- [[SYNTH]] node인 'Thin Harness'를 원문 용어와 명확히 분리함.
- 'Graph Layer -> Worker Guide' 같은 과잉 연결을 'ambiguous-link'로 분류하여 차단함.
- 모든 판단에 source anchor(비록 요약본일지라도)를 명시함.

## 9. 4-line Footer
status: 검증 필요
summary: Mini Graph Provenance Format Candidate v0를 다른 자료 묶음에 적용해 node/edge/source anchor 분류의 반복 가능성을 테스트함
risk: [[SYNTH]] node나 inferred-pattern edge가 원문 주장처럼 굳어질 수 있음
next: validation_round_10에서 truth-overreach와 source anchor 누락 여부를 검증
