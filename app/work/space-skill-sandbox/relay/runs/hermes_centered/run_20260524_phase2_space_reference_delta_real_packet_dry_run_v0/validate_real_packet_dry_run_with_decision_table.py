#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
WORK=Path('/Users/sungsookim/universe/vectorfl_replica/app/work')
DT=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_phase2_guard_priority_decision_table_v0/02_guard_priority_mini_decision_table_v0.json'
start=time.perf_counter()
packet=json.loads((RUN/'02_phase2_space_reference_delta_real_packet_dry_run_v0.json').read_text())
source=json.loads((RUN/'01_real_packet_dry_run_source_index_v0.json').read_text())
table=json.loads(DT.read_text())
priority=[r['class'] for r in sorted(table['decision_table'], key=lambda x:x['priority'])]

def signals(pkt):
    refs=pkt.get('space_references_used', [])
    deltas=pkt.get('space_reference_delta', [])
    hold=pkt.get('HOLD_receipt', {})
    lens=pkt.get('lens_card_results', {})
    hermes=pkt.get('hermes_merge_or_execution_result', {})
    delta_by_ref={d.get('ref_id'):d.get('changed_judgment','') for d in deltas}
    sig=set()
    if hold.get('promotion_status')!='HOLD' or hold.get('current_position_apply')!='NO' or hold.get('authority_effect')!='NO_AUTHORITY_MUTATION': sig.add('FAIL_AUTHORITY_OVERPROMOTION')
    if len(refs)>4 and not pkt.get('heavy_escalation_triggered'): sig.add('FAIL_OPERATOR_OVERLOAD')
    if str(lens.get('T_brain_operator_load','')).startswith('FAIL'): sig.add('FAIL_OPERATOR_OVERLOAD')
    if pkt.get('conflict_detected') and not pkt.get('heavy_escalation_triggered'): sig.add('FAIL_HEAVY_ESCALATION_MISSING')
    if not refs or not deltas:
        if 'model reasoning only' in hermes.get('why_not_model_only','').lower(): sig.add('FAIL_MODEL_ONLY_DRIFT')
        else: sig.add('FAIL_NO_SPACE_REFERENCE')
    if not any(r.get('ref_id')=='latest_next_lane' for r in refs): sig.add('FAIL_NO_SPACE_REFERENCE')
    for r in refs:
        rid=r.get('ref_id')
        if rid not in delta_by_ref or len(delta_by_ref.get(rid,''))<20: sig.add('FAIL_SPACE_REFERENCE_DECORATION_ONLY')
    return sig

def classify(pkt):
    sig=signals(pkt)
    for cls in priority:
        if cls in sig: return cls, sorted(sig)
    return 'PASS', sorted(sig)
cls,sig=classify(packet)
checks=[]
checks.append({'check':'decision_table_classifier_passes_packet','pass':cls=='PASS','classification':cls,'signals':sig})
checks.append({'check':'refs_max_4','pass':len(packet['space_references_used'])<=4,'observed':len(packet['space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in packet['space_references_used'])==set(d['ref_id'] for d in packet['space_reference_delta'])})
checks.append({'check':'each_delta_changed_judgment_sufficient','pass':all(len(d.get('changed_judgment',''))>=20 for d in packet['space_reference_delta'])})
checks.append({'check':'not_validator_plumbing_only','pass':'CHECKLIST' in packet['hermes_merge_or_execution_result'].get('artifact_type','') and 'validator' not in packet['target'].lower()})
checks.append({'check':'mind_sized_operator_output','pass':len(packet['hermes_merge_or_execution_result'].get('checklist_items',[]))<=7 and len(packet['space_references_used'])<=4})
checks.append({'check':'budget_gate_fast_no_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'hold_no_authority','pass':packet['HOLD_receipt']['promotion_status']=='HOLD' and packet['HOLD_receipt']['authority_effect']=='NO_AUTHORITY_MUTATION' and packet['HOLD_receipt']['current_position_apply']=='NO'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_SPACE_REFERENCE_DELTA_REAL_PACKET_DRY_RUN_WITH_HOLD' if ok else 'FAIL_PHASE2_SPACE_REFERENCE_DELTA_REAL_PACKET_DRY_RUN','checks':checks,'classification':cls,'signals':sig,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d class=%s active_hits=%d elapsed=%ss' % (len(checks),cls,len(hits),out['elapsed_seconds']))
sys.exit(0 if ok else 1)
