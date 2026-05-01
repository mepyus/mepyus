# Integrated Engine Worker Adapter Prompt Contract v0

## 1. Purpose

This contract makes actual worker returns less dependent on post-hoc parsing.

Package 1 identified the narrow boundary:

`CodexCliAdapter.start_run(...)` after stdout/stderr/exit status are known and before `structured_return.json` is written.

Package 2 adds the minimal actual-worker prompt contract for that boundary.

## 2. Required Worker-Emitted Block

Actual workers should include one parseable block near the end of stdout.

The delimiter must appear on its own lines:

```text
WORKER_RETURN_JSON
{
  "schema_version": "integrated_engine_worker_return_v0",
  "worker_id": "codex",
  "package_id": "<package id if known>",
  "run_kind": "<task type>",
  "answer": "<direct answer or main response>",
  "findings": ["<key observation>"],
  "files_artifacts": ["<path or artifact ref>"],
  "next_continue_hint": "<specific next step for this same package>",
  "open_questions": ["<unresolved blocker>"],
  "risks_or_limits": ["<uncertainty or limit>"],
  "source_refs": ["<bounded context ref actually used>"]
}
END_WORKER_RETURN_JSON
```

Arrays must remain JSON arrays of strings.

## 3. Prompt Boundary

The current adapter prompt is formed in:

- `_cli_session_prompt(session_spec)`

The prompt asks for:

- a short human-readable return
- the bounded structured block
- no file modification unless explicitly requested elsewhere

This does not create a new worker system. It only makes the existing actual worker return boundary more inspectable.

## 4. Extraction Rule

The runtime extracts only a delimiter block where:

- `WORKER_RETURN_JSON` appears alone on a line
- `END_WORKER_RETURN_JSON` appears alone on a later line
- the body parses as JSON object

Mentions of `WORKER_RETURN_JSON` inside prose or inside JSON strings are ignored as delimiters.

## 5. Return Source Labels

`worker_return_source` is recorded as one of:

- `worker_emitted`: a valid delimiter JSON block was found in actual stdout
- `runtime_normalized`: runtime generated or normalized structured return from controlled material
- `parser_fallback`: structure was inferred from raw text bullets/profile cues
- `raw_fallback`: only raw answer text could be preserved

The supervisor should prefer `worker_emitted` for actual worker validation.

## 6. Fallback Rule

If the worker block is missing or invalid:

1. preserve stdout/stderr artifacts
2. preserve top-level `result_summary`
3. normalize through `_normalize_worker_return(...)`
4. label the source as `runtime_normalized`, `parser_fallback`, or `raw_fallback`

Old sessions remain readable.

## 7. Non-Goals

This contract does not implement:

- multi-agent orchestration
- worker switching UX
- dashboard expansion
- artifact viewer
- streaming terminal
- automatic line / axis detection
- broad schema growth beyond the current worker return need

## 8. Package 3 Readiness Condition

Package 3 may proceed when:

- one actual worker run writes `worker_return_source = worker_emitted`
- package notebook can read that run as latest package material
- fallback behavior remains intact for missing block cases
