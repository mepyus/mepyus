#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_GAP_REVIEW_20260523_V0.md','app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_GAP_DASHBOARD_20260523_V0.json','app/work/VECTORFL_NEXT_WORK_AFTER_STRUCTURE_GAP_REVIEW_20260523_V0.md','app/work/VECTORFL_STRUCTURE_GAP_USER_STATUS_CARD_20260523_V0.md']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
for tok in ['PROGRAM_UNIT_STRUCTURE_GAP_REVIEW_WITH_HOLD','PROGRAM_UNIT_STRUCTURE_GAP_DASHBOARD_WITH_HOLD','NEXT_WORK_AFTER_STRUCTURE_GAP_REVIEW_WITH_HOLD','STRUCTURE_GAP_USER_STATUS_CARD_WITH_HOLD','input_layer','evidence_layer','review_guard_layer','surface_layer','tool_reentry_layer','operator_recovery_layer','GAP-01','GAP-02','GAP-03','GAP-04','GAP-05','GAP-06','VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0.md']:
    if tok not in text: problems.append('missing gap token '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
dash=json.loads((ROOT/'app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_GAP_DASHBOARD_20260523_V0.json').read_text(encoding='utf-8'))
if dash.get('layer_count') != 6: problems.append('layer_count mismatch')
if len(dash.get('gaps',[])) != 6: problems.append('gaps length mismatch')
for k in ['model_execution','real_codex_execution','real_gemini_execution','approval_applied','authority_mutation']:
    if dash.get(k) != 'NO': problems.append(k+' drift')
if dash.get('promotion') != 'HOLD': problems.append('promotion drift')
for bad in ['real_codex_execution: YES','real_gemini_execution: YES','approval_applied: YES','promotion_status: PROMOTED','program_alpha_status: READY','authority_mutation: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_PROGRAM_UNIT_STRUCTURE_GAP_REVIEW_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_PROGRAM_UNIT_STRUCTURE_GAP_REVIEW_WITH_HOLD')
print('layer_count=6')
print('gap_count=6')
print('next_work=trace_ledger_schema_candidate_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
