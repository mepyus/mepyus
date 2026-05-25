# U_RUN_BUNDLE_EVIDENCE_RETENTION_RULE_CANDIDATE_V0

status: RULE_CANDIDATE_ONLY / NOT_AUTHORITY / NO_ARCHIVE / NO_DELETE / HOLD

scan_count: 41449
review_sample_count: 32

## rules
- URB_R01_PRESERVE_VALIDATION_RECEIPT_EVIDENCE
  - evidence_count: 213
  - policy: preserve pointer/index and compact view; never auto-delete
  - forbidden: delete, archive, move, treat as authority registry
- URB_R02_FREEZE_AUTHORITY_SENSITIVE_RUN_BUNDLE
  - evidence_count: 4885
  - policy: freeze pointer-only until authority boundary review
  - forbidden: promotion, registry mutation, current-position mutation, archive/delete
- URB_R03_COMPACT_GENERATED_RUN_BUNDLE
  - evidence_count: 1835
  - policy: compact generated runs into operator view before any cleanup consideration
  - forbidden: auto-archive, auto-delete, bulk move
- URB_R04_HOLD_CLEANUP_LANGUAGE_BUNDLE
  - evidence_count: 573
  - policy: cleanup-language run bundles require explicit manifest/rollback before apply
  - forbidden: cleanup apply, archive, move, delete
- URB_R05_GENERAL_RUN_BUNDLE_POINTER_ONLY
  - evidence_count: 33943
  - policy: general run bundles remain pointer-only until grouped by evidence value
  - forbidden: source-of-truth substitution, bulk cleanup

## future apply preconditions
- explicit user approval id
- filled archive/delete/move manifest
- rollback manifest
- post-apply validation plan
- authority-boundary review
- secret/redaction check
- negative drift tests
