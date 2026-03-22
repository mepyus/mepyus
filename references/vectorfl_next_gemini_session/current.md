
---

### 3) `current.md`

```md
# current.md
## current task
### youtube_exam.md 1차 분절 + 값 부여 비교 실험

---

## 0. 이번 턴의 목적

이번 턴의 목적은 구현이 아니다.

이번 턴의 목적은 오직 하나다.

**`youtube_exam.md`를  
assistant와 gemini가 각각  
동일한 기준(3축 + 라벨기 + 시간축)으로 나누고 값을 붙이게 해서  
그 결과를 사람이 직접 비교할 수 있게 만드는 것.**

즉 지금은:

- dust 최소단위 확인
- 값 부여 기준 확인
- 비교 가능한 출력 확보

여기까지만 한다.

---

## 1. 입력 파일

이번 턴의 입력 파일은 아래 하나로 고정한다.

- `youtube_exam.md`

다른 파일은 보지 않는다.

---

## 2. 이번 턴의 작업

### task 1
`youtube_exam.md`를 의미 맥락 최소단위(dust)로 분절한다.

### task 2
각 dust에 아래 값을 부여한다.

- `D`
- `I`
- `S`
- `scene`
- `flow`
- `time`

### task 3
각 dust에 아래 설명을 짧게 붙인다.

- `why_one_unit`
- `why_this_value`

### task 4
assistant 결과와 비교 가능하도록  
출력 형식을 고정한다.

---

## 3. dust 판정 기준

dust는 문장 최소단위가 아니다.

dust는:

**3축 + 라벨기 + 시간축 값을 붙일 수 있는 의미 맥락 최소단위**

다.

판정 기준:
- 하나의 지배적 의미 작용이 있는가
- D/I/S를 붙일 수 있는가
- scene/flow를 붙일 수 있는가
- 더 자르면 의미 힘이 약해지는가
- 더 합치면 역할이 섞이는가

---

## 4. 값 부여 기준

### D
현재 화제/논리를 밀어주는 방향성인가, 연결하는가, 반대로 트는가

### I
강도, 강조, 확신, 압력, 충격의 크기

### S
하나의 dust로 버티는 안정도

### scene
- self
- work
- evidence
- meta
- unknown

### flow
- contract
- expand
- bridge
- tension
- unknown

### time
- `t01`, `t02`, `t03` ...
- timestamp가 있으면 병기 가능

---

## 5. 출력 형식

이번 턴의 출력은 아래 형식으로 고정한다.

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
merge_history:
- absorbed dust_02
- absorbed dust_04
confidence: ...

[excluded_marker_01]
source_range: ...
text: ...
reason:
- chapter header

## revised work order

1. youtube_exam.md를 1차 provisional dust로 분절한다
2. 각 provisional dust에 D/I/S + scene/flow + time을 임시 부여한다
3. 그 다음 반드시 merge pass를 수행한다
4. merge pass에서 아래를 점검한다
   - 짧은 보정 발화는 흡수할 것
   - 짧은 응답/동조는 흡수할 것
   - marker는 제거할 것
   - scene/flow가 기능 기준으로 붙었는지 재검토할 것
5. 최종 dust만 출력한다
6. 별도로 아래를 함께 출력한다
   - merged_into
   - excluded_as_marker
   - merge_reason