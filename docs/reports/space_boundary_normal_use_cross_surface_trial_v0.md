# Space Boundary Normal-Use Cross-Surface Trial v0

## 1. status

```yaml
report_status: normal_use_cross_surface_trial
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_record_created: false
index_updated: false
writer_created: false
```

## 2. purpose

The previous normal-use trial used one external material.

This trial checks whether the same default also works when the material is not an external article:

```text
material enters
-> source surface is detected
-> source-surface lens order is selected
-> Codex returns a 4-line card
-> optional 9-field markdown return record only if useful
```

This prevents the flow from collapsing back into an external-material-only ingest process.

## 3. cases

| Case | Source ref | Why tested |
| --- | --- | --- |
| A. generated report | `docs/reports/space_boundary_camera_lens_session6_normal_use_mini_trial_v0.md` | tests Codex-generated report as boundary material |
| B. runtime event artifact | `runtime/events/engine_event_ledger.jsonl` | tests runtime evidence/event material |

## 4. Case A. generated report

Command:

```text
python3 scripts/cli/space_boundary_lookup_packet.py docs/reports/space_boundary_camera_lens_session6_normal_use_mini_trial_v0.md
```

Helper result:

```yaml
source_surface:
  primary: generated_report
  confidence: medium
top_lenses:
  - user-intent
  - line/axis
  - risk
  - residue
  - return-state
```

Codex judgment:

```text
This report is not new external evidence. It is returned process material from the camera/lens package.
```

User-facing card:

```text
현재 판정: validation_return / process_residue
이유: 이 문서는 사용자의 전체 흐름 요청을 실제 pipeline trial로 돌린 결과라서, final 정의가 아니라 이후 정상 사용을 위한 반환 재료임
다음 이동: 새 재료가 들어올 때 source-surface lens order와 4줄 카드 기본값을 재사용
금지선: 보고서 문장을 baseline wording이나 새 schema로 승격 금지
```

9-field return record need:

```yaml
needed_now: no
reason: this report already contains its own return record candidate and closeout path
return_state: already_recorded_process_residue
```

## 5. Case B. runtime event artifact

Command:

```text
python3 scripts/cli/space_boundary_lookup_packet.py runtime/events/engine_event_ledger.jsonl
```

Helper result:

```yaml
source_surface:
  primary: runtime_artifact
  subtype: runtime_event
  confidence: medium
top_lenses:
  - evidence/event
  - technical
  - risk
  - residue
  - line/axis
```

Codex judgment:

```text
The ledger is not a summary source and not proof by itself. It is event/evidence material that needs slicing before supporting a concrete claim.
```

User-facing card:

```text
현재 판정: runtime_event / evidence_residue
이유: event ledger는 실제 발생 흔적이지만, 특정 event slice 없이 전체 ledger를 증거로 쓰면 과해석 위험이 있음
다음 이동: 필요할 때 event type, created output, succeeded/failed action, return-to-space relation을 좁혀서 읽음
금지선: ledger 존재만으로 실행 성공/구조 안정성/증거 확정으로 승격 금지
```

9-field return record need:

```yaml
needed_now: no
reason: there is no specific claim being validated in this trial
return_state: reread_priority / evidence_residue
future_record_condition: create a return record only when a concrete event slice is used to support a claim
```

## 6. cross-surface validation

| Check | Generated report | Runtime event | Judgment |
| --- | --- | --- | --- |
| Source surface detected | PASS | PASS | Different source surfaces were detected. |
| Lens order differs by surface | PASS | PASS | Generated report and runtime event did not share the same lens order. |
| Output stays compact | PASS | PASS | 4-line cards are enough. |
| Return record not forced | PASS | PASS | No unnecessary 9-field record was written. |
| Promotion avoided | PASS | PASS | No baseline, schema, or proof promotion. |
| Runtime JSON avoided | PASS | PASS | No runtime mutation. |

## 7. what this confirms

The normal-use default is not external-material-only.

It can handle at least:

- external material files
- generated reports
- runtime event artifacts

The important behavior is:

```text
same pipeline, different camera/lens order
```

not:

```text
same summary template for every input
```

## 8. observed friction

Runtime event artifacts still need a future event-slice convention.

Current healthy rule:

```text
do not create a full return record for broad runtime ledgers unless a specific claim or event slice is being validated.
```

## 9. verdict

```yaml
verdict: PASS_WITH_NOTE
ready_for_normal_use: true
writer_now: false
runtime_reingress_now: false
next_allowed_move: use normal pipeline on future real material; collect friction only when a material cannot be handled by 4-line card plus optional markdown record
```

