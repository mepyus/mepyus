# Integrated Engine First Real Worker Run Validation v0

## 1. Verdict

PASS

## 2. Selected Package

- package_id: `pkg_openharness_structure_probe`
- package title: `OpenHarness 구조 분석`
- reason for selection: this package already had continuity history and a clear bounded target under `references/git_search/openharness-main`.

This package previously contained dry-run / normalized / parser-fallback continuity records. Package 3 tested whether actual external worker output could become real notebook material.

## 3. Bounded Task Selection

Step A task:

- real bounded structural profile of `references/git_search/openharness-main`
- focus only on repo role, top-level areas, concrete files/dirs for next inspection, and a package-specific next hint

Why this task was chosen:

- real enough to require actual source reading
- bounded enough to avoid giant open-ended analysis
- output can be validated by concrete artifact refs
- naturally supports a continuation run

Step B task:

- continue from Step A, using Step A artifacts and selected OpenHarness execution/tool/permission refs
- extract bounded worker-boundary lessons for VectorFL
- identify what Package 4 should validate

## 4. Execution Condition

Actual Codex CLI execution was required.

Initial sandboxed actual-run attempt failed with a permission error:

- `thread/start: Operation not permitted`

The actual validation runs were then executed outside the sandbox with explicit escalation. The Codex CLI itself used read-only mode:

```text
codex exec --skip-git-repo-check --sandbox read-only --cd <repo> -
```

No files were intentionally modified by the worker runs.

## 5. Step A Result

Session:

- `cli_20260418T224406Z_754042af`

Result:

- status: `done`
- `worker_return_source`: `worker_emitted`

Notebook-readable answer:

- OpenHarness was identified as a Python agent-harness package with CLI entrypoints, provider/auth plumbing, streaming query execution, tool registry, permissions, MCP, skills/plugins, memory/context, sandboxing, background tasks, swarm/subagent coordination, and a React/Ink terminal surface.

Key findings included:

- package distribution / console script shape
- README framing as agent infrastructure
- `QueryEngine` and `run_query` as central model/tool loop surfaces
- `BaseTool` / `ToolRegistry` as normalized tool abstraction
- `PermissionChecker` as relevant boundary material

Concrete artifact refs included:

- `references/git_search/openharness-main/README.md`
- `references/git_search/openharness-main/pyproject.toml`
- `references/git_search/openharness-main/src/openharness/cli.py`
- `references/git_search/openharness-main/src/openharness/engine/query_engine.py`
- `references/git_search/openharness-main/src/openharness/engine/query.py`
- `references/git_search/openharness-main/src/openharness/tools/base.py`
- `references/git_search/openharness-main/src/openharness/tools/agent_tool.py`
- `references/git_search/openharness-main/src/openharness/permissions/checker.py`

Step A produced a specific continuation hint to inspect the OpenHarness execution path and map the smallest analogous VectorFL worker-boundary lessons.

## 6. Step B Continuation Result

Session:

- `cli_20260418T224608Z_681737e8`

Result:

- status: `done`
- `worker_return_source`: `worker_emitted`

Step B used prior Step A artifacts directly:

- `runtime/cli_sessions/cli_20260418T224406Z_754042af/structured_return.json`
- `runtime/cli_sessions/cli_20260418T224406Z_754042af/operator_report.md`
- `runtime/cli_sessions/cli_20260418T224406Z_754042af/stdout.log`

Step B also inspected bounded source refs from Step A's recommended path:

- `references/git_search/openharness-main/src/openharness/cli.py`
- `references/git_search/openharness-main/src/openharness/engine/query_engine.py`
- `references/git_search/openharness-main/src/openharness/engine/query.py`
- `references/git_search/openharness-main/src/openharness/tools/base.py`
- `references/git_search/openharness-main/src/openharness/permissions/checker.py`
- `app/runtime/vectorfl_integrated_engine_api.py`

Notebook-readable continuation answer:

- Step A established OpenHarness as useful internal lens material because its relevant boundaries are CLI entrypoint selection, session/query loop state, tool schema/normalization, permission decisions, streamed execution events, and post-run return normalization.

Key continuation findings included:

- Step A identified the correct continuation target: concrete worker/session boundary, not broad repo overview.
- OpenHarness CLI routes print, task-worker, and interactive modes through explicit entrypoint branches.
- `QueryEngine.submit_message` builds `QueryContext` and delegates the model/tool loop to `run_query`.
- `run_query` streams assistant events, executes tools, normalizes tool results, and appends tool-result user messages.
- Tool execution validates inputs before permission evaluation and execution.

Step B produced a Package 4-oriented next hint:

- validate worker-return handling with valid worker-emitted JSON, missing-block fallback, invalid-JSON fallback, suggested-next-use classification, failed/timeout routing, and deposit-candidate non-ingestion checks.

## 7. Notebook Continuity Judgment

Notebook continuity passed.

The package now reads as ongoing work, not only contract smoke:

- Step A entered as real source-reading work.
- Step B reused Step A's structured return and artifacts.
- The latest notebook run shows answer, findings, artifact refs, source refs, return source, and next continue hint.
- Prior dry-run / normalized runs remain visible behind the newer actual worker runs.

Important correction made during validation:

- The worker's concrete `next_continue_hint` was initially being overwritten by a generic `validation_target` route phrase.
- The RunRecord projection was adjusted to prefer the worker-return hint when present.
- After correction, notebook latest hint directly points toward Package 4 normalization validation.

## 8. Worker Return Source Summary

Observed package sources:

- Step A: `worker_emitted`
- Step B: `worker_emitted`
- prior OpenHarness dry-run: `runtime_normalized`
- older parser-derived run: `parser_fallback`

This confirms that the notebook can distinguish actual worker-emitted returns from normalized/fallback continuity.

## 9. Supervisor Judgment

The supervisor can judge the next step from notebook-visible material:

- what happened: real OpenHarness structure profile and continuation reread
- what was produced: concrete boundary lessons and source refs
- what remains limited: source inspection only, no behavioral execution trace
- what comes next: Package 4 normalization hardening with specific cases

This is materially stronger than a dry-run record board.

## 10. Risks

Remaining risks:

- only Codex was tested, not Gemini
- source inspection does not prove OpenHarness runtime behavior
- worker-emitted block proves structured return compliance, not full work quality
- Package 4 may require write-enabled test/fixture work if normalization needs regression coverage
- continuation depth is real but still one step only

## 11. Package 4 Readiness

Package 4 is ready.

Recommended Package 4 focus:

- valid `worker_emitted` JSON path
- missing block fallback
- invalid JSON fallback
- partial-field normalization
- failed/timeout routing
- preservation of concrete artifact refs vs findings
- non-ingestion boundary for deposit candidates
