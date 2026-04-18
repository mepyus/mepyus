from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFESTS_DIR = REPO_ROOT / "runtime" / "manifests"
CONTRACTS_DIR = REPO_ROOT / "runtime" / "contracts"


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    pilot_current = _load_json(MANIFESTS_DIR / "vectorfl_paper_pilot_current_v0.json")
    status_board = _load_json(CONTRACTS_DIR / "vectorfl_paper_weekend_pilot_status_board_v0.json")
    absorption_package = _load_json(MANIFESTS_DIR / "vectorfl_paper_absorption_package_v0.json")
    actual_export_slot = _load_json(MANIFESTS_DIR / "vectorfl_paper_actual_export_host_record_slot_v0.json")

    promotion_ready = (
        status_board["current_state"].get("actual_export_slot_ready")
        and status_board["current_state"].get("actual_export_swap_ready")
        and status_board["current_state"].get("absorption_package_ready")
        and actual_export_slot.get("current_state") != "waiting_for_actual_export"
    )

    out = {
        "promotion_candidate_id": "vectorfl_paper_proper_promotion_candidate_v0",
        "promotion_ready": promotion_ready,
        "blocking_reason": (
            None
            if promotion_ready
            else "actual exported host record has not yet replaced the placeholder slot occupant"
        ),
        "pilot_refs": pilot_current["canonical_refs"],
        "absorption_targets": absorption_package["absorption_targets"],
        "naming_rule": absorption_package["naming_rule"],
        "final_gate": absorption_package["final_gate"],
    }
    out_path = MANIFESTS_DIR / "vectorfl_paper_proper_promotion_candidate_v0.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"promotion_candidate_path": str(out_path), "promotion_ready": promotion_ready}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
