# Flow-Network Program Topology Check v0

## 1. Verdict

```text
FLOW_NETWORK_PROGRAM_TOPOLOGY_CHECK_DRAFTED_FOR_LEVEL_1_5_TO_LEVEL_2_BRIDGE_WITH_AUTOMATION_HOLD
```

## 2. Status

```text
status: topology_check_candidate
scope: Hermes main runtime -> Codex space worker -> Gemini exploration lens
authority: sandbox-local candidate
target_level: Level 1.5 to Level 2
```

This is not:

```text
workflow
automation
schema
registry
ontology
baseline
component
AGENTS.md
SKILL.md
current-position
output_manifest
```

This document does not authorize execution.

This document does not connect tools.

This document does not promote the packet validity line.

## 3. Purpose

Check whether this operating topology can be used safely in real program use:

```text
Hermes main runtime
  -> Codex space worker
    -> Gemini exploration lens
```

Goal:

```text
reduce user transfer burden
standardize packet / receipt / return path
preserve user approval points
prevent permission inheritance
```

Non-goals:

```text
automatic recurring tool calls
Hermes replacing VectorFL authority
Codex inheriting Hermes permissions
Gemini becoming truth/component authority
cron or recurring bridge
external connector execution
automatic promotion
```

## 4. Current Flow-Network Anchor

Base line:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

Program topology insertion point:

```text
MOL -> Packet -> Dispatch Approval -> Lane
```

Expanded lane possibility:

```text
Hermes main runtime
  -> Codex space worker
    -> Gemini exploration lens if explicitly declared
```

Return must flow back through:

```text
Gemini raw output
  -> Codex recovery summary
    -> Hermes receipt/report
      -> VectorFL recovery classification
        -> User / ChatGPT promotion decision if requested
```

## 5. Role Definitions

### Hermes

```text
role:
  main execution runtime
  receipt/report collector

not:
  VectorFL authority
  automatic promotion engine
  unrestricted approval holder
```

Hermes may have native capabilities:

```text
terminal
file
browser
web
connector
cron
messaging
skill
memory
```

But capability is not permission.

### Codex

```text
role:
  VectorFL space worker
  repo-side boundary reviewer
  packet/return/recovery formatter

not:
  inherited Hermes executor
  unrestricted repo mutator
  VectorFL promotion authority
```

Codex may be invoked by Hermes only through a declared scope.

### Gemini

```text
role:
  broad-context exploration lens
  candidate maturation aid

not:
  truth source
  final reviewer
  component approver
  promotion authority
```

Gemini output must be reduced by Codex before recovery.

### VectorFL

```text
role:
  recovery classifier
  promotion gate
  authority boundary
```

### User / ChatGPT

```text
role:
  direction
  WATCH/HOLD judgment
  dispatch approval
  external side-effect approval
  final promotion approval
```

## 6. Lane Type v0

```text
LANE_0_CHATGPT_ONLY:
  explanation, judgment, docs, scenario
  no execution

LANE_1_CODEX_LOCAL:
  repo-side structure check
  packet/return document creation
  VectorFL space work

LANE_2_HERMES_NATIVE:
  Hermes direct execution
  file/terminal/browser/connector/cron if explicitly approved

LANE_3_HERMES_TO_CODEX:
  Hermes prepares or invokes Codex worker request
  Codex performs declared repo-side scope only

LANE_4_HERMES_TO_CODEX_TO_GEMINI:
  Codex uses Gemini exploration lens
  Gemini output is raw evidence/residue, not truth

LANE_5_HERMES_EXTERNAL_APP:
  Slack/email/browser/DB/CRM/Obsidian or other external connector
  external side-effect approval required

LANE_6_MANUAL_BRIDGE:
  no direct tool connection
  packet/receipt/return path only
```

Recommended current default:

```text
design LANE_3 or LANE_4,
operate as LANE_6 or structured manual bridge until separately approved.
```

## 7. Bridge Levels

```text
Level 0:
  manual bridge
  user copies packet/return between tools

Level 1:
  structured manual bridge
  packet/receipt/return formats are fixed

Level 1.5:
  Hermes prepares Codex/Gemini request files and return contracts
  user passes short path + approval line

Level 2:
  harness-assisted bridge
  Hermes may invoke Codex CLI or worker in declared scope
  no recurring automation

Level 3:
  tool-linked Hermes -> Codex -> Gemini bridge
  HOLD

Level 4:
  cron / recurring / automatic detection / persistent bridge
  HOLD
```

Current target:

```text
Level 1.5 to Level 2 design only
```

Current HOLD:

```text
Level 3
Level 4
```

## 8. Packet Topology Fields

Future packets should include:

```text
EXECUTION_TOPOLOGY:
  Hermes main runtime
  -> Codex space worker
  -> Gemini exploration lens if explicitly declared

LANE_TYPE:
  CHATGPT_ONLY
  CODEX_LOCAL
  HERMES_NATIVE
  HERMES_TO_CODEX
  HERMES_TO_CODEX_TO_GEMINI
  HERMES_EXTERNAL_APP
  MANUAL_BRIDGE

DISPATCH_TARGET:
  Hermes | Codex | Manual | User

HERMES_ROLE:
  execution runtime / report collector
  not VectorFL authority

CODEX_ROLE:
  space worker / repo-side boundary reviewer
  not unrestricted Hermes delegate

GEMINI_ROLE:
  broad-context exploration lens
  not truth source
  not promotion authority

RETURN_PATH:
  Gemini raw output
  -> Codex recovery summary
  -> Hermes receipt/report
  -> VectorFL recovery classification
  -> User approval if promotion requested

PERMISSION_INHERITANCE_BOUNDARY:
  Hermes permission does not flow to Codex.
  Codex permission does not flow to Gemini.
  Gemini output does not become truth.
  Hermes orchestration does not become VectorFL approval.

ALLOWED_ACTIONS:
  explicit list only

FORBIDDEN_ACTIONS:
  memory write
  skill creation/update
  cron creation/update
  config mutation
  external connector side effect
  repo authority mutation
  VectorFL authority file mutation
  network/API use unless explicitly approved

OUTPUT_CONTRACT:
  required report path
  required receipt path
  required return packet path

RECOVERY_CLASS_HINT:
  discard | receipt | residue | candidate | component | proposal | STOP

PROMOTION_STATUS:
  no promotion without separate approval
```

## 9. Permission Inheritance Boundary

Core rule:

```text
Dispatch approval is not transitive.
```

Meaning:

```text
User approves Hermes dispatch
  != User approves Codex unrestricted work

Hermes invokes Codex
  != Codex inherits Hermes tool permissions

Codex invokes Gemini
  != Gemini output becomes accepted knowledge

Hermes collects receipt
  != VectorFL recovery approval

VectorFL recovery classification
  != promotion
```

Non-inheritable permissions:

```text
file write authority
repo mutation authority
git commit authority
network/API authority
browser authority
external connector authority
memory authority
skill authority
cron authority
config authority
promotion authority
```

## 10. User Approval Points

User must keep approval over:

```text
1. Dispatch Approval
2. External Side Effect Approval
3. Persistence Approval
4. Repo / Authority Mutation Approval
5. Promotion Approval
```

User burden may be reduced for:

```text
long context copying
tool-specific re-prompting
return format rewriting
prior state re-explaining
result interpretation formatting
```

User burden must not be reduced for:

```text
approval rights
STOP/HOLD judgment
promotion judgment
side-effect approval
```

## 11. Minimal Transfer Unit

For Level 1.5 to Level 2, a practical transfer unit can be:

```text
APPROVED_DISPATCH:
  packet: [absolute or repo-relative path]
  lane: HERMES_TO_CODEX_TO_GEMINI
  output_dir: [declared output path]
  return: RETURN_PACKET_V0 + RECEIPT_V0
  constraints:
    no memory
    no skill
    no cron
    no config
    no external side effect
    no promotion
    no authority mutation
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

This reduces transfer text.

It does not reduce approval responsibility.

## 12. Program Topology Check Questions

### A. Lane Selection

```text
[ ] ChatGPT-only is sufficient?
[ ] Codex-local repo-side work?
[ ] Hermes-native execution needed?
[ ] Hermes -> Codex needed?
[ ] Codex -> Gemini exploration needed?
[ ] External app / connector needed?
[ ] Manual bridge should remain?
```

### B. Invocation Reality

```text
[ ] Hermes -> Codex invocation method declared?
    CLI / terminal / file packet / manual bridge / ACP
[ ] Codex execution location is a git repo?
[ ] Codex PTY/interactive needs are known?
[ ] Codex output is stdout or file?
[ ] Declared output paths exist or can be created?
```

### C. Gemini Lens

```text
[ ] Why is Gemini needed?
[ ] Gemini input scope is bounded?
[ ] Gemini raw output path is declared?
[ ] Gemini output is not truth/component?
[ ] Codex reduction step is declared?
```

### D. Return Path

```text
[ ] raw output path exists?
[ ] Codex recovery summary path exists?
[ ] Hermes receipt/report path exists?
[ ] VectorFL recovery classification is pending, not automatic?
[ ] promotion remains separate approval?
```

### E. Permission Boundary

```text
[ ] Codex does not inherit Hermes authority?
[ ] Gemini does not inherit Codex/Hermes authority?
[ ] memory/skill/cron/config forbidden or separately approved?
[ ] external side effect forbidden or separately approved?
[ ] repo/authority mutation forbidden or separately approved?
```

### F. User Burden

```text
[ ] user need not copy long context?
[ ] user provides path + approval line only?
[ ] return file path is enough to recover?
[ ] user's judgment points remain explicit?
```

### G. STOP Criteria

```text
[ ] undeclared file write attempted
[ ] undeclared network/API use attempted
[ ] memory/skill/cron/config access attempted
[ ] VectorFL authority file mutation attempted
[ ] Gemini result treated as truth/component
[ ] Hermes receipt treated as approval
[ ] promotion automation attempted
[ ] return path missing
```

## 13. Recommended Output Contracts

```text
CODEX_WORKER_REQUEST_V0:
  Hermes -> Codex request packet

GEMINI_EXPLORATION_REQUEST_V0:
  Codex -> Gemini exploration packet

CODEX_RETURN_PACKET_V0:
  Codex -> Hermes/VectorFL recovery packet

HERMES_EXECUTION_RECEIPT_V0:
  Hermes execution receipt

PROGRAM_TOPOLOGY_STOP_RULES_V0:
  permission inheritance / automation / promotion stop rules
```

These are recommended future candidates only.

Do not create them unless separately requested.

## 14. Current Recommended Level

```text
GO:
  Level 1.5 design
  Level 2 design
  packet topology fields
  return path standardization

HOLD:
  Level 3 tool-linked bridge
  Level 4 cron / recurring bridge
  external connector execution
  memory/skill/config mutation
  automatic promotion
  Gemini truth adoption
  Codex permission inheritance
```

## 15. Recovery Classification

```text
receipt:
  program topology check drafted from Hermes response and current v0.1 packet validity line.

residue:
  real program use needs lane type, return path, and permission inheritance boundaries.

candidate:
  Level 1.5 to Level 2 structured bridge design is a strong candidate.

component:
  no.

space_update_proposal:
  no.

STOP:
  treating topology check as automation, connector approval, permission inheritance, or promotion.
```

## 16. WATCH

```text
1. Topology check becoming workflow/schema/ontology.
2. Hermes main runtime becoming VectorFL authority.
3. Codex inheriting Hermes permissions.
4. Gemini output becoming truth/component.
5. Return path bypassing Codex recovery summary.
6. Level 2 design drifting into Level 3/4 automation.
7. User approval burden being removed instead of transfer burden.
```

## 17. HOLD

```text
no Hermes dispatch
no Codex worker launch by Hermes
no Gemini dispatch
no tool-linked bridge
no recurring bridge
no external connector execution
no packet execution
no script run
no web browsing
no source lookup
no network / browser / MCP
no live connector use
no message sent
no cron created
no recurring automation
no gateway install
no Hermes memory / skill / cron / config edit
no implementation created
no component promotion
no workflow creation
no skill creation
no baseline promotion
no schema/registry/ontology creation
no current-position update
no output_manifest update
no AGENTS.md update
no SKILL.md creation
no VectorFL authority mutation
```

## 18. Next Smallest Action

Create one small future-candidate field definition only if needed:

```text
FLOW_PACKET_TOPOLOGY_FIELDS_V0
```

This should define fields, not implement a bridge.

Do not launch Hermes/Codex/Gemini.

Do not automate.

## 19. Hard Stop Confirmation

```text
No Hermes execution performed.
No Codex worker launched by Hermes.
No Gemini execution performed.
No packet executed.
No script run performed.
No web browsing performed.
No source lookup performed.
No live connector used.
No message sent.
No cron created.
No recurring automation created.
No gateway installed.
No Hermes memory/skill/config edited.
No implementation created.
No component promotion performed.
No workflow/schema/registry/ontology/baseline/automation created.
No AGENTS.md / SKILL.md / current-position / output_manifest update.
No VectorFL authority mutation.
```

