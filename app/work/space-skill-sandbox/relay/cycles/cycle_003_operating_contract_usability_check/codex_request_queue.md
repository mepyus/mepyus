# Codex Request Queue
# cycle_003_operating_contract_usability_check

cycle_id:
  cycle_003_operating_contract_usability_check

queue_status:
  CODEX_RETURNED

Purpose:
  Collect Gemini-created structure requests if Gemini finds structural gaps in the operating contract pack.

Authority:
  request queue only

not:
  registry
  workflow
  automation
  baseline
  current-position
  output_manifest

Current requests:
  processed with watch

| request_id | source Gemini task | structural gap | requested Codex work | expected output | priority | forbidden actions | status |
|---|---|---|---|---|---|---|---|
| cycle_003_gap_001_create_gemini_work_order_template | contract usability verification | missing physical Gemini work order template referenced by contracts | create Gemini work order template aligned with Manual Cycle Relay and Gemini execution lane | app/work/space-skill-sandbox/relay/templates/gemini_work_order_template_v0.md | Medium | no automation; no current-position update; no output_manifest update; no workflow/registry/schema/baseline promotion | DONE_WITH_WATCH |

Processed output:
  app/work/space-skill-sandbox/relay/templates/gemini_work_order_template_v0.md

Important:
  Request processing does not approve contracts as baseline.

Queue watch:
  - request queue is not registry
  - Codex request is not execution permission
  - template creation is not workflow creation

