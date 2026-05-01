# Risk Audit Note: Run 035 (Audit Run 034)

## Verdict: CLAIM_REFUTED / RECLASSIFIED

### 1. Technical Audit of RUN_ID Usage
Run 034에서 제기된 "Shell Injection" 주장을 `scripts/sandbox/run_gemini_packet.sh` 소스 코드 기반으로 전수 조사한 결과는 다음과 같다.

- **Usage Pattern**: `RUN_ID`는 스크립트 내에서 오직 `"$RUN_ID"` 또는 `"${RUN_ID}"`와 같이 **Double Quotes(인용 부호)에 감싸인 상태**로만 사용됨. (Evidence: 192, 193, 196, 198, 205, 223행)
- **Execution Context**: `eval`, `bash -c`, 또는 인용 부호가 없는 명령 위치(Unquoted command position)에서 사용되는 사례가 없음.
- **Injection Test (Mental/Dry)**: 만약 `RUN_ID`가 `; id`로 입력되더라도, 스크립트는 `; id_gemini_outbox_...`라는 리터럴 파일명을 생성할 뿐이며, `;`를 명령 구분자로 해석하여 `id` 명령을 실행할 수 없음.

### 2. Risk Reclassification
따라서 "Shell Injection"이라는 명칭은 기술적으로 부적절하며(False Positive), 다음과 같이 재분류한다.

- **Primary Risk: Filename Pollution / Unsanitized Input**: 파일 시스템에 메타문자가 포함된 비정상적인 파일명이 생성되거나, 로그/JSON 파일 내에 정제되지 않은 문자열이 기록되는 위험.
- **Secondary Risk: Minor Option Injection**: (현재 스크립트에는 해당 없으나) 만약 이 변수가 다른 도구의 인자로 바로 넘겨질 경우 옵션(`-`)으로 오인될 수 있는 잠재적 위험.

### 3. Lens v0 Feedback & "Risk Naming" Principle
이번 사례는 에이전트가 보안 위험을 식별할 때 **"그럴듯한 보안 용어"를 남용(Hallucination)**할 수 있음을 보여줌. 이에 따라 `Tool Affordance Lens`에 다음 원칙 보강이 필요함.

- **Principle: Risk Naming Requires Evidence**: 위험의 이름을 붙일 때는 반드시 실제 실행 가능한 공격 벡터(Exploit Vector)를 코드로 증명해야 함. "가능성"만으로 치명적 보안 용어를 사용하는 것은 운영 질서를 어지럽히는 '시그널 노이즈'임.

### 4. Conclusion
Run 034의 분석 결과는 **"위험 지점(Unsanitized Input)을 찾은 것에는 의미가 있으나, 위험의 성격(Shell Injection)을 오판함"**으로 결론지음. 렌즈 v0의 실전 적용 시 '정확한 명명'에 대한 주의가 필요함.

---
**4-line Footer**
status: 완료
summary: Run 035를 통해 Run 034의 Shell Injection 주장이 기술적 오판임을 입증하고 Filename Pollution으로 위험을 재분류함
risk: 에이전트가 보안 용어를 과장하여 시그널 노이즈를 만들 수 있음을 식별함 (Risk Naming Hallucination)
next: Tool Affordance Lens v0.1에 'Evidence-based Risk Naming' 원칙을 추가하고 다음 분석 진행
