# Codex Worker Request v0

## 1. Verdict

```text
CODEX_WORKER_REQUEST_V0_DRAFTED_AS_TEMPLATE_ONLY_WITH_EXECUTION_HOLD
```

## 2. Status

```text
status: request_template_candidate
authority: sandbox-local candidate
scope: request object for Codex as VectorFL space steward / recovery judge
execution_status: template only
promotion_status: no promotion
```

This is not a Codex dispatch.
This is not a Gemini dispatch.
This is not Hermes execution approval.
This is not workflow/schema/registry/ontology/baseline/component promotion.

## 3. Purpose

Define the minimum request object Codex should receive before it frames, delegates, or recovers a Hermes/Gemini bridge task.

Core principle:

```text
Codex owns scope and recovery.
Codex does not inherit Hermes permissions.
Codex request does not equal dispatch approval.
```

## 4. Template

```yaml
REQUEST_ID: CODEX_WORKER_REQUEST_[NAME]_V0
REQUEST_VERSION: v0
REQUEST_STATUS: draft | approved_for_review | approved_for_execution

OWNER:
  Codex-space-steward

REQUESTED_BY:
  User | ChatGPT | Hermes | VectorFL-packet-review

PURPOSE:
  [one sentence]

SOURCE_PACKET:
  path: [exact packet path]
  packet_validity: candidate_only
  execution_approval_in_packet: no

EVIDENCE_PACKET:
  path: [exact evidence packet path]
  scope: [existing assets only | declared files only | other]

LANE_TYPE:
  ASSET_ONLY_CODEX_GEMINI_RECOVERY_REHEARSAL
  # or CODEX_OWNED_HERMES_RUN_GEMINI_LITE_BRIDGE when real test is approved

CODEX_ROLE:
  - scope limiter
  - request author
  - Gemini question framer if needed
  - recovery checker
  - over-promotion filter
  - return packet writer

CODEX_NOT_ALLOWED:
  - inherit Hermes tool permissions
  - mutate undeclared repo files
  - approve promotion
  - treat Gemini output as truth
  - skip VectorFL recovery gate

HERMES_ROLE:
  - workbench
  - declared file reader/writer
  - runner host only if explicitly approved
  - receipt/report collector

HERMES_NOT_ALLOWED:
  - become VectorFL authority
  - promote artifacts
  - mutate memory/skill/cron/config
  - use network/browser/MCP/external connectors without approval

GEMINI_ROLE:
  - broad comparison lens
  - repeated pattern detector
  - candidate/residue surfacer
  - lite output producer

GEMINI_NOT_ALLOWED:
  - truth source
  - final reviewer
  - component approver
  - promotion authority

DECLARED_INPUT_FILES:
  - [exact path]

DECLARED_OUTPUT_DIR:
  path: [exact path]

EXPECTED_OUTPUTS:
  codex_return: [path]
  gemini_lite_output: [path or none]
  hermes_receipt: [path]
  hermes_report: [path]

ALLOWED_ACTIONS:
  - read declared input files
  - write declared outputs under declared output dir
  - summarize with WATCH/HOLD
  - classify recovery as discard/receipt/residue/candidate/component/proposal/STOP hint only

FORBIDDEN_ACTIONS:
  - broad repo search unless separately declared
  - network/API/browser/MCP
  - external connector
  - memory mutation
  - skill mutation
  - cron mutation
  - config mutation
  - VectorFL authority mutation
  - AGENTS.md / SKILL.md / current-position / output_manifest update
  - baseline/workflow/schema/registry/ontology/component promotion

MODEL_API_TRANSPORT_SCOPE:
  none | model_api_transport_only | separately_declared

LIVE_WEB_SOURCE_LOOKUP_SCOPE:
  no | separately_declared

EXTERNAL_CONNECTOR_SCOPE:
  no | separately_declared

RECOVERY_REQUIRED:
  yes

RECOVERY_CHECKLIST:
  - confirm scope
  - confirm output shape
  - remove or mark over-promotion language
  - restore WATCH/HOLD
  - classify recovery hint
  - identify next smallest action

PROMOTION_STATUS:
  no promotion

STOP_CONDITIONS:
  - missing exact paths
  - missing declared output dir
  - network ambiguity
  - Gemini truth/promotion language
  - Codex permission inheritance pressure
  - Hermes authority drift
  - receipt missing negative evidence

DISPATCH_APPROVAL:
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

## 5. Minimal Real-Test Approval Block

A real Codex/Gemini/Hermes test must not run unless this block is filled and explicitly approved:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
APPROVED_PACKET_PATH: [exact path]
APPROVED_CODEX_WORKER_REQUEST: [exact path]
APPROVED_OUTPUT_DIR: [exact path]
APPROVED_CODEX_COMMAND: [exact command or none]
APPROVED_GEMINI_COMMAND: [exact command or none]
APPROVED_NETWORK_SCOPE: none | model_api_transport_only | separately_declared
APPROVED_LIVE_WEB_SOURCE_LOOKUP: no | separately_declared
APPROVED_EXTERNAL_CONNECTOR: no | separately_declared
APPROVED_PROMOTION: no
```

## 6. WATCH

```text
Codex request being mistaken for dispatch approval
Codex inheriting Hermes permissions
Codex recovery being skipped after Gemini/Hermes output
Gemini lite output being treated as truth
Hermes receipt/report being treated as recovery approval
candidate becoming component too early
```

## 7. HOLD

```text
real Codex run
real Gemini run
network/model API transport unless explicitly approved
live web/source lookup
external connector
cron / recurring automation
memory/skill/config mutation
VectorFL authority mutation
promotion
```
