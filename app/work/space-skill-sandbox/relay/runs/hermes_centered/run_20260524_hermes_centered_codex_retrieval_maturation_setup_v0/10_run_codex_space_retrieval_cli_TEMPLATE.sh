#!/usr/bin/env bash
set -euo pipefail
# TEMPLATE ONLY. Local CLI/script bridge, no API/direct/server/replay.
ROOT="/Users/sungsookim/universe/vectorfl_replica"
READ_FIRST="/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/04_CODEX_READ_FIRST_FOR_SPACE_RETRIEVAL.md"
OUT="/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/07_CODEX_SPACE_RETRIEVAL_RETURN_PACKET_PLACEHOLDER.json"
cd "$ROOT"
printf 'Run Codex CLI read-only with input: %s and output: %s
' "$READ_FIRST" "$OUT"
# Example only; adjust flags to your local Codex CLI:
# codex --sandbox read-only --output "$OUT" "$(cat "$READ_FIRST")"
