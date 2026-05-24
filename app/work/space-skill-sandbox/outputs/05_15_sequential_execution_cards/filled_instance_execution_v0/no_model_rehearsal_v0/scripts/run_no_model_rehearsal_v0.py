#!/usr/bin/env python3
import json, os, re, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(BASE, 'outputs')
RAW = os.path.join(OUT, 'synthetic_gemini_raw_output.txt')
LITE = os.path.join(OUT, 'synthetic_gemini_lite_output.json')
CODEX = os.path.join(OUT, 'synthetic_codex_combined_bridge_recovery_return.md')
RECEIPT = os.path.join(OUT, 'synthetic_hermes_execution_receipt_v0.json')
REPORT = os.path.join(OUT, 'synthetic_hermes_execution_report_v0.md')
KEYS = ['observed_scope','repeated_patterns','candidate_items','uncertainties','possible_risks','do_not_promote','questions_for_codex','completion_signal']
def stop(m):
    print('STOP: '+m, file=sys.stderr); sys.exit(2)
def extract_json(text):
    m = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, flags=re.S)
    if not m: stop('no fenced json in synthetic raw')
    return json.loads(m.group(1))
def main():
    if not os.path.isfile(RAW): stop('missing synthetic raw')
    obj = extract_json(open(RAW, encoding='utf-8').read())
    missing = [k for k in KEYS if k not in obj]
    if missing: stop('synthetic lite missing keys: '+', '.join(missing))
    if obj.get('completion_signal') != 'GEMINI_LITE_OUTPUT_DONE': stop('bad Gemini completion')
    with open(LITE, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2); f.write('\n')
    if not os.path.isfile(CODEX): stop('missing synthetic Codex return')
    c = open(CODEX, encoding='utf-8').read()
    for lit in ['verdict','shape_validity','files_read','permission_boundary_check','recovery_class_hint','WATCH','HOLD','next_smallest_action','CODEX_RECOVERY_DONE']:
        if lit not in c: stop('synthetic Codex return missing '+lit)
    receipt = {
      'verdict':'NO_MODEL_REHEARSAL_PASS_WITH_EXECUTION_HOLD',
      'status':'synthetic_fixture_rehearsal_complete',
      'real_gemini_execution':False,
      'real_codex_execution':False,
      'model_api_transport_used':False,
      'synthetic_gemini_raw_output':RAW,
      'synthetic_gemini_lite_output':LITE,
      'synthetic_codex_recovery_return':CODEX,
      'gemini_lite_completion_signal_valid':True,
      'codex_completion_signal_valid':True,
      'vectorfl_authority_modified':False,
      'promotion_performed':False,
      'recovery_class_hint':'candidate',
      'required_final_line':'No execution was performed. No promotion was performed. Recovery class remains candidate.'
    }
    with open(RECEIPT, 'w', encoding='utf-8') as f:
        json.dump(receipt, f, ensure_ascii=False, indent=2); f.write('\n')
    lines = [
      '# No-Model Rehearsal Report v0','',
      'verdict:','  NO_MODEL_REHEARSAL_PASS_WITH_EXECUTION_HOLD','',
      'scope:','  synthetic fixture only','  no Gemini execution','  no Codex execution','  no model API transport','',
      'validated:','  synthetic raw -> synthetic lite materialization','  synthetic Codex recovery return shape','  synthetic Hermes receipt/report closeout','',
      'WATCH:','  synthetic fixture mistaken as real model output','  no-model rehearsal mistaken as S5/S6 entry','',
      'HOLD:','  real Gemini execution','  real Codex execution','  promotion','  VectorFL authority mutation','',
      'required_final_line:','  No execution was performed. No promotion was performed. Recovery class remains candidate.'
    ]
    open(REPORT, 'w', encoding='utf-8').write('\n'.join(lines)+'\n')
    print('verdict: NO_MODEL_REHEARSAL_PASS_WITH_EXECUTION_HOLD')
    print('wrote: '+LITE)
    print('wrote: '+RECEIPT)
    print('wrote: '+REPORT)
if __name__ == '__main__': main()
