# Formation-Movement Interface Single Real Input Pipeline Dry Run v2

## 1. status

```yaml
status: single_real_input_pipeline_dry_run
version: v2_content_inspected
verdict: PASS_WITH_NOTE
input_type: external_material_reference
source_path: references/git_search/oh-my-codex-main
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. input

```text
팀랄프 자료를 우리 공간에서 쓸 수 있게 봐줘
```

Resolved material:

```text
references/git_search/oh-my-codex-main
```

Key inspected files:

- `README.md`
- `AGENTS.md`
- `package.json`
- `src/pipeline/orchestrator.ts`
- `src/pipeline/types.ts`
- `src/pipeline/stages/ralplan.ts`
- `src/pipeline/stages/team-exec.ts`
- `src/pipeline/stages/ralph-verify.ts`
- `src/autoresearch/contracts.ts`
- `src/autoresearch/runtime.ts`
- `skills/ralph/SKILL.md`

## 3. initial route judgment

Route:

```text
external material
```

Reason:

- the user asks to make the material usable inside the space
- the input is not asking for immediate execution
- the source is a local external reference repository
- the right first move is content inspection and space/process placement

Initial path:

```text
external material
→ unclassified seed
→ content inspection
→ space-first line/lens check
→ safe state assignment
→ Codex worker-role elevation decision
→ return-to-space placement
→ user-facing 4-line card
```

## 4. Codex base mode

Base mode:

```text
Codex interpreter/output mode only
```

Meaning:

- Codex reads the repository material
- Codex compares it against existing formation-movement process lines
- Codex produces a compact user-facing judgment
- Codex is not elevated into a bounded worker role at entry

This is the corrected operating distinction:

```text
Codex is active as interpreter and output generator.
Worker-role elevation is conditional.
```

## 5. content reading

## 5.1 README.md

OMX describes itself as:

```text
a workflow layer for OpenAI Codex CLI
```

Strong signals:

- Codex remains the execution engine
- OMX adds task routing, workflow, skills, runtime state, and durable coordination
- canonical workflow: `$deep-interview`, `$ralplan`, `$team`, `$ralph`
- `.omx/` stores plans, logs, memory, and runtime state
- `omx doctor` and real execution smoke tests separate install readiness from actual runtime readiness

Formation-movement reading:

- very strong movement-layer orchestration reference
- strong process staging reference
- strong validation/readiness distinction

## 5.2 AGENTS.md

Strong signals:

- top-level operating contract
- role and skill routing
- delegation rules
- verification-before-completion discipline
- state and runtime marker boundaries
- guidance schema and lifecycle overlays

Formation-movement reading:

- strong B/C/A overlap source
- B: role and surface boundaries
- C: verification and completion gates
- A: order of planning/execution/verification

Important caution:

This file is assertive and contract-like.

It should be used as a comparison source, not imported as our own operating contract.

## 5.3 pipeline orchestrator

Strong signals:

- sequential stage orchestration
- persisted mode state after each transition
- accumulated artifacts passed between stages
- resume support
- explicit stage result statuses

Relevant staged flow:

```text
RALPLAN
→ team-exec
→ ralph-verify
```

Formation-movement reading:

- strong movement-layer pipeline reference
- strong return/artifact accumulation reference
- close to our need for process state and return-to-space artifacts

## 5.4 stage adapters

### ralplan stage

Signals:

- planning artifacts at `.omx/plans/`
- can skip if planning is complete
- produces downstream artifacts

Reading:

- A-heavy: plan before execution
- C-adjacent: planning-complete gate

### team-exec stage

Signals:

- wraps team mode into a pipeline stage
- converts approved plan artifacts into team execution descriptor
- explicitly uses Codex workers through team runtime

Reading:

- movement-layer execution stage
- worker-role elevation model

### ralph-verify stage

Signals:

- wraps persistent verification loop
- consumes execution artifacts
- builds verification descriptor and launch instruction

Reading:

- C-heavy validation/return stage
- strong example of execution result not being final until verification loop runs

## 5.5 autoresearch

Strong signals:

- mission/sandbox contract
- evaluator command and JSON result contract
- candidate artifact
- ledger entries
- keep/discard/ambiguous decisions
- iteration status and run manifest

Formation-movement reading:

- strong validation-return / candidate lifecycle reference
- strong movement-result evaluation structure
- useful for comparison with our `validation_return`, `hold`, `refine`, and residue branches

## 5.6 ralph skill

Strong signals:

- persistence loop until architect-verified completion
- context snapshot before execution
- parallel delegation
- fresh verification evidence
- explicit completion checklist
- cleanup/cancel state management

Formation-movement reading:

- strong C-heavy verification loop
- strong movement-layer completion discipline
- strong warning against premature final claims

## 6. safe state assignment

Initial safe state:

```text
framing_candidate
```

Candidate role:

```text
external Codex workflow/runtime orchestration comparison frame
```

Why it can rise above `reread_priority`:

- the material has concrete implementation surfaces, not only high-level advice
- it includes pipeline stages, persisted state, worker delegation, verification loops, and evaluator contracts
- it directly touches our current concern: making space/Codex workflow actually operate

Why it is not direct evidence:

- it is an external workflow layer with its own assumptions
- it treats Codex as execution engine inside an OMX runtime, while our space is a formation layer around Codex
- importing its contracts would over-collapse our own process into an external architecture

Promotion barrier:

```text
do not adopt OMX workflow, AGENTS.md contract, or Ralph loop as our baseline.
Use as comparison material for process/controller/Codex-coupling design only.
```

## 7. line and lens placement

## 7.1 closest internal lines

### 1. Codex role elevation / movement orchestration line

Reason:

- OMX explicitly separates role keywords, skill workflows, team execution, and persistent verification
- this maps strongly to our need to distinguish interpreter/output mode from bounded worker-role elevation

Strength:

```text
high
```

### 2. prepare / plan / execute / verify pipeline line

Reason:

- RALPLAN → team-exec → ralph-verify is a staged movement pipeline
- this strongly supports process ordering and completion gates

Strength:

```text
high
```

### 3. validation return / completion gate line

Reason:

- Ralph and autoresearch both refuse premature completion
- evaluator results, ledgers, and verification artifacts resemble validation-return objects

Strength:

```text
high
```

### 4. external ingest / comparison-frame line

Reason:

- the material is useful for rereading our own process but is still external
- it should remain comparison material, not direct operating contract

Strength:

```text
medium-high
```

## 7.2 lens reading

Primary lens:

```text
process-first lens
```

Secondary lenses:

- `movement_constraint`
- `validation_gate`
- `boundary_role`
- `return_loop`

Not primary:

- pure B lens
- pure external governance lens
- implementation import lens

## 8. Codex worker-role elevation decision

Decision:

```text
do not elevate Codex into a bounded worker role for this dry run
```

Why elevation is not needed now:

- the user asked to make the material usable in the space
- content-level reading and line/lens placement can be done in interpreter/output mode
- no specific bounded comparison target was requested
- no packet preparation or execution task exists

Possible later elevation:

```text
elevate Codex to bounded comparer
```

only if a follow-up asks:

- compare OMX pipeline to our workflow controller
- compare Ralph verification to our validation_return
- compare autoresearch candidate lifecycle to our provisional object lifecycle

Not appropriate now:

```text
elevate Codex to packet preparer
```

Reason:

- there is no bounded action packet to prepare
- no implementation target is requested

## 9. return-to-space state

Return state:

```text
framing_candidate / reusable comparison object
```

Space placement:

```text
external Codex workflow/runtime orchestration comparison frame
```

Use it for:

- checking whether our workflow controller is still too manual
- comparing staged movement pipelines
- rereading Codex role elevation logic
- strengthening validation-return and completion-gate discussions
- testing how external workflow layers differ from our formation-layer-first model

Do not use it as:

- baseline operating contract
- imported pipeline
- implementation blueprint
- direct evidence that our model is correct

## 10. user-facing 4-line card

```text
현재 판정: 재사용 가능한 비교재료
이유: oh-my-codex는 Codex 위의 workflow/runtime layer로서 plan→team execution→verification, role routing, state persistence를 구체적으로 보여주지만, 우리 공간의 직접 증거는 아님
다음 이동: workflow controller / Codex role elevation / validation_return 장면을 다시 읽을 때 comparison frame으로 사용
금지선: OMX 계약 수입 / baseline 반영 / Codex worker-role 즉시 승격 / 실행 금지
```

## 11. observed friction

What worked:

- the corrected terminology held
- Codex stayed in interpreter/output mode
- actual content moved the object from pending `reread_priority` to `framing_candidate`
- line/lens placement became possible
- worker-role elevation remained unnecessary at entry

Remaining friction:

- the material is rich enough that future bounded comparison will likely be useful
- deciding when to elevate to bounded comparer remains a judgment threshold
- the material may tempt architecture import because it has concrete runtime code and contracts

## 12. verdict

Overall verdict:

```text
PASS_WITH_NOTE
```

Why:

- the default pipeline worked beyond front-door intake
- actual repository content was read
- space/process lines were identified
- Codex operating mode stayed correctly separated from worker-role elevation
- the object can now be placed in space as reusable comparison material

Main note:

- this is stronger than a generic external reference, but still not direct evidence or a baseline candidate.
