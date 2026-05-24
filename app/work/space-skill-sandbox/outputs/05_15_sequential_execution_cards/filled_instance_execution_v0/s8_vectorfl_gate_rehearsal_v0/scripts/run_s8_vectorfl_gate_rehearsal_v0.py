#!/usr/bin/env python3
"""S8 VectorFL recovery gate rehearsal classifier.
No authority mutation. No promotion. No model execution.
Classifies evidence into receipt/residue/candidate/STOP only.
"""
import json, os, sys
BASE=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IN=os.path.join(BASE,'inputs','S8_REHEARSAL_INPUT_MANIFEST_V0.json')
OUT=os.path.join(BASE,'outputs')
def stop(msg):
    print('STOP: '+msg, file=sys.stderr)
    sys.exit(2)
def load(path):
    if not os.path.isfile(path): stop('missing referenced evidence: '+path)
    if path.endswith('.json'):
        return json.load(open(path, encoding='utf-8'))
    return open(path, encoding='utf-8').read()
def main():
    manifest=json.load(open(IN, encoding='utf-8'))
    refs=manifest['source_evidence']
    evidence={k:load(v) for k,v in refs.items()}
    # Hard no-action checks.
    if manifest.get('promotion') is not False: stop('manifest promotion not false')
    if manifest.get('vectorfl_authority_mutation') is not False: stop('manifest authority mutation not false')
    positive=evidence['positive_rehearsal_receipt']
    negative=evidence['negative_rehearsal_receipt']
    state=evidence['state']
    if positive.get('verdict')!='NO_MODEL_REHEARSAL_PASS_WITH_EXECUTION_HOLD': stop('positive rehearsal not pass')
    if negative.get('verdict')!='NEGATIVE_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED': stop('negative rehearsal not pass')
    if state.get('active_state')!='S4_APPROVAL_GATE_WAITING': stop('real lane not S4 approval waiting')
    classification={
      'verdict':'S8_VECTORFL_GATE_REHEARSAL_CLASSIFIED_CANDIDATE_WITH_PROMOTION_HOLD',
      'status':'rehearsal_classification_only',
      'classification':'candidate',
      'basis':['structure evidence exists','positive no-model rehearsal passed','negative fixtures stopped','real lane remains S4 approval waiting'],
      'not_basis':['not real Gemini output','not real Codex recovery','not VectorFL authority','not promotion'],
      'allowed_recovery_objects':['receipt','residue','candidate','STOP'],
      'selected_recovery_object':'candidate',
      'vectorfl_authority_modified':False,
      'promotion_performed':False,
      'real_gemini_execution':False,
      'real_codex_execution':False,
      'WATCH':['candidate classification mistaken as component','S8 rehearsal mistaken as authority mutation','synthetic evidence over-weighted as real execution evidence'],
      'HOLD':['promotion','VectorFL authority mutation','baseline/workflow/schema/registry/ontology/component','current-position/output_manifest'],
      'next_smallest_action':'prepare final S0-S8 route map and remaining explicit-approval checklist',
      'required_final_line':'No execution was performed. No promotion was performed. Recovery class remains candidate.'
    }
    receipt_path=os.path.join(OUT,'S8_VECTORFL_GATE_REHEARSAL_RECEIPT_V0.json')
    report_path=os.path.join(OUT,'S8_VECTORFL_GATE_REHEARSAL_REPORT_V0.md')
    with open(receipt_path,'w',encoding='utf-8') as f: json.dump(classification,f,ensure_ascii=False,indent=2); f.write('\n')
    lines=['# S8 VectorFL Gate Rehearsal Report v0','', 'verdict:', '  '+classification['verdict'], '', 'classification:', '  candidate', '', 'scope:', '  rehearsal classification only', '  no authority mutation', '  no promotion', '  no Gemini/Codex execution', '', 'basis:']
    for b in classification['basis']: lines.append('  - '+b)
    lines += ['', 'not_basis:']
    for b in classification['not_basis']: lines.append('  - '+b)
    lines += ['', 'WATCH:']
    for w in classification['WATCH']: lines.append('  - '+w)
    lines += ['', 'HOLD:']
    for h in classification['HOLD']: lines.append('  - '+h)
    lines += ['', 'required_final_line:', '  No execution was performed. No promotion was performed. Recovery class remains candidate.']
    open(report_path,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
    print('verdict: '+classification['verdict'])
    print('receipt: '+receipt_path)
    print('report: '+report_path)
if __name__=='__main__': main()
