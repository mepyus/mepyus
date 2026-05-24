#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
out=ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_real_codex_review_only_bundle_audit_v0/codex_output/codex_recovery_return.md'
problems=[]
if not out.exists():
    problems.append('missing codex output')
    text=''
else:
    text=out.read_text(encoding='utf-8')
for section in ['# Codex Recovery Return','## verdict','## scope_validity','## direction_fit_assessment','## contract_gaps','## test_value','## WATCH','## HOLD','## recovery_class_hint','## next_smallest_action']:
    if section not in text: problems.append('missing section '+section)
for token in ['DIRECTION_MATCHES_PROGRAM_UNIT_INTERNAL_STRUCTURE_BUILDUP_WITH_HOLD','no promotion','no authority mutation','no Program Alpha readiness','no M4 module confirmation','no live DB intake','no real Gemini execution','Codex review is evidence only','REVIEW_ONLY_DIRECTION_MATCH_WITH_HOLD_AND_INDEX_INTEGRITY_WATCH']:
    if token not in text: problems.append('missing token '+token)
for token in ['exists=FALSE sha256=PENDING_OR_MISSING','recovery-index integrity gap']:
    if token not in text: problems.append('missing detected gap '+token)
for bad in ['promotion_status: PROMOTED','Program Alpha readiness: YES','M4 module confirmation: YES','live DB intake enabled','real Gemini execution: YES','authority mutation: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_REAL_CODEX_REVIEW_ONLY_BUNDLE_AUDIT_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_REAL_CODEX_REVIEW_ONLY_BUNDLE_AUDIT_WITH_HOLD')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY')
print('real_gemini_execution=NO')
print('direction_fit=YES_WITH_HOLD')
print('gap_detected=quickstart_bundle_index_stale_exists_false')
print('authority_mutation=NO')
print('promotion=HOLD')
