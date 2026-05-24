#!/usr/bin/env python3
import os, sys, json
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(BASE, 'outputs')
RAW = os.path.join(OUT, 'gemini_raw_output.txt')
LITE = os.path.join(OUT, 'gemini_lite_output.json')
CODEX = os.path.join(OUT, 'codex_combined_bridge_recovery_return.md')
RECEIPT = os.path.join(BASE, 'HERMES_EXECUTION_RECEIPT_V0.json')
REPORT = os.path.join(BASE, 'HERMES_EXECUTION_REPORT_V0.md')
PACKET = os.path.join(BASE, 'FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md')
def stop(msg):
    print('STOP: ' + msg, file=sys.stderr); sys.exit(2)
def main():
    for p in [RAW, LITE, CODEX, PACKET]:
        if not os.path.isfile(p): stop('missing closeout input: ' + p)
    lite = json.load(open(LITE, encoding='utf-8'))
    if lite.get('completion_signal') != 'GEMINI_LITE_OUTPUT_DONE': stop('Gemini lite completion invalid')
    codex_text = open(CODEX, encoding='utf-8').read()
    if 'CODEX_RECOVERY_DONE' not in codex_text: stop('Codex completion invalid')
    receipt = {
        'verdict':'HERMES_EXECUTION_RECEIPT_DONE_WITH_PROMOTION_HOLD',
        'status':'approved_execution_closeout_from_declared_outputs',
        'packet_path':PACKET,
        'gemini_raw_output':RAW,
        'gemini_lite_output':LITE,
        'codex_recovery_return':CODEX,
        'gemini_lite_completion_signal_valid':True,
        'codex_completion_signal_valid':True,
        'real_gemini_executed':True,
        'real_codex_executed':True,
        'live_web_lookup_used':False,
        'external_connector_used':False,
        'browser_used':False,
        'mcp_used':False,
        'memory_modified':False,
        'skill_modified':False,
        'cron_modified':False,
        'config_modified':False,
        'vectorfl_authority_modified':False,
        'promotion_performed':False,
        'recovery_class_hint':'candidate',
        'completion_signal':'HERMES_EXECUTION_RECEIPT_DONE',
        'required_final_line':'No promotion was performed. Recovery class remains candidate.'
    }
    with open(RECEIPT, 'w', encoding='utf-8') as f:
        json.dump(receipt, f, ensure_ascii=False, indent=2); f.write('\n')
    report = '# Hermes Execution Report v0\n\nverdict:\n  HERMES_EXECUTION_RECEIPT_DONE_WITH_PROMOTION_HOLD\n\nfiles_created_or_used:\n  '+RAW+'\n  '+LITE+'\n  '+CODEX+'\n  '+RECEIPT+'\n\nGemini completion:\n  GEMINI_LITE_OUTPUT_DONE\n\nCodex completion:\n  CODEX_RECOVERY_DONE\n\npromotion_boundary:\n  APPROVED_PROMOTION: no\n  promotion_performed: false\n\nVectorFL_authority_boundary:\n  vectorfl_authority_modified: false\n  receipt/report are not authority\n\nWATCH:\n  Gemini output mistaken as truth\n  Codex recovery mistaken as authority mutation\n  Hermes receipt mistaken as VectorFL approval\n\nHOLD:\n  promotion\n  VectorFL authority mutation\n  baseline/workflow/schema/registry/ontology/component promotion\n\ncompletion_signal:\n  HERMES_EXECUTION_RECEIPT_DONE\n\nrequired_final_line:\n  No promotion was performed. Recovery class remains candidate.\n'
    with open(REPORT, 'w', encoding='utf-8') as f: f.write(report)
    print('verdict: HERMES_CLOSEOUT_WRITTEN_WITH_PROMOTION_HOLD')
    print('receipt: ' + RECEIPT)
    print('report: ' + REPORT)
if __name__ == '__main__': main()
