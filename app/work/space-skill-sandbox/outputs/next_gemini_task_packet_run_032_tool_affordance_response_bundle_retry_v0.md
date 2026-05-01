# Run 032 Retry - Tool Affordance / Caller Shift Lens v0 Response Bundle

## Mode

GEMINI / SANDBOX ONLY / RESPONSE BUNDLE DRAFT / NO FILE WRITE / NO PROMOTION / NO AUTOMATION

## Purpose

Create the Run 032 Tool Affordance / Caller Shift Lens materials as a response-only file bundle.

Important:

Do not write files directly.
Do not call file-write tools.
Do not call shell tools.
Return the requested file contents inside the `FILE_BUNDLE` blocks below.
Codex will validate and materialize the files later.

## Context

Previous Run 032 attempts failed because the Gemini CLI runner could return short text but did not reliably create repository files. This retry changes the handoff contract:

- Gemini drafts the content.
- Codex manages repository file creation after validation.

## Input References

Use the following references conceptually if available in prompt context:

- app/work/space-skill-sandbox/outputs/operating_order_principles_v0.md
- app/work/space-skill-sandbox/outputs/operating_order_source_map_v0.md
- app/work/space-skill-sandbox/outputs/sandbox_promotion_pipeline_v0.md
- app/work/space-skill-sandbox/outputs/session_role_map_v0.md
- app/work/space-skill-sandbox/outputs/sandbox_execution_chain_v0.md

If you cannot read files, proceed from the task packet only and state that limitation in the run record content.

## Target Files

Return content for exactly these target files:

- app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md
- app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md
- app/work/space-skill-sandbox/review/validation_round_32.md

## Required Structure for tool_affordance_caller_shift_lens_v0.md

# Tool Affordance / Caller Shift Lens v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- automation: false

## 1. Purpose

This lens is a sandbox candidate for reading which caller a tool, skill, existing program, relay packet, or session role assumes.

## 2. Core Idea

Function signature is not enough. For LLM or agent use, the context must identify:

- when to use
- when not to use
- who is the caller
- what context is required
- what output is expected
- what must be stopped
- what requires user judgment

## 3. Caller Types

Define all caller types:

1. Human Caller
2. LLM Caller
3. Codex Worker Session
4. Gemini Analysis Session
5. Validation Session
6. Relay Session
7. Future Agent Session
8. Existing Program Caller

For each caller, include:

- caller description
- likely intent
- risk
- required affordance
- required stop point
- allowed output
- forbidden output

## 4. Affordance Reading Checklist

Include checks for:

- What does it appear to do?
- Who is expected to call it?
- What hidden assumption does it make about the caller?
- Does it expect human judgment before action?
- Can an LLM misuse it?
- Does it change files?
- Does it change source-space?
- Does it install tools?
- Does it create automation?
- Does it require preflight?
- Is it reversible?
- What output should be captured?

## 5. Caller Shift Risk

Describe risks when a human-oriented tool is used by an LLM:

- insufficient instruction surface
- over-execution
- wrong file modification
- source-space contamination
- automation misread
- skipped validation
- readiness/promotion confusion
- failure-to-rule confusion

## 6. Lens Output Format

Include:

- target:
- original caller assumption:
- possible LLM caller:
- required affordance:
- required preflight:
- may read:
- may write:
- must not:
- expected output:
- stop point:
- user judgment required:
- candidate status:

## 7. Relationship to Existing Principles

Connect to:

- Function보다 Affordance
- Conversation보다 Agent-readable Context
- Plan before Execution
- Definition before Prompt
- User as Judge
- Core보다 Workspace

## 8. Non-Promotion Note

This lens is a sandbox candidate only.
It does not create a tool.
It does not install a tool.
It does not modify source-space.
It does not create automation.
It does not declare Relay v1.0.
It does not create a baseline.

## Required Run Record Content

Create response-bundle content for:

app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md

Include:

- mode
- purpose
- input references
- target output files
- source-space modification: false
- baseline created: false
- Relay v1 declared: false
- automation created: false
- tool installed: false
- agent implementation created: false
- note that this retry returned a response bundle and Codex materialization is required

## Required Validation Record Content

Create response-bundle content for:

app/work/space-skill-sandbox/review/validation_round_32.md

Validation checks:

- lens_content_returned: true
- run_record_content_returned: true
- validation_record_content_returned: true
- response_bundle_mode: true
- caller_types_defined: true
- affordance_checklist_included: true
- caller_shift_risk_included: true
- output_format_included: true
- source_space_modified: false
- baseline_created: false
- relay_v1_declared: false
- automation_created: false
- tool_installed: false
- agent_implementation_created: false

## Forbidden Actions

Do not:

- write files directly
- call file-write tools
- call shell tools
- modify source-space
- create baseline
- declare Relay v1.0
- modify worker guide
- create worker_guide_v0_4
- create automation
- install tools
- create MCP/hook/watch mode
- create router/controller/schema/ontology
- merge existing programs
- create production workflow

## Required Response Format

Return exactly one `FILE_BUNDLE` section.

Use this format:

```text
FILE_BUNDLE_BEGIN
FILE: app/work/space-skill-sandbox/outputs/tool_affordance_caller_shift_lens_v0.md
CONTENT_BEGIN
<full markdown content>
CONTENT_END

FILE: app/work/space-skill-sandbox/runs/run_032_tool_affordance_caller_shift_lens.md
CONTENT_BEGIN
<full markdown content>
CONTENT_END

FILE: app/work/space-skill-sandbox/review/validation_round_32.md
CONTENT_BEGIN
<full markdown content>
CONTENT_END
FILE_BUNDLE_END
```

## Closeout

This is a sandbox response-bundle lens draft retry only.
No direct file write was performed by Gemini.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No worker_guide_v0_4 was created.
No automation, hook, MCP, watch mode, router, controller, ontology, schema, agent implementation, tool installation, existing program merge, or production workflow was created.
tool_affordance_caller_shift_lens_v0 remains a sandbox candidate lens, not a source-space rule or baseline.
