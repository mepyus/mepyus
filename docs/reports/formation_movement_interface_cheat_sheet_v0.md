# Formation-Movement Interface Cheat Sheet v0

## 1. purpose

This sheet is for real use, not for theory review.

Use it when you want to quickly decide:

- should this be reread, compared, prepared, executed, or held?
- is this input too weak to promote?
- is this explanation too flat to reuse?
- is this Codex request still too under-bounded?

Core rule:

```text
애매하면 먼저 4줄 카드로 멈춘다.
```

## 2. default output

When the input is ambiguous, start here:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

This is the default user-facing output.

Do not start with:

- full sidecar
- final wording
- execution
- promotion

## 3. when to use this package

Use the package when:

- an external reference looks useful but may be over-promoted
- you want to send something to Codex but the boundary is weak
- a user explanation feels readable but suspiciously thin
- multiple lenses such as A/C/T/X/R/L are active at once
- a returned result may be misread as final

Do not use the package when:

- the task is trivial and already bounded
- the work is simple editing with no ambiguity
- no promotion or execution risk exists

## 4. the only 3 things the user needs to provide

```text
목적:
출처:
금지선:
```

Example:

```text
목적: 이 외부 자료가 B 후보와 관련 있는지 보고 싶다
출처: 방금 본 링크
금지선: 바로 promotion하지 말고 위치만 판정
```

The user does not fill Core 7.

## 5. quick object guide

### unclassified seed

Use when:

- something just entered
- role is unclear
- even reread_priority vs framing_candidate is not clear yet

### reread_priority

Use when:

- useful but still unclear
- direct evidence / defensive logic / comparison frame split is unresolved
- overlap is strong
- sending it forward would force over-interpretation

### framing_candidate

Use when:

- role is visible
- comparison use is possible
- promotion is still too early

### bounded_action_candidate

Use when:

- there is an actionable question
- there is a boundary
- there is an expected return form
- there is a reread return hook

Important:

```text
bounded_action_candidate는 대부분 prepare 상태지 execution 상태가 아니다.
```

### guarded_execution

Only use when:

- execution_constraint exists
- guardrail exists
- fallback_policy exists
- trust_scope exists
- expected_return_form exists
- reread_return_hook exists

### validation_return

Always use when a result comes back.

Never treat the result as automatically final.

## 6. three most common triggers

### trigger A. external reference

Say:

```text
이 자료를 formation_movement 패키지 기준으로 ingest 판정해줘.
바로 promotion하지 말고 unclassified seed부터 봐줘.
```

Default healthy outcome:

- `reread_priority`
- sometimes `framing_candidate`
- not evidence lock

### trigger B. Codex request

Say:

```text
이걸 Codex에게 바로 실행시키지 말고,
prepare_worker_packet 가능한지 먼저 판정해줘.
```

First check:

- boundary
- expected_return_form
- guardrail
- reread_return_hook

If missing:

```text
현재 판정: HOLD
이유: packet 조건 부족
다음 이동: boundary와 expected return 먼저 형성
금지선: execution 금지
```

### trigger C. user explanation

Say:

```text
이 설명이 acceptable simplification인지 R loss인지 봐줘.
final definition으로는 올리지 마.
```

Check:

- L: camera fit
- R: residue remains?
- T: ripe enough?
- X: translation structure exists?

Default healthy outcome:

- often `refine`
- sometimes `hold`
- not baseline wording

## 7. overlap trigger

If many lenses are active, say:

```text
이건 A/C/T/X/R/L overlap이 있는지 보고,
단일 축으로 정리하지 말고 hold 여부를 먼저 봐줘.
```

Default healthy outcome:

- `reread_priority`
- `hold`
- `reread_against_A_C_T_X_R_L`

Not:

- clean axis lock
- promotion

## 8. return trigger

When a result comes back, say:

```text
이 결과를 final로 보지 말고 validation_return으로 읽어줘.
refine / hold / residue 중 어디가 맞는지 봐줘.
```

Short form:

```text
observed_result:
reread_trigger:
next_recommended_state:
```

## 9. full validation return is needed when

- promotion risk appears
- baseline risk appears
- schema risk appears
- object_type changes
- trust_scope changes
- explanation flattening is strong
- overlap is strong enough that ambiguity is part of the result
- expected_return_form and actual result diverge significantly

## 10. hard do-not list

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
prepare_worker_packet을 execution으로 오해 금지
사용자에게 full sidecar 작성 요구 금지
```

## 11. stop rule

Stop and do not patch if:

```text
구조는 버티고 있음
READY_FOR_CLARIFICATION_PATCH 없음
남은 문제는 threshold/example 부족
지금 patch하면 operator cost가 늘어날 위험이 있음
```

Then the right move is:

- hold structure expansion
- keep using the package in real work
- collect natural weak cases

## 12. one-line memory

```text
평소에는 4줄 카드만 쓰고,
복잡해질 때만 sidecar를 열고,
결과는 final이 아니라 validation_return으로 회수한다.
```
