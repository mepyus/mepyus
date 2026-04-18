#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCOPE_REF = "tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check bounded reconstruction supervisor invariants.")
    parser.add_argument("scope_ref", nargs="?", default=DEFAULT_SCOPE_REF)
    parser.add_argument("--receipt")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scope_ref = args.scope_ref
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "build_reconstruction_supervisor_surface.py"), "--scope-ref", scope_ref]
    if args.receipt:
        cmd.extend(["--receipt", args.receipt])
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    result = json.loads(proc.stdout)

    packet_path = REPO_ROOT / result["json_ref"]
    latest_path = REPO_ROOT / result["latest_json_ref"]
    packet = load_json(packet_path)
    latest = load_json(latest_path)

    checks = {
        "kind_is_reconstruction_surface": packet.get("kind") == "bounded_reconstruction_supervisor_surface_v1",
        "non_governing_guard": packet.get("guards", {}).get("not_decision_surface") is True,
        "read_only_guard": packet.get("guards", {}).get("read_only_reconstruction_only") is True,
        "pointer_backed_guard": packet.get("guards", {}).get("pointer_backed_surface") is True,
        "no_state_mutation": packet.get("guards", {}).get("state_mutation_performed") is False,
        "receipt_is_lineage_spine": packet.get("lineage", {}).get("receipt_ref") in packet.get("linked_receipts", []),
        "views_present": bool(packet.get("linked_views")),
        "view_role_not_mixed_with_sidecar": all(ref.startswith("runtime/views/") for ref in packet.get("linked_views", [])),
        "sidecar_role_not_mixed_with_views": all(ref.startswith("runtime/observer/exploration/") for ref in packet.get("linked_sidecars", [])),
        "latest_is_pointer_surface": latest.get("kind") == "bounded_reconstruction_supervisor_latest_pointer_v1",
        "latest_not_authoritative": latest.get("authoritative_note") == "latest is a surfaced pointer, not the authoritative source",
        "latest_points_to_packet": latest.get("authoritative_reconstruction_ref") == result["json_ref"],
        "selection_trace_present": isinstance(packet.get("selection_trace", {}).get("receipt_selection"), dict),
    }

    output = {
        "scope_ref": scope_ref,
        "passed": all(checks.values()),
        "checks": checks,
        "result": result,
        "packet_refs": {
            "packet_json_ref": result["json_ref"],
            "packet_md_ref": result["md_ref"],
            "latest_json_ref": result["latest_json_ref"],
            "latest_md_ref": result["latest_md_ref"],
        },
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
