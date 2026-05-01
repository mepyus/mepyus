# Space Boundary Normal-Use Runtime Subtype Trial v0

## 1. status

```yaml
report_status: normal_use_runtime_subtype_trial
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_record_created: false
index_updated: false
writer_created: false
```

## 2. purpose

The prior cross-surface trial checked:

- external material
- generated report
- runtime event artifact

This trial checks the remaining runtime-adjacent subtypes:

- worker return
- program artifact

The purpose is to ensure that runtime-adjacent materials are not all flattened into a generic event-log camera.

## 3. cases

| Case | Source ref | Why tested |
| --- | --- | --- |
| A. worker return | `runtime/cli_sessions/cli_20260418T224406Z_754042af/structured_return.json` | tests returned worker output with expected/observed and next-use fields |
| B. program artifact | `app/work/observer_ingest_min/generated/line_seed_bundles_gemini_deep_research_api_note_v0_20260423_212542.json` | tests generated bundle/index-like artifact |

## 4. Case A. worker return

Command:

```text
python3 scripts/cli/space_boundary_lookup_packet.py runtime/cli_sessions/cli_20260418T224406Z_754042af/structured_return.json
```

Helper result:

```yaml
source_surface:
  primary: runtime_artifact
  subtype: worker_return
  confidence: medium
top_lenses:
  - expected-vs-observed
  - risk
  - residue
  - next-move
  - line/axis
```

Codex judgment:

```text
This is not a generic runtime log. It is a worker return that should be read by comparing task intent, returned findings, risks, open questions, and next_continue_hint.
```

User-facing card:

```text
현재 판정: worker_return / validation_return
이유: structured_return은 실행 흔적보다 worker가 무엇을 봤고 무엇을 남겼는지, 기대와 관측이 어떻게 갈렸는지를 읽어야 하는 반환 객체임
다음 이동: next_continue_hint와 risks/open_questions를 기준으로 다음 bounded inspection 여부만 판단
금지선: worker return을 실행 성공, 구현 승인, baseline 증거로 승격 금지
```

9-field return record need:

```yaml
needed_now: no
reason: the structured return already contains answer/findings/files/next hint/open questions/risks
future_record_condition: create a markdown return record only if this worker return becomes a reusable comparison or continuation anchor
return_state: validation_return / reread_target
```

## 5. Case B. program artifact

Command:

```text
python3 scripts/cli/space_boundary_lookup_packet.py app/work/observer_ingest_min/generated/line_seed_bundles_gemini_deep_research_api_note_v0_20260423_212542.json
```

Helper result:

```yaml
source_surface:
  primary: runtime_artifact
  subtype: program_artifact
  confidence: medium
top_lenses:
  - artifact-role
  - evidence/event
  - technical
  - residue
  - risk
```

Codex judgment:

```text
This is not an external material and not a worker decision. It is a generated artifact that needs its role, origin, and reuse boundary read before its contents are treated as line evidence.
```

User-facing card:

```text
현재 판정: program_artifact / artifact_residue
이유: line_seed_bundles 파일은 분석 결과라기보다 generated bundle이므로, 먼저 artifact 역할과 생성 출처를 읽어야 함
다음 이동: 필요할 때만 어떤 source에서 어떤 bundle이 생겼는지 확인하고 line/axis evidence로 쓸 수 있는지 재판정
금지선: generated bundle을 곧바로 축 증거, index truth, baseline 구조로 승격 금지
```

9-field return record need:

```yaml
needed_now: no
reason: the artifact is broad generated support material, not currently attached to a specific claim
future_record_condition: create a return record only if it is used to support a concrete line/axis claim
return_state: artifact_residue / reread_priority
```

## 6. validation

| Check | Worker return | Program artifact | Judgment |
| --- | --- | --- | --- |
| Source subtype detected | PASS | PASS | Helper separated subtypes under runtime artifact. |
| Lens order differs | PASS | PASS | Worker return and program artifact did not share event-log lenses. |
| Output compact | PASS | PASS | 4-line card is enough. |
| Return record not forced | PASS | PASS | No 9-field record needed now. |
| Promotion avoided | PASS | PASS | No implementation, baseline, or evidence promotion. |
| Runtime mutation avoided | PASS | PASS | No records were written. |

## 7. what this confirms

Runtime-adjacent material needs at least three readings:

```text
runtime_event -> evidence/event first
worker_return -> expected-vs-observed first
program_artifact -> artifact-role first
```

This reduces a major flattening risk:

```text
all runtime-looking files are not the same kind of material.
```

## 8. remaining friction

The helper can detect subtype by path/name patterns, but Codex still has to decide whether the artifact is actually useful for the current purpose.

This should remain judgment-based.

## 9. verdict

```yaml
verdict: PASS_WITH_NOTE
ready_for_normal_use: true
runtime_reingress_now: false
writer_now: false
next_allowed_move: normal_use_surface_coverage_closeout
```

