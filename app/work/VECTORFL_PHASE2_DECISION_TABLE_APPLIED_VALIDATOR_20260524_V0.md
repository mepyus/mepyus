# VECTORFL_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_20260524_V0

verdict: PASS_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_META_WITH_HOLD

run dir:
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_phase2_decision_table_applied_validator_v0

mode: FAST_NO_CALL_LOCAL_VALIDATION
Codex CLI: NO
Gemini CLI: NO

## applied priority order
1. FAIL_AUTHORITY_OVERPROMOTION
2. FAIL_OPERATOR_OVERLOAD
3. FAIL_HEAVY_ESCALATION_MISSING
4. FAIL_MODEL_ONLY_DRIFT
5. FAIL_NO_SPACE_REFERENCE
6. FAIL_SPACE_REFERENCE_DECORATION_ONLY


## result
- cases: 6
- blocked: 6
- checks: 9
- active_hits: 0
- elapsed_seconds: 0.0010449880000000002

## repair note
Validator evidence scan initially flagged its own forbidden-pattern literals; scan scope was repaired to generated evidence artifacts only. Applied classifier still blocked all drift fixtures.

HOLD: no authority/registry/current-position/promotion.

NEXT_SAFE_LANE:
PHASE2_SPACE_REFERENCE_DELTA_REAL_PACKET_DRY_RUN_WITH_DECISION_TABLE_NO_AUTHORITY_MUTATION_V0
