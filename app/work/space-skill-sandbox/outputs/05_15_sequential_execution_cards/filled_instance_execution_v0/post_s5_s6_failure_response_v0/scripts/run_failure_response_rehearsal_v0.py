#!/usr/bin/env python3
import json, os, sys
BASE=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT=os.path.join(BASE,'outputs')
SCENARIOS={
 'gemini_raw_missing':'S5_STOP_NO_RAW',
 'gemini_lite_invalid':'S5_STOP_INVALID_LITE',
 'codex_return_missing':'S6_STOP_NO_CODEX_RETURN',
 'codex_return_forbidden_promotion':'S6_STOP_FORBIDDEN_PROMOTION_CLAIM',
 'closeout_incomplete':'S7_STOP_CLOSEOUT_INCOMPLETE'
}
def main():
    receipts=[]
    for name,code in SCENARIOS.items():
        rec={
          'verdict':code,
          'scenario':name,
          'status':'simulated_failure_response_only',
          'action':'STOP_AND_PRESERVE',
          'recovery_class':'residue_or_STOP',
          'real_gemini_execution':False,
          'real_codex_execution':False,
          'model_api_transport_used':False,
          'promotion_performed':False,
          'vectorfl_authority_modified':False,
          'preserve_policy':'preserve raw/lite/recovery if they exist; never silently edit model outputs',
          'quarantine_policy':'quarantine suspicious Codex promotion/authority claims',
          'required_final_line':'No execution was performed. No promotion was performed. Recovery class remains candidate.'
        }
        p=os.path.join(OUT, name+'_INCIDENT_RECEIPT_V0.json')
        with open(p,'w',encoding='utf-8') as f: json.dump(rec,f,ensure_ascii=False,indent=2); f.write('\n')
        receipts.append(p)
    summary={
      'verdict':'POST_S5_S6_FAILURE_RESPONSE_REHEARSAL_PASS_WITH_EXECUTION_HOLD',
      'scenario_count':len(SCENARIOS),
      'incident_receipts':receipts,
      'real_gemini_execution':False,
      'real_codex_execution':False,
      'promotion_performed':False,
      'vectorfl_authority_modified':False,
      'required_final_line':'No execution was performed. No promotion was performed. Recovery class remains candidate.'
    }
    with open(os.path.join(OUT,'POST_S5_S6_FAILURE_RESPONSE_REHEARSAL_RECEIPT_V0.json'),'w',encoding='utf-8') as f: json.dump(summary,f,ensure_ascii=False,indent=2); f.write('\n')
    report=['# Post S5/S6 Failure Response Rehearsal Report v0','', 'verdict:', '  '+summary['verdict'], '', 'scenario_count:', '  '+str(len(SCENARIOS)), '', 'receipts:']
    for p in receipts: report.append('  '+p)
    report += ['', 'HOLD:', '  real Gemini execution', '  real Codex execution', '  promotion', '  VectorFL authority mutation', '', 'required_final_line:', '  No execution was performed. No promotion was performed. Recovery class remains candidate.']
    open(os.path.join(OUT,'POST_S5_S6_FAILURE_RESPONSE_REHEARSAL_REPORT_V0.md'),'w',encoding='utf-8').write('\n'.join(report)+'\n')
    print('verdict: '+summary['verdict'])
    print('scenario_count='+str(len(SCENARIOS)))
if __name__=='__main__': main()
