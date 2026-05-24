#!/usr/bin/env bash
set -euo pipefail
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$BASE"

printf '== static validator ==\n'
./scripts/run_execution_v0.sh validate-static

printf '== positive no-model rehearsal ==\n'
./no_model_rehearsal_v0/scripts/run_no_model_rehearsal_v0.py

printf '== negative rehearsal ==\n'
./negative_rehearsal_v0/scripts/run_negative_rehearsal_v0.py

printf '== S8 gate rehearsal ==\n'
./s8_vectorfl_gate_rehearsal_v0/scripts/run_s8_vectorfl_gate_rehearsal_v0.py

printf '== failure response rehearsal ==\n'
./post_s5_s6_failure_response_v0/scripts/run_failure_response_rehearsal_v0.py

printf '== guarded real execution remains blocked ==\n'
set +e
I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes ./scripts/run_execution_v0.sh run-gemini-after-approval >/tmp/execution_v0_regression_guard_stdout.txt 2>/tmp/execution_v0_regression_guard_stderr.txt
code=$?
set -e
if [ "$code" -eq 0 ]; then
  echo 'STOP: guarded Gemini command unexpectedly passed' >&2
  exit 2
fi
if ! grep -q 'STOP: packet does not grant execution approval: yes' /tmp/execution_v0_regression_guard_stderr.txt; then
  echo 'STOP: guard failed with unexpected message' >&2
  cat /tmp/execution_v0_regression_guard_stderr.txt >&2
  exit 2
fi
printf 'guard_stop_ok exit_code=%s\n' "$code"

printf 'verdict: ALL_SAFE_REGRESSION_PASS_WITH_EXECUTION_HOLD\n'
printf 'required_final_line: No execution was performed. No promotion was performed. Recovery class remains candidate.\n'
