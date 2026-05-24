#!/usr/bin/env bash
set -euo pipefail
BASE="/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0"
cd "$BASE"
printf '== validate-static ==\n'
./scripts/run_execution_v0.sh validate-static
printf '== validate-codex-return ==\n'
./scripts/run_execution_v0.sh validate-codex-return
printf '== post-execution verification ==\n'
python3 "$BASE/post_execution_verification_loop_v0/scripts/run_post_execution_verification_v0.py"
printf 'verdict: POST_EXECUTION_SAFE_REGRESSION_PASS_NO_MODEL_EXECUTION\n'
printf 'required_final_line: No promotion was performed. Recovery class remains candidate.\n'
