# compare candidate enrichment contract discussion memo v1

## 1. verdict

현재 `compare candidate enrichment` 논의에서
가장 핵심적인 contract discussion surface는
**compare model**이다.

이 memo의 목적은
contract를 어떻게 바꿀지 쓰는 것이 아니라,
다음 계약 논의를 **어디를 중심으로 해야 하는지**를 좁혀 판정하는 데 있다.

## 2. codex alignment note

- 감독관의 “다음은 contract discussion memo v1이다” 판단에 동의한다.
- 지금은 contract를 설계할 단계가 아니라, compare candidate thin relation의 origin과 가장 가까운 discussion surface를 먼저 좁혀야 한다.
- 나는 세 표면 중 `compare model`이 가장 핵심이라고 본다.
- 이유는 current thinness가 UI나 adapter보다 compare candidate relation을 생성하는 모델의 flatness와 더 직접적으로 연결되기 때문이다.
- resolution:
  - 이번 memo에서는 compare model을 primary surface로 두고
  - payload shaping은 보조, adapter mediation은 비중심 surface로 정리한다.

## 3. memo purpose

왜 이 memo가 필요한가:

- contract discussion pre-note에서
  논의 가능한 표면을
  - compare model
  - payload shaping
  - adapter mediation
  로 잘라 두었다
- 하지만 아직 이 셋 중 어디가 핵심인지 정하지 않으면
  다음 단계에서 contract 논의가 쉽게 퍼질 수 있다

즉 이번 memo의 핵심은:
- thin relation과 가장 직접적으로 연결된 표면을 찾고
- 그 표면을 중심으로만 다음 discussion을 준비하게 만드는 것이다

## 4. discussion surface comparison

### 4-1. compare model

#### current thinness와의 직접성

- 가장 높다

#### 왜 핵심 surface일 수 있는가

- natural live observation에서 보인 thin relation은
  compare candidate가 “있다”는 사실은 말하지만
  관계 두께는 거의 주지 못하는 상태였다
- engine-origin mapping도
  current compare model flatness를 주요 origin으로 읽었다

#### 왜 보조 surface일 수도 있는가

- compare model만 본다고 해서
  payload로 나올 때의 flattening이나 adapter mediation을 완전히 설명할 수는 없다

### 4-2. payload shaping

#### current thinness와의 직접성

- 중간 수준

#### 왜 핵심 surface일 수 있는가

- compare model에 relation hint 가능성이 있더라도
  payload에서 너무 flat하게 shaping되면
  UI에선 여전히 thin하게 읽힐 수 있다

#### 왜 보조 surface일 수 있는가

- 현재까지의 reading에서는
  thinness의 핵심이 payload suppression보다는
  compare model 자체의 flatness에 더 가까웠다

### 4-3. adapter mediation

#### current thinness와의 직접성

- 가장 낮다

#### 왜 핵심 surface일 수 있는가

- first-pass untouched 원칙 때문에
  adapter가 thinness를 거의 그대로 전달하고 있다는 점은 맞다

#### 왜 보조 surface일 수 있는가

- adapter는 origin보다 mediation layer다
- 여기서 문제를 정의하면
  origin layer의 구조적 thinness를 전달 계층 문제로 오인할 위험이 있다

## 5. primary vs secondary surface

### primary discussion surface

- **compare model**

이유:
- current compare candidate thin relation과 가장 직접적으로 연결된다
- future enrichment candidate를 말하더라도
  가장 먼저 좁혀야 할 질문은
  “compare candidate relation을 현재 모델이 얼마나 flat하게 만들고 있는가”다

### secondary supporting surface

- **payload shaping**

이유:
- compare model에서 생성된 정보가 payload surface에서
  얼마나 눌리거나 평평해지는지 보는 보조 축으로 의미가 있다

### why adapter mediation is not central now

- adapter는 current thinness를 전달하는 경계이긴 하지만
  origin 자체는 아니다
- 이번 단계에서 adapter를 중심 discussion surface로 올리면
  mediation layer를 문제의 본체처럼 읽게 될 위험이 크다

## 6. why not concrete contract yet

### 1. discussion surface 판정과 concrete contract 설계는 다른 단계다

- 지금은 어디를 중심으로 논의해야 하는지 정하는 단계지,
  무엇을 어떻게 바꿀지 정하는 단계가 아니다

### 2. concrete contract는 scope inflation을 빠르게 부른다

- compare model을 중심으로 보려던 것이
  곧바로 field, branch, schema 논의로 커질 수 있다

### 3. 아직 contract shape보다 origin reading이 우선이다

- current thinness의 핵심이 compare model인지, payload shaping인지,
  그 위계가 더 중요하다

## 7. risk note

primary surface를 잘못 잡았을 때 생길 수 있는 리스크:

### 1. mediation layer를 origin으로 오인

- adapter를 중심에 두면
  compare model flatness라는 구조 문제를
  단순 전달 문제처럼 읽을 수 있다

### 2. payload suppression과 model flatness를 혼동

- payload shaping을 primary로 놓으면
  실제 구조적 얇음보다 formatting/flattening 문제로 오해할 수 있다

### 3. UI need를 곧바로 contract shape로 번역

- “UI가 더 두껍게 읽히면 좋겠다”는 요구를
  곧바로 contract 설계로 바꾸면
  recommendation/workflow 쪽 inflation이 빨라질 수 있다

## 8. next-step gate

판정:
- **contract proposal readiness note**

이유:
- discussion surface 판정은 이제 충분히 좁혀졌다
- 다음 단계는 concrete contract proposal이 아니라,
  compare model 중심으로 contract proposal에 들어갈 준비가 되었는지
  다시 한 번 readiness 수준에서 확인하는 것이 맞다

## 9. board grounding separation

이번 memo에서도 board grounding은 compare 트랙 discussion surface와 합치지 않는다.

- board grounding absence는 여전히 existing signal reuse와 surface suppression 경계 문제에 가깝다
- compare candidate thin relation은 current compare model flatness와 더 직접적으로 연결된다
- 따라서 discussion surface memo도 compare candidate 트랙 내부에서만 유지하는 것이 맞다
