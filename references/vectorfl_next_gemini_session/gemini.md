
---

### 2) `gemini.md`

```md
# gemini.md
## VECTORFL_NEXT Gemini CLI Working Rule
### session 1: youtube_exam.md 분절 + 값 부여 연습

---

## 0. 이번 세션의 목표

이번 세션의 목표는 새 엔진을 만드는 것이 아니다.

이번 세션의 목표는 오직 하나다.

**`youtube_exam.md`를 읽고,  
3축(D/I/S) + 라벨(scene/flow) + time 값을 붙일 수 있는  
의미 맥락 최소단위(dust)로 나누는 연습을 수행하는 것.**

즉 이번 세션은:

- segmentation practice
- value assignment practice
- comparison-ready output generation

만 수행한다.

---

## 1. hard boundary

이번 세션에서 Gemini CLI는 아래를 하지 않는다.

### forbidden
- point 생성
- cluster 생성
- space 해석
- viewer 작업
- 기존 엔진 철학 재설계
- 기존 필드명 변경
- 과도한 확장
- 예쁜 요약문 만들기

이번 세션의 focus는:

**dust 분절 + D/I/S + scene/flow + time 부여**

뿐이다.

---

## 2. reference rule

기존 `vectorfl_next` 엔진은 참조 가능하다.

하지만 이번 세션의 1차 목표는 코드 수정이 아니라  
**기준 연습**이다.

즉 우선순위는:

1. `youtube_exam.md`를 dust로 나누기
2. 각 dust에 값 붙이기
3. assistant 결과와 비교 가능하게 만들기

코드 작업은 그 다음이다.

---

## 3. dust rule

dust는 문장 최소단위가 아니다.

dust는:

**하나의 지배적 의미 작용을 가진 최소 맥락 단위**

다.

dust는 아래를 만족해야 한다.

- 하나의 주된 역할이 있다
- 혼자 읽어도 역할이 보인다
- D/I/S를 붙일 수 있다
- scene/flow를 붙일 수 있다
- 더 자르면 의미 힘이 약해진다
- 더 합치면 역할이 섞인다

---

## 4. 3축 사용 규칙

### D = Direction
현재 맥락을 앞으로 밀거나 / 중립적으로 연결하거나 / 반대로 틀거나 하는 방향성

### I = Intensity
표현의 압력, 강조도, 확신도, 충격도

### S = Stability
하나의 dust로 얼마나 안정적으로 버티는가

값 범위:
- `0.00 ~ 1.00`

해석 구간:
- `0.00 ~ 0.40` : low / negative side
- `0.40 ~ 0.60` : neutral band
- `0.60 ~ 1.00` : high / positive side

주의:
낮은 값은 나쁜 값이 아니다.  
반대극 또는 약한 극이다.

---

## 5. label 사용 규칙

### scene allowed values
- `self`
- `work`
- `evidence`
- `meta`
- `unknown`

### flow allowed values
- `contract`
- `expand`
- `bridge`
- `tension`
- `unknown`

주의:
scene/flow는 정밀한 의미론이 아니라 **앵커 힌트**다.

---

## 6. time 사용 규칙

각 dust에는 반드시 time을 붙인다.

형식:
- `t01`, `t02`, `t03` ...
- 원문 timestamp가 있으면 함께 기입 가능

예:
- `time: t04 | 08:26~09:13`

---

## 7. output requirement

Gemini CLI는 각 dust마다 아래를 출력해야 한다.

```md
[dust_01]
source_range: ...
text: ...
unit_type: ...
D: ...
I: ...
S: ...
scene: ...
flow: ...
time: ...
why_one_unit:
- ...
why_this_value:
- ...
confidence: ...

## dust approval gate

Gemini CLI는 어떤 텍스트 조각도 아래 3개를 모두 통과하기 전에는 dust로 승인하지 않는다.

1. 독립 의미 작용 검사
- 이 조각이 혼자서도 하나의 지배적 역할을 가지는가
- 단순 보정, 짧은 동의, 짧은 응답, 짧은 사실 확인이면 독립 dust 승인 금지

2. 흡수 우선 검사
- 앞 dust 또는 뒤 dust에 흡수했을 때 더 자연스러운가
- 더 자연스럽다면 독립 dust로 만들지 말고 흡수한다

3. 앵커 안정성 검사
- D/I/S + scene + flow를 붙였을 때 설명력이 충분한가
- 값은 붙일 수 있지만 설명력이 약하면 dust 승인 금지

---

## forced merge rules

아래 경우는 독립 dust로 두지 말고 인접 dust에 흡수한다.

- 짧은 사실 보정 발화
- 짧은 동조/응답 발화
- 앞 문단의 반응을 한 줄 덧붙이는 발화
- 질문 1줄 + 응답 1줄처럼 너무 짧은 쌍
- 본문 의미를 만들지 못하는 짧은 연결 조각

---

## marker exclusion rule

아래는 dust가 아니라 marker로 분리한다.

- 챕터 제목
- 편집 헤더
- 타임스탬프 라벨
- 섹션 구분자

이들은 공간 입력 dust가 아니라 별도 marker metadata로 취급한다.

---

## scene decision priority

scene은 표면 단어가 아니라 문단의 기능으로 결정한다.

우선순위:
1. 이 문단이 무엇을 하고 있는가
2. 사건/사례를 말하는가 -> evidence
3. 해석/비교/역사/관점을 말하는가 -> meta
4. 실제 구현/도구/작업 방식을 말하는가 -> work
5. 자기감정/자기평가/내면인가 -> self

주의:
- 건물, 제품, 도구 같은 단어가 나와도 문단 기능이 사건 회고면 evidence 또는 meta가 우선이다
- 질문이라고 자동으로 self를 주지 않는다