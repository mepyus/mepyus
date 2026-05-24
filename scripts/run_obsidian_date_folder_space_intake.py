#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OBSIDIAN_BASE = Path(
    "/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_"
)
OUTPUT_DIR = ROOT / "app/work/space-skill-sandbox/outputs"
RUNS_DIR = ROOT / "app/work/space-skill-sandbox/runs"
RUNTIME_DIR = ROOT / "runtime/obsidian_date_folder_intake"


@dataclass(frozen=True)
class SourceFileSnapshot:
    path: str
    name: str
    line_count: int
    char_count: int
    headings: list[str]
    evidence_lines: list[str]


@dataclass(frozen=True)
class SignalCandidate:
    signal_id: str
    name: str
    score: int
    matched_terms: list[str]
    evidence: list[str]


CAMERA_RULES: dict[str, tuple[str, tuple[str, ...]]] = {
    "process_trace_camera": (
        "Process-Trace Camera",
        ("과정", "흔적", "피드백", "어긋남", "회수", "자동화", "실행"),
    ),
    "origin_derivative_camera": (
        "Origin / Derivative Camera",
        ("공간", "모체", "파생", "Camera", "Lens", "프로그램", "repo asset"),
    ),
    "reservoir_sandbox_camera": (
        "Reservoir / Sandbox Camera",
        ("저수지", "펌프", "샌드박스", "파생본", "원본", "회수로", "Attachment"),
    ),
    "workplace_process_camera": (
        "Workplace / Process Camera",
        ("회사", "직장", "공장", "오피스", "업무", "병목", "담당자"),
    ),
    "external_tool_recovery_camera": (
        "External Tool / Recovery Camera",
        ("Codex", "Gemini", "CLI", "worker", "외부도구", "패키지", "Return-to-Space"),
    ),
}

LENS_RULES: dict[str, tuple[str, tuple[str, ...]]] = {
    "thin_plan_thick_recovery_lens": (
        "Thin Plan / Thick Recovery Lens",
        ("얇은 계획", "두꺼운 회수", "피드백", "어긋남", "다음 작업 조건"),
    ),
    "pipeline_first_lens": (
        "Pipeline-First Lens",
        ("파이프라인", "흐름", "변화 지점", "Line", "Axis", "Camera", "Lens"),
    ),
    "origin_to_derivative_lens": (
        "Origin-to-Derivative Lens",
        ("공간은 기능이 아니라", "모체", "프로그램은", "파생", "repo asset"),
    ),
    "pump_ready_sandbox_lens": (
        "Pump-Ready Sandbox Lens",
        ("펌프", "접속부", "Temporary Pump", "Sandbox", "Derivative", "Return Channel"),
    ),
    "no_direct_promotion_boundary_lens": (
        "No-Direct-Promotion Boundary Lens",
        ("하지 않는다", "만들지 않는다", "강제하지 않는다", "대체", "Watch", "원본은"),
    ),
}

PLACEMENT_RULES: dict[str, tuple[str, tuple[str, ...]]] = {
    "return_to_space_value": (
        "RETURN_TO_SPACE_VALUE",
        ("공간", "판단", "회수", "조건", "기준", "모체", "숙성"),
    ),
    "external_tool_application": (
        "EXTERNAL_TOOL_APPLICATION",
        ("Codex", "Gemini", "CLI", "worker", "외부도구", "작업 패키지", "실행"),
    ),
    "sandbox_test_candidate": (
        "SANDBOX_TEST_CANDIDATE",
        ("샌드박스", "테스트", "파생본", "이미테이션", "실험", "카드"),
    ),
    "watch_or_boundary": (
        "WATCH_OR_BOUNDARY",
        ("Watch", "하지 않는다", "만들지 않는다", "강제하지 않는다", "착각", "대체"),
    ),
}


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    date_folder = _resolve_date_folder(args.date, args.folder, args.obsidian_base)
    if not date_folder.exists() or not date_folder.is_dir():
        print(f"date folder not found: {date_folder}", file=sys.stderr)
        return 2

    snapshots = [_snapshot_file(path) for path in sorted(date_folder.glob("*.md"))]
    if not snapshots:
        print(f"no markdown files found: {date_folder}", file=sys.stderr)
        return 3

    full_text = "\n\n".join(path.read_text(encoding="utf-8") for path in sorted(date_folder.glob("*.md")))
    cameras = _rank_signals(full_text, CAMERA_RULES)
    lenses = _rank_signals(full_text, LENS_RULES)
    placements = _rank_signals(full_text, PLACEMENT_RULES)
    payload = _build_payload(
        date_label=args.date or date_folder.name,
        date_folder=date_folder,
        snapshots=snapshots,
        cameras=cameras,
        lenses=lenses,
        placements=placements,
    )

    if args.no_write:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    runtime_output_dir = RUNTIME_DIR / _safe_slug(payload["date_label"])
    runtime_output_dir.mkdir(parents=True, exist_ok=True)

    output_path = OUTPUT_DIR / f"obsidian_date_folder_intake_{_safe_slug(payload['date_label'])}_candidate_v0.md"
    json_path = runtime_output_dir / "intake_payload.json"
    run_path = RUNS_DIR / f"run_{_next_run_number():03d}_obsidian_date_folder_{_safe_slug(payload['date_label'])}_space_intake.md"

    output_path.write_text(_render_markdown(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    run_path.write_text(_render_run_record(payload, output_path, json_path), encoding="utf-8")

    print(
        json.dumps(
            {
                "ok": True,
                "date_folder": str(date_folder),
                "output_path": str(output_path),
                "json_path": str(json_path),
                "run_path": str(run_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read one Obsidian date folder into a candidate VectorFL space-intake artifact."
    )
    parser.add_argument("--date", help="date folder name, for example 05-11")
    parser.add_argument("--folder", help="explicit date folder path")
    parser.add_argument("--obsidian-base", default=str(DEFAULT_OBSIDIAN_BASE))
    parser.add_argument("--no-write", action="store_true", help="print payload only")
    args = parser.parse_args(argv[1:])
    if not args.date and not args.folder:
        parser.error("provide --date or --folder")
    return args


def _resolve_date_folder(date_label: str | None, folder: str | None, obsidian_base: str) -> Path:
    if folder:
        return Path(folder).expanduser().resolve()
    return (Path(obsidian_base).expanduser() / str(date_label)).resolve()


def _snapshot_file(path: Path) -> SourceFileSnapshot:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    headings = [line.strip() for line in lines if re.match(r"^\s{0,3}#{1,6}\s+", line)]
    evidence_lines = _evidence_lines(lines)
    return SourceFileSnapshot(
        path=str(path),
        name=path.name,
        line_count=len(lines),
        char_count=len(text),
        headings=headings[:24],
        evidence_lines=evidence_lines[:16],
    )


def _evidence_lines(lines: Iterable[str]) -> list[str]:
    needles = (
        "핵심",
        "결론",
        "Watch",
        "다음",
        "공간",
        "파생",
        "회수",
        "샌드박스",
        "펌프",
        "하지 않는다",
        "만들지 않는다",
    )
    selected: list[str] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line or len(line) > 180:
            continue
        if line.startswith("#") or any(needle in line for needle in needles):
            selected.append(line)
    return selected


def _rank_signals(
    text: str,
    rules: dict[str, tuple[str, tuple[str, ...]]],
) -> list[SignalCandidate]:
    candidates: list[SignalCandidate] = []
    for signal_id, (name, terms) in rules.items():
        matched_terms = [term for term in terms if term.lower() in text.lower()]
        evidence = _find_evidence_for_terms(text, matched_terms)
        candidates.append(
            SignalCandidate(
                signal_id=signal_id,
                name=name,
                score=len(matched_terms),
                matched_terms=matched_terms,
                evidence=evidence,
            )
        )
    return sorted(candidates, key=lambda item: (-item.score, item.signal_id))


def _find_evidence_for_terms(text: str, terms: list[str]) -> list[str]:
    if not terms:
        return []
    evidence: list[str] = []
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in lines:
        if len(line) > 180:
            continue
        if any(term.lower() in line.lower() for term in terms):
            evidence.append(line)
        if len(evidence) >= 5:
            break
    return evidence


def _build_payload(
    date_label: str,
    date_folder: Path,
    snapshots: list[SourceFileSnapshot],
    cameras: list[SignalCandidate],
    lenses: list[SignalCandidate],
    placements: list[SignalCandidate],
) -> dict[str, object]:
    top_cameras = [item for item in cameras if item.score > 0][:5]
    top_lenses = [item for item in lenses if item.score > 0][:5]
    top_placements = [item for item in placements if item.score > 0]
    return {
        "pipeline": "obsidian_date_folder_space_intake_v0",
        "status": "CANDIDATE_REFERENCE_ONLY",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "date_label": date_label,
        "source_folder": str(date_folder),
        "source_status": [
            "RAW_CONVERSATION_MEMORY",
            "CANDIDATE_REFERENCE_ONLY",
            "NEEDS_USER_DECISION_BEFORE_PROMOTION",
        ],
        "source_files": [asdict(snapshot) for snapshot in snapshots],
        "camera_candidates": [asdict(item) for item in top_cameras],
        "lens_candidates": [asdict(item) for item in top_lenses],
        "placement_buckets": [asdict(item) for item in top_placements],
        "return_to_space_value": _return_to_space_value(top_cameras, top_lenses),
        "external_tool_application": _external_tool_application(top_placements),
        "sandbox_test_candidate": _sandbox_test_candidate(top_lenses, top_placements),
        "watch_items": _watch_items(top_lenses, top_placements),
        "next_safe_action": (
            "Keep this as a candidate intake artifact. If the user approves, run one small "
            "Sandbox Derivation Card using the Pump-Ready Sandbox Lens; do not promote the "
            "Obsidian notes directly."
        ),
        "boundary": [
            "no baseline promotion",
            "no official workflow creation",
            "no current-position update",
            "no package movement",
            "no external tool execution",
            "no broad Obsidian vault crawl",
        ],
    }


def _return_to_space_value(cameras: list[SignalCandidate], lenses: list[SignalCandidate]) -> list[str]:
    values = [
        "Use the date-folder material as a camera/lens source, not as direct execution instruction.",
        "Preserve the source folder as raw conversation memory while recovering candidate operating judgment.",
    ]
    if any(item.signal_id == "process_trace_camera" for item in cameras):
        values.append("Strengthen the process-trace reading: thin plan first, thick recovery after feedback.")
    if any(item.signal_id == "reservoir_sandbox_camera" for item in cameras):
        values.append("Treat original space as reservoir and sandbox outputs as derivative candidates that must return.")
    if any(item.signal_id == "pipeline_first_lens" for item in lenses):
        values.append("Read concepts after flow-change points appear; avoid freezing Line/Axis/Camera/Lens as ontology.")
    return values


def _external_tool_application(placements: list[SignalCandidate]) -> list[str]:
    if not any(item.signal_id == "external_tool_application" for item in placements):
        return ["No immediate external-tool packet. Keep as internal space-reading material."]
    return [
        "When routing to Codex/Gemini/CLI, require a Plan Basis that names source folder, camera, lens, boundary, and return path.",
        "External workers may observe or structure bounded evidence; they may not promote notes into rules or workflows.",
    ]


def _sandbox_test_candidate(
    lenses: list[SignalCandidate],
    placements: list[SignalCandidate],
) -> list[str]:
    if not any(item.signal_id == "sandbox_test_candidate" for item in placements):
        return ["No sandbox test required before user selects a specific derivative target."]
    lens_name = "Pump-Ready Sandbox Lens"
    pump_lens = next((item for item in lenses if item.signal_id == "pump_ready_sandbox_lens"), None)
    if pump_lens:
        lens_name = pump_lens.name
    elif lenses:
        lens_name = lenses[0].name
    return [
        f"Create one Sandbox Derivation Card using {lens_name}.",
        "Test whether one pulled asset can become a small derivative artifact without changing original-space authority.",
    ]


def _watch_items(lenses: list[SignalCandidate], placements: list[SignalCandidate]) -> list[str]:
    items = [
        "Do not treat saved Obsidian notes as active instructions.",
        "Do not turn repeated phrases into schema, registry, or baseline.",
    ]
    if any(item.signal_id == "watch_or_boundary" for item in placements) or any(
        item.signal_id == "no_direct_promotion_boundary_lens" for item in lenses
    ):
        items.append("Keep no-direct-promotion language visible when packaging follow-up work.")
    return items


def _render_markdown(payload: dict[str, object]) -> str:
    return "\n".join(
        [
            f"# Obsidian Date Folder Space Intake - {payload['date_label']} Candidate v0",
            "",
            "## 1. Status",
            "",
            "```text",
            "Status = CANDIDATE_REFERENCE_ONLY",
            "Source = RAW_CONVERSATION_MEMORY",
            "Not direct execution",
            "Not baseline / schema / workflow / registry",
            "No current-position update",
            "```",
            "",
            "## 2. Source Inventory",
            "",
            f"- Source folder: `{payload['source_folder']}`",
            f"- File count: {len(payload['source_files'])}",
            "",
            *_render_source_files(payload["source_files"]),
            "",
            "## 3. Camera Candidates",
            "",
            *_render_signal_list(payload["camera_candidates"]),
            "",
            "## 4. Lens Candidates",
            "",
            *_render_signal_list(payload["lens_candidates"]),
            "",
            "## 5. Placement Buckets",
            "",
            *_render_signal_list(payload["placement_buckets"]),
            "",
            "## 6. Return-to-Space Value",
            "",
            *_render_bullets(payload["return_to_space_value"]),
            "",
            "## 7. External Tool Application",
            "",
            *_render_bullets(payload["external_tool_application"]),
            "",
            "## 8. Sandbox Test Candidate",
            "",
            *_render_bullets(payload["sandbox_test_candidate"]),
            "",
            "## 9. Watch",
            "",
            *_render_bullets(payload["watch_items"]),
            "",
            "## 10. Next Safe Action",
            "",
            str(payload["next_safe_action"]),
            "",
            "## 11. Boundary Confirmation",
            "",
            *_render_bullets(payload["boundary"]),
            "",
            "`STATUS: OBSIDIAN_DATE_FOLDER_SPACE_INTAKE_CANDIDATE_PREPARED`",
            "",
        ]
    )


def _render_source_files(source_files: object) -> list[str]:
    lines: list[str] = []
    for raw_item in source_files if isinstance(source_files, list) else []:
        item = raw_item if isinstance(raw_item, dict) else {}
        lines.append(f"### {item.get('name', '')}")
        lines.append("")
        lines.append(f"- Lines: {item.get('line_count', 0)}")
        lines.append(f"- Characters: {item.get('char_count', 0)}")
        lines.append("- Headings:")
        headings = item.get("headings") or []
        if isinstance(headings, list) and headings:
            lines.extend(f"  - {heading}" for heading in headings[:12])
        else:
            lines.append("  - none")
        lines.append("")
    return lines


def _render_signal_list(items: object) -> list[str]:
    lines: list[str] = []
    if not isinstance(items, list) or not items:
        return ["- none"]
    for raw_item in items:
        item = raw_item if isinstance(raw_item, dict) else {}
        lines.append(f"### {item.get('name', '')}")
        lines.append("")
        lines.append(f"- Signal ID: `{item.get('signal_id', '')}`")
        lines.append(f"- Score: {item.get('score', 0)}")
        terms = item.get("matched_terms") or []
        if isinstance(terms, list) and terms:
            lines.append(f"- Matched terms: {', '.join(f'`{term}`' for term in terms)}")
        evidence = item.get("evidence") or []
        if isinstance(evidence, list) and evidence:
            lines.append("- Evidence:")
            lines.extend(f"  - {line}" for line in evidence[:4])
        lines.append("")
    return lines


def _render_bullets(items: object) -> list[str]:
    if not isinstance(items, list) or not items:
        return ["- none"]
    return [f"- {item}" for item in items]


def _render_run_record(payload: dict[str, object], output_path: Path, json_path: Path) -> str:
    return "\n".join(
        [
            f"# Run - Obsidian Date Folder Space Intake {payload['date_label']}",
            "",
            "## Purpose",
            "",
            "Read one Obsidian date folder as raw conversation memory and recover camera/lens/placement candidates.",
            "",
            "## Inputs",
            "",
            f"- Source folder: `{payload['source_folder']}`",
            f"- Pipeline: `{payload['pipeline']}`",
            "",
            "## Outputs",
            "",
            f"- Markdown artifact: `{output_path.relative_to(ROOT)}`",
            f"- JSON payload: `{json_path.relative_to(ROOT)}`",
            "",
            "## Boundary",
            "",
            *_render_bullets(payload["boundary"]),
            "",
            "## Result",
            "",
            "The date folder was not promoted or executed directly. It was converted into a candidate space-intake artifact.",
            "",
            "`STATUS: RUN_RECORD_PREPARED`",
            "",
        ]
    )


def _next_run_number() -> int:
    existing: list[int] = []
    if RUNS_DIR.exists():
        for path in RUNS_DIR.glob("run_*.md"):
            match = re.match(r"run_(\d+)_", path.name)
            if match:
                existing.append(int(match.group(1)))
    return max(existing, default=0) + 1


def _safe_slug(value: object) -> str:
    slug = re.sub(r"[^A-Za-z0-9_-]+", "_", str(value).strip())
    return slug.strip("_") or "unknown"


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
