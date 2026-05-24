# PACKET — Real Codex Review-Only Compact Recovery Bundle Audit

status: CODEX_REVIEW_ONLY_COMPACT_RECOVERY_BUNDLE_PACKET_APPROVED_FOR_SINGLE_TEST_WITH_HOLD
created_at: 2026-05-23 10:52:38 KST

REQUEST:
`/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/CODEX_WORKER_REQUEST.md`

OUTPUT_DIR:
`/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_real_codex_review_only_bundle_audit_v0/codex_output`

APPROVED_COMMAND:
```bash
codex exec --sandbox read-only --ask-for-approval never < app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_compact_recovery_bundle_20260523_v0/PROMPT.txt
```

BOUNDARY:
```text
real_codex_execution: YES_FOR_THIS_SINGLE_REVIEW_ONLY_TEST
real_gemini_execution: NO
live_web_source_lookup: NO
external_connector: NO
authority_mutation: NO
promotion: HOLD
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
