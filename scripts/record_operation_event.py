from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from uuid import uuid4

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.events.event_append_guard import append_jsonl_locked

EVENTS_ROOT = REPO_ROOT / "runtime" / "events"
ENGINE_LEDGER = EVENTS_ROOT / "engine_event_ledger.jsonl"
FOLDER_ACTIVITY_ROOT = EVENTS_ROOT / "folder_activity"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a minimal operation event record.")
    parser.add_argument("--event-type", required=True)
    parser.add_argument("--target-ref", required=True)
    parser.add_argument("--source-doc-ref", default="")
    parser.add_argument("--ticket-ref", default="")
    parser.add_argument("--folder-ref", default="")
    parser.add_argument("--status", default="recorded")
    parser.add_argument("--notes", default="")
    parser.add_argument("--output-ref", default="")
    parser.add_argument("--derived-from", default="")
    parser.add_argument("--actor", default="codex")
    return parser.parse_args()


def build_event(args: argparse.Namespace) -> dict[str, object]:
    event = {
        "event_id": f"evt_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}",
        "event_type": args.event_type,
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "actor": args.actor,
        "target_ref": args.target_ref,
        "source_doc_ref": args.source_doc_ref,
        "ticket_ref": args.ticket_ref,
        "status": args.status,
        "notes": args.notes,
    }
    if args.folder_ref:
        event["folder_ref"] = args.folder_ref
    if args.output_ref:
        event["output_ref"] = args.output_ref
    if args.derived_from:
        event["derived_from"] = args.derived_from
    return event


def append_jsonl(path: Path, row: dict[str, object]) -> None:
    append_jsonl_locked(path, row)


def main() -> None:
    args = parse_args()
    event = build_event(args)
    append_jsonl(ENGINE_LEDGER, event)
    if args.folder_ref:
        folder_path = FOLDER_ACTIVITY_ROOT / f"{args.folder_ref}.folder_activity_log.jsonl"
        append_jsonl(folder_path, event)
    print(json.dumps(event, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
