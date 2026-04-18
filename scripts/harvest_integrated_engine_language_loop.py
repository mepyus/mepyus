#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


FIELD_PATTERNS = {
    "internal_phrase": re.compile(r"internal phrase or signal observed:\s*`?([^`\n]+)`?", re.IGNORECASE),
    "source_context": re.compile(r"source context where it appeared:\s*(.+)", re.IGNORECASE),
    "internal_meaning": re.compile(r"internal meaning / operational role:\s*(.+)", re.IGNORECASE),
    "korean_candidate": re.compile(r"koreanization candidate, not final ui copy:\s*(.+)", re.IGNORECASE),
    "korean_preservation": re.compile(r"korean preservation requirement:\s*(.+)", re.IGNORECASE),
    "risky_korean_flattening": re.compile(r"risky korean flattening to avoid:\s*(.+)", re.IGNORECASE),
    "user_operation_help": re.compile(r"why this helps the user operate:\s*(.+)", re.IGNORECASE),
    "meaning_lost_if_shortened": re.compile(r"what meaning gets lost if shortened:\s*(.+)", re.IGNORECASE),
    "human_line": re.compile(r"human-readable line, not final wording:\s*(.+)", re.IGNORECASE),
    "connection": re.compile(r"repeated connection it belongs to:\s*(.+)", re.IGNORECASE),
    "axis": re.compile(r"emerging axis candidate:\s*(.+)", re.IGNORECASE),
    "surface": re.compile(r"surface exposure note:\s*(.+)", re.IGNORECASE),
    "external_support": re.compile(r"external expression support needed, if any:\s*(.+)", re.IGNORECASE),
    "do_not_flatten": re.compile(r"what must not be flattened:\s*(.+)", re.IGNORECASE),
    "next_question": re.compile(r"next reread question:\s*(.+)", re.IGNORECASE),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def latest_loop_dir(runtime_root: Path) -> Path:
    loops_root = runtime_root / "language_loops"
    candidates = [path for path in loops_root.glob("language_loop_*") if path.is_dir()]
    if not candidates:
        raise SystemExit(f"no language loops found under {loops_root}")
    return sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True)[0]


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).strip(" -")


def extract_fields(text: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    current: Dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("|") and line.endswith("|"):
            parts = [normalize(part.strip(" `")) for part in line.strip("|").split("|")]
            lower = [part.lower() for part in parts]
            if not parts or any(set(part) <= {"-"} for part in parts if part):
                continue
            if any("internal" in part and "phrase" in part for part in lower):
                continue
            if len(parts) >= 12:
                rows.append(
                    {
                        "internal_phrase": parts[0],
                        "source_context": parts[1],
                        "internal_meaning": parts[2],
                        "korean_candidate": parts[3],
                        "korean_preservation": parts[4],
                        "risky_korean_flattening": parts[5],
                        "user_operation_help": parts[6],
                        "meaning_lost_if_shortened": parts[7],
                        "connection": parts[8],
                        "axis": parts[9],
                        "surface": parts[10],
                        "external_support": parts[11],
                        "next_question": parts[12] if len(parts) > 12 else "",
                    }
                )
                continue
            if len(parts) >= 7:
                rows.append(
                    {
                        "internal_phrase": parts[0],
                        "human_line": parts[1],
                        "connection": parts[2],
                        "axis": parts[3],
                        "surface": parts[4],
                        "do_not_flatten": parts[5],
                        "next_question": parts[6],
                    }
                )
                continue
        matched = False
        for field, pattern in FIELD_PATTERNS.items():
            match = pattern.search(line)
            if not match:
                continue
            if field == "internal_phrase" and current:
                rows.append(current)
                current = {}
            current[field] = normalize(match.group(1))
            matched = True
            break
        if not matched:
            continue
    if current:
        rows.append(current)
    return rows


def snippets(values: Iterable[str], limit: int = 8) -> List[str]:
    result = []
    seen = set()
    for value in values:
        item = normalize(value)
        if not item or item in seen:
            continue
        seen.add(item)
        result.append(item)
        if len(result) >= limit:
            break
    return result


def top_counter(values: Iterable[str], limit: int = 10) -> List[Dict[str, Any]]:
    counter = Counter(normalize(value) for value in values if normalize(value))
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def harvest_loop(loop_dir: Path, runtime_root: Path) -> Dict[str, Any]:
    loop = read_json(loop_dir / "loop.json")
    rows: List[Dict[str, Any]] = []
    session_summaries = []
    for item in loop.get("sessions", []):
        session_id = str(item.get("session_id") or "").strip()
        structured_path = runtime_root.parent / str(item.get("structured_return_path") or "")
        operator_path = runtime_root.parent / str(item.get("operator_report_path") or "")
        structured = read_json(structured_path)
        result_text = str(structured.get("result_summary") or item.get("result_preview") or "")
        operator_text = read_text(operator_path)
        extracted = extract_fields(result_text)
        for row in extracted:
            row["session_id"] = session_id
            row["iteration"] = item.get("iteration")
            rows.append(row)
        session_summaries.append(
            {
                "iteration": item.get("iteration"),
                "session_id": session_id,
                "status": item.get("status"),
                "mark": item.get("mark"),
                "context_refs": item.get("context_refs") or [],
                "operator_report_path": item.get("operator_report_path"),
                "extracted_count": len(extracted),
                "operator_report_has_surface_split": "## Surface Split" in operator_text,
            }
        )

    grouped_by_axis: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    grouped_by_connection: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped_by_axis[row.get("axis", "unclassified")].append(row)
        grouped_by_connection[row.get("connection", "unclassified")].append(row)

    harvest = {
        "schema_version": "integrated_engine_language_loop_harvest_v0",
        "loop_id": loop.get("loop_id") or loop_dir.name,
        "source_loop_dir": str(loop_dir),
        "created_at": utc_now(),
        "session_count": len(loop.get("sessions", [])),
        "extracted_row_count": len(rows),
        "sessions": session_summaries,
        "top_internal_phrases": top_counter(row.get("internal_phrase", "") for row in rows),
        "top_korean_candidates": top_counter(row.get("korean_candidate", "") for row in rows),
        "top_risky_korean_flattening": top_counter(row.get("risky_korean_flattening", "") for row in rows),
        "top_connections": top_counter(row.get("connection", "") for row in rows),
        "top_axes": top_counter(row.get("axis", "") for row in rows),
        "rows": rows,
        "axis_groups": {
            axis: {
                "count": len(items),
                "sample_lines": snippets((item.get("human_line", "") for item in items), limit=5),
                "korean_candidates": snippets((item.get("korean_candidate", "") for item in items), limit=5),
                "korean_preservation": snippets((item.get("korean_preservation", "") for item in items), limit=5),
                "risky_korean_flattening": snippets((item.get("risky_korean_flattening", "") for item in items), limit=5),
                "user_operation_help": snippets((item.get("user_operation_help", "") for item in items), limit=5),
                "do_not_flatten": snippets((item.get("do_not_flatten", "") for item in items), limit=5),
                "next_questions": snippets((item.get("next_question", "") for item in items), limit=5),
            }
            for axis, items in grouped_by_axis.items()
        },
        "connection_groups": {
            connection: {
                "count": len(items),
                "sample_phrases": snippets((item.get("internal_phrase", "") for item in items), limit=5),
                "axes": snippets((item.get("axis", "") for item in items), limit=5),
            }
            for connection, items in grouped_by_connection.items()
        },
        "boundary": {
            "harvest_only": True,
            "no_ui_copy_patch": True,
            "no_final_glossary": True,
            "no_auto_promotion": True,
        },
    }
    return harvest


def write_harvest_md(path: Path, harvest: Dict[str, Any]) -> None:
    lines: List[str] = [
        "# Integrated Engine Language Loop Harvest",
        "",
        f"- loop_id: `{harvest.get('loop_id')}`",
        f"- session_count: `{harvest.get('session_count')}`",
        f"- extracted_row_count: `{harvest.get('extracted_row_count')}`",
        f"- created_at: `{harvest.get('created_at')}`",
        "",
        "## Reading",
        "",
        "This harvest collects repeated internal-language signals from loop outputs and groups them into Koreanization data plus line / connection / axis material.",
        "It is not UI copy, not a final glossary, and not a promotion gate.",
        "",
        "## Top Axes",
        "",
    ]
    for item in harvest.get("top_axes", []):
        lines.append(f"- `{item['value']}` ({item['count']})")
    lines.extend(["", "## Top Koreanization Candidates", ""])
    for item in harvest.get("top_korean_candidates", []):
        lines.append(f"- `{item['value']}` ({item['count']})")
    lines.extend(["", "## Top Risky Korean Flattening", ""])
    for item in harvest.get("top_risky_korean_flattening", []):
        lines.append(f"- `{item['value']}` ({item['count']})")
    lines.extend(["", "## Top Connections", ""])
    for item in harvest.get("top_connections", []):
        lines.append(f"- `{item['value']}` ({item['count']})")
    lines.extend(["", "## Axis Groups", ""])
    for axis, group in harvest.get("axis_groups", {}).items():
        lines.extend([f"### {axis}", "", f"- count: `{group.get('count')}`", ""])
        sample_lines = group.get("sample_lines") or []
        if sample_lines:
            lines.append("Sample human-readable lines:")
            for line in sample_lines:
                lines.append(f"- {line}")
            lines.append("")
        korean_candidates = group.get("korean_candidates") or []
        if korean_candidates:
            lines.append("Koreanization candidates:")
            for line in korean_candidates:
                lines.append(f"- {line}")
            lines.append("")
        korean_preservation = group.get("korean_preservation") or []
        if korean_preservation:
            lines.append("Korean preservation requirements:")
            for note in korean_preservation:
                lines.append(f"- {note}")
            lines.append("")
        risky_korean_flattening = group.get("risky_korean_flattening") or []
        if risky_korean_flattening:
            lines.append("Risky Korean flattening to avoid:")
            for note in risky_korean_flattening:
                lines.append(f"- {note}")
            lines.append("")
        user_operation_help = group.get("user_operation_help") or []
        if user_operation_help:
            lines.append("Why this helps user operation:")
            for note in user_operation_help:
                lines.append(f"- {note}")
            lines.append("")
        do_not_flatten = group.get("do_not_flatten") or []
        if do_not_flatten:
            lines.append("Do-not-flatten notes:")
            for note in do_not_flatten:
                lines.append(f"- {note}")
            lines.append("")
        next_questions = group.get("next_questions") or []
        if next_questions:
            lines.append("Next reread questions:")
            for question in next_questions:
                lines.append(f"- {question}")
            lines.append("")
    lines.extend(["## Sessions", ""])
    for item in harvest.get("sessions", []):
        lines.extend(
            [
                f"- `{item.get('session_id')}` iteration `{item.get('iteration')}` status `{item.get('status')}` extracted `{item.get('extracted_count')}`",
                f"  - operator_report: `{item.get('operator_report_path')}`",
            ]
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Harvest only.",
            "- No UI copy patch.",
            "- No final glossary.",
            "- No automatic promotion.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Harvest line / connection / axis material from an integrated-engine internal-language loop.")
    parser.add_argument("--runtime-root", default="runtime")
    parser.add_argument("--loop-id", default="")
    args = parser.parse_args()

    runtime_root = Path(args.runtime_root)
    loop_dir = runtime_root / "language_loops" / args.loop_id if args.loop_id else latest_loop_dir(runtime_root)
    if not loop_dir.exists():
        raise SystemExit(f"loop dir not found: {loop_dir}")

    harvest = harvest_loop(loop_dir, runtime_root)
    write_json(loop_dir / "harvest.json", harvest)
    write_harvest_md(loop_dir / "harvest.md", harvest)
    print(json.dumps({"ok": True, "loop_id": harvest.get("loop_id"), "harvest_path": str(loop_dir / "harvest.md"), "extracted_row_count": harvest.get("extracted_row_count")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
