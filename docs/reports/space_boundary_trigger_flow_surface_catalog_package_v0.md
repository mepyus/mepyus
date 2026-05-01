# Space Boundary Trigger Flow Surface Catalog Package v0

## 1. status

```yaml
catalog_status: surface_coverage_catalog
verdict: PASS_WITH_NOTE
normal_use_ready: true
baseline_lock: false
schema_enforcement: false
writer_now: false
runtime_reingress_now: false
next_allowed_move: apply_this_default_on_next_real_material
```

## 2. purpose

This document is the source-surface coverage catalog for Space Boundary Trigger Flow.

User-facing name:

```text
공간에 넣어보기
```

Secondary user-facing phrase:

```text
재료 넣어보기
```

It exists so that when the user says:

```text
이거 공간에 넣어봐
이 자료 공간에 넣어봐
이 결과 공간에 넣어봐
이 재료 넣어봐
공간에서 쓸 수 있게 봐줘
이거 우리 공간에서 쓸 수 있는지 봐줘
이 결과 다음으로 넘겨도 돼?
이 Codex return을 공간 기준으로 판단해줘
이 외부 자료를 우리 공간에서 쓸 수 있게 읽어줘
이 로그 의미 있는 변화인지 봐줘
이 Codex 결과 이어가도 되는지 봐줘
```

Codex/assistant can quickly check:

- which source surfaces have already been tested
- which lens order to apply
- which representative material was used
- whether a 4-line card worked
- whether a 9-field candidate was needed
- what the key risk is
- what remains pending

This is not:

- a controller spec
- an automation design
- a schema document
- a writer implementation plan
- a runtime system

## 3. default trigger flow

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

Default user-facing card:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

Internal card labels may still be used inside records:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

## 4. surface coverage table

| source_surface | status | test_material | applied_lens_order | 4-line_card | 9-field_candidate | key_risk | next_use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `conversation_material` | PASS_WITH_NOTE | trigger-flow validation request / user-Codex conversation material | user-intent -> feature-direction -> line/axis -> residue -> risk | 작동함 | No | 실제 재료가 아니라 테스트 지시였으므로 return record를 붙이면 과잉 기록 | 사용자 대화 결과나 설계 논의를 다음 작업으로 넘길 때 사용 |
| `external_material_file` | PASS | `inputs/external_cases/token_efficiency_claude_codex_stdy_note_v0.md` | technical -> maker-intent -> user-intent -> line/axis -> risk -> residue | 작동함 | No for this repeated test | token efficiency 자료를 Codex 설정 doctrine이나 baseline rule로 과승격할 위험 | 외부자료를 bounded operating reference로 읽을 때 비교 기준으로 사용 |
| `generated_report` | PASS | `docs/reports/space_boundary_normal_use_token_efficiency_material_trial_v0.md` | user-intent -> line/axis -> risk -> residue -> return-state | 작동함 | No | 원본 외부자료와 생성 보고서를 같은 surface로 읽는 위험 | 처리 결과 보고서를 validation_return 또는 comparison_reference로 다시 읽을 때 사용 |
| `worker_return` | PASS_WITH_NOTE | `runtime/cli_sessions/cli_20260418T224406Z_754042af/structured_return.json` | expected-vs-observed -> risk -> residue -> next-move -> line/axis | 작동함 | No | 좋은 보고서처럼 읽어 완료 산출물이나 도입 근거로 과승격할 위험 | worker가 기대한 작업을 실제로 수행했는지 expected-vs-observed 중심으로 검증할 때 사용 |
| `program_artifact` | PASS_WITH_NOTE | `scripts/cli/space_boundary_lookup_packet.py` | artifact-role -> evidence/event -> technical -> residue -> risk | 작동함 | No | `lookup_packet`이라는 이름 때문에 helper가 controller 본체, 자동 intake 실행기, final state 결정기로 오해될 위험 | 실제 재료가 들어올 때 packet seed 또는 보조 선택기로만 사용 |
| `runtime_event` | PASS_WITH_NOTE | `runtime/events/engine_event_ledger.jsonl` / `evt_20260324_194938_e93a99b8 / receipt_written` | evidence/event -> technical -> risk -> residue -> line/axis | worked | No for this validation session | runtime event를 generated_report, worker_return, program_artifact처럼 오독하거나 완료 증거로 과승격할 위험 | runtime/log/event를 읽을 때 ledger 전체가 아니라 구체적 event slice 1건을 선택해 evidence/event부터 읽음 |

Note for `external_material_file`:

```text
"No for this repeated test" does not mean the material has no record value.
It means the earlier normal-use trial already included a 9-field candidate,
so the repeated trigger-flow test did not create a duplicate record.
```

Note for `generated_report`:

```text
The tested report already contains a 9-field candidate from the prior trial,
so rereading it as generated_report should not create a duplicate record.
```

Note for `worker_return`:

```text
The structured return itself contains findings, files_artifacts,
next_continue_hint, open_questions, risks_or_limits, and source_refs.
That was enough for this test.
```

Note for `program_artifact`:

```text
The test only judged artifact role. It did not authorize implementation,
execution, or helper elevation.
```

## 5. source surface distinction principles

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

Same topic does not mean same source surface.

Example:

```text
original token efficiency external material = external_material_file
trial report created from that material = generated_report
```

Source surface is judged from the role the input plays now, not only from topic or filename.

Questions:

- Is this the source material itself?
- Is this a generated report about a prior run?
- Is this a worker return?
- Is this a runtime event/evidence artifact?
- Is this a generated program artifact?
- Is this user-Codex conversation material?

## 6. 9-field candidate principles

Do not force 9-field return records on every input.

Create a candidate when:

- the material is likely to re-emerge later
- a minimum continuity note is needed for return-to-space
- worker return, generated report, or conversation result becomes follow-up decision material
- there is no existing record and reuse value is high enough

Do not create a candidate when:

- the material already has a 9-field candidate and this is a repeated test
- `structured_return.json` already contains enough return fields for the current question
- the input is a simple dry-run or validation request
- the work is only artifact-role judgment
- adding a record would create over-recording

## 7. helper boundary

`scripts/cli/space_boundary_lookup_packet.py` is:

```text
read-only suggestion packet helper
source surface 후보 제안
lens order 후보 제안
asset 후보 제안
microspace match 후보 제안
guardrail 후보 제안
```

It is not:

```text
final state 결정기
4줄 카드 최종 작성 권한 독점자
writer
runtime record 생성기
schema enforcer
index/microspace updater
자동 controller
```

Core sentence:

```text
helper는 판단을 줄이는 보조 선택기이지, 판단을 대체하는 결정기가 아니다.
```

## 8. runtime_event validation note

`runtime_event` has now been validated as `PASS_WITH_NOTE`.

Validated material:

```text
runtime/events/engine_event_ledger.jsonl
```

Selected event:

```text
evt_20260324_194938_e93a99b8 / receipt_written
```

The lens order is:

```text
evidence/event -> technical -> risk -> residue -> line/axis
```

It must not be read as:

- `generated_report`
- `program_artifact`
- `worker_return`

The first question is:

```text
what event/evidence actually happened?
```

not:

```text
what report does this summarize?
what artifact role does this file have?
what did a worker return compared with expectation?
```

Catalog status:

```yaml
status: PASS_WITH_NOTE
4_line_card: worked
9_field_candidate_policy: No for this validation session
baseline_lock: false
schema_enforcement: false
runtime_manifest_created: false
controller_implemented: false
helper_modified: false
```

## 9. do not

- baseline lock 금지
- schema enforcement 금지
- runtime manifest 생성 금지
- return-record writer 구현 금지
- validator/script 강제 금지
- microspace/index 자동 update 금지
- helper가 final state를 결정하게 만들기 금지
- 모든 입력에 9-field record 강제 금지
- controller를 자동 실행 시스템으로 정의 금지
- 새 대형 패키지 생성 금지
- 기존 Trigger Flow를 새 시스템으로 과잉 확장 금지

## 10. next use

Next use:

```text
runtime_event
```

Candidate material:

```text
runtime/events/engine_event_ledger.jsonl
```

Expected output:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

Attach a 9-field candidate only if a specific event slice becomes reusable follow-up material.
