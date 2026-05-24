#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0.md','app/work/VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0.json','app/work/VECTORFL_NEXT_WORK_AFTER_CROSS_LAYER_GUARD_MATRIX_20260523_V0.md','app/work/VECTORFL_CROSS_LAYER_GUARD_MATRIX_USER_STATUS_CARD_20260523_V0.md','app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_cross_layer_guard_matrix_candidate_v0/fixtures/cross_layer_guard_matrix_fixture.json']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
fixture=json.loads((ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_cross_layer_guard_matrix_candidate_v0/fixtures/cross_layer_guard_matrix_fixture.json').read_text(encoding='utf-8'))
dashboard=json.loads((ROOT/'app/work/VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0.json').read_text(encoding='utf-8'))
allowed={'PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'}
layers={'input_layer','evidence_layer','review_guard_layer','surface_layer','tool_reentry_layer','operator_recovery_layer'}
if set(fixture.get('allowed_guard_status',[])) != allowed: problems.append('allowed guard set mismatch')
if set(fixture.get('layers',[])) != layers: problems.append('layer set mismatch')
if fixture.get('case_count') != 12: problems.append('fixture case_count mismatch')
if dashboard.get('case_count') != 12: problems.append('dashboard case_count mismatch')
for c in fixture.get('cases',[]):
    if c.get('layer') not in layers: problems.append('bad layer '+c.get('case_id','?'))
    if c.get('guard_status') not in allowed: problems.append('bad guard '+c.get('case_id','?'))
    gs=c.get('guard_status')
    label=c.get('surface_label_rule','')
    if gs in ['HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'] and gs not in label:
        problems.append('label softens '+gs+' '+c.get('case_id','?'))
for tok in ['CROSS_LAYER_GUARD_MATRIX_CANDIDATE_WITH_HOLD','CROSS_LAYER_GUARD_MATRIX_DASHBOARD_WITH_HOLD','NEXT_WORK_AFTER_CROSS_LAYER_GUARD_MATRIX_WITH_HOLD','CROSS_LAYER_GUARD_MATRIX_USER_STATUS_CARD_WITH_HOLD','VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_20260523_V0.md']:
    if tok not in text: problems.append('missing token '+tok)
for tok in ['PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT']:
    if tok not in text: problems.append('missing guard token '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','schema_mutation: no','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for data_name,data in [('fixture',fixture),('dashboard',dashboard)]:
    for k in ['model_execution','real_codex_execution','real_gemini_execution','authority_mutation','schema_mutation','shared_db_mutation']:
        if data.get(k)!='NO': problems.append(data_name+' '+k+' drift')
    if data.get('promotion')!='HOLD': problems.append(data_name+' promotion drift')
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','model_execution: YES','real_codex_execution: YES','real_gemini_execution: YES','schema_mutation: YES','authority_mutation: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_WITH_HOLD')
print('layer_count=6')
print('guard_status_count=5')
print('case_count=12')
print('next_work=surface_to_evidence_trace_map_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
