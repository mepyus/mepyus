# Minimal Brief Discipline Note v0

## 0. Status
- status: sandbox candidate
- version: 0.1
- operating_order_principle_ref: #11 (Plan before Execution), #13 (Definition before Prompt)
- source_space_rule: false
- baseline: false
- automation: false

## 1. Purpose
이 문서는 감독자(Supervisor/User)가 실행자(Gemini/Codex)에게 지시를 내릴 때, 세부 템플릿을 과잉 지정하여 실행자의 판단 여지를 박살내지 않도록 하는 '최소 브리프(Minimal Brief)' 운영 지침을 정의한다.

## 2. Over-specification vs Minimal Brief

### Case A: Over-specification (반면교사)
- **특징**: 산출물의 목차, 문장 수준의 내용, 검증 항목 20개 등을 감독자가 미리 다 써줌.
- **결과**: 실행기는 단순 복사-붙여넣기 기계로 전락함. 도구가 어디서 오해하는지, 무엇을 판단할 수 없는지 확인할 기회가 사라짐. 운영 질서가 "정답 받아쓰기"로 변질됨.
- **사례**: Run 032 이전의 안전장치 만들기 몰입 단계.

### Case B: Minimal Brief (지향점)
- **특징**: 작업의 목적, 참조할 기준, 절대 넘지 말아야 할 경계(금지), 기대하는 결과물의 성격, 나중에 리뷰할 질문만 제공함.
- **결과**: 실행기가 원칙을 해석하여 구조를 잡고 내용을 채움. 이 과정에서 발생하는 오판(예: Run 034의 Shell Injection 오해)이 오히려 운영 질서를 보강하는 핵심 재료(Signal)가 됨.
- **사례**: Run 032 ~ Run 042 실험 루프 전체.

## 3. The 5 Core Items of a Minimal Brief
앞으로 모든 지시는 다음 5개 항목 이하로 제한한다.

1. **목적 (Intent)**: 이 작업을 왜 하는가? (단순 "만들어라"가 아니라 "무엇을 검증/해결하기 위해"인지 명시)
2. **참조 (References)**: 어떤 원칙이나 이전 산출물을 손잡이(Affordance)로 잡아야 하는가?
3. **금지 (Forbidden/Boundary)**: 어떤 경계(source-space, automation, baseline 등)를 절대로 넘지 말아야 하는가?
4. **기대 산출물 (Expected Output)**: 어떤 형식의 문서나 기록이 나와야 하는가? (세부 목차 제외)
5. **리뷰 질문 (Review Questions)**: 작업 후 감독자가 무엇을 기준으로 판단의 질을 검토할 것인가?

## 4. Responsibility Mapping

### 도구의 판단 영역 (Tool Judgment)
- 문서의 세부 구조화 및 목차 구성
- 원칙을 실제 데이터에 적용하는 논리 전개
- 근거(Evidence)의 수집 및 매핑 방식
- 다음 단계에 대한 기술적 제안

### 감독자의 검토 영역 (Supervisor/User Review)
- 도구가 경계(Boundary)를 준수했는가?
- 도구가 원칙을 아전인수로 해석하지 않았는가?
- 도구가 명명한 위험(Risk Naming)에 타당한 근거가 있는가?
- 이 결과물이 다음 운영 경로(Route)로 넘어가기에 충분한 질을 갖췄는가?

## 5. Discipline Guardrails
- **No Specified Templates**: 실행기에게 "반드시 이 목차대로 써라"고 강제하지 않는다.
- **Leave Blank for Judgment**: 도구가 판단해야 할 부분을 감독자가 미리 채워서 주지 않는다.
- **Judge the Judgment**: 결과물 자체보다 도구가 결과물에 도달하기 위해 거친 '판단 과정'을 리뷰한다.

## 6. Non-Promotion Note
이 지침은 샌드박스 내 운영 협업을 위한 후보(candidate)일 뿐이다.
이 문서는 소스 공간의 규칙이나 베이스라인이 아니며, 어떠한 자동화 구현의 근거가 될 수 없다.

---
**4-line Footer**
status: 완료
summary: 과잉 지정의 위험을 경고하고 도구의 판단 공간을 확보하는 5대 최소 브리프 원칙을 수립함
risk: 최소 브리프가 지시의 모호함으로 변질되어 도구가 아예 엉뚱한 방향으로 실행하지 않도록 주의해야 함
next: 사용자 승인 후 이 원칙을 실제 다음 작업(Package 1 등)의 패킷 작성에 적용
