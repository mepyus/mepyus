# Formation-Movement Interface Usage Manual v0
_형성층-운동층 인터페이스 패키지 운용법_

## 0. 문서 상태

```yaml
manual_status: usage_manual_candidate
based_on: formation_movement_interface round1 + weak-signal round closeout
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
purpose: 실제 작업 중 애매한 입력을 과승격/과실행하지 않고 안전하게 다루기 위한 사용 매뉴얼
```

---

# 1. 이 매뉴얼의 한 줄 목적

**애매한 자료, 요청, 설명, Codex 작업, 외부 reference가 들어왔을 때
바로 실행하거나 바로 승격하지 않고
“현재 판정 / 이유 / 다음 이동 / 금지선”을 먼저 세워 안전하게 다루기 위한 매뉴얼이다.**

---

# 2. 기본 원칙

## 2.1 이 패키지는 절차표가 아니라 안전장치다

항상 꺼내 쓰는 무거운 양식이 아니다.

사용 시점은 다음과 같다.

* 외부 자료가 들어왔는데 쓸 만해 보일 때
* Codex에게 일을 넘기고 싶은데 범위가 애매할 때
* 사용자면 설명이 너무 납작해질 위험이 있을 때
* A/B/C/T/X/R/L 여러 렌즈가 겹쳐 보일 때
* 결과가 돌아왔는데 final인지, hold인지, refine인지 애매할 때

반대로 단순한 오타 수정, 파일명 변경, 이미 정해진 문구 삽입 같은 작업에는 쓰지 않는다.

---

## 2.2 사용자는 Core 7을 채우지 않는다

사용자는 아래 3가지만 말하면 된다.

```text
목적:
출처:
금지선:
```

예시:

```text
목적: 이 외부 자료가 B 후보와 관련 있는지 보고 싶다.
출처: 방금 본 외부 reference
금지선: 바로 promotion하지 말고 위치만 판정한다.
```

Core 7은 사용자가 채우는 입력 양식이 아니다.
Core 7은 객체가 생애주기를 돌며 점차 갖추는 logical core다.

---

## 2.3 기본 사용자면 출력은 4줄 카드다

사용자에게는 기본적으로 이것만 보인다.

```text
현재 판정:
이유:
다음 이동:
금지선:
```

예시:

```text
현재 판정: framing_candidate
이유: B와 닿지만 직접 증거라기보다 comparison frame에 가까움
다음 이동: 내부 CLI/외부도구 기록과 compare_only
금지선: B promotion / baseline 반영 / operating rule 승격 금지
```

---

# 3. 핵심 용어

## 3.1 형성층

```text
공간 + VectorFL
```

역할:

* 흔적과 기록을 다시 읽는다
* 잠정 객체를 형성한다
* candidate / hold / reread_priority를 판정한다
* 아직 익지 않은 것을 과승격하지 않는다

---

## 3.2 운동층

```text
엔진면 / Codex / worker / 실행 / 반환
```

역할:

* 제한된 작업을 수행한다
* worker handoff를 한다
* expected_return_form에 따라 결과를 돌려준다
* 결과는 final이 아니라 validation_return으로 돌아온다

---

## 3.3 형성층-운동층 인터페이스

완성물을 넘기는 export 지점이 아니다.

```text
잠정 객체에 “지금 bounded하게 움직여도 된다”는 운동 자격을 부여하는 조건부 문턱
```

---

# 4. 잠정 객체 5종

## 4.1 unclassified seed

아직 object_type을 확정하지 않은 초기 상태.

사용 시점:

* 자료가 막 들어왔을 때
* 요청은 있지만 역할이 불명확할 때
* 아직 reread_priority인지 framing_candidate인지 모를 때

사용자 입력:

```text
current_purpose
source_trace
initial_boundary 또는 why_now
```

주의:

* seed 단계에서 object_type 확정 금지
* Core 7 전체 요구 금지
* execution 금지

---

## 4.2 reread_priority

더 읽어야 하는 객체.

사용 시점:

* 유용해 보이지만 역할이 불명확할 때
* direct evidence / defensive logic / comparison frame 구분이 안 될 때
* A/C/T/X/R/L overlap이 강할 때
* 지금 넘기면 과해석될 위험이 있을 때

기본 다음 이동:

```text
reread_only
compare_later
hold
```

---

## 4.3 framing_candidate

현재 목적과 연결되기 시작한 후보.

사용 시점:

* 어떤 역할 후보인지는 보일 때
* comparison frame으로 쓸 수 있을 때
* 그러나 promotion은 아직 이른 경우

필수 조건:

```text
candidate_role
promotion_barrier
next_allowed_move
reread_return_hook
```

---

## 4.4 bounded_action_candidate

제한된 작업으로 준비할 수 있는 객체.

사용 시점:

* actionable question이 있음
* boundary가 있음
* expected_return_form이 있음
* return_hook이 있음

주의:

```text
bounded_action_candidate는 실행이 아니다.
대부분 allowed_to_prepare 상태다.
```

---

## 4.5 guarded_execution

실제로 실행 가능한 상태.

필요 조건:

```text
execution_constraint
guardrail
fallback_policy
trust_scope
expected_return_form
reread_return_hook
```

주의:

* prepare_worker_packet은 guarded_execution이 아니다
* 실행 전에는 반드시 guardrail이 있어야 한다
* 결과는 validation_return으로 회수한다

---

## 4.6 validation_return

운동층에서 돌아온 결과.

역할:

* final result가 아니다
* 다음 형성 루프의 입력이다
* refine / hold / downgrade / archive_as_residue / promote 금지 중 하나로 분기한다

기본 short form:

```text
observed_result
reread_trigger
next_recommended_state
```

full form 필요 조건:

* promotion risk
* baseline risk
* schema risk
* object_type 변경
* trust_scope 변경
* R loss / flattening
* overlap-heavy case
* expected_return_form과 실제 결과 차이 큼

---

# 5. 실제 사용 흐름

## 5.1 외부 자료를 볼 때

### 사용자 호출문

```text
이 자료를 formation_movement 패키지 기준으로 ingest 판정해줘.
바로 promotion하지 말고 unclassified seed부터 봐줘.
```

### 내가 먼저 해야 할 판정

```text
현재 판정:
이유:
다음 이동:
금지선:
```

### 건강한 흐름

```text
unclassified seed
→ reread_priority 또는 framing_candidate
→ 필요 시 bounded_action_candidate
→ validation_return
→ refine / hold / archive_as_residue
```

### 금지

* 외부 reference를 바로 evidence로 보기
* B-adjacent reference를 바로 B 증거로 보기
* operating rule로 승격하기
* baseline 반영하기

---

## 5.2 Codex에게 넘길 때

### 사용자 호출문

```text
이걸 Codex에게 바로 실행시키지 말고,
prepare_worker_packet 가능한지 먼저 판정해줘.
```

### 먼저 확인할 것

```text
boundary가 있는가?
expected_return_form이 있는가?
guardrail이 있는가?
reread_return_hook이 있는가?
```

없으면:

```text
현재 판정: HOLD
이유: Codex에게 넘길 packet 조건이 부족함
다음 이동: boundary / expected_return_form / guardrail 먼저 형성
금지선: 실행 금지
```

### prepare와 execute 구분

```text
allowed_to_prepare != allowed_to_execute
```

실행으로 넘어가려면:

```text
execution_constraint
guardrail
fallback_policy
trust_scope
expected_return_form
reread_return_hook
```

이 필요하다.

---

## 5.3 사용자면 설명을 만들 때

### 사용자 호출문

```text
이 설명이 acceptable simplification인지 R loss인지 패키지 기준으로 봐줘.
final definition으로는 올리지 마.
```

### 확인할 것

```text
L: 사용자면 카메라가 맞는가?
R: residue / intermediate layer / reread / provisionality가 남아 있는가?
T: 개념이 설명 가능한 만큼 익었는가?
X: 사용자 언어로 변환되는 구조가 있는가?
```

### 흔한 실패

```text
내부 언어 과잉 설명 → L 실패
너무 쉬운 설명 → R loss / flattening
강하지만 final처럼 보이는 설명 → full validation 필요
```

### 건강한 판정 예시

```text
현재 판정: user_surface_draft_candidate
이유: 이해 가능하지만 일부 residue hook이 약함
다음 이동: refine
금지선: final definition / baseline wording 승격 금지
```

---

## 5.4 A/C/T/X/R/L overlap이 있을 때

### 사용자 호출문

```text
이건 A/C/T/X/R/L overlap이 있는지 보고,
단일 축으로 정리하지 말고 hold 여부를 먼저 봐줘.
```

### 기본 원칙

overlap-heavy case는 clean framing보다 hold/reread가 더 안전하다.

### 확인 질문

```text
하나의 축으로 정리하면 다른 후보를 흡수하는가?
어떤 렌즈가 중심인지 아직 불명확한가?
translation risk가 있는가?
short validation으로 충분한가?
full validation이 필요한가?
```

### 건강한 판정 예시

```text
현재 판정: reread_priority
이유: A/C/T/X/R/L이 동시에 강해 단일 축으로 정리하면 과흡수 위험이 있음
다음 이동: reread_against_A_C_T_X_R_L
금지선: 축 확정 / promotion 금지
```

---

## 5.5 결과가 돌아왔을 때

### 사용자 호출문

```text
이 결과를 final로 보지 말고 validation_return으로 읽어줘.
refine / hold / residue 중 어디가 맞는지 봐줘.
```

### short validation return

```text
observed_result:
reread_trigger:
next_recommended_state:
```

### 분기

```text
refine:
  방향은 맞지만 보완 필요

hold:
  의미는 있지만 더 움직이면 위험

downgrade:
  상태 판정이 너무 높았음

archive_as_residue:
  지금은 쓰지 않지만 나중에 자산

promote:
  기본 경로 아님. 반복성/설명력/재배치력/반례 처리/reopen 조건 필요
```

---

# 6. 판단 카드 템플릿

## 6.1 기본 사용자면 카드

```text
현재 판정:
이유:
다음 이동:
금지선:
```

---

## 6.2 외부 reference 카드

```text
현재 판정:
이유:
다음 이동:
금지선:
```

예시:

```text
현재 판정: reread_priority
이유: B와 닿지만 direct evidence인지 defensive logic인지 아직 불명확함
다음 이동: direct evidence / defensive logic / comparison frame 구분
금지선: B promotion / operating rule 승격 금지
```

---

## 6.3 Codex prepare 카드

```text
현재 판정:
이유:
다음 이동:
금지선:
```

예시:

```text
현재 판정: HOLD before prepare
이유: boundary와 expected_return_form이 부족해 one-shot packet으로 만들기 이름
다음 이동: 범위와 반환 형식 먼저 형성
금지선: Codex 실행 금지
```

---

## 6.4 사용자면 설명 카드

```text
현재 판정:
이유:
다음 이동:
금지선:
```

예시:

```text
현재 판정: refine
이유: 설명은 읽히지만 intermediate layer와 validation return의 결이 약해 R loss 위험 있음
다음 이동: residue hook을 남기는 방향으로 재작성
금지선: final definition / baseline wording 승격 금지
```

---

# 7. Codex 지시서 기본 구조

Codex에게 넘길 때는 항상 아래 구조를 쓴다.

```text
작업 목적:

작업 범위:

읽을 문서:

작성할 문서:

반드시 포함할 내용:

금지선:
- baseline lock 금지
- schema enforcement 금지
- implementation 금지
- runtime manifest 생성 금지
- validator/script 생성 금지
- Core 7 변경 금지
- object family 변경 금지

결과 보고 형식:
1. Verdict
2. 생성/수정한 파일 경로
3. 핵심 결과
4. intentionally not changed
5. unresolved questions
```

---

# 8. 언제 멈춰야 하는가

다음이 나오면 멈춘다.

```text
READY_FOR_CLARIFICATION_PATCH 없음
구조는 버팀
남은 문제는 threshold/example 부족
operator cost가 더 늘어날 위험
```

이 경우:

```text
structure expansion HOLD
patch NOW 금지
실제 운용 중 자연 발생 사례 수집
```

---

# 9. 언제 patch를 고려하는가

patch는 자동으로 하지 않는다.

다음 조건이 반복될 때만 후보로 만든다.

```text
같은 threshold 문제가 여러 사례에서 반복됨
operator cost를 늘리지 않는 wording clarification으로 해결 가능함
Core 7 확장이나 object family 추가 없이 해결 가능함
patch하지 않으면 실제 운용에서 반복 혼선이 생김
```

그래도 바로 patch하지 않고 먼저:

```text
threshold comparison note
→ patch readiness check
→ bounded clarification patch
```

순서로 간다.

---

# 10. 절대 금지

```text
Core 7 확장 금지
object family 추가 금지
weak-signal 전용 새 상태명 추가 금지
baseline lock 금지
schema enforcement 금지
validator/script 생성 금지
runtime manifest 생성 금지
PASS_WITH_NOTE를 promotion으로 오해 금지
validation_return을 final result로 오해 금지
사용자에게 full sidecar 작성 요구 금지
prepare_worker_packet을 실행으로 오해 금지
```

---

# 11. 실전 호출문 모음

## 외부 자료

```text
이 자료를 formation_movement 패키지 기준으로 ingest 판정해줘.
바로 promotion하지 말고 unclassified seed부터 봐줘.
```

## Codex 작업

```text
이걸 Codex에게 바로 실행시키지 말고,
prepare_worker_packet 가능한지 먼저 판정해줘.
```

## 사용자면 설명

```text
이 설명이 acceptable simplification인지 R loss인지 봐줘.
final definition으로는 올리지 마.
```

## overlap

```text
이건 A/C/T/X/R/L overlap이 있는지 보고,
단일 축으로 정리하지 말고 hold 여부를 먼저 봐줘.
```

## 결과 회수

```text
이 결과를 final로 보지 말고 validation_return으로 읽어줘.
refine / hold / residue 중 어디가 맞는지 봐줘.
```

---

# 12. 최종 사용 원칙

**평소에는 4줄 카드만 쓴다.**

```text
현재 판정:
이유:
다음 이동:
금지선:
```

**복잡해질 때만 full sidecar를 쓴다.**

**Codex/엔진으로 넘길 때만 motion sidecar를 쓴다.**

**결과는 final이 아니라 validation_return으로 회수한다.**

**패키지는 일을 늘리는 절차가 아니라, 애매한 것을 과승격하지 않게 하는 안전장치다.**
