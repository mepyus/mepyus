#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEFAULT_SCOPE_REF="tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md"
SCOPE_REF="${1:-$DEFAULT_SCOPE_REF}"

echo "[build] reconstruction supervisor packet"
python3 "$REPO_ROOT/scripts/build_reconstruction_supervisor_surface.py" --scope-ref "$SCOPE_REF"

echo "[sync] reconstruction supervisor navigation surfaces"
python3 "$REPO_ROOT/scripts/sync_reconstruction_supervisor_surfaces.py"

echo "[check] bounded reconstruction fixture"
python3 "$REPO_ROOT/scripts/run_reconstruction_supervisor_fixture_check.py" "$SCOPE_REF"

echo "[check] state-backed reconstruction fixture"
python3 "$REPO_ROOT/scripts/run_reconstruction_supervisor_state_fixture_check.py"
