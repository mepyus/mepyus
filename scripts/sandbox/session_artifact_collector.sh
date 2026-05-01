#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/sandbox/session_artifact_collector.sh PACKAGE_DIR

Collect key artifacts from session_* subdirectories into <PACKAGE_DIR>/collected_artifacts/.

Boundary:
  - PACKAGE_DIR must be under app/work/space-skill-sandbox/packages/
  - output is <PACKAGE_DIR>/collected_artifacts/
  - session-specific prefix is added to each file
  - refuses to overwrite existing collected_artifacts directory
  - discovery-first: does not judge content, only transports files
USAGE
}

PACKAGE_ROOT="app/work/space-skill-sandbox/packages"
OUTPUT_DIR_NAME="collected_artifacts"

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

PACKAGE_DIR="${1%/}"

if [[ "$PACKAGE_DIR" == *".."* ]]; then
  echo "PACKAGE_DIR must not contain '..'." >&2
  exit 2
fi

if [[ ! -d "$PACKAGE_DIR" ]]; then
  echo "Package directory not found: $PACKAGE_DIR" >&2
  exit 1
fi

ROOT_ABS="$(cd "$PACKAGE_ROOT" 2>/dev/null && pwd -P)"
PACKAGE_ABS="$(cd "$PACKAGE_DIR" 2>/dev/null && pwd -P)"

case "$PACKAGE_ABS" in
  "$ROOT_ABS"/*) ;;
  *)
    echo "PACKAGE_DIR must be under $PACKAGE_ROOT." >&2
    exit 2
    ;;
esac

if [[ "$PACKAGE_ABS" == "$ROOT_ABS" ]]; then
  echo "PACKAGE_DIR must be one package directory, not the packages root." >&2
  exit 2
fi

OUTPUT_DIR="$PACKAGE_ABS/$OUTPUT_DIR_NAME"
MANIFEST_PATH="$OUTPUT_DIR/manifest.md"

if [[ -e "$OUTPUT_DIR" ]]; then
  echo "Refusing to overwrite existing directory: $OUTPUT_DIR" >&2
  exit 3
fi

mkdir -p "$OUTPUT_DIR"

echo "Collecting artifacts into $OUTPUT_DIR..."

# Start manifest
cat <<EOF > "$MANIFEST_PATH"
# Artifact Collection Manifest

## Collection Metadata

- collection_timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- package_path: $PACKAGE_ABS
- script_name: $(basename "$0")
- script_path: $0

## Collected Files

| Target Filename | Source Relative Path | Size (Bytes) | Source MTime |
| :--- | :--- | :--- | :--- |
EOF

find "$PACKAGE_ABS" -maxdepth 2 -type d -name "session_*" | sort | while IFS= read -r session_dir; do
  session_name="$(basename "$session_dir")"
  echo "- Processing $session_name"

  # Standard artifacts to collect
  for artifact in gemini_packet.md handoff_log.md codex_review_bundle.md analysis_result.md package_brief.md; do
    src="$session_dir/$artifact"
    if [[ -f "$src" ]]; then
      dest_name="${session_name}_$artifact"
      dest="$OUTPUT_DIR/$dest_name"
      
      cp "$src" "$dest"
      
      # Extract metadata (Darwin stat)
      fsize=$(stat -f%z "$src")
      fmtime=$(date -u -r "$(stat -f%m "$src")" +"%Y-%m-%dT%H:%M:%SZ")
      rel_src="${src#$PACKAGE_ABS/}"
      
      echo "| $dest_name | $rel_src | $fsize | $fmtime |" >> "$MANIFEST_PATH"
      echo "  + Collected: $artifact"
    fi
  done
done

echo "Collection complete."
echo "Manifest created at: $MANIFEST_PATH"
echo "Artifacts are available in: $OUTPUT_DIR"
