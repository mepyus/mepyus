# VECTORFL_PERSONAL_PROGRAM_UNIT_CONTRACT_20260523_V0

status: STAGE1_PERSONAL_PROGRAM_UNIT_CONTRACT_WITH_HOLD
date: 2026-05-23

## Verdict

VECTORFL_PERSONAL_PROGRAM_UNIT_CONTRACT_READY_FOR_BOUNDED_BUILDUP_WITH_HOLD

## Contract Object

Name:

```text
VECTORFL_PERSONAL_LOCAL_PROGRAM_UNIT_V0
```

Purpose:

```text
Let one user repeatedly turn personal inputs into local evidence,
reviewable receipts, and bounded next actions without losing provenance
or accidentally promoting candidate material into authority.
```

## Included In Stage 1

Stage 1 includes:

1. local-only operation
2. personal input intake
3. input classification and placement
4. boundary/authority check
5. local persistence
6. receipt generation
7. HOLD review state
8. read-only review surface
9. deterministic validation
10. explicit re-entry handoff for Codex/Gemini/Hermes

## Excluded From Stage 1

Stage 1 excludes:

- public product readiness
- Program Alpha readiness
- authority mutation
- promotion
- M3/M4 confirmation
- reusable internal module claim
- router implementation
- runner.py implementation
- model/API/network connector
- external execution dependency
- multi-user auth
- write-capable Web UI
- automatic baseline mutation

## Minimal Functional Spine

The Stage 1 personal program unit spine is:

```text
User Input
-> Source Type / Lens / Boundary
-> Local Request
-> Decision
-> Execution Record
-> Receipt
-> Review HOLD
-> Maturation Candidate / Next Action
-> Read-only Review Surface
-> Deterministic Replay
```

## Mapping To Existing Assets

### Input Semantics

Use candidate semantics from 05-22 Input Localization:

```text
Any Input
-> Source Type
-> Camera / Lens
-> Boundary / Authority Check
-> Valid For / Not Valid For
-> Placement / Routing
-> Receipt
-> Re-entry Compression
-> Space Maturation Candidate
```

Status:

```text
CANDIDATE_MATERIAL_WITH_HOLD
```

### Persistence / Evidence Loop

Use Phase 0.5 local loop:

```text
app/work/vectorfl_ops_phase_0_5/
```

Status:

```text
LOCAL_EVIDENCE_LOOP_PROTOTYPE_WITH_HOLD
```

### Review Surface

Use Phase 1 read-only Web/API skeleton:

```text
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/
```

Status:

```text
READ_ONLY_LOCAL_WEB_MVP_SKELETON_STABILIZED_WITH_HOLD
```

### Runtime / Fragment Baseline

Keep core runtime baseline as adjacent material, not the first integration target:

```text
CURRENT.md
app/runtime/
runtime/
```

Status:

```text
RUNTIME_BASELINE_ADJACENT_NOT_YET_STAGE1_INTEGRATED
```

Reason:

The fragment runtime is important, but Stage 1 personal program unit should first stabilize the personal operating loop before deep runtime integration.

## Minimum Data Contract

The smallest Stage 1 personal intake must preserve:

- title
- body
- source_type
- lens
- boundary_level
- valid_for
- not_valid_for
- placement_candidate
- authority_status
- promotion_status
- receipt content
- review verdict
- next smallest action

Required default values:

```text
authority_status=NO
promotion_status=HOLD
external_execution=NO
real_company_data=NO
program_alpha_evidence=NO
```

## First Implementation Candidate

Name:

```text
personal_intake_min.py
```

Target directory:

```text
app/work/vectorfl_ops_phase_0_5/tools/
```

Allowed behavior:

- accept local CLI arguments or JSON input
- validate required fields
- insert one request into SQLite
- insert one decision
- insert one execution record marked local/no-model
- insert one receipt
- insert one review with HOLD
- insert one maturation candidate with authority mutation NO
- write markdown receipt/export

Forbidden behavior:

- network access
- model/API invocation
- router/runner claim
- authority mutation
- promotion
- schema mutation unless separately approved
- v1 snapshot creation

## First Test Contract

The first implementation must include:

1. fixture DB test
2. live DB no-op test unless explicitly running live intake
3. required HOLD fields test
4. receipt file creation test
5. Phase 1 read-only API still PASS after fixture test
6. live-safety PASS after any approved live intake

## Tool Role Contract

### Codex

Role:

```text
structural design, boundary definition, code review, small local patches when safe
```

Codex should:

- keep Stage 1 contract honest
- classify candidate vs implementation
- write bounded packets
- verify tests
- prevent promotion drift

### Gemini

Role:

```text
broad internal exploration and gap scan
```

Gemini should:

- scan 05-* Obsidian assets
- map terms to UI/program labels
- find missing negative guard cases
- identify conflicts between Hermes outputs and repo implementation

Gemini must not:

- authorize promotion
- claim implementation
- mutate authority

### Hermes

Role:

```text
bounded execution only
```

Hermes should:

- apply minimal patches from packets
- run local tests
- produce receipts

Hermes must not:

- expand scope
- call external connectors
- mutate authority
- promote candidate material

## Stage 1 Readiness Gates

### Gate 1. Contract Ready

Current status:

```text
PASS_CONTRACT_READY_WITH_HOLD
```

### Gate 2. Stable Existing Base

Current status:

```text
PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD
PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD
```

### Gate 3. Minimal Personal Intake

Current status:

```text
PASS_PERSONAL_INTAKE_MIN_IMPLEMENTED_AND_FIXTURE_TESTED_WITH_HOLD
```

Receipt:

```text
app/work/CODEX_REVIEW_PERSONAL_INTAKE_MIN_IMPLEMENTATION_20260523_V0.md
```

### Gate 4. Intake Receipt Replay

Current status:

```text
PARTIAL_FIXTURE_RECEIPT_CREATED_BY_TESTS__LIVE_REPLAY_NOT_APPROVED
```

### Gate 5. Read-only Personal Review Surface

Current status:

```text
PARTIAL_EXISTS_AS_PHASE1_READ_ONLY_WEB_MVP
```

## Recommended Next Build Step

Prepare this packet:

```text
app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_personal_intake_minimal_cli_packet_20260523_v0.md
```

Packet goal:

```text
Implement and test personal_intake_min.py against a fixture DB first.
```

Current status:

```text
IMPLEMENTED_AND_FIXTURE_TESTED_BY_CODEX_WITH_HOLD
```

Do not run live DB intake until the user approves live evidence mutation.

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- v1 snapshot creation: HOLD unless explicitly approved
- write UI: NO
- production readiness: NO

## One-Line Contract

```text
Stage 1 VectorFL is a local personal evidence-and-receipt program, not yet an autonomous router, runner, promoted module, or production app.
```
