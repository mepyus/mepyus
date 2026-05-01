# External Material Review Trial v0

## 1. Target Material
- **Title**: Building Effective Agents
- **Author/Source**: Anthropic (Blog/Research)
- **URL**: https://www.anthropic.com/research/building-effective-agents
- **Status**: Raw material analyzed via `external_material_review_route`

## 2. Borrow / Hold / Reject Classification

### [Borrow] 
- **Workflow-first Approach**: 에이전트의 완전한 자율성보다는 "사전에 정의된 경로(Workflow)"를 우선시하는 태도. 우리의 `Intent-Level Route Map`과 일맥상통함.
- **Evaluator-Optimizer Pattern**: 생성(Gemini)과 평가(Codex/Reviewer)를 분리하여 반복 개선하는 루프. 우리의 `Validation Session` 및 `Review` 구조의 이론적 근거로 활용 가능.
- **Transparency & Planning**: 계획 단계를 명시적으로 노출하여 신뢰를 높이는 것. 우리의 `Plan before Execution` 원칙을 강화하는 신호.

### [Hold]
- **Orchestrator-Workers Pattern**: 중앙 LLM이 동적으로 작업을 분해하는 방식. 현재 우리의 '수동 전달(Manual Handoff)' 경계를 무너뜨릴 위험이 있으므로, 자동화 허용 전까지는 보류(Hold).
- **Careful ACI (Agent-Computer Interface)**: 도구 설계를 에이전트 가독성에 맞추는 것. 중요하지만, 현재는 '기존 프로그램의 재료화'가 우선이므로 대규모 리팩토링은 나중에 고려.

### [Reject for Now]
- **Fully Autonomous Agents**: 에이전트가 실행 제어권을 완전히 갖는 시스템. 우리의 `User as Judge` 원칙과 정면 배치되므로 현재 단계에서는 수용 거부.

## 3. Signals Connected to Our Order
- **Signal 1 (Harness)**: "Harness matters more than the model." Anthropic도 에이전트의 성능보다 그를 둘러싼 '제어 구조'와 '평가 기준'의 중요성을 강조함.
- **Signal 2 (Route vs Skill)**: 단순 툴 사용(Skill)보다 작업의 흐름(Workflow/Route)을 설계하는 것이 품질의 핵심임을 재확인.
- **Signal 3 (Ground Truth)**: 도구 실행 결과로부터 얻는 피드백이 에이전트 교정의 유일한 길임을 강조. 우리의 `Error보다 Signal` 원칙과 연결됨.

## 4. Provenance & Risk of Over-interpretation
- **Source Claim**: Anthropic은 복잡한 작업에서 Orchestrator 패턴이 효율적이라고 주장함.
- **Our Interpretation**: 우리는 이를 '자동 오케스트레이션'이 아닌 '수동 세션 역할 분담(Session Role Map)'의 정당성으로 해석함.
- **Over-interpretation Risk**: "Anthropic이 그랬으니 우리도 에이전트에게 전체 제어권을 주자"는 식의 해석은 샌드박스 경계를 무너뜨리는 치명적인 과잉 해석임.

## 5. Next Small Candidate
- **Validation Feedback Patch**: `Evaluator-Optimizer` 패턴을 참고하여, `Validation Session` 결과가 단순 PASS/FAIL을 넘어 "어떻게 수정해야 하는지"에 대한 구체적 피드백을 `Gemini`에게 전달하는 표준 형식을 `Output Contract`에 보강해볼 수 있음.

## 6. Conclusion
Anthropic의 아티클은 우리의 `Operating Order Principles v0`가 지향하는 'Harness 중심', 'Route 중심', 'Validation 중심'의 운영이 옳음을 강력하게 지지하는 외부 근거이다. 다만, 그들이 제안하는 자율적 오케스트레이션은 우리의 수동 경계 내로 낮추어(Lowering) 수용해야 한다.

---
**4-line Footer**
status: 완료
summary: Anthropic의 에이전트 아티클을 분석하여 Workflow 중심 운영과 Evaluator-Optimizer 패턴의 유효성을 확인함
risk: 외부 자료의 '자율성' 강조 부분을 오해하여 우리 샌드박스의 '수동 제어 경계'를 조기에 포기하면 안 됨
next: 사용자 판단 후 'Evaluator-Optimizer' 피드백 구조를 Output Contract 후보로 보강하는 실험 진행
