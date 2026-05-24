#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPO_SEED = ROOT / "app/work/reservoir-pipeline-repo-seed"
OUTPUT_DIR = ROOT / "app/work/space-skill-sandbox/outputs"
RUNS_DIR = ROOT / "app/work/space-skill-sandbox/runs"
RUNTIME_DIR = ROOT / "runtime/reservoir_pipeline_repo_seed_audit"

REQUIRED_DIRS = (
    "docs",
    "templates",
    "indexes",
    "records",
    "tests",
    "bundles",
    "derivatives",
    "examples",
)

REQUIRED_FILES = (
    "README.md",
    "docs/operating_model.md",
    "docs/asset_families.md",
    "docs/attachment_ports.md",
    "docs/repo_as_space_principle.md",
    "docs/script_maturation_ladder.md",
    "docs/scriptable_setup_map.md",
    "templates/reservoir_access_gate.md",
    "templates/pipeline_connector.md",
    "templates/sandbox_derivation_card.md",
    "templates/return_record.md",
    "templates/process_trace_record.md",
    "templates/script_candidate_card.md",
    "templates/source_reference_map.md",
    "indexes/source_reference_map.md",
    "records/decision_log.md",
    "records/output_manifest.md",
)

TRACE_PACKET_SECTIONS = (
    "Purpose",
    "Source Refs",
    "Thin Plan",
    "What Was Read",
    "What Was Not Read",
    "Output Created",
    "Feedback Or Mismatch",
    "Recovered Judgment",
    "Watch",
    "Next Condition",
    "Return Placement",
)

BOUNDARY_TERMS = (
    "Not automation",
    "Not schema",
)


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    detail: str


@dataclass(frozen=True)
class TracePacketAudit:
    path: str
    status: str
    missing_sections: list[str]
    boundary_terms_present: list[str]


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    repo_seed = Path(args.repo_seed).expanduser().resolve()
    if not repo_seed.exists():
        print(f"repo seed not found: {repo_seed}", file=sys.stderr)
        return 2

    payload = _build_payload(repo_seed=repo_seed, tag=args.tag)
    if args.no_write:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0 if payload["overall_status"] != "BLOCKED" else 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)

    date_slug = datetime.now().strftime("%Y%m%d")
    tag_slug = _safe_slug(args.tag)
    output_path = OUTPUT_DIR / f"reservoir_pipeline_repo_seed_scriptable_setup_audit_{tag_slug}_{date_slug}_candidate_v0.md"
    json_path = RUNTIME_DIR / f"{tag_slug}_{date_slug}_audit_payload.json"
    run_path = RUNS_DIR / f"run_{_next_run_number():03d}_reservoir_pipeline_repo_seed_scriptable_setup_audit.md"

    output_path.write_text(_render_markdown(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    run_path.write_text(_render_run_record(payload, output_path, json_path), encoding="utf-8")

    print(
        json.dumps(
            {
                "ok": payload["overall_status"] != "BLOCKED",
                "overall_status": payload["overall_status"],
                "output_path": str(output_path),
                "json_path": str(json_path),
                "run_path": str(run_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if payload["overall_status"] != "BLOCKED" else 1


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit the reservoir-pipeline repo seed for scriptable setup and trace-packet readiness."
    )
    parser.add_argument("--repo-seed", default=str(DEFAULT_REPO_SEED))
    parser.add_argument("--tag", default="current")
    parser.add_argument("--no-write", action="store_true")
    return parser.parse_args(argv[1:])


def _build_payload(repo_seed: Path, tag: str) -> dict[str, object]:
    dir_checks = _check_dirs(repo_seed)
    file_checks = _check_files(repo_seed)
    packet_audits = _audit_trace_packets(repo_seed)
    manifest_coverage = _check_manifest_mentions(repo_seed)
    scriptable_candidates = _scriptable_candidates(packet_audits)
    human_boundaries = _human_boundaries()

    statuses = [check.status for check in dir_checks + file_checks + manifest_coverage]
    packet_statuses = [packet.status for packet in packet_audits]
    overall_status = _overall_status(statuses + packet_statuses)

    return {
        "tag": tag,
        "repo_seed": str(repo_seed),
        "created_at_local": datetime.now().isoformat(timespec="seconds"),
        "overall_status": overall_status,
        "dir_checks": [asdict(check) for check in dir_checks],
        "file_checks": [asdict(check) for check in file_checks],
        "trace_packet_audits": [asdict(packet) for packet in packet_audits],
        "manifest_coverage": [asdict(check) for check in manifest_coverage],
        "scriptable_candidates": scriptable_candidates,
        "human_boundaries": human_boundaries,
        "next_condition": _next_condition(overall_status),
    }


def _check_dirs(repo_seed: Path) -> list[CheckResult]:
    checks: list[CheckResult] = []
    for relative in REQUIRED_DIRS:
        path = repo_seed / relative
        checks.append(
            CheckResult(
                name=f"dir:{relative}",
                status="OK" if path.is_dir() else "MISSING",
                detail=str(path),
            )
        )
    return checks


def _check_files(repo_seed: Path) -> list[CheckResult]:
    checks: list[CheckResult] = []
    for relative in REQUIRED_FILES:
        path = repo_seed / relative
        checks.append(
            CheckResult(
                name=f"file:{relative}",
                status="OK" if path.is_file() else "MISSING",
                detail=str(path),
            )
        )
    return checks


def _audit_trace_packets(repo_seed: Path) -> list[TracePacketAudit]:
    records_dir = repo_seed / "records"
    audits: list[TracePacketAudit] = []
    for path in sorted(records_dir.glob("run_*_minimum_trace_packet.md")):
        text = path.read_text(encoding="utf-8")
        missing = [
            section
            for section in TRACE_PACKET_SECTIONS
            if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, flags=re.MULTILINE)
        ]
        boundary_present = [term for term in BOUNDARY_TERMS if term in text]
        status = "OK"
        if missing:
            status = "NEEDS_TRACE_FIELD"
        if len(boundary_present) < len(BOUNDARY_TERMS):
            status = "NEEDS_BOUNDARY_LABEL" if status == "OK" else status
        audits.append(
            TracePacketAudit(
                path=str(path.relative_to(repo_seed)),
                status=status,
                missing_sections=missing,
                boundary_terms_present=boundary_present,
            )
        )
    if not audits:
        audits.append(
            TracePacketAudit(
                path="records/run_*_minimum_trace_packet.md",
                status="MISSING",
                missing_sections=list(TRACE_PACKET_SECTIONS),
                boundary_terms_present=[],
            )
        )
    return audits


def _check_manifest_mentions(repo_seed: Path) -> list[CheckResult]:
    manifest = repo_seed / "records/output_manifest.md"
    if not manifest.is_file():
        return [
            CheckResult(
                name="manifest:records/output_manifest.md",
                status="MISSING",
                detail=str(manifest),
            )
        ]
    text = manifest.read_text(encoding="utf-8")
    checks: list[CheckResult] = []
    for packet in sorted((repo_seed / "records").glob("run_*_minimum_trace_packet.md")):
        relative = str(packet.relative_to(repo_seed))
        checks.append(
            CheckResult(
                name=f"manifest:{relative}",
                status="OK" if relative in text else "WATCH",
                detail="mentioned in output manifest" if relative in text else "not mentioned in output manifest",
            )
        )
    return checks


def _scriptable_candidates(packet_audits: list[TracePacketAudit]) -> list[dict[str, str]]:
    return [
        {
            "candidate": "repo_seed_scaffold_check",
            "can_script": "check/create expected directories and required files from templates",
            "must_not_script": "decide that the repo seed is official",
        },
        {
            "candidate": "script_maturation_gate",
            "can_script": "check that script_maturation_ladder and script_candidate_card exist before any new script expansion",
            "must_not_script": "promote a friction point into a script without recorded examples",
        },
        {
            "candidate": "minimum_trace_packet_audit",
            "can_script": "detect missing packet sections and boundary labels",
            "must_not_script": "decide recovered judgment or promotion value",
        },
        {
            "candidate": "run_record_and_output_stub",
            "can_script": "draft output and run-record filenames with next run number",
            "must_not_script": "invent source refs or user intent",
        },
        {
            "candidate": "manifest_sync_candidate",
            "can_script": "list files absent from output_manifest as candidate additions",
            "must_not_script": "turn manifest into registry or approval list",
        },
        {
            "candidate": "status_boundary_lint",
            "can_script": "flag missing Not automation / Not schema labels",
            "must_not_script": "replace human boundary judgment",
        },
        {
            "candidate": "packet_pressure_router",
            "can_script": _packet_pressure_summary(packet_audits),
            "must_not_script": "choose final reuse/HOLD/WATCH placement without review",
        },
    ]


def _packet_pressure_summary(packet_audits: list[TracePacketAudit]) -> str:
    needs = [packet.path for packet in packet_audits if packet.status != "OK"]
    if not needs:
        return "suggest next pressure after all current packets pass structural checks"
    return "surface packet files needing trace-field or boundary-label repair"


def _human_boundaries() -> list[str]:
    return [
        "source material selection",
        "recovered_judgment wording",
        "reuse / HOLD / WATCH placement",
        "promotion to baseline or official workflow",
        "claim that a worker understands the user",
        "decision to automate beyond linting and scaffolding",
    ]


def _overall_status(statuses: list[str]) -> str:
    if any(status == "MISSING" for status in statuses):
        return "BLOCKED"
    if any(status.startswith("NEEDS") or status == "WATCH" for status in statuses):
        return "READY_WITH_WATCH"
    return "READY_FOR_SCRIPTABLE_SETUP_SUPPORT"


def _next_condition(overall_status: str) -> str:
    if overall_status == "BLOCKED":
        return "repair missing scaffold files before adding more automation"
    if overall_status == "READY_WITH_WATCH":
        return "review watch items, then use script output as setup support only"
    return "use this audit only as setup support after the script maturation ladder remains present"


def _render_markdown(payload: dict[str, object]) -> str:
    lines: list[str] = [
        "# Reservoir Pipeline Repo Seed Scriptable Setup Audit",
        "",
        "## Status",
        "",
        "```text",
        f"Status = {payload['overall_status']}",
        "Authority = candidate setup support only",
        "Not baseline",
        "Not official workflow",
        "Not automation of judgment",
        "Not schema",
        "```",
        "",
        "## Repo Seed",
        "",
        "```text",
        str(payload["repo_seed"]),
        "```",
        "",
        "## What This Script Can Reduce",
        "",
        "```text",
        "manual CLI reading for scaffold presence",
        "manual CLI reading for trace packet section completeness",
        "manual CLI reading for boundary label presence",
        "manual next-run/output filename bookkeeping",
        "manual manifest coverage checks",
        "manual check that script growth is gated by a maturation ladder",
        "```",
        "",
        "## What Must Stay Human",
        "",
        "```text",
    ]
    lines.extend(str(item) for item in payload["human_boundaries"])
    lines.extend(["```", "", "## Directory Checks", ""])
    lines.extend(_render_check_table(payload["dir_checks"]))
    lines.extend(["", "## Required File Checks", ""])
    lines.extend(_render_check_table(payload["file_checks"]))
    lines.extend(["", "## Trace Packet Audits", ""])
    lines.extend(_render_packet_table(payload["trace_packet_audits"]))
    lines.extend(["", "## Manifest Coverage", ""])
    lines.extend(_render_check_table(payload["manifest_coverage"]))
    lines.extend(["", "## Scriptable Candidates", ""])
    lines.append("| Candidate | Can script | Must not script |")
    lines.append("|---|---|---|")
    for item in payload["scriptable_candidates"]:
        lines.append(f"| `{item['candidate']}` | {item['can_script']} | {item['must_not_script']} |")
    lines.extend(
        [
            "",
            "## Next Condition",
            "",
            "```text",
            str(payload["next_condition"]),
            "```",
            "",
            "`STATUS: RESERVOIR_PIPELINE_REPO_SEED_SCRIPTABLE_SETUP_AUDIT_PREPARED`",
            "",
        ]
    )
    return "\n".join(lines)


def _render_check_table(items: object) -> list[str]:
    rows = ["| Check | Status | Detail |", "|---|---|---|"]
    for item in items:
        rows.append(f"| `{item['name']}` | `{item['status']}` | {item['detail']} |")
    return rows


def _render_packet_table(items: object) -> list[str]:
    rows = ["| Packet | Status | Missing sections | Boundary labels |", "|---|---|---|---|"]
    for item in items:
        missing = ", ".join(item["missing_sections"]) if item["missing_sections"] else "none"
        boundaries = ", ".join(item["boundary_terms_present"]) if item["boundary_terms_present"] else "none"
        rows.append(f"| `{item['path']}` | `{item['status']}` | {missing} | {boundaries} |")
    return rows


def _render_run_record(payload: dict[str, object], output_path: Path, json_path: Path) -> str:
    return "\n".join(
        [
            "# Run - Reservoir Pipeline Repo Seed Scriptable Setup Audit",
            "",
            "## Purpose",
            "",
            "Audit which repo-seed setup checks can be handled by a script without automating judgment.",
            "",
            "## Inputs",
            "",
            "```text",
            str(payload["repo_seed"]),
            "```",
            "",
            "## Outputs",
            "",
            "```text",
            str(output_path),
            str(json_path),
            "```",
            "",
            "## Result",
            "",
            "```text",
            str(payload["overall_status"]),
            "```",
            "",
            "## Boundary",
            "",
            "```text",
            "no baseline promotion",
            "no official workflow creation",
            "no schema",
            "no automation of judgment",
            "```",
            "",
            "`STATUS: RUN_RECORD_PREPARED`",
            "",
        ]
    )


def _next_run_number() -> int:
    max_seen = 0
    for path in RUNS_DIR.glob("run_*"):
        match = re.match(r"run_(\d+)", path.name)
        if match:
            max_seen = max(max_seen, int(match.group(1)))
    return max_seen + 1


def _safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())
    return slug.strip("_") or "current"


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
