# Run 033 - Diagnose Run 032 Runner Failure

## Mode

CODEX / SANDBOX ONLY / RUNNER DIAGNOSIS / NO PROMOTION / NO AUTOMATION

## Purpose

Diagnose why the Run 032 Gemini runner invocation did not produce the required Tool Affordance / Caller Shift Lens artifacts, then harden runner evidence capture.

## Files Checked

- app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md
- app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md
- app/work/space-skill-sandbox/review/validation_round_32.md
- app/work/space-skill-sandbox/relay/outbox/run_032_gemini_outbox_*.md
- app/work/space-skill-sandbox/outputs/gemini_raw_results/run_032_gemini_raw_*.json
- app/work/space-skill-sandbox/outputs/gemini_raw_results/run_032_gemini_stderr_*.log

## Findings

- Run 032 required artifacts are still missing.
- A non-dry-run Run 032 invocation was attempted, but it did not materialize the required files.
- The previous runner version captured stdout only, so Gemini CLI stderr errors were not preserved in the raw result or outbox.
- During manual observation, Gemini CLI reported unavailable tools such as `run_shell_command` and `write_file`.
- During manual observation, Gemini CLI also reported model capacity exhaustion for a Gemini preview model.
- A short smoke-text prompt succeeds through the runner.
- A bounded write probe does not create the requested test file and times out.

## Runner Patch

Modified:

- scripts/sandbox/run_gemini_packet.sh

Patch summary:

- stderr is now captured to `app/work/space-skill-sandbox/outputs/gemini_raw_results/*_stderr_*.log`.
- outbox now records `stderr_result`.
- outbox now records Gemini exit code after completed invocations.
- timeout outbox records now include stderr path and stderr tail when present.
- terminal output now prints stderr path for completed and timed-out invocations.

## Tests

- bash -n scripts/sandbox/run_gemini_packet.sh: PASS
- bash scripts/sandbox/run_gemini_packet.sh --help: PASS
- bash scripts/sandbox/run_gemini_packet.sh --preflight: PASS
- bash scripts/sandbox/run_gemini_packet.sh --smoke-text --timeout-seconds 60 smoke_text_033_diagnostic: PASS
- bash scripts/sandbox/run_gemini_packet.sh --timeout-seconds 45 app/work/space-skill-sandbox/test_materials/gemini_write_probe_packet_v0.md write_probe_033_diagnostic: TIMEOUT

## Diagnostic Output Files

- app/work/space-skill-sandbox/relay/outbox/smoke_text_033_diagnostic_gemini_outbox_20260429_182358.md
- app/work/space-skill-sandbox/outputs/gemini_raw_results/smoke_text_033_diagnostic_gemini_raw_20260429_182358.json
- app/work/space-skill-sandbox/outputs/gemini_raw_results/smoke_text_033_diagnostic_gemini_stderr_20260429_182358.log
- app/work/space-skill-sandbox/relay/outbox/write_probe_033_diagnostic_gemini_outbox_20260429_182450.md
- app/work/space-skill-sandbox/outputs/gemini_raw_results/write_probe_033_diagnostic_gemini_raw_20260429_182450.json
- app/work/space-skill-sandbox/outputs/gemini_raw_results/write_probe_033_diagnostic_gemini_stderr_20260429_182450.log

## Root Cause Assessment

The manual runner can call Gemini CLI for short non-interactive responses, but the current CLI/tool configuration is not reliable for direct repo file creation. The failing path is not packet reading or runner launch. The failure is at the Gemini execution/materialization layer:

- file-write tool availability is not stable in the observed Gemini CLI session
- long tool-using tasks may hit model capacity errors
- earlier runner evidence capture hid these errors because stderr was not saved

## Run 033 Verdict

FAIL

Run 032 cannot be validated because its required lens, run record, and validation record are missing. Run 034 packet should not be created from this failed materialization path.

## Recommended Next Step

Prepare a response-bundle variant of the Run 032 Gemini packet. Gemini should return the target file contents as a structured file bundle instead of directly writing repository files. Codex should then validate and materialize the bundle into sandbox files.

This keeps the intended split:

- Gemini: heavy analysis and drafting
- Codex: repo file manager, validation, and next packet generation

## Retry Packet Created

- app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_032_tool_affordance_response_bundle_retry_v0.md

This packet is for rerunning Run 032 in response-bundle mode. It is not a Run 034 packet.

## Closeout

This is a sandbox runner diagnosis run only.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, router, controller, ontology, schema, agent implementation, tool installation, existing program merge, or production workflow was created.
