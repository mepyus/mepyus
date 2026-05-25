#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
FIXTURE = BASE / "fast_cross_inspection_fixture_run"
HERMES = FIXTURE / "hermes_exec"
CODEX = FIXTURE / "codex_space"
SHARED = FIXTURE / "shared_handoff"


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(FIXTURE))


def main():
    run_id = "fast_cross_inspection_fixture_20260524_v0"
    boundary = {
        "authority_mutation": "NO",
        "current_position_apply": "NO",
        "folder_tree_mutation": "NO",
        "promotion": "HOLD",
        "registry_mutation": "NO",
        "source_code_mutation": "NO"
    }

    hermes_artifact = HERMES / "20_HERMES_MERGE_EXECUTION_TRACE.json"
    codex_artifact = CODEX / "30_CODEX_MATURATION_PROPOSAL.json"
    hermes_card = HERMES / "90_HERMES_LATEST_SUMMARY_CARD.json"
    codex_card = CODEX / "90_CODEX_LATEST_SUMMARY_CARD.json"
    quick_board = SHARED / "90_QUICK_EXCHANGE_BOARD.json"
    latest = SHARED / "99_LATEST_POINTERS.json"

    write_json(hermes_artifact, {
        "packet_id": "20_HERMES_MERGE_EXECUTION_TRACE",
        "run_id": run_id,
        "writer_role": "HERMES",
        "allowed_namespace": "hermes_exec",
        "immutable_after_publish": True,
        "space_refs_used": ["compact_asset_index"],
        "execution_decision": "WITHHELD_FIXTURE_ONLY",
        "changed_judgment": "Hermes created a readable execution state for Codex.",
        "promotion_status": "HOLD"
    })
    write_json(codex_artifact, {
        "packet_id": "30_CODEX_MATURATION_PROPOSAL",
        "run_id": run_id,
        "writer_role": "CODEX",
        "allowed_namespace": "codex_space",
        "immutable_after_publish": True,
        "maturation_decision": "PROPOSE_SUMMARY_CHANNEL_ONLY",
        "changed_judgment": "Codex can read Hermes summary without touching Hermes namespace.",
        "promotion_status": "HOLD"
    })

    hermes_artifact_sha = sha(hermes_artifact)
    codex_artifact_sha = sha(codex_artifact)
    write_json(hermes_card, {
        "packet_id": "90_HERMES_LATEST_SUMMARY_CARD",
        "run_id": run_id,
        "writer_role": "HERMES",
        "owner_namespace": "hermes_exec",
        "allowed_namespace": "hermes_exec",
        "immutable_after_publish": True,
        "source_handle": rel(hermes_artifact),
        "source_sha256": hermes_artifact_sha,
        "latest_state": "HERMES_EXECUTION_TRACE_READY_FOR_CODEX",
        "used_for": "fast Codex inspection",
        "changed_judgment": "Hermes state can be inspected through summary card and quick board.",
        "next_for_other_actor": "CODEX_READ_SUMMARY_OR_REENTRY",
        "read_only_assertion": True,
        "promotion_status": "HOLD"
    })
    write_json(codex_card, {
        "packet_id": "90_CODEX_LATEST_SUMMARY_CARD",
        "run_id": run_id,
        "writer_role": "CODEX",
        "owner_namespace": "codex_space",
        "allowed_namespace": "codex_space",
        "immutable_after_publish": True,
        "source_handle": rel(codex_artifact),
        "source_sha256": codex_artifact_sha,
        "latest_state": "CODEX_MATURATION_PROPOSAL_READY_FOR_HERMES",
        "used_for": "fast Hermes inspection",
        "changed_judgment": "Codex state can be inspected through summary card and quick board.",
        "next_for_other_actor": "HERMES_RECORD_HOLD_RECEIPT",
        "read_only_assertion": True,
        "promotion_status": "HOLD"
    })

    hermes_card_sha = sha(hermes_card)
    codex_card_sha = sha(codex_card)
    write_json(latest, {
        "packet_id": "99_LATEST_POINTERS",
        "run_id": run_id,
        "writer_role": "HERMES_OR_CODEX_APPEND_VERSION",
        "allowed_namespace": "shared_handoff",
        "immutable_after_publish": True,
        "pointers": {
            "hermes_execution_trace": {"handle": rel(hermes_artifact), "sha256": hermes_artifact_sha},
            "codex_maturation_proposal": {"handle": rel(codex_artifact), "sha256": codex_artifact_sha},
            "hermes_summary_card": {"handle": rel(hermes_card), "sha256": hermes_card_sha},
            "codex_summary_card": {"handle": rel(codex_card), "sha256": codex_card_sha}
        },
        "promotion_status": "HOLD"
    })
    latest_sha = sha(latest)
    write_json(quick_board, {
        "packet_id": "90_QUICK_EXCHANGE_BOARD",
        "run_id": run_id,
        "board_version": "v0",
        "writer_role": "HERMES_OR_CODEX_APPEND_VERSION",
        "allowed_namespace": "shared_handoff",
        "immutable_after_publish": True,
        "last_updated_by": "CODEX_TEST_FIXTURE",
        "hermes_latest": {
            "summary_card_handle": rel(hermes_card),
            "summary_card_sha256": hermes_card_sha,
            "latest_artifact_handle": rel(hermes_artifact),
            "latest_artifact_sha256": hermes_artifact_sha,
            "latest_state": "HERMES_EXECUTION_TRACE_READY_FOR_CODEX",
            "changed_judgment": "Hermes has a trace ready for Codex inspection.",
            "next_for_other_actor": "CODEX_READ_SUMMARY_OR_REENTRY",
            "owner_namespace": "hermes_exec",
            "read_only_assertion": True
        },
        "codex_latest": {
            "summary_card_handle": rel(codex_card),
            "summary_card_sha256": codex_card_sha,
            "latest_artifact_handle": rel(codex_artifact),
            "latest_artifact_sha256": codex_artifact_sha,
            "latest_state": "CODEX_MATURATION_PROPOSAL_READY_FOR_HERMES",
            "changed_judgment": "Codex has a HOLD proposal ready for Hermes receipt.",
            "next_for_other_actor": "HERMES_RECORD_HOLD_RECEIPT",
            "owner_namespace": "codex_space",
            "read_only_assertion": True
        },
        "open_questions": [],
        "blocked_or_waiting_on": "USER_APPROVAL_REQUIRED_FOR_ANY_APPLY",
        "latest_pointer_ref": {"handle": rel(latest), "sha256": latest_sha},
        "next_safe_lane": "HERMES_OR_CODEX_READ_QUICK_BOARD_THEN_FOLLOW_POINTERS_WITH_HOLD",
        "boundary": boundary,
        "promotion_status": "HOLD"
    })

    print(json.dumps({
        "fixture": str(FIXTURE),
        "quick_board": str(quick_board),
        "files": sorted(str(p.relative_to(FIXTURE)) for p in FIXTURE.rglob("*.json"))
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

