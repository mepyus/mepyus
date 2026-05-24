#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_pre_approval_structure_spec_source_index_v0.json').read_text())
spec=json.loads((RUN/'02_pre_approval_reviewed_structure_spec_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and spec['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'spec_only_not_approval','pass':spec['status']=='HOLD_SPEC_ONLY_NOT_APPROVAL_NOT_APPLY' and spec['approval_state']['user_approval_to_apply']=='NOT_GRANTED' and spec['approval_state']['apply_lane_open']=='NO'})
checks.append({'check':'source_refs_exist','pass':len(spec['space_references_used'])==4 and all(r['exists'] and len(r['sha256'])==64 for r in spec['space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in spec['space_references_used'])==set(d['ref_id'] for d in spec['space_reference_delta'])})
checks.append({'check':'phase_model_present','pass':set(spec['reviewed_structure']['phase_model'].keys())==set(['Phase1','Phase2','Phase3'])})
checks.append({'check':'whole_flow_7_stages','pass':len(spec['reviewed_structure']['whole_flow_stages'])==7})
checks.append({'check':'priority_groups_preserved','pass':set(spec['reviewed_structure']['phase3_plan_priorities'].keys())==set(['MUST_FIX','SHOULD_FIX','WATCH_ONLY'])})
checks.append({'check':'revision_groups_5','pass':len(spec['reviewed_structure']['revision_groups'])==5})
checks.append({'check':'interface_contracts_6','pass':set(spec['interface_contracts'].keys())==set(['input_contract','space_reference_contract','merge_contract','agent_role_contract','operator_surface_contract','budget_contract'])})
checks.append({'check':'authority_model_separate','pass':spec['reviewed_structure']['authority_model']['approval_to_apply'].startswith('separate explicit') and spec['reviewed_structure']['authority_model']['current_position']=='not mutated by this spec'})
checks.append({'check':'out_of_scope_blocks_apply','pass':all(x in spec['out_of_scope_for_this_spec'] for x in ['implementation changes','source/schema mutation','authority/current-position mutation','registry updates','API/direct/server/replay','promotion'])})
checks.append({'check':'pre_apply_checklist_requires_choice','pass':any('Choose HOLD' in x for x in spec['pre_apply_checklist']) and any('allowed files' in x for x in spec['pre_apply_checklist'])})
checks.append({'check':'budget_fast_no_agent_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'hold_boundary_complete','pass':source['boundary']['approval_granted']=='NO' and source['boundary']['implementation_apply']=='NO' and source['boundary']['authority_mutation']=='NO' and source['boundary']['promotion']=='HOLD'})
checks.append({'check':'next_review_hold_or_approve','pass':spec['next_test_candidate'].startswith('PRE_APPROVAL_STRUCTURE_SPEC_REVIEW')})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PRE_APPROVAL_REVIEWED_STRUCTURE_SPEC_WITH_HOLD' if ok else 'FAIL_PRE_APPROVAL_REVIEWED_STRUCTURE_SPEC','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'spec_id':spec['spec_id'],'contracts_count':len(spec['interface_contracts']),'stages_count':len(spec['reviewed_structure']['whole_flow_stages']),'revision_groups_count':len(spec['reviewed_structure']['revision_groups']),'next_safe_lane':spec['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','approval_granted':'NO','implementation_apply':'NO'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d contracts=%d stages=%d revisions=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),out['contracts_count'],out['stages_count'],out['revision_groups_count'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
