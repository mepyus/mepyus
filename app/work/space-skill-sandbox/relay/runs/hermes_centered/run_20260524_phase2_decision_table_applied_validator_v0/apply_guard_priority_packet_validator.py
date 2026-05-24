#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
WORK=Path('/Users/sungsookim/universe/vectorfl_replica/app/work')
DT_RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_phase2_guard_priority_decision_table_v0'
FX_RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_phase2_source_selection_rule_negative_drift_test_v0'
table=json.loads((DT_RUN/'02_guard_priority_mini_decision_table_v0.json').read_text())
fixtures=json.loads((FX_RUN/'02_source_selection_rule_drift_fixtures_v0.json').read_text())
priority=[r['class'] for r in sorted(table['decision_table'], key=lambda x:x['priority'])]
start=time.perf_counter()

def signals(pkt):
    refs=pkt.get('space_references_used', [])
    deltas=pkt.get('space_reference_delta', [])
    hold=pkt.get('HOLD_receipt', {})
    lens=pkt.get('lens_card_results', {})
    hermes=pkt.get('hermes_merge_or_execution_result', {})
    delta_by_ref={d.get('ref_id'):d.get('changed_judgment','') for d in deltas}
    sig=set()
    if hold.get('promotion_status')!='HOLD' or hold.get('current_position_apply')!='NO' or hold.get('authority_effect')!='NO_AUTHORITY_MUTATION':
        sig.add('FAIL_AUTHORITY_OVERPROMOTION')
    if any(str(r.get('path','')).endswith('CURRENT_VECTORFL_POSITION.md') and 'apply' in r.get('used_for','').lower() for r in refs):
        sig.add('FAIL_AUTHORITY_OVERPROMOTION')
    if len(refs)>4 and not pkt.get('heavy_escalation_triggered'):
        sig.add('FAIL_OPERATOR_OVERLOAD')
    if str(lens.get('T_brain_operator_load','')).startswith('FAIL'):
        sig.add('FAIL_OPERATOR_OVERLOAD')
    if pkt.get('conflict_detected') and not pkt.get('heavy_escalation_triggered'):
        sig.add('FAIL_HEAVY_ESCALATION_MISSING')
    if not refs or not deltas:
        if 'model reasoning only' in hermes.get('why_not_model_only','').lower(): sig.add('FAIL_MODEL_ONLY_DRIFT')
        else: sig.add('FAIL_NO_SPACE_REFERENCE')
    if not any(r.get('ref_id')=='phase2_next' for r in refs):
        sig.add('FAIL_NO_SPACE_REFERENCE')
    for r in refs:
        rid=r.get('ref_id')
        if rid not in delta_by_ref or len(delta_by_ref.get(rid,''))<20:
            sig.add('FAIL_SPACE_REFERENCE_DECORATION_ONLY')
    return sig

def classify(pkt):
    sig=signals(pkt)
    for cls in priority:
        if cls in sig:
            return cls, sorted(sig)
    return 'PASS', sorted(sig)

results=[]
for fx in fixtures:
    cls,sig=classify(fx['packet'])
    results.append({'case_id':fx['case_id'],'expected_failure':fx['expected_failure'],'actual_failure':cls,'signals':sig,'blocked':cls==fx['expected_failure']})
summary={'packet_id':'02_applied_decision_table_validator_result_v0','verdict':'PASS_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_WITH_HOLD' if all(r['blocked'] for r in results) else 'FAIL_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR','priority_order':priority,'case_results':results,'blocked':sum(1 for r in results if r['blocked']),'cases':len(results),'elapsed_seconds':time.perf_counter()-start,'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'02_applied_decision_table_validator_result_v0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
print(summary['verdict'])
print('cases=%d blocked=%d elapsed=%ss' % (summary['cases'],summary['blocked'],summary['elapsed_seconds']))
sys.exit(0 if summary['verdict'].startswith('PASS') else 1)
