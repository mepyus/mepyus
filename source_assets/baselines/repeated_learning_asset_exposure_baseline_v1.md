[[A]] [[OBJ:codex_baseline_repeated_learning_asset_exposure_v1]] [[SEM:codex_learns_operating_philosophy_by_repeated_reference_not_one_shot_instruction]]

# CODEx 기준문 — 반복 학습 자산 노출로 운용 철학을 체득시키는 기준

## 0. 목적

이 기준문의 목적은 간단하다.

> **Codex는 한 번의 설명으로 우리의 철학과 운용 방식을 완전히 체득하지 못한다.
> 따라서 앞으로는 기준문/지시서/예시서/리뷰 리포트 같은 명시적 학습 자산을 반복적으로 노출하여,
> 같은 철학을 여러 각도에서 계속 참조하게 만들어야 한다.**

즉 이 문서는
- 이번 한 턴의 실행 지시서가 아니라
- 앞으로 Codex를 어떻게 학습시키며 같이 갈 것인가에 대한
상위 운영 기준이다.

---

## 1. 최상위 선언

우리는 Codex를
단순 명령 실행기로만 쓰지 않는다.

우리는 Codex가
- 엔진의 철학
- 연결의 의미
- 사용자 층위 번역
- 외곽 고정 / 내부 미세조정
- premature generalization 보류
- reasoning residue 기록
같은 운용 감각을
점차 반복적으로 체득하도록 만들어야 한다.

따라서 앞으로의 기본 원칙은 아래다.

> **Codex에게 중요한 운영 원칙은 한 번 설명하고 끝내지 않는다.
> 반복 가능한 학습 자산으로 남기고, 여러 턴에 걸쳐 다시 참조하게 하며,
> 서로 다른 사례 위에서 같은 철학을 반복 노출하여 몸에 익히게 만든다.**

---

## 2. 왜 이 기준이 필요한가

## 2-1. 사람과 Codex의 차이
사용자는 이미 방향과 감각을 어느 정도 몸으로 알고 있다.
그래서 짧은 표현만으로도 이전 맥락을 다시 불러올 수 있다.

하지만 Codex는 다르다.

Codex는
- 이번 턴의 지시를 실행할 수는 있어도
- 그 지시가 어느 철학 아래 있는지
- 왜 어떤 수정은 보류되고 어떤 수정은 허용되는지
- 왜 예시 하나를 일반 법칙으로 잠그면 안 되는지
를 한 번에 깊게 체득하지 못할 수 있다.

따라서 필요한 것은
더 긴 설명이 아니라
**더 반복적인 참조 구조**다.

## 2-2. 한 번의 설명은 쉽게 사라진다
특히 철학/운용 규칙은
실행 결과와 달리 눈에 바로 보이는 산출물이 아니기 때문에
한 번의 대화로만 전달하면 쉽게 흐려진다.

따라서 철학은 반드시
- 문서화되고
- 반복 참조되며
- 서로 다른 실행 사례에 다시 연결되어야 한다.

---

## 3. Codex 학습의 기본 관점

앞으로 Codex 학습은 아래처럼 본다.

### 3-1. 일회성 설명이 아니라 반복 노출
하나의 철학은
- 기준문에서 선언되고
- 지시서에서 실행 규칙으로 구체화되고
- 예시서에서 적용 감각을 보여주고
- 리뷰 리포트에서 결과와 판단 이유를 다시 되짚는 방식으로
반복 노출되어야 한다.

### 3-2. 실행 결과만이 아니라 판단 이유도 같이 남긴다
Codex가 진짜로 배워야 하는 것은
단순 output pattern만이 아니다.

아래도 함께 학습해야 한다.

- 왜 이걸 지금 수정하지 않았는가
- 왜 이건 HOLD인가
- 왜 이건 PASS_WITH_NOTE인가
- 왜 residue를 바로 지우지 않고 후순위 후보로 봤는가
- 왜 axis를 안 건드리고 surface만 조율했는가

즉
**행동 결과와 판단 기준이 함께 자산화되어야 한다.**

### 3-3. 같은 철학을 여러 사례에 반복 적용한다
철학은 한 사례에만 걸리면 약하다.

따라서 같은 원칙을
- `AI의 미래`
- `ontology / vectorfl / 연결`
- interview residue
- summary-stage deprioritization
같은 다른 사례에 반복 적용해
Codex가 “형태는 달라도 원칙은 같다”는 것을 익히게 해야 한다.

---

## 4. 앞으로 Codex에게 반복 노출해야 하는 학습 자산 종류

## 4-1. baseline
역할:
- 절대 기준면
- 상위 철학 잠금
- 실행 전 먼저 통과해야 하는 원칙

예:
- connection meaning
- user-layer translation
- outer-layer lock
- repeated hardening pattern
- future scaling guardrails

## 4-2. directive
역할:
- 이번 턴에서 실제로 무엇을 하고 무엇을 하지 않는지 명확히 제한
- baseline을 실행 규칙으로 번역

즉 directive는
**철학을 실행 가능한 범위로 잘라주는 문서**다.

## 4-3. example
역할:
- 같은 철학이 실제로 어떻게 적용되는지 보여줌
- Codex가 추상 기준을 실제 장면과 연결하게 도와줌

즉 example은
**철학의 감각을 몸에 익히게 하는 자산**이다.

## 4-4. review/report
역할:
- 실제 실행 결과가 철학과 맞았는지 되짚음
- 무엇이 잘 먹혔고 무엇이 premature였는지 기록
- judgment residue를 남김

즉 review/report는
**Codex가 왜 그런 판정을 받았는지 다시 학습하는 복기 자산**이다.

---

## 5. Codex 학습 루프

앞으로 Codex 학습은 아래 루프로 반복한다.

### Step 1. baseline으로 철학을 잠근다
먼저 상위 기준을 선언한다.

예:
- 연결은 공출현이 아니라 의미 운동
- 층위는 engine label이 아니라 사용자 질문의 펼쳐짐
- 수정 전에 철학 기준을 다시 확인
- generalization은 늦춘다

### Step 2. directive로 bounded task를 만든다
그다음
이번 턴에서 할 일 / 하지 말 일을 분명히 자른다.

예:
- axis untouched
- gloss stability check only
- residue review only
- summary-stage deprioritization candidate review only

### Step 3. example로 적용 감각을 심는다
같은 철학이 실제 케이스에서 어떻게 작동하는지 보여준다.

예:
- `AI의 미래`
- `장미`
- `ontology/vectorfl`
- interview residue

### Step 4. review/report로 결과와 판단 이유를 남긴다
실행 후에는
- 무엇이 먹혔는지
- 왜 PASS_WITH_NOTE인지
- 무엇을 아직 잠그면 안 되는지
를 반드시 남긴다.

### Step 5. 다음 턴에서 다시 참조한다
중요:
문서를 만들고 끝내지 않는다.

다음 턴에서
- baseline을 다시 통과시키고
- directive를 그 위에 얹고
- example을 다시 보여주고
- report를 다시 읽게 한다

즉
**학습 자산은 저장용이 아니라 반복 호출용**이다.

---

## 6. Codex에게 특히 반복 학습시켜야 하는 것

### 6-1. 외곽 고정 / 내부 미세조정
- outer layer를 쉽게 흔들지 않는다
- 내부에서 bounded하게 조율한다
- 다만 outer layer는 sacred가 아니라 evidence-gated다

### 6-2. PASS_WITH_NOTE / HOLD discipline
- local success를 바로 일반화하지 않는다
- candidate / hold / note를 유지한다
- negative control과 failure axis를 본다

### 6.3. user-layer translation
- engine label이 최종 의미가 아니다
- 사용자 질문의 층위를 열어주는 표면이 중요하다
- gloss와 summary는 그 번역을 돕는 수단이다

### 6-4. reasoning residue
- output만 쌓지 않는다
- 왜 그렇게 읽었는지의 판단 흔적도 남긴다

### 6-5. exploration topic as reusable object
- `AI의 미래` 같은 탐색은 일회성 결과가 아니다
- 하나의 객체/응결핵 주변에 의미 층위를 계속 붙이는 축적 과정이다
- 나중에 page, live_input, OS-level memo layer의 시작점이 될 수 있다

---

## 7. 예시 하나로 끝내지 않는 이유

예시 하나만 있으면 Codex는 그 예시 모양만 따라갈 위험이 있다.

따라서 우리는
- 같은 철학을 여러 문장으로 다시 쓰고
- 다른 사례에 반복 적용하고
- 예시서도 여러 장 만들고
- 리뷰 리포트로 반복 교정해야 한다.

즉 앞으로는
“한 번 잘 설명했으니 이해했겠지”
가 아니라

> **같은 철학을 여러 자산으로, 여러 사례 위에서, 여러 번 참조하게 만들어
> 점차 내부화되게 한다**
를 기본 원칙으로 삼는다.

---

## 8. Codex가 앞으로 잊지 말아야 할 것

### 절대 기억할 것
- 한 번의 설명은 충분하지 않다
- 명시적 학습 자산이 반복적으로 필요하다
- baseline / directive / example / review는 서로 다른 역할을 가진다
- 실행 결과보다 철학과 판단 기준도 같이 배워야 한다
- 철학/운용 대화는 build material이다
- 탐색 주제는 미래의 시작점이 될 수 있는 객체로 계속 두꺼워진다

### 금지할 것
- 한 번 설명한 철학이 이미 체득됐다고 가정하기
- 예시 하나를 일반 법칙처럼 취급하기
- output만 남기고 판단 이유를 버리기
- 리뷰 없이 다음 수정으로 바로 넘어가기
- 철학/운용 대화를 일회성 채팅으로 소비하기

---

## 9. 운영 해석

앞으로 우리는 Codex를 이렇게 다룬다.

> Codex는 아직 매번 참조가 필요하다.
> 따라서 중요한 철학과 운용 규칙은 반복 가능한 문서 자산으로 남기고,
> 서로 다른 사례와 실행 결과에 계속 다시 연결해 주어야 한다.
> 그래야 Codex가 단순 명령 수행을 넘어,
> 우리의 운영 감각을 점차 체득할 수 있다.

---

## 10. 한 줄 최종 잠금

> **앞으로 Codex 학습은 일회성 설명이 아니라, baseline·directive·example·review 자산을 반복적으로 참조시키는 방식으로 수행하며, 철학과 판단 기준까지 함께 축적·재노출하여 운영 감각을 점차 체득시키는 것을 원칙으로 한다.**
