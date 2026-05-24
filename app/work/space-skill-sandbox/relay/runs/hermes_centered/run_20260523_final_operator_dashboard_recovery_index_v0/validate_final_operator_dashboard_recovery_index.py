#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_END_OF_DAY_OPERATOR_RECOVERY_INDEX_20260523_V0.md','app/work/VECTORFL_FINAL_OPERATOR_DASHBOARD_20260523_V0.json','app/work/VECTORFL_NEXT_SESSION_QUICKSTART_CARD_20260523_V0.md']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
for tok in ['END_OF_DAY_OPERATOR_RECOVERY_INDEX_WITH_HOLD','FINAL_OPERATOR_DASHBOARD_WITH_HOLD','NEXT_SESSION_QUICKSTART_CARD_WITH_HOLD','TWELVE_CANDIDATE_PERSONAL_PROGRAM_CORE_CHAIN_WITH_MODEL_SAFE_REENTRY_PREPARED_AND_HOLD','no-model continuation only','Codex review-only audit only']:
    if tok not in text: problems.append('missing recovery token '+tok)
for tok in ['real Codex execution','real Gemini execution','live DB intake','v1 snapshot creation','write UI','schema/registry/baseline/workflow mutation','M4/module promotion']:
    if tok not in text: problems.append('missing approval boundary '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
dash=json.loads((ROOT/'app/work/VECTORFL_FINAL_OPERATOR_DASHBOARD_20260523_V0.json').read_text(encoding='utf-8'))
if dash.get('candidate_count')!=12: problems.append('candidate_count mismatch')
if dash.get('pass_with_hold_count')!=12: problems.append('pass_with_hold_count mismatch')
for k in ['real_codex_execution','real_gemini_execution','approval_applied','authority_mutation']:
    if dash.get(k)!='NO': problems.append(k+' drift')
if dash.get('promotion')!='HOLD': problems.append('promotion drift')
for bad in ['real_codex_execution: YES','real_gemini_execution: YES','approval_applied: YES','promotion_status: PROMOTED','program_alpha_status: READY']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_FINAL_OPERATOR_DASHBOARD_RECOVERY_INDEX_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_FINAL_OPERATOR_DASHBOARD_RECOVERY_INDEX_WITH_HOLD')
print('candidate_count=12')
print('pass_with_hold_count=12')
print('default_next=no-model continuation only')
print('real_codex_execution=NO')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
