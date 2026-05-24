# Hermes Automation Session Pilot Manifest v0

purpose:
  one-shot Hermes automation session pilot for VectorFL

inputs:
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md
  - app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md

outputs:
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/run_automation_session.py
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md

automation boundary:
  no real cron, no recurring job, no Hermes memory/skill/config, no VectorFL authority

success criteria:
  explicit-file only
  report and receipt written
  vessel terms detected
  automation safety terms detected
  no promotion language in final judgment
