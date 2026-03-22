# Boundary Case Generation Prompt v1

목적:
- ChatGPT 또는 Gemini에게 `scene / role / score`가 실제로 갈릴 수 있는 경계 사례를 만들게 한다.
- 이 사례들은 정답 데이터가 아니라 calibration용 충돌 유도 데이터다.

사용 위치:
- `processor_execution_prompt_v2.md`로 라벨링을 시키기 전에
- 먼저 `경계 사례 세트`를 생성할 때 사용한다.

## 사용법

이 프롬프트를 `ChatGPT`나 `Gemini`에게 주고,
아래 요청 블록을 함께 붙인다.

## 생성 지시

너의 역할은 정답 생성기가 아니라 calibration용 boundary case generator다.

너는 아래 축들에서 여러 처리자가 다르게 판정할 수 있는
짧은 한국어 문단들을 생성해야 한다.

목적:
- scene / role / score 경계가 실제로 흔들리는 샘플을 만든다.
- 한쪽으로 너무 명확한 쉬운 예시는 만들지 않는다.
- 너무 난해하거나 무의미한 문장도 만들지 않는다.
- 실제 문서 조각처럼 읽히는 자연스러운 짧은 문단을 만든다.

중요 규칙:
1. 출력은 JSON 배열 하나만 반환한다.
2. 마크다운 금지.
3. 설명문 금지.
4. 각 원소는 아래 필드만 가진다.
   - case_id
   - target_axis
   - boundary_pair
   - case_text
   - why_boundary
   - expected_tension
5. case_text는 2~6문장 길이의 자연스러운 한국어 문단이어야 한다.
6. 입력 문단은 실제 설명문, 대화 일부, 비평문, 회고문처럼 읽혀야 한다.
7. 한쪽 라벨로 너무 쉽게 떨어지는 예시는 피한다.
8. 허무맹랑한 비문, 의미 없는 추상문은 금지한다.
9. 같은 패턴을 단어만 바꿔 반복하지 말 것.

target_axis 허용값:
- scene
- role
- score

boundary_pair 예시:
- explanation_vs_reflection
- explanation_vs_evidence
- explanation_vs_comparison
- thesis_vs_expansion
- support_vs_example
- contrast_vs_expansion
- problem_vs_support
- confidence_vs_ambiguity
- stability_vs_mixed

필드 의미:
- case_id: 고유 id
- target_axis: scene / role / score 중 하나
- boundary_pair: 어떤 경계를 흔들기 위한 사례인지
- case_text: 실제 라벨링에 넣을 짧은 문단
- why_boundary: 왜 이 사례가 그 경계에서 갈릴 수 있는지 1문장
- expected_tension: 짧은 키워드 2~4개 배열

## 품질 기준

좋은 case_text:
- explanation처럼 보이지만 reflection의 여지가 있음
- support처럼 보이지만 example로 읽힐 수 있음
- confidence를 높게 주고 싶지만 ambiguity도 남아야 함
- stability가 높아 보이지만 실제로는 두 논지가 섞여 있음

나쁜 case_text:
- 한눈에 답이 명확한 교과서형 문장
- 무의미하게 모호한 문장
- 지나치게 메타적이어서 실제 문서 조각처럼 읽히지 않는 문장
- 특정 처리자가 프롬프트만으로 유리해지는 인위적 문장

## 요청 블록 템플릿

아래 형식으로 요청한다.

```text
다음 boundary case 세트를 만들어라.

총 개수: 30

분포:
- explanation_vs_reflection: 5
- explanation_vs_evidence: 4
- explanation_vs_comparison: 3
- thesis_vs_expansion: 4
- support_vs_example: 4
- contrast_vs_expansion: 3
- problem_vs_support: 3
- confidence_vs_ambiguity: 2
- stability_vs_mixed: 2

문체 제약:
- 설명문 / 비평문 / 회고문 / 대화문이 고르게 섞이게 할 것
- 특정 도메인만 반복하지 말 것
- 실제 문서 조각처럼 자연스럽게 쓸 것
```
