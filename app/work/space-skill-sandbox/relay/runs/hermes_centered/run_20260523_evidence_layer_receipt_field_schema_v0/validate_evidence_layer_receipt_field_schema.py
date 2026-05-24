#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path("/Users/sungsookim/universe/vectorfl_replica")
RUN = ROOT / "app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_evidence_layer_receipt_field_schema_v0"

files = [
    "app/work/VECTORFL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_20260523_V0.md",
    "app/work/VECTORFL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_20260523_V0.json",
    "app/work/VECTORFL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_USER_STATUS_CARD_20260523_V0.md",
    "app/work/VECTORFL_NEXT_WORK_AFTER_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_20260523_V0.md",
    "app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_evidence_layer_receipt_field_schema_v0/fixtures/evidence_receipt_field_schema_cases.json",
]

problems = []
texts = []
for rel in files:
    path = ROOT / rel
    if not path.exists():
        problems.append("missing " + rel)
    else:
        texts.append(path.read_text(encoding="utf-8"))

combined = "\n".join(texts)
fixture_path = RUN / "fixtures/evidence_receipt_field_schema_cases.json"
schema_path = ROOT / "app/work/VECTORFL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_20260523_V0.json"

try:
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    dashboard = json.loads(schema_path.read_text(encoding="utf-8"))
except Exception as exc:
    print("FAIL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_VALIDATOR")
    print("json error " + repr(exc))
    sys.exit(1)

required = fixture.get("required_fields", [])
allowed = set(fixture.get("allowed_guard_statuses", []))
cases = fixture.get("cases", [])

if fixture.get("layer") != "evidence_layer":
    problems.append("wrong layer")
if dashboard.get("layer") != "evidence_layer":
    problems.append("wrong dashboard layer")
if dashboard.get("fixture_case_count") != len(cases):
    problems.append("dashboard fixture count mismatch")
if len(cases) != 4:
    problems.append("case_count not 4")

for field in required:
    if field not in dashboard.get("required_fields", []):
        problems.append("dashboard missing required field " + field)
    if field not in combined:
        problems.append("text missing required field " + field)

for case in cases:
    case_id = case.get("case_id", "?")
    receipt = case.get("receipt", {})
    for field in required:
        value = receipt.get(field)
        if value in (None, "", []):
            if case.get("expected_result") == "PASS_WITH_HOLD":
                problems.append("positive case missing " + field + " in " + case_id)
    guard = receipt.get("guard_status")
    if guard not in allowed:
        problems.append("bad guard " + case_id)
    if "promotion" not in " ".join(receipt.get("forbidden_actions", [])).lower() and case.get("expected_result") == "PASS_WITH_HOLD":
        problems.append("positive case lacks promotion forbidden action " + case_id)
    if case.get("expected_result") == "STOP" and receipt.get("classification") != "USER_APPROVED_PROGRAM_COMPONENT":
        problems.append("STOP fixture no authority overclaim " + case_id)
    if case.get("expected_result") == "HOLD_STOP_REVIEW" and receipt.get("not_valid_for"):
        problems.append("HOLD fixture should expose missing not_valid_for " + case_id)
    if case.get("expected_result") == "WATCH" and guard != "HOLD_UNTIL_APPROVED_MODEL_OUTPUT":
        problems.append("WATCH fixture should preserve model-output hold " + case_id)

for step in ["S1 Diagnose", "S2 Verify", "S3 Test", "S4 Reflect", "S5 Apply", "S6 Surface", "S7 Receipt", "S8 Decide next"]:
    if step not in combined:
        problems.append("missing step " + step)

for token in [
    "EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_WITH_HOLD",
    "PASS_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_WITH_HOLD",
    "PASS_WITH_HOLD",
    "WATCH",
    "HOLD_STOP_REVIEW",
    "STOP",
    "HOLD_UNTIL_APPROVED_MODEL_OUTPUT",
    "promotion_status: HOLD",
    "program_alpha_status: NOT_READY",
    "schema_registry_mutation: no",
    "live_db_intake: HOLD",
]:
    if token not in combined:
        problems.append("missing token " + token)

for data_name, data in [("fixture", fixture), ("dashboard", dashboard)]:
    for key in ["authority_mutation", "model_execution", "real_codex_execution", "real_gemini_execution", "schema_registry_mutation", "shared_db_mutation"]:
        if data.get(key) != "NO":
            problems.append(data_name + " " + key + " drift")
    if data.get("promotion") != "HOLD":
        problems.append(data_name + " promotion drift")

for bad in [
    "promotion_status: PROMOTED",
    "program_alpha_status: READY",
    "model_execution: YES",
    "real_codex_execution: YES",
    "real_gemini_execution: YES",
    "schema_registry_mutation: YES",
    "authority_mutation: YES",
    "approval_applied: YES",
]:
    if bad in combined:
        problems.append("contamination " + bad)

if problems:
    print("FAIL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_VALIDATOR")
    print("\n".join(problems))
    sys.exit(1)

print("PASS_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_WITH_HOLD")
print("layer=evidence_layer")
print("required_field_count=" + str(len(required)))
print("case_count=" + str(len(cases)))
print("guard_statuses=" + ",".join(sorted(allowed)))
print("schema_registry_mutation=NO")
print("model_execution=NO")
print("authority_mutation=NO")
print("promotion=HOLD")
