#!/usr/bin/env python3
"""Static validator for filled_instance_execution_v0.
No Gemini/Codex/model execution. No network. No authority mutation.
"""
import json, os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(BASE, 'outputs')
PACKET = os.path.join(BASE, 'FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md')
GEMINI_PROMPT = os.path.join(BASE, 'GEMINI_PROMPT_EXECUTION_V0.md')
CODEX_PROMPT = os.path.join(BASE, 'CODEX_RECOVERY_PROMPT_EXECUTION_V0.md')
RECEIPT_CONTRACT = os.path.join(BASE, 'HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json')
REQUIRED = [PACKET, GEMINI_PROMPT, CODEX_PROMPT, RECEIPT_CONTRACT, os.path.join(BASE, 'HERMES_EXECUTION_REPORT_CONTRACT_V0.md')]
FUTURE_OUTPUTS = [os.path.join(OUT, 'gemini_raw_output.txt'), os.path.join(OUT, 'gemini_lite_output.json'), os.path.join(OUT, 'codex_combined_bridge_recovery_return.md')]

def fail(msg):
    print('STOP: ' + msg)
    sys.exit(2)

def main():
    for p in REQUIRED:
        if not os.path.isfile(p): fail('missing required file: ' + p)
    if not os.path.isdir(OUT): fail('missing output dir: ' + OUT)
    packet = open(PACKET, encoding='utf-8').read()
    codex = open(CODEX_PROMPT, encoding='utf-8').read()
    contract = json.load(open(RECEIPT_CONTRACT, encoding='utf-8'))
    approval_no = packet.count('EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no')
    approval_yes = packet.count('EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes')
    if approval_no + approval_yes != 1:
        fail('packet must contain exactly one execution approval line, no or yes')
    approval_state = 'yes' if approval_yes == 1 else 'no'
    required_literals = [
        'APPROVED_PROMOTION: no',
        'Gemini raw stdout must be saved to:',
        'Gemini lite JSON must be materialized and validated at:',
        'Codex must read exactly these four inputs',
    ]
    for lit in required_literals:
        if lit not in packet: fail('packet missing literal: ' + lit)
    four = [
        PACKET,
        os.path.join(OUT, 'gemini_lite_output.json'),
        os.path.join(OUT, 'gemini_raw_output.txt'),
        RECEIPT_CONTRACT,
    ]
    for p in four:
        if p not in packet: fail('packet missing Codex input path: ' + p)
        if p not in codex: fail('Codex prompt missing input path: ' + p)
    if contract.get('approval_defaults', {}).get('execution_approval_granted') is not False:
        fail('receipt contract execution approval default is not false')
    if contract.get('approval_defaults', {}).get('approved_promotion') != 'no':
        fail('receipt contract approved_promotion is not no')
    keys = contract.get('gemini_lite_required_keys', [])
    if len(keys) != 8: fail('Gemini lite key count is not 8')
    if len(contract.get('codex_required_inputs', [])) != 4: fail('Codex input count is not 4')
    print('verdict: EXECUTION_V0_STATIC_VALIDATOR_PASS')
    print('execution_approval_state: ' + approval_state)
    print('future_outputs_declared:')
    for p in FUTURE_OUTPUTS:
        print(('  declared_only_missing_ok: ' if not os.path.exists(p) else '  present: ') + p)
    print('boundary_confirmation: static validation only; no new Gemini/Codex execution during validation; no dispatch; no promotion')
if __name__ == '__main__':
    main()
