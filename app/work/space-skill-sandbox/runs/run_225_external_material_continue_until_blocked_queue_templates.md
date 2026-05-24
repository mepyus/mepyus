# Run 225 - External Material Continue-Until-Blocked Queue Templates

## 1. Source Basis
This run is based on the validated internal patterns from:
- `run_199`: Internal material usage test (4-line card success).
- `run_200`/`run_201`: Material gate correctly stopping at missing source.
- `run_202`: Real external reference comparison discipline.
- `run_207`: PROCESS_MEMORY_LIGHT closeout practice.
- `run_223`/`run_224`: Two-agent pipeline candidate and packet field refinements.

## 2. Gemini Extraction Result
Accepted the Gemini extraction result: `PIPELINE_FLOW_EXTRACTED_WITH_WATCH`. The extraction correctly identified the 10-task sequence and the "Continue-Until-Blocked" decision logic.

## 3. Files Created
- `app/work/space-skill-sandbox/outputs/gemini_external_material_queue_template_v0.md`
- `app/work/space-skill-sandbox/outputs/gemini_external_material_task_packet_template_v0.md`
- `app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md`
- `app/work/space-skill-sandbox/outputs/gemini_external_material_continue_until_blocked_rules_v0.md`
- `app/work/space-skill-sandbox/outputs/gemini_external_material_pipeline_memory_note_v0.md`

## 4. Why This Is Useful
These templates provide a durable structural frame for handling external materials across AI sessions. By defining clear "Stop Conditions" and "Continue Rules," we can reduce manual relay load without sacrificing human-in-the-loop control or authority boundaries.

## 5. Why This Is Not Automation
This is "Semi-Automation" or "Harness-Guided Execution." Each task is a bounded observation. The "auto-continue" only moves to the next *predefined* task in a static queue. There is no autonomous routing, no hidden decisions, and the User remains the final decision gate.

## 6. How It Reduces User Relay Load
By allowing Gemini to process a queue of read/observe tasks (e.g., Summary -> Card -> Comparison) in a single worker burst, the User does not need to repeatedly trigger "next" for low-risk evidence collection.

## 7. Stop Conditions Preserved
All critical stop conditions (NEEDS_USER_MATERIAL, AUTHORITY_RISK, PROMOTION_RISK, etc.) are explicitly codified in the Rules and Template metadata.

## 8. Current-Position Decision
Verdict: `CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED`.
Reason: This represents a meaningful candidate direction, but the templates should be reviewed by User/ChatGPT before becoming the latest active anchor.

## 9. Recommendation
`REVIEW_QUEUE_TEMPLATES_BEFORE_FIRST_REAL_USE`.

## 10. Boundary Confirmation
- no baseline promotion
- no official workflow
- no automation/router/controller
- no registry/index/ledger
- no formal permission system
- no Gemini approval authority
- no Gemini verified-truth authority
- no Codex-to-Gemini autonomous routing without User-selected purpose
- no package movement
- no Run 117 approval
- no hidden background execution
- no executable scripts
- no current-position update applied

STATUS: EXTERNAL_MATERIAL_CONTINUE_UNTIL_BLOCKED_QUEUE_TEMPLATES_PREPARED
