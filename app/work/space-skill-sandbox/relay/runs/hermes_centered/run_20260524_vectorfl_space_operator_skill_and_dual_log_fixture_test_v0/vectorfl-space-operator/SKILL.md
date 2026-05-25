---
name: vectorfl-space-operator
description: Use when working in VectorFL Hermes-centered loops where Codex must check space, retrieve space references for Hermes, analyze Hermes execution/reentry logs, propose HOLD-only space maturation, or preserve dual-log collision-free Hermes/Codex namespaces.
metadata:
  short-description: Operate VectorFL space around Hermes execution
---

# VectorFL Space Operator

Use this skill when the user asks to check VectorFL space, analyze Hermes work, retrieve space material for Hermes, judge reentry-based maturation, or maintain collision-free Hermes/Codex logs.

## Role Split

Hermes is the execution workbench:
- preserves original input
- requests Codex space retrieval through CLI/script bridge when needed
- merges original + retrieved space + model reasoning
- executes or withholds
- writes trace, receipt, and Codex-readable reentry records

Codex is the space operator:
- checks the current space
- retrieves bounded space refs for Hermes
- analyzes Hermes work after execution
- judges space delta and maturation pressure
- decides whether Gemini exploration is needed
- proposes HOLD-only index/layer/schema updates
- inspects how program results act inside the space, not only whether local tests pass

Gemini is optional and Codex-internal:
- use only when Codex needs wider layer/space analysis
- never treat Gemini output as authority
- Hermes does not call Gemini directly

## Stack Order

Use this order when instructions or artifacts appear to conflict:

1. Governance layer decides role, boundary, and policy.
2. Router layer maps the instruction to a Codex route.
3. Dual-log layer decides where each actor writes and how cross-inspection works.
4. Space maturation layer decides how execution/reentry results should be remembered.
5. Program-result space-effect layer decides how local program outputs affect the space.
6. Return schemas decide packet fields.

If governance and router disagree, governance wins for role/boundary; router wins for route-specific reads and return fields. If Codex proposes maturation but Hermes has no user approval, Hermes records HOLD receipt only.

## Routes

For `공간을 확인해`, run `CODEX_SPACE_CHECK`.
Read compact controls and current handoff handles, then return space snapshot, active controls, relevant assets, missing handles, next safe lane, and HOLD boundary.

For `헤르메스 작업 내용을 분석해`, run `CODEX_HERMES_WORK_ANALYSIS`.
Read Hermes merge/trace/reentry/validation and answer what Hermes took from space, how it merged with model reasoning, what it executed or held, and what should re-enter space.

For `공간자료를 찾아줘` or a Hermes retrieval request, run `CODEX_SPACE_RETRIEVAL_BY_ORIGINAL`.
Return selected refs, rejected refs, original-to-space fit, changed judgment for Hermes, risks, recommended Hermes merge inputs, and HOLD status.

For `공간 숙성 판단해` or a Hermes reentry record, run `CODEX_SPACE_MATURATION_BY_REENTRY_RECORD`.
Return maturation decision, proposed reindex/layer/schema changes, Gemini use decision, rejected maturation options, risks, next safe lane, and HOLD status.

For function or program checks, inspect the space effect after local pass/fail.
Separate program behavior, execution trace, space contact, space effect, and maturation decision. Classify the result as no space effect, reference evidence, pattern confirmed/strengthened/changed, new pattern candidate, missing handle, stale/superseded effect, duplicate pressure, boundary risk, or reentry repair needed.

For every maturation pass, follow:
`OBSERVE -> CLASSIFY -> COMPARE -> JUDGE_SPACE_DELTA -> DECIDE_GEMINI -> PROPOSE_MATURATION -> VERIFY -> RETURN`.

## Dual-Log Rule

Use collision-free namespaces:
- Hermes writes only `hermes_exec/`
- Codex writes only `codex_space/`
- shared handoff files live in `shared_handoff/`

Published return/trace/receipt artifacts are immutable. New versions use `*_vN` or timestamped files. Latest pointers point to immutable artifacts and include sha256.

Every cross-read must record:
- `source_handle`
- `source_sha256`
- `used_for`
- `changed_judgment`
- `owner_namespace`
- `read_only_assertion`

For fast mutual inspection, read `shared_handoff/90_QUICK_EXCHANGE_BOARD.json` first when it exists. It points to each side's latest summary card and latest artifact with sha256. Use `shared_handoff/99_LATEST_POINTERS.json` for full integrity verification.

## Boundaries

Default status is `HOLD`.

Do not mutate source, authority, current-position, registry, or folder tree. Do not run direct Codex/Gemini API, Hermes direct Gemini, server, replay, or external API lanes unless a separate explicit approved lane exists.

## References

Read only the reference needed for the current route:
- `references/operation_routes.md`
- `references/space_governance.md`
- `references/dual_log_collision_free.md`
- `references/fast_cross_inspection.md`
- `references/integrated_stack.md`
- `references/space_maturation_principle.md`
- `references/program_result_space_effect.md`
- `references/return_schemas.md`
