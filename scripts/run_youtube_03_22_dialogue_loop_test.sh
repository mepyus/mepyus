#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INPUT_PATH="$REPO_ROOT/inputs/external_cases/youtube_03_22.md"
LABEL="youtube_03_22_dialogue_loop_test"
REPORT_PATH="$REPO_ROOT/docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md"

mkdir -p "$REPO_ROOT/app/work/dialogue_loop_test/generated"

configs=(
  "3 1"
  "4 2"
  "6 3"
  "8 4"
)

probe_files=()

for config in "${configs[@]}"; do
  read -r window stride <<<"$config"
  echo "[loop] window=$window stride=$stride"
  python3 "$REPO_ROOT/scripts/run_dialogue_asset_probe.py" \
    --input "$INPUT_PATH" \
    --label "$LABEL" \
    --window-size "$window" \
    --stride "$stride"
  latest_probe="$(python3 - <<PY
from pathlib import Path
root = Path(r"$REPO_ROOT")
paths = sorted((root / "app" / "work" / "dialogue_loop_test" / "generated").glob(f"${LABEL}_w${window}_s${stride}_*.json"))
print(paths[-1] if paths else "")
PY
)"
  if [[ -n "$latest_probe" ]]; then
    probe_files+=("$latest_probe")
  fi
done

if [[ "${#probe_files[@]}" -gt 0 ]]; then
  echo "[synthesis] purpose-aligned reading"
  synthesis_args=()
  for probe in "${probe_files[@]}"; do
    synthesis_args+=(--probe "$probe")
  done
  python3 "$REPO_ROOT/scripts/run_dialogue_asset_purpose_synthesis.py" \
    --input-asset "$INPUT_PATH" \
    --report-path "$REPORT_PATH" \
    "${synthesis_args[@]}"
fi
