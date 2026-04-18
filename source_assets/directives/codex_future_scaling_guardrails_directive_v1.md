[[A]] [[OBJ:codex_future_scaling_guardrails_directive]] [[SEM:judgment_versioning_reasoning_residue_generalization_discipline_failure_axis]]

# CODEx 지시서 — 다음 성장 단계에서 반드시 잠가야 할 운영 경계선

## 0. 목적

이번 턴의 목적은 새 기능을 크게 추가하는 것이 아니다.

현재 엔진은
- source / current / delta / receipt / raw log 분리,
- external-case intake,
- middle layer bounded refinement,
- reusable internal hardening pattern

까지는 꽤 잘 잠겨 있다.

하지만 앞으로 재료가 더 늘고 비교 축이 더 많아질수록,
지금의 강점이 그대로 약점으로 뒤집힐 수 있는 지점이 보인다.

따라서 이번 턴의 목표는 아래 5개를
**향후 scaling 단계의 운영 경계선**
으로 명시적으로 잠그는 것이다.

1. 판단 기준 버전 관리
2. premature generalization 억제
3. reasoning residue 별도 층 확보
4. outer-layer lock의 evidence-gated 해석
5. failure / negative-control 비교 축 확장

이 문서는
“잘 되고 있으니 계속 간다”
가 아니라,

**지금 잘 되는 구조가 커질 때도 무너지지 않도록, 미리 운영상 주의점을 기준으로 승격하는 문서**
로 읽어야 한다.

## 1. 최상위 선언

앞으로 엔진 공고화는 단순히 출력 기록을 많이 남기는 방향으로만 가면 안 된다.

> **출력 기록의 풍부함과 별개로, 판단 기준의 변화 이력과 reasoning residue를 같이 구조화하지 않으면 엔진은 성장할수록 결과는 쌓이는데 판단은 사람 바깥에 남는 시스템이 된다.**

따라서 앞으로의 공고화는
- 결과를 남기는 것
- 기준을 남기는 것
- 기준이 왜 바뀌었는지를 남기는 것
을 함께 포함해야 한다.

## 2. 경계선 1 — 판단 기준 버전 관리층 추가

## 2-1. 현재 취약점
지금은 아래는 잘 남는다.

- 무엇을 반영했는가
- 어디에 연결했는가
- 최근 변화는 무엇인가
- 실행 흔적은 있었는가

하지만 아래는 상대적으로 약하다.

- 왜 어떤 신호를 dominant로 보았는가
- 왜 어떤 역할을 secondary로 내렸는가
- 왜 observer_only로 미루었는가
- 왜 promotion이 premature라고 판단되었는가
- 왜 어떤 차이는 의미 있고 어떤 차이는 noise라고 본 것인가

즉 현재는 **output history는 두껍지만 judgment history는 얇다.**

## 2-2. 앞으로 잠글 원칙
앞으로 refinement가 발생할 때마다,
단순 결과 리포트와 별도로
**judgment criteria versioning 관점**
을 반드시 남긴다.

반드시 남겨야 하는 질문:
- 이번 판정 기준은 이전과 무엇이 같고 무엇이 달라졌는가
- role 판정 기준이 바뀌었다면 그 이유는 무엇인가
- dominant / secondary / observer_only 경계가 왜 조정되었는가
- 이 변화가 local tweak인지 reusable lesson인지 무엇으로 읽어야 하는가

## 2-3. 목적
나중에 결과가 달라졌을 때
단순 output drift인지,
아니면 judgment rule drift인지
구분 가능하게 만드는 것이 목적이다.

## 3. 경계선 2 — PASS_WITH_NOTE와 hold discipline 보존

## 3-1. 현재 강점
지금 엔진은
“작동했다”와
“일반화해도 된다”를
구분하는 태도가 있다.

이건 매우 큰 장점이다.

특히 아래 감각을 잃지 않는 것이 중요하다.

- local success는 general law가 아니다
- candidate는 아직 candidate다
- repeated frame은 바로 baseline이 아니다
- 잘 먹힌 refinement는 promotion 대상이 아니라 hold 대상일 수 있다

## 3-2. 앞으로의 위험
엔진이 조금 더 잘 작동하기 시작하면,
사람은 자꾸 아래 유혹으로 이동한다.

- 이 정도면 충분하다
- 이제 승격해도 된다
- 계속 note를 붙일 필요가 없다
- hold를 빨리 풀어도 된다

이 유혹을 그대로 따르면
candidate -> lock note -> hold -> local success -> not yet generalizable
계단이 무너진다.

## 3-3. 앞으로 잠글 원칙
다음은 계속 유지한다.

- `PASS_WITH_NOTE`는 약한 성공이 아니라, 일반화 보류가 포함된 강한 판정이다
- local success가 확인되어도 자동 승격하지 않는다
- repeated pattern이 보여도 negative control 또는 failure axis를 보기 전까지 baseline화하지 않는다
- promotion은 evidence 부족 시 보류가 기본값이다

즉:
**잘 되는 것보다, 아직 일반화하면 안 되는 것을 같이 잠그는 태도**를 계속 유지한다.

## 4. 경계선 3 — reasoning residue를 별도 자산으로 다룬다

## 4-1. 현재 구조의 한계
지금은 대체로 아래 층이 잘 분리되어 있다.

- source
- derived
- report
- evidence
- receipt
- raw delta

하지만 앞으로는 이것만으로 부족하다.

왜냐하면 실제 refinement의 핵심은
결과 그 자체보다도
**그 결과를 좋다고 판단한 이유**
에 있기 때문이다.

## 4-2. 반드시 남겨야 하는 residue
앞으로 아래 종류의 판단 흔적은
별도 residue 관점으로 남긴다.

- 왜 이 차이를 case-bearing signal로 봤는가
- 왜 이 차이를 discourse noise로 봤는가
- why dominant role was chosen over secondary role
- 왜 observer 성분을 보이게만 하고 경쟁에서 뺐는가
- 왜 이 결과를 compare-ready가 아니라 compare-meaningful 쪽으로 읽었는가
- 왜 promotion은 premature라고 봤는가
- 왜 이 수정은 outer-layer가 아니라 inner refinement로 해결해야 한다고 판단했는가

## 4-3. 핵심 목적
이 residue가 안 남으면
엔진은 계속 출력은 쌓이는데
판단은 assistant/Codex/사용자 머릿속에만 남는다.

반대로 residue가 쌓이면
엔진은 나중에 아래 방향으로 발전할 수 있다.

- difference explanation 내장
- refinement candidate 제안 정교화
- judgment reuse 가능성 증가
- compare failure의 원인 추적 용이

즉:
**reasoning residue는 부가 메모가 아니라, 미래의 판단 엔진 재료다.**

## 5. 경계선 4 — outer-layer lock은 고정이 아니라 evidence-gated 원칙이다

## 5-1. 현재 원칙은 맞다
지금 단계에서는
- baseline
- current
- shared reality
- core
- inputter / labeler 직접 수정

을 쉽게 흔들지 않는 것이 맞다.

이건 시스템 안정성을 지키는 데 필수다.

## 5-2. 앞으로의 위험
하지만 이 원칙이 잘못 굳어지면,
나중에는 아래 같은 문제가 생길 수 있다.

- 입력 종류가 크게 달라졌는데도 외곽을 건드리지 않음
- 운영 규모가 달라졌는데도 오래된 surface 해석을 유지함
- internal tuning으로는 해결되지 않는 문제를 계속 억지로 내부에만 묶음
- “외곽은 sacred”라는 잘못된 금기 형성

## 5-3. 앞으로 잠글 원칙
외곽은 기본적으로 고정한다.
그러나 성역화하지는 않는다.

즉 아래 식으로 해석한다.

> outer-layer lock은 기본값이다.  
> 다만 충분한 comparative evidence가 누적되고, bounded internal refinement만으로 설명/해결되지 않으며, 입력 또는 운영 조건의 구조적 변화가 확인될 경우에 한해 천천히 재검토할 수 있다.

즉:
**고정과 경직을 구분한다.**

## 6. 경계선 5 — 성공 사례만이 아니라 failure / negative-control 축을 비교에 넣는다

## 6-1. 현재 비교 축
지금 비교는 대체로 아래 셋을 중심으로 잘 작동하고 있다.

- standard document
- external document
- general/raw document

이 축은 유지한다.

## 6-2. 앞으로 추가해야 할 축
하지만 이 세 축만으로는 부족하다.

앞으로는 아래도 의도적으로 비교 세트에 넣는다.

- 실패 사례
- degraded 사례
- overly flattened 사례
- noisy 사례
- broader negative control

## 6-3. 이유
성공적으로 읽히는 재료만 계속 넣으면,
엔진은 깔끔한 사례에만 적응하는 방향으로 과적합될 수 있다.

실패 축이 있어야 아래가 가능하다.

- 어디서 role resolution이 무너지는가
- 어떤 입력에서 generic discourse가 다시 떠오르는가
- 어떤 조건에서 compare가 형식 중복 확인기로 떨어지는가
- 어떤 경우 note/hold가 더 강하게 필요해지는가

즉:
**failure axis는 품질 확인용 부록이 아니라 일반화 과잉을 막는 핵심 방어선이다.**

## 7. 앞으로의 반복 공고화 루프 보강판

앞으로 reusable internal hardening pattern은 아래 보강판으로 읽는다.

### Step A. outer-layer untouched 기본 확인
- outer surface 유지 여부
- baseline/current/shared reality/core 비수정 원칙 확인
- 이번 문제가 내부 미세조정 문제인지 먼저 판정

### Step B. comparative set 구성
최소 아래 4종을 고려한다.

- standard
- external
- general/raw
- failure or negative-control

### Step C. output 비교
비교 대상:
- anchor dominance
- topic-bearing signal
- dominant / secondary role mix
- observer_only 분리
- case_specific_signals
- packet quality
- flattening 여부

### Step D. judgment reason 추출
반드시 뽑는다.

- 왜 이 결과를 더 낫다고 보는가
- 왜 저 결과를 premature라고 보는가
- 왜 이 차이는 의미 있고 저 차이는 noise인가
- 왜 이건 local success이고 not-yet-generalizable인가

### Step E. bounded refinement
- 1~2 layer 또는 1~2 bounded surface 수준만 수정
- untouched 목록 명시
- judgment-criteria change 여부 명시
- evidence-gated note 명시

### Step F. reusable lesson + residue capture
- 이번 refinement가 재사용 가능한지 기록
- reasoning residue를 요약 자산으로 남김
- 일반화 금지 사유가 있으면 함께 기록

## 8. Codex가 앞으로 절대 잊지 말아야 할 것

### 8-1. 기억해야 할 원칙
- output 기록만으로는 충분하지 않다
- judgment criteria의 변화 이력을 남겨야 한다
- PASS_WITH_NOTE / hold discipline을 계속 유지해야 한다
- reasoning residue를 엔진 안쪽 자산으로 점차 이식해야 한다
- outer-layer lock은 sacred가 아니라 evidence-gated stability 원칙이다
- failure / negative-control 비교 축을 의도적으로 넣어야 한다

### 8-2. 금지할 것
- local success를 너무 빨리 promotion으로 읽기
- result improvement를 곧바로 baseline 승격으로 연결하기
- reasoning residue를 사람 머릿속에만 남기기
- 성공 사례만 보고 일반화하기
- outer-layer lock을 무비판적 금기로 해석하기

## 9. 이번 턴에서 실제로 잠그는 해석

이번 턴의 핵심은
“운용이 꽤 잘 되고 있다”
가 아니다.

정확히는 아래를 잠그는 것이다.

> **앞으로 엔진이 커질수록 조심해야 할 핵심은 output abundance에 비해 judgment versioning과 reasoning residue가 얇아지는 것이며, 이를 막기 위해 premature generalization 억제, evidence-gated outer-layer governance, failure-axis comparative reading을 운영 기준으로 승격한다.**

## 10. Codex 실행 지시

다음 유사 상황에서는 아래 순서로 행동한다.

1. 이번 문제가 결과 문제인지, 판단 기준 문제인지 먼저 구분한다.
2. judgment criteria drift 여부를 별도로 적는다.
3. standard / external / general / failure 축으로 비교 세트를 구성한다.
4. output 차이뿐 아니라 판단 이유 차이를 같이 뽑는다.
5. reasoning residue를 별도 자산으로 남긴다.
6. local success라면 note와 hold를 먼저 붙인다.
7. outer-layer 수정은 충분한 비교 증거가 없으면 보류한다.
8. reusable lesson과 generalization 금지 사유를 함께 기록한다.

## 11. 한 줄 최종 잠금

> **다음 성장 단계의 핵심 운영 경계선은, output 기록 중심 구조를 judgment-versioning·reasoning-residue·failure-axis까지 확장하여 premature generalization 없이 evidence-gated 공고화를 유지하는 것이다.**
