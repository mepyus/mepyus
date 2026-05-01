# Manual Gemini Runner Script Candidate v0

## 0. Status
- status: sandbox candidate
- automation: false
- relay_v1: false
- source_space_rule: false
- baseline: false
- runner_executes_only_on_manual_command: true

## 1. Purpose
This document defines a candidate manual-triggered Gemini runner for the current Codex -> Gemini -> Codex sandbox chain.

The runner reads a saved Gemini task packet, calls Gemini CLI in non-interactive mode, and stores the raw and readable result files. It does not apply Gemini output to the repository.

## 2. Allowed Scope
The candidate script may:
- read one packet file supplied by the user
- call `gemini -p` only when the user explicitly runs the script
- write a markdown outbox result
- write a raw JSON or raw text result
- record packet path, run id, timestamp, mode, and output paths
- support `--dry-run` for local testing without Gemini API calls
- support `--timeout-seconds` so an auth/network wait cannot hang the operator session indefinitely

The candidate script must not:
- watch folders
- install Gemini CLI
- create hooks
- create MCP
- run in the background
- modify source-space
- apply Gemini output to files
- create baseline
- declare Relay v1.0
- modify worker guides
- create worker_guide_v0_4
- merge existing programs
- create production workflow

## 3. Files
Script candidate:

```text
scripts/sandbox/run_gemini_packet.sh
```

Default output locations:

```text
app/work/space-skill-sandbox/relay/outbox
app/work/space-skill-sandbox/outputs/gemini_raw_results
```

## 4. Command Shape
Expected use:

```bash
bash scripts/sandbox/run_gemini_packet.sh \
  app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_032_tool_affordance_v0.md \
  run_032
```

Dry-run use:

```bash
bash scripts/sandbox/run_gemini_packet.sh --dry-run \
  app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_032_tool_affordance_v0.md \
  run_032
```

## 5. Output Contract
The markdown outbox result should include:
- packet path
- run id
- timestamp
- command mode
- raw output path
- timeout seconds
- Gemini response, or dry-run note

The raw result file should preserve the original Gemini CLI output whenever an actual call is made.

## 6. Safety Rationale
This is lower risk than copy/paste automation because the user still explicitly triggers each run. It keeps the user's judgment point while reducing manual prompt transfer.

The runner is not an automation system because it does not monitor files or invoke itself.

The runner is not an application step because it only stores Gemini output. Codex or a reviewer must validate and decide whether any generated content should become a sandbox artifact.

## 7. Relationship To Sandbox Execution Chain
This candidate extends `sandbox_execution_chain_v0` with an optional terminal handoff path:

```text
Codex writes next Gemini task packet
→ user runs script manually
→ script stores Gemini result
→ Codex/reviewer reads result
→ Codex/reviewer validates and creates next packet
```

## 8. Non-Automation Note
This document is not automation.
This document is not Relay v1.0.
This document is not MCP, hook, or watch mode.
This document is not an agent implementation.
This document is not source-space promotion.

## 9. Closeout Note
This document is a sandbox manual Gemini runner candidate only.
No automation was created.
No Relay v1.0 was declared.
No source-space promotion was performed.
No baseline was created.
No worker_guide_v0_4 was created.
The runner script candidate only reads a packet and stores Gemini output when manually invoked by the user.

## 10. 4-line Footer
status: 완료
summary: manual_gemini_runner_script_candidate_v0는 사용자가 명시적으로 실행하는 Gemini CLI packet runner 후보의 허용 범위와 금지선을 정의함
risk: runner를 watch mode, hook, automation, source-space modifier, Gemini 결과 자동 적용기로 오해하면 안 됨
next: scripts/sandbox/run_gemini_packet.sh를 dry-run으로 검증한 뒤 실제 Gemini 호출은 사용자 승인/인증 상태와 timeout 결과에 따라 별도 수행
