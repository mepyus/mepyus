# Gemini Run Result

- packet: app/work/space-skill-sandbox/packages/package_000_smoke/gemini_packet.md
- run_id: package_000_smoke_handoff
- timestamp: 20260430_174744
- dry_run: false
- smoke_text: false
- output_format: json
- timeout_seconds: 30
- raw_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_raw_20260430_174744.json
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_stderr_20260430_174744.log

## Result

Gemini CLI timed out after 30 seconds.

- timeout_seconds: 30
- command_attempted: gemini -p "<prompt redacted>" --output-format json
- gemini_path: /usr/local/bin/gemini
- gemini_version: 0.40.0
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_stderr_20260430_174744.log
- likely_state: auth_interactive_wait
- next_manual_check: gemini -p "Reply with exactly: GEMINI_SMOKE_OK" --output-format json

## Raw Tail


Opening authentication page in your browser. Do you want to continue? [Y/n]: 
No repository files were modified by this runner.
