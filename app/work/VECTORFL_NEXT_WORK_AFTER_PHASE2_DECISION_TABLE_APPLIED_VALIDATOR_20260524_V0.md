# VECTORFL_NEXT_WORK_AFTER_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_20260524_V0

NEXT_SAFE_LANE: PHASE2_SPACE_REFERENCE_DELTA_REAL_PACKET_DRY_RUN_WITH_DECISION_TABLE_NO_AUTHORITY_MUTATION_V0

purpose:
Run a dry-run Phase2 packet on a new small space-reference-delta target using the applied decision-table validator.

Required:
- choose one small target that is not just validator plumbing
- read up to 4 refs by source-selection rule
- produce space_reference_delta
- run applied decision-table validator
- keep HOLD

Do not promote to schema/router/authority/current-position.
