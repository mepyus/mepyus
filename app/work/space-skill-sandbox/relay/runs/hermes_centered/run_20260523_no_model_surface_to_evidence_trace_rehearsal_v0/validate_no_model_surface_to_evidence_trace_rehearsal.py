#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_surface_to_evidence_trace_rehearsal_v0'
trace=json.loads((RUN/'program_spine_phase1_stable_cycle_surface_to_evidence_trace_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_20260523_V0.json').read_text())
problems=[]
required=['trace_id','surface_ref','surface_claim','evidence_receipt_ref','source_receipt_ref','guard_status','valid_for','not_valid_for','hold_boundaries','evidence_refs','surface_language_guard','forbidden_actions']
for k in required:
    if k not in trace or trace[k] in (None,'',[]): problems.append('missing '+k)
if trace.get('guard_status')!='PASS_WITH_HOLD': problems.append('guard not PASS_WITH_HOLD')
if 'WITH_HOLD' not in trace.get('surface_language_guard',{}).get('allowed_surface_label',''): problems.append('surface label lacks WITH_HOLD')
for bad in ['Program Alpha ready','authority approved','schema registry accepted','baseline snapshot created','live DB intake approved','write UI ready','model execution evidence']:
    if bad not in trace.get('surface_language_guard',{}).get('forbidden_interpretations',[]): problems.append('missing forbidden interpretation '+bad)
for token in ['Program Alpha','authority mutation','schema registry mutation','baseline/snapshot creation','promotion','live DB intake','model execution evidence']:
    if token not in trace.get('not_valid_for',[]): problems.append('not_valid_for missing '+token)
for token in ['promotion_status: HOLD','program_alpha_status: NOT_READY','authority_mutation: NO','schema_registry_mutation: NO','model_execution: NO']:
    if token not in trace.get('hold_boundaries',[]): problems.append('hold boundary missing '+token)
for k in ['promotion','authority_mutation','model_execution','schema_registry_mutation','surface_mutation','original_receipt_mutation']:
    expected='HOLD' if k=='promotion' else 'NO'
    if trace.get(k)!=expected: problems.append('trace '+k+' drift')
    if meta.get(k)!=expected: problems.append('meta '+k+' drift')
for p in [WORK/'VECTORFL_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_20260523_V0.md']:
    if not p.exists(): problems.append('missing '+str(p.relative_to(ROOT)))
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_20260523_V0.md'] if p.exists())
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','authority_mutation: YES','schema_registry_mutation: YES','model_execution: YES','automatic enforcement: YES']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_MODEL_SURFACE_TO_EVIDENCE_TRACE_REHEARSAL_WITH_HOLD')
print('trace_id='+trace['trace_id'])
print('guard_status='+trace['guard_status'])
print('surface_mutation=NO')
print('authority_mutation=NO')
print('model_execution=NO')
print('promotion=HOLD')
