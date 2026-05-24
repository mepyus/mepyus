#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/persistence_positive_chain_event.json','fixtures/persistence_negative_authority_db_claim.json','fixtures/persistence_negative_shared_db_claim.json','persistence_records/ELP-POS-001_record.json','persistence_records/ELP-NEG-STOP-001_record.md','persistence_records/ELP-NEG-HOLD-001_record.md','persistence_records/fixture_event_log.jsonl','replay/ELP-POS-001_replay.md','persistence_dashboard.json','user_surface_cards/evidence_loop_persistence_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','authority_database: no']
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
  o=json.loads((ROOT/rel).read_text(encoding='utf-8')); fixtures[o['case_id']]=o['expected_recovery']
record=json.loads((ROOT/'persistence_records/ELP-POS-001_record.json').read_text(encoding='utf-8'))
if record.get('classification') != fixtures['ELP-POS-001']: problems.append('positive record classification mismatch')
if record.get('shared_db_mutation')!='no': problems.append('positive record shared_db_mutation mismatch')
if record.get('authority_database')!='no': problems.append('positive record authority_database mismatch')
jsonl=(ROOT/'persistence_records/fixture_event_log.jsonl').read_text(encoding='utf-8').strip().splitlines()
if len(jsonl)!=1: problems.append('fixture_event_log line count mismatch')
else:
 line=json.loads(jsonl[0])
 if line.get('record_id') != record.get('record_id'): problems.append('jsonl record id mismatch')
replay=(ROOT/'replay/ELP-POS-001_replay.md').read_text(encoding='utf-8')
if 'replay_status: MATCH' not in replay: problems.append('replay match missing')
for rel, exp in [('persistence_records/ELP-NEG-STOP-001_record.md','STOP'),('persistence_records/ELP-NEG-HOLD-001_record.md','HOLD_STOP_REVIEW')]:
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if exp not in txt: problems.append(f'{rel} expected {exp} missing')
dash=json.loads((ROOT/'persistence_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
if dash['record_counts']['shared_db_writes']!=0: problems.append('shared_db_writes nonzero')
if dash['record_counts']['authority_db_writes']!=0: problems.append('authority_db_writes nonzero')
for k,v in [('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no'),('live_db_mutation','no'),('schema_mutation','no'),('snapshot_mutation','no'),('authority_database','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_EVIDENCE_LOOP_PERSISTENCE_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_EVIDENCE_LOOP_PERSISTENCE_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=3')
print('positive=PERSISTED_FIXTURE_RECORD_WITH_HOLD')
print('replay=REPLAY_MATCH_WITH_HOLD')
print('negative_authority_database_claim=STOP')
print('negative_shared_db_language=HOLD_STOP_REVIEW')
print('shared_db_mutation=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
