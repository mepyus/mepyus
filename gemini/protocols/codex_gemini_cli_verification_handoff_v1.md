# Codex-Gemini CLI Verification Handoff v1

Date: 2026-04-26

## 0. Purpose

This protocol defines a low-conflict collaboration loop between Codex and Gemini CLI.

Codex owns task framing, code edits, canonical interpretation, and final user return.
Gemini CLI may run bounded tests, inspect results, and write verification records only in a reserved Gemini output lane.

The goal is simple:

1. Codex gives Gemini a narrow instruction packet.
2. Gemini performs read-only or test-only verification.
3. Gemini writes a structured verification return under `gemini/`.
4. Codex reads that return, decides what it means, and reports or patches from there.

## 1. Authority Split

| Area | Codex | Gemini CLI |
|---|---|---|
| User intent interpretation | owner | no |
| Code edits | owner | no |
| Canonical docs / runtime state | owner | no |
| Test command execution | may run directly or delegate | bounded delegation allowed |
| Verification observation | owner of final interpretation | may produce evidence |
| Final answer to user | owner | no |
| Writing collaboration artifacts | may write anywhere allowed by task | `gemini/verification_returns/` only |

Gemini output is evidence, not a decision. Codex must translate the result before it affects repo behavior, baseline, status, or user-facing claims.

## 2. Collision Boundaries

Gemini CLI must not modify:

- source code
- tests
- `runtime/`
- `docs/`
- `app/`
- manifests
- read maps
- package locks
- root configuration files
- staged Git state

Gemini CLI may write only:

- `gemini/verification_returns/<task_id>.md`
- `gemini/verification_returns/<task_id>.json`

Codex should treat any Gemini write outside this lane as invalid until the user explicitly approves it.

## 3. Safe Gemini Task Types

Use Gemini CLI for tasks where independent execution or inspection is useful but edit authority is unnecessary:

- run a specified test command and record exact outcome
- inspect a build or lint failure and summarize likely cause
- compare Codex's claimed result with terminal output
- check whether a specific file/path/report exists
- review a small diff in read-only mode
- cross-check that an artifact follows a named schema

Do not use Gemini CLI for:

- designing broad architecture
- choosing canonical state
- making patches
- deleting, moving, or renaming files
- resolving Git conflicts
- deciding whether to commit or push

## 4. Codex Instruction Packet

Codex should give Gemini a packet with this exact shape.

```text
TASK_ID: <stable_short_id>
ROLE: bounded verification worker

INPUTS:
- <exact files, commands, or artifacts to inspect>

COMMANDS_ALLOWED:
- <exact command 1>
- <exact command 2>

FORBIDDEN:
- Do not modify source files.
- Do not modify tests.
- Do not edit docs, runtime, app, scripts, manifests, package files, or Git state.
- Do not propose broad refactors.
- Do not finalize policy or status.

OUTPUT_DESTINATION:
- gemini/verification_returns/<task_id>.md

OUTPUT_SHAPE:
- task_id
- commands_run
- exit_codes
- observed_output_summary
- pass_fail_unknown
- evidence_paths
- suspected_issue_if_any
- limits_or_uncertainties
- recommendation_to_codex
```

If Gemini cannot run a command, it should record `pass_fail_unknown: unknown` and explain the environment blocker.

## 5. Gemini Return Contract

Every Gemini verification return must include this block:

```yaml
task_id:
worker: gemini_cli
return_type: verification_return
status: completed | blocked | failed
pass_fail_unknown: pass | fail | unknown
commands_run:
exit_codes:
evidence_paths:
files_modified: []
codex_action_needed: none | inspect | patch | rerun | ask_user
```

`files_modified` must be an empty list unless the only modified files are the allowed verification return files.

## 6. Codex Intake Rule

After Gemini returns, Codex must do three checks before using the result:

1. Path check: Gemini wrote only under `gemini/verification_returns/`.
2. Evidence check: claims are tied to commands, exit codes, or file paths.
3. Authority check: recommendations are treated as input to Codex, not accepted as final decisions.

If any check fails, Codex should mark the return as `invalid_or_needs_review` and avoid using it as proof.

## 7. Preferred Loop

1. Codex implements or frames the work.
2. Codex creates a Gemini packet.
3. Gemini runs the exact allowed commands or inspections.
4. Gemini writes a verification return.
5. Codex reads the return and, if needed, patches or reruns locally.
6. Codex gives the user the final summary, including whether Gemini verification passed, failed, or was blocked.

This keeps Gemini useful as an independent verifier without letting two agents edit the same surface.

## 8. Minimal Prompt Template

```text
You are Gemini CLI acting as a bounded verification worker for Codex.

Follow this packet exactly. You may run only the commands listed under COMMANDS_ALLOWED.
Do not modify source files, tests, docs, runtime, app, scripts, manifests, package files, or Git state.
Write your return only to OUTPUT_DESTINATION.

<paste Codex instruction packet here>
```

## 9. Closeout Rule

Codex may say "Gemini verified this" only when the Gemini return includes:

- exact command or inspection performed
- exit code or concrete observed evidence
- no unauthorized file modifications
- clear pass/fail/unknown status

Otherwise Codex should say "Gemini produced a review note" or "Gemini verification was blocked," not "verified."
