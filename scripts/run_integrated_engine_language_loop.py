#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.vectorfl_integrated_engine_api import (
    mark_integrated_engine_cli_session,
    run_integrated_engine_cli_session,
)


DEFAULT_CONTEXT_SETS = [
    [
        "docs/reports/integrated_engine_cli_on_top_shared_language_grammar_reread_v0.md",
        "docs/reports/integrated_engine_cli_on_top_operator_report_grammar_trial_v0.md",
    ],
    [
        "docs/reports/integrated_engine_cli_on_top_current_operating_state_v0.md",
        "docs/reports/integrated_engine_surface_exposure_and_shared_language_boundary_v0.md",
    ],
    [
        "docs/reports/integrated_engine_line_connection_axis_to_shared_language_map_v0.md",
        "docs/reports/integrated_engine_internal_language_grammar_candidate_v0.md",
    ],
    [
        "docs/reports/integrated_engine_cli_operator_report_loop_patch_note_v0.md",
        "docs/reports/integrated_engine_shared_operational_language_growth_note_v0.md",
    ],
]


PROMPT_TEMPLATE = """Read the bounded context as a Koreanization data collection loop for integrated-engine internal language.

Do not modify files.
Do not propose UI copy.
Do not create a final glossary.
Do not promote features.

Return compact data in this shape:
- internal phrase or signal observed
- source context where it appeared
- internal meaning / operational role
- Koreanization candidate, not final UI copy
- Korean preservation requirement
- risky Korean flattening to avoid
- why this helps the user operate
- what meaning gets lost if shortened
- repeated connection it belongs to
- emerging axis candidate
- surface exposure note: user / vectorfl / engine
- external expression support needed, if any
- next reread question
- suggested next use: validation target
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_id(value: str) -> str:
    return value.replace(":", "").replace("-", "").replace(".", "").replace("Z", "Z")


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_loop_index(path: Path, loop_record: Dict[str, Any]) -> None:
    lines: List[str] = [
        "# Integrated Engine Internal Language Loop Index",
        "",
        f"- loop_id: `{loop_record['loop_id']}`",
        f"- status: `{loop_record['status']}`",
        f"- started_at: `{loop_record['started_at']}`",
        f"- ended_at: `{loop_record.get('ended_at') or ''}`",
        f"- requested_count: `{loop_record['requested_count']}`",
        f"- completed_count: `{loop_record['completed_count']}`",
        "",
        "## Purpose",
        "",
        "Collect repeated internal-language signals and convert them into Koreanization data for operating language without opening UI copy or glossary work.",
        "",
        "## Sessions",
        "",
    ]
    for item in loop_record.get("sessions", []):
        lines.extend(
            [
                f"### {item.get('iteration')} / {item.get('session_id')}",
                "",
                f"- status: `{item.get('status')}`",
                f"- mark: `{item.get('mark')}`",
                f"- session_path: `{item.get('session_path')}`",
                f"- structured_return_path: `{item.get('structured_return_path')}`",
                f"- operator_report_path: `{item.get('operator_report_path')}`",
                f"- context_refs: {', '.join('`' + ref + '`' for ref in item.get('context_refs', []))}",
                "",
                "Return preview:",
                "",
                "```text",
                (item.get("result_preview") or "no preview")[:1000],
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## Boundary",
            "",
            "- This loop produces Koreanization data material only.",
            "- It does not patch UI wording.",
            "- It does not create a final glossary.",
            "- It does not ingest or promote deposits automatically.",
            "- It does not add Gemini adapter behavior.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_context_sets(value: str) -> List[List[str]]:
    if not value.strip():
        return DEFAULT_CONTEXT_SETS
    groups: List[List[str]] = []
    for chunk in value.split(";"):
        refs = [part.strip() for part in chunk.split(",") if part.strip()]
        if refs:
            groups.append(refs)
    return groups or DEFAULT_CONTEXT_SETS


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a bounded internal-language Koreanization data loop through the existing CLI session path.")
    parser.add_argument("--runtime-root", default="runtime")
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--mark", default="validation_target")
    parser.add_argument("--loop-id", default="", help="Optional caller-provided loop id for background UI runs.")
    parser.add_argument(
        "--context-sets",
        default="",
        help="Optional ';' separated context groups, each group comma-separated.",
    )
    args = parser.parse_args()

    if args.count < 1:
        raise SystemExit("--count must be >= 1")

    runtime_root = Path(args.runtime_root)
    repo_root = runtime_root.resolve().parent
    context_sets = parse_context_sets(args.context_sets)
    loop_id = args.loop_id.strip() or ("language_loop_" + safe_id(utc_now()))
    loop_dir = repo_root / "runtime" / "language_loops" / loop_id
    loop_record: Dict[str, Any] = {
        "schema_version": "integrated_engine_internal_language_koreanization_loop_v1",
        "loop_id": loop_id,
        "status": "running",
        "started_at": utc_now(),
        "ended_at": "",
        "requested_count": args.count,
        "completed_count": 0,
        "sessions": [],
        "boundary": {
            "translation_data_only": True,
            "no_ui_copy_patch": True,
            "no_final_glossary": True,
            "no_auto_ingestion": True,
            "no_extension_promotion": True,
        },
    }
    write_json(loop_dir / "loop.json", loop_record)

    for index in range(args.count):
        iteration = index + 1
        context_refs = context_sets[index % len(context_sets)]
        payload = {
            "backend_kind": "codex",
            "task_type": "reread",
            "requested_by_surface": "user_surface",
            "requested_by_page": "scripts/run_integrated_engine_language_loop.py",
            "purpose_text": f"Internal language Koreanization data loop {iteration}: collect Korean operating-language data from bounded context.",
            "bounded_context_refs": "\n".join(context_refs),
            "prompt_payload": PROMPT_TEMPLATE,
            "timeout_seconds": args.timeout,
        }
        result = run_integrated_engine_cli_session(runtime_root, payload)
        session = result.get("session") or {}
        structured = result.get("structured_return") or {}
        mark_result = mark_integrated_engine_cli_session(runtime_root, {"session_id": session.get("session_id"), "mark": args.mark})
        marked_session = mark_result.get("session") or session
        session_item = {
            "iteration": iteration,
            "session_id": marked_session.get("session_id"),
            "status": marked_session.get("status"),
            "mark": args.mark,
            "session_path": result.get("session_path"),
            "structured_return_path": marked_session.get("structured_return_path"),
            "operator_report_path": marked_session.get("operator_report_path"),
            "context_refs": context_refs,
            "result_preview": structured.get("result_summary") or marked_session.get("result_summary") or "",
        }
        loop_record["sessions"].append(session_item)
        loop_record["completed_count"] = len(loop_record["sessions"])
        write_json(loop_dir / "loop.json", loop_record)
        write_loop_index(loop_dir / "index.md", loop_record)
        print(json.dumps(session_item, ensure_ascii=False))
        if args.sleep and iteration < args.count:
            time.sleep(args.sleep)

    loop_record["status"] = "completed"
    loop_record["ended_at"] = utc_now()
    write_json(loop_dir / "loop.json", loop_record)
    write_loop_index(loop_dir / "index.md", loop_record)
    print(json.dumps({"ok": True, "loop_id": loop_id, "loop_dir": str(loop_dir), "completed_count": loop_record["completed_count"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
