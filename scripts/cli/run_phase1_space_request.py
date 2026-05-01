#!/usr/bin/env python3
"""Thin invocation wrapper for the Phase 1 stable four-artifact spine."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from lower_upper_admission_classifier import classify


def _read_request(args: argparse.Namespace) -> str:
    if args.input_file:
        return args.input_file.read_text(encoding="utf-8").strip()
    if args.request:
        return args.request
    if args.admission_only and args.artifact_path:
        return f"Admission-only check for {args.artifact_path}"
    raise SystemExit("Provide a request string, --input-file, or --admission-only with --artifact-path.")


def _build_wrapped_request(request: str, args: argparse.Namespace, admission: dict | None) -> str:
    parts = [request.strip()]
    if args.mode:
        parts.append(f"Requested task mode: {args.mode}.")
    if admission:
        parts.append(
            "Lower artifact admission context: "
            f"{admission['artifact_path']} -> {admission['upper_admission']} "
            f"({'; '.join(admission.get('reasons', [])[:3])})."
        )
        parts.append(
            "Bridge guardrail: do not treat admission classification as readiness promotion; "
            "preserve evidence_only and hold discipline."
        )
    if args.evidence_only:
        parts.append("Operator constraint: keep lower artifact as evidence_only unless checklist support explicitly says otherwise.")
    if args.hold_on_risk:
        parts.append("Operator constraint: hold on baseline, canonical path, final naming, or admission inflation risk.")
    return "\n".join(part for part in parts if part)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("request", nargs="?")
    parser.add_argument("--input-file", type=Path)
    parser.add_argument("--mode", choices=["exploration", "extraction", "comparison", "merge", "verification", "reflection_support"])
    parser.add_argument("--artifact-path")
    parser.add_argument("--readiness-hint", choices=["residue-only", "evidence-ready", "engine-ingest-ready", "packet-candidate"], default="")
    parser.add_argument("--admission-only", action="store_true")
    parser.add_argument("--evidence-only", action="store_true")
    parser.add_argument("--hold-on-risk", action="store_true")
    parser.add_argument("--stem")
    parser.add_argument("--force-merge-mode", choices=["merge", "diff", "hold"], default="")
    args = parser.parse_args()

    admission = None
    if args.artifact_path:
        admission = classify(args.artifact_path, readiness_hint=args.readiness_hint)

    request = _read_request(args)
    if args.admission_only:
        print(json.dumps({"admission": admission}, ensure_ascii=False, indent=2))
        return

    wrapped_request = _build_wrapped_request(request, args, admission)
    cmd = [sys.executable, "scripts/cli/run_phase1_space_query.py", wrapped_request]
    if args.mode:
        cmd.extend(["--mode", args.mode])
    if args.stem:
        cmd.extend(["--stem", args.stem])
    if args.force_merge_mode:
        cmd.extend(["--force-merge-mode", args.force_merge_mode])
    elif args.hold_on_risk and admission and admission["upper_admission"] == "reject_for_upper":
        cmd.extend(["--force-merge-mode", "hold"])

    completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
    summary = json.loads(completed.stdout)
    summary["wrapper"] = {
        "wrapped_request": wrapped_request,
        "classifier_used": admission is not None,
        "admission": admission,
        "core_entrypoint": "scripts/cli/run_phase1_space_query.py",
        "four_artifact_spine_preserved": True,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
