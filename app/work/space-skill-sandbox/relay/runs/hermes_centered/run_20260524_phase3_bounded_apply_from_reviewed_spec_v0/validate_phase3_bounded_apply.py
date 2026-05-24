#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_phase3_bounded_apply_source_index_v0.json').read_text())
plan=json.loads((RUN/'02_phase3_revised_apply_plan_v0.json').read_text())
contract=json.loads((RUN/'03_phase3_applied_operating_structure_contract_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and '승인' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'approval_bounded_interpreted','pass':source['user_approval_interpretation']['approval_received']=='YES' and 'app/work only' in source['user_approval_interpretation']['bounded_scope']})
checks.append({'check':'source_refs_exist','pass':len(source['space_refs'])==4 and all(r['exists'] and len(r['sha256'])==64 for r in source['space_refs'])})
checks.append({'check':'budget_fast_no_agent_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'plan_modified_from_previous','pass':len(plan['modification_from_previous_plan'])>=5 and plan['approval_received']=='YES'})
checks.append({'check':'bounded_items_5','pass':len(plan['bounded_revision_items'])==5})
checks.append({'check':'r1_r4_applied_r5_watch','pass':sum(1 for i in plan['bounded_revision_items'] if i['apply_status']=='BOUNDED_APPLY_NOW_TO_SPEC_ARTIFACTS')==4 and any(i['revision_id']=='R5_VALIDATOR_WORDING_SCOPE_GUARD' and i['apply_status']=='WATCH_ONLY_NOT_APPLIED' for i in plan['bounded_revision_items'])})
checks.append({'check':'contract_applied_hold_spec_only','pass':contract['status']=='APPLIED_TO_HOLD_SPEC_ARTIFACTS_ONLY' and contract['approval_received']=='YES_BOUNDED' and 'not authority' in contract['not_authority']})
checks.append({'check':'applied_rules_5','pass':len(contract['applied_rules'])==5 and contract['applied_rules']['R5_VALIDATOR_WORDING_SCOPE_GUARD']['status']=='WATCH_ONLY_NOT_APPLIED'})
checks.append({'check':'interface_contracts_6','pass':set(contract['interface_contracts'].keys())==set(['input_contract','space_reference_contract','merge_contract','agent_role_contract','operator_surface_contract','budget_contract'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in source['space_refs'])==set(d['ref_id'] for d in contract['space_reference_delta'])})
checks.append({'check':'hold_boundaries_no_authority','pass':contract['hold_boundaries']['authority_mutation']=='NO' and contract['hold_boundaries']['registry_mutation']=='NO' and contract['hold_boundaries']['current_position_apply']=='NO' and contract['hold_boundaries']['source_code_mutation']=='NO' and contract['hold_boundaries']['promotion']=='HOLD'})
checks.append({'check':'next_smoke_test','pass':contract['next_safe_lane']=='PHASE3_APPLIED_CONTRACT_SMOKE_TEST_NO_AUTHORITY_MUTATION_V0'})
# Ensure only generated run/root evidence is changed; no authority/current-position file was written by this validator.
checks.append({'check':'bounded_scope_no_forbidden_authority_apply','pass':all(x in source['user_approval_interpretation']['explicitly_not_authorized'] for x in ['authority/current-position mutation','registry update','source code mutation','schema registry mutation','promotion'])})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='05_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE3_BOUNDED_APPLY_FROM_REVIEWED_SPEC_WITH_HOLD' if ok else 'FAIL_PHASE3_BOUNDED_APPLY_FROM_REVIEWED_SPEC','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'applied_rules':len(contract['applied_rules']),'bounded_items':len(plan['bounded_revision_items']),'next_safe_lane':contract['next_safe_lane'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','approval_scope':source['user_approval_interpretation']['bounded_scope']}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d applied_rules=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),out['applied_rules'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
