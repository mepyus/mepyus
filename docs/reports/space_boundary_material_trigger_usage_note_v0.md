# space boundary material trigger usage note v0

## verdict

```yaml
verdict: PASS_WITH_NOTE
normal_use_ready: true
baseline_lock: false
schema_enforcement: false
writer_now: false
runtime_reingress_now: false
next_allowed_move: apply_this_default_on_next_real_material
```

## purpose

This note is not a new controller spec.

This note explains how user trigger phrases such as "이 재료 넣어봐" should call the existing Space Boundary Camera/Lens normal-use flow.

Internal operating name:

```text
Space Boundary Trigger Flow
```

User-facing name:

```text
공간에 넣어보기
```

Secondary user-facing phrase:

```text
재료 넣어보기
```

The allowed meaning is:

```text
user trigger
-> existing source-surface camera/lens flow
-> compact judgment
```

The disallowed meaning is:

```text
new controller system
automatic execution
writer
schema enforcer
final state decider
```

## trigger phrases

These user phrases should invoke the default trigger flow:

- 이거 공간에 넣어봐
- 이 자료 공간에 넣어봐
- 이 결과 공간에 넣어봐
- 이 재료 넣어봐
- 공간에서 쓸 수 있게 봐줘
- 이거 우리 공간에서 쓸 수 있는지 봐줘
- 이 결과 다음으로 넘겨도 돼?
- 이 Codex return을 공간 기준으로 판단해줘
- 이 외부 자료를 우리 공간에서 쓸 수 있게 읽어줘
- 이 대화 결과를 다음 작업으로 넘길 수 있는지 봐줘
- 이 로그 의미 있는 변화인지 봐줘
- 이 Codex 결과 이어가도 되는지 봐줘

The user does not need to name Core 7, object type, source surface, or lens order.

## invoked default flow

The trigger invokes this existing flow:

```text
material enters
-> source surface 판단
-> source-surface별 lens order 적용
-> 필요한 경우 관련 자산 일부만 packet으로 참조
-> Codex/assistant가 제한된 역할로 판단
-> 사용자에게 4줄 카드 반환
-> 재등장 가치가 있으면 9-field markdown return record 후보 작성
-> deeper probe일 때만 reingress/runtime 계열 사용
```

Operating rules:

- The user does not choose Core 7, object type, or lenses.
- Codex/assistant judges the source surface.
- Do not load every Space Boundary asset at once.
- Reference only the asset slice needed for the current packet.
- User-facing output defaults to a 4-line card.
- 9-field return record is optional, not mandatory.

## output contract

Internal default card:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

User-facing default card:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

Use the user-facing card by default when answering the user.

The internal card labels may remain in internal records.

Long reports, schema, runtime manifests, automatic records, and index updates are not default outputs.

## user language mapping

| 내부 표현 | 사용자 표현 |
| --- | --- |
| Space Boundary Trigger Flow | 공간에 넣어보기 |
| Boundary Material Intake Controller | 사용하지 않음 / 오해 위험 표현 |
| source surface | 이 재료가 어디서 온 건지 |
| lens order | 어떤 순서로 읽을지 |
| 4-line card | 짧은 판단 카드 |
| 9-field return record | 나중에 다시 쓸 표시 |
| external_material_file | 외부자료 |
| generated_report | 만들어진 보고서 |
| runtime_event | 실행 흔적 |
| worker_return | 작업 결과 |
| program_artifact | 코드/도구 조각 |
| conversation_material | 대화 재료 |

## optional return record

A 9-field return record candidate is used only when continuity matters.

Use it when:

- the material is likely to re-emerge later
- the judgment trace will be reused in a later task
- the material needs a minimal return-to-space continuity note
- worker return, generated report, external material, or conversation material becomes follow-up decision material

The 9-field return record is not an automatic writer output and not runtime JSON by default.

Candidate fields:

```yaml
source_ref:
input_summary:
selected_lenses:
space_relation:
codex_judgment:
return_state:
reemergence_trigger:
created_outputs:
do_not:
```

## source surface lens order

This table is not a user menu.

Codex/assistant applies it internally after judging the input material's source surface.

| source surface | lens order |
| --- | --- |
| `external_material_file` | technical -> maker-intent -> user-intent -> line/axis -> risk -> residue |
| `generated_report` | user-intent -> line/axis -> risk -> residue -> return-state |
| `runtime_event` | evidence/event -> technical -> risk -> residue -> line/axis |
| `worker_return` | expected-vs-observed -> risk -> residue -> next-move -> line/axis |
| `program_artifact` | artifact-role -> evidence/event -> technical -> residue -> risk |
| `conversation_material` | user-intent -> feature-direction -> line/axis -> residue -> risk |

Same pipeline, different camera/lens order.

## controller wording caution

`Boundary Material Intake Controller` is risky wording at this stage.

Allowed meaning:

- usage label for connecting user trigger phrases to the existing flow
- shorthand for interpreting "재료를 넣어봐" as Space Boundary normal-use intake
- thin phrase for source-surface judgment, lens order selection, and 4-line card return

Disallowed meaning:

- automatic execution system
- final state decider
- writer
- schema enforcer
- runtime manifest generator
- microspace/index updater
- helper elevation
- new controller implementation spec

Prefer:

```text
Space Boundary Trigger Flow
trigger note
usage note
```

Use `controller` only with caution and only as an informal label.

## helper boundary

`scripts/cli/space_boundary_lookup_packet.py` is a read-only suggestion helper.

Allowed roles:

- create read-only suggestion packet
- guess source surface
- suggest source-surface lens order
- suggest related asset candidates
- suggest microspace matches
- suggest guardrails

Disallowed roles:

- decide final state
- write files
- create runtime records
- update index or microspace
- fetch web content
- enforce schema
- act as automatic controller

Best current description:

```text
작업 패킷 조립기의 seed 또는 보조 선택기
```

## do not

- Do not baseline lock.
- Do not enforce schema.
- Do not create runtime manifest.
- Do not implement return-record writer.
- Do not force validator or script.
- Do not auto-update microspace/index.
- Do not let the helper decide final state.
- Do not force 9-field return record on every input.
- Do not define controller as an automatic execution system.
- Do not create a new large package for this trigger flow.
- Do not redesign existing structure.

## next real test

Next step is not implementation.

Next step is to apply the trigger flow to one real material.

Example user input:

```text
이 재료 넣어봐.
```

Candidate materials:

- external URL
- external document
- Codex report
- worker return
- runtime event
- program artifact
- conversation result

Expected output:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

Attach a 9-field return record candidate only when the material has future re-emergence value.
