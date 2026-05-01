# Gemini CLI Sandbox Execution Protocol v0

## 1. status

```yaml
protocol_status: sandbox_execution_protocol
default_permission: no-write
execution_mode: read_only_or_sandbox
baseline_lock: false
runtime_manifest: false
schema_enforcement: false
```

## 2. execution principle

Gemini may execute.

Gemini must not modify existing repo files.

Allowed execution modes:

- read-only inspection
- dry-run
- check mode
- stdout-only execution
- sandbox-output execution

## 3. sandbox output path

If Gemini must create output files, the instruction must explicitly provide:

```text
runtime/gemini_sandbox/<case_id>/
```

No other output path is allowed by default.

The path must be task-specific. Gemini must not invent global runtime or manifest paths.

## 4. pre-execution fields

Gemini must confirm:

```text
case_id:
task_type:
scope_level:
script_or_command:
input_ref:
output_mode:
output_path:
forbidden_write_paths:
```

If `output_path` is blank and the command writes files, do not run.

## 5. post-execution fields

Gemini must return:

```text
Verdict:
Task type:
Scope level:
Command run:
Exit code:
Output mode:
Output path:
Files modified:
Files created:
Files deleted:
Files overwritten:
Stdout summary:
Stderr summary:
Risk:
Next:
```

## 6. failure behavior

If execution fails, Gemini must not fix files.

Return:

```text
Execution failed.
Do not modify files.
Observed error:
Likely cause:
Suggested next check:
Needs Codex:
```

## 7. important prohibitions

- Do not modify files to fix failure.
- Do not create missing files.
- Do not change paths and retry broadly.
- Do not scan the whole repo.
- Do not run whole test suite.
- Do not clean caches or build outputs.
- Do not generate runtime manifests.
- Do not update indexes.
- Do not promote sandbox output into repo truth.

## 8. safe verdict guide

### PASS

Use when:

- command was allowed
- no existing files changed
- output mode matched the instruction
- stdout/stderr were summarized
- risk was stated

### PASS_WITH_NOTE

Use when:

- command ran but output is incomplete
- sandbox output exists but needs Codex review
- stderr has warnings
- result should not be promoted

### HOLD

Use when:

- command might write existing files
- output path is unclear
- source surface or task scope is unclear
- failure requires human/Codex decision

### FAIL

Use when:

- forbidden command was used
- existing files were modified/deleted/moved/overwritten
- schema/controller/runtime/index changes occurred
