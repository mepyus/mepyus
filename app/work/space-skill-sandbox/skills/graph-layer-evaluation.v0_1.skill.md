# graph-layer-evaluation.v0_1.skill

## Status
sandbox candidate skill

## Trigger
사용자가 외부 Graph-based 도구(Graphify 등) 또는 공간 구조 시각화 자료를 내부 공간에 적용하고 싶어 할 때.

## Inputs
- 외부 자료 또는 테스트 폴더 구조
- 관련 Deep Space 참조 자료 (최대 3개)

## Procedure
1. 대상 자료가 Graph Layer 평가 대상인지 판정.
2. Graph Layer가 해결하려는 문제를 정의.
3. Deep Space / Worker Guide / Run Output과의 위치 관계 확인.
4. EXTRACTED / INFERRED / AMBIGUOUS 같은 provenance 구분이 가능한지 확인.
5. 토큰 절감보다 구조 탐색 가치가 있는지 확인.
6. Graph 결과가 truth/baseline으로 오해될 위험 확인.
7. Borrow / Hold / Reject로 분류.
8. status / summary / risk / next 반환.

## Required Checks
- 해당 자료가 즉시 구현/도입을 유도하지 않는가?
- 사용자가 그래프 해석 부담보다 맥락 연결의 이점을 더 크게 느끼는가?

## Borrow / Hold / Reject Criteria
- Borrow: 읽기 전용 구조 분석, 필요한 subgraph 추출, provenance(EXTRACTED/INFERRED) 명시.
- Hold: 도구 설치, hook/MCP 연결, 전체 공간 영구 분석, 자동 reingestion.
- Reject: 그래프를 truth로 취급, 자동 baseline 수정, 민감 자료 무검토 반영.

## Forbidden Drift
- Graphify 설치 금지
- 전체 공간 graph화 금지
- always-on hook 금지
- MCP 연결 금지
- 자동 reingestion 금지
- graph 결과를 baseline으로 사용 금지

## Output Format
- 구조 분석 요약
- Borrow/Hold/Reject 분류
- 위험 분석(Risk Check)
- 4줄 Footer

## 4-line Footer
status: [검증 필요 / 사용자 판단 필요 / 완료]
summary: [한 문장 요약]
risk: [핵심 위험 요소]
next: [다음 행동]
