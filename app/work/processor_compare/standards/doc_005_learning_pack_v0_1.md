# CODEX LEARNING PACK
# doc_005 기반 입력기 / 라벨기 보정 기준선 v0.1

목적:
- Codex가 doc_005 비교 결과를 학습하고, 이후 비교/보정/문서화 작업에서 같은 방향성을 유지하도록 한다.
- 입력기(fragment boundary) 보정, 라벨기(scene / role / tags / score) 보정, 비교 리포트 해석 기준, calibration 문서 재실행 기준을 고정한다.

중요:
- 이 문서는 정답 문서가 아니다.
- 이 문서는 비교를 통해 드러난 처리자 성향과 그에 따른 보정 기준을 Codex에게 학습시키기 위한 문서다.

## 0. 최상위 전제

현재 실험의 목적은 "누가 가장 똑똑한가"를 고르는 것이 아니다.

목적은:
- 동일 원문을 여러 처리자가 어떻게 다르게 자르는지
- 같은 조각을 어떻게 다르게 라벨링하는지
- 그 차이를 누적해
- 내 방식의 입력기 / 앵커기 / 라벨기를 제련하는 것이다

따라서 Codex는 비교 결과를 볼 때 "정답/오답" 프레임보다 "경향/편향/보정 포인트" 프레임으로 읽어야 한다.

## 1. doc_005가 왜 중요한가

doc_005는 지금까지 비교한 문서 중에서 입력기 차이와 라벨기 차이가 가장 넓고 선명하게 드러난 calibration 문서다.

이 문서에서는 다음이 동시에 드러났다.
- 도입 요약과 정의를 분리할지 통합할지
- 문제와 해법을 분리할지 한 흐름으로 묶을지
- 기술 메커니즘과 전략적 가치, AI 활용을 분리할지 통합할지
- Object / Property / Link / Action 개념을 얼마나 세밀하게 쪼갤지
- 결론을 thesis로 읽을지 reflection/meta로 읽을지

앞으로 입력기 / 라벨기 변경 후 반드시 다시 돌려봐야 하는 calibration 문서로 취급한다.

## 2. 처리자별 성향

### Codex
- 중간 granularity
- 구조적 분해
- 보수적 점수
- 극단적 추상화, 메타화 적음
- 기술 구조와 의미 구조를 함께 유지하려는 경향

실무적 의미:
- 현재 단계에서 Codex는 절대 정답은 아니지만 중간 기준 후보로 유용하다.

### ChatGPT
- 세분화 경향 강함
- 해법, 결론을 빨리 독립 주장으로 세움
- confidence 높음
- ambiguity 낮음
- scene 오용 반복 (`definition`, `example` 등을 scene에 넣는 경향)

실무적 의미:
- ChatGPT가 항상 쪼개는 구간은 과세분화 후보로 봐야 한다.
- scene 오용은 schema 보정이 필요하다는 명확한 신호다.

### Gemini
- 큰 의미 덩어리로 묶음
- 요약, 정의, 결론을 상위 추상화로 흡수
- 메타 해석 증가
- 결론을 thesis보다 reflection/meta로 읽는 경향
- anchor 수를 적게 두고 더 큰 상위 label로 이동

실무적 의미:
- Gemini가 늘 크게 묶는 구간은 과대묶음 후보로 봐야 한다.
- 결론에서 메타화가 쉽게 발생하므로 role/scene 기준을 더 세게 잠글 필요가 있다.

## 3. 잠가야 할 핵심 결론

1. Codex / ChatGPT / Gemini의 차이는 우연이 아니라 누적 관찰에서 반복된 처리자 고유 성향이다.
2. scene/role 기준은 현재 너무 약하고, 더 엄격하게 고정해야 한다.
3. 입력기 경계 규칙은 추상적으로 두지 말고 대표 패턴으로 잠가야 한다.
4. Codex는 현재 calibration 중간값으로 유용하다.

## 4. 입력기 보정 기준 v0.1

### 패턴 A. 요약/도입 vs 정의
- 단순 도입, 요약과 명시적 정의는 기본적으로 분리 후보다.
- 도입이 정의를 직접 다시 말하는 수준이면 통합 가능하다.
- 개념 소개와 개념 정의를 무조건 하나로 흡수하지 않는다.

Codex 행동 원칙:
- 도입 문단이 "무엇을 설명하려는가"를 소개하고
- 다음 문단이 "그것이 정확히 무엇인가"를 직접 정의하면
- 우선 분리 후보로 본다.

### 패턴 B. 문제 제기 vs 해법 진술
- 문제와 해법은 논리적으로 구분되면 분리 후보다.
- 전환이 짧고 해법이 문제의 직접 귀결로 붙어 있으면 하나의 문제-해법 흐름으로 유지할 수도 있다.
- 이 구간은 calibration 대상이므로 보고서에서 반드시 분리 가능성을 언급한다.

Codex 행동 원칙:
- 문제 서술이 충분히 독립적이면 별도 fragment
- 문제 제기 직후 한두 문장으로 해법이 붙으면 하나의 흐름으로 유지 가능
- 리포트에 `problem_solution_boundary_candidate`를 남긴다

### 패턴 C. 기술 메커니즘 vs 전략적 가치 / AI 활용
- 기술적 구현 설명과 활용 가치 설명은 기본적으로 분리 후보다.
- "어떻게 구현되는가"와 "왜 중요한가"는 의미 움직임이 다르다.

Codex 행동 원칙:
- 메커니즘 설명이 길고 독립적이면 분리
- 뒤이어 가치, 응용, AI 활용 설명이 나오면 별도 fragment 후보
- 이 패턴은 입력기 조정의 핵심 calibration 포인트로 취급한다.

## 5. 라벨기 보정 기준 v0.1

핵심 원칙:
- scene과 role은 절대 섞지 않는다.
- scene = 장면 성격, 서술 모드
- role = 기능적 역할, 논리적 기능

강제 규칙:
- `definition`, `example`, `thesis`, `support`, `problem`, `bridge`는 role 계열이다.
- scene으로 쓰면 안 된다.

scene 허용값:
- discovery
- explanation
- comparison
- evidence
- question
- reflection
- instruction
- transition
- unknown

role 허용값:
- thesis
- support
- bridge
- example
- contrast
- definition
- expansion
- problem
- meta
- unknown

대표 매핑 규칙:
- 정의를 설명하는 문단: `scene=explanation`, `role=definition`
- 사례 문단: `scene=explanation`, `role=example`
- 문제 제기 문단: `scene=explanation`, `role=problem`
- 결론 주장 문단: `scene=explanation`, `role=thesis`
- 진짜 메타 반성일 때만: `scene=reflection`, `role=meta`

Gemini 보정 규칙:
- 결론을 쉽게 reflection/meta로 올리는 경향이 있으므로 실제 메타 해석인지 재판정한다.

ChatGPT 보정 규칙:
- `definition`, `example`를 scene에 넣는 경향이 있으므로 normalize로 숨기지 말고 `scene_schema_violation`으로 리포트에 남긴다.

## 6. anchor / tag 보정 기준 v0.1

ChatGPT 보정:
- 불필요한 세분 anchor인지
- 상위 anchor로 재사용 가능한지
- 해법, 결론을 과도하게 독립 anchor로 승격했는지 확인한다

Gemini 보정:
- anchor가 지나치게 상위 개념으로 올라갔는지
- 원문에 있는 중요한 중간 손잡이가 사라졌는지
- meta label이 과도하게 붙었는지 확인한다

Codex 기준:
- 재사용 가능하고
- 너무 세밀하지 않고
- 너무 추상적이지 않은
- 중간 anchor granularity를 유지한다

## 7. 점수 해석 기준

doc_005 관찰:
- ChatGPT: confidence 높고 ambiguity 낮음
- Gemini: Codex보다 조금 더 안정적, 단정적
- Codex: 보수적 점수

따라서 Codex는 다음을 전제한다.
- 높은 confidence는 곧 좋은 것이 아니다
- 낮은 ambiguity는 곧 좋은 것이 아니다
- Codex의 보수적 점수는 calibration 기준 후보로 유용하다

## 8. doc_005 기반 리포트 작성 규약

Codex는 doc_005와 유사 문서를 비교할 때 아래 순서로 리포트를 작성한다.

1. fragment count 비교
2. 평균 점수 비교
- direction
- intensity
- stability
- confidence
- ambiguity
3. 경계 패턴 비교
- 요약/정의
- 문제/해법
- 메커니즘/가치
4. scene/role schema 위반 체크
- ChatGPT의 scene 오용
- Gemini의 meta 과사용
5. anchor granularity 비교
- 세분 anchor
- 중간 anchor
- 상위 추상 anchor
6. calibration 포인트 도출
- 이 문서가 입력기/라벨기 기준 보정에 어떤 신호를 주는지 마지막에 한 줄로 적는다

## 9. Codex 행동 규약

1. doc_005를 calibration_doc으로 취급한다.
2. doc_005와 유사한 문서가 나오면 대표 경계 패턴을 먼저 본다.
3. scene과 role을 절대 섞지 않는다.
4. ChatGPT의 scene 위반은 normalize로 숨기지 말고 report에 남긴다.
5. Gemini의 meta/reflection 확대는 실제 메타인지 재판정한다.
6. Codex 자신은 중간 granularity 기준을 유지하려고 한다.
7. 입력기 수정 제안은 항상 과세분화 후보, 과대묶음 후보, 중간 기준 후보 구조로 제시한다.
8. viewer나 UI보다 calibration 리포트를 우선한다.
9. 지금 단계에서 core redesign를 자동 제안하지 않는다.
10. 비교 데이터가 더 쌓인 뒤에만 입력기/라벨기 기준 승격을 제안한다.

## 10. 잠금 문장

doc_005는 calibration 문서다.
scene/role은 분리한다.
입력기 경계는 추상적으로 두지 않고 대표 패턴으로 잠근다.
ChatGPT의 과세분화와 Gemini의 대묶음 사이에서 Codex는 중간 granularity 기준 후보를 유지한다.
