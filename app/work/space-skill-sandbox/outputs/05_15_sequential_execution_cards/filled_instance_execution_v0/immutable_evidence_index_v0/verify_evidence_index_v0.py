#!/usr/bin/env python3
import json, os, hashlib, sys
BASE=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IDX=os.path.join(BASE,'immutable_evidence_index_v0','IMMUTABLE_EVIDENCE_INDEX_V0.json')
def sha(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()
def main():
    idx=json.load(open(IDX,encoding='utf-8'))
    expected={e['relative_path']:e for e in idx['entries']}
    missing=[]; changed=[]; extra=[]
    for rel,e in expected.items():
        p=os.path.join(BASE,rel)
        if not os.path.exists(p): missing.append(rel)
        elif sha(p)!=e['sha256']: changed.append(rel)
    for root, dirs, files in os.walk(BASE):
        if root.startswith(os.path.join(BASE,'immutable_evidence_index_v0')): continue
        for fn in files:
            rel=os.path.relpath(os.path.join(root,fn),BASE)
            if rel not in expected: extra.append(rel)
    real_outputs=['outputs/gemini_raw_output.txt','outputs/gemini_lite_output.json','outputs/codex_combined_bridge_recovery_return.md','HERMES_EXECUTION_RECEIPT_V0.json','HERMES_EXECUTION_REPORT_V0.md']
    real_present=[p for p in real_outputs if os.path.exists(os.path.join(BASE,p))]
    packet=open(os.path.join(BASE,'FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md'),encoding='utf-8').read()
    approval_yes=packet.count('EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes')
    verdict='EVIDENCE_INDEX_VERIFY_PASS_UNCHANGED_WITH_EXECUTION_HOLD'
    if missing or changed or real_present or approval_yes:
        verdict='EVIDENCE_INDEX_VERIFY_STOP_DRIFT_DETECTED'
    result={'verdict':verdict,'missing':missing,'changed':changed,'extra':extra,'real_outputs_present':real_present,'approval_yes_count':approval_yes,'promotion_yes_count':packet.count('APPROVED_PROMOTION: yes'),'required_final_line':'No execution was performed. No promotion was performed. Recovery class remains candidate.'}
    out=os.path.join(BASE,'immutable_evidence_index_v0','EVIDENCE_INDEX_VERIFY_RESULT_V0.json')
    with open(out,'w',encoding='utf-8') as f: json.dump(result,f,ensure_ascii=False,indent=2); f.write('\n')
    print('verdict: '+verdict)
    print('missing_count='+str(len(missing)))
    print('changed_count='+str(len(changed)))
    print('extra_count='+str(len(extra)))
    print('real_outputs_present_count='+str(len(real_present)))
    if verdict.endswith('DRIFT_DETECTED'): sys.exit(2)
if __name__=='__main__': main()
