# Tool Affordance / Caller Shift Lens v0

## 0. Status
- status: sandbox candidate
- operating_order_principle_ref: #2, #10, #11
- source_space_rule: false
- baseline: false
- automation: false

## 1. Purpose
이 문서는 호출자(Caller)가 인간에서 LLM/Agent로 바뀔 때 발생하는 운영 위험을 식별하고, 기존 프로그램을 안전한 '손잡이(Affordance)'를 가진 '재료(Material)'로 다루기 위한 분석 렌즈를 제공한다.

단순히 기능의 입출력을 정의하는 것을 넘어, 도구가 오용되지 않도록 하는 제동 장치와 경계를 설정하는 것이 목적이다.

## 2. Caller Shift: Human to LLM
호출자가 인간에서 LLM으로 바뀔 때 상실되는 '상식적 제동'을 보완해야 한다.

### Lost Contexts (위험 요소)
- **Implicit Boundary**: 인간은 "이 폴더 밖은 건드리지 마"라고 하지 않아도 상식적으로 멈추지만, LLM은 명시적 금지가 없으면 경로를 이탈할 수 있다.
- **Side Effect Awareness**: 인간은 명령 실행 전 시스템 전체에 미칠 영향을 직관적으로 판단하지만, LLM은 주어진 도구의 성공 결과에만 집중한다.
- **Tool Hallucination**: LLM은 존재하지 않는 옵션이나 인자를 도구에 억지로 끼워 넣으려 할 수 있다.

### Caller Shift Lens Checklist
- [ ] 도구가 명시적 경로 제약(sandbox-only)을 가지고 있는가?
- [ ] 파괴적 동작(삭제, 수정) 전 반드시 중단점(Preflight)이 있는가?
- [ ] 에러 발생 시 LLM이 스스로 판단하지 않고 보고해야 할 지점이 정의되었는가?

## 3. Function vs Affordance
도구는 "무엇을 할 수 있는가"가 아니라 "어떻게 사용해야 하고, 언제 사용하면 안 되는가"를 드러내야 한다.

### Affordance Components (손잡이 구성 요소)
1. **Intended Caller**: 이 도구를 사용하도록 허용된 세션 역할 (예: Intake Session 전용).
2. **Allowed Use Case**: 도구 사용이 권장되는 구체적 상황.
3. **Forbidden Use Case**: 기능적으로는 가능하더라도 운영 질서상 금지된 사용법 (예: source-space 직접 수정).
4. **Preflight Stop Point**: 실행 전 사용자 판단이 반드시 필요한 트리거 (예: 도구 설치, 권한 변경).

### Affordance Analysis Checklist
- [ ] 도구 설명에 "언제 사용하지 말아야 하는지"가 명시되었는가?
- [ ] 도구 호출 전 확인해야 할 'Preflight' 항목이 존재하는가?
- [ ] 호출자가 도구를 잘못 잡았을 때(오용 시) 발생하는 시그널이 정의되었는가?

## 4. Program as Material
기존 프로그램(Existing Program)은 즉시 머지할 대상이 아니라, 분석해야 할 '재료'다.

### Material Analysis Stages
1. **Surface Mapping**: 입출력, 파일 시스템 쓰기, 외부 호출 여부 확인.
2. **State Mutation Risk**: 프로그램이 시스템의 상태(DB, Config)를 영구적으로 바꾸는지 분석.
3. **Session Role Mapping**: 이 프로그램이 샌드박스의 어떤 세션 역할(Role)에 적합한지 결정.
4. **Adapter Candidate**: 직접 노출 대신 안전한 인터페이스(Adapter)가 필요한지 판단.

### Material Analysis Checklist
- [ ] 프로그램의 모든 부수 효과(Side-effects)가 나열되었는가?
- [ ] 이 프로그램을 사용하기 위해 필요한 세션 역할과 권한이 정의되었는가?
- [ ] 프로그램 실행 결과가 샌드박스 표준 출력 계약(Output Contract)을 따르는가?

## 5. User Judgment Surface
렌즈의 최종 목적은 사용자에게 '판단할 근거'를 제공하는 것이다.

- **Judgment Point**: 에이전트가 "다 했습니다"라고 하기 전에 "이 경계에서 당신의 승인이 필요합니다"라고 멈추는 지점.
- **Risk Reporting**: 렌즈를 통해 식별된 위험을 사용자에게 어떻게 보고할 것인가?

## 6. Non-Promotion Note
이 렌즈는 샌드박스 내 분석 도구일 뿐이다.
이 문서는 source-space rule이나 baseline이 아니며, 자동화나 에이전트 구현의 근거가 될 수 없다.

## 7. 4-line Footer
status: 완료
summary: Run 032를 통해 호출자 변화(Caller Shift)와 도구 손잡이(Affordance) 분석을 위한 운영 렌즈 후보 v0를 작성함
risk: 이 렌즈를 자동화된 룰셋이나 실제 에이전트 구현 지침으로 오해하여 경계를 넘어가면 안 됨
next: 사용자 리뷰 후 이 렌즈를 실제 기존 프로그램(Existing Program) 분석 Run에 적용해볼지 결정
