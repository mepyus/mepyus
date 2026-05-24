#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_20260523_V0.md','app/work/VECTORFL_REUSABLE_INTERNAL_STRUCTURE_SPEC_20260523_V0.md','app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_DASHBOARD_20260523_V0.json','app/work/VECTORFL_NEXT_WORK_AFTER_PROGRAM_UNIT_PROGRESS_REVIEW_20260523_V0.md','app/work/VECTORFL_PROGRAM_UNIT_PROGRESS_REVIEW_USER_STATUS_CARD_20260523_V0.md']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
dash=json.loads((ROOT/'app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_DASHBOARD_20260523_V0.json').read_text(encoding='utf-8'))
for tok in ['PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_WITH_HOLD','REUSABLE_INTERNAL_STRUCTURE_SPEC_CANDIDATE_WITH_HOLD','PROGRAM_UNIT_STRUCTURE_PROGRESS_DASHBOARD_WITH_HOLD','NEXT_WORK_AFTER_PROGRAM_UNIT_PROGRESS_REVIEW_WITH_HOLD','PROGRAM_UNIT_PROGRESS_REVIEW_USER_STATUS_CARD_WITH_HOLD','DIRECTION_MATCHES_PROGRAM_UNIT_INTERNAL_STRUCTURE_BUILDUP_WITH_HOLD','VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md']:
    if tok not in text: problems.append('missing token '+tok)
for layer in ['input_layer','evidence_layer','review_guard_layer','surface_layer','tool_reentry_layer','operator_recovery_layer']:
    if layer not in text: problems.append('missing layer '+layer)
for tok in ['trace ledger row shape','guard status matrix','surface-to-evidence coupling','model re-entry capture contract','operator recovery shape']:
    if tok not in text: problems.append('missing reusable spec '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','schema_mutation: no','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
if dash.get('direction_fit')!='YES_WITH_HOLD': problems.append('direction_fit drift')
if dash.get('component_count')!=8: problems.append('component_count mismatch')
for k in ['model_execution','real_codex_execution','real_gemini_execution','authority_mutation','schema_mutation','shared_db_mutation']:
    if dash.get(k)!='NO': problems.append(k+' drift')
if dash.get('promotion')!='HOLD': problems.append('promotion drift')
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','model_execution: YES','real_codex_execution: YES','real_gemini_execution: YES','schema_mutation: YES','authority_mutation: YES','approval_applied: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_WITH_HOLD')
print('direction_fit=YES_WITH_HOLD')
print('component_count=8')
print('reusable_spec=CREATED')
print('next_work=compact_recovery_bundle_index_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
