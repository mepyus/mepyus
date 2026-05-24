#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[7]
path=ROOT/'app/work/CHATGPT_CODEX_GEMINI_MODEL_SAFE_HANDOFF_FROM_TEN_CANDIDATE_CHAIN_20260523_V0.md'
text=path.read_text(encoding='utf-8')
required=[
'MODEL_SAFE_HANDOFF_WITH_HOLD',
'ChatGPT first',
'STRONG_PERSONAL_PROGRAM_CORE_CANDIDATE_CHAIN_WITH_SYNTHETIC_MODEL_SAFE_REENTRY_AND_HOLD',
'M-CAND-01','M-CAND-03','M-CAND-04','M-CAND-05','M-CAND-06','M-CAND-07','M-CAND-08','M-CAND-09','M-CAND-10','M-CAND-12',
'PASS_CROSS_TOOL_REENTRY_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD',
'real_gemini_execution: no','real_codex_execution: no','promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','approval_applied: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no','hidden_transport: no','authority_inheritance: no',
'For ChatGPT Specifically','For Codex Specifically','For Gemini Specifically','STOP if any output claims','HOLD_STOP_REVIEW if any output says'
]
problems=[]
for r in required:
    if r not in text:
        problems.append('missing '+r)
# Allow overclaim phrases only inside explicit negative/STOP sections; this validator checks that those sections exist.
if 'It does not mean:' not in text: problems.append('missing does not mean section')
if 'No real Codex/Gemini model execution occurred' not in text: problems.append('missing no-real-model statement')
if problems:
    print('FAIL_MODEL_SAFE_HANDOFF_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_MODEL_SAFE_HANDOFF_VALIDATOR_WITH_HOLD')
print('handoff=CHATGPT_CODEX_GEMINI_MODEL_SAFE_HANDOFF_FROM_TEN_CANDIDATE_CHAIN_20260523_V0.md')
print('chatgpt_self_contained=YES')
print('ten_candidate_chain_included=YES')
print('real_codex_execution=NO')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
