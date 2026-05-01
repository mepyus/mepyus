#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/sandbox/package_metadata_scan.sh [--max-lines N] PACKAGE_DIR

Create a compact metadata scan report for one bounded sandbox package.

Boundary:
  - PACKAGE_DIR must be under app/work/space-skill-sandbox/packages/
  - output is <PACKAGE_DIR>/metadata_scan_report.md
  - refuses to overwrite by default
  - does not scan the whole md space
  - does not mark candidate guesses as reviewed
USAGE
}

MAX_LINES=40
PACKAGE_ROOT="app/work/space-skill-sandbox/packages"
OUTPUT_NAME="metadata_scan_report.md"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --max-lines)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --max-lines" >&2
        exit 2
      fi
      MAX_LINES="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      break
      ;;
  esac
done

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

PACKAGE_DIR="${1%/}"

if [[ ! "$MAX_LINES" =~ ^[0-9]+$ ]] || [[ "$MAX_LINES" -lt 1 ]] || [[ "$MAX_LINES" -gt 120 ]]; then
  echo "--max-lines must be an integer between 1 and 120." >&2
  exit 2
fi

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

OUTPUT_FILE="$PACKAGE_ABS/$OUTPUT_NAME"
TMP_FILE="$PACKAGE_ABS/.${OUTPUT_NAME}.tmp.$$"

if [[ -e "$OUTPUT_FILE" ]]; then
  echo "Refusing to overwrite existing report: $OUTPUT_FILE" >&2
  exit 3
fi

cleanup() {
  rm -f "$TMP_FILE"
}
trap cleanup EXIT

rel_path() {
  local path="$1"
  printf '%s\n' "${path#$PACKAGE_ABS/}"
}

write_file_list() {
  find "$PACKAGE_ABS" -type f ! -name ".${OUTPUT_NAME}.tmp.*" | sort | while IFS= read -r file; do
    rel_path "$file"
  done
}

write_size_list() {
  find "$PACKAGE_ABS" \( -path "*/raw/*" -o -path "*/outbox/*" \) -type f | sort | while IFS= read -r file; do
    bytes="$(wc -c < "$file" | tr -d ' ')"
    printf -- '- %s: %s bytes\n' "$(rel_path "$file")" "$bytes"
  done
}

is_standard_package_record() {
  case "$1" in
    package_brief.md|user_summary.md|package_closeout.md|codex_review_bundle.md|codex_validation.md|handoff_log.md|gemini_packet.md|metadata_scan_report.md)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

write_core_authored_doc_candidates() {
  find "$PACKAGE_ABS" -maxdepth 1 -type f -name '*.md' | sort | while IFS= read -r file; do
    rel="$(rel_path "$file")"
    if ! is_standard_package_record "$rel"; then
      printf -- '- `%s`\n' "$rel"
    fi
  done
}

write_header_excerpt() {
  local rel="$1"
  local file="$PACKAGE_ABS/$rel"
  if [[ -f "$file" ]]; then
    {
      echo "### $rel"
      echo
      echo '```text'
      sed -n "1,${MAX_LINES}p" "$file"
      echo '```'
      echo
    } >> "$TMP_FILE"
  fi
}

cat > "$TMP_FILE" <<REPORT
# Package Metadata Scan Report

## 0. Status

- status: generated
- package: ${PACKAGE_ABS}
- scan_scope: one bounded package directory
- scan_mode: observed signals only
- tone_guidance: avoid over-finalization (candidate requires review)
- max_header_lines: ${MAX_LINES}
- whole_md_scan: false
- graph: false
- ontology: false
- automation: false
- reviewed_by: pending

## 1. Files Seen

\`\`\`text
REPORT

write_file_list >> "$TMP_FILE"

cat >> "$TMP_FILE" <<'REPORT'
```

## 2. Raw / Outbox / Stderr Sizes

REPORT

if find "$PACKAGE_ABS" \( -path "*/raw/*" -o -path "*/outbox/*" \) -type f | grep -q .; then
  write_size_list >> "$TMP_FILE"
else
  echo "- none found" >> "$TMP_FILE"
fi

cat >> "$TMP_FILE" <<'REPORT'

## 3. Found

Directly observed by package-local metadata scan:

REPORT

for rel in package_brief.md user_summary.md package_closeout.md codex_review_bundle.md codex_validation.md analysis_result.md handoff_log.md; do
  if [[ -f "$PACKAGE_ABS/$rel" ]]; then
    printf -- '- `%s`: present\n' "$rel" >> "$TMP_FILE"
  fi
done

raw_count="$(find "$PACKAGE_ABS" -path "*/raw/*" -type f | wc -l | tr -d ' ')"
outbox_count="$(find "$PACKAGE_ABS" -path "*/outbox/*" -type f | wc -l | tr -d ' ')"
printf -- '- raw_files: %s\n' "$raw_count" >> "$TMP_FILE"
printf -- '- outbox_files: %s\n' "$outbox_count" >> "$TMP_FILE"

cat >> "$TMP_FILE" <<'REPORT'

## 4. Candidate Guess

- candidate package-level review files are listed in the header excerpts below when present
- core authored doc candidates are package-root markdown files that are not standard package records
- raw/outbox files are treated as debugging or fidelity evidence by default
- candidate guesses require Codex/User review before becoming reviewed findings
- **Tone Guard:** 모든 후보(Candidate)는 잠정적이며, 확정적 단정(입증됨, 완벽함 등)을 지양합니다.

## 5. Review Needed

- confirm whether the listed deep-read candidates are enough
- confirm whether core authored doc candidates are actually relevant
- confirm whether raw/outbox content needs deeper inspection
- confirm boundary status from package closeout or validation
- reviewed_by: pending

## 6. Core Authored Doc Candidates

REPORT

core_candidates="$(write_core_authored_doc_candidates)"
if [[ -n "$core_candidates" ]]; then
  printf '%s\n' "$core_candidates" >> "$TMP_FILE"
else
  echo "- none found" >> "$TMP_FILE"
fi

cat >> "$TMP_FILE" <<'REPORT'

reviewed_by: pending

## 7. Deep-Read Candidates

REPORT

if [[ -n "$core_candidates" ]]; then
  printf '%s\n' "$core_candidates" >> "$TMP_FILE"
fi

for rel in package_closeout.md user_summary.md codex_validation.md codex_review_bundle.md; do
  if [[ -f "$PACKAGE_ABS/$rel" ]]; then
    printf -- '- `%s`\n' "$rel" >> "$TMP_FILE"
  fi
done

cat >> "$TMP_FILE" <<'REPORT'

## 8. Usually Skip Unless Debugging

- raw JSON files
- full outbox transcripts
- stderr logs with no package-level warning need

## 9. Header Excerpts

REPORT

for rel in package_brief.md user_summary.md package_closeout.md codex_validation.md analysis_result.md codex_review_bundle.md handoff_log.md; do
  write_header_excerpt "$rel"
done

cat >> "$TMP_FILE" <<'REPORT'
## 10. Boundary Check

- package_local_output_only: true
- whole_md_scan: false
- reviewed_by: pending
- judgment_replaced: false

## 11. Closeout

This report is package-local metadata discovery output only.
It does not validate package success.
It does not mark candidate guesses as reviewed.
It does not create graph, ontology, automation, baseline, router, controller, source-space modification, or production workflow.
It does not make baseline promotion or source-space modification decisions.
REPORT

mv "$TMP_FILE" "$OUTPUT_FILE"
trap - EXIT

echo "Package metadata scan report created:"
echo "- $OUTPUT_FILE"
