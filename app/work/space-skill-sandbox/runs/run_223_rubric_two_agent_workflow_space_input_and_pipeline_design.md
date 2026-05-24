# Run 223 - Rubric Two-Agent Workflow Space Input and Pipeline Design

## 1. Source Identification

```text
Source = Rubric Labs / Claude한테 짜게 시키고 Codex한테 까게 시키기 / Ch 1
URL = https://rubric.im/curriculum/claude-codex-workflow/01-why-two-agents
Source type = external reference
User-provided = yes
Adoption = not adopted
Use = external comparison / pipeline inspiration
```

## 2. Files Created

```text
app/work/space-skill-sandbox/runs/run_223_rubric_two_agent_workflow_space_input_and_pipeline_design.md
app/work/space-skill-sandbox/outputs/rubric_two_agent_gemini_execution_pipeline_candidate_v0.md
```

No Gemini packet folder was created.

No executable automation was created.

## 3. Source Summary

Rubric Ch 1 argues for using two agents to reduce blind spots from single-agent self-review. It frames one agent as the main writer and another as an advisory reviewer with a different viewpoint.

The key source lessons preserved:

```text
different model / different viewpoint can catch blind spots
advisory reviewer is not a gate
review failure should not automatically block work
human judgment remains necessary
cost and complexity must justify multi-agent use
```

## 4. Our Adaptation

```text
Codex = design / structure / Gemini task packet creation
Gemini = read-heavy / observation-heavy / repeated evidence execution
ChatGPT = direction validation / role-drift detection
User = purpose selection / final judgment
```

This adaptation does not copy Rubric's Claude/Codex model directly.

## 5. Candidate Pipeline Stages Captured

```text
Stage 0. User purpose selection
Stage 1. ChatGPT direction / validation frame
Stage 2. Codex design packet
Stage 3. Codex creates Gemini task queue
Stage 4. Gemini executes task packets
Stage 5. Gemini returns evidence/results
Stage 6. Codex packages Gemini results
Stage 7. ChatGPT/User review
Stage 8. Recovery into space as run record / process-memory / watch item / current-position only if needed
```

## 6. Proposed Durable Artifact Layout

Proposed only, not implemented:

```text
app/work/space-skill-sandbox/worker-handoff-candidate/
  README.md
  queue/gemini_task_queue_candidate.md
  packets/gemini_task_packet_001.md
  results/gemini_result_001_template.md
  logs/gemini_execution_log_candidate.md
  state/handoff_state_candidate.md
```

Status:

```text
LAYOUT_CANDIDATE_ONLY
not implemented
not official workflow
not router
not automation
not registry
not ledger
```

## 7. Gemini Task Packet Design

Minimum fields:

```text
task_id
source_material
purpose
read_scope
execution_steps
expected_output
evidence_required
uncertainty_required
forbidden_actions
stop_conditions
return_format
recovery_target
```

## 8. Role Drift Checks

```text
Codex design becoming implementation authority = WATCH_ONLY
Gemini execution becoming verified truth = WATCH_ONLY
task queue becoming workflow = WATCH_ONLY
packet list becoming router = WATCH_ONLY
execution log becoming ledger = WATCH_ONLY
semi-automation becoming hidden automation = WATCH_ONLY
Rubric source becoming adoption plan = WATCH_ONLY
two-agent model overriding our Roles reference = NO_RISK_FOUND
User decision gate being bypassed = WATCH_ONLY
```

## 9. Fit Judgment

```text
FITS_WITH_WATCH
```

## 10. Current-Position Decision

```text
CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED
```

Reason:

```text
This may become the next active design direction if the User chooses it, but it should not update current-position until User/ChatGPT reviews the candidate pipeline.
```

## 11. Recommendation

```text
HOLD_FOR_USER_REVIEW
```

## 12. Boundary Confirmation

```text
no Rubric workflow adoption
no Claude/Codex model copied directly
no baseline promotion
no official workflow creation
no architecture finalization
no automation/router/controller
no registry/index/ledger promotion
no formal permission system
no Codex-to-Gemini autonomous routing
no Gemini broad run
no Gemini verified-truth authority
no package movement
no Run 117 approval
no current-position update unless explicitly required
no hidden background execution
```

`STATUS: RUBRIC_TWO_AGENT_GEMINI_PIPELINE_CANDIDATE_PREPARED`
