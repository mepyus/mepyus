# Run 049 - Package 000 Actual Handoff Smoke

## Mode

CODEX / SANDBOX ONLY / ACTUAL HANDOFF SMOKE / NO PROMOTION / NO AUTOMATION

## Purpose

Check whether the package handoff and collect structure created in Run 048 works beyond dry-run mode.

This is not a real work package execution. It is a handoff layer smoke test.

## Package

- app/work/space-skill-sandbox/packages/package_000_smoke

## Executed

- bash scripts/sandbox/package_handoff.sh app/work/space-skill-sandbox/packages/package_000_smoke
- bash scripts/sandbox/package_collect.sh app/work/space-skill-sandbox/packages/package_000_smoke
- bash scripts/sandbox/package_handoff.sh --timeout-seconds 15 app/work/space-skill-sandbox/packages/package_000_smoke
- bash scripts/sandbox/package_collect.sh app/work/space-skill-sandbox/packages/package_000_smoke

## Result

The package handoff script invoked Gemini CLI in non-dry-run mode, but Gemini CLI entered an interactive browser authentication prompt and timed out.

Evidence:

- dry_run: false
- timeout: true
- likely_state: auth_interactive_wait
- raw prompt observed: `Opening authentication page in your browser. Do you want to continue? [Y/n]:`

## Generated / Updated

- app/work/space-skill-sandbox/relay/outbox/package_000_smoke_handoff_gemini_outbox_20260430_173755.md
- app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_raw_20260430_173755.json
- app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_stderr_20260430_173755.log
- app/work/space-skill-sandbox/relay/outbox/package_000_smoke_handoff_gemini_outbox_20260430_174354.md
- app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_raw_20260430_174354.json
- app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_stderr_20260430_174354.log
- app/work/space-skill-sandbox/packages/package_000_smoke/codex_review_bundle.md
- app/work/space-skill-sandbox/packages/package_000_smoke/handoff_log.md

## Script Patch During Diagnosis

- scripts/sandbox/run_gemini_packet.sh now classifies auth prompts as `auth_interactive_wait`.
- scripts/sandbox/run_gemini_packet.sh now includes raw tail in timeout outbox records.
- scripts/sandbox/package_handoff.sh now records runner exit code even when the runner fails.

## Boundary Check

- source_space_modified: false
- baseline_created: false
- relay_v1_declared: false
- automation_created: false
- hook_created: false
- mcp_created: false
- watch_mode_created: false
- agent_implementation_created: false
- production_workflow_created: false
- gemini_result_auto_applied: false

## Verdict

PASS

The transport layer invoked Gemini CLI, received `PACKAGE_SMOKE_OK`, captured raw/outbox evidence, recorded runner exit code 0, and collected package evidence.

Earlier non-escalated `package_handoff.sh` attempts entered `auth_interactive_wait`. Direct runner calls and the approved `package_handoff.sh` prefix succeeded. The observed failure was therefore not packet content or script structure; it was execution-environment dependent.

Successful evidence:

- app/work/space-skill-sandbox/relay/outbox/package_000_smoke_handoff_gemini_outbox_20260430_174854.md
- app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_raw_20260430_174854.json
- app/work/space-skill-sandbox/outputs/gemini_raw_results/package_000_smoke_handoff_gemini_stderr_20260430_174854.log

## Next

Use the approved `bash scripts/sandbox/package_handoff.sh` execution path for future actual handoff smoke tests.

If auth prompts reappear, stabilize Gemini CLI authentication for non-interactive use. Candidate options are:

- complete interactive Google login manually in a normal terminal
- provide `GEMINI_API_KEY`
- configure Vertex/Google Cloud credentials intentionally

Credential values must not be printed in logs.

## Closeout

This is a sandbox package handoff smoke run only.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No automation, hook, MCP, watch mode, router, controller, ontology, schema, agent implementation, tool installation, Gemini result auto-application, or production workflow was created.
