from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a thin exploration observation stub in json/md form."
    )
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--source-type", default="structured_internal_doc")
    parser.add_argument("--observation-type", default="pattern_seen")
    parser.add_argument("--label", default="sample")
    args = parser.parse_args()

    root = Path("runtime/observer/exploration")
    json_dir = root / "json"
    md_dir = root / "md"
    json_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exploration_id = f"explore_{stamp}_{args.label}"

    payload = {
        "schema": "exploration_observation_stub_v1",
        "exploration_id": exploration_id,
        "session_id": args.session_id,
        "run_id": args.run_id,
        "observed_at": now_iso(),
        "source_ref": args.source_ref,
        "source_type": args.source_type,
        "observation_type": args.observation_type,
        "candidate_slots": [],
        "kept_as_core_candidate": [],
        "kept_as_outer_candidate": [],
        "deferred_items": [],
        "deferred_reason": "",
        "future_use_hint": "",
        "next_action_hint": "",
        "notes": "",
    }

    json_path = json_dir / f"{exploration_id}.json"
    md_path = md_dir / f"{exploration_id}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")

    md = "\n".join(
        [
            f"# {exploration_id}",
            "",
            "## context",
            f"- session_id: `{args.session_id}`",
            f"- run_id: `{args.run_id}`",
            f"- observed_at: `{payload['observed_at']}`",
            f"- source_ref: `{args.source_ref}`",
            f"- source_type: `{args.source_type}`",
            f"- observation_type: `{args.observation_type}`",
            "",
            "## readout",
            "- candidate_slots:",
            "- kept_as_core_candidate:",
            "- kept_as_outer_candidate:",
            "- deferred_items:",
            "- deferred_reason:",
            "",
            "## next",
            "- future_use_hint:",
            "- next_action_hint:",
            "- notes:",
            "",
        ]
    )
    md_path.write_text(md, encoding="utf-8")

    print(str(json_path))
    print(str(md_path))


if __name__ == "__main__":
    main()
