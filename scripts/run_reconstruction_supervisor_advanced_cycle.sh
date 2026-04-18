#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

scope_ref=""
receipt=""
operation_board=""
supervisor_view=""
sidecar=""
engine_state=""
engine_event=""
reconstruction_id=""
skip_bounded_check="false"
skip_state_check="false"

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --scope-ref)
      scope_ref="$2"
      shift 2
      ;;
    --receipt)
      receipt="$2"
      shift 2
      ;;
    --operation-board)
      operation_board="$2"
      shift 2
      ;;
    --supervisor-view)
      supervisor_view="$2"
      shift 2
      ;;
    --sidecar)
      sidecar="$2"
      shift 2
      ;;
    --engine-state)
      engine_state="$2"
      shift 2
      ;;
    --engine-event)
      engine_event="$2"
      shift 2
      ;;
    --reconstruction-id)
      reconstruction_id="$2"
      shift 2
      ;;
    --skip-bounded-check)
      skip_bounded_check="true"
      shift
      ;;
    --skip-state-check)
      skip_state_check="true"
      shift
      ;;
    *)
      echo "unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

build_args=()
if [[ -n "$scope_ref" ]]; then
  build_args+=(--scope-ref "$scope_ref")
fi
if [[ -n "$receipt" ]]; then
  build_args+=(--receipt "$receipt")
fi
if [[ -n "$operation_board" ]]; then
  build_args+=(--operation-board "$operation_board")
fi
if [[ -n "$supervisor_view" ]]; then
  build_args+=(--supervisor-view "$supervisor_view")
fi
if [[ -n "$sidecar" ]]; then
  build_args+=(--sidecar "$sidecar")
fi
if [[ -n "$engine_state" ]]; then
  build_args+=(--engine-state "$engine_state")
fi
if [[ -n "$engine_event" ]]; then
  build_args+=(--engine-event "$engine_event")
fi
if [[ -n "$reconstruction_id" ]]; then
  build_args+=(--reconstruction-id "$reconstruction_id")
fi

echo "[build] reconstruction supervisor packet (advanced)"
python3 "$REPO_ROOT/scripts/build_reconstruction_supervisor_surface.py" "${build_args[@]}"

echo "[sync] reconstruction supervisor navigation surfaces"
python3 "$REPO_ROOT/scripts/sync_reconstruction_supervisor_surfaces.py"

if [[ "$skip_bounded_check" != "true" ]]; then
  if [[ -n "$scope_ref" ]]; then
    echo "[check] bounded reconstruction fixture"
    bounded_args=("$scope_ref")
    if [[ -n "$receipt" ]]; then
      bounded_args+=(--receipt "$receipt")
    fi
    python3 "$REPO_ROOT/scripts/run_reconstruction_supervisor_fixture_check.py" "${bounded_args[@]}"
  else
    echo "[check] bounded reconstruction fixture skipped because --scope-ref was not provided"
  fi
fi

if [[ "$skip_state_check" != "true" ]]; then
  if [[ -n "$engine_state" || -n "$engine_event" ]]; then
    echo "[check] state-backed reconstruction fixture"
    python3 "$REPO_ROOT/scripts/run_reconstruction_supervisor_state_fixture_check.py"
  else
    echo "[check] state-backed reconstruction fixture skipped because explicit state/event was not provided"
  fi
fi
