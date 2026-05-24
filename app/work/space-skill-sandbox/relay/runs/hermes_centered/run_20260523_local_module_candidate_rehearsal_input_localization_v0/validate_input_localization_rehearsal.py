#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/positive_personal_goal_input.json','fixtures/negative_authority_claim_input.json','fixtures/negative_ambiguous_routing_input.json','outputs/IL-POS-001_localization.md','outputs/IL-NEG-STOP-001_localization.md','outputs/IL-NEG-HOLD-001_localization.md','dashboard.json','user_surface_cards/input_localization_candidate_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no']
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
outs={'IL-POS-001':'outputs/IL-POS-001_localization.md','IL-NEG-STOP-001':'outputs/IL-NEG-STOP-001_localization.md','IL-NEG-HOLD-001':'outputs/IL-NEG-HOLD-001_localization.md'}
for cid, rel in outs.items():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if expect[cid] not in txt: problems.append(f'expected recovery missing for {cid}')
dash=json.loads((ROOT/'dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
for k,v in [('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_INPUT_LOCALIZATION_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_INPUT_LOCALIZATION_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=3')
print('positive=CANDIDATE_MATERIAL_WITH_HOLD')
print('negative_authority_claim=STOP')
print('negative_router_runner_ambiguity=HOLD_STOP_REVIEW')
print('authority_mutation=NO')
print('promotion=HOLD')
