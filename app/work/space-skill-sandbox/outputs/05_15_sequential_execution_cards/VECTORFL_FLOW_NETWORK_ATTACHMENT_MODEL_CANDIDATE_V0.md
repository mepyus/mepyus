# VectorFL Flow-Network Attachment Model Candidate v0

## 1. Status

```text
status: working_model_candidate
scope: sandbox-local / chat-usable / external-tool attachment framing
not_authority: ontology, registry, workflow, schema, baseline, automation, AGENTS.md, SKILL.md
source_context:
  05-15 mode selector recovery
  VectorFL vessel working standard candidate
  Hermes native harness / VectorFL recovery ladder
  Stage 1 local diff-audit execution tests
```

This document does not replace the existing vessel standard, Hermes ladder, recovery classes, or Stage 1 tests.

It sits above them as a map for how VectorFL attaches external tools, domain pipelines, execution agents, and output surfaces without losing recovery discipline.

## 2. Core Judgment

```text
VectorFL is not one pipe.
VectorFL is a flow-network that observes, routes, controls, and selectively recovers
materials produced by users, tools, models, domains, and execution harnesses.
```

Short rule:

```text
External tools may move.
VectorFL must observe, classify, and recover selectively.
```

Current Hermes-specific rule generalized:

```text
Let external tools act natively.
Let VectorFL recover selectively.
```

## 3. Metaphor Stack

### 3.1 Factory Pipeline

Useful for a single bounded task:

```text
input -> processing -> output
```

Example:

```text
diff fixture -> audit script -> report/receipt
```

Limit:

```text
It hides multi-agent routing, permission gates, repeated traces, side effects, and promotion boundaries.
```

### 3.2 Traffic Network

Useful for external tool attachment:

```text
roads:
  lanes, routes, junctions, detours, restricted roads

vehicles:
  tasks, agents, outputs, artifacts

cargo:
  content, evidence, decisions, generated files, customer drafts, traces

traffic control:
  permission gates, STOP/HOLD, routing, recovery classes
```

Core reading:

```text
VectorFL is a traffic-control and recovery space for many flows,
not a single linear pipeline.
```

### 3.3 Power Grid

Useful for capability and load:

```text
models/tools:
  power plants

packet builder:
  transformer/substation

mode selector:
  load balancer

recovery gate:
  meter + circuit breaker

STOP/HOLD:
  breaker

VectorFL reservoir:
  battery/reservoir
```

Core reading:

```text
Strong capability should not be connected directly to authority or memory.
It must pass through transformation, metering, and circuit-breaking.
```

## 4. LACL as Intersection Camera

```text
LACL = local axis / layer camera / intersection observation lens
```

LACL does not know the whole life of a task.

It observes a flow at a specific point:

```text
what layer is this material moving through?
what direction is it taking?
is this execution, recovery, proposal, or promotion pressure?
is this receipt, residue, candidate, component, proposal, or STOP?
```

Traffic metaphor:

```text
A CCTV at an intersection can see that a vehicle entered from north and exited east.
It cannot know the full origin, destination, motive, or final authority status alone.
```

Therefore:

```text
Single LACL observation is evidence.
Multiple LACL observations can reveal route.
Route still does not equal authority.
```

## 5. Vessel Synchronization

The existing vessel standard maps into the flow network:

```text
IIC:
  intake control / entry reading
  "What is this vehicle and where does it seem to be going?"

SOF:
  traffic law / permission / authority gate
  "Is this vehicle allowed on this road?"

RML:
  CCTV archive / travel record / receipt spine
  "Where did it come from and what trace did it leave?"

MOL:
  road network / routes / machinery / tool lane
  "What path, script, tool, or vehicle actually moves it?"
```

Non-negotiable separations:

```text
reading != permission
route != execution approval
record != memory promotion
execution success != VectorFL approval
tool exposure != invocation approval
delivery != recovery
persistence != memory
```

## 6. Packet Builder

```text
Packet = waybill + route permit + recovery contract
```

A packet tells an external tool:

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

Without a packet:

```text
"do this" can become open-ended execution, persistence, tool drift, or authority mutation.
```

The Stage 1 local diff-audit packet was a first successful small route permit:

```text
read only fixture diffs
create one script
run once
write report/receipt
do not patch, commit, use network, create skill, write memory, schedule cron, or update VectorFL authority
recover as receipt/residue/candidate only
```

## 7. Gate Stack

Every external-tool run should be split into four gates:

```text
1. Action Permission
   May the tool perform this action?

2. External Side Effect Permission
   Will this affect an external system?
   Examples: send email, post Slack, write DB, deploy VPS, publish page, write external note.

3. Persistence Permission
   What remains after the run?
   Examples: file, report, receipt, memory, skill, cron, config, MCP registration, note output.

4. VectorFL Recovery Permission
   How does VectorFL receive the result?
   discard / receipt / residue / candidate / component / space_update_proposal / STOP.
```

Important:

```text
No external side effect does not mean no persistence.
Hermes persistence does not mean VectorFL recovery.
Successful external-tool execution does not mean VectorFL approval.
```

## 8. Recovery Classes as Cargo Classification

```text
discard:
  disposable packaging / one-off byproduct

receipt:
  travel record / delivery evidence

residue:
  repeated trace / meaningful residue, not reusable yet

candidate:
  reusable route, rule, threshold, prompt, or behavior candidate

component:
  validated small part / bounded reusable lane element

space_update_proposal:
  proposal to change the road map or authority surface, not approved

STOP:
  hazardous cargo / unauthorized entry / authority boundary violation

external_action_approval_required:
  vehicle may be able to move, but external side effect needs explicit approval
```

Key recovery rule:

```text
External-tool success is receipt.
Repeated signal is residue.
Reusable possibility is candidate.
Only validated bounded parts become component.
Space change is proposal.
Authority mutation pressure is STOP.
```

## 9. Hermes Lane as First Strong External Tool Lane

Hermes is the first strong test case:

```text
Hermes = native execution harness / work vehicle / automation engine
```

Hermes-native capabilities may include:

```text
terminal
file read/write
execute_code
browser/web
MCP
memory
skills
cron
messaging
external apps
deployment
delegation
```

But:

```text
Hermes memory != VectorFL memory
Hermes skill != VectorFL SKILL.md
Hermes cron != VectorFL workflow
Hermes note/output sink != VectorFL authority
Hermes report != VectorFL baseline
Hermes successful run != VectorFL approval
Hermes execution permission != VectorFL recovery permission
Hermes side effect approval != VectorFL promotion approval
```

## 10. External Tool / Domain Lanes

The same model can attach other lanes:

```text
Codex lane:
  code edits, local repo work, recovery, structural judgment

Gemini lane:
  broad comparison, large synthesis, maturation

browser/web lane:
  source discovery, citation recovery, external-current verification

email/app lane:
  read-only export, draft-only write, send approval gate

database lane:
  schema/sample read, query drafting, live mutation approval

content lane:
  blog, shorts, cards, daily brief, publishing approval

company-docs lane:
  onboarding, protocol docs, repo/docs/debug outputs, team trace recovery

notes/output lane:
  Obsidian/Notion/local markdown as output sink, not authority
```

Each lane needs:

```text
packet
permission surface
persistence boundary
receipt contract
recovery class
promotion boundary
WATCH/HOLD
```

## 11. Stage 1 Diff-Audit Position

The Stage 1 diff-audit tests were not the destination.

They were the first road segment test.

Validated:

```text
Hermes native local execution:
  passed

persistence boundary:
  passed

report/receipt contract:
  passed

VectorFL selective recovery:
  receipt/residue/candidate passed

promotion hold:
  component/workflow/skill/baseline held
```

Still not:

```text
component
workflow
skill
baseline
VectorFL authority
```

Rule-quality test added:

```text
clean diff:
  no hard findings

borderline diff:
  review note

docs false-positive:
  documentation-context review note
```

This supports candidate refinement, not promotion.

## 12. Real-World Hermes Use Case Mapping

Real Hermes use cases fit the flow-network model:

```text
inbox -> Slack brief:
  delivery is not recovery

landing page -> VPS deploy:
  public deploy requires external side-effect approval

daily briefing card -> Telegram:
  cron is not VectorFL workflow

team repo/docs/MCP debug:
  tool output is not organizational truth

two-tier email detector:
  cheap detector -> only-if-needed session -> selective recovery

daily research across channels:
  output flood needs reduction before recovery

chief-of-staff multi-agent:
  sub-agent memory is not VectorFL memory

git diff audit:
  good Stage 1 local lane candidate

skill factory:
  observed repetition is not approved skill/component
```

Common rules:

```text
Delivery is not recovery.
Persistence is not memory.
Skill is not component.
Cron is not workflow.
Tool exposure is not invocation approval.
Successful run is not VectorFL approval.
Repeated pattern is not baseline.
Generated artifact is not judgment.
```

## 13. Test Strategy

Small tests are not toy tasks.

They are pressure tests on the flow network:

```text
Can the vehicle move?
Did it stay on the permitted route?
What did it leave behind?
Can we distinguish output, receipt, residue, candidate, component, proposal, STOP?
Did it avoid unauthorized side effects?
Did we avoid authority promotion?
```

Escalation pattern:

```text
Stage 0:
  simulated inputs

Stage 1:
  local deterministic execution

Stage 2:
  read-only web/browser or pre-captured source packet

Stage 3:
  external app read-only

Stage 4:
  write-draft only

Stage 5:
  manual automation

Stage 6:
  recurring automation

Stage 7:
  native memory/skill
```

Escalation should happen only when:

```text
packet quality is clear
receipt quality is clear
persistence boundary is clear
recovery class is clear
STOP/HOLD behavior is clear
prior stage passed with WATCH
```

## 14. WATCH

```text
WATCH:
  traffic/power-grid metaphor becoming ontology
  flow-network model becoming workflow
  LACL observation being treated as full truth
  route fluency becoming execution approval
  receipt becoming memory
  candidate becoming component too early
  component becoming workflow
  Hermes output becoming VectorFL authority
  external side-effect approval being confused with promotion approval
  raw output flood entering VectorFL Space
```

## 15. HOLD

```text
HOLD:
  AGENTS.md update
  SKILL.md creation
  Hermes memory/skill/config edit
  real cron / recurring automation
  baseline promotion
  workflow/schema/registry/ontology creation
  current-position update
  output_manifest update
  local core / derived / surface authority change
  official ontology promotion
  raw Hermes output bulk ingestion
```

## 16. Next Smallest Action

Recommended next action:

```text
Real-ish Stage 1 diff fixture expansion
```

Purpose:

```text
Test whether the candidate diff-audit lane handles more varied fixtures:
clean, borderline, actual risk, docs example, test fixture, generated file, config file.
```

Recovery expectation:

```text
receipt:
  run evidence

residue:
  false-positive / borderline behavior

candidate:
  refined rule set

component:
  still HOLD until repeated validation on real diffs
```

Alternative:

```text
Reduced Gemini maturation packet for Stage 1 diff-audit results.
```

But fixture expansion should come first if component candidacy is being considered.

