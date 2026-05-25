#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
FIXTURE = BASE / "dual_log_fixture_run"
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
    run_id = "dual_log_fixture_20260524_v0"
    boundary = {
        "authority_mutation": "NO",
        "current_position_apply": "NO",
        "folder_tree_mutation": "NO",
        "promotion": "HOLD",
        "registry_mutation": "NO",
        "source_code_mutation": "NO"
    }

    manifest_path = SHARED / "00_RUN_MANIFEST.json"
    request_path = SHARED / "01_SPACE_REFERENCE_REQUEST.json"
    retrieval_path = CODEX / "10_CODEX_RETRIEVAL_RETURN.json"
    trace_path = HERMES / "20_HERMES_MERGE_EXECUTION_TRACE.json"
    reentry_path = SHARED / "21_CODEX_READABLE_REENTRY_INDEX.json"
    proposal_path = CODEX / "30_CODEX_MATURATION_PROPOSAL.json"
    receipt_path = HERMES / "40_HERMES_MATURATION_MERGE_RECEIPT.json"
    latest_path = SHARED / "99_LATEST_POINTERS.json"

    write_json(manifest_path, {
        "packet_id": "00_RUN_MANIFEST",
        "run_id": run_id,
        "writer_role": "HERMES_INITIALIZER",
        "allowed_namespace": "shared_handoff",
        "immutable_after_publish": True,
        "user_original_ref": "inline_fixture_original",
        "boundaries": boundary,
        "latest_pointer": rel(latest_path),
        "promotion_status": "HOLD"
    })

    write_json(request_path, {
        "packet_id": "01_SPACE_REFERENCE_REQUEST",
        "run_id": run_id,
        "writer_role": "HERMES",
        "allowed_namespace": "shared_handoff",
        "immutable_after_publish": True,
        "fresh_space_reference_needed": True,
        "task": "Retrieve bounded space refs for a fixture Hermes execution.",
        "does_not_mutate_handles": [],
        "promotion_status": "HOLD"
    })

    request_sha = sha(request_path)
    write_json(retrieval_path, {
        "packet_id": "10_CODEX_RETRIEVAL_RETURN",
        "run_id": run_id,
        "writer_role": "CODEX",
        "allowed_namespace": "codex_space",
        "immutable_after_publish": True,
        "read_requests": [
            {
                "source_handle": rel(request_path),
                "source_sha256": request_sha,
                "used_for": "space retrieval fixture input",
                "changed_judgment": "fresh space reference is needed before Hermes merge",
                "owner_namespace": "shared_handoff",
                "read_only_assertion": True
            }
        ],
        "selected_space_material": ["compact_layer_map", "compact_asset_index"],
        "rejected_space_material": ["broad_raw_history"],
        "changed_judgment_for_hermes": "Use compact controls only for fixture merge.",
        "promotion_status": "HOLD"
    })

    retrieval_sha = sha(retrieval_path)
    write_json(trace_path, {
        "packet_id": "20_HERMES_MERGE_EXECUTION_TRACE",
        "run_id": run_id,
        "writer_role": "HERMES",
        "allowed_namespace": "hermes_exec",
        "immutable_after_publish": True,
        "read_codex_handles": [
            {
                "source_handle": rel(retrieval_path),
                "source_sha256": retrieval_sha,
                "used_for": "merge original + retrieved space + model reasoning",
                "changed_judgment": "Codex retrieval bounded Hermes execution setup",
                "owner_namespace": "codex_space",
                "read_only_assertion": True
            }
        ],
        "space_refs_used": ["compact_layer_map", "compact_asset_index"],
        "model_merge_judgment": "Fixture execution should remain HOLD and produce reentry.",
        "execution_decision": "WITHHELD_REAL_EXECUTION_LOCAL_FIXTURE_ONLY",
        "withheld_actions": ["authority_apply", "registry_mutation", "folder_move"],
        "promotion_status": "HOLD"
    })

    trace_sha = sha(trace_path)
    write_json(reentry_path, {
        "packet_id": "21_CODEX_READABLE_REENTRY_INDEX",
        "run_id": run_id,
        "writer_role": "HERMES",
        "allowed_namespace": "shared_handoff",
        "immutable_after_publish": True,
        "read_hermes_handles": [
            {
                "source_handle": rel(trace_path),
                "source_sha256": trace_sha,
                "used_for": "Codex maturation reentry",
                "changed_judgment": "Hermes trace is ready for Codex space maturation check",
                "owner_namespace": "hermes_exec",
                "read_only_assertion": True
            }
        ],
        "codex_questions": ["Should fixture pattern be proposed for future indexing?"],
        "next_safe_lane": "CODEX_MATURATION_PROPOSAL_OR_HOLD",
        "promotion_status": "HOLD"
    })

    reentry_sha = sha(reentry_path)
    write_json(proposal_path, {
        "packet_id": "30_CODEX_MATURATION_PROPOSAL",
        "run_id": run_id,
        "writer_role": "CODEX",
        "allowed_namespace": "codex_space",
        "immutable_after_publish": True,
        "read_hermes_handles": [
            {
                "source_handle": rel(reentry_path),
                "source_sha256": reentry_sha,
                "used_for": "HOLD-only maturation proposal",
                "changed_judgment": "Fixture validates namespace separation and reentry shape",
                "owner_namespace": "shared_handoff",
                "read_only_assertion": True
            }
        ],
        "maturation_decision": "PROPOSE_PATTERN_ONLY",
        "space_assets_to_reindex": [rel(manifest_path), rel(retrieval_path), rel(trace_path), rel(reentry_path)],
        "rejected_maturation_options": ["apply_authority", "mutate_registry"],
        "gemini_via_codex_script_used": "NO",
        "promotion_status": "HOLD"
    })

    proposal_sha = sha(proposal_path)
    write_json(receipt_path, {
        "packet_id": "40_HERMES_MATURATION_MERGE_RECEIPT",
        "run_id": run_id,
        "writer_role": "HERMES",
        "allowed_namespace": "hermes_exec",
        "immutable_after_publish": True,
        "read_codex_handles": [
            {
                "source_handle": rel(proposal_path),
                "source_sha256": proposal_sha,
                "used_for": "record Codex proposal as evidence only",
                "changed_judgment": "proposal accepted as HOLD evidence, not applied",
                "owner_namespace": "codex_space",
                "read_only_assertion": True
            }
        ],
        "applied": False,
        "authority_effect": "NO_AUTHORITY_MUTATION",
        "promotion_status": "HOLD"
    })

    receipt_sha = sha(receipt_path)
    write_json(latest_path, {
        "packet_id": "99_LATEST_POINTERS",
        "run_id": run_id,
        "writer_role": "HERMES_OR_CODEX_APPEND_VERSION",
        "allowed_namespace": "shared_handoff",
        "immutable_after_publish": True,
        "pointers": {
            "manifest": {"handle": rel(manifest_path), "sha256": sha(manifest_path)},
            "space_reference_request": {"handle": rel(request_path), "sha256": request_sha},
            "codex_retrieval_return": {"handle": rel(retrieval_path), "sha256": retrieval_sha},
            "hermes_execution_trace": {"handle": rel(trace_path), "sha256": trace_sha},
            "codex_readable_reentry": {"handle": rel(reentry_path), "sha256": reentry_sha},
            "codex_maturation_proposal": {"handle": rel(proposal_path), "sha256": proposal_sha},
            "hermes_maturation_receipt": {"handle": rel(receipt_path), "sha256": receipt_sha}
        },
        "promotion_status": "HOLD"
    })

    print(json.dumps({
        "fixture": str(FIXTURE),
        "files": sorted(str(p.relative_to(FIXTURE)) for p in FIXTURE.rglob("*.json"))
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

