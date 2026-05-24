# VectorFL Vessel Working Standard Candidate v0

## 1. Status

```text
status: working_standard_candidate
authority: sandbox-local / chat-usable
not_authority: baseline, ontology, registry, workflow, schema, AGENTS.md, SKILL.md
source_runs: run_403 through run_410
```

This document consolidates the vessel frame tested across the 05-15 recovery sequence.

It is ready for practical chat use as a context-retrieval and safety frame.
It is not an official VectorFL baseline.

## 2. Core Frame

```text
IIC -> SOF -> RML
```

Optional read-only route view:

```text
MOL
```

Plain language:

```text
IIC reads input pressure.
SOF checks current authority.
RML recovers trace and evidence.
MOL maps route machinery read-only unless explicitly approved.
```

Korean:

```text
IIC는 입력의 압력과 깊이를 읽는다.
SOF는 현재 구조와 권한을 확인한다.
RML은 과거 흔적과 근거를 회수한다.
MOL은 경로와 부품을 read-only로 매핑한다.
```

## 3. The Four Vessels

### 3.1 IIC

```text
name: Intake & Interpretation Cockpit
korean: 인입 및 해석 콕핏
primary question: How should this input be read?
```

Responsibilities:

- complexity probe
- input depth selection
- response mode selection
- STOP mode selection
- layer-shift detection
- authority pressure detection
- wording-to-pressure detection

IIC meanings:

- `gate` = mode/depth selector
- `trace` = reasoning delta / meaning delta
- `pipeline` = pressure signal if the user asks to make a route standing
- `policy` = authority pressure signal
- `memory` = write pressure signal

IIC does not:

- grant permission to execute
- grant permission to promote
- write memory
- create policy
- create automation

IIC selected modes:

```text
plain chat
simple answer
light review
full review
layer-shift
STOP
```

`STOP` means:

```text
The input contains an unauthorized action, promotion, automation,
memory write, policy creation, file mutation, or persistent behavior change.
The assistant may explain why and offer a safe candidate/read-only alternative,
but must not perform the blocked action.
```

### 3.2 SOF

```text
name: Space Operating Frame
korean: 공간 운영 프레임
primary question: Is this allowed in the current space authority?
```

Responsibilities:

- current authority check
- folder/source/reference classification
- promotion boundary check
- baseline/current/sandbox separation
- freeze and locked-surface awareness

SOF meanings:

- `gate` = authority/promotion gate
- `policy` = locked authority surface
- `reference` = classification, not automatic authority
- `baseline` = promotion boundary
- `memory` = write authority boundary

SOF does not:

- accept prior evidence as permission
- treat usefulness as maturity
- treat chat approval as hidden persistent rule
- move files without explicit file-operation approval

### 3.3 MOL

```text
name: Organ & Pipeline Machinery
korean: 기관 및 파이프라인 기구
primary question: What route, organ, script, or component is involved?
```

Responsibilities:

- read-only route mapping
- script/component/organ identification
- handoff path mapping
- execution machinery description

MOL meanings:

- `pipeline` = route machinery
- `trace` = execution path
- `return` = execution output
- `gate` = handoff point, not authority

MOL does not:

- create automation by default
- run scripts unless explicitly requested and allowed
- convert route maps into workflows
- bypass SOF

### 3.4 RML

```text
name: Trace & Memory Spine
korean: 기록 및 기억 중추
primary question: What evidence, trace, receipt, residue, or validation return exists?
```

Responsibilities:

- provenance/evidence recovery
- prior run trace lookup
- receipt/log/history reading
- residue and reflux identification
- validation_return distinction

RML meanings:

- `trace` = provenance / evidence / history
- `return` = validation_return / residue / reflux
- `memory` = provenance spine or memory layer, not automatic write
- `reference` = evidence status

RML does not:

- grant authority
- override SOF
- convert repeated residue into memory
- convert validation_return into completion

RML memory boundary:

```text
runtime/tmp, residue, relay output, raw logs, and validation_return
are evidence or reread material.
They are not core memory by default.
Repeated residue may strengthen a candidate proposal,
but it does not authorize memory write or baseline movement.
```

## 4. Authority Ordering

When vessels conflict:

```text
1. SOF current authority wins.
2. IIC pressure detection determines read mode.
3. RML prior evidence strengthens or weakens confidence.
4. MOL route mapping remains read-only unless approved.
```

Short rule:

```text
RML can strengthen confidence.
RML cannot grant authority.
IIC can pass readability.
IIC cannot grant execution.
MOL can map routes.
MOL cannot automate by default.
SOF decides whether movement is allowed.
```

## 5. Stop Rule

If any vessel returns STOP, the whole request stops.

STOP triggers:

- AGENTS.md update
- SKILL.md creation
- automation script creation
- baseline promotion
- workflow/schema/registry/ontology creation
- current-position update
- output_manifest update
- local core / derived / surface authority change
- official ontology promotion
- file modification without explicit approval
- persistent hidden behavior change
- memory write / core memory update
- policy creation or closeout
- "always use this" / "from now on" / "continue as default"

User relay fact rule:

```text
User-provided facts, summaries, or manual relay from another tool
may be used as input material.
They cannot become authority until SOF checks source status,
current boundary, and whether supporting evidence is required.
```

## 5.1 WATCH / HOLD Definitions

```text
WATCH:
  A visible risk, ambiguity, or drift pressure.
  WATCH does not block the answer by itself.
  It must be named so the user can see what could go wrong.

HOLD:
  A forbidden action, missing authority, or STOP trigger.
  HOLD blocks execution, promotion, file mutation, automation, memory write,
  baseline movement, or hidden persistent behavior change.
```

Examples:

```text
WATCH:
  "pipeline" may drift into automation.
  "trace" may confuse reasoning with evidence.
  "reference" may be mistaken for authority.

HOLD:
  no AGENTS.md update
  no SKILL.md creation
  no automation script
  no baseline promotion
  no memory write
  no docs/specs move
```

## 5.2 Multi-Vessel Handoff Requirement

For multi-vessel or authority-touching requests, use this order:

```text
1. IIC: detect input pressure, complexity, layer shift, and selected mode.
2. SOF: check current authority, folder/source status, and promotion boundary.
3. RML: recover evidence, prior runs, provenance, residue, or validation_return.
4. MOL: map routes/components only if the request needs route visibility.
```

Rule:

```text
IIC may start the handoff.
SOF must run before MOL execution or RML memory/write claims.
RML may support confidence after SOF status is known.
MOL stays read-only unless explicit execution approval and SOF clearance are both present.
```

## 5.3 MOL Approval Boundary

MOL has two modes:

```text
MOL read-only:
  map scripts, routes, organs, handoff points, runner behavior, or component relationships.
  This is allowed when no execution or file mutation is requested.

MOL execution:
  run scripts, create scripts, modify runner behavior, automate a route, or make a route recurring.
  This is blocked unless the user explicitly requests that action and SOF confirms it does not violate current authority.
```

Default:

```text
MOL = read-only.
```

MOL must STOP when the request includes:

```text
자동화해
매번 돌려
스크립트 만들어
runner 수정해
route를 기본값으로 써
pipeline을 official workflow로 만들어
```

## 6. Safe Invocation Phrases

Use these in chat:

```text
IIC complexity probe 해줘.
IIC mode selection 해줘.
SOF authority check 해줘.
SOF reference classification 해줘.
MOL route mapping만 해줘.
MOL component map을 read-only로 보여줘.
RML trace recovery 해줘.
RML provenance receipts 찾아줘.
IIC -> SOF -> RML 순서로 봐줘.
```

Korean-only equivalents:

```text
인입 해석 콕핏으로 먼저 읽어줘.
공간 운영 프레임 기준으로 권한 확인해줘.
기관/파이프라인 기구 기준으로 경로만 매핑해줘.
기록 및 기억 중추에서 흔적을 찾아줘.
입력 판독 -> 권한 확인 -> 흔적 회수 순서로 봐줘.
```

## 7. Dangerous Phrases

These require STOP or full review with SOF:

```text
계속 기준으로 써.
앞으로 기본 판단 루틴으로 써.
공식화해.
반영해.
policy로 닫아.
baseline 후보로 계속 쓰자.
memory에 남겨.
AGENTS.md에 넣어.
SKILL.md로 만들어.
자동화해서 매번 돌려.
current-position 업데이트해.
output_manifest에 반영해.
```

## 8. Bounded Language Rule

```text
하나의 단어는 그릇을 통과할 때마다 해당 그릇의 역할에 맞춰 의미가 재정의된다.
IIC는 독해 깊이를,
SOF는 권한을,
MOL은 경로를,
RML은 증거를 기준으로 같은 단어를 다르게 해석한다.
```

Stronger collision rule:

```text
유창함은 권한을 대체할 수 없다.
다수의 VectorFL 용어가 섞인 문장일수록
IIC-SOF-MOL-RML로 성분 분해를 선행한다.
한 그릇이라도 STOP이면 전체 요청은 정지한다.
```

## 9. 0-9 Family Relationship

The 4 vessels sit above the 0-9 function family frame.

```text
SOF contains:
  0 space_frame
  1 source_basis
  4 authority_gate
  9 promotion_boundary

IIC contains:
  2 input_gate
  3 lens_reader
  4 authority pressure detection

MOL contains:
  5 pipeline_family
  6 organ_component

RML contains:
  7 surface_return
  8 memory_residue
```

The 0-9 frame remains a lower retrieval heuristic.
It is not an ontology.

## 10. Minimal Return Format

When using the vessel frame, return:

```text
selected vessel(s):
selected mode:
IIC reading:
SOF authority:
MOL route status:
RML evidence:
safe answer:
WATCH:
HOLD:
```

If the task is small, use the compact form:

```text
mode:
vessel:
answer:
WATCH:
HOLD:
```

## 11. Current Use Permission

Allowed now:

- use as chat retrieval handle
- use as context filter
- use as reasoning guardrail
- use as manual check sequence
- cite as working standard candidate

Not allowed:

- official baseline use
- hidden persistent behavior update
- AGENTS.md / SKILL.md reflection
- automation
- registry/schema/workflow creation
- file placement change outside sandbox

## 12. Evidence Summary

Test sequence:

```text
run_403: space-wide function family reread
run_404: vessel-based retrieval test
run_405: vessel-to-vessel handoff test
run_406: external lens vessel reread
run_407: bounded language integrity test
run_408: linguistic collision test
run_409: cross-session reflux authority test
run_410: promotion gap analysis
```

Recovered maturity:

```text
ready_for_working_standard_candidate
not_ready_for_provisional_stable_subset
not_ready_for_baseline
```

## 13. Remaining Gaps

- Needs fresh-session verification using this document only.
- Needs a validation report linking runs to criteria.
- MOL read-only boundary should be repeatedly checked.
- No machine-readable manifest exists, and none should be created without explicit approval.

## 14. One-Line Standard Candidate

```text
Use IIC to read input pressure, SOF to check authority, MOL to map routes read-only, and RML to recover evidence; never let evidence, readability, route fluency, or user shorthand override current SOF authority.
```
