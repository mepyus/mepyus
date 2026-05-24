# Scenario 1 Hermes Execution Receipt

{
  "receipt_id": "scenario_1_hermes_execution_receipt_v0",
  "classification": "receipt_hermes_no_call_execution_with_hold",
  "source_layer": "tool_reentry_layer",
  "status": "PASS",
  "validators_run": [
    {
      "path": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_no_call_real_reentry_test_v0/validate_no_call_real_reentry_test.py",
      "rc": 0,
      "seconds": 0.1,
      "stdout": "PASS_NO_CALL_REAL_REENTRY_TEST_WITH_HOLD\nvalidators=5/5\nforbidden_scan=PASS\napi_call=NO\npromotion=HOLD",
      "stderr": ""
    },
    {
      "path": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_model_result_intake_reentry_dry_run_v0/validate_model_result_intake_reentry_dry_run.py",
      "rc": 0,
      "seconds": 0.067,
      "stdout": "PASS_MODEL_RESULT_INTAKE_REENTRY_DRY_RUN_WITH_HOLD\ncases_checked=5\nreal_codex_execution=NO\nreal_gemini_execution=NO\nsynthetic_model_outputs=YES\nraw_lite_receipt_reentry_contract=PASS\nauthority_mutation=NO\npromotion=HOLD",
      "stderr": ""
    }
  ],
  "forbidden_scan": {
    "scan_hits": [
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_hermes_execution_packet_v0.json",
        "pattern": "api_contract_replay\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_hermes_execution_packet_v0.json",
        "pattern": "api_drift_replay_gate\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_hermes_execution_packet_v0.json",
        "pattern": "phase1_deterministic_stable_cycle\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_space_reading_packet_v0.json",
        "pattern": "api_contract_replay\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_space_reading_packet_v0.json",
        "pattern": "api_drift_replay_gate\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_space_reading_packet_v0.json",
        "pattern": "phase1_deterministic_stable_cycle\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_space_mediated_merge_packet_v0.json",
        "pattern": "api_contract_replay\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_space_mediated_merge_packet_v0.json",
        "pattern": "api_drift_replay_gate\\.py"
      },
      {
        "file": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_scenario_1_space_mediated_program_behavior_test_v0/scenario_1_space_mediated_merge_packet_v0.json",
        "pattern": "phase1_deterministic_stable_cycle\\.py"
      }
    ],
    "active_call_hits": [],
    "active_call_scan_status": "PASS"
  },
  "seconds": 0.171,
  "api_call": "NO",
  "local_http_endpoint_replay": "NO",
  "local_server_start": "NO",
  "model_execution": "NO_FIXTURE_ONLY",
  "authority_effect": "NO_AUTHORITY_MUTATION",
  "promotion_status": "HOLD",
  "guard_status": "PASS_WITH_HOLD"
}
