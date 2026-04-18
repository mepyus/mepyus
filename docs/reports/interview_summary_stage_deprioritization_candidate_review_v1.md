# interview_summary_stage_deprioritization_candidate_review_v1.md

## 1. purpose

이 문서는 suppression 실행 문서가 아니다.

직전 residue review와
`example_connection_translation_first_refinement_v1` 예시서를 학습 기준으로 삼아,
다음 bounded step을
**summary-stage deprioritization candidate review**
로 정리하는 문서다.

즉 이번 단계의 목적은
- 지우기
- hard rule 확정
- axis 변경
이 아니라,

**interview류 summary에서 무엇을 뒤로 밀면 user-layer opening이 더 잘 살아날지 후보를 정리하는 것**
이다.

---

## 2. why this is the right next step

예시서 기준으로 보면,
지금 바로 해야 하는 것은 구조 패치가 아니다.

먼저 물어야 하는 것은 아래다.

- 우리는 무엇을 연결하려는가
- 그 연결은 사용자에게 어떤 의미 층위를 열어줘야 하는가
- 현재 출력은 왜 그 질문을 충분히 못 열어주는가

현재 interview류에서 이미 보이는 것은 아래다.

- role gloss는 살아 있다
- dominant role mix도 갈린다
- 하지만 summary 첫 표면에서 residue가 사용자 층위 열림을 막는다

즉 다음 step은
hard suppression보다 먼저
**summary-stage candidate deprioritization**
이 맞다.

---

## 3. per-case deprioritization candidates

## 3-1. Dario

### keep high
- scaling
- compute
- training
- verification
- AGI timeline / acceleration

### deprioritize in summary first
- `모델이`
- `완벽히`
- `수많은`
- `기술적`
- `봅니다`
- `말입니다`

### reason
- role gloss는 `핵심 메커니즘 + 검증/평가`로 충분히 좋다
- 문제는 summary가 일반 추상어와 구어체로 다시 탁해지는 것이다

## 3-2. Andrej

### keep high
- reflection / gap
- RL
- human comparison
- cognition / limitation

### deprioritize in summary first
- `LRM`
- `봅니다`
- `아닙니다`
- `있다는`
- `아니라`

### reason
- `LRM`은 raw signal로는 유의미할 수 있지만
  user-layer summary 첫 줄에서는 설명을 더 닫는다
- 발화 습관형 표현도 user-layer opening을 흐린다

## 3-3. Alex

### keep high
- deployment
- control
- security
- national / industrial operation

### deprioritize in summary first
- `Sector`
- `그들은`
- `실제로`
- `초하지만`
- `제대로`

### reason
- `문제/제약 + 운영/배치` role은 이미 잘 보인다
- 그런데 summary 앞단에서 quasi-topic과 conversational residue가 앞에 튄다

---

## 4. cross-case candidate classes

### class A. conversational deprioritization candidate
- `봅니다`
- `말입니다`
- `그들은`
- `실제로`
- `아닙니다`

### class B. generic abstraction deprioritization candidate
- `모델이`
- `완벽히`
- `수많은`
- `기술적`
- `있다는`

### class C. quasi-topic deprioritization candidate
- `LRM`
- `Sector`

### class D. keep-high do-not-push-down
- `verification`
- `deployment`
- `security`
- `검증`
- `통제`
- `운영`
- `안보`
- `scaling`
- `AGI`

---

## 5. what to do next

다음 bounded step은 아래 쪽이 맞다.

1. summary-stage만 한정해서
2. 위 deprioritization candidate를 후보로 보고
3. role gloss와 user-layer opening이 더 잘 살아나는지 읽어본다
4. hard suppression은 아직 하지 않는다

즉 다음 수정은 있어도
- extraction stage
- axis
- core engine
가 아니라
**summary rendering 우선순위**
쪽이어야 한다.

---

## 6. what stays untouched

- axis values
- scene/flow 체계
- role taxonomy
- core engine
- broad concept probe logic
- dictionary / encyclopedia thickening

---

## 7. one-line result

- 예시서를 학습 기준으로 삼아 보면, 다음 단계는 residue를 지우는 것이 아니라 interview summary에서 무엇을 뒤로 밀어야 사용자 층위 열림이 더 살아나는지 보는 bounded deprioritization review가 맞다.
