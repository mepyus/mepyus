#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[7]
FILES = [
    'app/work/VECTORFL_MAY_GOAL_PERSONAL_PROGRAM_AND_MODULE_EXTRACTION_ALIGNMENT_20260523_V0.md',
    'app/work/VECTORFL_MODULE_EXTRACTION_CANDIDATE_MAP_20260523_V0.md',
    'app/work/VECTORFL_PRINCIPLE_PHILOSOPHY_HARDENING_CHECKLIST_20260523_V0.md',
    'app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_goal_module_philosophy_buildup_packet_20260523_v0.md',
    'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_goal_module_philosophy_buildup/run_brief.md',
    'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_goal_module_philosophy_buildup/commands_run.md',
    'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_goal_module_philosophy_buildup/tool_calls.md',
    'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_goal_module_philosophy_buildup/outputs_summary.md',
    'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_goal_module_philosophy_buildup/receipt.md',
]
REQUIRED = [
    'WITH_HOLD',
    'authority mutation: NO',
    'promotion: HOLD',
    'Program Alpha claim: NO',
    'M3/M4 claim: NO',
    'router/runner claim: NO',
]
FORBIDDEN = [
    'verdict: M3 confirmed',
    'verdict: M4 reusable internal module confirmed',
    'verdict: Program Alpha ready',
    'verdict: promotion complete',
    'verdict: authority updated',
    'verdict: registry updated',
    'verdict: schema updated',
    'verdict: baseline updated',
]
problems = []
for rel in FILES:
    p = ROOT / rel
    if not p.exists():
        problems.append(f'missing: {rel}')
        continue
    text = p.read_text(encoding='utf-8')
    for token in REQUIRED:
        if token not in text:
            problems.append(f'missing token {token!r} in {rel}')
    for token in FORBIDDEN:
        if token in text:
            problems.append(f'forbidden token {token!r} in {rel}')
if problems:
    print('FAIL_GOAL_MODULE_PHILOSOPHY_VALIDATOR')
    for item in problems:
        print(item)
    raise SystemExit(1)
print('PASS_GOAL_MODULE_PHILOSOPHY_VALIDATOR_WITH_HOLD')
print('files_checked=' + str(len(FILES)))
print('authority_mutation=NO')
print('promotion=HOLD')
