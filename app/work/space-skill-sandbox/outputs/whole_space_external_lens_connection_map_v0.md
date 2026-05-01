# Whole-Space External Lens Connection Map v0

## Status

- status: connection map candidate
- baseline: false
- source_space_law: false
- automation: false
- schema: false
- controller: false

This map connects external lens materials, internal philosophy / baseline records, sandbox operating principles, and recent process-memory rules.

It is a connection aid, not a new authority layer.

## 1. Why This Exists

The project is building a space that handles:

```text
line
axis
connection
reread
hold
reflux
process memory
```

But the current working records had become locally connected around sandbox runs while the broader internal/external lens structure was not explicit enough.

This map fixes that by connecting:

```text
external lens set
-> internal philosophy / baseline
-> sandbox 15 principles
-> package-loop lessons
-> process-memory operating rules
-> whole-space handoff checklist
```

## 2. External Lens Source Sets

### Set A. Run 029 Operating Order Source Set

Source map:

- `app/work/space-skill-sandbox/outputs/operating_order_source_map_v0.md`

Sources:

```text
S1 Agent Harness Engineering
S2 Tools Live Beyond Their Maker
S3 Warp
S4 Browser Harness
S5 mini-swe-agent
S6 Graphify
S7 AWS sample-deep-insight
S8 Laws of Software Engineering
```

Role:

```text
generated sandbox 15 operating principles as audit lenses
```

### Set B. Package 001 External Lens Reread

Sources:

```text
Agent Harness Engineering
Tools Live Beyond Their Maker
mini-swe-agent
```

Core lessons:

```text
failure -> package-level signal, not session annoyance
caller shift -> affordance / forbidden-use surface
small stateless execution unit + linear trace -> cheaper validation
```

### Set C. External Material Synthesis Round 001

Sources:

```text
Fowler fragment
Skillify
GStack
Google Cloud Agent Governance Stack
Agentic patterns / harness evolution
```

Common pressure:

```text
AI worker value increases when the process around the worker becomes explicit.
AI worker risk increases when that process becomes invisible automation.
```

Needed surface:

```text
identity
context
permission
validation
routing
risk
next action
```

## 3. Internal Philosophy / Baseline Anchors

### Space First / LLM Last

Anchor:

- `docs/specs/space_first_llm_last_principle_v0.md`

Connection:

```text
external worker/harness materials must not become meaning sources.
LLM and agent outputs are late-stage worker returns, not primary space meaning.
```

### Open Interpretation Space

Anchor:

- `docs/specs/open_interpretation_space_operating_principles_v1.md`

Connection:

```text
failure / weak / fallback / hold remain future comparison memory.
external lens signals should not close interpretation too early.
```

### Current Layer Baseline Contract

Anchor:

- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

Connection:

```text
mixed hold is productive hold corridor.
re-entry does not equal canonical promotion.
observer-only specificity must not become core truth.
```

### Engine Input Lane Baseline

Anchor:

- `docs/policies/engine_input_lane_baseline_v1.md`

Connection:

```text
external material is an intake lane, not core promotion.
source first, summary later.
input acceptance and structural promotion are separate.
```

### Three-Axis Operating Loop

Anchor:

- `docs/specs/space_three_axis_operating_loop_and_material_intake_spec_v0.md`

Connection:

```text
material intake -> construction -> line reading -> human-language reread -> line inspection -> next construction
```

External materials should enter this loop as reread material, not doctrine.

### Engine Memory Spine

Anchor:

- `docs/specs/engine_memory_spine_and_context_externalization_v1.md`

Connection:

```text
memory belongs to layers:
directionality / user problem recognition / resource boundary / feedback / episodic / current reality
```

Process memory should be placed into the right memory layer rather than one giant folder.

## 4. Sandbox 15 Principles Connection

Source:

- `app/work/space-skill-sandbox/outputs/operating_order_principles_v0.md`
- `app/work/space-skill-sandbox/outputs/operating_order_source_map_v0.md`

The 15 principles are connected as audit lenses:

```text
Model보다 Harness
Function보다 Affordance
Skill보다 Route
Core보다 Workspace
Conversation보다 Agent-readable Context
Error보다 Signal
Graph보다 Provenance
Readiness와 Promotion 분리
User as Judge
Program as Material
Plan before Execution
Metadata before Full Context
Definition before Prompt
File before Chat
Ops Trace before Memory Loss
```

Placement:

```text
sandbox audit lens
package/run review lens
worker overreach detector
promotion barrier
not source-space law
```

## 5. Crosswalk

| External Pressure | Internal Anchor | Sandbox Principle | Process-Memory Translation |
| --- | --- | --- | --- |
| Agent Harness Engineering: harness before raw model power | Space First / LLM Last; A/B/C A-layer | Model보다 Harness; Plan before Execution | structure before worker action |
| Tools Live Beyond Their Maker: caller shift | Engine Input Lane; Program as Material | Function보다 Affordance; Definition before Prompt | handoff must state caller, capability, forbidden use |
| Warp: workspace / terminal as operating surface | Three-surface / file context | File before Chat; Agent-readable Context | durable file entry before chat memory |
| Browser Harness: environment boundary | Current Layer Baseline; Core/Workspace split | Core보다 Workspace; Model보다 Harness | worker execution belongs in bounded surface |
| mini-swe-agent: small loop / linear trace | Engine Memory Spine; process memory | Metadata before Full Context; Skill보다 Route | small stateless execution unit, trace before interpretation |
| Graphify: graph temptation | Open Interpretation Space | Graph보다 Provenance | provenance before graph / ontology |
| AWS sample-deep-insight: planner / supervisor / HITL / ops trace | Role routing; User approval | User as Judge; Readiness와 Promotion 분리; Ops Trace before Memory Loss | role-aware handoff, user gate, trace preservation |
| Laws of Software Engineering: failure as signal | Current Layer hold / failure memory | Error보다 Signal | failure-to-pipeline, not deletion |
| Fowler: verification and intent are scarce | Space First / LLM Last | User as Judge; Readiness와 Promotion 분리 | confident prose needs evidence boundary |
| Skillify: recurring failures become durable structures | Open Interpretation; process memory | Error보다 Signal; Skill보다 Route | failure -> guide candidate/check case before automation |
| GStack: visible workflow stages | Three-surface reading | Plan before Execution; File before Chat | stage/role/return visibility |
| Google Cloud governance: identity / access / monitoring | Engine Memory Spine; role boundary | User as Judge; Ops Trace before Memory Loss | lightweight posture card before governance stack |
| Harness evolution: rigor moves from prompt to context to harness | A/B/C hierarchy | Model보다 Harness; Agent-readable Context | make rigor location visible before building machinery |

## 6. What This Means For Whole-Space Handoff

A whole-space handoff checklist must include:

```text
identity:
context:
permission:
validation:
routing:
risk:
next:
source_refs:
allowed_actions:
forbidden_actions:
authority_status:
memory_layer:
```

This extends the current entry-surface checklist.

## 7. Non-Promotion Boundaries

Do not:

- treat external materials as authority
- treat sandbox 15 principles as source-space law
- install mini-swe-agent, AWS stack, Graphify, or any external tool from this map
- create automation / schema / controller / graph / ontology
- collapse whole-space philosophy into sandbox package bookkeeping
- promote process-memory rules without repeated use and ChatGPT/User validation

## 8. Next Structural Move

Create `whole_space_handoff_checklist_v1` by adding the external-lens crosswalk fields:

```text
identity / context / permission / validation / routing / risk / next
source_refs / allowed_actions / forbidden_actions / authority_status / memory_layer
```

Then send v1 to ChatGPT for structural validation.

