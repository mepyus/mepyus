# Codex Plan - Package 001

## Role Split

- Codex: package orchestrator and validator
- Gemini: bounded analysis worker
- script: transport layer only
- User: final judge

## Execution Shape

This package uses three subpackage sessions because `package_handoff.sh` transports one `gemini_packet.md` per package directory.

Session package directories:

- app/work/space-skill-sandbox/packages/package_001_external_lens_reread/session_01_agent_harness
- app/work/space-skill-sandbox/packages/package_001_external_lens_reread/session_02_tool_lives_beyond_maker
- app/work/space-skill-sandbox/packages/package_001_external_lens_reread/session_03_mini_swe_agent

## Validation Shape

After all handoffs and collections:

- read each session outbox
- check transport success
- check boundary violations
- synthesize package-level lenses
- write `codex_validation.md`
- write `user_summary.md`
- write `package_closeout.md`
