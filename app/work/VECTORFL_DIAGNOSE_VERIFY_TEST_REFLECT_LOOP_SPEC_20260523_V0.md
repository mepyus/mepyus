# VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_20260523_V0

status: DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_WITH_HOLD
created_at: 2026-05-23 11:06:11 KST

## 0. Why this exists

User correction:

```text
진단/검증/테스트/반영을 필수 요소에 포함시켜야 한다.
너무 닫아서 리허설/드라이런만 반복하면 실제 contract drift를 놓친다.
```

This spec makes the loop mandatory for future VectorFL/Hermes work.

## 1. Required work loop

Every bounded VectorFL continuation must state which step it is in:

```text
S1 Diagnose: identify current claim, risk, gap, stale index, or contract pressure.
S2 Verify: check local files/receipts/checksums/declared inputs before adding material.
S3 Test: run a bounded local validator or, when explicitly approved, one real bounded tool/model test.
S4 Reflect: compare expected vs actual result, including CLI/tool quirks and contract drift.
S5 Apply: update only non-authority specs/receipts/bundles needed to preserve recovery.
S6 Surface: write a user/status card that preserves HOLD/WATCH/STOP labels.
S7 Receipt: record read_before_work/files_touched/commands_run/state_mutations/HOLD.
S8 Decide next: stop, repair, choose one layer, or request separate approval for a real test.
```

## 2. Real-test insertion rule

Rehearsal and dry-run work is allowed, but not sufficient forever.
Periodic real bounded tests must be inserted when:

```text
- a packet contract claims a tool can execute it
- a CLI command template has not been exercised recently
- a recovery/index/checksum surface has grown large enough to drift
- user explicitly requests actual testing
- a no-model rehearsal assumes behavior of Codex/Gemini/Hermes CLI
```

Real bounded test does NOT mean broad execution.
It means one declared packet, one declared output path, explicit scope, and post-run Hermes verification.

## 3. Test lane types

| lane | allowed when | output status | HOLD boundary |
|---|---|---|---|
| local_validator | always if file scope is declared | deterministic validation evidence | not implementation readiness |
| fixture_rehearsal | no external approval needed | synthetic candidate evidence | not live DB or real model output |
| real_codex_review_only | explicit user approval / packet approval | review evidence only | not authority/promotion/M4 |
| real_gemini_gap_scan | explicit user approval / packet approval | broad scan evidence only | not truth/authority |
| live_db_or_write_ui | separate future authority only | not currently allowed | HOLD |

## 4. Mandatory reflection fields

Each receipt after a real or local test must include:

```text
diagnosis:
verification:
test_run:
actual_result:
contract_drift_found:
reflection:
applied_change:
not_applied:
next_smallest_action:
```

## 5. What the real Codex test proved

The bounded Codex review-only audit found:

```text
DIRECTION_MATCHES_PROGRAM_UNIT_INTERNAL_STRUCTURE_BUILDUP_WITH_HOLD
quickstart_bundle_index_stale_exists_false
codex_cli_0.133.0_exec_flag_contract_drift
output_last_message_capture_issue_with_-o
```

This proves the user's correction is valid:

```text
closed rehearsal alone would not have caught these real CLI/index contract issues.
```

## 6. Required interpretation

```text
real bounded test = evidence and diagnostic pressure
not promotion
not authority mutation
not Program Alpha readiness
not M4 module confirmation
not live DB intake
```

## 7. HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
real_codex_execution: YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET
real_gemini_execution: no
approval_applied_to_promotion: no
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
