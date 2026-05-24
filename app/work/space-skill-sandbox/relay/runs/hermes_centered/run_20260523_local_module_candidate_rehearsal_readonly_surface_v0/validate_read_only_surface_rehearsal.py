#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/surface_positive_chain_fixture.json','fixtures/surface_negative_write_control_fixture.json','fixtures/surface_negative_soft_promotion_badge_fixture.json','surface/ROS-POS-001_surface.md','surface/ROS-NEG-STOP-001_surface.md','surface/ROS-NEG-HOLD-001_surface.md','surface_dashboard.json','user_surface_cards/read_only_chain_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','write_ui: no']
problems=[]
for rel in required:
 p=ROOT/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for t in tokens:
   if t not in txt: problems.append(f'missing {t!r} in {rel}')
expect={}
for rel in required:
 if rel.startswith('fixtures/'):
  o=json.loads((ROOT/rel).read_text(encoding='utf-8')); expect[o['case_id']]=o['expected_recovery']
outs={'ROS-POS-001':'surface/ROS-POS-001_surface.md','ROS-NEG-STOP-001':'surface/ROS-NEG-STOP-001_surface.md','ROS-NEG-HOLD-001':'surface/ROS-NEG-HOLD-001_surface.md'}
for cid, rel in outs.items():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if expect[cid] not in txt: problems.append(f'expected recovery missing for {cid}')
dash=json.loads((ROOT/'surface_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
if dash.get('write_ui')!='no': problems.append('dashboard write_ui not no')
for k,v in [('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
# ensure positive surface has no write/promotion/authority badge
pos=(ROOT/'surface/ROS-POS-001_surface.md').read_text(encoding='utf-8')
for phrase in ['write_controls: present','promotion_badge: approved','authority_badge: authority']:
 if phrase in pos: problems.append('positive surface contains forbidden '+phrase)
if problems:
 print('FAIL_READ_ONLY_SURFACE_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_READ_ONLY_SURFACE_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=3')
print('positive=VISIBLE_WITH_HOLD')
print('negative_write_ui=STOP')
print('negative_soft_promotion_badge=HOLD_STOP_REVIEW')
print('authority_mutation=NO')
print('promotion=HOLD')
