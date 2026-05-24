# VECTORFL_PHASE2_SOURCE_SELECTION_RULE_REAL_USE_20260524_V0

verdict: PASS_PHASE2_SOURCE_SELECTION_RULE_REAL_USE_WITH_HOLD

run dir:
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_phase2_source_selection_rule_real_use_v0

target:
Phase2 source-selection rule candidate

mode:
FAST_NO_CALL_LOCAL_VALIDATION

new Codex/Gemini calls:
NO_SKIPPED_BY_BUDGET_GATE

## source-selection candidate 핵심

primary_refs:
Use current user original + immediate predecessor PASS/HOLD report + latest next-work card + one domain/pressure artifact if it changes judgment.

secondary_refs:
Use older/broader space artifacts only when current refs conflict, are insufficient, or trigger architecture/layer ambiguity.

required_for_each_ref:
- absolute_path
- exists
- sha256
- used_for
- changed_judgment

reject_ref_when:
- no changed_judgment
- citation is only decorative
- reference increases operator load without changing decision
- reference is authority/current-position/registry unless explicitly approved for read-only orientation


max_default_refs: 4

## validation
- checks: 11
- negative_cases: 5
- active_hits: 0
- elapsed_seconds: 0.0009540830069454387

HOLD: no authority/registry/current-position/promotion.

NEXT_SAFE_LANE:
PHASE2_SOURCE_SELECTION_RULE_NEGATIVE_DRIFT_TEST_NO_AUTHORITY_MUTATION_V0
