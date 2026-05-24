#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_20260523_V0.md','app/work/VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_20260523_V0.json','app/work/VECTORFL_NEXT_WORK_AFTER_SURFACE_TO_EVIDENCE_TRACE_MAP_20260523_V0.md','app/work/VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_USER_STATUS_CARD_20260523_V0.md','app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_surface_to_evidence_trace_map_candidate_v0/fixtures/surface_to_evidence_trace_map_fixture.json']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
fixture=json.loads((ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_surface_to_evidence_trace_map_candidate_v0/fixtures/surface_to_evidence_trace_map_fixture.json').read_text(encoding='utf-8'))
dash=json.loads((ROOT/'app/work/VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_20260523_V0.json').read_text(encoding='utf-8'))
allowed={'PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'}
entries=fixture.get('entries',[])
if len(entries)!=8: problems.append('entry_count mismatch')
if dash.get('entry_count')!=8: problems.append('dashboard entry_count mismatch')
required=['surface_id','surface_artifact','display_label','source_artifact','receipt_ref','trace_id','guard_status','drift_block']
for e in entries:
    for k in required:
        if not e.get(k): problems.append('missing '+k+' in '+str(e.get('surface_id')))
    gs=e.get('guard_status')
    label=e.get('display_label','')
    if gs not in allowed: problems.append('bad guard '+str(e.get('surface_id')))
    if gs in ['WATCH','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'] and gs not in label:
        problems.append('label does not preserve '+gs+' in '+str(e.get('surface_id')))
    if gs=='PASS_WITH_HOLD' and not any(tok in label for tok in ['HOLD','candidate','fixture','evidence','not Program Alpha ready','not DB rows','not implemented']):
        problems.append('PASS label too soft '+str(e.get('surface_id')))
for tok in ['SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_WITH_HOLD','SURFACE_TO_EVIDENCE_TRACE_MAP_DASHBOARD_WITH_HOLD','NEXT_WORK_AFTER_SURFACE_TO_EVIDENCE_TRACE_MAP_WITH_HOLD','SURFACE_TO_EVIDENCE_TRACE_MAP_USER_STATUS_CARD_WITH_HOLD','VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_20260523_V0.md']:
    if tok not in text: problems.append('missing token '+tok)
for tok in ['receipt_ref','trace_id','guard_status','drift_block','PASS_WITH_HOLD','WATCH','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT']:
    if tok not in text: problems.append('missing map token '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','schema_mutation: no','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for data_name,data in [('fixture',fixture),('dashboard',dash)]:
    for k in ['model_execution','real_codex_execution','real_gemini_execution','authority_mutation','schema_mutation','shared_db_mutation']:
        if data.get(k)!='NO': problems.append(data_name+' '+k+' drift')
    if data.get('promotion')!='HOLD': problems.append(data_name+' promotion drift')
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','model_execution: YES','real_codex_execution: YES','real_gemini_execution: YES','schema_mutation: YES','authority_mutation: YES','approval_applied: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_WITH_HOLD')
print('entry_count=8')
print('guard_statuses='+','.join(sorted(set(e['guard_status'] for e in entries))))
print('next_work=program_unit_structure_progress_review_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
