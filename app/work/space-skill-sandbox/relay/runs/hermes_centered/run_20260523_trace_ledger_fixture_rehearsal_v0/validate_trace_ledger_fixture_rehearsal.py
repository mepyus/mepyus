#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
ledger=ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_trace_ledger_fixture_rehearsal_v0/fixtures/six_layer_trace_ledger_fixture.json'
files=['app/work/VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_FIXTURE_REHEARSAL_20260523_V0.md','app/work/VECTORFL_TRACE_LEDGER_FIXTURE_REHEARSAL_DASHBOARD_20260523_V0.json','app/work/VECTORFL_NEXT_WORK_AFTER_TRACE_LEDGER_FIXTURE_REHEARSAL_20260523_V0.md','app/work/VECTORFL_TRACE_LEDGER_FIXTURE_REHEARSAL_USER_STATUS_CARD_20260523_V0.md','app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_trace_ledger_fixture_rehearsal_v0/fixtures/six_layer_trace_ledger_fixture.json']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
data=json.loads(ledger.read_text(encoding='utf-8'))
allowed_layers={'input_layer','evidence_layer','review_guard_layer','surface_layer','tool_reentry_layer','operator_recovery_layer'}
allowed_guard={'PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'}
rows=data.get('rows',[])
if len(rows)!=6: problems.append('row_count mismatch')
if set(r.get('source_layer') for r in rows)!=allowed_layers: problems.append('layer coverage mismatch')
required=['trace_id','created_at','source_layer','source_artifact','receipt_ref','guard_status','surface_label','authority_effect','promotion_status','next_action','watch_notes']
for r in rows:
    for k in required:
        if k not in r: problems.append('missing '+k+' in '+str(r.get('trace_id')))
    if r.get('source_layer') not in allowed_layers: problems.append('bad layer '+str(r.get('trace_id')))
    if r.get('guard_status') not in allowed_guard: problems.append('bad guard '+str(r.get('trace_id')))
    if r.get('authority_effect')!='NO_AUTHORITY_MUTATION': problems.append('authority drift '+str(r.get('trace_id')))
    if r.get('promotion_status')!='HOLD': problems.append('promotion drift '+str(r.get('trace_id')))
    label=(r.get('surface_label') or '')
    gs=r.get('guard_status')
    if gs in ['HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'] and gs not in label:
        problems.append('surface label softens '+gs+' in '+str(r.get('trace_id')))
for tok in ['TRACE_LEDGER_FIXTURE_REHEARSAL_WITH_HOLD','TRACE_LEDGER_FIXTURE_REHEARSAL_DASHBOARD_WITH_HOLD','NEXT_WORK_AFTER_TRACE_LEDGER_FIXTURE_REHEARSAL_WITH_HOLD','TRACE_LEDGER_FIXTURE_REHEARSAL_USER_STATUS_CARD_WITH_HOLD','VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0.md']:
    if tok not in text: problems.append('missing token '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','schema_mutation: no','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for k in ['model_execution','real_codex_execution','real_gemini_execution','authority_mutation','schema_mutation','shared_db_mutation']:
    if data.get(k)!='NO': problems.append(k+' drift')
if data.get('promotion')!='HOLD': problems.append('promotion dashboard drift')
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','authority_effect: AUTHORITY_MUTATION','model_execution: YES','real_codex_execution: YES','real_gemini_execution: YES','schema_mutation: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_TRACE_LEDGER_FIXTURE_REHEARSAL_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_TRACE_LEDGER_FIXTURE_REHEARSAL_WITH_HOLD')
print('row_count=6')
print('layer_count=6')
print('guard_statuses='+','.join(sorted(set(r['guard_status'] for r in rows))))
print('next_work=cross_layer_guard_matrix_candidate_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
