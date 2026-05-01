# Space Feedback Loop Scriptability Feasibility Reread v0

## 1. status

```yaml
report_status: scriptability_feasibility_reread
based_on: docs/reports/space_feedback_loop_scriptability_audit_v0.md
verdict: PASS_WITH_NOTE
script_created_now: false
implementation_now: false
schema_enforcement: false
runtime_manifest: false
baseline_lock: false
```

## 2. purpose

This reread narrows the prior scriptability audit into implementation-feasible pieces.

The core question:

```text
현재 repo의 기존 scripts/runtime 자산을 재사용하면,
공간 사용 루프 중 어디를 실제로 스크립트화할 수 있는가?
```

## 3. existing reusable script/runtime assets

| Existing asset | Reusable for | Feasibility |
| --- | --- | --- |
| `scripts/record_operation_event.py` | append operation/event records | already usable |
| `scripts/cli/run_phase1_space_query.py` | full question packet -> exploration -> merge/diff/hold -> reingress chain | usable but heavy |
| `scripts/cli/build_question_packet.py` | infer rough mode and select known targets | reusable partially |
| `scripts/cli/explore_space.py` | read selected assets and produce evidence units | reusable for heavier runs |
| `scripts/cli/write_reingress_record.py` | create reingress record after a run | reusable after judgment |
| `scripts/run_external_input_gate.py` | determine whether external file can be directly ingested or needs preprocessing | already usable for file inputs |
| `scripts/run_external_case_raw_intake_probe.py` | quick raw texture probe for external files | already usable for local files |
| `app/runtime/internal_search_minimum.py` | search internal observation/capability candidates | reusable for lookup packet |
| `app/core/runtime/live_input.py` | real live input ingest into runtime formation service | too mutating for default loop |
| `app/core/runtime/live_input_space.py` | form local space from live input | too mutating for default loop |

## 4. practical separation

There are three implementation zones.

### Zone A. Already scriptable now

These need no new conceptual work.

```yaml
operation_event_recording:
  existing: scripts/record_operation_event.py
  status: ready
  risk: low

external_file_gate:
  existing: scripts/run_external_input_gate.py
  status: ready_for_local_file_inputs
  risk: low

raw_external_file_probe:
  existing: scripts/run_external_case_raw_intake_probe.py
  status: ready_for_local_file_inputs
  risk: low

phase1_query_chain:
  existing: scripts/cli/run_phase1_space_query.py
  status: ready_but_heavy
  risk: medium
```

### Zone B. Small new helper is justified

These are not covered cleanly by current scripts, but can be implemented without runtime mutation.

```yaml
space_boundary_lookup_packet:
  proposed_path: scripts/cli/space_boundary_lookup_packet.py
  mode: read_only
  purpose: produce compact context packet from known indexes and simple source-surface detection
  risk: low_if_suggestion_only

translation_base_slice:
  proposed_path: scripts/cli/translation_base_slice.py
  mode: read_only
  purpose: extract a small language-base subset by source type
  risk: low
```

### Zone C. Do not script yet

These still require Codex judgment.

```yaml
final_state_judgment:
  status: codex_only

active_lens_selection:
  status: codex_only

promotion_or_action_decision:
  status: codex_only

direct_evidence_vs_comparison_frame:
  status: codex_only

guarded_execution_elevation:
  status: codex_only

automatic_microspace_index_mutation:
  status: hold
```

## 5. candidate-by-candidate feasibility

### 5.1 `space_boundary_lookup_packet.py`

Feasibility:

```yaml
implementation_size: small
mutation: none
depends_on:
  - pathlib
  - re
  - json
  - existing markdown/index files
optional_dependency:
  - app/runtime/internal_search_minimum.py
```

Input:

```text
raw user input or --input-file
```

Output:

```yaml
input_ref:
source_surface_guess:
matched_indexes:
matched_microspace_clusters:
candidate_assets:
candidate_lenses:
known_guardrails:
card_template:
```

What it can decide:

- URL vs local path vs plain text
- whether input looks like external material, runtime artifact, generated report, or conversation material
- which known index files mention matching terms
- whether external material microspace has a related cluster
- which lens labels appear relevant by keyword

What it must not decide:

- final object_type
- final state
- direct evidence vs comparison frame
- index update permission
- execution permission

Verdict:

```yaml
priority: 1
build_readiness: READY_FOR_SMALL_READ_ONLY_IMPLEMENTATION
```

### 5.2 `translation_base_slice.py`

Feasibility:

```yaml
implementation_size: small
mutation: none
depends_on:
  - docs/indexes/space_translation_language_base_v0.md
```

Input:

```text
--source-type external_material | codex_handoff | user_surface | runtime_return | all
```

Output:

```yaml
selected_terms:
do_not_reduce:
bridge_phrases:
guardrails:
```

Why useful:

```text
외부도구에 전체 번역 베이스를 주면 토큰이 커진다.
source type별 작은 slice가 있으면 번역 보존 조건만 빠르게 줄 수 있다.
```

Verdict:

```yaml
priority: 2
build_readiness: READY_AFTER_LOOKUP_PACKET
```

### 5.3 `space_return_record_writer.py`

Feasibility:

```yaml
implementation_size: medium
mutation: yes
depends_on:
  - scripts/record_operation_event.py
  - optional markdown report template
```

Why not first:

```text
기록기는 쓰기 작업이므로, 기록 기준이 먼저 안정되어야 한다.
지금 만들면 trivial answer까지 기록해 문서/이벤트 노이즈를 만들 수 있다.
```

Verdict:

```yaml
priority: 3
build_readiness: HOLD_UNTIL_LOOKUP_PACKET_TRIAL
```

### 5.4 `external_material_cockpit_card.py`

Feasibility:

```yaml
implementation_size: small
mutation: none
```

Why not separate first:

```text
cockpit card는 lookup packet 출력 내부에 포함하면 충분하다.
별도 script로 분리하면 또 하나의 양식처럼 보일 위험이 있다.
```

Verdict:

```yaml
priority: 4
build_readiness: DO_NOT_SEPARATE_YET
```

### 5.5 full automated boundary-material pipeline

Feasibility:

```yaml
implementation_size: large
mutation: likely
risk: high
```

Why not:

- would blur Codex judgment and script output
- would likely create schema pressure
- could mutate microspace/index too early
- could make web fetching / runtime ingest feel automatic

Verdict:

```yaml
priority: none
build_readiness: NOT_READY
```

## 6. recommended minimal build order

If implementation is opened later, use this order.

```text
1. Build read-only lookup packet helper.
2. Test it on 3 live inputs:
   - URL external material
   - generated report path
   - user conversation excerpt
3. Only if useful, add translation-base slice helper.
4. Only after repeated use, add optional event/return writer.
```

## 7. how token savings would happen

Current expensive pattern:

```text
Codex rereads multiple large docs:
space_boundary_material_flow_map
external_material_microspace_index
translation_language_base
usage_manual
recent closeout
```

Desired cheap pattern:

```text
script reads known indexes
→ emits compact lookup packet
→ Codex reads only packet + maybe 1-2 source docs
```

Expected savings:

```yaml
best_case: large
reason: repeated index/context reading becomes one compact packet
limit: judgment still requires Codex reasoning
```

## 8. why existing phase1 query chain is not enough

`scripts/cli/run_phase1_space_query.py` is useful, but it is too heavy as the default live-use helper.

It creates:

- question packet
- exploration result
- merge/diff/hold report
- reingress record

That is appropriate for a bounded query run, but too much for every incoming boundary material.

The missing helper is lighter:

```text
lookup packet only
no merge
no reingress
no mutation
no final state
```

## 9. direct answer

Scriptable with high confidence:

- source surface guess
- known index lookup
- external material cluster suggestion
- candidate lens suggestion
- guardrail extraction
- cockpit card template
- operation event append when explicitly needed

Codex must keep:

- intent reading
- final lens selection
- state judgment
- next move judgment
- promotion barrier wording
- deciding whether to write/update any space record

## 10. verdict

```yaml
verdict: PASS_WITH_NOTE
most_implementable_now:
  - scripts/cli/space_boundary_lookup_packet.py
implementation_mode:
  - read_only
  - suggestion_only
  - no runtime mutation
  - no index update
best_reuse:
  - docs/indexes/space_boundary_material_flow_map_v0.md
  - docs/indexes/external_material_microspace_index_v0.md
  - docs/indexes/space_translation_language_base_v0.md
  - docs/guides/space_asset_retrieval_manual_v0.md
  - docs/notes/executable_runner_index_v0.md
defer:
  - return record writer
  - automatic microspace mutation
  - full boundary-material pipeline
```

## 11. next recommended move

The next bounded action, if the user wants implementation, should be:

```text
Implement scripts/cli/space_boundary_lookup_packet.py as a read-only helper.
```

Acceptance criteria:

- accepts raw text or path
- emits JSON only
- reads only known indexes
- suggests but does not decide
- includes cockpit card template
- does not fetch web
- does not write files
- does not update runtime

