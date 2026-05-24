#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
fixtures=json.loads((RUN/'02_source_selection_rule_drift_fixtures_v0.json').read_text())
start=time.perf_counter()

def judge(pkt):
    refs=pkt.get('space_references_used', [])
    deltas=pkt.get('space_reference_delta', [])
    hold=pkt.get('HOLD_receipt', {})
    lens=pkt.get('lens_card_results', {})
    hermes=pkt.get('hermes_merge_or_execution_result', {})
    if not refs or not deltas:
        return 'FAIL_MODEL_ONLY_DRIFT' if 'model reasoning only' in hermes.get('why_not_model_only','').lower() else 'FAIL_NO_SPACE_REFERENCE'
    # Priority matters: authority/promotion and operator-overload drift must not be
    # masked by secondary citation-shape failures on the same malformed packet.
    if hold.get('promotion_status') != 'HOLD' or hold.get('current_position_apply') != 'NO' or hold.get('authority_effect') != 'NO_AUTHORITY_MUTATION':
        return 'FAIL_AUTHORITY_OVERPROMOTION'
    if len(refs) > 4 and not pkt.get('heavy_escalation_triggered'):
        return 'FAIL_OPERATOR_OVERLOAD'
    if pkt.get('conflict_detected') and not pkt.get('heavy_escalation_triggered'):
        return 'FAIL_HEAVY_ESCALATION_MISSING'
    delta_by_ref={d.get('ref_id'):d.get('changed_judgment','') for d in deltas}
    for r in refs:
        rid=r.get('ref_id')
        if rid not in delta_by_ref or len(delta_by_ref.get(rid,'')) < 20:
            return 'FAIL_SPACE_REFERENCE_DECORATION_ONLY'
    if not any(r.get('ref_id')=='phase2_next' for r in refs):
        return 'FAIL_NO_SPACE_REFERENCE'
    if any(str(r.get('path','')).endswith('CURRENT_VECTORFL_POSITION.md') and 'apply' in r.get('used_for','').lower() for r in refs):
        return 'FAIL_AUTHORITY_OVERPROMOTION'
    if lens.get('T_brain_operator_load','').startswith('FAIL'):
        return 'FAIL_OPERATOR_OVERLOAD'
    return 'PASS'

results=[]
for fx in fixtures:
    actual=judge(fx['packet'])
    results.append({'case_id':fx['case_id'],'expected_failure':fx['expected_failure'],'actual_failure':actual,'blocked':actual==fx['expected_failure']})
checks=[]
checks.append({'check':'fixtures_count_6','pass':len(fixtures)==6,'observed':len(fixtures)})
checks.append({'check':'all_expected_failures_blocked','pass':all(r['blocked'] for r in results),'results':results})
checks.append({'check':'decorative_ref_blocked','pass':any(r['case_id']=='NEG_DECORATIVE_REF_NO_CHANGED_JUDGMENT' and r['blocked'] for r in results)})
checks.append({'check':'operator_overload_blocked','pass':any(r['case_id']=='NEG_TOO_MANY_REFS_NO_HEAVY_ESCALATION' and r['blocked'] for r in results)})
checks.append({'check':'authority_overpromotion_blocked','pass':any(r['case_id']=='NEG_AUTHORITY_REF_WRITABLE' and r['blocked'] for r in results)})
checks.append({'check':'model_only_drift_blocked','pass':any(r['case_id']=='NEG_MODEL_ONLY_RULE_NO_REFS' and r['blocked'] for r in results)})
checks.append({'check':'missing_predecessor_blocked','pass':any(r['case_id']=='NEG_MISSING_IMMEDIATE_PREDECESSOR' and r['blocked'] for r in results)})
checks.append({'check':'conflict_without_heavy_blocked','pass':any(r['case_id']=='NEG_CONFLICT_NO_HEAVY_TRIGGER' and r['blocked'] for r in results)})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='03_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_SOURCE_SELECTION_RULE_NEGATIVE_DRIFT_TEST_WITH_HOLD' if ok else 'FAIL_PHASE2_SOURCE_SELECTION_RULE_NEGATIVE_DRIFT_TEST','checks':checks,'case_results':results,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'03_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d cases=%d blocked=%d active_hits=%d elapsed=%ss' % (len(checks),len(results),sum(1 for r in results if r['blocked']),len(hits),out['elapsed_seconds']))
sys.exit(0 if ok else 1)
