from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parent.parent
RETURN_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_codex_return_latest_v0.json"
REVIEW_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_gemini_review_latest_v0.json"
ACTUAL_EXPORT_SLOT_REF = "runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json"
EXTERNAL_RECORD_ANCHOR_REF = "runtime/contracts/vectorfl_paper_weekend_live_export_shaped_host_record_v2.json"
GEMINI_TIMEOUT_SECONDS = 45
GEMINI_REVIEW_TOP_FILES = [
    "runtime/manifests/vectorfl_paper_codex_return_latest_v0.json",
    "runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json",
    ACTUAL_EXPORT_SLOT_REF,
    EXTERNAL_RECORD_ANCHOR_REF,
]


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_codex_return() -> Dict[str, Any]:
    if not RETURN_PATH.exists():
        raise FileNotFoundError(f"latest codex return not found: {RETURN_PATH}")
    payload = json.loads(RETURN_PATH.read_text(encoding="utf-8"))
    required = [
        "summary",
        "changed_files",
        "blockers",
        "next_recommendation",
        "needs_supervisor_decision",
    ]
    missing = [key for key in required if key not in payload]
    if missing:
        raise ValueError(f"latest codex return malformed; missing keys: {', '.join(missing)}")
    return payload


def _build_prompt(codex_return: Dict[str, Any]) -> str:
    return f"""You are Gemini acting only as a cross-check reviewer for a Codex result inside VectorFL Paper.

Do not propose new implementation work. Do not expand scope. Review the Codex return only.
Return JSON only with these exact keys:
- review_summary
- agreement_assessment
- detected_risks
- missing_points
- recommendation
- suggested_supervisor_action

Allowed values for agreement_assessment:
- mostly_agree
- partial_concern
- major_concern

Allowed values for suggested_supervisor_action:
- continue
- hold
- reopen
- request_codex_revision

Source Codex return artifact:
{RETURN_PATH.relative_to(REPO_ROOT)}

Codex summary:
{codex_return["summary"]}

Codex changed_files:
{json.dumps(codex_return["changed_files"], ensure_ascii=False, indent=2)}

Codex blockers:
{json.dumps(codex_return["blockers"], ensure_ascii=False, indent=2)}

Codex next_recommendation:
{codex_return["next_recommendation"]}

needs_supervisor_decision:
{json.dumps(codex_return["needs_supervisor_decision"], ensure_ascii=False)}

Gemini review top files:
{json.dumps(GEMINI_REVIEW_TOP_FILES, ensure_ascii=False, indent=2)}

External validation anchor:
{json.dumps({"slot": ACTUAL_EXPORT_SLOT_REF, "record": EXTERNAL_RECORD_ANCHOR_REF, "scope": "single export-shaped anchor; do not treat as full gate closure if Codex still reports local fixture limits"}, ensure_ascii=False, indent=2)}

Review questions:
1. Is the Codex summary faithful to the current return?
2. Are there omitted risks or missing constraints?
3. Is the blocker interpretation sound?
4. Is the next recommendation proportionate?
5. Should the supervisor continue, hold, reopen, or request Codex revision?

Return compact, supervisor-readable JSON only.
"""


def _extract_json(text: str) -> Dict[str, Any]:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("gemini output did not contain a JSON object")
    return json.loads(text[start : end + 1])


def _to_string_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def _write_review(payload: Dict[str, Any]) -> None:
    REVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _failed_review(message: str, exit_code: int, raw_command: List[str]) -> Dict[str, Any]:
    return {
        "schema_version": "vectorfl_paper_gemini_review_latest_v0",
        "source_return_artifact": str(RETURN_PATH.relative_to(REPO_ROOT)),
        "worker": "gemini",
        "review_status": "failed",
        "review_summary": "Gemini cross-check did not complete a usable review result.",
        "agreement_assessment": "partial_concern",
        "detected_risks": [message],
        "missing_points": [],
        "recommendation": "Check Gemini CLI environment and rerun the same latest Codex return through the cross-check bridge.",
        "suggested_supervisor_action": "hold",
        "gemini_review_top_files": GEMINI_REVIEW_TOP_FILES,
        "external_record_anchor": {
            "slot": ACTUAL_EXPORT_SLOT_REF,
            "record": EXTERNAL_RECORD_ANCHOR_REF,
        },
        "reviewed_at": _now_iso(),
        "raw_command": raw_command,
        "execution_mode": "gemini_prompt_plan",
        "exit_code": exit_code,
    }


def main() -> None:
    print(f"[vectorfl-paper-gemini-bridge] reading codex return: {RETURN_PATH.relative_to(REPO_ROOT)}")
    try:
        codex_return = _load_codex_return()
    except Exception as error:
        print(f"[vectorfl-paper-gemini-bridge] error: {error}", file=sys.stderr)
        raise

    prompt = _build_prompt(codex_return)
    command = [
        "gemini",
        "--prompt",
        prompt,
        "--output-format",
        "text",
    ]
    print(f"[vectorfl-paper-gemini-bridge] running gemini command: {' '.join(command[:4])} ...")

    try:
        completed = subprocess.run(
            command,
            text=True,
            capture_output=True,
            cwd=str(REPO_ROOT),
            timeout=GEMINI_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        failure = _failed_review(
            f"gemini prompt timed out after {GEMINI_TIMEOUT_SECONDS} seconds",
            124,
            command,
        )
        _write_review(failure)
        print(f"[vectorfl-paper-gemini-bridge] wrote failed review: {REVIEW_PATH.relative_to(REPO_ROOT)}")
        raise SystemExit(124)

    if completed.stdout.strip():
        print(completed.stdout.strip())
    if completed.stderr.strip():
        print(completed.stderr.strip(), file=sys.stderr)

    if completed.returncode != 0:
        failure = _failed_review(
            f"gemini exited with code {completed.returncode}",
            completed.returncode,
            command,
        )
        _write_review(failure)
        print(f"[vectorfl-paper-gemini-bridge] wrote failed review: {REVIEW_PATH.relative_to(REPO_ROOT)}")
        raise SystemExit(completed.returncode)

    try:
        parsed = _extract_json(completed.stdout)
    except Exception as error:
        failure = _failed_review(
            f"gemini output parse failed: {error}",
            1,
            command,
        )
        _write_review(failure)
        print(f"[vectorfl-paper-gemini-bridge] wrote failed review: {REVIEW_PATH.relative_to(REPO_ROOT)}")
        raise

    latest_review = {
        "schema_version": "vectorfl_paper_gemini_review_latest_v0",
        "source_return_artifact": str(RETURN_PATH.relative_to(REPO_ROOT)),
        "worker": "gemini",
        "review_status": "completed",
        "review_summary": parsed["review_summary"],
        "agreement_assessment": parsed["agreement_assessment"],
        "detected_risks": _to_string_list(parsed.get("detected_risks", [])),
        "missing_points": _to_string_list(parsed.get("missing_points", [])),
        "recommendation": parsed["recommendation"],
        "suggested_supervisor_action": parsed["suggested_supervisor_action"],
        "gemini_review_top_files": GEMINI_REVIEW_TOP_FILES,
        "external_record_anchor": {
            "slot": ACTUAL_EXPORT_SLOT_REF,
            "record": EXTERNAL_RECORD_ANCHOR_REF,
        },
        "reviewed_at": _now_iso(),
        "raw_command": command,
        "execution_mode": "gemini_prompt_plan",
        "exit_code": completed.returncode,
    }
    _write_review(latest_review)
    print(f"[vectorfl-paper-gemini-bridge] wrote latest review: {REVIEW_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
