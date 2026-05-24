#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/live_safety_positive_probe.json','fixtures/live_safety_negative_shared_db_drift.json','fixtures/live_safety_negative_promotion_label_drift.json','fixtures/live_safety_negative_write_ui_probe.json','probe_results/LSV-POS-001_probe.md','probe_results/LSV-NEG-STOP-001_probe.md','probe_results/LSV-NEG-HOLD-001_probe.md','probe_results/LSV-NEG-STOP-002_probe.md','shared_db_counts_before.json','shared_db_counts_after.json','live_safety_dashboard.json','user_surface_cards/live_safety_validator_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','shared_db_mutation: no','write_ui: no','authority_database: no']
problems=[]
for rel in required:
 p=ROOT/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for t in tokens:
   if t not in txt: problems.append(f'missing {t!r} in {rel}')
fixtures={}
for rel in required:
 if rel.startswith('fixtures/'):
  o=json.loads((ROOT/rel).read_text(encoding='utf-8')); fixtures[o['case_id']]=o
before=json.loads((ROOT/'shared_db_counts_before.json').read_text(encoding='utf-8'))
after=json.loads((ROOT/'shared_db_counts_after.json').read_text(encoding='utf-8'))
if before != after: problems.append('real shared db before/after count mismatch')
if fixtures['LSV-POS-001']['db_before_counts'] != fixtures['LSV-POS-001']['db_after_counts']: problems.append('positive fixture counts changed')
if fixtures['LSV-NEG-STOP-001']['db_before_counts'] == fixtures['LSV-NEG-STOP-001']['db_after_counts']: problems.append('negative drift fixture does not drift')
if fixtures['LSV-NEG-HOLD-001']['promotion_label'] == 'HOLD': problems.append('negative promotion label fixture not drifting')
if fixtures['LSV-NEG-STOP-002']['write_ui'] != 'yes': problems.append('negative write ui fixture missing')
expected={'LSV-POS-001':'CANDIDATE_MATERIAL_WITH_HOLD','LSV-NEG-STOP-001':'STOP','LSV-NEG-HOLD-001':'HOLD_STOP_REVIEW','LSV-NEG-STOP-002':'STOP'}
for cid, exp in expected.items():
 rel={'LSV-POS-001':'probe_results/LSV-POS-001_probe.md','LSV-NEG-STOP-001':'probe_results/LSV-NEG-STOP-001_probe.md','LSV-NEG-HOLD-001':'probe_results/LSV-NEG-HOLD-001_probe.md','LSV-NEG-STOP-002':'probe_results/LSV-NEG-STOP-002_probe.md'}[cid]
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if exp not in txt: problems.append(f'{cid} expected {exp} missing')
dash=json.loads((ROOT/'live_safety_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
if dash['shared_db_counts_before'] != dash['shared_db_counts_after']: problems.append('dashboard shared db counts mismatch')
for k,v in [('shared_db_mutation','no'),('write_ui','no'),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no'),('live_db_mutation','no'),('schema_mutation','no'),('snapshot_mutation','no'),('authority_database','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_LIVE_SAFETY_VALIDATOR_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_LIVE_SAFETY_VALIDATOR_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=4')
print('positive=SAFE_WITH_HOLD')
print('negative_shared_db_drift=STOP')
print('negative_promotion_label_drift=HOLD_STOP_REVIEW')
print('negative_write_ui=STOP')
print('shared_db_mutation=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
