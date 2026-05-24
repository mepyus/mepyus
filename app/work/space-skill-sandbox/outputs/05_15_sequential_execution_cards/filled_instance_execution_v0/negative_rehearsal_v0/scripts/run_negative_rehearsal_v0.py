#!/usr/bin/env python3
import json, os, sys
BASE=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CASES=os.path.join(BASE,'cases')
REQUIRED=['observed_scope','repeated_patterns','candidate_items','uncertainties','possible_risks','do_not_promote','questions_for_codex','completion_signal']
results=[]
def expect_stop(name, fn):
    try:
        fn()
        results.append((name, False, 'unexpected pass'))
    except Exception as e:
        results.append((name, True, str(e)))
def check_gemini_json(path):
    obj=json.load(open(path, encoding='utf-8'))
    missing=[k for k in REQUIRED if k not in obj]
    if missing: raise RuntimeError('missing keys: '+','.join(missing))
    if obj.get('completion_signal')!='GEMINI_LITE_OUTPUT_DONE': raise RuntimeError('bad completion_signal')
    for k in REQUIRED[:-1]:
        if not isinstance(obj.get(k), list): raise RuntimeError(k+' not array')
def check_codex(path):
    text=open(path, encoding='utf-8').read()
    required=['verdict','shape_validity','files_read','permission_boundary_check','actual_gemini_scope','premature_claims_removed','recovery_class_hint','WATCH','HOLD','next_smallest_action','completion_signal','hard_stop_confirmation','CODEX_RECOVERY_DONE']
    missing=[r for r in required if r not in text]
    if missing: raise RuntimeError('missing sections/signals: '+','.join(missing))
    forbidden=['promotion_performed: true','APPROVED_PROMOTION: yes','baseline updated','schema updated','registry updated','ontology updated']
    found=[f for f in forbidden if f in text]
    if found: raise RuntimeError('forbidden language: '+','.join(found))
def main():
    expect_stop('bad_gemini_missing_completion', lambda: check_gemini_json(os.path.join(CASES,'bad_gemini_missing_completion.json')))
    expect_stop('bad_gemini_wrong_completion', lambda: check_gemini_json(os.path.join(CASES,'bad_gemini_wrong_completion.json')))
    expect_stop('bad_gemini_wrong_type', lambda: check_gemini_json(os.path.join(CASES,'bad_gemini_wrong_type.json')))
    expect_stop('bad_codex_missing_completion', lambda: check_codex(os.path.join(CASES,'bad_codex_missing_completion.md')))
    expect_stop('bad_codex_promotion_claim', lambda: check_codex(os.path.join(CASES,'bad_codex_promotion_claim.md')))
    failed=[r for r in results if not r[1]]
    receipt={
      'verdict':'NEGATIVE_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED' if not failed else 'NEGATIVE_REHEARSAL_STOP_UNEXPECTED_PASS',
      'status':'negative_fixture_rehearsal_complete',
      'results':[{'case':n,'stopped':ok,'reason':reason} for n,ok,reason in results],
      'unexpected_passes':[n for n,ok,reason in failed],
      'real_gemini_execution':False,
      'real_codex_execution':False,
      'model_api_transport_used':False,
      'promotion_performed':False,
      'vectorfl_authority_modified':False,
      'required_final_line':'No execution was performed. No promotion was performed. Recovery class remains candidate.'
    }
    out=os.path.join(BASE,'NEGATIVE_REHEARSAL_RECEIPT_V0.json')
    with open(out,'w',encoding='utf-8') as f: json.dump(receipt,f,ensure_ascii=False,indent=2); f.write('\n')
    report=os.path.join(BASE,'NEGATIVE_REHEARSAL_REPORT_V0.md')
    lines=['# Negative Rehearsal Report v0','', 'verdict:', '  '+receipt['verdict'], '', 'bad_fixture_results:']
    for n,ok,reason in results:
        lines.append('  - '+n+': '+('STOP_OK' if ok else 'UNEXPECTED_PASS')+' / '+reason)
    lines += ['', 'scope:', '  no-model negative fixture rehearsal', '  no Gemini execution', '  no Codex execution', '', 'HOLD:', '  real Gemini execution', '  real Codex execution', '  promotion', '  VectorFL authority mutation', '', 'required_final_line:', '  No execution was performed. No promotion was performed. Recovery class remains candidate.']
    open(report,'w',encoding='utf-8').write('\n'.join(lines)+'\n')
    print('verdict: '+receipt['verdict'])
    print('receipt: '+out)
    print('report: '+report)
    if failed: sys.exit(2)
if __name__=='__main__': main()
