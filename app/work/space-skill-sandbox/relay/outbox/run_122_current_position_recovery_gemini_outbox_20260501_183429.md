# Gemini Run Result

- packet: app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_122_current_position_recovery_v0.md
- run_id: run_122_current_position_recovery
- timestamp: 20260501_183429
- dry_run: false
- smoke_text: false
- output_format: json
- timeout_seconds: 120
- raw_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/run_122_current_position_recovery_gemini_raw_20260501_183429.json
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/run_122_current_position_recovery_gemini_stderr_20260501_183429.log

## Result

Gemini CLI timed out after 120 seconds.

- timeout_seconds: 120
- command_attempted: gemini -p "<prompt redacted>" --output-format json
- gemini_path: /usr/local/bin/gemini
- gemini_version: 0.40.0
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/run_122_current_position_recovery_gemini_stderr_20260501_183429.log
- likely_state: tool_configuration_error
- next_manual_check: gemini -p "Reply with exactly: GEMINI_SMOKE_OK" --output-format json

## Stderr Tail

Ripgrep is not available. Falling back to GrepTool.
Attempt 1 failed: You have exhausted your capacity on this model. Your quota will reset after 2s.. Retrying after 5001ms...
Attempt 1 failed: You have exhausted your capacity on this model. Your quota will reset after 0s.. Retrying after 5426ms...
Attempt 1 failed: You have exhausted your capacity on this model. Your quota will reset after 4s.. Retrying after 5568ms...
Error executing tool write_file: Tool "write_file" not found. Did you mean one of: "read_file", "update_topic", "grep_search"?
Error executing tool write_file: Tool "write_file" not found. Did you mean one of: "read_file", "update_topic", "grep_search"?
Error executing tool run_shell_command: Tool "run_shell_command" not found. Did you mean one of: "update_topic", "grep_search", "invoke_agent"?
Error executing tool run_shell_command: Tool "run_shell_command" not found. Did you mean one of: "update_topic", "grep_search", "invoke_agent"?
[LocalAgentExecutor] Blocked call: Unauthorized tool call: 'run_shell_command' is not available to this agent.
Attempt 1 failed: You have exhausted your capacity on this model. Your quota will reset after 1s.. Retrying after 5454ms...
[LocalAgentExecutor] Blocked call: Unauthorized tool call: 'write_file' is not available to this agent.
[LocalAgentExecutor] Blocked call: Unauthorized tool call: 'write_file' is not available to this agent.
Attempt 1 failed: You have exhausted your capacity on this model. Your quota will reset after 4s.. Retrying after 5396ms...

No repository files were modified by this runner.
