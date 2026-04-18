#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

OUTPUT_DIR = REPO_ROOT / "app" / "work" / "archive_review" / "external_case_support" / "external_case_folder_sweep" / "generated"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare or run a bounded external-case folder sweep loop."
    )
    parser.add_argument("runtime_root", help="Runtime root used by intake commands.")
    parser.add_argument(
        "--input-root",
        default="inputs/external_cases",
        help="Folder to sweep. Defaults to inputs/external_cases.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Optional max file count. 0 means all matching files.",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Optional filename stem filter. Can be passed multiple times.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Run the bounded intake/probe commands. Default is plan-only.",
    )
    return parser.parse_args()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _relative(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        rel = path.resolve()
    return str(rel).replace("\\", "/")


def _slug(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def _iter_external_files(input_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(input_root.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        if path.name in {"README.md", "folder_status.md"}:
            continue
        files.append(path)
    return files


def _detect_material_profile(path: Path) -> str:
    if path.suffix.lower() == ".md":
        return "structured_external_markdown"
    return "raw_external_transcript"


def _build_plan_row(path: Path) -> dict[str, Any]:
    stem = _slug(path.stem)
    material_profile = _detect_material_profile(path)
    supports_structured_intake = path.suffix.lower() == ".md"
    return {
        "input_path": _relative(path),
        "stem": stem,
        "material_profile": material_profile,
        "supports_structured_intake": supports_structured_intake,
        "planned_steps": [
            "external_input_gate",
            "structured_intake" if supports_structured_intake else "skip_structured_intake",
            "raw_intake_probe",
            "first_pass_report_stub",
            "watchpoint_report_stub",
            "strong_line_contact_stub",
        ],
        "planned_commands": [
            f"python3 scripts/run_external_input_gate.py {_relative(path)}",
            (
                f"python3 scripts/process_structured_doc_with_routing.py --doc {_relative(path)}"
                if supports_structured_intake
                else None
            ),
            f"python3 scripts/run_external_case_raw_intake_probe.py {_relative(path)}",
        ],
        "expected_reports": [
            f"docs/reports/{stem}_transcript_aware_first_pass_v1.md",
            f"docs/reports/{stem}_latent_line_watchpoints_v1.md",
            f"docs/reports/{stem}_strong_line_contact_map_v1.md",
        ],
        "status": "planned",
    }


def _run_command(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "command": " ".join(cmd),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def main() -> int:
    args = parse_args()
    runtime_root = Path(args.runtime_root).resolve()
    input_root = Path(args.input_root)
    if not input_root.is_absolute():
        input_root = (REPO_ROOT / input_root).resolve()
    if not input_root.exists():
        raise FileNotFoundError(f"input root not found: {input_root}")

    include = {_slug(item) for item in args.include}
    files = _iter_external_files(input_root)
    if include:
        files = [path for path in files if _slug(path.stem) in include]
    if args.limit > 0:
        files = files[: args.limit]

    rows = [_build_plan_row(path) for path in files]

    if args.execute:
        for row in rows:
            executions: list[dict[str, Any]] = []
            input_path = REPO_ROOT / row["input_path"]
            executions.append(
                _run_command(
                    [
                        sys.executable,
                        "scripts/run_external_input_gate.py",
                        _relative(input_path),
                    ]
                )
            )
            if row["supports_structured_intake"]:
                executions.append(
                    _run_command(
                        [
                            sys.executable,
                            "scripts/process_structured_doc_with_routing.py",
                            "--doc",
                            _relative(input_path),
                        ]
                    )
                )
            executions.append(
                _run_command(
                    [
                        sys.executable,
                        "scripts/run_external_case_raw_intake_probe.py",
                        _relative(input_path),
                    ]
                )
            )
            row["status"] = (
                "executed"
                if all(execution["returncode"] == 0 for execution in executions)
                else "execution_failed"
            )
            row["executions"] = executions

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"external_case_folder_sweep_loop_{_stamp()}.json"
    payload = {
        "created_at": _now_iso(),
        "mode": "execute" if args.execute else "plan_only",
        "runtime_root": _relative(runtime_root),
        "input_root": _relative(input_root),
        "file_count": len(rows),
        "rows": rows,
    }
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "output_path": _relative(output_path),
                "mode": payload["mode"],
                "file_count": len(rows),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
