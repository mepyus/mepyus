#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [[ "$#" -eq 0 ]]; then
  scopes=(
    "tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md"
  )
else
  scopes=("$@")
fi

for scope_ref in "${scopes[@]}"; do
  echo "[batch] scope_ref=$scope_ref"
  bash "$REPO_ROOT/scripts/run_reconstruction_supervisor_cycle.sh" "$scope_ref"
done
