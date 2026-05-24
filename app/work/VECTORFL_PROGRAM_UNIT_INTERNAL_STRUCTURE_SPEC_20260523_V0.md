# VECTORFL_PROGRAM_UNIT_INTERNAL_STRUCTURE_SPEC_20260523_V0

status: PROGRAM_UNIT_INTERNAL_STRUCTURE_SPEC_WITH_HOLD
created_at: 2026-05-23 09:50:36 KST

## 0. Why this spec exists

우리는 지금 단일 기능 하나를 만드는 것이 아니라, 프로그램 단위의 큰 틀 안에서 내부 구조를 설계하고 있다.

따라서 오늘 만든 산출물은 “완성 모듈”이 아니라, 개인 프로그램 단위 내부 구조를 안전하게 자라게 하기 위한 후보층/검증층/회수층이다.

This spec re-states what was created so far as a program-unit internal structure, while preserving HOLD.

## 1. Current correct classification

```text
TWELVE_CANDIDATE_PERSONAL_PROGRAM_CORE_CHAIN_WITH_MODEL_SAFE_REENTRY_PREPARED_AND_HOLD
```

Meaning:

```text
12 module candidates have local/no-model or synthetic/no-model evidence.
Model packets and recovery templates exist.
Operator recovery/index/checksum surfaces exist.
Authority and promotion remain unchanged.
```

## 2. Program-unit structure overview

```text
[1 input_layer]
  -> [2 evidence_layer]
  -> [3 review_guard_layer]
  -> [4 surface_layer]
  -> [5 tool_reentry_layer]
  -> [6 operator_recovery_layer]
```

이것은 구현된 router/runner가 아니다.
이것은 내부 구조 명세/후보 지도이다.

## 3. Internal layers

### input_layer

purpose:
```text
외부/개인 입력을 fixture/local 경계 안에서 위치시키는 층
```

current members:
- M-CAND-01 Input Localization
- M-CAND-02 Personal Intake coupling


boundary:
```text
live DB intake/write UI는 HOLD
```

status:
```text
CANDIDATE_STRUCTURE_WITH_HOLD
```

### evidence_layer

purpose:
```text
모든 작업을 receipt/evidence loop로 남기는 층
```

current members:
- M-CAND-04 Receipt Writer
- M-CAND-03 Evidence Loop Persistence


boundary:
```text
receipt는 authority 아님
```

status:
```text
CANDIDATE_STRUCTURE_WITH_HOLD
```

### review_guard_layer

purpose:
```text
promotion/authority/live drift를 STOP/HOLD로 잡는 층
```

current members:
- M-CAND-05 HOLD Review State
- M-CAND-06 Live-Safety Validator
- M-CAND-12 Module Extraction Gate


boundary:
```text
M4/Program Alpha 승격 금지
```

status:
```text
CANDIDATE_STRUCTURE_WITH_HOLD
```

### surface_layer

purpose:
```text
사람이 읽고 재현할 수 있는 read-only/status/replay 층
```

current members:
- M-CAND-08 Read-only Surface
- M-CAND-07 Deterministic Stable Cycle


boundary:
```text
write UI/v1 snapshot 아님
```

status:
```text
CANDIDATE_STRUCTURE_WITH_HOLD
```

### tool_reentry_layer

purpose:
```text
Codex/Gemini/ChatGPT 결과를 raw/lite/receipt/re-entry로만 받아들이는 층
```

current members:
- M-CAND-09 Cross-tool Re-entry synthetic
- M-CAND-10 Codex Review Guard synthetic
- M-CAND-11 Gemini Gap Scan Lens synthetic


boundary:
```text
실제 모델 실행/권한 상속 아님
```

status:
```text
CANDIDATE_STRUCTURE_WITH_HOLD
```

### operator_recovery_layer

purpose:
```text
다음 세션/다른 도구가 이어받게 하는 회수 표면
```

current members:
- handoff
- operator dashboard
- checksum index
- quickstart card


boundary:
```text
baseline freeze/authority registry 아님
```

status:
```text
CANDIDATE_STRUCTURE_WITH_HOLD
```

## 4. 12 candidate chain as internal program skeleton

```text
M-CAND-01 Input Localization
-> M-CAND-02 Personal Intake coupling
-> M-CAND-04 Receipt Writer
-> M-CAND-05 HOLD Review State
-> M-CAND-08 Read-only Surface
-> M-CAND-03 Evidence Loop Persistence
-> M-CAND-06 Live-Safety Validator
-> M-CAND-07 Deterministic Stable Cycle
-> M-CAND-12 Module Extraction Gate
-> M-CAND-10 Codex Review Guard synthetic
-> M-CAND-09 Cross-tool Re-entry synthetic
-> M-CAND-11 Gemini Gap Scan Lens synthetic
```

This chain should be read as:

```text
input is localized
personal intake stays fixture/local
receipts are emitted
HOLD review blocks overclaim
read-only surface exposes state
persistence is evidence loop only
live-safety blocks shared/live mutation
stable cycle checks deterministic replay shape
module gate blocks M4/promotion claims
Codex guard blocks review-to-authority drift
cross-tool re-entry blocks hidden transport/role inheritance
Gemini lens keeps exploration as candidate/WATCH only
```

## 5. What we created in this round

### Handoff/recovery set

```text
app/work/CHATGPT_CODEX_GEMINI_SAME_DAY_FINAL_HANDOFF_UPDATE_20260523_V0.md
app/work/VECTORFL_END_OF_DAY_OPERATOR_RECOVERY_INDEX_20260523_V0.md
app/work/VECTORFL_FINAL_OPERATOR_DASHBOARD_20260523_V0.json
app/work/VECTORFL_NEXT_SESSION_QUICKSTART_CARD_20260523_V0.md
app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_20260523_V0.md
app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_20260523_V0.json
app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_QUICK_VERIFY_20260523_V0.md
```

### 12-candidate set

```text
app/work/VECTORFL_TWELVE_CANDIDATE_PERSONAL_PROGRAM_COMPLETE_CHAIN_RECEIPT_20260523_V0.md
app/work/VECTORFL_TWELVE_CANDIDATE_CONSOLIDATION_DASHBOARD_20260523_V0.json
app/work/VECTORFL_TWELVE_CANDIDATE_USER_STATUS_CARD_20260523_V0.md
app/work/VECTORFL_TWELVE_CANDIDATE_HOLD_STOP_COVERAGE_MAP_20260523_V0.md
```

### Model-safe preparation set, not executed

```text
app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_twelve_candidate_dashboard_20260523_v0/PACKET.md
app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_gap_scan_twelve_candidate_dashboard_20260523_v0/PACKET.md
app/work/VECTORFL_MODEL_EXECUTION_DECISION_CARD_20260523_V0.md
app/work/VECTORFL_MODEL_EXECUTION_APPROVAL_BOUNDARY_MAP_20260523_V0.json
app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_model_result_intake_reentry_dry_run_v0/
app/work/space-skill-sandbox/relay/templates/post_model_run_receipt_pack_20260523_v0/
```

## 6. Structural rules before next work

Before adding new structure, check these:

```text
1. Does the new thing belong to input, evidence, guard, surface, tool_reentry, or operator_recovery layer?
2. Does it have a declared input boundary?
3. Does it produce a declared local artifact?
4. Does it produce a receipt?
5. Does it preserve STOP/HOLD behavior?
6. Does it avoid authority inheritance?
7. Does it avoid live DB intake/write UI/schema/registry/baseline mutation?
8. Does it avoid claiming M3/M4/Program Alpha readiness?
```

## 7. Next work direction

Default next step without explicit approval:

```text
no-model continuation: structure gap review across the six internal layers
```

Concrete next artifact:

```text
VECTORFL_PROGRAM_UNIT_STRUCTURE_GAP_REVIEW_20260523_V0.md
```

Purpose:

```text
find which internal layers are under-specified before any implementation/promotion/model execution
```

## 8. Not this

```text
not M4 reusable module
not Program Alpha ready
not promotion complete
not authority updated
not router/runner implemented
not live DB intake
not write UI
not real Codex execution
not real Gemini execution
not schema/registry/baseline/workflow mutation
not v1 snapshot
not baseline freeze
```

## 9. HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
approval_applied: no
live_db_intake: HOLD
schema_mutation: no
snapshot_mutation: no
router_runner_claim: no
write_ui: no
authority_database: no
shared_db_mutation: no
v1_snapshot_creation: no
m4_reusable_module: no
module_promotion: no
program_alpha_ready: no
