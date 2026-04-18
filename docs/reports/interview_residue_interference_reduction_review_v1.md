# interview_residue_interference_reduction_review_v1.md

## 1. review target

- primary:
  - `app/work/archive_review/interview_support/middle_layer_experiments/generated/middle_layer_interview_probe_20260328T002752Z.json`
  - `app/work/archive_review/probe_support/concept_segment_probe/generated/interview_future_probe_v1_20260328T003707Z.json`
- supporting:
  - `inputs/external_cases/dario_amodei_youtube.txt`
  - `inputs/external_cases/andrej_karpathy_youtube.txt`
  - `inputs/external_cases/alexkarp_youtube.txt`

이번 턴은 suppression patch가 아니라
interview류 residue를 더 정밀하게 분해하는 review 턴이다.

---

## 2. key finding

문제는 단순히 discourse term이 많다는 것이 아니다.

interview류에서는 아래가 겹쳐서 user-layer translation을 방해한다.

- discourse connective residue
- generic abstraction residue
- quasi-topic residue
- observer/transition residue
- 일부 speaker/source residue

즉 지금 간섭은 한 종류의 noise가 아니라,
**서로 다른 residue가 다른 위치에서 다른 방식으로 summary를 흐리게 만드는 구조**
다.

---

## 3. residue vocabulary draft

이번 턴에서는 hard rule로 잠그지 않고,
아래 review vocabulary로 본다.

### 3-1. discourse_connective_residue
예:
- `우리가`
- `하지만`
- `그리고`
- `겁니다`
- `있습니다`

특징:
- 발화 연결과 강조를 담당한다
- anchor 경쟁 상위에 계속 올라온다
- topic-bearing signal 자체를 없애지는 않지만,
  user-facing summary의 선명도를 크게 낮춘다

### 3-2. speaker_or_source_residue
예:
- `CEO`
- `Highlights`
- 화자명 / source-specific proper noun

특징:
- source identity 흔적 자체는 필요할 수 있다
- 하지만 topic-bearing signal처럼 summary 앞에 나오면 번역을 흐린다
- 따라서 완전 제거 대상이 아니라, 후순위 처리 검토 대상이다

### 3-3. conversational_filler_residue
예:
- `말입니다`
- `볼까요`
- `저는`
- `제가`

특징:
- 구어체 인터뷰에서 자연스럽게 반복된다
- 의미 운동을 직접 열지 못한다
- summary 단계에서 남으면 engine wording을 강하게 만든다

### 3-4. generic_abstraction_residue
예:
- `모델이`
- `완벽히`
- `수많은`
- `기술적`

특징:
- topic-like하게 보이지만 너무 일반적이다
- role gloss는 유지해도 user-layer hint를 열어 주지는 못한다
- interview packet의 `case_specific_signal`을 흐리는 대표 패턴이다

### 3-5. quasi_topic_residue
예:
- `LRM`
- `Sector`

특징:
- topic처럼 보이지만 사용자 층위 힌트로는 너무 좁거나 맥락 의존적이다
- raw signal로는 유의미할 수 있어도,
  user-facing summary 첫 줄에 바로 나오면 방해가 된다

### 3-6. observer_transition_residue
예:
- `Opening`
- `챕터`
- `질문 하나`
- `본격적인 대담에 앞서`

특징:
- 발화 구조 전환에는 유용하다
- 하지만 user-layer translation에는 직접 기여하지 않는다
- observer-only 후보에 가깝다

---

## 4. where interference happens

## 4-1. anchor extraction stage
여기서는 residue가 아직 제거되지 않는다.

문제:
- interview 텍스트의 발화체 반복이 토큰으로 잘 살아남는다
- 그래서 `우리가`, `하지만`, `겁니다` 같은 값이 mass를 크게 차지한다

해석:
- extraction의 실패라기보다, 인터뷰 형식의 자연스러운 결과다
- 따라서 바로 hard delete로 가면 안 된다

## 4-2. anchor bucket stage
여기서 residue는 이미 일부 분리되지만,
여전히 bucket 내부 질감 차이가 남아 있다.

예:
- discourse residue 안에서도
  - 단순 접속어
  - filler
  - observer transition
  가 섞여 있다
- core topic 안에서도
  - 진짜 topic-bearing signal
  - generic abstraction residue
  - quasi-topic residue
  가 섞여 있다

즉 이번 review의 핵심은 바로 이 지점이다.

## 4-3. opening summary stage
concept probe에서는 여기서 비교적 안정적이다.

하지만 interview-only probe에서는
- Dario
- Alex
둘 다 `명확한 사용자 층위 힌트 없음`으로 읽힌다.

즉 interview류는 broad theme hint가 약하면
summary가 여전히 잘 안 열린다.

## 4-4. user-facing summary stage
middle-layer packet에서는 여기서 가장 큰 간섭이 보인다.

예:
- Dario:
  - `모델이, 완벽히, 수많은, 기술적`
- Andrej:
  - `LRM, 봅니다, 아닙니다, 인간은`
- Alex:
  - `Sector, 그들은, 초하지만, 실제로`

문제:
- role gloss는 좋다
- 하지만 case-specific signal에 residue가 너무 많이 섞여
  user-layer opening이 다시 약해진다

즉:
**가장 실제적인 간섭 위치는 user-facing summary 생성 단계**
다.

---

## 5. case-by-case interference

## 5-1. Dario

### 실제 topic-bearing signal
- scaling / compute / training / verification 쪽

### 가리는 residue
- discourse_connective:
  - `우리가`, `하지만`, `있습니다`
- generic_abstraction:
  - `모델이`, `완벽히`, `수많은`, `기술적`
- conversational_filler:
  - `말입니다`, `봅니다`

### 간섭 방식
- role은 `mechanism + verification`로 잘 보이는데
- case-specific signal이 너무 일반 추상어로 밀려
  사용자가 다음 질문을 떠올리기 어렵다

## 5-2. Andrej

### 실제 topic-bearing signal
- reflection / RL / gap / human comparison 쪽

### 가리는 residue
- discourse_connective:
  - `우리가`, `하지만`, `겁니다`
- quasi_topic:
  - `LRM`
- conversational_filler:
  - `봅니다`
- generic abstraction:
  - `있다는`, `아니라`

### 간섭 방식
- role mix는 잘 산다
- 하지만 summary signal에서 `LRM`과 발화 습관어가 사용자 층위보다 먼저 보인다

## 5-3. Alex

### 실제 topic-bearing signal
- deployment / control / security / national-scale operation 쪽

### 가리는 residue
- discourse_connective:
  - `우리가`, `그리고`, `겁니다`
- speaker/source residue:
  - `Highlights`, `CEO`
- quasi_topic:
  - `Sector`
- conversational / generic:
  - `그들은`, `실제로`

### 간섭 방식
- `문제/제약 + 운영/배치` role은 잘 보인다
- 하지만 front summary에 quasi-topic과 conversational residue가 섞여
  사용자 층위 힌트가 약해진다

---

## 6. what should not be suppressed

무조건 억제하면 안 되는 값도 있다.

### do-not-suppress candidate
- `security`
- `verification`
- `deployment`
- `automation`
- `통제`
- `운영`
- `검증`
- `신뢰`
- `안보`

이 값들은 residue와 함께 나타나도
실제 user-layer opening에 기여한다.

### borderline candidate
- `model`
- `structure`
- `future`
- `sector`
- `LRM`

이들은 맥락에 따라
- topic-bearing signal일 수도 있고
- quasi-topic residue일 수도 있다

따라서 이번 턴에서는 억제 확정이 아니라
**context-sensitive review 대상**
으로만 둔다.

---

## 7. provisional candidates only

이번 턴은 suppression을 실행하지 않는다.
대신 아래 후보만 남긴다.

### provisional down-weight candidate
- `우리가`
- `하지만`
- `그리고`
- `겁니다`
- `있습니다`
- `봅니다`
- `말입니다`

### observer-only candidate
- `챕터`
- `Opening`
- `Highlights`
- `질문 하나`

### summary deprioritization candidate
- `모델이`
- `완벽히`
- `수많은`
- `기술적`
- `그들은`
- `실제로`
- `있다는`
- `아니라`

### do-not-suppress candidate
- `verification`
- `deployment`
- `security`
- `검증`
- `통제`
- `운영`
- `안보`

---

## 8. next bounded step

다음 단계는 아래 쪽이 맞다.

- interview summary 생성 단계에서
  - generic abstraction residue
  - quasi-topic residue
  - conversational filler
  를 후순위 처리하는 bounded suppression review

아직 하지 말아야 할 것:
- hard delete
- axis change
- broad concept probe 재설계
- lexicon thickening

---

## 9. final judgment

- status: `PASS`

한 줄로 요약하면:

- interview류 residue는 하나의 noise가 아니라 `discourse connective / generic abstraction / quasi-topic / observer transition`이 각기 다른 위치에서 번역을 흐리는 구조로 보이며, 다음 step은 suppression 실행이 아니라 summary-stage 후보 억제 검토로 가는 것이 맞다.
