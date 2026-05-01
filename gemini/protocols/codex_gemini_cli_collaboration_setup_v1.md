# Codex-Gemini CLI Collaboration Setup v1

Date: 2026-04-26

## 0. Setup Summary

This is the active collaboration setting for Codex and Gemini CLI.

Codex designs structure, applies patches, frames task boundaries, and makes final decisions.
Gemini CLI runs bounded verification loops and records evidence for Codex to read back.

Gemini is not a second canonical editor. Gemini is a bounded verification worker.

## 1. Active Reading Locations

Gemini CLI should learn this operating mode from these files, in this order:

1. `gemini/readme.md`
2. `gemini/protocols/gemini_task_dispatch_policy_v1.md`
3. `gemini/protocols/codex_gemini_cli_verification_handoff_v1.md`
4. `gemini/protocols/codex_gemini_cli_collaboration_setup_v1.md`

Codex should use the same files before delegating verification work to Gemini CLI.

## 2. Operating Agreement

| Step | Owner | Rule |
|---|---|---|
| Structure design | Codex | Codex decides shape, scope, and safety boundary. |
| Code / doc patch | Codex | Gemini does not patch source, docs, runtime, app, scripts, package files, or Git state. |
| Verification packet | Codex | Codex gives exact inputs, exact allowed commands, and exact output destination. |
| Test / check execution | Gemini CLI | Gemini may run only listed commands or inspections. |
| Verification return | Gemini CLI | Gemini writes only under `gemini/verification_returns/`. |
| Result interpretation | Codex | Codex decides whether the evidence means pass, fail, blocked, or needs rerun. |
| User-facing answer | Codex | Codex summarizes the verified state and remaining uncertainty. |

## 3. Conflict Resolution

If a task packet and a general Gemini rule conflict, the stricter rule wins.

Examples:

- If a command might modify source files, Gemini must not run it unless Codex explicitly permits that exact output path and the user has accepted the risk.
- If Gemini discovers a likely fix, Gemini records it as `recommendation_to_codex`; it does not patch.
- If Gemini needs a command outside `COMMANDS_ALLOWED`, it records `blocked` or `unknown`.
- If Gemini writes outside `gemini/verification_returns/`, Codex treats the return as invalid until reviewed.

## 4. Allowed Gemini Execution Meaning

The phrase "Gemini may execute" means only this:

- run a specified test, lint, build, schema check, file existence check, or read-only diff inspection
- collect exit codes and concise output evidence
- write a verification return

It does not mean:

- edit implementation
- change canonical status
- decide policy
- alter manifests, runtime, app, scripts, docs, or Git state
- commit or push

## 5. Standard Delegation Prompt

Codex should use this prompt shape when handing work to Gemini CLI:

```text
Read these files first:
- gemini/readme.md
- gemini/protocols/gemini_task_dispatch_policy_v1.md
- gemini/protocols/codex_gemini_cli_verification_handoff_v1.md
- gemini/protocols/codex_gemini_cli_collaboration_setup_v1.md

You are Gemini CLI acting as a bounded verification worker for Codex.
Run only the commands listed below.
Do not modify source files, tests, docs, runtime, app, scripts, manifests, package files, or Git state.
Write your return only to the output destination.

TASK_ID: <task_id>
INPUTS:
- <exact input path>

COMMANDS_ALLOWED:
- <exact command>

OUTPUT_DESTINATION:
- gemini/verification_returns/<task_id>.md

Return the required verification block plus a short evidence summary.
```

## 6. Codex Intake Checklist

Before using a Gemini return, Codex checks:

- Return path is under `gemini/verification_returns/`.
- Return includes commands run and exit codes.
- Return includes `pass_fail_unknown`.
- Return includes evidence paths or concrete terminal observations.
- Return does not claim final authority.
- No unauthorized files were modified.

Only after this checklist passes may Codex describe the result as Gemini-verified.

## 7. Practical Use

Use this collaboration mode when:

- Codex has designed or patched a structure and needs independent test feedback.
- A command loop is repetitive and evidence-oriented.
- The risk is in runtime behavior, not in deciding architecture.
- The result can be represented as pass, fail, or unknown with evidence.

Keep the design and final interpretation in Codex. Keep the verification loop in Gemini.
