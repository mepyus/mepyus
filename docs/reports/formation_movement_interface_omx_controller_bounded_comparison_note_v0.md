# Formation-Movement Interface OMX Controller Bounded Comparison Note v0

## 1. status

```yaml
status: bounded_comparison_note
verdict: PASS_WITH_NOTE
source_material: references/git_search/oh-my-codex-main
comparison_target: formation_movement workflow controller
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. purpose

This note compares the OMX workflow/runtime layer against the current Formation-Movement workflow controller.

It does not import OMX.

It asks:

```text
What does OMX reveal about our controller's weak points?
```

especially around:

- staged flow
- artifact passing
- state persistence
- role elevation
- verification return

## 3. source reading

Relevant OMX surfaces:

- `README.md`: OMX as workflow layer for Codex CLI
- `AGENTS.md`: top-level operating contract, role routing, verification discipline
- `src/pipeline/orchestrator.ts`: sequential stage orchestration and persisted state
- `src/pipeline/types.ts`: stage context/result/artifact contracts
- `src/pipeline/stages/ralplan.ts`: planning stage adapter
- `src/pipeline/stages/team-exec.ts`: team execution stage adapter
- `src/pipeline/stages/ralph-verify.ts`: verification stage adapter
- `src/autoresearch/*`: evaluator, candidate, ledger, keep/discard/ambiguous lifecycle
- `skills/ralph/SKILL.md`: persistent completion and verification loop

## 4. our controller baseline

Current Formation-Movement controller flow:

```text
input
→ routing
→ state transition
→ output policy
→ Codex worker-role elevation decision
→ space reread / return
```

Current strong points:

- safe front door
- 4-line card output
- `interpreter/output mode` vs `worker-role elevation`
- no premature execution
- no direct evidence lock for external material

Current weak points:

- route maturity still judgment-heavy
- worker-role elevation timing is not concrete enough
- returned artifacts are conceptually defined but not consistently shaped
- line/lens placement has no default artifact shape

## 5. comparison matrix

| Dimension | OMX | Formation-Movement current state | Reading |
| --- | --- | --- | --- |
| Primary frame | Codex runtime/workflow layer | space-first formation layer around Codex | Similar concern, different center |
| Stage model | explicit stages: ralplan, team-exec, ralph-verify | implicit route/state transitions | OMX is more operationally concrete |
| Artifact passing | `StageContext.artifacts`, per-stage results | validation_return / reread material | Our concept is right, shape is looser |
| State persistence | ModeState, stage index, stage results | notes and space placement | Our flow is less runtime-concrete |
| Worker role | Codex CLI workers through team runtime | bounded worker-role elevation | Strong overlap |
| Verification | ralph verify, evaluator, ledgers | validation_return / hold / refine | Strong conceptual match |
| User surface | role keywords and CLI commands | 4-line card front door | Our user surface is lighter |

## 6. what OMX strengthens

### 6.1 stage transition clarity

OMX makes stages explicit:

```text
ralplan
→ team-exec
→ ralph-verify
```

This helps us see that our controller may need clearer internal stage labels, but not necessarily new object families.

Possible future clarification:

```text
route stage
→ formation stage
→ worker-elevation decision stage
→ return stage
```

Do not patch yet.

### 6.2 artifact passing

OMX passes accumulated artifacts through `StageContext.artifacts`.

Our equivalent is:

```text
validation_return / reread material / space placement
```

This reveals a weakness:

```text
our return artifacts are conceptually clear but shape-light.
```

Possible future clarification:

- every elevated worker-role output should return with a minimal reread artifact
- not a schema, but a shaped return expectation

Do not patch yet.

### 6.3 worker-role elevation

OMX makes worker execution explicit through team runtime.

Our corrected language now says:

```text
Codex interpreter/output mode
→ bounded worker-role elevation
```

OMX strongly supports this distinction.

But OMX is more execution-centered.

Our model must keep formation-first routing.

### 6.4 verification return

Ralph and autoresearch show that execution is not done until verification/evaluator logic runs.

This strongly supports:

```text
validation_return != final
```

It also suggests that our return branch could be made more operational later:

- observed result
- verification/evaluation signal
- next branch
- residue or promotion barrier

Do not patch yet.

## 7. what should not be imported

Do not import:

- OMX command surface
- AGENTS.md contract style
- team runtime as default movement layer
- RALPLAN/team/Ralph sequence as our default pipeline
- `.omx/` state model as our space model

Reason:

OMX centers a runtime/workflow layer around Codex CLI.

Formation-Movement centers a space/formation layer that decides when and how Codex worker roles are elevated.

These are adjacent but not identical.

## 8. likely correction candidates

These are candidates only.

### candidate 1. stage labels inside controller

Potential wording:

```text
route stage
formation read stage
worker-role elevation stage
return/reread stage
```

Why:

- could reduce user/operator confusion
- does not require new object families

Readiness:

```text
not ready for patch
```

### candidate 2. shaped return artifact expectation

Potential wording:

```text
every elevated worker-role output should return as reread material with observed output, contact point, and next branch
```

Why:

- would connect Codex output to space more reliably

Readiness:

```text
emerging patch candidate
```

### candidate 3. worker-role elevation timing note

Potential wording:

```text
elevate only when output shape and return-to-space handling are explicit
```

Why:

- directly targets the current usability bottleneck

Readiness:

```text
patch candidate after one more live case
```

## 9. validation return from this comparison

Observed result:

```text
OMX is a strong comparison frame for making our controller more operational, especially around stage transitions, artifact passing, and verification return.
```

Reread trigger:

```text
If future live cases keep showing unclear worker-role elevation timing or weak output-return shape, use this comparison as support for a clarification patch.
```

Next recommended state:

```text
hold as reusable comparison frame
```

## 10. user-facing 4-line card

```text
현재 판정: 유용한 controller 비교재료
이유: OMX는 stage/artifact/state/verification을 실제 runtime layer로 구체화해서 우리 controller의 약한 지점을 잘 비춰주지만, 그대로 수입할 구조는 아님
다음 이동: worker-role elevation timing과 return artifact shape가 다시 막힐 때 bounded comparison 근거로 재사용
금지선: OMX pipeline 수입 / AGENTS 계약 복사 / baseline 반영 / 즉시 패치 금지
```

## 11. verdict

Overall verdict:

```text
PASS_WITH_NOTE
```

Reason:

- bounded comparison produced useful correction candidates
- no direct import or package mutation occurred
- the strongest next value is not implementation, but clarifying worker-role elevation and return artifact shape after one more live case
