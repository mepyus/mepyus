DONE: top60 cluster rollup v0.1

verdict: PASS_TOP60_ROLLUP_EIGHT_MODULE_SKELETON_WITH_HOLD

module_counts_v0_1:
{
  "SAAS_M3_GUARD_PRECHECK_ENGINE": 10,
  "SAAS_M4_MATURATION_GOVERNANCE": 10,
  "SAAS_M6_ADAPTER_FACTORY": 5,
  "SAAS_M5_SPACE_INBOX_REVIEW": 5,
  "SAAS_M2_ASSET_GRAPH_ROUTER": 10,
  "SAAS_M7_ASSET_HYGIENE_OPERATOR_DASHBOARD": 10,
  "SAAS_M8_EVALUATION_TRACE_OBSERVABILITY": 10
}

key correction:
M1/M3 split restored. M1=intake/provenance, M3=guard/precheck.

folder cleanup precondition:
M2 + M7 + M8 + M4 required before any move/archive.

HOLD: no move, no authority/registry/current-position mutation, no promotion.
