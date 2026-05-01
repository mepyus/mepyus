# Space Boundary Material Application Examples Package v0

## 1. status

```yaml
package_name: space_boundary_material_application_examples_package_v0
user_facing_name: 공간에 넣어보기 예시 패키지
package_status: package_candidate
verdict: PASS_WITH_NOTE-ready
baseline_lock: false
schema_enforcement: false
writer_now: false
runtime_reingress_now: false
controller_implementation: false
```

## 2. purpose

This package does not redesign Space Boundary Trigger Flow.

It collects practical examples for the user-facing action:

```text
이거 공간에 넣어봐.
```

Internal flow remains:

```text
material enters
-> source surface 판단
-> source-surface별 lens order 적용
-> Codex/assistant 판단
-> 사용자에게 4줄 카드 반환
-> 필요할 때만 9-field 후보 작성
```

User-facing output:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

## 3. principles

Do:

- use real material examples
- judge source surface internally
- apply the correct lens order
- return the user-facing 4-line card first
- leave internal record candidates only when needed
- check whether the result leads to a next action

Do not:

- create a new controller
- create a new schema
- create runtime manifests
- auto-update indexes
- elevate the helper into a final-state decider
- force every input into a 9-field record
- lock examples as baseline

## 4. example set

Representative examples:

1. `worker_return`
2. `external_material_file`
3. `program_artifact`

Boundary examples:

4. `runtime_event`
5. `conversation_material`

Optional example:

6. `generated_report`

## 5. case definitions

| case_id | source_surface | internal lens order | purpose |
| --- | --- | --- | --- |
| Case 1 | `worker_return` | expected-vs-observed -> risk -> residue -> next-move -> line/axis | Check whether Codex/CLI returns can become next instruction material. |
| Case 2 | `external_material_file` | technical -> maker-intent -> user-intent -> line/axis -> risk -> residue | Read external material as reference/comparison/risk/residue, not doctrine. |
| Case 3 | `program_artifact` | artifact-role -> evidence/event -> technical -> residue -> risk | Read code/helper by role before technical detail. |
| Case 4 | `runtime_event` | evidence/event -> technical -> risk -> residue -> line/axis | Read one event slice as evidence, not whole-system proof. |
| Case 5 | `conversation_material` | user-intent -> feature-direction -> line/axis -> residue -> risk | Read conversation as user intent/friction/next-use material. |
| Optional Case 6 | `generated_report` | user-intent -> line/axis -> risk -> residue -> return-state | Read generated reports as returned process material, not source or baseline. |

## 6. case record format

Each case should be recorded as:

```text
case_id:
input_type:
source_surface:
lens_order:
user_card:
  쓸 수 있나?
  왜?
  다음엔?
  조심할 점은?
internal_note:
risk:
next_move:
record_candidate:
verdict:
```

## 7. output boundary

The examples package is for training the use of the user-facing flow.

It should not make the user see:

- `source_surface`
- `lens_order`
- `9-field`
- `runtime_event`
- `worker_return`

by default.

Those remain internal reading labels.

## 8. do not

- baseline lock 금지
- schema enforcement 금지
- runtime manifest 생성 금지
- return-record writer 구현 금지
- validator/script 강제 금지
- microspace/index 자동 update 금지
- helper가 final state를 결정하게 만들기 금지
- 모든 입력에 9-field record 강제 금지
- controller를 자동 실행 시스템으로 정의 금지
- 예시를 baseline으로 잠그기 금지

