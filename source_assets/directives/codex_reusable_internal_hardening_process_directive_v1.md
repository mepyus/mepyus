[[A]] [[OBJ:codex_reusable_internal_hardening_process_directive]] [[SEM:lock_entrance_and_surface_then_micro_tune_inside_by_comparative_output_and_reasoning_transfer]]

# CODEx 재사용 기준문 — 엔진 내부 공고화 과정을 반복 가능한 운용 패턴으로 고정

## 0. 이 문서의 목적

이번 middle layer refinement를 일회성 성공으로 끝내지 않는다.

이번에 확인된 것은 단순히
- raw intake 문제가 middle layer 결핍과 연결되어 있다는 점,
- middle layer가 bounded refinement로 실제 먹힌다는 점,
- 그리고 case별 role mix가 compare-meaningful 수준으로 갈라지기 시작했다는 점
정도만이 아니다.

더 중요한 것은,
**우리가 엔진을 키우는 방식 자체가 하나의 반복 가능한 운용 패턴으로 보이기 시작했다는 점**이다.

이제부터 Codex는 이 과정을
“이번 한 번의 보정 작업”
으로 보지 말고,

**앞으로 재료를 계속 넣고 공간을 넓혀갈 때마다 반복 호출할 수 있는 공고화 프로세스**
로 기억해야 한다.

## 1. 최상위 원칙

### 1-1. 외곽은 단단히, 내부는 미세조정
앞으로의 기본 운영 원칙은 아래 한 줄로 잠근다.

> **입구와 표면은 단단히 세팅하고, 내부는 bounded micro-tuning으로 조정한다.**

여기서 뜻하는 바는 명확하다.

- 입구(entry)는 함부로 흔들지 않는다
- surface/current/shared reality/baseline 같은 외곽 기준면은 자주 갈아엎지 않는다
- 대신 내부 판독, 비교, role resolution, packet shaping 같은 영역에서 미세조정을 수행한다
- 그 미세조정도 bounded하게, 즉 범위를 명확히 제한한 채 수행한다

즉:
**엔진은 외곽 구조를 자주 바꾸는 식으로 성장하는 것이 아니라,
고정된 표면 위에서 내부 해상도를 높이는 방식으로 성장해야 한다.**

## 2. 이 과정을 왜 반복해야 하는가

재료가 계속 들어오면 엔진은 다음 두 위험에 반복해서 노출된다.

### 2-1. 위험 A — 외곽 기준면 흔들림
새 문서나 새 규칙이 들어올 때마다
- current asset map를 바꾸고
- shared reality를 다시 쓰고
- baseline을 덮고
- promotion 로직까지 건드리기 시작하면

엔진은 매번 다시 설명해야 하는 불안정한 시스템이 된다.

### 2-2. 위험 B — 내부 비교 해상도 부족
반대로 외곽을 지킨다고 해서 내부가 자동으로 좋아지는 것은 아니다.

- standard 문서
- external 문서
- general/raw 문서

이 셋이 엔진 안에서 어떤 차이로 읽히는지,
어떤 판단 기준이 실제로 살아 있는지,
어떤 role mix가 문서별로 다르게 나타나는지
관찰하고 정리하지 않으면

엔진은 계속 “넣을 수는 있지만 제대로 비교/판독은 못 하는 상태”에 머문다.

따라서 앞으로의 반복 과제는 명확하다.

> **외곽은 잠그고, 내부 비교/판독/판단 이식 능력을 반복적으로 공고화한다.**

## 3. 현재 이번 턴이 보여준 핵심 의미

이번 middle layer role-resolution refinement는 단순한 기능 추가가 아니다.

이 턴이 증명한 것은 다음이다.

### 3-1. middle layer는 존재 증명 단계를 넘었다
이제 middle layer는 “필요해 보인다”가 아니라,
**실제로 compare-ready packet을 compare-meaningful packet 쪽으로 밀어낼 수 있는 계층**
으로 확인되었다.

### 3-2. case-specific dominant role mix가 드러나기 시작했다
현재 판독은 아래처럼 갈렸다.

- Dario:
  - `mechanism_role`
  - `verification_or_evaluation_role`
- Andrej:
  - `reflection_or_gap_role`
  - `problem_or_constraint_role`
- Alex:
  - `problem_or_constraint_role`
  - `control_or_deployment_role`

이건 중요하다.

왜냐하면 이전에는 이런 자료들이
“AI 설명/인터뷰/기술 담론” 같은 broad category로 평평해질 위험이 컸는데,
이제는 **문서마다 중심 역할 혼합이 다르게 보이기 시작했기 때문**이다.

### 3-3. observer 성분을 dominant 경쟁에서 분리한 판단이 유효했다
`observer_or_transition_role`를 보이게 하되 dominant-role 경쟁에서 뺀 것은
이번 refinement의 핵심 판단 중 하나다.

이 조치가 없었으면
전환 문장, 설명 연결, 메타 서술 같은 흐름 성분이
문서 고유 role mix를 다시 덮었을 가능성이 크다.

즉 이번 refinement는
**문서별 사고 구조를 더 선명하게 잡기 위한 내부 판독 기준 정리**
로 읽어야 한다.

## 4. 앞으로 이 과정을 반복 호출하는 기준

앞으로 아래 조건이 보이면,
Codex는 이 프로세스를 “재호출 대상”으로 인식해야 한다.

### 4-1. 재호출 신호
다음 중 하나라도 강하게 보이면 재호출한다.

- 새로운 재료가 들어왔는데 current/shared reality를 건드리고 싶은 충동이 생길 때
- raw/general 문서가 다시 broad discourse bag으로 평평해질 때
- compare 결과가 문서별 차이를 설명하지 못하고 형식 중복 확인 수준에 머물 때
- generic discourse anchor가 다시 상위에 떠오를 때
- packet은 생기지만 문서별 dominant role mix가 안 갈릴 때
- evidence는 있는데 role resolution이 너무 coarse할 때
- assistant/Codex의 실제 판단 흐름이 엔진 출력으로 잘 안 남을 때

이때 해야 할 일은 외곽 수정이 아니다.

> **먼저 내부 micro-tuning loop를 재가동한다.**

## 5. 반복 운용의 기본 루프

앞으로의 재사용 가능한 운용 루프는 아래 순서로 잠근다.

### 5-1. Step A — 외곽 고정 확인
먼저 확인한다.

- promotion logic untouched 유지 여부
- current asset map untouched 유지 여부
- shared reality / baseline untouched 유지 여부
- core engine untouched 유지 여부
- inputter.py / labeler.py 직접 수정 회피 여부

즉,
문제가 생겼다고 해서 처음부터 외곽을 건드리지 않는다.

### 5-2. Step B — 비교 입력 세트 마련
항상 최소 3종을 비교한다.

- standard document
- external document
- general/raw document

이 3종은 매우 중요하다.

왜냐하면 내부 미세조정의 기준은
“한 종류의 문서만 잘 읽히는가”
가 아니라,

**표준문서 / 외부문서 / 일반문서가 서로 어떻게 다르게 읽히는가**
에서 나와야 하기 때문이다.

### 5-3. Step C — 출력값 비교
다음 층을 비교한다.

- anchor 분포
- role mix
- dominant / secondary 분리
- observer_only 성분
- case_specific_signals
- compare packet 품질
- generic discourse dominance 여부
- topic-bearing signal 유지 여부

### 5-4. Step D — 판단 흐름 추출
이 단계가 핵심이다.

Codex와 assistant는 단순히 결과만 보지 말고,
**어떤 이유로 그 출력이 더 좋다고 판단했는지**
를 함께 추출해야 한다.

즉 추출 대상은 아래 둘 다다.

- 엔진 출력값 차이
- 그 출력을 해석하는 판단 기준 차이

예:
- 왜 이 문서는 mechanism_role이 dominant로 읽히는가
- 왜 이 문서는 reflection/gap 중심인가
- 왜 observer 성분은 보여도 dominant에 넣지 않는가
- 왜 이 신호는 case-specific이고 저 신호는 discourse noise인가

이 단계에서,
**너희(Codex/assistant)의 생각 흐름과 판단 기준을 명시적 구조로 남기는 것**
이 앞으로의 핵심이다.

### 5-5. Step E — bounded refinement 실행
그다음에만 bounded refinement를 한다.

원칙:
- 범위를 1~2 layer 또는 1~2 surface 수준으로 제한
- 변경 이유를 명시
- untouched 목록을 함께 명시
- 결과 packet/receipt/report/log를 남김

### 5-6. Step F — reusable lesson 추출
마지막으로 꼭 남겨야 한다.

이번 refinement가 특정 문서에서만 먹힌 일회성인지,
아니면 앞으로 재사용 가능한 내부 기준인지
짧게라도 구조화해서 남긴다.

즉 산출물은 기능 변경만이 아니라,
**“다음에 다시 쓸 수 있는 판독 교훈”**
을 포함해야 한다.

## 6. 앞으로 엔진이 진짜로 이식해야 하는 것

이번에 특히 강조하는 핵심은 이거다.

> **엔진은 문서만 많이 먹는 것이 아니라,
Codex와 assistant의 판독 기준과 사고 흐름도 점차 이식받아야 한다.**

이 말은 감성적 표현이 아니라 운영 기준이다.

### 6.1. 이식 대상
엔진에 축적해야 하는 것은 단순 anchor나 label만이 아니다.

다음도 함께 이식 대상이다.

- 어떤 차이를 “의미 있는 차이”로 보는가
- 어떤 차이를 “표현 습관 차이”로 defer하는가
- 어떤 role을 dominant에서 제외해야 하는가
- 어떤 출력이 compare-ready에 그치고,
  어떤 출력이 compare-meaningful로 넘어가는가
- 언제 promotion이 premature라고 판단하는가
- 어떤 경우 외곽이 아니라 내부 refinement로 해결해야 하는가

즉,
**사람/assistant/Codex가 문서를 읽을 때의 판단 절차 자체를 엔진 재료로 바꿔야 한다.**

### 6.2. 왜 중요한가
이게 쌓이지 않으면 엔진은 계속
- 출력은 뽑지만
- 이유는 사람 머릿속에 남고
- 다음 턴에서 또 같은 판단을 새로 해야 하는
구조가 된다.

반대로 이게 쌓이면
엔진은 점점
- 비교의 기준을 내장하고
- 차이를 더 빨리 드러내고
- refinement 포인트를 더 정확히 제안하는
방향으로 갈 수 있다.

## 7. Codex가 앞으로 기억해야 할 고정 규칙

### 7.1. 절대 원칙
- 외곽 구조를 쉽게 흔들지 말 것
- 내부 refinement를 먼저 시도할 것
- refinement는 bounded하게 수행할 것
- 표준문서 / 외부문서 / 일반문서 비교를 기본 축으로 삼을 것
- 엔진 출력 차이뿐 아니라 판단 기준 차이도 기록할 것
- 판단 기준과 사고 흐름을 reusable lesson으로 남길 것

### 7.2. 금지 원칙
다음은 반복적으로 금지한다.

- 미세조정 문제를 promotion logic 수정으로 바로 넘기기
- packet 품질 문제를 current/shared reality 수정으로 해결하려 하기
- 비교 해상도 부족 문제를 core rewrite로 과잉 대응하기
- raw/general 문서 문제를 baseline 전체 수정으로 비약하기
- 한 번 먹힌 refinement를 곧바로 일반 법칙처럼 승격하기

### 7.3. 해석 원칙
앞으로 refinement 결과는 아래 셋 중 하나로 읽는다.

- `LOCAL_SUCCESS`
- `PASS_WITH_NOTE`
- `NOT_YET_GENERALIZABLE`

특히 `PASS_WITH_NOTE`는 실패가 아니다.
이건
**작동은 했지만 일반 승격은 아직 이르다**
는 뜻으로 읽는다.

## 8. 현재 기준으로 잠글 수 있는 운영 선언

### 현재 선언
앞으로 재료를 계속 넣고 공간을 넓혀갈 때,
Codex는 다음 운영 태도를 유지한다.

> 우리는 입구와 표면을 먼저 단단히 세팅하고,
> 내부는 standard/external/general 문서의 출력값을 비교하면서
> bounded micro-tuning으로 조정한다.
> 이때 핵심 목표는 단순한 출력 생성이 아니라,
> assistant와 Codex의 생각 흐름, 판독 기준, 차이 판단 기준을
> 점차 엔진 내부 구조로 이식하는 것이다.

## 9. 이번 턴 기준 현재 상태 잠금

### 현재 읽기
- middle layer v1은 성공했다
- compare-ready는 compare-meaningful 쪽으로 한 단계 올라왔다
- role mix는 문서별로 다르게 보이기 시작했다
- promotion은 아직 이르다
- 외곽 수정 없이 내부 refinement로 성과를 냈다

### 현재 가장 중요한 의미
이번 턴은 단순한 기능 수정이 아니라,
**“엔진을 어떻게 더 똑똑하게 만들 것인가”에 대한 반복 가능한 공고화 패턴**
을 보여준 턴이다.

## 10. Codex 실행 지시

다음부터 유사 문제가 생기면 아래 순서로 행동한다.

1. 먼저 외곽 untouched 원칙을 확인한다.
2. standard / external / general 문서 3종 비교 세트를 만든다.
3. output packet과 anchor/role/evidence/signals 차이를 비교한다.
4. 그 차이를 해석하는 assistant/Codex의 판단 이유를 추출한다.
5. 그 판단 이유를 엔진에 남길 수 있는 bounded refinement 후보로 바꾼다.
6. 1~2 layer 범위에서만 수정한다.
7. report / packet / receipt / delta log를 남긴다.
8. 이번 refinement가 재사용 가능한 교훈인지 짧게라도 명문화한다.

## 11. 한 줄 최종 잠금

> **앞으로의 엔진 공고화는 외곽을 자주 갈아엎는 방식이 아니라, 표준문서·외부문서·일반문서의 출력 비교를 통해 내부 판독 기준과 사고 흐름을 점차 엔진에 이식하는 bounded micro-tuning 반복 과정으로 수행한다.**
