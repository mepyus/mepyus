#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
FIXTURE = BASE / "fast_cross_inspection_fixture_run"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, passed, **extra):
    item = {"check": name, "pass": bool(passed)}
    item.update(extra)
    return item


def main():
    quick = FIXTURE / "shared_handoff" / "90_QUICK_EXCHANGE_BOARD.json"
    latest = FIXTURE / "shared_handoff" / "99_LATEST_POINTERS.json"
    hermes_card = FIXTURE / "hermes_exec" / "90_HERMES_LATEST_SUMMARY_CARD.json"
    codex_card = FIXTURE / "codex_space" / "90_CODEX_LATEST_SUMMARY_CARD.json"
    required = [quick, latest, hermes_card, codex_card]

    checks = []
    checks.append(check("quick_channel_handles_present", all(p.exists() for p in required), count=sum(p.exists() for p in required)))

    namespace_ok = True
    for p in (FIXTURE / "hermes_exec").glob("*.json"):
        namespace_ok = namespace_ok and load_json(p).get("allowed_namespace") == "hermes_exec"
    for p in (FIXTURE / "codex_space").glob("*.json"):
        namespace_ok = namespace_ok and load_json(p).get("allowed_namespace") == "codex_space"
    for p in (FIXTURE / "shared_handoff").glob("*.json"):
        namespace_ok = namespace_ok and load_json(p).get("allowed_namespace") == "shared_handoff"
    checks.append(check("namespace_write_zones_respected", namespace_ok))

    board = load_json(quick)
    required_board = {
        "run_id", "board_version", "last_updated_by", "hermes_latest", "codex_latest",
        "open_questions", "blocked_or_waiting_on", "latest_pointer_ref", "next_safe_lane",
        "boundary", "promotion_status"
    }
    checks.append(check("quick_board_required_sections_present", required_board.issubset(board.keys())))

    latest_entry_fields = {
        "summary_card_handle", "summary_card_sha256", "latest_artifact_handle", "latest_artifact_sha256",
        "latest_state", "changed_judgment", "next_for_other_actor", "owner_namespace", "read_only_assertion"
    }
    entries_ok = latest_entry_fields.issubset(board["hermes_latest"].keys()) and latest_entry_fields.issubset(board["codex_latest"].keys())
    checks.append(check("latest_entry_fields_present", entries_ok))

    sha_ok = True
    for side in ("hermes_latest", "codex_latest"):
        entry = board[side]
        summary = FIXTURE / entry["summary_card_handle"]
        artifact = FIXTURE / entry["latest_artifact_handle"]
        sha_ok = sha_ok and summary.exists() and artifact.exists()
        sha_ok = sha_ok and sha(summary) == entry["summary_card_sha256"]
        sha_ok = sha_ok and sha(artifact) == entry["latest_artifact_sha256"]
        sha_ok = sha_ok and entry["read_only_assertion"] is True
    pointer = FIXTURE / board["latest_pointer_ref"]["handle"]
    sha_ok = sha_ok and pointer.exists() and sha(pointer) == board["latest_pointer_ref"]["sha256"]
    checks.append(check("quick_board_sha_links_valid", sha_ok))

    latest_data = load_json(latest)
    pointer_ok = True
    for item in latest_data["pointers"].values():
        target = FIXTURE / item["handle"]
        pointer_ok = pointer_ok and target.exists() and sha(target) == item["sha256"]
    checks.append(check("latest_pointer_sha_links_valid", pointer_ok, pointer_count=len(latest_data["pointers"])))

    cards_ok = True
    card_fields = {
        "source_handle", "source_sha256", "used_for", "changed_judgment",
        "owner_namespace", "read_only_assertion", "next_for_other_actor"
    }
    for card in (hermes_card, codex_card):
        data = load_json(card)
        source = FIXTURE / data["source_handle"]
        cards_ok = cards_ok and card_fields.issubset(data.keys())
        cards_ok = cards_ok and source.exists() and sha(source) == data["source_sha256"]
        cards_ok = cards_ok and data["read_only_assertion"] is True
    checks.append(check("summary_card_cross_read_fields_valid", cards_ok))

    hold_ok = board["promotion_status"] == "HOLD" and all(load_json(p).get("promotion_status") == "HOLD" for p in FIXTURE.rglob("*.json"))
    checks.append(check("promotion_hold_all_fast_channel_files", hold_ok))

    verdict = "PASS_FAST_CROSS_INSPECTION_CHANNEL_WITH_HOLD" if all(c["pass"] for c in checks) else "FAIL_FAST_CROSS_INSPECTION_CHANNEL"
    result = {
        "packet_id": "03_validation_fast_cross_inspection_channel_v0",
        "verdict": verdict,
        "checks": checks,
        "checks_count": len(checks),
        "fixture_path": str(FIXTURE),
        "quick_board": str(quick),
        "next_safe_lane": "ABSORB_FAST_CROSS_INSPECTION_CHANNEL_INTO_SPACE_OPERATOR_SKILL_OR_USE_IN_REAL_RUN_WITH_HOLD_V0",
        "promotion_status": "HOLD"
    }
    out = BASE / "03_validation_fast_cross_inspection_channel_v0.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
