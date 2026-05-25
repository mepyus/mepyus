#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
SKILL = BASE / "vectorfl-space-operator"
FIXTURE = BASE / "dual_log_fixture_run"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(FIXTURE))


def pass_check(name, passed, **extra):
    payload = {"check": name, "pass": bool(passed)}
    payload.update(extra)
    return payload


def main():
    checks = []

    skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    checks.append(pass_check("skill_frontmatter_present", skill_md.startswith("---\nname: vectorfl-space-operator")))
    for route in [
        "CODEX_SPACE_CHECK",
        "CODEX_HERMES_WORK_ANALYSIS",
        "CODEX_SPACE_RETRIEVAL_BY_ORIGINAL",
        "CODEX_SPACE_MATURATION_BY_REENTRY_RECORD"
    ]:
        checks.append(pass_check(f"skill_route_{route}", route in skill_md))

    refs = [
        SKILL / "references" / "operation_routes.md",
        SKILL / "references" / "space_governance.md",
        SKILL / "references" / "dual_log_collision_free.md",
        SKILL / "references" / "fast_cross_inspection.md",
        SKILL / "references" / "integrated_stack.md",
        SKILL / "references" / "return_schemas.md"
    ]
    checks.append(pass_check("skill_references_present", all(p.exists() for p in refs), count=sum(p.exists() for p in refs)))
    integrated = (SKILL / "references" / "integrated_stack.md").read_text(encoding="utf-8")
    checks.append(pass_check("integrated_stack_records_governance_above_router", "Governance layer" in skill_md and "L1_SPACE_GOVERNANCE" in integrated and "L2_OPERATION_ROUTER" in integrated))
    fast = (SKILL / "references" / "fast_cross_inspection.md").read_text(encoding="utf-8")
    checks.append(pass_check("fast_cross_inspection_reference_present", "90_QUICK_EXCHANGE_BOARD" in skill_md and "90_HERMES_LATEST_SUMMARY_CARD" in fast and "90_CODEX_LATEST_SUMMARY_CARD" in fast))

    required_fixture_files = [
        FIXTURE / "shared_handoff" / "00_RUN_MANIFEST.json",
        FIXTURE / "shared_handoff" / "01_SPACE_REFERENCE_REQUEST.json",
        FIXTURE / "codex_space" / "10_CODEX_RETRIEVAL_RETURN.json",
        FIXTURE / "hermes_exec" / "20_HERMES_MERGE_EXECUTION_TRACE.json",
        FIXTURE / "shared_handoff" / "21_CODEX_READABLE_REENTRY_INDEX.json",
        FIXTURE / "codex_space" / "30_CODEX_MATURATION_PROPOSAL.json",
        FIXTURE / "hermes_exec" / "40_HERMES_MATURATION_MERGE_RECEIPT.json",
        FIXTURE / "shared_handoff" / "99_LATEST_POINTERS.json"
    ]
    checks.append(pass_check("fixture_required_handles_present", all(p.exists() for p in required_fixture_files), count=sum(p.exists() for p in required_fixture_files)))

    namespace_ok = True
    for p in (FIXTURE / "hermes_exec").rglob("*.json"):
        namespace_ok = namespace_ok and load_json(p).get("allowed_namespace") == "hermes_exec"
    for p in (FIXTURE / "codex_space").rglob("*.json"):
        namespace_ok = namespace_ok and load_json(p).get("allowed_namespace") == "codex_space"
    for p in (FIXTURE / "shared_handoff").rglob("*.json"):
        namespace_ok = namespace_ok and load_json(p).get("allowed_namespace") == "shared_handoff"
    checks.append(pass_check("namespace_write_zones_respected", namespace_ok))

    immutable_ok = all(load_json(p).get("immutable_after_publish") is True for p in required_fixture_files)
    checks.append(pass_check("immutable_after_publish_all_handles", immutable_ok))

    cross_fields = {"source_handle", "source_sha256", "used_for", "changed_judgment", "owner_namespace", "read_only_assertion"}
    cross_ok = True
    for p in required_fixture_files:
        data = load_json(p)
        for key in ("read_requests", "read_codex_handles", "read_hermes_handles"):
            for item in data.get(key, []):
                cross_ok = cross_ok and cross_fields.issubset(item.keys()) and item.get("read_only_assertion") is True
                source_path = FIXTURE / item["source_handle"]
                cross_ok = cross_ok and source_path.exists() and sha(source_path) == item["source_sha256"]
    checks.append(pass_check("cross_read_fields_and_sha_valid", cross_ok))

    latest = load_json(FIXTURE / "shared_handoff" / "99_LATEST_POINTERS.json")
    pointer_ok = True
    for pointer in latest["pointers"].values():
        target = FIXTURE / pointer["handle"]
        pointer_ok = pointer_ok and target.exists() and sha(target) == pointer["sha256"]
    checks.append(pass_check("latest_pointers_sha_valid", pointer_ok, pointer_count=len(latest["pointers"])))

    no_apply = all(load_json(p).get("promotion_status") == "HOLD" for p in required_fixture_files)
    checks.append(pass_check("promotion_hold_all_fixture_handles", no_apply))

    verdict = "PASS_SKILL_PACKAGE_AND_DUAL_LOG_LOCAL_FIXTURE_WITH_HOLD" if all(c["pass"] for c in checks) else "FAIL_SKILL_PACKAGE_AND_DUAL_LOG_LOCAL_FIXTURE"
    result = {
        "packet_id": "03_validation_skill_and_dual_log_fixture_v0",
        "verdict": verdict,
        "checks": checks,
        "checks_count": len(checks),
        "skill_path": str(SKILL),
        "fixture_path": str(FIXTURE),
        "next_safe_lane": "INSTALL_VECTORFL_SPACE_OPERATOR_SKILL_OR_RUN_REAL_DUAL_LOG_FIXTURE_WITH_HOLD_V0",
        "promotion_status": "HOLD"
    }
    out = BASE / "03_validation_skill_and_dual_log_fixture_v0.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
