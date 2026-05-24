# CODEX_WORKER_REQUEST — Compact Recovery Bundle Review-Only Audit

status: REAL_CODEX_REVIEW_ONLY_TEST_REQUEST_WITH_HOLD
created_at: 2026-05-23 10:52:38 KST

## 0. User approval basis

User selected option C and said actual tests are required:

```text
c. 실제 테스트로 돌려봐야 함! 우리는 실제 동작하지 않고 리허설과 드라이런을 계속 돌리기 때문에 중간 중간에 점검/검증/테스트가 필수야!
```

This is interpreted as approval for this single bounded Codex review-only test packet only.

## 1. Approval block

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
APPROVED_PACKET_PATH: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/PACKET.md
APPROVED_CODEX_WORKER_REQUEST: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/CODEX_WORKER_REQUEST.md
APPROVED_OUTPUT_DIR: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_real_codex_review_only_bundle_audit_v0/codex_output
APPROVED_CODEX_COMMAND: codex exec --sandbox read-only --ask-for-approval never < app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/PROMPT.txt
APPROVED_GEMINI_COMMAND: none
APPROVED_NETWORK_SCOPE: model_api_transport_only
APPROVED_LIVE_WEB_SOURCE_LOOKUP: no
APPROVED_EXTERNAL_CONNECTOR: no
APPROVED_PROMOTION: no
```

## 2. Declared input files Codex may read

Read only these declared files:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/VECTORFL_COMPACT_RECOVERY_QUICKSTART_20260523_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/VECTORFL_REUSE_LOOKUP_SPEC_20260523_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/VECTORFL_REUSABLE_INTERNAL_STRUCTURE_SPEC_20260523_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_20260523_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/VECTORFL_TWELVE_CANDIDATE_PERSONAL_PROGRAM_COMPLETE_CHAIN_RECEIPT_20260523_V0.md
```

## 3. Required output

Write exactly one output file:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_real_codex_review_only_bundle_audit_v0/codex_output/codex_recovery_return.md
```

Required sections:

```text
verdict
scope_validity
direction_fit_assessment
contract_gaps
test_value
WATCH
HOLD
recovery_class_hint
next_smallest_action
```

## 4. Hard prohibitions

```text
Do not edit source files.
Do not modify authority files.
Do not write anywhere except the declared output file.
Do not run Gemini.
Do not use browser/live web/source lookup/MCP/external connectors.
Do not access secrets, memory, skills, cron, config, auth files, or system keychains.
Do not claim approval/promotion/M4/Program Alpha readiness.
Do not mutate schema/registry/baseline/workflow/shared DB.
```


## CLI compatibility correction

updated_at: 2026-05-23 10:53:16 KST

The originally recorded `--ask-for-approval never` flag is not supported by codex-cli 0.133.0.
Corrected approved command for this same packet-bound test:

```bash
codex exec -s workspace-write -C /Users/sungsookim/universe/vectorfl_replica -o /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_real_codex_review_only_bundle_audit_v0/codex_output/codex_recovery_return.md - < /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/PROMPT.txt
```

Boundary remains unchanged:
- review-only
- output path only
- model_api_transport_only
- no Gemini
- no authority mutation
- no promotion


## Second CLI compatibility correction

updated_at: 2026-05-23 10:54:56 KST

The `-o/--output-last-message` option overwrote the file with Codex's final short message. Corrected command removes `-o` so Codex writes the declared file itself:

```bash
codex exec -s workspace-write -C /Users/sungsookim/universe/vectorfl_replica - < /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/PROMPT.txt
```

This is the same single bounded review-only packet; first model attempt exposed an output-capture contract issue and is preserved in logs.
