#!/usr/bin/env python3
from pathlib import Path
import json, sys, hashlib
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/deterministic_positive_cycle_fixture.json','fixtures/deterministic_negative_timestamp_drift_fixture.json','fixtures/deterministic_negative_v1_snapshot_claim_fixture.json','fixtures/deterministic_negative_promotion_claim_fixture.json','cycle_runs/run_A/canonical_output.json','cycle_runs/run_B/canonical_output.json','cycle_runs/run_A/hash.txt','cycle_runs/run_B/hash.txt','diffs/DSC-POS-001_diff.md','diffs/DSC-NEG-HOLD-001_diff.md','diffs/DSC-NEG-STOP-001_diff.md','diffs/DSC-NEG-STOP-002_diff.md','deterministic_dashboard.json','user_surface_cards/deterministic_stable_cycle_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','shared_db_mutation: no','write_ui: no','authority_database: no','v1_snapshot_creation: no']
problems=[]
for rel in required:
 p=ROOT/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for t in tokens:
   if t not in txt: problems.append(f'missing {t!r} in {rel}')
A=(ROOT/'cycle_runs/run_A/canonical_output.json').read_text(encoding='utf-8')
B=(ROOT/'cycle_runs/run_B/canonical_output.json').read_text(encoding='utf-8')
hA=(ROOT/'cycle_runs/run_A/hash.txt').read_text(encoding='utf-8').strip()
hB=(ROOT/'cycle_runs/run_B/hash.txt').read_text(encoding='utf-8').strip()
calcA=hashlib.sha256(json.dumps(json.loads(A),sort_keys=True,ensure_ascii=False).encode()).hexdigest()
calcB=hashlib.sha256(json.dumps(json.loads(B),sort_keys=True,ensure_ascii=False).encode()).hexdigest()
if A != B: problems.append('canonical outputs differ')
if hA != hB: problems.append('hash files differ')
if hA != calcA or hB != calcB: problems.append('hash calculation mismatch')
fixtures={}
for rel in required:
 if rel.startswith('fixtures/'):
  o=json.loads((ROOT/rel).read_text(encoding='utf-8')); fixtures[o['case_id']]=o
if fixtures['DSC-POS-001']['run_A_hash'] != fixtures['DSC-POS-001']['run_B_hash']: problems.append('positive fixture hashes do not match')
if fixtures['DSC-NEG-HOLD-001']['run_A_hash'] == fixtures['DSC-NEG-HOLD-001']['run_B_hash']: problems.append('negative drift fixture hashes match')
expected={'DSC-POS-001':'CANDIDATE_MATERIAL_WITH_HOLD','DSC-NEG-HOLD-001':'HOLD_STOP_REVIEW','DSC-NEG-STOP-001':'STOP','DSC-NEG-STOP-002':'STOP'}
for cid, exp in expected.items():
 rel={'DSC-POS-001':'diffs/DSC-POS-001_diff.md','DSC-NEG-HOLD-001':'diffs/DSC-NEG-HOLD-001_diff.md','DSC-NEG-STOP-001':'diffs/DSC-NEG-STOP-001_diff.md','DSC-NEG-STOP-002':'diffs/DSC-NEG-STOP-002_diff.md'}[cid]
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if exp not in txt: problems.append(f'{cid} expected {exp} missing')
dash=json.loads((ROOT/'deterministic_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
if dash['hash_match']!='yes': problems.append('dashboard hash_match not yes')
for k,v in [('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no'),('live_db_mutation','no'),('schema_mutation','no'),('snapshot_mutation','no'),('authority_database','no'),('v1_snapshot_creation','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_DETERMINISTIC_STABLE_CYCLE_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_DETERMINISTIC_STABLE_CYCLE_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=4')
print('positive=DETERMINISTIC_MATCH_WITH_HOLD')
print('negative_timestamp_drift=HOLD_STOP_REVIEW')
print('negative_v1_snapshot_claim=STOP')
print('negative_promotion_by_determinism=STOP')
print('run_A_equals_run_B=YES')
print('v1_snapshot_creation=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
