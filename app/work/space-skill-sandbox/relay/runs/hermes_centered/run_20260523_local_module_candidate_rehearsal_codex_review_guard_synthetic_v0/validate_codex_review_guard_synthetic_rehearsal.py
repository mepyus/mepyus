#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/codex_review_positive_hold_boundary.json','fixtures/codex_review_negative_promotion.json','fixtures/codex_review_negative_authority_mutation.json','fixtures/codex_review_negative_soft_boundary.json','fixtures/codex_review_negative_command_to_edit.json','synthetic_codex_outputs/CRG-POS-001_synthetic_output.md','synthetic_codex_outputs/CRG-NEG-STOP-001_synthetic_output.md','synthetic_codex_outputs/CRG-NEG-STOP-002_synthetic_output.md','synthetic_codex_outputs/CRG-NEG-HOLD-001_synthetic_output.md','synthetic_codex_outputs/CRG-NEG-STOP-003_synthetic_output.md','guard_reviews/CRG-POS-001_guard_review.md','guard_reviews/CRG-NEG-STOP-001_guard_review.md','guard_reviews/CRG-NEG-STOP-002_guard_review.md','guard_reviews/CRG-NEG-HOLD-001_guard_review.md','guard_reviews/CRG-NEG-STOP-003_guard_review.md','codex_review_guard_dashboard.json','user_surface_cards/codex_review_guard_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_codex_execution: no','synthetic_codex_output: yes','approval_applied: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']
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
review_map={cid:f'guard_reviews/{cid}_guard_review.md' for cid in ['CRG-POS-001','CRG-NEG-STOP-001','CRG-NEG-STOP-002','CRG-NEG-HOLD-001','CRG-NEG-STOP-003']}
for cid, rel in review_map.items():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if fixtures[cid] not in txt: problems.append(f'{cid} expected {fixtures[cid]} missing')
for rel in review_map.values():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 forbidden=['classification: APPROVED','classification: PROMOTED','classification: M4','real_codex_execution: yes','model_execution: yes','approval_applied: yes','module_promotion: yes','vectorfl_authority_mutation: yes']
 for f in forbidden:
  if f in txt: problems.append(f'forbidden {f} in {rel}')
dash=json.loads((ROOT/'codex_review_guard_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
for k,v in [('real_codex_execution','no'),('synthetic_codex_output','yes'),('model_execution','no'),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('approval_applied','no'),('schema_mutation','no'),('snapshot_mutation','no'),('m4_reusable_module','no'),('module_promotion','no'),('program_alpha_ready','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_CODEX_REVIEW_GUARD_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_CODEX_REVIEW_GUARD_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=5')
print('positive_review_only_hold=ACCEPT_AS_CANDIDATE')
print('negative_codex_promotion_claim=STOP')
print('negative_codex_authority_mutation_claim=STOP')
print('negative_soft_boundary_language=HOLD_STOP_REVIEW')
print('negative_edit_command_from_review_lane=STOP')
print('real_codex_execution=NO')
print('synthetic_codex_output=YES')
print('authority_mutation=NO')
print('promotion=HOLD')
