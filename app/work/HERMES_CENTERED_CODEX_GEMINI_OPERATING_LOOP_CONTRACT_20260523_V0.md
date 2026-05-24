# HERMES_CENTERED_CODEX_GEMINI_OPERATING_LOOP_CONTRACT_20260523_V0

status: HERMES_CENTERED_OPERATING_CONTRACT_WITH_HOLD
date: 2026-05-23

## Verdict

HERMES_CAN_BE_MAIN_PLAYGROUND_IF_SPACE_REENTRY_AND_AUTHORITY_GUARDS_ARE_MAINTAINED

## Purpose

Move the main execution playground to Hermes while preserving VectorFL boundaries.

Hermes may orchestrate local commands and bounded Codex/Gemini calls, but Hermes does not become an authority source.

## Operating Model

Recommended model:

```text
User
-> Hermes main playground
   -> local tests / scripts / receipts
   -> Gemini broad scan packets
   -> Codex review-only packets
-> shared space receipts/status cards
-> Codex final structural review when needed
```

Role split:

```text
Hermes = execution orchestrator / bounded runner / receipt producer
Codex = structure, contract, review, overclaim guard
Gemini = broad internal exploration, asset archaeology, gap scan
Shared space = memory / source of truth / re-entry surface
```

## Why Hermes As Main Playground

Hermes is better as the main playground when the work requires:

- repeated local command execution
- test loops
- receipt creation
- bounded file materialization
- invoking Codex/Gemini from scripts
- keeping execution outputs in one run folder

Codex remains better for:

- contract design
- boundary classification
- deciding candidate vs implementation vs STOP
- reviewing Hermes/Gemini returns
- preventing authority/promotion drift

Gemini remains better for:

- reading large 05-* Obsidian surfaces
- broad gap scans
- repeated pattern extraction
- finding missing guard cases

## Non-Negotiable Boundary

No tool output automatically creates authority.

Even if Hermes executes Codex/Gemini:

```text
Hermes output = execution receipt evidence
Codex output = review-only structural evidence
Gemini output = exploration/candidate evidence
```

None of these automatically mean:

- promotion
- authority mutation
- M3/M4 confirmation
- Program Alpha readiness
- router implementation
- runner.py implementation
- baseline/schema/registry mutation

## Shared Space Rule

Each tool must re-enter by reading the shared space.

Do not rely on private tool memory as the source of truth.

Required first reads for every Hermes-centered run:

```text
app/work/VECTORFL_PROGRAM_SPINE_STATUS_CARD_20260523_V0.md
app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_POSITION_AND_BUILDUP_20260523_V0.md
app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_CONTRACT_20260523_V0.md
app/work/HERMES_CENTERED_EXECUTION_WORKLIST_20260523_V0.md
app/work/TOOL_SPACE_REENTRY_INSTRUCTION_20260523_V0.md
```

Task-specific reads:

```text
app/work/vectorfl_ops_phase_0_5/
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/
app/work/space-skill-sandbox/relay/packets/
```

Obsidian reads when relevant:

```text
/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/
/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-22/
```

## Hermes Run Shape

Each Hermes run should create or update a run receipt under:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/
```

Recommended run folder:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/run_YYYYMMDD_<short_task_id>/
```

Required files:

```text
run_brief.md
commands_run.md
tool_calls.md
outputs_summary.md
receipt.md
```

Optional files:

```text
codex_review_return.md
gemini_gap_scan_return.md
local_test_output.md
watch_items.md
```

## Hermes May Invoke Codex

Allowed Codex invocation types:

- review-only packet
- contract consistency check
- overclaim audit
- next-smallest-action recommendation

Codex invocation must include:

- required shared-space read list
- exact scope
- explicit HOLD language
- forbidden claims
- required return shape

Codex invocation must not:

- silently approve authority mutation
- silently approve promotion
- create M3/M4 confirmation
- claim router/runner implementation

## Hermes May Invoke Gemini

Allowed Gemini invocation types:

- broad internal folder scan
- 05-* asset archaeology
- gap scan
- missing negative guard discovery
- terminology/user-surface mapping

Gemini invocation must include:

- read list
- bounded questions
- required classification labels
- explicit non-implementation boundary

Gemini invocation must not:

- mutate repo or Obsidian files
- authorize implementation
- promote candidate material
- claim M3/M4

## Hermes Local Execution Rules

Hermes may execute:

- tests
- validators
- fixture-only commands
- bounded scripts already approved by packet
- receipt generation

Hermes must stop or ask before:

- live DB mutation
- snapshot creation
- schema mutation
- baseline/registry mutation
- network/API/model connector expansion
- write UI implementation
- deleting or rewriting prior evidence

## Current Stage 1 Work Context

Current target:

```text
VECTORFL_PERSONAL_LOCAL_PROGRAM_UNIT_V0
```

Current stage:

```text
minimal personal intake implemented and fixture-tested with HOLD
```

Current verified receipts:

```text
app/work/CODEX_REVIEW_PERSONAL_INTAKE_MIN_IMPLEMENTATION_20260523_V0.md
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md
app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_v1_preflight_receipt.md
```

## Recommended Main Loop

For each task:

```text
1. Hermes reads shared status/contract/re-entry docs.
2. Hermes chooses exact packet/worklist item.
3. Hermes executes local commands or invokes Gemini/Codex.
4. Hermes writes receipt and command log.
5. Codex reviews receipt if structural judgment is needed.
6. Status card is updated only with evidence-backed statements.
```

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO unless separately packeted
- live DB mutation: HOLD unless explicitly approved
- v1 snapshot creation: HOLD unless explicitly approved
- write UI: NO unless separately contracted

## One-Line Contract

```text
Hermes may become the main execution playground, but shared space remains memory and Codex remains the structural guard.
```
