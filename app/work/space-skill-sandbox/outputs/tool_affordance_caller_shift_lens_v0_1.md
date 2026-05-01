# Tool Affordance / Caller Shift Lens v0.1

## 0. Status
- status: sandbox candidate
- version: 0.1 (Evidence-based Risk Naming Patch)
- operating_order_principle_ref: #2, #10, #11, #13
- source_space_rule: false
- baseline: false
- automation: false

## 1. Purpose
이 문서는 호출자(Caller)가 인간에서 LLM/Agent로 바뀔 때 발생하는 운영 위험을 식별하고, 기존 프로그램을 안전한 '손잡이(Affordance)'를 가진 '재료(Material)'로 다루기 위한 분석 렌즈를 제공한다.

v0.1에서는 '근거 기반 위험 명명(Evidence-based Risk Naming)' 원칙을 추가하여, 보안 용어 남용에 의한 시그널 노이즈를 방지하고 판단의 정밀도를 높인다.

## 2. Caller Shift: Human to LLM
호출자가 인간에서 LLM으로 바뀔 때 상실되는 '상식적 제동'을 보완해야 한다.

### Lost Contexts (위험 요소)
- **Implicit Boundary**: LLM은 명시적 금지가 없으면 경로를 이탈할 수 있다.
- **Side Effect Awareness**: LLM은 주어진 도구의 성공 결과에만 집중하며 부수 효과 판단이 약하다.
- **Tool Hallucination**: LLM은 존재하지 않는 옵션이나 인자를 도구에 주입하려 할 수 있다.

## 3. Function vs Affordance
도구는 "무엇을 할 수 있는가"가 아니라 "어떻게 사용해야 하고, 언제 사용하면 안 되는가"를 드러내야 한다.

### Affordance Components
1. **Intended Caller**: 허용된 세션 역할.
2. **Allowed Use Case**: 권장되는 상황.
3. **Forbidden Use Case**: 운영 질서상 금지된 사용법.
4. **Preflight Stop Point**: 실행 전 사용자 판단이 필요한 트리거.

## 4. Program as Material
기존 프로그램은 즉시 머지할 대상이 아니라, 분석해야 할 '재료'다.

### Material Analysis Stages
1. **Surface Mapping**: 입출력 및 부수 효과 확인.
2. **State Mutation Risk**: 상태 변이 여부 분석.
3. **Session Role Mapping**: 적합한 세션 역할 결정.
4. **Adapter Candidate**: 안전한 인터페이스 필요성 판단.

## 5. [NEW] Evidence-based Risk Naming
위험의 이름을 붙일 때는 반드시 기술적 근거(Evidence)와 실제 실행 가능한 공격 벡터(Exploit Vector)를 코드로 확인해야 한다.

### Risk Classification
- **Risk Candidate**: 위험 가능성이 의심되지만 구체적 경로가 확인되지 않은 상태.
- **Confirmed Risk**: 실제 exploit vector(예: unquoted variable, eval usage 등)가 코드로 증명된 상태.
- **Refuted Claim**: 분석 결과 기술적으로 불가능함이 입증된 주장.
- **Reclassified Risk**: 원래 주장과 다른 성격의 위험으로 재분류된 상태.

### Strong Security Terms Rule
'Shell Injection', 'Remote Code Execution' 등 강한 보안 용어는 오직 **Confirmed Risk** 단계에서만 사용한다. 그전에는 'Unsanitized Input', 'Path Handling Risk' 등 현상을 묘사하는 용어를 사용한다.

### Case Study: Run 034 Shell Injection Claim
- **Signal**: `RUN_ID`에 대한 필터링이 부족하여 메타문자가 주입될 수 있음 (Valid Signal).
- **Initial Claim**: Shell Injection (Wrong Risk Name - Code was quoted).
- **Result**: Reclassified as **Filename Pollution / Unsanitized Input**.
- **Lesson**: "그럴듯한 보안 용어"를 남용하면 운영 질서에 노이즈가 발생한다.

## 6. Checklist Update
- [ ] 위험 명칭이 실제 기술적 근거(코드 라인 등)와 연결되었는가?
- [ ] 강한 보안 용어를 사용했다면, 실제 exploit vector를 증명했는가?
- [ ] 기술적으로 불가능한 경계(Quoting 등)를 무시하고 위험을 과장하지 않았는가?

## 7. Non-Promotion Note
이 렌즈는 샌드박스 내 분석 도구일 뿐이다.
이 문서는 source-space rule이나 baseline이 아니며, 자동화나 에이전트 구현의 근거가 될 수 없다.

## 8. 4-line Footer
status: 완료
summary: Run 034/035의 교훈을 반영하여 '근거 기반 위험 명명' 원칙을 추가한 Tool Affordance Lens v0.1을 작성함
risk: 위험 분류 체계가 복잡해지면 에이전트가 판단을 회피하거나 보고를 지연할 수 있음
next: 사용자 리뷰 후 v0.1 렌즈를 사용하여 다른 기존 프로그램 분석을 지속할지 결정
