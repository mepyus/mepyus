# Package 008 Smoke Test Result

## Target

- script: `scripts/sandbox/package_metadata_scan.sh`
- smoke package: `app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback`
- generated report: `app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback/metadata_scan_report.md`

## Commands Tested

- `bash -n scripts/sandbox/package_metadata_scan.sh`
- `bash scripts/sandbox/package_metadata_scan.sh --help`
- `bash scripts/sandbox/package_metadata_scan.sh app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback`
- `bash scripts/sandbox/package_metadata_scan.sh app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback`
- `bash scripts/sandbox/package_metadata_scan.sh app/work/space-skill-sandbox`
- `bash scripts/sandbox/package_metadata_scan.sh app/work/space-skill-sandbox/packages`

## Results

- syntax_check: PASS
- help_output: PASS
- package_003_smoke: PASS
- report_created_package_local: true
- reviewed_left_pending: true
- whole_md_scan_declared_false: true
- overwrite_refusal: PASS
- invalid_path_rejection: PASS
- packages_root_rejection: PASS
- output_outside_package: false

## Notes

The second smoke command refused to overwrite the existing report with exit code `3`.
Invalid paths were rejected with exit code `2`.
The generated report records `reviewed_by: pending` and does not assign Reviewed status.

