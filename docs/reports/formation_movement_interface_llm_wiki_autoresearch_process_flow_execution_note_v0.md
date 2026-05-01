# Formation-Movement Interface LLM-Wiki + Autoresearch Process-Flow Execution Note v0

## 1. status

```yaml
status: process_flow_execution_note
mode: bounded_reread_only
verdict: PASS_WITH_NOTE
package_candidate_support: true
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. source

External material A:

- GeekNews summary:
  `https://news.hada.io/topic?id=28208`
- upstream gist:
  `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`

External material B:

- GitHub:
  `https://github.com/karpathy/autoresearch`

Source note:

- The user phrased the second source as `git_search/autoresearch`.
- This note interprets that as the official GitHub repo `karpathy/autoresearch`, because that is the strongest primary-source match available in GitHub search.

Internal package anchors:

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_process_first_external_material_note_v0.md`
- `docs/reports/formation_movement_interface_codex_oneshot_validation_case_v0.md`
- `docs/reports/formation_movement_interface_external_reference_ingest_validation_case_v0.md`

## 3. why this note exists

This note follows the process-first rule:

```text
외부자료를 먼저 내부 공정 흐름과 기존 line/axis로 읽고,
그 다음에 provisional typing과 merge를 수행한다.
```

So the order here is:

1. internal line / axis check first
2. material A analysis
3. material B analysis
4. merge
5. Codex-style re-analysis of the merge
6. space insertion
7. combined output reread

## 4. step 1: existing internal lines checked first

Before classifying either source, the strongest already-existing internal lines are:

### line 1. formation-layer persistent artifact / ingest-return line

Closest package basis:

- formation layer as identity body
- external ingest handling
- validation-return loop

Core internal question:

```text
입력된 자료가 공간 안에서 누적/숙성/재판독되는 artifact를 만드는가?
```

### line 2. Codex prepare / execution gate line

Closest package basis:

- `prepare_worker_packet != execution`
- boundary / expected return / guardrail / trust_scope

Core internal question:

```text
이 입력은 bounded preparation을 지지하는가, 아니면 실행을 너무 빨리 열게 만드는가?
```

### line 3. validation gate / return loop line

Closest package basis:

- result is not final by default
- return becomes reread material

Core internal question:

```text
산출물이 누적된 판단 자산으로 돌아오는가, 아니면 일회성 결과로 닫히는가?
```

### line 4. schema-guided workflow line

Closest package basis:

- schema / AGENTS-like guidance
- sidecar / process discipline

Core internal question:

```text
agent를 generic chatbot이 아니라 특정 공정을 따르는 운영자처럼 만드는가?
```

## 5. step 2: material A analysis — LLM-Wiki

### raw reading

LLM-Wiki strongly emphasizes:

- raw sources as immutable source of truth
- wiki as LLM-maintained persistent artifact
- schema (`AGENTS.md`-like file) as workflow discipline
- ingest / query / lint as explicit operations
- index/log as navigation and chronology support
- accumulation rather than re-derivation

### first process contact

Strongest first contact:

`formation-layer persistent artifact / ingest-return line`

Why:

- this source is primarily about how material is compiled into a maintained intermediate knowledge layer
- it is much closer to space formation and cumulative reread than to immediate worker execution

### provisional reading

- strongest reading:
  `comparison frame`
- secondary reading:
  `defensive logic`
- not justified:
  `direct evidence`

### local card

```text
현재 판정: strong comparison frame for formation-layer accumulation
이유: raw sources / wiki / schema / ingest-query-lint 구조가 공간의 숙성 artifact 논리를 강하게 비춥니다.
다음 이동: formation-layer line과 validation-return line에 먼저 bounded compare
금지선: 외부 wiki pattern을 package doctrine으로 채택 금지
```

## 6. step 3: material B analysis — autoresearch

### raw reading

Autoresearch strongly emphasizes:

- one bounded file to modify
- fixed metric and fixed time budget
- modify -> train -> check -> keep/discard loop
- `program.md` as lightweight agent instruction file
- preparation/setup before autonomous loop
- explicit iteration under constrained execution

### first process contact

Strongest first contact:

`Codex prepare / execution gate line`

Why:

- this source is primarily about bounded autonomous execution under explicit constraints
- it is not mostly about accumulation of a knowledge artifact
- it is mostly about when and how a loop may move

### provisional reading

- strongest reading:
  `defensive logic`
- secondary reading:
  `comparison frame`
- not justified:
  `direct evidence`

### local card

```text
현재 판정: strong defensive logic for bounded execution loops
이유: fixed metric, fixed budget, one-file scope, keep/discard loop이 무제한 실행이 아니라 constrained movement를 강하게 지지합니다.
다음 이동: Codex prepare / validation gate line에 bounded compare
금지선: 외부 research loop를 그대로 package execution doctrine으로 채택 금지
```

## 7. step 4: merge

### why merge is valid

The two materials are not the same kind of source, but they are complementary:

- `LLM-Wiki`:
  strong on formation-layer compilation, persistent artifact, ingest/query/lint
- `autoresearch`:
  strong on movement-layer constraint, verification metric, bounded autonomous iteration

Together they produce a stronger cross-layer object:

```text
schema-guided compiled artifact + constrained iteration workflow cluster
```

### merged provisional type

`framing_candidate`

Reason:

- enough role clarity to become reusable
- still too external to become direct evidence
- best used as bounded process-compare object

### merged candidate_role

`formation-to-movement workflow comparison cluster`

### merged promotion_barrier

- no internal repeated explanatory / relocation force has yet been demonstrated
- the merged object supports both formation and movement logic from outside
- importing its workflow directly would prematurely collapse the package into external process doctrine

## 8. step 5: Codex re-analysis of the merge

If Codex rereads the merged object through the package, the result is:

### what becomes clearer

- not all external material should enter at the same stage
- some sources first clarify formation-layer accumulation
- some sources first clarify movement-layer gating
- schema-guided agent behavior can sit across both layers

### aggregate split

- `direct evidence`:
  not supported
- `defensive logic`:
  strong
- `comparison frame`:
  strong

### A/B/C/T/X/R/L contact

- `A`:
  strong via prior structure, schema, and ordered stages
- `B`:
  moderate via bounded roles, one-file scope, architecture-like separation of mutable vs immutable layers
- `C`:
  strong via metric, check, lint, keep/discard, validation posture
- `T/X/R/L`:
  touched indirectly, but not central

Compressed reread:

```text
이 merged object는 A/C가 강하고 B가 보조적으로 붙는 process cluster다.
```

## 9. step 6: space insertion

This merged object should enter the space as:

```text
formation-to-movement workflow comparison cluster
→ framing_candidate
→ compare_only
→ reusable reread-support object
```

It should not enter as:

- package doctrine
- baseline workflow
- direct evidence for A/B/C
- execution recipe

## 10. step 7: combined output reread

### what line/axis does it reinforce most?

Current ranking:

1. formation-layer persistent artifact / ingest-return line
2. Codex prepare / execution gate line
3. validation gate / return loop line
4. schema-guided workflow line

### what camera/lens reads it best?

Best lens:

`process-first lens`

Why:

- the value of the merge is not primarily in ontology naming
- the value is in showing how external material can be routed through existing internal process lines before any stronger classification

Secondary lens:

`A/C-heavy governance lens`

### what healthy output does this suggest?

```text
외부자료는 먼저
1) formation-side accumulation source인지
2) movement-side bounded loop source인지
를 보고,
그 다음 merge와 space insertion을 결정하는 것이 건강하다.
```

## 11. practical 4-line card

If similar external material arrives later, the safest default response is:

```text
현재 판정: 기존 formation/movement process line에 먼저 태워볼 수 있는 framing candidate
이유: 외부자료의 역할은 바로 축 확정이 아니라, 이미 있는 공정 line에서 어떤 단계와 닿는지 먼저 보는 데 있습니다.
다음 이동: formation-side 또는 movement-side 첫 접점을 먼저 선택해 bounded compare
금지선: direct evidence lock, workflow import, baseline 반영 금지
```

## 12. verdict

`PASS_WITH_NOTE`

Reason:

- the package can execute the requested process flow in order
- the two materials do not collapse into one shallow governance blob
- instead they separate into formation-side and movement-side strengths before merge
- the note is that this merged cluster is still external support, not internal proof

## 13. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- any existing validation case
- Core 7
- object family 5종
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 14. unresolved questions

- after repeated use, does the merged cluster remain A/C-heavy or does B become stronger through boundary rereads?
- should schema-guided workflow be promoted to its own reusable internal line later, or remain a cross-line reading?
- how often should external sources be split into formation-first vs movement-first before merge becomes justified?
