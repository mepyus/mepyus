# VectorFL Flow-Network Attachment Model v0

## 1. Verdict

```text
VECTORFL_FLOW_NETWORK_ATTACHMENT_MODEL_DRAFTED_WITH_WATCH
```

## 2. Status

```text
status: working_model_candidate
scope: 05-15 / Hermes / external-tool attachment / selective recovery framing
authority: sandbox-local candidate
```

This is not:

```text
ontology
registry
workflow
schema
baseline
automation
AGENTS.md
SKILL.md
current-position
output_manifest
```

## 3. Purpose

This model exists to connect VectorFL to external execution tools like Hermes without confusing execution with recovery or promotion.

Core sentence:

```text
VectorFL is a judgment reservoir / traffic-control layer for external tool outputs.
Hermes is a native execution harness.
The attachment model defines how tasks move, how they are observed, how outputs return, and how promotion is gated.
```

Current recovered position:

```text
05-15 bundle:
  input depth / response mode selector candidate
  +
  external-tool selective recovery frame

Hermes:
  native execution harness

VectorFL:
  selective recovery / promotion gate

Diff-audit rule set:
  strong candidate

Component:
  HOLD
```

## 4. Core Model

```text
Hermes executes.
VectorFL recovers selectively.
Codex translates outputs into recovery classes.
Gemini matures/checks candidate boundaries.
User approves side effects and promotions.
```

Critical separations:

```text
Hermes execution permission != VectorFL recovery permission
Hermes side effect approval != VectorFL promotion approval
Hermes memory != VectorFL memory
Hermes skill != VectorFL SKILL.md
Hermes cron != VectorFL workflow
Hermes successful run != VectorFL approval
```

## 5. Metaphor Mapping

The metaphors are working lenses.

They are not schema.
They are not ontology.
They are not registry entries.

### 5.1 Traffic Network

Traffic network lens explains:

```text
trace
provenance
route
flow
actor
vehicle identity
permissioned roads
intersections
detours
checkpoints
```

Use it when asking:

```text
Where did this task enter?
Which lane did it take?
Which tool carried it?
What did it bring back?
Where did it stop?
What evidence proves the route?
```

### 5.2 Electric Grid

Electric grid lens explains:

```text
load
capacity
transformation
breaker
overload
safe distribution
```

Use it when asking:

```text
Is this input too heavy for plain chat?
Should it go to Gemini, Hermes, Codex, or STOP?
Is a capability being connected directly to authority?
Where should load be transformed before use?
```

### 5.3 Factory Pipeline

Factory pipeline lens explains:

```text
local domain-specific processing sequence
```

Use it for bounded lanes:

```text
diff fixture -> audit script -> report/receipt
customer message -> draft-for-review -> receipt
research input -> brief -> residue/candidate
```

Limit:

```text
A factory pipe explains one lane.
It does not explain the whole road/grid network.
```

## 6. LACL as Intersection CCTV

A single LACL does not know the whole truth.

It observes a flow at one judgment intersection.

```text
intersection:
  judgment split point

CCTV:
  LACL observation

vehicle:
  task / material / output / artifact

license plate:
  provenance / packet id / run id

driver:
  executing agent: User / ChatGPT / Codex / Hermes / Gemini

cargo:
  content / report / receipt / artifact / candidate

traffic control:
  VectorFL selective recovery and promotion gate
```

Key rule:

```text
A single LACL observes one intersection.
Connected LACL observations can recover route, provenance, flow, and pattern.
Route recovery still does not create authority.
```

LACL can help ask:

```text
Is this execution, review, recovery, proposal, promotion, or STOP pressure?
Is this receipt, residue, candidate, component, or space_update_proposal?
Is the surface request hiding a layer-shift?
```

## 7. Sync with IIC / SOF / RML / MOL

Existing Vessel Working Standard maps into the flow network:

```text
IIC:
  entry interpretation / intake control
  "What is this vehicle and where is it trying to go?"

SOF:
  permission / law / authority boundary
  "Is this route/action allowed?"

RML:
  trace / memory spine / CCTV record
  "Where did it come from, what evidence exists, what residue remains?"

MOL:
  route / machinery / pipeline organs
  "Which lane/tool/path should carry it?"
```

Key hierarchy:

```text
IIC reading does not create permission.
MOL route availability does not create approval.
RML trace does not create memory promotion.
Execution success does not create VectorFL approval.
```

Expanded separation:

```text
tool exposure != tool invocation approval
delivery != recovery
persistence != memory
receipt != authority
candidate != component
component != workflow
```

## 8. External Tool Attachment Pipeline

Large attachment pipeline:

```text
User purpose
  ->
IIC input/mode reading
  ->
SOF permission check
  ->
MOL tool/lane selection
  ->
Packet Builder
  ->
Hermes native execution / Codex / Gemini / other external lane
  ->
Report + Receipt return
  ->
Codex recovery classification
  ->
VectorFL recovery gate
  ->
Gemini maturation if needed
  ->
User promotion decision
```

This is a flow-network, not one pipe.

Different lanes can carry different vehicle types:

```text
Hermes:
  native execution / local or external work

Codex:
  workspace reading, editing when approved, recovery translation

Gemini:
  broad lens, maturation, threshold review, comparison

ChatGPT/User:
  intent, judgment, side-effect approval, promotion approval
```

## 9. Packet Builder

Packet Builder is:

```text
vehicle manifest
travel permit
recovery contract
```

It must define:

```text
purpose
input/cargo
allowed routes/actions
forbidden routes/actions
permission surface
persistence boundary
expected output
receipt format
recovery expectation
STOP / HOLD conditions
```

Without packet boundaries, external execution can drift into:

```text
unbounded search
external side effects
memory writes
skill creation
cron creation
source mutation
VectorFL authority mutation
```

## 10. Gate Stack

Every external-tool run should be split through gates.

```text
Action Permission:
  May Hermes/tool do this action?

External Side Effect Permission:
  Does it affect external systems?

Persistence Permission:
  What remains locally or inside Hermes/tool state?

VectorFL Recovery Permission:
  How does VectorFL receive the result?
```

Also include:

```text
Promotion Gate:
  Can candidate become component?
  Can component become adapter?
  Can adapter become official structure?
```

Promotion gate is separate from successful execution:

```text
successful run -> receipt
repeated pattern -> residue/candidate
stable maintained bounded part -> possible component
explicit approval -> possible promotion
```

## 11. Recovery Classes

```text
discard
receipt
residue
candidate
component
space_update_proposal
STOP
external_action_approval_required
```

Traffic/cargo mapping:

```text
discard:
  packaging or one-off cargo with no retained value

receipt:
  passage evidence / delivery proof

residue:
  repeated trace or meaningful leftover

candidate:
  possible reusable route/rule

component:
  maintained bounded reusable part

space_update_proposal:
  proposed change to the traffic/control system

STOP:
  unauthorized mutation / dangerous cargo / authority breach

external_action_approval_required:
  vehicle can move technically, but destination affects external systems
```

## 12. Hermes Lane

Hermes is:

```text
native execution harness
work vehicle
automation-capable lane
```

It should not be over-restricted into a passive reader.

Hermes value includes:

```text
terminal
file
browser
MCP
memory
skill
cron
messaging
automation
external app connection
```

But Hermes outputs are not VectorFL authority:

```text
Hermes output != VectorFL authority
Hermes memory != VectorFL memory
Hermes skill != VectorFL SKILL.md
Hermes cron != VectorFL workflow
Hermes report != VectorFL baseline
Hermes success = receipt, not approval
```

The attachment model should let Hermes act natively while preserving:

```text
action permission
external side-effect permission
persistence permission
VectorFL recovery permission
promotion gate
```

## 13. Diff-Audit as First Validated Lane

Diff-audit is the first Stage 1 local lane pressure test.

It validated:

```text
Hermes native execution
persistence boundary
report/receipt contract
VectorFL selective recovery
candidate rule refinement
Codex/Hermes independent replay
Gemini readiness check
current tracked worktree pressure
```

It did not validate:

```text
component promotion
workflow
skill
baseline
authority update
security assurance
runtime reachability
full repository safety
```

Current diff-audit state:

```text
DIFF_AUDIT_CONFIRMED_STRONG_CANDIDATE_COMPONENT_HOLD_ON_IMPLEMENTATION_BOUNDARY
```

Meaning:

```text
diff-audit is a proven test road segment.
It is not the national road network.
It is not the center of VectorFL.
```

## 14. Existing Asset Synchronization

05-15 mode selector:

```text
role:
  IIC / entry reading / input depth selector

status:
  sandbox-local candidate
```

Hermes recovery ladder:

```text
role:
  SOF / permission ladder / external execution lane boundary

status:
  candidate operating map, not authority
```

Recovery classification tests:

```text
role:
  RML / return classification / cargo checkpoint

status:
  candidate classification evidence
```

Diff-audit tests:

```text
role:
  MOL test lane + report/receipt contract pressure test

status:
  strong candidate, component HOLD
```

Gemini readiness review:

```text
role:
  maturation lens / independent threshold review

status:
  confirmed strong candidate, component HOLD
```

## 15. WATCH

```text
traffic/grid metaphor becoming ontology
flow model becoming registry/schema/workflow
diff-audit becoming the center
Hermes output becoming authority
Hermes success becoming approval
candidate becoming component too early
component becoming workflow/skill/baseline
small tests driving the vessel
external tool capability becoming permission
repeated run becoming baseline
packet builder becoming automation
recovery classes becoming policy without approval
```

## 16. HOLD

```text
component promotion
workflow creation
skill creation
baseline promotion
schema/registry/ontology creation
automation
AGENTS.md update
SKILL.md creation
current-position update
output_manifest update
VectorFL authority mutation
Hermes memory/skill/cron/config promotion
```

## 17. Next Smallest Action

Do not promote.

Next valid action:

```text
review maintained implementation boundary for diff-audit as a future component candidate
```

This remains:

```text
review only
no implementation
no component packaging
no promotion
```
