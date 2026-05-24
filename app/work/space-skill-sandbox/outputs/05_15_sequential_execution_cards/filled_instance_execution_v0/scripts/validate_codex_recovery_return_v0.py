#!/usr/bin/env python3
import os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(BASE, 'outputs')
RET = os.path.join(OUT, 'codex_combined_bridge_recovery_return.md')
REQUIRED_SECTIONS = ['verdict','shape_validity','files_read','permission_boundary_check','actual_gemini_scope','premature_claims_removed','recovery_class_hint','WATCH','HOLD','next_smallest_action','completion_signal','hard_stop_confirmation']
def stop(msg):
    print('STOP: ' + msg, file=sys.stderr); sys.exit(2)
def main():
    if not os.path.isfile(RET): stop('missing Codex recovery return: ' + RET)
    text = open(RET, encoding='utf-8').read()
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    if missing: stop('Codex return missing required sections: ' + ', '.join(missing))
    if 'CODEX_RECOVERY_DONE' not in text: stop('missing CODEX_RECOVERY_DONE')
    forbidden = ['APPROVED_PROMOTION: yes','promotion_performed: true','baseline updated','schema updated','registry updated','ontology updated']
    found = [f for f in forbidden if f in text]
    if found: stop('forbidden promotion/authority language found: ' + ', '.join(found))
    print('verdict: CODEX_RECOVERY_RETURN_SHAPE_VALID')
    print('validated: ' + RET)
if __name__ == '__main__': main()
